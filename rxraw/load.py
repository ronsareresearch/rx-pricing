"""Load MED-File v2 files into rxraw.raw_* tables. No dependency on etl."""

import logging
from datetime import datetime
from pathlib import Path
from uuid import UUID

from rxraw.config import get_database_url, get_insert_batch_size
from rxraw.parse_utils import is_empty_or_delimiter_only
from rxraw.schema import (
    DICT_SOURCE_FILE,
    RAW_POS_COUNT,
    RAW_SOURCE_FILES,
    SCHEMA_NAME,
    raw_table_name,
)

logger = logging.getLogger(__name__)


def _file_date_to_date(file_date: str | None) -> str | None:
    """YYYYMMDD -> YYYY-MM-DD or None."""
    if not file_date or len(file_date) != 8:
        return None
    try:
        dt = datetime.strptime(file_date.strip(), "%Y%m%d")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        return None


def _pad_parts(parts: list[str], n: int) -> list[str | None]:
    """Pad or trim to n elements; empty string -> None for DB."""
    return [
        (parts[i].strip() or None) if i < len(parts) and parts[i].strip() else None
        for i in range(n)
    ]


def load_one_file(
    run_dir: Path,
    file_id: UUID,
    file_date: str,
    source_file: str,
    volume_number: str = "",
    supplement_number: str = "",
    *,
    _conn=None,
) -> int:
    """Load one MED-File v2 file into rxraw.raw_<file>. Returns row count or 0."""
    path = run_dir / source_file
    if not path.is_file():
        logger.debug("%s not found in %s", source_file, run_dir)
        return 0

    date_val = _file_date_to_date(file_date)
    if not date_val:
        logger.error("Invalid file_date: %s", file_date)
        return 0

    url = None if _conn else get_database_url()
    if not _conn and not url:
        return 0

    rows: list[tuple] = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.rstrip()
            if is_empty_or_delimiter_only(line):
                continue
            parts = line.split("|")
            padded = _pad_parts(parts, RAW_POS_COUNT)
            rows.append((
                str(file_id),
                date_val,
                source_file,
                line_num,
                volume_number,
                supplement_number,
                *padded,
            ))

    if not rows:
        logger.info("%s: no data rows", path)
        return 0

    table = raw_table_name(source_file)
    _insert(table, rows, url, _conn=_conn)
    logger.info("rxraw.%s: inserted %d rows (source_file=%s file_date=%s)", table, len(rows), source_file, date_val)
    return len(rows)


def load_run(
    run_dir: Path,
    file_id: UUID,
    file_date: str,
    volume_number: str = "",
    supplement_number: str = "",
    *,
    _conn=None,
) -> dict[str, int]:
    """Load all MED-File v2 files present in run_dir into rxraw.raw_*. Returns source_file -> row_count.
    Uses one connection when _conn is provided. Skips files already loaded for this (file_date, volume) to support resume.
    """
    url = None if _conn else get_database_url()
    if not _conn and not url:
        return {}
    conn = _conn
    own_conn = False
    if conn is None:
        import psycopg2
        conn = psycopg2.connect(url)
        own_conn = True
    try:
        counts: dict[str, int] = {}
        for source_file in RAW_SOURCE_FILES:
            if file_already_loaded(
                file_date, volume_number, source_file, url, _conn=conn
            ):
                logger.debug("skip already loaded: %s (file_date=%s volume=%s)", source_file, file_date, volume_number)
                continue
            n = load_one_file(
                run_dir, file_id, file_date, source_file, volume_number, supplement_number, _conn=conn
            )
            if n > 0:
                counts[source_file] = n
        return counts
    finally:
        if own_conn:
            conn.close()


def _table_row_count(table: str, url: str) -> int:
    """Return row count for rxraw.<table>. Used to decide if MF2DICT should be loaded."""
    import psycopg2
    conn = psycopg2.connect(url)
    try:
        with conn.cursor() as cur:
            cur.execute(f"SELECT COUNT(*) FROM {SCHEMA_NAME}.{table}")
            return cur.fetchone()[0]
    finally:
        conn.close()


def run_already_loaded(
    file_date: str, volume_number: str, url: str | None = None, *, _conn=None
) -> bool:
    """True if this (file_date, volume_number) was already loaded; prevents duplicate run loads."""
    date_val = _file_date_to_date(file_date)
    if not date_val:
        return False
    if _conn is not None:
        with _conn.cursor() as cur:
            cur.execute(
                "SELECT 1 FROM rxraw.loaded_runs WHERE file_date = %s AND volume_number = %s LIMIT 1",
                (date_val, (volume_number or "").strip()),
            )
            return cur.fetchone() is not None
    u = url or get_database_url()
    if not u:
        return False
    import psycopg2
    conn = psycopg2.connect(u)
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT 1 FROM rxraw.loaded_runs WHERE file_date = %s AND volume_number = %s LIMIT 1",
                (date_val, (volume_number or "").strip()),
            )
            return cur.fetchone() is not None
    finally:
        conn.close()


