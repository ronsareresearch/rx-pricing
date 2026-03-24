"""View pipeline: create/refresh medfile views from refinement tables.

Separate process from raw (rxraw) and refine. Run after refinement:

    uv run python -m view

CLI options are defined in ``view.__main__`` (e.g. ``--refresh-only``, ``--reset``).
"""

from view.runner import run_views

__all__ = ["run_views"]
