"""Locate and parse MF2SUM (Summary File). No dependency on etl."""

import re
from dataclasses import dataclass, field
from pathlib import Path

from rxraw.parse_utils import is_empty_or_delimiter_only

MF2SUM_NAME = "MF2SUM"
CFT = "CFT"  # Product File Type (T=Total, U=Update)
CDI = "CDI"  # Issue Date
CVL = "CVL"  # Volume Number and Supplement Number
CFF = "CFF"  # Product File Format
TOC = "TOC"  # Table of Contents


@dataclass
class TocEntry:
    part: str
    file_num: str
    file_name: str
    record_count: int


@dataclass
class SummaryInfo:
    file_type: str  # "T" or "U"
    issue_date: str  # YYYYMMDD
    volume_number: str
    supplement_number: str
    file_format: str
    toc: list[TocEntry] = field(default_factory=list)


def find_mf2sum(data_dir: Path) -> Path | None:
    """Path to MF2SUM under data_dir (direct, or one/two levels down)."""
    direct = data_dir / MF2SUM_NAME
    if direct.is_file():
        return direct
    if not data_dir.is_dir():
        return None
    for sub in sorted(data_dir.iterdir()):
        if sub.is_dir():
            candidate = sub / MF2SUM_NAME
            if candidate.is_file():
                return candidate
            for sub2 in sorted(sub.iterdir()):
                if sub2.is_dir():
                    c2 = sub2 / MF2SUM_NAME
                    if c2.is_file():
                        return c2
    return None


def _parse_data_value(line: str) -> tuple[str, str, str] | None:
    parts = line.split("|")
    if len(parts) < 6:
        return None
    rec_type = (parts[0] or "").strip()
    seq = (parts[2] or "").strip()
    comment = (parts[4] or "").strip()
    data = (parts[5] or "").strip()
    if comment == "*" or not rec_type:
        return None
    return (rec_type, seq, data)


def _parse_toc_data(data: str) -> TocEntry | None:
    tokens = data.split()
    if len(tokens) < 4:
        return None
    part, file_num, file_name = tokens[0], tokens[1], tokens[2]
    try:
        rec_count = int(tokens[3])
    except ValueError:
        return None
    return TocEntry(part=part, file_num=file_num, file_name=file_name, record_count=rec_count)


def parse_mf2sum(path: Path) -> SummaryInfo | None:
    """Parse MF2SUM file. Returns SummaryInfo or None."""
    values: dict[str, str] = {}
    toc_entries: list[TocEntry] = []
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.rstrip()
                if is_empty_or_delimiter_only(line):
                    continue
                parsed = _parse_data_value(line)
                if not parsed:
                    continue
                rec_type, seq, data = parsed
                if rec_type == TOC:
                    entry = _parse_toc_data(data)
                    if entry:
                        toc_entries.append(entry)
                else:
                    key = rec_type
                    prev_seq = values.get("_seq_" + key, "")
                    if key not in values or (seq and seq > prev_seq):
                        values[key] = data
                        values["_seq_" + key] = seq
    except OSError:
        return None
    vol_supp = (values.get(CVL) or "").strip()
    vol_match = re.match(r"(\S+)\s+(\S+)", vol_supp)
    if vol_match:
        volume_number, supplement_number = vol_match.group(1).strip(), vol_match.group(2).strip()
    else:
        volume_number = vol_supp
        supplement_number = ""
    return SummaryInfo(
        file_type=(values.get(CFT) or "").strip() or "?",
        issue_date=(values.get(CDI) or "").strip() or "",
        volume_number=volume_number,
        supplement_number=supplement_number,
        file_format=(values.get(CFF) or "").strip() or "?",
        toc=toc_entries,
    )


def find_all_mf2sum_paths(data_dir: Path) -> list[Path]:
    """Find all MF2SUM paths under data_dir (direct, one level down, two levels down)."""
    out: list[Path] = []
    direct = data_dir / MF2SUM_NAME
    if direct.is_file():
        out.append(direct)
    if not data_dir.is_dir():
        return out
    for sub in sorted(data_dir.iterdir()):
        if not sub.is_dir():
            continue
        candidate = sub / MF2SUM_NAME
        if candidate.is_file():
            out.append(candidate)
        for sub2 in sorted(sub.iterdir()):
            if sub2.is_dir():
                c2 = sub2 / MF2SUM_NAME
                if c2.is_file():
                    out.append(c2)
    return out