def get_existing_file_id_for_run(
    file_date: str, volume_number: str, url: str | None = None, *, _conn=None
) -> UUID | None:
    """If this run was partially loaded (e.g. after a crash), return the existing file_id so we can resume without duplicating rows."""
    date_val = _file_date_to_date(file_date)
    if not date_val:
        return None
    vol = (volume_number or "").strip()
    table = raw_table_name(RAW_SOURCE_FILES[0])
    sql = f"SELECT file_id FROM {SCHEMA_NAME}.{table} WHERE file_date = %s AND volume_number = %s LIMIT 1"
    params = (date_val, vol)
    if _conn is not None:
        with _conn.cursor() as cur:
            cur.execute(sql, params)
            row = cur.fetchone()
            return UUID(row[0]) if row else None
    u = url or get_database_url()
    if not u:
        return None
    import psycopg2
    conn = psycopg2.connect(u)
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            row = cur.fetchone()
            return UUID(row[0]) if row else None
    finally:
        conn.close()


def file_already_loaded(
    file_date: str,
    volume_number: str,
    source_file: str,
    url: str | None = None,
    *,
    _conn=None,
) -> bool:
    """True if this (file_date, volume_number, source_file) already has rows in the raw table; skip to avoid duplicate file load."""
    date_val = _file_date_to_date(file_date)
    if not date_val:
        return False
    table = raw_table_name(source_file)
    sql = f"SELECT 1 FROM {SCHEMA_NAME}.{table} WHERE file_date = %s AND volume_number = %s AND source_file = %s LIMIT 1"
    params = (date_val, (volume_number or "").strip(), source_file)
    if _conn is not None:
        with _conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone() is not None
    u = url or get_database_url()
    if not u:
        return False
    import psycopg2
    conn = psycopg2.connect(u)
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone() is not None
    finally:
        conn.close()


def record_loaded_run(
    file_id: UUID,
    file_date: str,
    volume_number: str,
    supplement_number: str = "",
    url: str | None = None,
    *,
    _conn=None,
) -> None:
    """Record a run as loaded so it is not loaded again."""
    date_val = _file_date_to_date(file_date)
    if not date_val:
        return
    if _conn is not None:
        with _conn.cursor() as cur:
            cur.execute(
                "INSERT INTO rxraw.loaded_runs (file_id, file_date, volume_number, supplement_number) VALUES (%s, %s, %s, %s)",
                (str(file_id), date_val, (volume_number or "").strip(), (supplement_number or "").strip()),
            )
        _conn.commit()
        return
    u = url or get_database_url()
    if not u:
        return
    import psycopg2
    conn = psycopg2.connect(u)
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO rxraw.loaded_runs (file_id, file_date, volume_number, supplement_number) VALUES (%s, %s, %s, %s)",
                (str(file_id), date_val, (volume_number or "").strip(), (supplement_number or "").strip()),
            )
        conn.commit()
    finally:
        conn.close()


def load_mf2dict_once(
    run_dir: Path,
    file_id: UUID,
    file_date: str,
    volume_number: str = "",
    supplement_number: str = "",
) -> int:
    """Load MF2DICT into rxraw.raw_mf2dict only if the table is empty. Returns rows loaded (0 if skipped or missing)."""
    url = get_database_url()
    if not url:
        return 0
    dict_table = raw_table_name(DICT_SOURCE_FILE)
    if _table_row_count(dict_table, url) > 0:
        logger.info("rxraw.%s: already loaded, skip", dict_table)
        return 0
    return load_one_file(
        run_dir, file_id, file_date, DICT_SOURCE_FILE, volume_number, supplement_number
    )


def _insert(table: str, rows: list[tuple], url: str | None, *, _conn=None) -> None:
    pos_cols = ", ".join(f"pos{i}" for i in range(1, RAW_POS_COUNT + 1))
    sql = f"""
        INSERT INTO {SCHEMA_NAME}.{table} (file_id, file_date, source_file, line_number, volume_number, supplement_number, {pos_cols})
        VALUES %s
    """
    page_size = get_insert_batch_size()
    if _conn is not None:
        from psycopg2.extras import execute_values
        with _conn.cursor() as cur:
            execute_values(cur, sql, rows, page_size=page_size)
        _conn.commit()
        return
    import psycopg2
    from psycopg2.extras import execute_values
    conn = psycopg2.connect(url)
    try:
        with conn.cursor() as cur:
            execute_values(cur, sql, rows, page_size=page_size)
        conn.commit()
    finally:
        conn.close()
