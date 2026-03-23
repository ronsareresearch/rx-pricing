"""
View pipeline: create/refresh medfile views from refinement. Separate process from rxraw and refine.

Run: uv run python -m view
Skip PCIP views: uv run python -m view --no-pcip
Refresh only (after incremental refine): uv run python -m view --refresh-only
Reset materialized views: uv run python -m view --reset

Default build includes:
- current entity views (regular)
- monthly materialized views (created + indexed, or refreshed concurrently)
- optional PCIP current-state reference views (regular)

Requires EXTERNAL_DATABASE_URL (same as refine). Run after refinement so tables exist.
"""

import logging
import sys

import psycopg2

from view.config import get_database_url
from view.runner import run_views


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(
        description="View pipeline: create/refresh current and monthly medfile views (separate from rxraw and refine)",
    )
    parser.add_argument(
        "--no-pcip",
        action="store_true",
        help="Skip PCIP reference views (v_ndc_pcip_reference, v_gpi_equivalents, v_drg_maintenance)",
    )
    parser.add_argument(
        "--refresh-only",
        action="store_true",
        help="Only refresh materialized views (skip entity/PCIP view recreation and orphan cleanup)",
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Drop and recreate all materialized views from scratch",
    )
    args = parser.parse_args()

    configure_logging()
    log = logging.getLogger("view")

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
        if args.reset:
            from view.monthly_views import drop_materialized_views
            drop_materialized_views(conn)
            log.info("Materialized views dropped, recreating")

        run_views(
            conn,
            include_pcip=not args.no_pcip,
            refresh_only=args.refresh_only,
        )
        log.info(
            "Views %s (PCIP=%s)",
            "refreshed" if args.refresh_only else "created/refreshed",
            not args.no_pcip,
        )
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
