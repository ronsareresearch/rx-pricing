"""MF2SUM sequence check: for incrementals (U), volume must equal last_refined_volume + 1."""


class SequenceBreakError(Exception):
    """Raised when an incremental run has volume != last_volume + 1."""

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
    Validate that this run is in sequence.
    - Full (T): always allowed.
    - Incremental (U): volume_number must equal last_refined_volume + 1 (or first run).
    Raises SequenceBreakError if invalid.
    """
    if file_type == "T":
        return
    if file_type != "U":
        raise SequenceBreakError(f"Invalid file_type: {file_type!r}. Expected T or U.")
    vol = (volume_number or "").strip()
    if last_refined_volume is None:
        # First run must be full (T). If we get U with no previous run, that's a sequence break.
        raise SequenceBreakError(
            "Incremental run (U) has no prior refined run. Refine a full load (T) first."
        )
    try:
        last_num = int(last_refined_volume)
        expected = str(last_num + 1)
    except ValueError:
        expected = None
    if expected is not None and vol != expected:
        raise SequenceBreakError(
            f"Sequence break: expected volume {expected} (last was {last_refined_volume}), got {vol!r}. "
            "See operations.md §2."
        )
