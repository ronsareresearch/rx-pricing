"""Error correction audit views.

Provides a queryable audit trail of MF2ERR (Error Correct File) records.
Each record flags a data entry revision in another entity file — the view
enriches the raw flags with human-readable entity types and run metadata.
"""

from refine.schema import SCHEMA_NAME


def get_v_error_corrections_sql() -> str:
    """SQL for v_error_corrections.

    Grain: one row per (key_identifier, unique_key, data_element_code, run_id).
    Joins refinement_err with refine_runs to surface run-level context.
    """
    return f"""
CREATE OR REPLACE VIEW {SCHEMA_NAME}.v_error_corrections AS
SELECT
    e.key_identifier,
    CASE e.key_identifier
        WHEN '1' THEN 'Drug Descriptor ID'
        WHEN '2' THEN 'NDC-UPC-HRI'
        WHEN '3' THEN 'NDC-UPC-HRI + Price Type'
        ELSE 'Unknown (' || e.key_identifier || ')'
    END AS entity_type,
    trim(e.unique_key) AS unique_key,
    trim(e.data_element_code) AS data_element_code,
    e.data_element_length,
    r.file_date,
    r.volume_number,
    e.run_id,
    e.issue_date,
    e.created_at
FROM {SCHEMA_NAME}.refinement_err e
JOIN {SCHEMA_NAME}.refine_runs r ON r.run_id = e.run_id
WHERE e.is_active = true
""".strip()


def create_err_views(conn) -> None:
    """Create or replace error correction audit views."""
    with conn.cursor() as cur:
        cur.execute(get_v_error_corrections_sql())
    conn.commit()
