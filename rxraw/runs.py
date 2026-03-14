"""Discover MED-File v2 runs: full (T) + incrementals (U) in order. No dependency on etl."""

from dataclasses import dataclass
from pathlib import Path

from rxraw.summary import find_all_mf2sum_paths, parse_mf2sum


@dataclass
class RunInfo:
    """One load run: directory containing MF2SUM and data files."""
    run_dir: Path
    file_type: str  # "T" or "U"
    file_date: str  # YYYYMMDD
    volume_number: str
    supplement_number: str


def discover_runs(data_dir: Path) -> list[RunInfo]:
    """
    Find all runs under data_dir (each run = directory with MF2SUM).
    Returns list sorted: one full (T) first, then all incrementals (U) by volume.
    """
    paths = find_all_mf2sum_paths(data_dir)
    runs: list[RunInfo] = []
    seen_dirs: set[Path] = set()

    for mf2sum_path in paths:
        run_dir = mf2sum_path.parent
        if run_dir in seen_dirs:
            continue
        seen_dirs.add(run_dir)
        summary = parse_mf2sum(mf2sum_path)
        if not summary or summary.file_type not in ("T", "U"):
            continue
        if not summary.issue_date or len(summary.issue_date) != 8:
            continue
        runs.append(RunInfo(
            run_dir=run_dir,
            file_type=summary.file_type,
            file_date=summary.issue_date,
            volume_number=summary.volume_number or "",
            supplement_number=summary.supplement_number or "",
        ))

    # Sort: T first (single full), then U by volume
    def key(r: RunInfo) -> tuple[int, str]:
        # 0 = T first, 1 = U
        order = 0 if r.file_type == "T" else 1
        return (order, r.volume_number)

    runs.sort(key=key)
    return runs
