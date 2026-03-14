"""
Rxraw ETL: create schema rxraw, load full + incremental runs (28 raw tables).
Run: uv run python -m rxraw
Reset (drop all tables and reload): uv run python -m rxraw --reset

Efficiency:
- Duplicate runs are skipped via rxraw.loaded_runs (file_date + volume_number).
- Within a run, files already loaded for that run are skipped (resume after crash; no duplicate rows).
- One DB connection per run; configurable insert batch size (RXRAW_INSERT_BATCH_SIZE).
"""

import logging
import sys
import time
import uuid
from pathlib import Path

from rxraw.config import get_data_dir, get_database_url
from rxraw.load import (
    get_existing_file_id_for_run,
    load_mf2dict_once,
    load_run,
    record_loaded_run,
    run_already_loaded,
)
from rxraw.runs import discover_runs
from rxraw.schema import SCHEMA_NAME, get_raw_ddl


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )


def check_connection() -> bool:
    url = get_database_url()
    if not url:
        logging.getLogger("rxraw").error("EXTERNAL_DATABASE_URL not set")
        return False
    try:
        import psycopg2
        conn = psycopg2.connect(url)
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()
            return True
        finally:
            conn.close()
    except Exception as e:
        logging.getLogger("rxraw").exception("Database connection failed: %s", e)
        return False


def drop_schema() -> bool:
    """Drop schema rxraw and all tables (CASCADE). Use with --reset to reload from scratch."""
    url = get_database_url()
    if not url:
        return False
    try:
        import psycopg2
        conn = psycopg2.connect(url)
        conn.autocommit = True
        try:
            with conn.cursor() as cur:
                cur.execute(f"DROP SCHEMA IF EXISTS {SCHEMA_NAME} CASCADE")
            logging.getLogger("rxraw").info("Schema %s dropped", SCHEMA_NAME)
            return True
        finally:
            conn.close()
    except Exception as e:
        logging.getLogger("rxraw").exception("Schema drop failed: %s", e)
        return False


def deploy_schema() -> bool:
    """Create schema rxraw and all raw_* tables."""
    url = get_database_url()
    if not url:
        return False
    try:
        import psycopg2
        conn = psycopg2.connect(url)
        conn.autocommit = True
        try:
            with conn.cursor() as cur:
                cur.execute(get_raw_ddl())
            logging.getLogger("rxraw").info("Schema rxraw deployed")
            return True
        finally:
            conn.close()
    except Exception as e:
        logging.getLogger("rxraw").exception("Schema deploy failed: %s", e)
        return False


def run(reset: bool = False) -> int:
    """Create rxraw schema, discover runs (full + incrementals), load each run in order."""
    configure_logging()
    log = logging.getLogger("rxraw")
    start = time.monotonic()

    data_dir = get_data_dir()
    if not data_dir.exists():
        log.error("data_dir missing: %s", data_dir)
        return 1

    if not get_database_url():
        log.error("EXTERNAL_DATABASE_URL not set")
        return 1
    if not check_connection():
        log.error("database connection failed")
        return 1

    if reset:
        log.info("Reset requested: dropping schema rxraw and reloading all tables")
        if not drop_schema():
            log.error("drop schema failed")
            return 1

    if not deploy_schema():
        log.error("rxraw schema deploy failed")
        return 1

    # MF2DICT: load once (data dictionary)
    runs = discover_runs(data_dir)
    dict_load_dir = data_dir
    dict_file_date = ""
    dict_volume = ""
    dict_supplement = ""
    if runs:
        dict_load_dir = runs[0].run_dir
        dict_file_date = runs[0].file_date
        dict_volume = runs[0].volume_number
        dict_supplement = runs[0].supplement_number or ""
    if (dict_load_dir / "MF2DICT").is_file():
        n_dict = load_mf2dict_once(
            dict_load_dir,
            uuid.uuid4(),
            dict_file_date or "19700101",
            volume_number=dict_volume,
            supplement_number=dict_supplement,
        )
        if n_dict > 0:
            log.info("MF2DICT loaded once: %d rows", n_dict)
    else:
        log.debug("MF2DICT not found in %s, skip", dict_load_dir)

    if not runs:
        log.warning("No runs found under %s (no MF2SUM with T/U)", data_dir)
        # Single run from data_dir if no MF2SUM: treat as one full load
        runs = [_make_fallback_run(data_dir)]
        log.info("Using single run from data_dir (no MF2SUM): %s", runs[0].run_dir)

    total_rows = 0
    skipped_runs = 0
    for i, run_info in enumerate(runs):
        if not reset and run_already_loaded(run_info.file_date, run_info.volume_number):
            log.info(
                "run %d/%d already loaded (file_date=%s volume=%s), skip",
                i + 1, len(runs), run_info.file_date, run_info.volume_number,
            )
            skipped_runs += 1
            continue
        # One connection per run: resume uses existing file_id if run was partially loaded
        import psycopg2
        conn = psycopg2.connect(get_database_url())
        try:
            file_id = get_existing_file_id_for_run(
                run_info.file_date, run_info.volume_number, _conn=conn
            ) or uuid.uuid4()
            log.info(
                "run %d/%d file_type=%s volume=%s file_date=%s run_dir=%s",
                i + 1, len(runs), run_info.file_type, run_info.volume_number, run_info.file_date, run_info.run_dir,
            )
            counts = load_run(
                run_info.run_dir,
                file_id,
                run_info.file_date,
                volume_number=run_info.volume_number,
                supplement_number=run_info.supplement_number or "",
                _conn=conn,
            )
            run_total = sum(counts.values())
            total_rows += run_total
            record_loaded_run(
                file_id,
                run_info.file_date,
                run_info.volume_number,
                supplement_number=run_info.supplement_number or "",
                _conn=conn,
            )
            log.info("run file_id=%s files_loaded=%d rows=%d", str(file_id)[:8], len(counts), run_total)
        finally:
            conn.close()

    elapsed = time.monotonic() - start
    log.info(
        "rxraw load complete runs_loaded=%d runs_skipped=%d total_rows=%d duration_seconds=%.2f",
        len(runs) - skipped_runs, skipped_runs, total_rows, elapsed,
    )
    return 0


def _make_fallback_run(data_dir: Path):
    """When no MF2SUM found: one run from data_dir with default file_date/volume."""
    from rxraw.runs import RunInfo
    from datetime import date
    return RunInfo(
        run_dir=data_dir,
        file_type="T",
        file_date=date.today().strftime("%Y%m%d"),
        volume_number="0",
        supplement_number="",
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Rxraw ETL: load MED-File v2 into rxraw schema.")
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Drop schema rxraw and all tables, then reload all 28 tables from data (removes duplicates).",
    )
    args = parser.parse_args()
    sys.exit(run(reset=args.reset))
