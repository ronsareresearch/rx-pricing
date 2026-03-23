"""View runner: create or replace all medfile views.

Builds normalized views across five domain families, monthly materialized
views, and an error correction audit view. Run after refine.

Monthly views are materialized for query performance and refreshed
concurrently so UI reads are never blocked.

Maintains a registry of managed views and drops orphaned views on each run.
"""

import logging

from refine.schema import SCHEMA_NAME

log = logging.getLogger(__name__)

MANAGED_REGULAR_VIEWS: set[str] = {
    # Family 1: Packaged drug reference (current)
    "v_product_package_current",
    "v_product_package_price_current",
    "v_product_package_modifier_current",
    "v_product_package_price_history",
    # Family 2: GPI and equivalence
    "v_gpi_current",
    "v_gppc_current",
    "v_gpi_ndc_equivalent_current",
    # Family 3: Clinical concept hierarchy
    "v_drug_name_current",
    "v_routed_drug_current",
    "v_drug_dose_form_current",
    "v_routed_drug_form_current",
    "v_dispensable_drug_current",
    "v_dispensable_drug_rollup_current",
    # Family 4: Ingredient composition
    "v_concept_ingredient_set_current",
    "v_ingredient_set_member_current",
    "v_ingredient_current",
    "v_concept_ingredient_current",
    # Family 5: Terminology and alternate IDs
    "v_code_lookup_current",
    "v_concept_description_current",
    "v_concept_reference_name_current",
    "v_alternate_id_current",
    # Error correction audit view
    "v_error_corrections",
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


def run_views(conn, refresh_only: bool = False) -> None:
    """Create or replace all medfile views then drop orphaned views.

    Regular views (all five domain families + error corrections):
        Always recreated with CREATE OR REPLACE VIEW.

    Materialized views (monthly):
        - Normal run: CREATE MATERIALIZED VIEW IF NOT EXISTS ... WITH DATA,
          then REFRESH CONCURRENTLY for any that already existed.
        - refresh_only=True: only REFRESH CONCURRENTLY (faster, for use
          after incremental refine runs when view definitions haven't changed).
    """
    from view.clinical_views import create_clinical_views
    from view.current_views import create_current_views
    from view.err_views import create_err_views
    from view.gpi_views import create_gpi_views
    from view.indexes import ensure_performance_indexes
    from view.ingredient_views import create_ingredient_views
    from view.monthly_views import create_monthly_views, refresh_monthly_views
    from view.terminology_views import create_terminology_views

    ensure_performance_indexes(conn)

    if refresh_only:
        refresh_monthly_views(conn)
        log.info("Materialized views refreshed (refresh-only mode)")
        return

    create_terminology_views(conn)
    log.info("Terminology helper views created (Family 5)")

    create_current_views(conn)
    create_err_views(conn)
    log.info("Packaged drug reference views created (Family 1)")

    create_gpi_views(conn)
    log.info("GPI and equivalence views created (Family 2)")

    create_clinical_views(conn)
    log.info("Clinical hierarchy views created (Family 3)")

    create_ingredient_views(conn)
    log.info("Ingredient composition views created (Family 4)")

    create_monthly_views(conn)

    dropped = drop_orphaned_views(conn)
    if dropped:
        log.info("Cleaned up %d orphaned view(s): %s", len(dropped), dropped)
