"""Clinical concept hierarchy views (Family 3).

Exposes MED-File clinical concepts at their natural levels: drug name,
routed drug, drug-dose form, routed drug form, and dispensable drug.
Each level has a distinct grain and meaning; downstream consumers should
use concept-appropriate views instead of reconstructing hierarchy joins.
"""

from refine.schema import SCHEMA_NAME


def _desc_lateral(alias: str, concept_alias: str) -> str:
    """LATERAL subquery to pick one description per concept (lowest type_code)."""
    return f"""
LEFT JOIN LATERAL (
    SELECT d.description
    FROM {SCHEMA_NAME}.refinement_desc d
    WHERE d.concept_type = {concept_alias}.concept_type
      AND d.country_code = {concept_alias}.country_code
      AND d.concept_id = {concept_alias}.concept_id
      AND d.is_current = true
    ORDER BY d.type_code
    LIMIT 1
) {alias} ON true"""


def get_v_drug_name_current_sql() -> str:
    """SQL for v_drug_name_current.

    Grain: one row per (concept_type, country_code, concept_id) for drug names.
    Concept type 1 = Drug Name (SDI Drug Name / MF2DRGNM).
    """
    desc_join = _desc_lateral("dn_desc", "dn")
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_drug_name_current AS
SELECT
    dn.concept_type,
    dn.country_code,
    dn.concept_id,
    dn_desc.description AS drug_name,
    dn.name_type,
    dn.status,
    dn.link_value,
    dn.link_date
FROM {SCHEMA_NAME}.refinement_drgnm dn{desc_join}
WHERE dn.is_current = true
""".strip()


def get_v_routed_drug_current_sql() -> str:
    """SQL for v_routed_drug_current.

    Grain: one row per routed drug concept (concept_type=2).
    Enriched with drug name and route descriptions.
    """
    desc_join = _desc_lateral("rt_desc", "rt")
    rte_desc_join = _desc_lateral("rte_desc", "rte")
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_routed_drug_current AS
SELECT
    rt.concept_type,
    rt.country_code,
    rt.concept_id,
    rt_desc.description AS routed_drug_name,
    rt.drug_name_id,
    dn_desc.description AS drug_name,
    rt.route_id,
    rte_desc.description AS route_name,
    rt.status,
    rt.link_value,
    rt.link_date
FROM {SCHEMA_NAME}.refinement_rtdrg rt{desc_join}
LEFT JOIN LATERAL (
    SELECT d.description
    FROM {SCHEMA_NAME}.refinement_desc d
    WHERE d.concept_type = 1
      AND d.country_code = rt.country_code
      AND d.concept_id = rt.drug_name_id
      AND d.is_current = true
    ORDER BY d.type_code
    LIMIT 1
) dn_desc ON true
LEFT JOIN {SCHEMA_NAME}.refinement_rte rte
    ON rte.concept_id = rt.route_id AND rte.is_current = true{rte_desc_join}
WHERE rt.is_current = true
""".strip()


def get_v_drug_dose_form_current_sql() -> str:
    """SQL for v_drug_dose_form_current.

    Grain: one row per drug-dose-form concept (concept_type=221).
    Enriched with drug name and dose form descriptions.
    """
    desc_join = _desc_lateral("df_desc", "df")
    frm_desc_join = _desc_lateral("frm_desc", "frm")
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_drug_dose_form_current AS
SELECT
    df.concept_type,
    df.country_code,
    df.concept_id,
    df_desc.description AS drug_dose_form_name,
    df.drug_name_id,
    dn_desc.description AS drug_name,
    df.dose_form_id,
    frm_desc.description AS dose_form_name,
    df.status,
    df.link_value,
    df.link_date
FROM {SCHEMA_NAME}.refinement_dfdrg df{desc_join}
LEFT JOIN LATERAL (
    SELECT d.description
    FROM {SCHEMA_NAME}.refinement_desc d
    WHERE d.concept_type = 1
      AND d.country_code = df.country_code
      AND d.concept_id = df.drug_name_id
      AND d.is_current = true
    ORDER BY d.type_code
    LIMIT 1
) dn_desc ON true
LEFT JOIN {SCHEMA_NAME}.refinement_frm frm
    ON frm.concept_id = df.dose_form_id AND frm.is_current = true{frm_desc_join}
WHERE df.is_current = true
""".strip()


def get_v_routed_drug_form_current_sql() -> str:
    """SQL for v_routed_drug_form_current.

    Grain: one row per routed-drug-form concept (concept_type=3).
    Enriched with routed drug and dose form descriptions.
    """
    desc_join = _desc_lateral("rtdf_desc", "rtdf")
    frm_desc_join = _desc_lateral("frm_desc", "frm")
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_routed_drug_form_current AS
SELECT
    rtdf.concept_type,
    rtdf.country_code,
    rtdf.concept_id,
    rtdf_desc.description AS routed_drug_form_name,
    rtdf.routed_drug_id,
    rt_desc.description AS routed_drug_name,
    rtdf.dose_form_id,
    frm_desc.description AS dose_form_name,
    rtdf.status,
    rtdf.link_value,
    rtdf.link_date
FROM {SCHEMA_NAME}.refinement_rtdf rtdf{desc_join}
LEFT JOIN LATERAL (
    SELECT d.description
    FROM {SCHEMA_NAME}.refinement_desc d
    WHERE d.concept_type = 2
      AND d.country_code = rtdf.country_code
      AND d.concept_id = rtdf.routed_drug_id
      AND d.is_current = true
    ORDER BY d.type_code
    LIMIT 1
) rt_desc ON true
LEFT JOIN {SCHEMA_NAME}.refinement_frm frm
    ON frm.concept_id = rtdf.dose_form_id AND frm.is_current = true{frm_desc_join}
WHERE rtdf.is_current = true
""".strip()


