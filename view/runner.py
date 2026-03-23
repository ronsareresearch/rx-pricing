"""View runner: create or replace all medfile views.

Builds normalized current views, monthly materialized views, and legacy
entity/PCIP views from refinement tables only. Run after refine.

Monthly views are materialized for query performance and refreshed
concurrently so UI reads are never blocked.

Maintains a registry of managed views and drops orphaned views on each run.
"""

import logging

from refine.schema import SCHEMA_NAME

log = logging.getLogger(__name__)

MANAGED_REGULAR_VIEWS: set[str] = {
    # Normalized current views
    "v_product_package_current",
    "v_product_package_price_current",
    "v_product_package_modifier_current",
    # Legacy entity views (deprecated — kept for backward compatibility)
    "v_ndc",
    "v_ndc_price",
    "v_drg",
    # Legacy PCIP views (v_ndc_pcip_reference deprecated — kept for backward compatibility)
    "v_ndc_pcip_reference",
    "v_gpi_equivalents",
    "v_drg_maintenance",
}

DEPRECATED_VIEWS: dict[str, str] = {
    "v_ndc": "v_product_package_current",
    "v_ndc_price": "v_product_package_price_current",
    "v_ndc_pcip_reference": "v_product_package_current + v_product_package_price_current",
}


def drop_orphaned_views(conn) -> list[str]:
    """Drop regular views and materialized views not in the managed sets."""
    from view.monthly_views import MATERIALIZED_VIEW_NAMES

    managed_all = MANAGED_REGULAR_VIEWS | MATERIALIZED_VIEW_NAMES
    dropped: list[str] = []

    with conn.cursor() as cur:
        cur.execute(
            "SELECT table_name FROM information_schema.views "
            "WHERE table_schema = %s ORDER BY table_name",
            (SCHEMA_NAME,),
        )
        db_regular = {row[0] for row in cur.fetchall()}

        cur.execute(
            "SELECT matviewname FROM pg_matviews "
            "WHERE schemaname = %s ORDER BY matviewname",
            (SCHEMA_NAME,),
        )
        db_materialized = {row[0] for row in cur.fetchall()}

    orphaned_regular = sorted(db_regular - managed_all)
    orphaned_materialized = sorted(db_materialized - MATERIALIZED_VIEW_NAMES)

    if not orphaned_regular and not orphaned_materialized:
        log.info("No orphaned views found")
        return []

    with conn.cursor() as cur:
        for name in orphaned_regular:
            cur.execute(f"DROP VIEW IF EXISTS {SCHEMA_NAME}.{name}")
            log.info("Dropped orphaned view %s.%s", SCHEMA_NAME, name)
            dropped.append(name)
        for name in orphaned_materialized:
            cur.execute(f"DROP MATERIALIZED VIEW IF EXISTS {SCHEMA_NAME}.{name}")
            log.info("Dropped orphaned materialized view %s.%s", SCHEMA_NAME, name)
            dropped.append(name)
    conn.commit()
    return dropped


def run_views(conn, include_pcip: bool = True, refresh_only: bool = False) -> None:
    """Create or replace all medfile views then drop orphaned views.

    Regular views (normalized current, legacy entity, legacy PCIP):
        Always recreated with CREATE OR REPLACE VIEW.

    Materialized views (monthly):
        - Normal run: CREATE MATERIALIZED VIEW IF NOT EXISTS ... WITH DATA,
          then REFRESH CONCURRENTLY for any that already existed.
        - refresh_only=True: only REFRESH CONCURRENTLY (faster, for use
          after incremental refine runs when view definitions haven't changed).
    """
    from view.current_views import create_current_views
    from view.entity_views import create_entity_views
    from view.indexes import ensure_performance_indexes
    from view.monthly_views import create_monthly_views, refresh_monthly_views
    from view.pcip_views import create_pcip_views

    ensure_performance_indexes(conn)

    if refresh_only:
        refresh_monthly_views(conn)
        log.info("Materialized views refreshed (refresh-only mode)")
        return

    create_current_views(conn)
    log.info("Normalized current views created")

    create_entity_views(conn, entities=["ndc", "ndc_price", "drg"])
    create_monthly_views(conn)
    if include_pcip:
        create_pcip_views(conn)

    for old_view, replacement in DEPRECATED_VIEWS.items():
        log.warning(
            "View %s.%s is deprecated — use %s instead",
            SCHEMA_NAME, old_view, replacement,
        )

    dropped = drop_orphaned_views(conn)
    if dropped:
        log.info("Cleaned up %d orphaned view(s): %s", len(dropped), dropped)
