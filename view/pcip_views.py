"""PCIP (Pharmacy Claims Intelligence Platform) reference views.

Builds v_ndc_pcip_reference, v_gpi_equivalents, and v_drg_maintenance from
medfile refinement tables. Used by downstream claims/analytics (separate project)
via Reference API or replicated data.

DEPRECATION NOTICE:
    v_ndc_pcip_reference is superseded by v_product_package_current
    (see view/current_views.py) plus v_product_package_price_current for AWP.
    v_gpi_equivalents will be superseded by v_gpi_ndc_equivalent_current
    (not yet implemented).
    v_drg_maintenance has no replacement yet and is not deprecated.
    These views remain for backward compatibility only.
"""

from refine.schema import SCHEMA_NAME

# NDC hyphenation patterns. PostgreSQL substr is 1-based.
_NDC_HYPHENATE = {
    "5-4-2": "substr(n.ndc_upc_hri, 1, 5) || '-' || substr(n.ndc_upc_hri, 6, 4) || '-' || substr(n.ndc_upc_hri, 10, 2)",
    "4-6": "substr(n.ndc_upc_hri, 1, 4) || '-' || substr(n.ndc_upc_hri, 5, 6)",
    "5-5": "substr(n.ndc_upc_hri, 1, 5) || '-' || substr(n.ndc_upc_hri, 6, 5)",
}
_DEFAULT_NDC_FMT = _NDC_HYPHENATE["5-4-2"]


def _ndc_formatted_expr() -> str:
    """CASE expression for display NDC from id_number_format_code (H054)."""
    whens = [
        "WHEN n.id_number_format_code = '1' THEN " + _NDC_HYPHENATE["5-4-2"],
        "WHEN n.id_number_format_code = '2' THEN " + _NDC_HYPHENATE["5-4-2"],
        "WHEN n.id_number_format_code = '3' THEN " + _NDC_HYPHENATE["5-4-2"],
        "WHEN n.id_number_format_code = '4' THEN " + _NDC_HYPHENATE["4-6"],
        "WHEN n.id_number_format_code = '5' THEN " + _NDC_HYPHENATE["5-5"],
        "WHEN n.id_number_format_code = '6' THEN " + _NDC_HYPHENATE["5-4-2"],
    ]
    return f"CASE {' '.join(whens)} ELSE {_DEFAULT_NDC_FMT} END"


def get_v_ndc_pcip_reference_sql() -> str:
    """SQL for medfile.v_ndc_pcip_reference: NDC + GPI + latest AWP + specialty/maintenance flags."""
    ndc_fmt = _ndc_formatted_expr()
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_ndc_pcip_reference AS
SELECT
  n.ndc_upc_hri,
  {ndc_fmt} AS ndc_formatted,
  n.drug_descriptor_id,
  n.tee_code,
  n.dea_class_code,
  n.multi_source_code,
  n.name_type_code,
  n.gppc_code,
  g.generic_product_identifier AS gpi,
  n.dollar_rank_code,
  n.rx_rank_code,
  n.limited_distribution_code,
  n.item_status_flag,
  (
    SELECT p.unit_price
    FROM {SCHEMA_NAME}.refinement_ndc_price p
    WHERE p.ndc_upc_hri = n.ndc_upc_hri
      AND p.price_code = 'A'
      AND p.is_active = true
    ORDER BY p.price_effective_date DESC
    LIMIT 1
  ) AS latest_awp_unit_price,
  nm.maintenance_drug_code,
  CASE
    WHEN n.dollar_rank_code IS NOT NULL AND trim(n.dollar_rank_code) <> '' THEN true
    WHEN n.rx_rank_code IS NOT NULL AND trim(n.rx_rank_code) <> '' THEN true
    WHEN n.limited_distribution_code IS NOT NULL AND trim(n.limited_distribution_code) <> '' THEN true
    ELSE false
  END AS specialty_proxy
FROM {SCHEMA_NAME}.refinement_ndc n
LEFT JOIN {SCHEMA_NAME}.refinement_gppc g
  ON g.gppc_code = n.gppc_code AND g.is_current = true
LEFT JOIN {SCHEMA_NAME}.refinement_name nm
  ON nm.drug_descriptor_id = n.drug_descriptor_id AND nm.is_current = true
WHERE n.is_current = true
""".strip()


def get_v_gpi_equivalents_sql() -> str:
    """SQL for medfile.v_gpi_equivalents: (GPI, NDC) substitution candidates.

    Full 14-char GPI, multi_source in ('Y','O'), TEE like 'A%' excluding A1–A4.
    Excludes partial GPIs (tc_gpi_name contains '*' in TC-GPI Name file).
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_gpi_equivalents AS
SELECT
  g.generic_product_identifier AS gpi,
  n.ndc_upc_hri AS ndc
FROM {SCHEMA_NAME}.refinement_ndc n
JOIN {SCHEMA_NAME}.refinement_gppc g
  ON g.gppc_code = n.gppc_code AND g.is_current = true
JOIN {SCHEMA_NAME}.refinement_tcgpi t
  ON t.tc_gpi_key = g.generic_product_identifier
  AND t.is_current = true
  AND t.tc_gpi_name NOT LIKE '%*%'
WHERE n.is_current = true
  AND n.multi_source_code IN ('Y', 'O')
  AND n.tee_code LIKE 'A%'
  AND n.tee_code NOT IN ('A1', 'A2', 'A3', 'A4')
""".strip()


def get_v_drg_maintenance_sql() -> str:
    """SQL for medfile.v_drg_maintenance: DDID (drug_descriptor_id) + maintenance_drug_code.

    Valid values (per manual): 0=Undetermined, 1=Not a Maintenance Drug, 2=Maintenance Drug.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_drg_maintenance AS
SELECT
  drug_descriptor_id,
  maintenance_drug_code
FROM {SCHEMA_NAME}.refinement_name
WHERE is_current = true
""".strip()


def create_pcip_views(conn) -> None:
    """Create or replace all PCIP reference views in medfile schema."""
    with conn.cursor() as cur:
        cur.execute(get_v_ndc_pcip_reference_sql())
        cur.execute(get_v_gpi_equivalents_sql())
        cur.execute(get_v_drg_maintenance_sql())
    conn.commit()
