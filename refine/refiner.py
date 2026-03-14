"""Generic refine logic: replace, SCD2, append_only. Reads from rxraw.raw_* and writes to medfile."""

import logging
from datetime import date
from decimal import Decimal
from uuid import UUID

from psycopg2.extras import execute_values, RealDictCursor

from refine.rule_engine import apply_column_map, load_rules

logger = logging.getLogger(__name__)


def _ensure_date(issue_date: date | str | None) -> date | None:
    """Convert YYYYMMDD string or date to date."""
    if issue_date is None:
        return None
    if isinstance(issue_date, date):
        return issue_date
    s = (issue_date if isinstance(issue_date, str) else str(issue_date)).strip()
    if len(s) != 8:
        return None
    try:
        return date(int(s[:4]), int(s[4:6]), int(s[6:8]))
    except (ValueError, TypeError):
        return None


def _raw_rows(conn, source_table: str, file_id: UUID) -> list[dict]:
    """Fetch all rows from source_table for this file_id. Returns list of dicts (pos1, pos2, ...)."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            f"SELECT * FROM {source_table} WHERE file_id = %s ORDER BY line_number",
            (str(file_id),),
        )
        return [dict(row) for row in cur.fetchall()]


def _serialize_val(v):
    """Convert Python types for psycopg2 (Decimal, date -> str for INSERT)."""
    if v is None:
        return None
    if isinstance(v, Decimal):
        return str(v)
    if isinstance(v, date):
        return v.isoformat()
    return v


def refine_replace(
    conn,
    file_id: UUID,
    file_type: str,
    run_id: UUID,
    entity: str,
) -> int:
    """
    Refine MF2VAL: Full (T) = truncate + insert; Incremental (U) = upsert by PK.
    Returns number of rows written.
    """
    rules = load_rules(entity)
    source_table = rules["source_table"]
    target_table = rules["target_table"]
    columns = rules["columns"]
    target_cols = [c["name"] for c in columns] + ["run_id"]

    raw_list = _raw_rows(conn, source_table, file_id)
    if not raw_list:
        logger.info("%s: no raw rows for file_id=%s", entity, file_id)
        return 0

    rows = []
    for raw in raw_list:
        parsed = apply_column_map(raw, columns)
        row_tuple = tuple(_serialize_val(parsed.get(n)) for n in [c["name"] for c in columns])
        rows.append(row_tuple + (str(run_id),))

    with conn.cursor() as cur:
        if file_type == "T":
            cur.execute(f"TRUNCATE TABLE {target_table}")
        cols_str = ", ".join(target_cols)
        updates = ", ".join(f"{c} = EXCLUDED.{c}" for c in ["value_description", "value_abbreviation", "run_id"])
        sql = f"""
            INSERT INTO {target_table} ({cols_str})
            VALUES %s
            ON CONFLICT (field_id, field_value, language_cd)
            DO UPDATE SET {updates}
        """
        execute_values(cur, sql, rows, page_size=5000)
    conn.commit()
    logger.info("%s: refine_replace %s rows into %s", entity, len(rows), target_table)
    return len(rows)


def refine_scd2(
    conn,
    file_id: UUID,
    file_type: str,
    issue_date: date | str,
    run_id: UUID,
    entity: str,
) -> int:
    """
    Refine NDC or DRG: Full = insert all with is_current=true; Incremental = apply A/C/D.
    Returns number of rows inserted.
    """
    rules = load_rules(entity)
    source_table = rules["source_table"]
    target_table = rules["target_table"]
    columns = rules["columns"]
    business_key = rules["business_key"]
    txn_col = rules.get("transaction_cd_column", "transaction_cd")
    source_file = rules.get("source_file", entity.upper())

    issue_d = _ensure_date(issue_date)
    if not issue_d:
        raise ValueError(f"Invalid issue_date for SCD2: {issue_date!r}")

    raw_list = _raw_rows(conn, source_table, file_id)
    if not raw_list:
        logger.info("%s: no raw rows for file_id=%s", entity, file_id)
        return 0

    col_names = [c["name"] for c in columns]
    scd2_cols = ["run_id", "issue_date", "source_file", "is_current", "effective_start_date", "effective_end_date"]
    all_cols = col_names + scd2_cols
    inserted = 0

    with conn.cursor() as cur:
        if file_type == "T":
            rows = []
            for raw in raw_list:
                parsed = apply_column_map(raw, columns)
                vals = [_serialize_val(parsed.get(n)) for n in col_names]
                rows.append(
                    tuple(vals)
                    + (str(run_id), issue_d.isoformat(), source_file, True, issue_d.isoformat(), None)
                )
            if rows:
                execute_values(
                    cur,
                    f"INSERT INTO {target_table} ({', '.join(all_cols)}) VALUES %s",
                    rows,
                    page_size=5000,
                )
                inserted = len(rows)
        else:
            for raw in raw_list:
                parsed = apply_column_map(raw, columns)
                txn = (parsed.get(txn_col) or "").strip().upper()
                bk_vals = [parsed.get(k) for k in business_key]
                if txn == "A":
                    row_tuple = tuple(_serialize_val(parsed.get(n)) for n in col_names)
                    cur.execute(
                        f"""
                        INSERT INTO {target_table} ({', '.join(all_cols)})
                        VALUES ({', '.join(['%s'] * len(col_names))}, %s, %s, %s, true, %s, NULL)
                        """,
                        row_tuple + (str(run_id), issue_d.isoformat(), source_file, issue_d.isoformat()),
                    )
                    inserted += 1
                elif txn == "C":
                    # Close current row(s), then insert new
                    where_parts = " AND ".join(f"{k} = %s" for k in business_key)
                    cur.execute(
                        f"""
                        UPDATE {target_table}
                        SET is_current = false, effective_end_date = %s
                        WHERE {where_parts} AND is_current = true
                        """,
                        [issue_d.isoformat()] + bk_vals,
                    )
                    row_tuple = tuple(_serialize_val(parsed.get(n)) for n in col_names)
                    cur.execute(
                        f"""
                        INSERT INTO {target_table} ({', '.join(all_cols)})
                        VALUES ({', '.join(['%s'] * len(col_names))}, %s, %s, %s, true, %s, NULL)
                        """,
                        row_tuple + (str(run_id), issue_d.isoformat(), source_file, issue_d.isoformat()),
                    )
                    inserted += 1
                elif txn == "D":
                    where_parts = " AND ".join(f"{k} = %s" for k in business_key)
                    cur.execute(
                        f"""
                        UPDATE {target_table}
                        SET is_current = false, effective_end_date = %s
                        WHERE {where_parts} AND is_current = true
                        """,
                        [issue_d.isoformat()] + bk_vals,
                    )

    conn.commit()
    logger.info("%s: refine_scd2 %s rows into %s", entity, inserted, target_table)
    return inserted


def refine_append(
    conn,
    file_id: UUID,
    file_type: str,
    issue_date: date | str,
    run_id: UUID,
    entity: str,
) -> int:
    """
    Refine NDC Price: Full or A/C = insert; D = set is_active=false.
    Returns number of rows inserted.
    """
    rules = load_rules(entity)
    source_table = rules["source_table"]
    target_table = rules["target_table"]
    columns = rules["columns"]
    business_key = rules["business_key"]
    txn_col = rules.get("transaction_cd_column", "transaction_cd")
    source_file = rules.get("source_file", "MF2PRC")

    issue_d = _ensure_date(issue_date)
    if not issue_d:
        raise ValueError(f"Invalid issue_date for append: {issue_date!r}")

    raw_list = _raw_rows(conn, source_table, file_id)
    if not raw_list:
        logger.info("%s: no raw rows for file_id=%s", entity, file_id)
        return 0

    col_names = [c["name"] for c in columns]
    extra_cols = ["run_id", "issue_date", "source_file", "is_active"]
    all_cols = col_names + extra_cols
    inserted = 0

    with conn.cursor() as cur:
        for raw in raw_list:
            parsed = apply_column_map(raw, columns)
            txn = (parsed.get(txn_col) or "").strip().upper()
            if txn == "D":
                # Deactivate by business key
                where_parts = " AND ".join(f"{k} = %s" for k in business_key)
                bk_vals = [_serialize_val(parsed.get(k)) for k in business_key]
                cur.execute(
                    f"UPDATE {target_table} SET is_active = false WHERE {where_parts} AND is_active = true",
                    bk_vals,
                )
            else:
                row_tuple = tuple(_serialize_val(parsed.get(n)) for n in col_names)
                cur.execute(
                    f"""
                    INSERT INTO {target_table} ({', '.join(all_cols)})
                    VALUES ({', '.join(['%s'] * len(col_names))}, %s, %s, %s, true)
                    """,
                    row_tuple + (str(run_id), issue_d.isoformat(), source_file),
                )
                inserted += 1
    conn.commit()
    logger.info("%s: refine_append %s rows into %s", entity, inserted, target_table)
    return inserted
