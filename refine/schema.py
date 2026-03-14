"""DDL for medfile schema: refine_runs, mf2val, refinement_ndc, refinement_ndc_price, refinement_drg."""

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


def get_ddl() -> str:
    """Full DDL: CREATE SCHEMA medfile + all tables and indexes."""
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

    # mf2val
    mf2val_cols = _table_columns_from_rules("mf2val")
    mf2val_defs = ", ".join(f"{n} {sql}" for n, sql in mf2val_cols)
    parts.append(f"""
CREATE TABLE IF NOT EXISTS {SCHEMA_NAME}.mf2val (
    {mf2val_defs},
    run_id              UUID NOT NULL,
    PRIMARY KEY (field_id, field_value, language_cd)
);
""")

    # refinement_ndc: columns from rules + SCD2/provenance
    ndc_cols = _table_columns_from_rules("ndc")
    ndc_defs = ", ".join(f"{n} {sql}" for n, sql in ndc_cols)
    parts.append(f"""
CREATE TABLE IF NOT EXISTS {SCHEMA_NAME}.refinement_ndc (
    id                      BIGSERIAL PRIMARY KEY,
    {ndc_defs},
    run_id                  UUID NOT NULL,
    issue_date              DATE NOT NULL,
    source_file             VARCHAR(30) NOT NULL DEFAULT 'MF2NDC',
    is_current              BOOLEAN NOT NULL DEFAULT true,
    effective_start_date    DATE NOT NULL,
    effective_end_date      DATE,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_refinement_ndc_bk ON {SCHEMA_NAME}.refinement_ndc (ndc_upc_hri, is_current);
""")

    # refinement_ndc_price
    prc_cols = _table_columns_from_rules("ndc_price")
    prc_defs = ", ".join(f"{n} {sql}" for n, sql in prc_cols)
    parts.append(f"""
CREATE TABLE IF NOT EXISTS {SCHEMA_NAME}.refinement_ndc_price (
    id                      BIGSERIAL PRIMARY KEY,
    {prc_defs},
    run_id                  UUID NOT NULL,
    issue_date              DATE NOT NULL,
    source_file             VARCHAR(30) NOT NULL DEFAULT 'MF2PRC',
    is_active               BOOLEAN NOT NULL DEFAULT true,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_refinement_ndc_price_bk ON {SCHEMA_NAME}.refinement_ndc_price (ndc_upc_hri, price_code, price_effective_date);
""")

    # refinement_drg
    drg_cols = _table_columns_from_rules("drg")
    drg_defs = ", ".join(f"{n} {sql}" for n, sql in drg_cols)
    parts.append(f"""
CREATE TABLE IF NOT EXISTS {SCHEMA_NAME}.refinement_drg (
    id                      BIGSERIAL PRIMARY KEY,
    {drg_defs},
    run_id                  UUID NOT NULL,
    issue_date              DATE NOT NULL,
    source_file             VARCHAR(30) NOT NULL DEFAULT 'MF2DRG',
    is_current              BOOLEAN NOT NULL DEFAULT true,
    effective_start_date    DATE NOT NULL,
    effective_end_date      DATE,
    created_at              TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_refinement_drg_bk ON {SCHEMA_NAME}.refinement_drg (concept_type, country_code, concept_id, is_current);
""")

    return "\n".join(p.strip() for p in parts).strip()


def drop_schema_ddl() -> str:
    """Return DROP SCHEMA ... CASCADE for medfile."""
    return f"DROP SCHEMA IF EXISTS {SCHEMA_NAME} CASCADE"
