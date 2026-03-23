"""Monthly Medi-Span reference views keyed by file month.

These views publish audit-facing reference data by Medi-Span delivery month.
They are built from `medfile` refinement tables only and intentionally avoid
claims-side date logic.

All monthly views are materialized for query performance. They use
REFRESH MATERIALIZED VIEW CONCURRENTLY so UI reads are never blocked
during refresh. Each materialized view has a unique index (required for
concurrent refresh) plus query-oriented indexes for interactive use.
"""

import logging

from refine.schema import SCHEMA_NAME

log = logging.getLogger(__name__)

# PostgreSQL substr is 1-based.
_NDC_HYPHENATE = {
    "5-4-2": "{a}.ndc_upc_hri IS NOT NULL AND length({a}.ndc_upc_hri) = 11 AND "
    "substr({a}.ndc_upc_hri, 1, 5) || '-' || substr({a}.ndc_upc_hri, 6, 4) || '-' || substr({a}.ndc_upc_hri, 10, 2)",
    "4-6": "{a}.ndc_upc_hri IS NOT NULL AND length({a}.ndc_upc_hri) = 10 AND "
    "substr({a}.ndc_upc_hri, 1, 4) || '-' || substr({a}.ndc_upc_hri, 5, 6)",
    "5-5": "{a}.ndc_upc_hri IS NOT NULL AND length({a}.ndc_upc_hri) = 10 AND "
    "substr({a}.ndc_upc_hri, 1, 5) || '-' || substr({a}.ndc_upc_hri, 6, 5)",
}


def _ndc_formatted_expr(alias: str = "n") -> str:
    default_fmt = (
        f"CASE WHEN {alias}.ndc_upc_hri IS NOT NULL AND length({alias}.ndc_upc_hri) = 11 "
        f"THEN substr({alias}.ndc_upc_hri, 1, 5) || '-' || substr({alias}.ndc_upc_hri, 6, 4) || '-' || substr({alias}.ndc_upc_hri, 10, 2) "
        f"ELSE {alias}.ndc_upc_hri END"
    )
    return f"""CASE
        WHEN {alias}.id_number_format_code = '4' THEN
            CASE
                WHEN {alias}.ndc_upc_hri IS NOT NULL AND length({alias}.ndc_upc_hri) = 10
                THEN substr({alias}.ndc_upc_hri, 1, 4) || '-' || substr({alias}.ndc_upc_hri, 5, 6)
                ELSE {alias}.ndc_upc_hri
            END
        WHEN {alias}.id_number_format_code = '5' THEN
            CASE
                WHEN {alias}.ndc_upc_hri IS NOT NULL AND length({alias}.ndc_upc_hri) = 10
                THEN substr({alias}.ndc_upc_hri, 1, 5) || '-' || substr({alias}.ndc_upc_hri, 6, 5)
                ELSE {alias}.ndc_upc_hri
            END
        ELSE {default_fmt}
    END"""


def _monthly_runs_cte() -> str:
    return f"""
WITH ranked_runs AS (
    SELECT
        rr.run_id,
        rr.file_date,
        rr.volume_number,
        rr.supplement_number,
        rr.completed_at,
        date_trunc('month', rr.file_date)::date AS reference_month,
        row_number() OVER (
            PARTITION BY date_trunc('month', rr.file_date)
            ORDER BY rr.file_date DESC, rr.completed_at DESC NULLS LAST, rr.run_id DESC
        ) AS month_rank
    FROM {SCHEMA_NAME}.refine_runs rr
    WHERE rr.status = 'done'
),
selected_runs AS (
    SELECT
        run_id AS reference_run_id,
        file_date AS reference_file_date,
        volume_number,
        supplement_number,
        completed_at,
        reference_month
    FROM ranked_runs
    WHERE month_rank = 1
)
""".strip()


# ---------------------------------------------------------------------------
# Query definitions (SELECT only, no CREATE prefix)
# ---------------------------------------------------------------------------

