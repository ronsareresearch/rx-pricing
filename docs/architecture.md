# Architecture

**Role:** Single source of truth for the `rx-pricing` project: what it is, how it works, and what it produces.

---

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
- Drug reference views intended for pharmacy-claims analytics and other downstream consumers

This repo does not own:

- Claims ingestion or claims month-selection rules
- Enrollment ingestion
- PHI or PII workflows
- Claims fact tables, analytics marts, dashboards, or customer reporting

---

## Design Principles

| Principle | Meaning in this repo |
|-----------|----------------------|
| History is preserved | Raw data stays vendor-faithful, and refined history is modeled explicitly. |
| Processes stay separate | Raw ingestion, refinement, and view creation are separate commands and codepaths. |
| Schema is code-driven | Refinement tables and view logic are generated from repo-managed rules and SQL builders. |
| MED-File semantics stay explicit | Translation, casts, and code lookups are documented and implemented from vendor definitions. |
| Downstream scope stays narrow | This repo publishes reference data, not claims analytics products. |

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

Process boundaries:

- `rxraw` discovers runs and writes raw tables only.
- `refine` reads raw runs and writes refinement tables only.
- `view` reads refined tables and creates views only.

---

## Data Layers

### Raw layer: `rxraw`

- One run is one directory that contains `MF2SUM`.
- Raw tables use a common shape: `file_id`, `file_date`, `source_file`, `line_number`, `volume_number`, `supplement_number`, and `pos1` through `pos80`.
- `rxraw.loaded_runs` is the run registry.
- Duplicate runs are skipped by `(file_date, volume_number)`.
- If a run was partially loaded, `rxraw` reuses the existing `file_id` and continues that run instead of duplicating it.

### Refinement layer: `medfile`

- `medfile.refine_runs` tracks refinement status per loaded run.
- `medfile.mf2val` is the translation table.
- 26 entity tables are populated from `refine/rules/*.yaml`.
- History behavior is rule-driven:
  - `replace` for tables such as `mf2val`
  - `scd2` for current plus history entities (indexed on business key + `is_current` and business key + temporal dates)
  - `append_only` for price-style history tables and the error correction audit trail
- Entity load order is defined in `refine/load_order.py`.
- Entity mappings and casts are driven by `refine/rules/*.yaml`.
- Performance indexes on source tables are ensured by the view runner before view creation or refresh.

### View layer: `medfile`

- Regular views are organized into five domain families plus an error corrections audit view. All are recreated on each run.
- Monthly views are **materialized views** populated with `WITH DATA` and refreshed with `REFRESH MATERIALIZED VIEW CONCURRENTLY` so UI reads are never blocked during refresh.
- Each materialized view has a unique index (required for concurrent refresh) plus query-oriented indexes for interactive use (NDC lookup, GPI lookup, month filtering, drug name search).
- Use `uv run python -m view --refresh-only` after incremental refine runs to refresh materialized views without recreating regular views.
- Use `uv run python -m view --reset` to drop and recreate materialized views from scratch.
- The view runner maintains a registry of managed views and drops orphaned views (both regular and materialized) on each run.

---

## Run Semantics

### Run discovery

- `rxraw` finds every directory under `DATA_DIR` that contains `MF2SUM`.
- Runs are sorted with one full file (`T`) first and then incrementals (`U`) by volume.
- If no valid `MF2SUM` is found, `rxraw` falls back to a single synthetic full run from `DATA_DIR`. That behavior is useful for local recovery but should not be the normal production path.

### File-month semantics

- One Medi-Span delivery corresponds to one monthly reference state.
- Historical audit use should be keyed to the Medi-Span file month, not to claim-date logic implemented inside this repository.
- External audit or claims systems can decide whether `paid_date`, `processed_date`, or another business date maps to that month.
- This repo should publish month-keyed reference views; it should not own claims-side month-selection logic.

### Refinement sequencing

- A full file (`T`) is always allowed.
- An incremental file (`U`) requires a prior refined run.
- Current refine validation allows:
  - normal sequencing: current volume equals last volume plus one
  - gap loads: current volume is greater than last volume plus one
  - backfills: current volume is less than or equal to the last refined volume

That behavior is implemented in `refine/validate.py`.

### Failure recovery

- Raw data is treated as immutable once loaded.
- If refinement fails partway through a run, clean failed-run data with `uv run python -m refine --clean-failed` before re-running `refine`.
- Views can be recreated independently after refinement completes.

---

## Implemented Database Surface

