"""GPI and equivalence views (Family 2).

Therapeutic-class, substitution, and packaging-level reference surfaces.
Separates GPI/GPPC semantics from the NDC master reference.
"""

from refine.schema import SCHEMA_NAME


def get_v_gpi_current_sql() -> str:
    """SQL for v_gpi_current.

    Grain: one row per gpi (14-character Generic Product Identifier).
    Canonical current GPI classification surface with TC-GPI hierarchy names.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_gpi_current AS
SELECT DISTINCT
    g.generic_product_identifier AS gpi,
    tc.tc_gpi_name,
    tc.tc_level_code
FROM {SCHEMA_NAME}.refinement_gppc g
JOIN {SCHEMA_NAME}.refinement_tcgpi tc
    ON tc.tc_gpi_key = g.generic_product_identifier
    AND tc.is_current = true
WHERE g.is_current = true
  AND g.generic_product_identifier IS NOT NULL
  AND trim(g.generic_product_identifier) <> ''
""".strip()


def get_v_gppc_current_sql() -> str:
    """SQL for v_gppc_current.

    Grain: one row per gppc_code.
    Current packaging-level reference between NDC and GPI domains.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_gppc_current AS
SELECT
    g.gppc_code,
    g.generic_product_identifier AS gpi,
    g.package_size,
    g.package_size_uom,
    g.package_quantity,
    g.unit_dose_unit_of_use_code,
    uduu.value_description AS unit_dose_unit_of_use_desc,
    g.package_description_code,
    pkgdesc.value_description AS package_description_desc
FROM {SCHEMA_NAME}.refinement_gppc g
LEFT JOIN {SCHEMA_NAME}.mf2val uduu
    ON uduu.field_id = 'J040' AND uduu.field_value = g.unit_dose_unit_of_use_code AND uduu.language_cd = '01'
LEFT JOIN {SCHEMA_NAME}.mf2val pkgdesc
    ON pkgdesc.field_id = 'J044' AND pkgdesc.field_value = g.package_description_code AND pkgdesc.language_cd = '01'
WHERE g.is_current = true
""".strip()


def get_v_gpi_ndc_equivalent_current_sql() -> str:
    """SQL for v_gpi_ndc_equivalent_current.

    Grain: one row per (gpi, ndc_upc_hri).
    Normalized current generic-equivalence candidate set. Successor to
    the legacy v_gpi_equivalents view.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_gpi_ndc_equivalent_current AS
SELECT
    g.generic_product_identifier AS gpi,
    n.ndc_upc_hri,
    n.tee_code,
    tee.value_description AS tee_desc,
    n.multi_source_code,
    multisource.value_description AS multi_source_desc,
    n.item_status_flag,
    itemstatus.value_description AS item_status_desc,
    CASE
        WHEN length(trim(g.generic_product_identifier)) = 14
             AND trim(g.generic_product_identifier) NOT LIKE '%0000000000'
        THEN true
        ELSE false
    END AS full_gpi,
    CASE
        WHEN n.multi_source_code IN ('Y', 'O')
             AND n.tee_code IS NOT NULL
             AND left(n.tee_code, 1) = 'A'
             AND n.tee_code NOT IN ('A1', 'A2', 'A3', 'A4')
        THEN true
        ELSE false
    END AS generic_equivalent_eligible
FROM {SCHEMA_NAME}.refinement_ndc n
JOIN {SCHEMA_NAME}.refinement_gppc g
    ON g.gppc_code = n.gppc_code AND g.is_current = true
LEFT JOIN {SCHEMA_NAME}.mf2val tee
    ON tee.field_id = 'H018' AND tee.field_value = n.tee_code AND tee.language_cd = '01'
LEFT JOIN {SCHEMA_NAME}.mf2val multisource
    ON multisource.field_id = 'H072' AND multisource.field_value = n.multi_source_code AND multisource.language_cd = '01'
LEFT JOIN {SCHEMA_NAME}.mf2val itemstatus
    ON itemstatus.field_id = 'H074' AND itemstatus.field_value = n.item_status_flag AND itemstatus.language_cd = '01'
WHERE n.is_current = true
  AND g.generic_product_identifier IS NOT NULL
  AND trim(g.generic_product_identifier) <> ''
""".strip()


def create_gpi_views(conn) -> None:
    """Create or replace all GPI and equivalence views."""
    with conn.cursor() as cur:
        cur.execute(get_v_gpi_current_sql())
        cur.execute(get_v_gppc_current_sql())
        cur.execute(get_v_gpi_ndc_equivalent_current_sql())
    conn.commit()
