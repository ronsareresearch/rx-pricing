"""Load YAML rules and apply column mapping with casts. No DB dependency."""

from pathlib import Path
from typing import Any

import yaml

from refine.casting import (
    str_strip,
    to_bigint,
    to_date,
    to_decimal,
    to_int,
)


def _rules_dir() -> Path:
    """Directory containing rules/*.yaml (next to this package)."""
    return Path(__file__).resolve().parent / "rules"


def load_rules(entity: str) -> dict[str, Any]:
    """Load refine/rules/{entity}.yaml. Returns parsed config dict."""
    path = _rules_dir() / f"{entity}.yaml"
    if not path.is_file():
        raise FileNotFoundError(f"Rules file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_common_rules() -> dict[str, Any]:
    """Load refine/rules/common.yaml (formatting rules)."""
    path = _rules_dir() / "common.yaml"
    if not path.is_file():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _get_caster(cast_name: str, decimal_places: int | None = None):
    """Return a callable that takes (val) and returns cast value."""
    if cast_name == "str":
        return lambda v: str_strip(v)
    if cast_name == "int":
        return lambda v: to_int(v)
    if cast_name == "bigint":
        return lambda v: to_bigint(v)
    if cast_name == "date_yyyymmdd":
        return lambda v: to_date(v)
    if cast_name == "implied_decimal":
        places = decimal_places if decimal_places is not None else 0
        return lambda v: to_decimal(v, places)
    raise ValueError(f"Unknown cast: {cast_name}")


def apply_column_map(raw_row: dict[str, Any], columns: list[dict]) -> dict[str, Any]:
    """
    Convert a raw row (keys: pos1, pos2, ... and optionally file_id, file_date, etc.)
    to a dict of named, typed columns per the YAML columns list.
    """
    result: dict[str, Any] = {}
    for col in columns:
        pos = col["pos"]
        key = f"pos{pos}"
        raw_val = raw_row.get(key) if isinstance(raw_row, dict) else None
        cast_name = col.get("cast", "str")
        decimal_places = col.get("decimal_places")
        caster = _get_caster(cast_name, decimal_places)
        result[col["name"]] = caster(raw_val)
    return result
