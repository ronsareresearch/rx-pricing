"""DDL for medfile schema: refine_runs + one table per refinement entity (from load order and rules)."""

from refine.load_order import get_load_order
from refine.rule_engine import load_rules

SCHEMA_NAME = "medfile"


def _col_type_sql(col: dict) -> str:
    """Map YAML column type to PostgreSQL type."""
    t = col.get("type", "varchar(255)")
    if isinstance(t, str) and t.upper() in ("INTEGER", "INT", "SMALLINT", "BIGINT", "DATE"):
        return t.upper()
    if isinstance(t, str) and t.startswith("varchar"):
        return t.upper()
    if isinstance(t, str) and t.startswith("char"):
        return t.upper()
    if isinstance(t, str) and t.startswith("decimal"):
        return t.upper()
    return "VARCHAR(255)"


def _table_columns_from_rules(entity: str) -> list[tuple[str, str]]:
    """Return list of (name, sql_type) from entity rules columns."""
    rules = load_rules(entity)
    return [(c["name"], _col_type_sql(c)) for c in rules["columns"]]


def _ddl_for_entity(entity: str) -> str:
    """Generate CREATE TABLE (+ index) for one entity from its rules. Raises if rules missing."""
    rules = load_rules(entity)
    target_table = rules["target_table"]
    history_type = (rules.get("history_type") or "scd2").strip().lower()
    columns = rules["columns"]
    col_defs = ", ".join(f"{c['name']} {_col_type_sql(c)}" for c in columns)
    source_file = rules.get("source_file", "MF2FILE")
    business_key = rules.get("business_key") or []

    if history_type == "replace":
        pk_cols = ", ".join(business_key)
        return f"""
CREATE TABLE IF NOT EXISTS {target_table} (
    {col_defs},
    run_id              UUID NOT NULL,
    PRIMARY KEY ({pk_cols})
);
"""
    if history_type == "scd2":
        bk_index_cols = ", ".join(business_key + ["is_current"])
        return f"""
CREATE TABLE IF NOT EXISTS {target_table} (
    id                      BIGSERIAL PRIMARY KEY,
    {col_defs},
    run_id                  UUID NOT NULL,
    issue_date              DATE NOT NULL,
    source_file             VARCHAR(30) NOT NULL DEFAULT '{source_file}',
    is_current              BOOLEAN NOT NULL DEFAULT true,
    effective_start_date    DATE NOT NULL,
    effective_end_date      DATE,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_{target_table.split('.')[-1]}_bk ON {target_table} ({bk_index_cols});
"""
    # append_only (e.g. ndc_price, gpr)
    bk_index_cols = ", ".join(business_key)
    return f"""
CREATE TABLE IF NOT EXISTS {target_table} (
    id                      BIGSERIAL PRIMARY KEY,
    {col_defs},
    run_id                  UUID NOT NULL,
    issue_date              DATE NOT NULL,
    source_file             VARCHAR(30) NOT NULL DEFAULT '{source_file}',
    is_active               BOOLEAN NOT NULL DEFAULT true,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_{target_table.split('.')[-1]}_bk ON {target_table} ({bk_index_cols});
"""


def get_ddl() -> str:
    """Full DDL: CREATE SCHEMA medfile + refine_runs + one table per entity in load order."""
    parts = [
        f"""
CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME};

CREATE TABLE IF NOT EXISTS {SCHEMA_NAME}.refine_runs (
    run_id              UUID NOT NULL PRIMARY KEY,
    file_id             UUID NOT NULL,
    file_type           CHAR(1) NOT NULL,
    file_date           DATE NOT NULL,
    volume_number       VARCHAR(10) NOT NULL,
    supplement_number   VARCHAR(10) NOT NULL DEFAULT '',
    status              VARCHAR(20) NOT NULL DEFAULT 'in_progress',
    started_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at        TIMESTAMPTZ
);
"""
    ]
    for entity in get_load_order():
        try:
            parts.append(_ddl_for_entity(entity))
        except FileNotFoundError:
            continue
    return "\n".join(p.strip() for p in parts).strip()


def drop_schema_ddl() -> str:
    """Return DROP SCHEMA ... CASCADE for medfile."""
    return f"DROP SCHEMA IF EXISTS {SCHEMA_NAME} CASCADE"
