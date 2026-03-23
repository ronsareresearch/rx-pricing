"""Terminology and alternate-ID helper views (Family 5).

Reusable lookup surfaces for code translations, concept descriptions,
reference name mappings, and alternate-ID crosswalks. These views reduce
duplication in other business-facing views and downstream queries.
"""

from refine.schema import SCHEMA_NAME


def get_v_code_lookup_current_sql() -> str:
    """SQL for v_code_lookup_current.

    Grain: one row per (field_id, field_value, language_cd).
    Thin wrapper over mf2val that provides a stable consumer contract
    for code-to-description translation.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_code_lookup_current AS
SELECT
    field_id,
    field_value,
    language_cd,
    value_description,
    value_abbreviation
FROM {SCHEMA_NAME}.mf2val
""".strip()


def get_v_concept_description_current_sql() -> str:
    """SQL for v_concept_description_current.

    Grain: one row per (concept_type, country_code, concept_id, type_code).
    Current concept descriptions from the Description file (MF2DESC).
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_concept_description_current AS
SELECT
    d.concept_type,
    d.country_code,
    d.concept_id,
    d.type_code,
    d.description
FROM {SCHEMA_NAME}.refinement_desc d
WHERE d.is_current = true
""".strip()


def get_v_concept_reference_name_current_sql() -> str:
    """SQL for v_concept_reference_name_current.

    Grain: one row per (concept_type, country_code, concept_id).
    Maps branded concepts to their generic-named concept ID.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_concept_reference_name_current AS
SELECT
    r.concept_type,
    r.country_code,
    r.concept_id,
    r.id_for_generic_named_drug,
    r.medi_span_reference_flag
FROM {SCHEMA_NAME}.refinement_rnm r
WHERE r.is_current = true
""".strip()


def get_v_alternate_id_current_sql() -> str:
    """SQL for v_alternate_id_current.

    Grain: one row per (external_drug_id, alternate_drug_id).
    Crosswalk between external drug identifiers and their alternates.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_alternate_id_current AS
SELECT
    s.external_drug_id,
    s.external_drug_id_format_code,
    s.alternate_drug_id,
    s.alternate_drug_id_format_code
FROM {SCHEMA_NAME}.refinement_sec s
WHERE s.is_current = true
""".strip()


def create_terminology_views(conn) -> None:
    """Create or replace all terminology and alternate-ID views."""
    with conn.cursor() as cur:
        cur.execute(get_v_code_lookup_current_sql())
        cur.execute(get_v_concept_description_current_sql())
        cur.execute(get_v_concept_reference_name_current_sql())
        cur.execute(get_v_alternate_id_current_sql())
    conn.commit()
