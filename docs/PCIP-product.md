# PCIP Context

**Role:** Explain why this repo publishes PCIP-oriented reference views without turning the repo into a claims analytics project.

---

## What PCIP Means Here

PCIP stands for **Pharmacy Claims Intelligence Platform**.

In this repo, PCIP is a downstream consumer context, not the full product implementation. The project provides drug-reference data that a separate claims system can use for enrichment and analysis.

For retrospective pharmacy audit use, the intended historical model is monthly: downstream systems should map audit records to the appropriate Medi-Span file month and use the reference state published for that month.

---

## What This Repo Provides for PCIP

The `view` process creates reference outputs that support claims-side use cases such as:

- generic substitution logic
- latest AWP lookup
- maintenance drug identification
- DEA and specialty-related drug attributes
- current NDC, GPPC, and GPI relationships
- future month-keyed drug reference outputs for retrospective audit

Current PCIP-oriented views:

- `medfile.v_ndc_pcip_reference`
- `medfile.v_gpi_equivalents`
- `medfile.v_drg_maintenance`

These views are intended to be consumed by another system or exported into another data platform.

---

## What Stays Out of Scope

This repo does not implement:

- claims ingestion
- claims month-selection rules
- enrollment ingestion
- member-level analytics
- prescriber performance reporting
- pharmacy network analytics
- dashboards or customer-facing reporting

Those belong in a separate claims and analytics project built on top of the reference data from this repo.

---

## Reference Semantics Used by Current Views

The current PCIP-oriented views rely on these MED-File concepts:

- GPI from `medfile.refinement_gppc.generic_product_identifier`
- current NDC attributes from `medfile.refinement_ndc`
- current maintenance drug code from `medfile.refinement_name`
- latest active AWP from `medfile.refinement_ndc_price`
- substitution filtering from `tee_code`, `multi_source_code`, and non-partial GPI logic

The repo deliberately stops at this reference layer. It should publish current and month-keyed reference data, but not claims-side audit logic.

---

## Downstream Examples

A separate claims project could join the reference outputs to pharmacy claims in order to support work such as:

- brand-when-generic-available analysis
- generic fill rate reporting
- payment consistency review
- specialty and maintenance segmentation
- controlled-substance classification

Those outcomes are valid downstream uses, but they are not implemented in this repository.
