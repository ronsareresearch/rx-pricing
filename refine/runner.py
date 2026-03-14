"""Orchestrate refinement: find unrefined runs, validate, refine each entity, create views."""

import logging
import uuid
from pathlib import Path

from refine.config import get_database_url
from refine.refiner import refine_append, refine_replace, refine_scd2
from refine.validate import SequenceBreakError, get_last_refined_volume, validate_run
from refine.views import create_views

logger = logging.getLogger(__name__)


def get_data_dir() -> Path:
    """Reuse rxraw data dir for run discovery (file_type)."""
    try:
        from rxraw.config import get_data_dir as _get
        return _get()
    except ImportError:
        import os
        raw = os.environ.get("DATA_DIR")
        if raw:
            return Path(raw)
        return Path(__file__).resolve().parent.parent / "data"


def _file_type_map() -> dict[tuple[str, str], str]:
    """(file_date_iso, volume_number) -> file_type (T or U). From discovered runs."""
    data_dir = get_data_dir()
    try:
        from rxraw.runs import discover_runs
        runs = discover_runs(data_dir)
    except Exception as e:
        logger.warning("Could not discover runs for file_type map: %s", e)
        return {}
    out = {}
    for r in runs:
        # file_date from RunInfo is YYYYMMDD
        if len(r.file_date) == 8:
            iso = f"{r.file_date[:4]}-{r.file_date[4:6]}-{r.file_date[6:8]}"
            out[(iso, (r.volume_number or "").strip())] = r.file_type
    return out


def get_unrefined_runs(conn) -> list[dict]:
    """Rows from rxraw.loaded_runs that have no completed medfile.refine_runs. Ordered by file_date, volume."""
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT lr.file_id, lr.file_date, lr.volume_number, lr.supplement_number
            FROM rxraw.loaded_runs lr
            LEFT JOIN medfile.refine_runs rr ON rr.file_id = lr.file_id AND rr.status = 'done'
            WHERE rr.run_id IS NULL
            ORDER BY lr.file_date, lr.volume_number
            """
        )
        columns = [d[0] for d in cur.description]
        return [dict(zip(columns, row)) for row in cur.fetchall()]


def run_refinement(conn, reset: bool = False) -> tuple[int, int]:
    """
    Refine all unrefined runs. If reset=True, drop medfile schema first (caller must re-create).
    Returns (runs_processed, total_rows_refined).
    """
    if reset:
        from refine.schema import drop_schema_ddl
        with conn.cursor() as cur:
            cur.execute(drop_schema_ddl())
        conn.commit()
        logger.info("Dropped medfile schema (reset)")

    from refine.schema import get_ddl
    with conn.cursor() as cur:
        cur.execute(get_ddl())
    conn.commit()
    logger.info("Ensured medfile schema and tables exist")

    unrefined = get_unrefined_runs(conn)
    if not unrefined:
        logger.info("No unrefined runs")
        return 0, 0

    file_type_map = _file_type_map()
    runs_done = 0
    total_rows = 0

    for run_row in unrefined:
        file_id = run_row["file_id"]
        file_date = run_row["file_date"]
        volume_number = (run_row["volume_number"] or "").strip()
        supplement_number = (run_row["supplement_number"] or "").strip()
        file_date_iso = str(file_date) if file_date else ""
        file_type = file_type_map.get((file_date_iso, volume_number), "U")

        last_vol = get_last_refined_volume(conn)
        try:
            validate_run(file_type, volume_number, last_vol)
        except SequenceBreakError as e:
            logger.error("Validation failed: %s", e)
            raise

        run_id = uuid.uuid4()
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO medfile.refine_runs (run_id, file_id, file_type, file_date, volume_number, supplement_number, status)
                VALUES (%s, %s, %s, %s, %s, %s, 'in_progress')
                """,
                (str(run_id), str(file_id), file_type, file_date, volume_number, supplement_number),
            )
        conn.commit()

        try:
            total_rows += refine_replace(conn, file_id, file_type, run_id, "mf2val")
            total_rows += refine_scd2(conn, file_id, file_type, file_date, run_id, "ndc")
            total_rows += refine_append(conn, file_id, file_type, file_date, run_id, "ndc_price")
            total_rows += refine_scd2(conn, file_id, file_type, file_date, run_id, "drg")
            create_views(conn)
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE medfile.refine_runs SET status = 'done', completed_at = now() WHERE run_id = %s",
                    (str(run_id),),
                )
            conn.commit()
            runs_done += 1
            logger.info("Refined run file_id=%s volume=%s", str(file_id)[:8], volume_number)
        except Exception as e:
            logger.exception("Refinement failed for run %s: %s", file_id, e)
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE medfile.refine_runs SET status = 'failed' WHERE run_id = %s",
                    (str(run_id),),
                )
            conn.commit()
            raise

    return runs_done, total_rows