| Schema | Objects |
|--------|---------|
| `rxraw` | `loaded_runs` and 28 raw tables |
| `medfile` | `refine_runs`, `mf2val`, 26 refinement tables, 22 regular views, and 6 materialized views |

### Normalized current views

| View | Grain | Purpose |
|------|-------|---------|
| `medfile.v_product_package_current` | `ndc_upc_hri` | Canonical current packaged-drug reference with identity, packaging, labeler, classifications, and specialty proxy |
| `medfile.v_product_package_price_current` | `(ndc_upc_hri, price_code)` | Latest active price per NDC and price type (AWP, WAC, DP, etc.) |
| `medfile.v_product_package_modifier_current` | `(ndc_upc_hri, modifier_code)` | Current modifier attachments for packaged drug records |

### Price history view

| View | Grain | Purpose |
|------|-------|---------|
| `medfile.v_product_package_price_history` | `(ndc_upc_hri, price_code, price_effective_date)` | Full active price history surface with decoded descriptions |

### GPI and equivalence views

| View | Grain | Purpose |
|------|-------|---------|
| `medfile.v_gpi_current` | `gpi` | Current GPI classification with TC-GPI hierarchy name |
| `medfile.v_gppc_current` | `gppc_code` | Current packaging-level reference between NDC and GPI |
| `medfile.v_gpi_ndc_equivalent_current` | `(gpi, ndc_upc_hri)` | Current generic-equivalence candidate set with eligibility flags |

### Clinical concept hierarchy views

| View | Grain | Purpose |
|------|-------|---------|
| `medfile.v_drug_name_current` | `(concept_type, country_code, concept_id)` | Drug name concept layer with description |
| `medfile.v_routed_drug_current` | `(concept_type, country_code, concept_id)` | Routed drug with drug name and route enrichment |
| `medfile.v_drug_dose_form_current` | `(concept_type, country_code, concept_id)` | Drug-dose-form with drug name and form descriptions |
| `medfile.v_routed_drug_form_current` | `(concept_type, country_code, concept_id)` | Routed-drug-form with routed drug and form descriptions |
| `medfile.v_dispensable_drug_current` | `(concept_type, country_code, concept_id)` | Dispensable drug (DDID) with hierarchy enrichment |
| `medfile.v_dispensable_drug_rollup_current` | `(concept_type, country_code, concept_id)` | Flattened hierarchy from drug name through dispensable drug |

### Ingredient composition views

| View | Grain | Purpose |
|------|-------|---------|
| `medfile.v_concept_ingredient_set_current` | `(concept_type, country_code, concept_id)` | Concept-to-ingredient-set mapping |
| `medfile.v_ingredient_set_member_current` | `(ingredient_set_id, ingredient_id)` | Ingredient set membership |
| `medfile.v_ingredient_current` | `ingredient_id` | Ingredient reference with drug naming and strength |
| `medfile.v_concept_ingredient_current` | `(concept_type, country_code, concept_id, ingredient_id)` | End-product concept-to-ingredient composition bridge |

### Terminology and alternate-ID views

| View | Grain | Purpose |
|------|-------|---------|
| `medfile.v_code_lookup_current` | `(field_id, field_value, language_cd)` | Reusable code-to-description translation layer |
| `medfile.v_concept_description_current` | `(concept_type, country_code, concept_id, type_code)` | Current concept descriptions |
| `medfile.v_concept_reference_name_current` | `(concept_type, country_code, concept_id)` | Brand-to-generic concept name mapping |
| `medfile.v_alternate_id_current` | `(external_drug_id, alternate_drug_id)` | Alternate-ID crosswalk |

### Error correction audit view

| View | Grain | Purpose |
|------|-------|---------|
| `medfile.v_error_corrections` | `(key_identifier, unique_key, data_element_code, run_id)` | Audit trail of MF2ERR data entry revision flags with decoded entity types and run metadata |

### Monthly historical views (materialized)

All monthly views are materialized and refreshed concurrently for UI-ready query performance.

| View | Unique Key | Purpose |
|------|-----------|---------|
| `medfile.v_product_package_monthly` | `(reference_month, ndc_upc_hri)` | Monthly packaged-drug reference keyed by Medi-Span file month |
| `medfile.v_product_package_price_monthly` | `(reference_month, ndc_upc_hri, price_code)` | Monthly benchmark pricing (all price codes) keyed by Medi-Span file month |
| `medfile.v_product_package_price_awp_monthly` | `(reference_month, ndc_upc_hri)` | Monthly AWP (Average Wholesale Price) keyed by Medi-Span file month |
| `medfile.v_product_package_price_wac_monthly` | `(reference_month, ndc_upc_hri)` | Monthly WAC (Wholesale Acquisition Cost) keyed by Medi-Span file month |
| `medfile.v_product_package_price_dp_monthly` | `(reference_month, ndc_upc_hri)` | Monthly DP (Direct Price) keyed by Medi-Span file month |
| `medfile.v_gpi_ndc_equivalent_monthly` | `(reference_month, gpi, ndc_upc_hri)` | Monthly generic-equivalence and substitution candidate set |

