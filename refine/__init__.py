"""Refine ETL: read from rxraw.raw_*, write to medfile schema (tables only). Views are a separate process (python -m view)."""

from refine.schema import SCHEMA_NAME

__all__ = ["SCHEMA_NAME"]
