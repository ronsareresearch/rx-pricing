"""
View pipeline: create/refresh medfile views from refinement. Separate process from rxraw and refine.

Run: uv run python -m view
Skip PCIP views: uv run python -m view --no-pcip

Default build includes:
- current entity views
- monthly Medi-Span file-month views
- optional PCIP current-state reference views

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
        run_views(conn, include_pcip=not args.no_pcip)
        log.info("Views created/refreshed (monthly=true PCIP=%s)", not args.no_pcip)
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main())
