"""View runner: create or replace all medfile views.

Builds current entity views, monthly Medi-Span file-month views, and optional
PCIP reference views from refinement tables only. Run after refine.
"""


def run_views(conn, include_pcip: bool = True) -> None:
    """
    Create or replace all medfile views.

    - Entity views: v_ndc, v_ndc_price, v_drg.
    - Monthly views: v_product_package_monthly, v_product_package_price_monthly,
      v_gpi_ndc_equivalent_monthly.
    - PCIP views (if include_pcip): v_ndc_pcip_reference, v_gpi_equivalents, v_drg_maintenance.
    """
    from view.entity_views import create_entity_views
    from view.monthly_views import create_monthly_views
    from view.pcip_views import create_pcip_views

    create_entity_views(conn, entities=["ndc", "ndc_price", "drg"])
    create_monthly_views(conn)
    if include_pcip:
        create_pcip_views(conn)
