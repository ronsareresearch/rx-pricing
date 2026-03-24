# Operations

**Role:** Run commands, recovery steps, and practical operating guidance for the current pipeline.

**Greenfield / blank state:** See [runbook.md](runbook.md) for prerequisites, first-time setup, verification, and scheduling context.

---

## Configuration

Required:

- `EXTERNAL_DATABASE_URL`: PostgreSQL connection string used by `rxraw`, `refine`, and `view`

Optional:

- `DATA_DIR`: directory that contains MED-File runs; defaults to `data/`
- `RXRAW_INSERT_BATCH_SIZE`: bulk insert page size for raw loading
- `REFINE_INSERT_PAGE_SIZE`: bulk insert page size for refinement writes

Store configuration in the environment or a local `.env` file. Do not commit secrets.

---

## Standard Run Order

From the project root:

```bash
uv run python -m rxraw
uv run python -m refine
uv run python -m view
```

The default `view` build includes:

- normalized current views across five domain families (regular, recreated each run)
- error correction audit view (regular)
- monthly historical views (materialized views with concurrent refresh and query indexes)

---

## View Refresh Modes

After an incremental refine run where view definitions have not changed, use refresh-only mode for faster execution:

```bash
uv run python -m view --refresh-only
```

This only refreshes the materialized monthly views concurrently (UI reads continue unblocked) and skips regular view recreation.

To drop and recreate all materialized views from scratch (e.g. after changing view definitions):

```bash
uv run python -m view --reset
```

---

## Full Reload

Use this when rebuilding from scratch.

1. Reload raw data:

```bash
uv run python -m rxraw --reset
```

2. Rebuild refinement from the loaded raw runs:

```bash
uv run python -m refine --reset
```

3. Recreate views:

```bash
uv run python -m view
```

Notes:

- `rxraw --reset` drops schema `rxraw` and reloads raw tables.
- `refine --reset` drops schema `medfile`, recreates it, and refines all loaded runs again.
- Run the view step after refinement completes.

---

## Incremental Processing

For a normal delivery:

1. Place the new delivery under `DATA_DIR` in a directory with `MF2SUM`.
2. Run `uv run python -m rxraw`.
3. Run `uv run python -m refine`.
4. Run `uv run python -m view`.

Current refine sequencing behavior:

- full loads (`T`) are allowed
- incrementals (`U`) require at least one prior refined run
- volume gaps are allowed
- backfills are allowed

That behavior comes from `refine/validate.py`, so operational expectations should follow the code, not an older strict-sequence assumption.

---

## Failed Refinement Run

If raw loading succeeded but refinement failed or was interrupted:

1. Fix the root cause.
2. Remove rows written by failed refine runs:

```bash
uv run python -m refine --clean-failed
```

3. Run refinement again:

```bash
uv run python -m refine
```

4. Recreate views:

```bash
uv run python -m view
```

Do not re-ingest the same delivery into raw as a new run.

---

## Raw-Load Notes

- `rxraw` discovers runs from directories that contain `MF2SUM`.
- Duplicate runs are skipped based on `(file_date, volume_number)`.
- If a run was partially loaded, `rxraw` can resume it by reusing the same `file_id`.
- If no valid `MF2SUM` exists anywhere under `DATA_DIR`, `rxraw` falls back to one synthetic full run from `DATA_DIR`. Treat that as a recovery or local-development behavior, not the preferred operating pattern.

---

## MF2ERR Correction Processing

`MF2ERR` (Error Correct File) is fully integrated into the refinement pipeline.

- MF2ERR records are refined into `medfile.refinement_err` as `append_only` history (all correction flags are preserved across deliveries).
- MF2ERR is processed as Phase 4 in the load order — after all entity processing.
- MF2ERR is only present in incremental updates (`U`); total replacements (`T`) have no MF2ERR records.
- The `v_error_corrections` view provides a human-readable audit trail with decoded entity types (`Drug Descriptor ID`, `NDC-UPC-HRI`, `NDC-UPC-HRI + Price Type`) and run metadata.
- MF2ERR flags which records had data entry revisions; the corrected data itself is in the corresponding entity files (MF2NDC, MF2NAME, MF2PRC, etc.) and is already processed by the normal entity refinement.

---

## Monitoring Checklist

Track at minimum:

- run success or failure for `rxraw`, `refine`, and `view`
- counts of loaded raw rows per source file
- counts of refined rows written per run
- last refined volume number
- view refresh completion

Investigate when:

- `EXTERNAL_DATABASE_URL` is missing or invalid
- an incremental run has no prior refined run
- repeated failed refine runs require `--clean-failed`
- row counts differ sharply from recent deliveries

---

## Current View Outputs

The view runner maintains a registry of managed views and drops orphaned views (both regular and materialized) on each run.

Packaged drug reference views (Family 1):

- `medfile.v_product_package_current` — canonical NDC reference (one row per NDC)
- `medfile.v_product_package_price_current` — latest active price per NDC and price type
- `medfile.v_product_package_modifier_current` — current modifier attachments per NDC
- `medfile.v_product_package_price_history` — full active price history

GPI and equivalence views (Family 2):

- `medfile.v_gpi_current` — GPI classification with TC-GPI hierarchy
- `medfile.v_gppc_current` — packaging-level reference
- `medfile.v_gpi_ndc_equivalent_current` — generic-equivalence candidates

Clinical hierarchy views (Family 3):

- `medfile.v_drug_name_current` — drug name concept layer
- `medfile.v_routed_drug_current` — routed drug with route enrichment
- `medfile.v_drug_dose_form_current` — drug-dose-form with form descriptions
- `medfile.v_routed_drug_form_current` — routed-drug-form
- `medfile.v_dispensable_drug_current` — dispensable drug (DDID)
- `medfile.v_dispensable_drug_rollup_current` — flattened hierarchy rollup

Ingredient composition views (Family 4):

- `medfile.v_concept_ingredient_set_current` — concept-to-ingredient-set mapping
- `medfile.v_ingredient_set_member_current` — ingredient set membership
- `medfile.v_ingredient_current` — ingredient reference with strength
- `medfile.v_concept_ingredient_current` — concept-to-ingredient bridge

Terminology and alternate-ID views (Family 5):

- `medfile.v_code_lookup_current` — code-to-description translation
- `medfile.v_concept_description_current` — concept descriptions
- `medfile.v_concept_reference_name_current` — brand-to-generic name mapping
- `medfile.v_alternate_id_current` — alternate-ID crosswalk

Error correction audit view:

- `medfile.v_error_corrections` — audit trail of MF2ERR data entry revision flags

Monthly historical views (materialized, concurrently refreshable):

- `medfile.v_product_package_monthly`
- `medfile.v_product_package_price_monthly` (all price codes)
- `medfile.v_product_package_price_awp_monthly` (AWP only)
- `medfile.v_product_package_price_wac_monthly` (WAC only)
- `medfile.v_product_package_price_dp_monthly` (DP only)
- `medfile.v_gpi_ndc_equivalent_monthly`

Monthly view rule:

- `reference_month` is derived from the Medi-Span file month in `medfile.refine_runs.file_date`
- if multiple completed refine runs exist in the same month, the latest completed run is published for that month
- claims-side selection of `paid_date` versus `processed_date` remains out of scope for this repo
- materialized views include unique indexes for concurrent refresh plus query indexes on NDC, GPI, month, and drug name for UI query performance
- the view runner ensures performance indexes on source refinement tables (temporal indexes for LATERAL joins, price ranking indexes, refine_runs status index) before creating or refreshing views
