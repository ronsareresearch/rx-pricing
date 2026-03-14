"""Generic refine logic: replace, SCD2, append_only. Reads from rxraw.raw_* and writes to medfile.
Uses configurable page size, chunked processing, and optional rules cache for throughput and scalability.
"""

import logging
from datetime import date
from decimal import Decimal
from uuid import UUID

from psycopg2.extras import execute_values, RealDictCursor

from refine.config import get_refine_page_size
from refine.rule_engine import apply_column_map, load_rules

logger = logging.getLogger(__name__)


def _batch_iter(items: list, size: int):
    """Yield chunks of items of length size."""
    for i in range(0, len(items), size):
        yield items[i : i + size]


def _ensure_date(issue_date: date | str | None) -> date | None:
    """Convert YYYYMMDD string or date to date."""
    if issue_date is None:
        return None
    if isinstance(issue_date, date):
        return issue_date
    s = (issue_date if isinstance(issue_date, str) else str(issue_date)).strip()
    if len(s) != 8:
        return None
    try:
        return date(int(s[:4]), int(s[4:6]), int(s[6:8]))
    except (ValueError, TypeError):
        return None


def _raw_rows(conn, source_table: str, file_id: UUID) -> list[dict]:
    """Fetch all rows from source_table for this file_id. Returns list of dicts (pos1, pos2, ...)."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            f"SELECT * FROM {source_table} WHERE file_id = %s ORDER BY line_number",
            (str(file_id),),
        )
        return [dict(row) for row in cur.fetchall()]


def _serialize_val(v):
    """Convert Python types for psycopg2 (Decimal, date -> str for INSERT)."""
    if v is None:
        return None
    if isinstance(v, Decimal):
        return str(v)
    if isinstance(v, date):
        return v.isoformat()
    return v


def refine_replace(
    conn,
    file_id: UUID,
    file_type: str,
    run_id: UUID,
    entity: str,
    rules: dict | None = None,
) -> int:
    """
    Refine MF2VAL: Full (T) = truncate + insert; Incremental (U) = upsert by PK.
    Processes raw rows in chunks (configurable page size). Returns number of rows written.
    """
    rules = rules or load_rules(entity)
    source_table = rules["source_table"]
    target_table = rules["target_table"]
    columns = rules["columns"]
    target_cols = [c["name"] for c in columns] + ["run_id"]
    business_key = rules.get("business_key") or []
    col_names = [c["name"] for c in columns]
    page_size = get_refine_page_size()

    raw_list = _raw_rows(conn, source_table, file_id)
    if not raw_list:
        logger.info("%s: no raw rows for file_id=%s", entity, file_id)
        return 0

    cols_str = ", ".join(target_cols)
    update_cols = [c["name"] for c in columns if c["name"] not in business_key] + ["run_id"]
    conflict_cols = ", ".join(business_key)
    updates = ", ".join(f"{c} = EXCLUDED.{c}" for c in update_cols)
    sql = f"""
        INSERT INTO {target_table} ({cols_str})
        VALUES %s
        ON CONFLICT ({conflict_cols})
        DO UPDATE SET {updates}
    """
    total_written = 0
    with conn.cursor() as cur:
        if file_type == "T":
            cur.execute(f"TRUNCATE TABLE {target_table}")
        for chunk in _batch_iter(raw_list, page_size):
            rows = []
            for raw in chunk:
                parsed = apply_column_map(raw, columns)
                if any(parsed.get(k) is None for k in business_key):
                    continue
                row_tuple = tuple(_serialize_val(parsed.get(n)) for n in col_names)
                rows.append(row_tuple + (str(run_id),))
            if rows:
                execute_values(cur, sql, rows, page_size=page_size)
                total_written += len(rows)
    if total_written == 0:
        logger.info("%s: no valid rows (all skipped for null business key) for file_id=%s", entity, file_id)
    else:
        conn.commit()
        logger.info("%s: refine_replace %s rows into %s", entity, total_written, target_table)
    return total_written


def refine_scd2(
    conn,
    file_id: UUID,
    file_type: str,
    issue_date: date | str,
    run_id: UUID,
    entity: str,
    rules: dict | None = None,
) -> int:
    """
    Refine SCD2 entities: Full (T) = chunked insert; Incremental (U) = per-chunk classify then batch UPDATE/INSERT.
    Returns number of rows inserted.
    """
    rules = rules or load_rules(entity)
    source_table = rules["source_table"]
    target_table = rules["target_table"]
    columns = rules["columns"]
    business_key = rules["business_key"]
    txn_col = rules.get("transaction_cd_column", "transaction_cd")
    source_file = rules.get("source_file", entity.upper())
    page_size = get_refine_page_size()

    issue_d = _ensure_date(issue_date)
    if not issue_d:
        raise ValueError(f"Invalid issue_date for SCD2: {issue_date!r}")

    raw_list = _raw_rows(conn, source_table, file_id)
    if not raw_list:
        logger.info("%s: no raw rows for file_id=%s", entity, file_id)
        return 0

    col_names = [c["name"] for c in columns]
    scd2_cols = ["run_id", "issue_date", "source_file", "is_current", "effective_start_date", "effective_end_date"]
    all_cols = col_names + scd2_cols
    inserted = 0
    bk_cols = ", ".join(business_key)

    with conn.cursor() as cur:
        if file_type == "T":
            for chunk in _batch_iter(raw_list, page_size):
                rows = []
                for raw in chunk:
                    parsed = apply_column_map(raw, columns)
                    vals = [_serialize_val(parsed.get(n)) for n in col_names]
                    rows.append(
                        tuple(vals)
                        + (str(run_id), issue_d.isoformat(), source_file, True, issue_d.isoformat(), None)
                    )
                if rows:
                    execute_values(
                        cur,
                        f"INSERT INTO {target_table} ({', '.join(all_cols)}) VALUES %s",
                        rows,
                        page_size=page_size,
                    )
                    inserted += len(rows)
        else:
            for chunk in _batch_iter(raw_list, page_size):
                adds: list[tuple] = []
                changes: list[tuple] = []
                delete_bk_list: list[tuple] = []
                scd2_suffix = (str(run_id), issue_d.isoformat(), source_file, True, issue_d.isoformat(), None)
                for raw in chunk:
                    parsed = apply_column_map(raw, columns)
                    txn = (parsed.get(txn_col) or "").strip().upper()
                    bk_vals = tuple(parsed.get(k) for k in business_key)
                    row_tuple = tuple(_serialize_val(parsed.get(n)) for n in col_names)
                    if txn == "A":
                        adds.append(row_tuple + scd2_suffix)
                    elif txn == "C":
                        changes.append((bk_vals, row_tuple + scd2_suffix))
                    elif txn == "D":
                        delete_bk_list.append(bk_vals)
                end_date_keys = delete_bk_list + [c[0] for c in changes]
                if end_date_keys:
                    for batch in _batch_iter(end_date_keys, page_size):
                        placeholders = ", ".join(
                            "(" + ", ".join("%s" for _ in business_key) + ")" for _ in batch
                        )
                        flat = [v for tup in batch for v in tup]
                        cur.execute(
                            f"""
                            UPDATE {target_table}
                            SET is_current = false, effective_end_date = %s
                            WHERE ({bk_cols}) IN ({placeholders}) AND is_current = true
                            """,
                            [issue_d.isoformat()] + flat,
                        )
                if adds:
                    execute_values(
                        cur,
                        f"INSERT INTO {target_table} ({', '.join(all_cols)}) VALUES %s",
                        adds,
                        page_size=page_size,
                    )
                    inserted += len(adds)
                if changes:
                    execute_values(
                        cur,
                        f"INSERT INTO {target_table} ({', '.join(all_cols)}) VALUES %s",
                        [c[1] for c in changes],
                        page_size=page_size,
                    )
                    inserted += len(changes)

    conn.commit()
    logger.info("%s: refine_scd2 %s rows into %s", entity, inserted, target_table)
    return inserted


def refine_append(
    conn,
    file_id: UUID,
    file_type: str,
    issue_date: date | str,
    run_id: UUID,
    entity: str,
    rules: dict | None = None,
) -> int:
    """
    Refine append_only (e.g. NDC Price, GPR): A/C = batched insert; D = batched is_active=false.
    Processes raw rows in chunks. Returns number of rows inserted.
    """
    rules = rules or load_rules(entity)
    source_table = rules["source_table"]
    target_table = rules["target_table"]
    columns = rules["columns"]
    business_key = rules["business_key"]
    txn_col = rules.get("transaction_cd_column", "transaction_cd")
    source_file = rules.get("source_file", "MF2PRC")
    page_size = get_refine_page_size()

    issue_d = _ensure_date(issue_date)
    if not issue_d:
        raise ValueError(f"Invalid issue_date for append: {issue_date!r}")

    raw_list = _raw_rows(conn, source_table, file_id)
    if not raw_list:
        logger.info("%s: no raw rows for file_id=%s", entity, file_id)
        return 0

    col_names = [c["name"] for c in columns]
    extra_cols = ["run_id", "issue_date", "source_file", "is_active"]
    all_cols = col_names + extra_cols
    inserted = 0
    bk_cols = ", ".join(business_key)

    with conn.cursor() as cur:
        for chunk in _batch_iter(raw_list, page_size):
            inserts: list[tuple] = []
            deactivate_bk_list: list[tuple] = []
            suffix = (str(run_id), issue_d.isoformat(), source_file)
            for raw in chunk:
                parsed = apply_column_map(raw, columns)
                txn = (parsed.get(txn_col) or "").strip().upper()
                if txn == "D":
                    deactivate_bk_list.append(tuple(_serialize_val(parsed.get(k)) for k in business_key))
                else:
                    row_tuple = tuple(_serialize_val(parsed.get(n)) for n in col_names)
                    inserts.append(row_tuple + suffix + (True,))
            if deactivate_bk_list:
                for batch in _batch_iter(deactivate_bk_list, page_size):
                    placeholders = ", ".join(
                        "(" + ", ".join("%s" for _ in business_key) + ")" for _ in batch
                    )
                    flat = [v for tup in batch for v in tup]
                    cur.execute(
                        f"UPDATE {target_table} SET is_active = false WHERE ({bk_cols}) IN ({placeholders}) AND is_active = true",
                        flat,
                    )
            if inserts:
                execute_values(
                    cur,
                    f"INSERT INTO {target_table} ({', '.join(all_cols)}) VALUES %s",
                    inserts,
                    page_size=page_size,
                )
                inserted += len(inserts)
    conn.commit()
    logger.info("%s: refine_append %s rows into %s", entity, inserted, target_table)
    return inserted
