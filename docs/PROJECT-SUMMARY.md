# rx-pricing: Project Summary

## Purpose

`rx-pricing` is a MED-File v2 reference-data pipeline.

It does three things:

1. Loads Wolters Kluwer MED-File deliveries into raw PostgreSQL tables.
2. Refines those raw records into durable history-aware `medfile` tables.
3. Publishes reference views that downstream systems can use for drug enrichment.

This repo is not a claims platform. It prepares the drug-reference layer that other systems can consume.

The core historical use case is month-based: downstream consumers should be able to join claims or audit records to the appropriate Medi-Span file month. That month-selection logic belongs outside this repo; this repo publishes the month-keyed reference layer.

---

## Scope

This repo owns:

- MED-File run discovery and raw ingestion
- MED-File refinement into normalized PostgreSQL tables
- Reference views built from refinement tables
- PCIP-oriented drug reference outputs

This repo does not own:

- Claims ingestion
- Enrollment ingestion
- PHI or PII workflows
- Claims fact tables
- Final analytics marts, dashboards, or customer reporting

---

## Runtime Architecture

The project has three separate processes:

| Process | Command | Responsibility |
|---------|---------|----------------|
| `rxraw` | `uv run python -m rxraw` | Load source files into schema `rxraw` |
| `refine` | `uv run python -m refine` | Transform `rxraw` data into history-aware tables in schema `medfile` |
| `view` | `uv run python -m view` | Create or refresh reference views in schema `medfile` |

Data flow:

```text
MED-File delivery -> rxraw -> refine -> view
```

Boundary rules:

- `rxraw` only handles raw ingestion.
- `refine` only handles refinement tables.
- `view` only creates views from refined tables.

---

## Current Implementation

### Raw layer

- Source runs are discovered from directories that contain `MF2SUM`.
- Raw records land in `rxraw.raw_*` tables.
- Run metadata is stored in `rxraw.loaded_runs`.
- Raw tables preserve vendor fidelity with `pos1` through `pos80`.

### Refinement layer

- Refinement tables live in schema `medfile`.
- The pipeline supports `mf2val` plus 25 MED-File entities.
- History handling uses `replace`, `scd2`, or `append_only` depending on the entity rule.
- Entity load order is defined in `refine/load_order.py`.
- Entity mappings and casts are driven by `refine/rules/*.yaml`.

### View layer

- View generation is implemented under `view/`.
- Views are built only from `medfile` refinement tables.
- The view runner supports base entity views and optional PCIP reference views.
- The view runner now also builds monthly normalized views keyed by Medi-Span file month.

---

## Implemented Views

### Entity views

| View | Purpose |
|------|---------|
| `medfile.v_ndc` | Current NDC reference with MF2VAL descriptions and formatted NDC |
| `medfile.v_ndc_price` | Current NDC price reference |
| `medfile.v_drg` | Current dispensable drug reference |

### PCIP-oriented reference views

| View | Purpose |
|------|---------|
| `medfile.v_ndc_pcip_reference` | NDC reference join with GPI, latest AWP, TEE, multi-source, DEA, maintenance, and specialty proxy fields |
| `medfile.v_gpi_equivalents` | Candidate generic-substitution set based on current GPI, TEE, and multi-source logic |
| `medfile.v_drg_maintenance` | Current maintenance-drug mapping by `drug_descriptor_id` |

These are reference views, not claims analytics outputs.

### Monthly historical views

| View | Purpose |
|------|---------|
| `medfile.v_product_package_monthly` | Monthly packaged-drug reference keyed by Medi-Span file month |
| `medfile.v_product_package_price_monthly` | Monthly file-month benchmark pricing keyed by Medi-Span file month |
| `medfile.v_gpi_ndc_equivalent_monthly` | Monthly generic-equivalence and substitution candidate set |

---

## Key MED-File Semantics In Use

- GPI comes from `medfile.refinement_gppc.generic_product_identifier`.
- NDC records link to GPI through `gppc_code`.
- Generic-equivalent logic requires a full 14-character non-partial GPI, `multi_source_code` in `('Y', 'O')`, and `tee_code` that starts with `A` but is not `A1` through `A4`.
- Maintenance drug logic uses `medfile.refinement_name.maintenance_drug_code`.
- The current specialty proxy is derived from `dollar_rank_code`, `rx_rank_code`, and `limited_distribution_code`.
- Current AWP comes from active `medfile.refinement_ndc_price` rows with `price_code = 'A'`.
- The major historical product requirement is month-based reference matching by Medi-Span file month, not claim-date logic inside this repository.

---

## Current Gaps

Not implemented yet:

- MF2ERR correction processing
- A dedicated reference API or export layer
- Claims-side enrichment tables and analytics outputs
- Non-reference reporting products built on plan claims data

---

## Project Guardrails

1. Keep this repo focused on MED-File reference data.
2. Keep `rxraw`, `refine`, and `view` as separate processes.
3. Do not add claims storage or claims analytics into this repo.
4. Prefer explicit, durable table design over ad hoc reporting logic.
5. Treat `medfile` tables and views as the source of truth for downstream drug-reference semantics.