def _product_package_monthly_query() -> str:
    ndc_fmt = _ndc_formatted_expr("n")
    return f"""
{_monthly_runs_cte()}
SELECT
    sr.reference_month,
    sr.reference_run_id,
    sr.reference_file_date,
    sr.volume_number,
    sr.supplement_number,
    n.run_id AS ndc_run_id,
    n.issue_date AS ndc_issue_date,
    n.effective_start_date AS ndc_effective_start_date,
    n.effective_end_date AS ndc_effective_end_date,
    n.ndc_upc_hri,
    {ndc_fmt} AS ndc_formatted,
    n.drug_descriptor_id,
    nm.drug_name,
    nm.maintenance_drug_code,
    nm.generic_product_identifier AS name_gpi,
    n.gppc_code,
    g.generic_product_identifier AS gpi,
    g.package_size,
    g.package_size_uom,
    g.package_quantity,
    g.package_description_code,
    n.labeler_id,
    lab.manufacturer_name,
    lab.manufacturer_abbrev,
    n.tee_code,
    tee.value_description AS tee_desc,
    n.dea_class_code,
    dea.value_description AS dea_class_desc,
    n.rx_otc_indicator_code,
    rxotc.value_description AS rx_otc_desc,
    n.multi_source_code,
    multisource.value_description AS multi_source_desc,
    n.item_status_flag,
    itemstatus.value_description AS item_status_desc,
    n.name_type_code,
    nametype.value_description AS name_type_desc,
    n.dollar_rank_code,
    n.rx_rank_code,
    n.limited_distribution_code,
    CASE
        WHEN n.dollar_rank_code IS NOT NULL AND trim(n.dollar_rank_code) <> '' THEN true
        WHEN n.rx_rank_code IS NOT NULL AND trim(n.rx_rank_code) <> '' THEN true
        WHEN n.limited_distribution_code IS NOT NULL AND trim(n.limited_distribution_code) <> '' THEN true
        ELSE false
    END AS specialty_proxy
FROM selected_runs sr
JOIN {SCHEMA_NAME}.refinement_ndc n
  ON n.effective_start_date <= sr.reference_file_date
 AND (n.effective_end_date IS NULL OR n.effective_end_date > sr.reference_file_date)
LEFT JOIN LATERAL (
    SELECT nm.*
    FROM {SCHEMA_NAME}.refinement_name nm
    WHERE nm.drug_descriptor_id = n.drug_descriptor_id
      AND nm.effective_start_date <= sr.reference_file_date
      AND (nm.effective_end_date IS NULL OR nm.effective_end_date > sr.reference_file_date)
    ORDER BY nm.effective_start_date DESC, nm.id DESC
    LIMIT 1
) nm ON true
LEFT JOIN LATERAL (
    SELECT g.*
    FROM {SCHEMA_NAME}.refinement_gppc g
    WHERE g.gppc_code = n.gppc_code
      AND g.effective_start_date <= sr.reference_file_date
      AND (g.effective_end_date IS NULL OR g.effective_end_date > sr.reference_file_date)
    ORDER BY g.effective_start_date DESC, g.id DESC
    LIMIT 1
) g ON true
LEFT JOIN LATERAL (
    SELECT lab.*
    FROM {SCHEMA_NAME}.refinement_lab lab
    WHERE lab.labeler_id = n.labeler_id
      AND lab.effective_start_date <= sr.reference_file_date
      AND (lab.effective_end_date IS NULL OR lab.effective_end_date > sr.reference_file_date)
    ORDER BY lab.effective_start_date DESC, lab.id DESC
    LIMIT 1
) lab ON true
LEFT JOIN {SCHEMA_NAME}.mf2val tee
  ON tee.field_id = 'H018' AND tee.field_value = n.tee_code AND tee.language_cd = '01'
LEFT JOIN {SCHEMA_NAME}.mf2val dea
  ON dea.field_id = 'H020' AND dea.field_value = n.dea_class_code AND dea.language_cd = '01'
LEFT JOIN {SCHEMA_NAME}.mf2val rxotc
  ON rxotc.field_id = 'H022' AND rxotc.field_value = n.rx_otc_indicator_code AND rxotc.language_cd = '01'
LEFT JOIN {SCHEMA_NAME}.mf2val multisource
  ON multisource.field_id = 'H072' AND multisource.field_value = n.multi_source_code AND multisource.language_cd = '01'
LEFT JOIN {SCHEMA_NAME}.mf2val itemstatus
  ON itemstatus.field_id = 'H074' AND itemstatus.field_value = n.item_status_flag AND itemstatus.language_cd = '01'
LEFT JOIN {SCHEMA_NAME}.mf2val nametype
  ON nametype.field_id = 'H073' AND nametype.field_value = n.name_type_code AND nametype.language_cd = '01'
""".strip()