def get_v_dispensable_drug_current_sql() -> str:
    """SQL for v_dispensable_drug_current.

    Grain: one row per dispensable drug concept (concept_type=4, DDID).
    Enriched with routed drug, dose form, strength, and description lookups.
    """
    desc_join = _desc_lateral("drg_desc", "drg")
    frm_desc_join = _desc_lateral("frm_desc", "frm")
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_dispensable_drug_current AS
SELECT
    drg.concept_type,
    drg.country_code,
    drg.concept_id,
    drg_desc.description AS dispensable_drug_name,
    drg.routed_drug_id,
    rt_desc.description AS routed_drug_name,
    drg.routed_drug_form_id,
    drg.drug_dose_form_id,
    drg.dose_form_id,
    frm_desc.description AS dose_form_name,
    drg.strength,
    drg.strength_uom,
    drg.strength_strength_uom_id,
    drg.name_source,
    drg.device_flag,
    drg.status,
    drg.link_value,
    drg.link_date
FROM {SCHEMA_NAME}.refinement_drg drg{desc_join}
LEFT JOIN LATERAL (
    SELECT d.description
    FROM {SCHEMA_NAME}.refinement_desc d
    WHERE d.concept_type = 2
      AND d.country_code = drg.country_code
      AND d.concept_id = drg.routed_drug_id
      AND d.is_current = true
    ORDER BY d.type_code
    LIMIT 1
) rt_desc ON true
LEFT JOIN {SCHEMA_NAME}.refinement_frm frm
    ON frm.concept_id = drg.dose_form_id AND frm.is_current = true{frm_desc_join}
WHERE drg.is_current = true
""".strip()


def get_v_dispensable_drug_rollup_current_sql() -> str:
    """SQL for v_dispensable_drug_rollup_current.

    Grain: one row per dispensable drug concept (concept_type=4).
    Convenience rollup that flattens the full hierarchy from drug name
    down through routed drug to dispensable drug with all descriptions.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_dispensable_drug_rollup_current AS
SELECT
    drg.concept_type,
    drg.country_code,
    drg.concept_id AS ddid,
    drg_desc.description AS dispensable_drug_name,
    drg.strength,
    drg.strength_uom,
    drg.dose_form_id,
    frm_desc.description AS dose_form_name,
    drg.routed_drug_id,
    rt_desc.description AS routed_drug_name,
    rt.drug_name_id,
    dn_desc.description AS drug_name,
    rt.route_id,
    rte_desc.description AS route_name,
    drg.device_flag,
    drg.status
FROM {SCHEMA_NAME}.refinement_drg drg
LEFT JOIN LATERAL (
    SELECT d.description
    FROM {SCHEMA_NAME}.refinement_desc d
    WHERE d.concept_type = drg.concept_type
      AND d.country_code = drg.country_code
      AND d.concept_id = drg.concept_id
      AND d.is_current = true
    ORDER BY d.type_code LIMIT 1
) drg_desc ON true
LEFT JOIN {SCHEMA_NAME}.refinement_rtdrg rt
    ON rt.concept_id = drg.routed_drug_id AND rt.is_current = true
LEFT JOIN LATERAL (
    SELECT d.description
    FROM {SCHEMA_NAME}.refinement_desc d
    WHERE d.concept_type = 2
      AND d.country_code = drg.country_code
      AND d.concept_id = drg.routed_drug_id
      AND d.is_current = true
    ORDER BY d.type_code LIMIT 1
) rt_desc ON true
LEFT JOIN LATERAL (
    SELECT d.description
    FROM {SCHEMA_NAME}.refinement_desc d
    WHERE d.concept_type = 1
      AND d.country_code = rt.country_code
      AND d.concept_id = rt.drug_name_id
      AND d.is_current = true
    ORDER BY d.type_code LIMIT 1
) dn_desc ON true
LEFT JOIN {SCHEMA_NAME}.refinement_rte rte
    ON rte.concept_id = rt.route_id AND rte.is_current = true
LEFT JOIN LATERAL (
    SELECT d.description
    FROM {SCHEMA_NAME}.refinement_desc d
    WHERE d.concept_type = rte.concept_type
      AND d.country_code = rte.country_code
      AND d.concept_id = rte.concept_id
      AND d.is_current = true
    ORDER BY d.type_code LIMIT 1
) rte_desc ON true
LEFT JOIN {SCHEMA_NAME}.refinement_frm frm
    ON frm.concept_id = drg.dose_form_id AND frm.is_current = true
LEFT JOIN LATERAL (
    SELECT d.description
    FROM {SCHEMA_NAME}.refinement_desc d
    WHERE d.concept_type = frm.concept_type
      AND d.country_code = frm.country_code
      AND d.concept_id = frm.concept_id
      AND d.is_current = true
    ORDER BY d.type_code LIMIT 1
) frm_desc ON true
WHERE drg.is_current = true
""".strip()


def create_clinical_views(conn) -> None:
    """Create or replace all clinical concept hierarchy views."""
    with conn.cursor() as cur:
        cur.execute(get_v_drug_name_current_sql())
        cur.execute(get_v_routed_drug_current_sql())
        cur.execute(get_v_drug_dose_form_current_sql())
        cur.execute(get_v_routed_drug_form_current_sql())
        cur.execute(get_v_dispensable_drug_current_sql())
        cur.execute(get_v_dispensable_drug_rollup_current_sql())
    conn.commit()
