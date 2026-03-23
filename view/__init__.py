"""View pipeline: create/refresh medfile views from refinement tables.

Separate process from raw (rxraw) and refine. Run after refinement:

    uv run python -m view

Options:
    --no-pcip   Skip PCIP reference views (v_ndc_pcip_reference, v_gpi_equivalents, v_drg_maintenance).
"""

from view.runner import run_views

__all__ = ["run_views"]
