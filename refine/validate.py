"""MF2SUM sequence check for incrementals (U). Allows normal (last+1), gap (skip missing), and backfill."""

import logging

logger = logging.getLogger(__name__)


class SequenceBreakError(Exception):
    """Raised when validation fails (e.g. U with no prior run, or non-numeric volume)."""

    pass


def get_last_refined_volume(conn) -> str | None:
    """Return the volume_number of the most recently completed refine run, or None if none."""
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT volume_number FROM medfile.refine_runs
            WHERE status = 'done'
            ORDER BY file_date DESC, volume_number DESC
            LIMIT 1
            """
        )
        row = cur.fetchone()
        return row[0] if row else None


def validate_run(file_type: str, volume_number: str, last_refined_volume: str | None) -> None:
    """
    Validate this run. Full (T): always allowed.
    Incremental (U): allowed if (1) normal: volume == last+1, (2) gap: volume > last+1 (missing
    volumes skipped), or (3) backfill: volume <= last (e.g. run 144 loaded later after 145 done).
    Logs gap/backfill; raises SequenceBreakError only for invalid cases (no prior run, non-numeric).
    """
    if file_type == "T":
        return
    if file_type != "U":
        raise SequenceBreakError(f"Invalid file_type: {file_type!r}. Expected T or U.")
    vol = (volume_number or "").strip()
    if last_refined_volume is None:
        raise SequenceBreakError(
            "Incremental run (U) has no prior refined run. Refine a full load (T) first."
        )
    try:
        last_num = int(last_refined_volume)
        vol_num = int(vol)
    except ValueError:
        raise SequenceBreakError(
            f"Volume numbers must be numeric. last_refined={last_refined_volume!r}, current={vol!r}."
        )
    if vol_num == last_num + 1:
        return
    if vol_num > last_num + 1:
        logger.warning(
            "Gap: volume(s) %s..%s missing; refining volume %s (last was %s).",
            last_num + 1,
            vol_num - 1,
            vol,
            last_refined_volume,
        )
        return
    # Backfill: vol_num <= last_num (e.g. refining 144 after 145 already done)
    logger.info(
        "Backfill: refining volume %s (last refined %s).",
        vol,
        last_refined_volume,
    )