Legacy entity views (`v_ndc`, `v_ndc_price`, `v_drg`) and legacy consumer-specific views (`v_ndc_pcip_reference`, `v_gpi_equivalents`, `v_drg_maintenance`) have been removed. Their functionality is fully covered by the normalized view families above. The orphan cleanup mechanism will automatically drop them from the database on the next view run.

Monthly view rule:

- `reference_month` is derived from the Medi-Span file month in `medfile.refine_runs.file_date`
- if multiple completed refine runs exist in the same month, the latest completed run is published for that month
- claims-side selection of `paid_date` versus `processed_date` remains out of scope for this repo

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

## Downstream consumers

This repository delivers **Medi-Span–aligned drug reference** only. **Pharmacy claims ingestion, analytics products, customer UI, and audit workflows** live in **separate systems** (and typically separate repositories). Product requirements and roadmaps for those systems are **not** maintained here.

The `view` process creates reference outputs that downstream systems can use for:

- generic substitution logic
- latest AWP lookup
- maintenance drug identification
- DEA and specialty-related drug attributes
- current NDC, GPPC, and GPI relationships
- month-keyed drug reference outputs for retrospective audit

A separate claims or analytics application joins these reference outputs to pharmacy claims (e.g. brand-when-generic analysis, generic fill rate, payment consistency, specialty segmentation, controlled-substance classification). Those outcomes are valid downstream uses; **they are not implemented in this repository.**

**Integration contract:** Consumers should document view names, grains, and `reference_month` semantics against [schema-validation.md](schema-validation.md), [operations.md](operations.md), and [reference-api-spec.md](reference-api-spec.md) (when using an HTTP API).

---

## Technology Choices

- Language: Python 3.10+
- Package and run tool: `uv`
- Database: PostgreSQL via `psycopg2`
- Config source: environment variables, with `.env` support
- Input source: local filesystem under `DATA_DIR`

Relevant environment variables:

- `EXTERNAL_DATABASE_URL`
- `DATA_DIR`
- `RXRAW_INSERT_BATCH_SIZE`
- `REFINE_INSERT_PAGE_SIZE`

---

## Current Gaps

Not implemented yet:

- A dedicated reference API or export layer — **specification:** [reference-api-spec.md](reference-api-spec.md) and [openapi/medfile-reference-v1.yaml](openapi/medfile-reference-v1.yaml)
- Monthly historical views for the later-phase families (clinical, ingredient, GPI)
- Claims-side enrichment tables and analytics outputs
- Non-reference reporting products built on plan claims data

---

## Project Guardrails

1. Keep this repo focused on MED-File reference data.
2. Keep `rxraw`, `refine`, and `view` as separate processes.
3. Do not add claims storage or claims analytics into this repo.
4. Prefer explicit, durable table design over ad hoc reporting logic.
5. Treat `medfile` tables and views as the source of truth for downstream drug-reference semantics.

---

## Document Map

| Document | Purpose |
|----------|---------|
| [deployment.md](deployment.md) | Production deployment patterns for the batch pipeline, scheduling, env vars, downstream integration (thin API vs DB) |
| [reference-api-spec.md](reference-api-spec.md) | Full HTTP spec for the thin MED-File reference API (not implemented in-repo); [OpenAPI YAML](openapi/medfile-reference-v1.yaml) |
| [operations.md](operations.md) | Run commands, recovery steps, and monitoring guidance |
| [rxraw-pipeline.md](rxraw-pipeline.md) | Raw-ingestion behavior, run discovery, and table shape |
| [schema-validation.md](schema-validation.md) | MED-File coverage, source file inventory, and entity mappings |
| [transformation-specs.md](transformation-specs.md) | Cast and translation rules used during refinement |
| [glossary.md](glossary.md) | Shared MED-File and project terminology |
| [normalized-view-design.md](normalized-view-design.md) | Target architecture for the normalized view layer |
| [med-file-manual.md](med-file-manual.md) | Vendor source reference |
