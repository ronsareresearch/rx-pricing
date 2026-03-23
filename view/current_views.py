"""Normalized current-state reference views.

These views provide the canonical current reference surface for the end product.
They replace the consumer role of the legacy entity views (v_ndc, v_ndc_price)
and the PCIP reference view (v_ndc_pcip_reference).

All current views filter with is_current = true (SCD2) or is_active = true
(append_only) and expose stable semantic columns rather than SELECT *.
"""

from refine.schema import SCHEMA_NAME

_NDC_HYPHENATE = {
    "5-4-2": "substr(n.ndc_upc_hri, 1, 5) || '-' || substr(n.ndc_upc_hri, 6, 4) || '-' || substr(n.ndc_upc_hri, 10, 2)",
    "4-6": "substr(n.ndc_upc_hri, 1, 4) || '-' || substr(n.ndc_upc_hri, 5, 6)",
    "5-5": "substr(n.ndc_upc_hri, 1, 5) || '-' || substr(n.ndc_upc_hri, 6, 5)",
}
_DEFAULT_NDC_FMT = _NDC_HYPHENATE["5-4-2"]


def _ndc_formatted_expr() -> str:
    whens = [
        "WHEN n.id_number_format_code = '1' THEN " + _NDC_HYPHENATE["5-4-2"],
        "WHEN n.id_number_format_code = '2' THEN " + _NDC_HYPHENATE["5-4-2"],
        "WHEN n.id_number_format_code = '3' THEN " + _NDC_HYPHENATE["5-4-2"],
        "WHEN n.id_number_format_code = '4' THEN " + _NDC_HYPHENATE["4-6"],
        "WHEN n.id_number_format_code = '5' THEN " + _NDC_HYPHENATE["5-5"],
        "WHEN n.id_number_format_code = '6' THEN " + _NDC_HYPHENATE["5-4-2"],
    ]
    return f"CASE {' '.join(whens)} ELSE {_DEFAULT_NDC_FMT} END"


def get_v_product_package_current_sql() -> str:
    """SQL for v_product_package_current.

    Grain: one row per ndc_upc_hri.
    Canonical current packaged-drug reference surface. Replaces the consumer
    role of v_ndc and v_ndc_pcip_reference.
    """
    ndc_fmt = _ndc_formatted_expr()
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_product_package_current AS
SELECT
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
FROM {SCHEMA_NAME}.refinement_ndc n
LEFT JOIN {SCHEMA_NAME}.refinement_name nm
    ON nm.drug_descriptor_id = n.drug_descriptor_id AND nm.is_current = true
LEFT JOIN {SCHEMA_NAME}.refinement_gppc g
    ON g.gppc_code = n.gppc_code AND g.is_current = true
LEFT JOIN {SCHEMA_NAME}.refinement_lab lab
    ON lab.labeler_id = n.labeler_id AND lab.is_current = true
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
WHERE n.is_current = true
""".strip()


def get_v_product_package_price_current_sql() -> str:
    """SQL for v_product_package_price_current.

    Grain: one row per (ndc_upc_hri, price_code).
    Latest active price per NDC and price type. Replaces the consumer role
    of v_ndc_price.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_product_package_price_current AS
SELECT
    p.ndc_upc_hri,
    p.price_code,
    pricecode.value_description AS price_code_desc,
    p.price_effective_date,
    p.unit_price,
    p.unit_price_extended,
    p.package_price,
    p.awp_indicator_code,
    awp.value_description AS awp_indicator_desc
FROM (
    SELECT
        rp.ndc_upc_hri,
        rp.price_code,
        rp.price_effective_date,
        rp.unit_price,
        rp.unit_price_extended,
        rp.package_price,
        rp.awp_indicator_code,
        row_number() OVER (
            PARTITION BY rp.ndc_upc_hri, rp.price_code
            ORDER BY rp.price_effective_date DESC, rp.issue_date DESC, rp.id DESC
        ) AS rn
    FROM {SCHEMA_NAME}.refinement_ndc_price rp
    WHERE rp.is_active = true
) p
LEFT JOIN {SCHEMA_NAME}.mf2val pricecode
    ON pricecode.field_id = 'M012' AND pricecode.field_value = p.price_code AND pricecode.language_cd = '01'
LEFT JOIN {SCHEMA_NAME}.mf2val awp
    ON awp.field_id = 'M055' AND awp.field_value = p.awp_indicator_code AND awp.language_cd = '01'
WHERE p.rn = 1
""".strip()


def get_v_product_package_modifier_current_sql() -> str:
    """SQL for v_product_package_modifier_current.

    Grain: one row per (ndc_upc_hri, modifier_code).
    Current modifier attachments for packaged drug records.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_product_package_modifier_current AS
SELECT
    ndcm.ndc_upc_hri,
    ndcm.modifier_code,
    m.modifier_description
FROM {SCHEMA_NAME}.refinement_ndcm ndcm
JOIN {SCHEMA_NAME}.refinement_mod m
    ON m.modifier_code = ndcm.modifier_code AND m.is_current = true
WHERE ndcm.is_current = true
""".strip()


def create_current_views(conn) -> None:
    """Create or replace all normalized current-state views."""
    with conn.cursor() as cur:
        cur.execute(get_v_product_package_current_sql())
        cur.execute(get_v_product_package_price_current_sql())
        cur.execute(get_v_product_package_modifier_current_sql())
    conn.commit()
