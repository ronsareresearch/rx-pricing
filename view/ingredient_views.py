"""Ingredient composition views (Family 4).

Models ingredient relationships as their own domain: concept-to-set
mapping, set membership, ingredient reference, and the full
concept-to-ingredient bridge.
"""

from refine.schema import SCHEMA_NAME


def get_v_concept_ingredient_set_current_sql() -> str:
    """SQL for v_concept_ingredient_set_current.

    Grain: one row per (concept_type, country_code, concept_id).
    Maps clinical concepts to their ingredient set ID.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_concept_ingredient_set_current AS
SELECT
    s.concept_type,
    s.country_code,
    s.concept_id,
    s.ingredient_set_id,
    s.representative_set_indicator
FROM {SCHEMA_NAME}.refinement_set s
WHERE s.is_current = true
""".strip()


def get_v_ingredient_set_member_current_sql() -> str:
    """SQL for v_ingredient_set_member_current.

    Grain: one row per (ingredient_set_id, ingredient_id).
    Normalized ingredient-set membership surface.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_ingredient_set_member_current AS
SELECT
    ig.ingredient_set_id,
    ig.ingredient_id,
    ig.active_inactive_flag
FROM {SCHEMA_NAME}.refinement_ings ig
WHERE ig.is_current = true
""".strip()


def get_v_ingredient_current_sql() -> str:
    """SQL for v_ingredient_current.

    Grain: one row per ingredient_id.
    Canonical ingredient reference with drug naming, strength, and volume.
    Joins refinement_str (strength) with refinement_idrg (ingredient drug name).
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_ingredient_current AS
SELECT
    st.ingredient_id,
    idrg.ingredient_drug_name,
    idrg.cas_number,
    idrg.generic_id,
    st.ingredient_drug_id,
    st.ingredient_strength_value,
    st.ingredient_strength_uom_combined,
    st.ingredient_strength_uom_individual,
    st.volume_value,
    st.volume_uom
FROM {SCHEMA_NAME}.refinement_str st
LEFT JOIN {SCHEMA_NAME}.refinement_idrg idrg
    ON idrg.ingredient_drug_id = st.ingredient_drug_id AND idrg.is_current = true
WHERE st.is_current = true
""".strip()


def get_v_concept_ingredient_current_sql() -> str:
    """SQL for v_concept_ingredient_current.

    Grain: one row per (concept_type, country_code, concept_id, ingredient_id).
    End-product ingredient composition bridge: concept -> set -> member -> ingredient.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_concept_ingredient_current AS
SELECT
    s.concept_type,
    s.country_code,
    s.concept_id,
    s.ingredient_set_id,
    ig.ingredient_id,
    ig.active_inactive_flag,
    idrg.ingredient_drug_name,
    idrg.cas_number,
    st.ingredient_strength_value,
    st.ingredient_strength_uom_combined,
    st.ingredient_strength_uom_individual,
    st.volume_value,
    st.volume_uom
FROM {SCHEMA_NAME}.refinement_set s
JOIN {SCHEMA_NAME}.refinement_ings ig
    ON ig.ingredient_set_id = s.ingredient_set_id AND ig.is_current = true
LEFT JOIN {SCHEMA_NAME}.refinement_str st
    ON st.ingredient_id = ig.ingredient_id AND st.is_current = true
LEFT JOIN {SCHEMA_NAME}.refinement_idrg idrg
    ON idrg.ingredient_drug_id = st.ingredient_drug_id AND idrg.is_current = true
WHERE s.is_current = true
""".strip()


def create_ingredient_views(conn) -> None:
    """Create or replace all ingredient composition views."""
    with conn.cursor() as cur:
        cur.execute(get_v_concept_ingredient_set_current_sql())
        cur.execute(get_v_ingredient_set_member_current_sql())
        cur.execute(get_v_ingredient_current_sql())
        cur.execute(get_v_concept_ingredient_current_sql())
    conn.commit()