def _product_package_price_monthly_query() -> str:
    return f"""
{_monthly_runs_cte()},
ranked_price AS (
    SELECT
        sr.reference_month,
        sr.reference_run_id,
        sr.reference_file_date,
        sr.volume_number,
        sr.supplement_number,
        p.run_id AS price_run_id,
        p.issue_date,
        p.price_effective_date,
        p.ndc_upc_hri,
        p.price_code,
        p.unit_price,
        p.unit_price_extended,
        p.package_price,
        p.awp_indicator_code,
        row_number() OVER (
            PARTITION BY sr.reference_month, p.ndc_upc_hri, p.price_code
            ORDER BY p.price_effective_date DESC, p.issue_date DESC, p.id DESC
        ) AS price_rank
    FROM selected_runs sr
    JOIN {SCHEMA_NAME}.refinement_ndc_price p
      ON p.issue_date <= sr.reference_file_date
     AND p.price_effective_date <= sr.reference_file_date
)
SELECT
    rp.reference_month,
    rp.reference_run_id,
    rp.reference_file_date,
    rp.volume_number,
    rp.supplement_number,
    rp.price_run_id,
    rp.issue_date,
    rp.ndc_upc_hri,
    rp.price_code,
    pricecode.value_description AS price_code_desc,
    rp.price_effective_date,
    rp.unit_price,
    rp.unit_price_extended,
    rp.package_price,
    rp.awp_indicator_code,
    awp.value_description AS awp_indicator_desc
FROM ranked_price rp
LEFT JOIN {SCHEMA_NAME}.mf2val pricecode
  ON pricecode.field_id = 'M012' AND pricecode.field_value = rp.price_code AND pricecode.language_cd = '01'
LEFT JOIN {SCHEMA_NAME}.mf2val awp
  ON awp.field_id = 'M055' AND awp.field_value = rp.awp_indicator_code AND awp.language_cd = '01'
WHERE rp.price_rank = 1
""".strip()


def _gpi_ndc_equivalent_monthly_query() -> str:
    return f"""
{_monthly_runs_cte()}
SELECT DISTINCT
    sr.reference_month,
    sr.reference_run_id,
    sr.reference_file_date,
    sr.volume_number,
    sr.supplement_number,
    g.generic_product_identifier AS gpi,
    n.ndc_upc_hri,
    n.tee_code,
    n.multi_source_code
FROM selected_runs sr
JOIN {SCHEMA_NAME}.refinement_ndc n
  ON n.effective_start_date <= sr.reference_file_date
 AND (n.effective_end_date IS NULL OR n.effective_end_date > sr.reference_file_date)
JOIN LATERAL (
    SELECT g.*
    FROM {SCHEMA_NAME}.refinement_gppc g
    WHERE g.gppc_code = n.gppc_code
      AND g.effective_start_date <= sr.reference_file_date
      AND (g.effective_end_date IS NULL OR g.effective_end_date > sr.reference_file_date)
    ORDER BY g.effective_start_date DESC, g.id DESC
    LIMIT 1
) g ON true
JOIN LATERAL (
    SELECT t.*
    FROM {SCHEMA_NAME}.refinement_tcgpi t
    WHERE t.tc_gpi_key = g.generic_product_identifier
      AND t.effective_start_date <= sr.reference_file_date
      AND (t.effective_end_date IS NULL OR t.effective_end_date > sr.reference_file_date)
      AND t.tc_gpi_name NOT LIKE '%*%'
    ORDER BY t.effective_start_date DESC, t.id DESC
    LIMIT 1
) t ON true
WHERE n.multi_source_code IN ('Y', 'O')
  AND n.tee_code LIKE 'A%'
  AND n.tee_code NOT IN ('A1', 'A2', 'A3', 'A4')
""".strip()


