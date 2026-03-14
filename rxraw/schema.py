"""
Raw table DDL for schema rxraw. Each table: file_id, file_date, source_file, line_number, volume_number, supplement_number, pos1..pos80.
"""

SCHEMA_NAME = "rxraw"
RAW_POS_COUNT = 80

# Data dictionary: load once (not per run)
DICT_SOURCE_FILE = "MF2DICT"

RAW_SOURCE_FILES = (
    "MF2SUM",  # control/summary – raw load like all others
    "MF2VAL", "MF2NAME", "MF2TCGPI", "MF2NDC", "MF2LAB", "MF2GPPC", "MF2ERR", "MF2GPR", "MF2PRC",
    "MF2MOD", "MF2NDCM", "MF2DRGNM", "MF2RTDRG", "MF2DFDRG", "MF2RTDF", "MF2DRG", "MF2DESC", "MF2RTE",
    "MF2FRM", "MF2STUOM", "MF2SET", "MF2INGS", "MF2STR", "MF2IDRG", "MF2SEC", "MF2RNM",
)


def raw_table_name(source_file: str) -> str:
    """e.g. MF2NDC -> raw_mf2ndc."""
    return f"raw_{source_file.lower()}"


def get_raw_ddl() -> str:
    """Full DDL: CREATE SCHEMA rxraw + all raw_* tables with file_id, file_date, source_file."""
    pos_defs = ", ".join(f"pos{i} TEXT" for i in range(1, RAW_POS_COUNT + 1))
    parts = [f"""
-- Rxraw: MED-File v2 raw tables (file_id, file_date, source_file)
CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME};
-- Track loaded runs to prevent duplicate loads (one row per run)
CREATE TABLE IF NOT EXISTS {SCHEMA_NAME}.loaded_runs (
    file_id           UUID NOT NULL PRIMARY KEY,
    file_date         DATE NOT NULL,
    volume_number     VARCHAR(10) NOT NULL,
    supplement_number VARCHAR(10) NOT NULL DEFAULT '',
    loaded_at         TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX IF NOT EXISTS ix_loaded_runs_file_date_volume ON {SCHEMA_NAME}.loaded_runs (file_date, volume_number);
"""]

    # MF2DICT: data dictionary, load once (same structure as other raw_*)
    dict_table = raw_table_name(DICT_SOURCE_FILE)
    parts.append(f"""
CREATE TABLE IF NOT EXISTS {SCHEMA_NAME}.{dict_table} (
    file_id           UUID NOT NULL,
    file_date         DATE NOT NULL,
    source_file       VARCHAR(30) NOT NULL DEFAULT '{DICT_SOURCE_FILE}',
    line_number       BIGINT NOT NULL,
    volume_number     VARCHAR(10) NOT NULL DEFAULT '',
    supplement_number VARCHAR(10) NOT NULL DEFAULT '',
    {pos_defs}
);
CREATE INDEX IF NOT EXISTS ix_{dict_table}_file_id ON {SCHEMA_NAME}.{dict_table} (file_id);
""")

    for source_file in RAW_SOURCE_FILES:
        table = raw_table_name(source_file)
        default_src = f"DEFAULT '{source_file}'"
        parts.append(f"""
CREATE TABLE IF NOT EXISTS {SCHEMA_NAME}.{table} (
    file_id           UUID NOT NULL,
    file_date         DATE NOT NULL,
    source_file       VARCHAR(30) NOT NULL {default_src},
    line_number       BIGINT NOT NULL,
    volume_number     VARCHAR(10) NOT NULL DEFAULT '',
    supplement_number VARCHAR(10) NOT NULL DEFAULT '',
    {pos_defs}
);
CREATE INDEX IF NOT EXISTS ix_{table}_file_id ON {SCHEMA_NAME}.{table} (file_id);
CREATE INDEX IF NOT EXISTS ix_{table}_file_date_source ON {SCHEMA_NAME}.{table} (file_date, source_file);
""")
    return "\n".join(p.strip() for p in parts).strip()
