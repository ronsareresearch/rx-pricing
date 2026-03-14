"""Minimal parsing helpers for MED-File v2 pipe-delimited files."""

import re


def is_empty_or_delimiter_only(line: str, delimiter: str = "|") -> bool:
    """True if line is blank, whitespace-only, or only delimiters."""
    if not line:
        return True
    stripped = line.strip()
    if not stripped:
        return True
    pattern = rf"^[\s{re.escape(delimiter)}]*$"
    return bool(re.match(pattern, stripped))
