"""Generate CREATE OR REPLACE VIEW SQL from YAML lookups and derived. Execute against medfile schema.

Not invoked by the refine pipeline. Use in separate view processing once end-product view
requirements are defined (see create_views)."""

from refine.rule_engine import load_common_rules, load_rules
from refine.schema import SCHEMA_NAME

# Map format code pattern to SQL expression (value column, format_code column)
# PostgreSQL substr is 1-based: substr(s, start, length)
NDC_HYPHENATE_SQL = {
    "5-4-2": "substr(r.ndc_upc_hri, 1, 5) || '-' || substr(r.ndc_upc_hri, 6, 4) || '-' || substr(r.ndc_upc_hri, 10, 2)",
    "4-6": "substr(r.ndc_upc_hri, 1, 4) || '-' || substr(r.ndc_upc_hri, 5, 6)",
    "5-5": "substr(r.ndc_upc_hri, 1, 5) || '-' || substr(r.ndc_upc_hri, 6, 5)",
}


def _view_entity_name(entity: str) -> str:
    """ndc -> v_ndc, ndc_price -> v_ndc_price, drg -> v_drg."""
    return f"v_{entity}"


def _base_table_for_entity(entity: str) -> str:
    """Entity to base table (from rules target_table)."""
    rules = load_rules(entity)
    return rules["target_table"]


def _ndc_formatted_sql() -> str:
    """CASE expression for ndc_formatted from common.yaml format_map."""
    common = load_common_rules()
    fr = (common.get("formatting_rules") or {}).get("ndc_hyphenate") or {}
    fmt_map = fr.get("format_map") or {}
    default = fr.get("default") or "5-4-2"
    default_sql = NDC_HYPHENATE_SQL.get(default, NDC_HYPHENATE_SQL["5-4-2"])
    whens = []
    for code, pattern in fmt_map.items():
        sql = NDC_HYPHENATE_SQL.get(pattern, default_sql)
        whens.append(f"WHEN r.id_number_format_code = '{code}' THEN {sql}")
    when_clause = " ".join(whens)
    return f"CASE {when_clause} ELSE {default_sql} END"


def generate_view_sql(entity: str) -> str:
    """
    Generate CREATE OR REPLACE VIEW medfile.v_{entity} AS ...
    Uses lookups and derived from entity YAML; base table from rules.
    """
    rules = load_rules(entity)
    base_table = _base_table_for_entity(entity)
    view_name = f"{SCHEMA_NAME}.{_view_entity_name(entity)}"
    lookups = rules.get("lookups") or []
    derived = rules.get("derived") or []

    select_parts = ["r.*"]
    join_parts = []

    for i, lu in enumerate(lookups):
        field_id = lu["field_id"]
        col = lu["column"]
        desc_col = lu["description_column"]
        alias = f"v_{field_id}_{i}"
        select_parts.append(f"{alias}.value_description AS {desc_col}")
        join_parts.append(
            f"LEFT JOIN {SCHEMA_NAME}.mf2val {alias} "
            f"ON {alias}.field_id = '{field_id}' "
            f"AND {alias}.field_value = r.{col} "
            f"AND {alias}.language_cd = '01'"
        )

    for dr in derived:
        name = dr.get("name")
        rule_name = dr.get("rule")
        if rule_name == "ndc_hyphenate" and name == "ndc_formatted":
            select_parts.append(f"{_ndc_formatted_sql()} AS {name}")

    joins = "\n  ".join(join_parts)
    select_list = ",\n  ".join(select_parts)

    return f"""CREATE OR REPLACE VIEW {view_name} AS
SELECT
  {select_list}
FROM {base_table} r
  {joins}
"""


def create_views(conn, entities: list[str] | None = None) -> None:
    """
    Create or replace views for the given entities (default: ndc, ndc_price, drg).
    """
    if entities is None:
        entities = ["ndc", "ndc_price", "drg"]
    with conn.cursor() as cur:
        for entity in entities:
            sql = generate_view_sql(entity)
            cur.execute(sql)
    conn.commit()
