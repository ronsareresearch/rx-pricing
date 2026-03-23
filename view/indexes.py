"""Performance indexes for view query patterns.

These indexes optimize the source refinement tables for the query patterns
used by monthly materialized views and current-state views. They are
idempotent (IF NOT EXISTS) and safe to run on existing databases.

New schemas get temporal indexes automatically via refine/schema.py.
This module adds view-specific composite indexes that further optimize
the LATERAL joins and ranking queries used during materialized view refresh.
"""

import logging

from refine.schema import SCHEMA_NAME

log = logging.getLogger(__name__)

PERFORMANCE_INDEXES: list[str] = [
    # -- refinement_ndc: monthly view main join filters on temporal range --
    f"CREATE INDEX IF NOT EXISTS ix_refinement_ndc_temporal "
    f"ON {SCHEMA_NAME}.refinement_ndc (ndc_upc_hri, effective_start_date, effective_end_date)",

    # -- refinement_name: LATERAL join on (drug_descriptor_id + temporal) --
    f"CREATE INDEX IF NOT EXISTS ix_refinement_name_temporal "
    f"ON {SCHEMA_NAME}.refinement_name (drug_descriptor_id, effective_start_date, effective_end_date)",

    # -- refinement_gppc: LATERAL join on (gppc_code + temporal) --
    f"CREATE INDEX IF NOT EXISTS ix_refinement_gppc_temporal "
    f"ON {SCHEMA_NAME}.refinement_gppc (gppc_code, effective_start_date, effective_end_date)",

    # -- refinement_lab: LATERAL join on (labeler_id + temporal) --
    f"CREATE INDEX IF NOT EXISTS ix_refinement_lab_temporal "
    f"ON {SCHEMA_NAME}.refinement_lab (labeler_id, effective_start_date, effective_end_date)",

    # -- refinement_tcgpi: LATERAL join on (tc_gpi_key + temporal) --
    f"CREATE INDEX IF NOT EXISTS ix_refinement_tcgpi_temporal "
    f"ON {SCHEMA_NAME}.refinement_tcgpi (tc_gpi_key, effective_start_date, effective_end_date)",

    # -- refinement_ndc_price: price ranking in monthly views --
    f"CREATE INDEX IF NOT EXISTS ix_refinement_ndc_price_ranking "
    f"ON {SCHEMA_NAME}.refinement_ndc_price (ndc_upc_hri, price_code, price_effective_date DESC, issue_date DESC, id DESC)",

    # -- refinement_ndc_price: current price view (is_active filter + ranking) --
    f"CREATE INDEX IF NOT EXISTS ix_refinement_ndc_price_active "
    f"ON {SCHEMA_NAME}.refinement_ndc_price (is_active, ndc_upc_hri, price_code, price_effective_date DESC)",

    # -- mf2val: already has PK on (field_id, field_value, language_cd) --
    # No additional index needed.

    # -- refine_runs: monthly CTE filters on status --
    f"CREATE INDEX IF NOT EXISTS ix_refine_runs_status "
    f"ON {SCHEMA_NAME}.refine_runs (status, file_date)",
]


def ensure_performance_indexes(conn) -> None:
    """Create performance indexes if they don't exist. Idempotent."""
    with conn.cursor() as cur:
        for ddl in PERFORMANCE_INDEXES:
            cur.execute(ddl)
    conn.commit()
    log.info("Performance indexes ensured (%d indexes)", len(PERFORMANCE_INDEXES))
