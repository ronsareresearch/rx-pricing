"""
Refine ETL: refine raw runs into medfile schema (tables only). Views are separate.
Run: uv run python -m refine
Reset (drop medfile and re-refine all): uv run python -m refine --reset
Clean failed runs before re-run: uv run python -m refine --clean-failed
"""

import logging
import sys
import time

import psycopg2

from refine.config import get_database_url
from refine.runner import delete_failed_run_data, run_refinement


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Refine ETL: rxraw -> medfile tables (views are separate)")
    parser.add_argument("--reset", action="store_true", help="Drop medfile schema and re-refine all runs")
    parser.add_argument("--clean-failed", action="store_true", help="Delete refinement data for failed runs (then re-run refine)")
    args = parser.parse_args()

    configure_logging()
    log = logging.getLogger("refine")

    url = get_database_url()
    if not url:
        log.error("EXTERNAL_DATABASE_URL not set")
        return 1

    try:
        conn = psycopg2.connect(url)
    except Exception as e:
        log.exception("Database connection failed: %s", e)
        return 1

    try:
        if args.clean_failed:
            n = delete_failed_run_data(conn)
            log.info("Cleaned %s failed run(s). Re-run without --clean-failed to refine.", n)
            return 0
        start = time.monotonic()
        runs_done, total_rows = run_refinement(conn, reset=args.reset)
        elapsed = time.monotonic() - start
        log.info(
            "Refine complete runs=%s total_rows=%s duration_seconds=%.2f",
            runs_done, total_rows, elapsed,
        )
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
