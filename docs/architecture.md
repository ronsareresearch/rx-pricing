# Architecture

**Role:** Current-state architecture for the `rx-pricing` MED-File pipeline.

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

## Runtime Components

| Component | Command | Output |
|-----------|---------|--------|
| `rxraw` | `uv run python -m rxraw` | `rxraw.loaded_runs` plus `rxraw.raw_*` tables |
| `refine` | `uv run python -m refine` | `medfile.refine_runs`, `medfile.mf2val`, and 25 refinement tables |
| `view` | `uv run python -m view` | `medfile` views for entity reference and PCIP-oriented reference outputs |

Data flow:

```text
filesystem MED-File runs -> rxraw -> refine -> view
```

Process boundaries:

- `rxraw` discovers runs and writes raw tables only.
- `refine` reads raw runs and writes tables only.
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
- 25 entity tables are populated from `refine/rules/*.yaml`.
- History behavior is rule-driven:
  - `replace` for tables such as `mf2val`
  - `scd2` for current plus history entities
  - `append_only` for price-style history tables
- The end-product historical requirement is month-based: consumers need reference data tied to the Medi-Span file month, not claims logic inside this repo.

### View layer: `medfile`

- Entity views are created from refined tables through `view/entity_views.py`.
- Monthly normalized views are created from refined tables through `view/monthly_views.py`.
- PCIP-oriented reference views are created through `view/pcip_views.py`.
- The view process can skip PCIP views with `uv run python -m view --no-pcip`.
- The current implementation now includes month-keyed normalized views for retrospective audit.

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

That behavior is implemented in `refine/validate.py` and should be reflected in operational runbooks.

### Failure recovery

- Raw data is treated as immutable once loaded.
- If refinement fails partway through a run, clean failed-run data with `uv run python -m refine --clean-failed` before re-running `refine`.
- Views can be recreated independently after refinement completes.

---

## Implemented Database Surface

| Schema | Objects |
|--------|---------|
| `rxraw` | `loaded_runs` and 28 raw tables |
| `medfile` | `refine_runs`, `mf2val`, 25 refinement tables, and project views |

Current view set:

- `medfile.v_ndc`
- `medfile.v_ndc_price`
- `medfile.v_drg`
- `medfile.v_product_package_monthly`
- `medfile.v_product_package_price_monthly`
- `medfile.v_gpi_ndc_equivalent_monthly`
- `medfile.v_ndc_pcip_reference`
- `medfile.v_gpi_equivalents`
- `medfile.v_drg_maintenance`

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

## Scope Boundary

This architecture intentionally stops at reusable drug reference outputs.

In scope:

- MED-File ingestion
- MED-File refinement
- Reference views for downstream consumers
- Month-keyed historical reference views derived from Medi-Span file months

Out of scope:

- Claims storage
- Claims month selection rules
- Member or enrollment modeling
- PHI or PII handling
- Claims-side analytics marts and dashboards

---

## Document Map

| Document | Purpose |
|----------|---------|
| [PROJECT-SUMMARY.md](PROJECT-SUMMARY.md) | Compact overview of scope, commands, and current outputs |
| [rxraw-pipeline.md](rxraw-pipeline.md) | Raw-ingestion behavior and table shape |
| [schema-validation.md](schema-validation.md) | MED-File coverage and schema inventory |
| [transformation-specs.md](transformation-specs.md) | Cast and translation rules used during refinement |
| [operations.md](operations.md) | Current run commands and recovery procedures |
| [glossary.md](glossary.md) | Shared MED-File and project terminology |
| [PCIP-product.md](PCIP-product.md) | Downstream context for the PCIP-oriented views |
| [med-file-manual.md](med-file-manual.md) | Vendor source reference |
