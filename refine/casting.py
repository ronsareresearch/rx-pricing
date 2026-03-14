"""Casting functions for refinement: dates, integers, implied decimals. Used by rule_engine."""

from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any


def to_date(val: str | None) -> Any:
    """YYYYMMDD string to Python date, or None if invalid/empty."""
    if not val or not isinstance(val, str):
        return None
    s = val.strip()
    if not s or len(s) != 8:
        return None
    try:
        return datetime.strptime(s, "%Y%m%d").date()
    except ValueError:
        return None


def to_int(val: str | None) -> int | None:
    """Strip and parse as int, or None if empty/invalid."""
    if val is None:
        return None
    s = (val.strip() if isinstance(val, str) else str(val)).strip()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        return None


def to_bigint(val: str | None) -> int | None:
    """Same as to_int; Python int handles 64-bit. For BIGINT columns."""
    return to_int(val)


def to_decimal(val: str | None, decimal_places: int = 0) -> Decimal | None:
    """Implied decimal: raw integer string / 10^decimal_places. Returns None if empty/invalid."""
    if val is None:
        return None
    s = (val.strip() if isinstance(val, str) else str(val)).strip()
    if not s:
        return None
    try:
        raw = int(s)
        return Decimal(raw) / (Decimal(10) ** decimal_places)
    except (ValueError, InvalidOperation):
        return None


def str_strip(val: str | None) -> str | None:
    """Strip whitespace; empty string becomes None."""
    if val is None:
        return None
    s = (val if isinstance(val, str) else str(val)).strip()
    return s if s else None
