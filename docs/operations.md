# Operations

**Role:** Run commands, recovery steps, and practical operating guidance for the current pipeline.

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

If you only want the entity views and want to skip the PCIP-oriented views:

```bash
uv run python -m view --no-pcip
```

The default `view` build now includes:

- current entity views
- monthly historical views keyed by Medi-Span file month
- PCIP-oriented current-state views unless `--no-pcip` is used

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

## MF2ERR Status

`MF2ERR` is loaded into raw, but correction processing is not implemented in refinement yet.

Current guidance:

- keep the raw file with the rest of the delivery
- do not document the run as fully correction-aware
- treat downstream history as incomplete until MF2ERR handling is implemented

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

Entity views:

- `medfile.v_ndc`
- `medfile.v_ndc_price`
- `medfile.v_drg`

Monthly historical views:

- `medfile.v_product_package_monthly`
- `medfile.v_product_package_price_monthly`
- `medfile.v_gpi_ndc_equivalent_monthly`

PCIP-oriented views:

- `medfile.v_ndc_pcip_reference`
- `medfile.v_gpi_equivalents`
- `medfile.v_drg_maintenance`

Monthly view rule:

- `reference_month` is derived from the Medi-Span file month in `medfile.refine_runs.file_date`
- if multiple completed refine runs exist in the same month, the latest completed run is published for that month
- claims-side selection of `paid_date` versus `processed_date` remains out of scope for this repo