def _price_type_monthly_query(price_code: str) -> str:
    """SELECT query for a monthly price view filtered to a single price code."""
    return f"""
{_monthly_runs_cte()},
ranked_price AS (
    SELECT
        sr.reference_month,
        sr.reference_run_id,
        sr.reference_file_date,
        sr.volume_number,
        sr.supplement_number,
        p.run_id AS price_run_id,
        p.issue_date,
        p.price_effective_date,
        p.ndc_upc_hri,
        p.price_code,
        p.unit_price,
        p.unit_price_extended,
        p.package_price,
        p.awp_indicator_code,
        row_number() OVER (
            PARTITION BY sr.reference_month, p.ndc_upc_hri
            ORDER BY p.price_effective_date DESC, p.issue_date DESC, p.id DESC
        ) AS price_rank
    FROM selected_runs sr
    JOIN {SCHEMA_NAME}.refinement_ndc_price p
      ON p.issue_date <= sr.reference_file_date
     AND p.price_effective_date <= sr.reference_file_date
     AND p.price_code = '{price_code}'
)
SELECT
    rp.reference_month,
    rp.reference_run_id,
    rp.reference_file_date,
    rp.volume_number,
    rp.supplement_number,
    rp.price_run_id,
    rp.issue_date,
    rp.ndc_upc_hri,
    rp.price_code,
    rp.price_effective_date,
    rp.unit_price,
    rp.unit_price_extended,
    rp.package_price,
    rp.awp_indicator_code,
    awp.value_description AS awp_indicator_desc
FROM ranked_price rp
LEFT JOIN {SCHEMA_NAME}.mf2val awp
  ON awp.field_id = 'M055' AND awp.field_value = rp.awp_indicator_code AND awp.language_cd = '01'
WHERE rp.price_rank = 1
""".strip()


# ---------------------------------------------------------------------------
# Materialized view registry
# ---------------------------------------------------------------------------

MATERIALIZED_VIEW_DEFS: list[dict] = [
    {
        "name": "v_product_package_monthly",
        "query_fn": _product_package_monthly_query,
        "unique_cols": "reference_month, ndc_upc_hri",
        "indexes": [
            ("ndc", "ndc_upc_hri"),
            ("gpi", "gpi"),
            ("month", "reference_month"),
            ("name", "drug_name"),
            ("labeler", "labeler_id"),
        ],
    },
    {
        "name": "v_product_package_price_monthly",
        "query_fn": _product_package_price_monthly_query,
        "unique_cols": "reference_month, ndc_upc_hri, price_code",
        "indexes": [
            ("ndc", "ndc_upc_hri"),
            ("month", "reference_month"),
            ("ndc_month", "ndc_upc_hri, reference_month"),
        ],
    },
    {
        "name": "v_product_package_price_awp_monthly",
        "query_fn": lambda: _price_type_monthly_query("A"),
        "unique_cols": "reference_month, ndc_upc_hri",
        "indexes": [
            ("ndc", "ndc_upc_hri"),
            ("month", "reference_month"),
        ],
    },
    {
        "name": "v_product_package_price_wac_monthly",
        "query_fn": lambda: _price_type_monthly_query("W"),
        "unique_cols": "reference_month, ndc_upc_hri",
        "indexes": [
            ("ndc", "ndc_upc_hri"),
            ("month", "reference_month"),
        ],
    },
    {
        "name": "v_product_package_price_dp_monthly",
        "query_fn": lambda: _price_type_monthly_query("D"),
        "unique_cols": "reference_month, ndc_upc_hri",
        "indexes": [
            ("ndc", "ndc_upc_hri"),
            ("month", "reference_month"),
        ],
    },
    {
        "name": "v_gpi_ndc_equivalent_monthly",
        "query_fn": _gpi_ndc_equivalent_monthly_query,
        "unique_cols": "reference_month, gpi, ndc_upc_hri",
        "indexes": [
            ("gpi", "gpi"),
            ("ndc", "ndc_upc_hri"),
            ("month", "reference_month"),
        ],
    },
]

MATERIALIZED_VIEW_NAMES: set[str] = {d["name"] for d in MATERIALIZED_VIEW_DEFS}


# ---------------------------------------------------------------------------
# Lifecycle functions
# ---------------------------------------------------------------------------

def _matview_exists(cur, name: str) -> bool:
    cur.execute(
        "SELECT 1 FROM pg_matviews WHERE schemaname = %s AND matviewname = %s",
        (SCHEMA_NAME, name),
    )
    return cur.fetchone() is not None


def _regular_view_exists(cur, name: str) -> bool:
    cur.execute(
        "SELECT 1 FROM information_schema.views "
        "WHERE table_schema = %s AND table_name = %s",
        (SCHEMA_NAME, name),
    )
    return cur.fetchone() is not None


def _create_indexes(cur, view_def: dict) -> None:
    name = view_def["name"]
    fqn = f"{SCHEMA_NAME}.{name}"
    cur.execute(
        f"CREATE UNIQUE INDEX IF NOT EXISTS ux_{name} ON {fqn} ({view_def['unique_cols']})"
    )
    for suffix, cols in view_def["indexes"]:
        cur.execute(
            f"CREATE INDEX IF NOT EXISTS ix_{name}_{suffix} ON {fqn} ({cols})"
        )


def create_monthly_views(conn) -> None:
    """Create materialized monthly views (first-time or after reset).

    Idempotent: skips views that already exist as materialized views.
    Drops any regular VIEW with the same name (transition from older code).
    """
    with conn.cursor() as cur:
        for vdef in MATERIALIZED_VIEW_DEFS:
            name = vdef["name"]
            fqn = f"{SCHEMA_NAME}.{name}"

            if _regular_view_exists(cur, name):
                cur.execute(f"DROP VIEW IF EXISTS {fqn}")
                log.info("Dropped regular view %s (replacing with materialized)", fqn)

            if _matview_exists(cur, name):
                log.info("Materialized view %s already exists, skipping create", fqn)
                continue

            query = vdef["query_fn"]()
            cur.execute(f"CREATE MATERIALIZED VIEW {fqn} AS {query} WITH DATA")
            _create_indexes(cur, vdef)
            log.info("Created materialized view %s with indexes", fqn)

    conn.commit()


def refresh_monthly_views(conn) -> None:
    """Refresh all materialized monthly views concurrently.

    Uses CONCURRENTLY so existing reads (e.g. UI queries) are not blocked.
    Requires the unique index created by create_monthly_views.
    """
    with conn.cursor() as cur:
        for vdef in MATERIALIZED_VIEW_DEFS:
            name = vdef["name"]
            fqn = f"{SCHEMA_NAME}.{name}"

            if not _matview_exists(cur, name):
                log.warning(
                    "Materialized view %s does not exist, run without --refresh-only first",
                    fqn,
                )
                continue

            cur.execute(f"REFRESH MATERIALIZED VIEW CONCURRENTLY {fqn}")
            log.info("Refreshed materialized view %s", fqn)

    conn.commit()


def drop_materialized_views(conn) -> None:
    """Drop all managed materialized views (used by --reset)."""
    with conn.cursor() as cur:
        for vdef in MATERIALIZED_VIEW_DEFS:
            fqn = f"{SCHEMA_NAME}.{vdef['name']}"
            cur.execute(f"DROP MATERIALIZED VIEW IF EXISTS {fqn}")
            log.info("Dropped materialized view %s", fqn)
    conn.commit()
