# Rxraw pipeline

Separate ETL pipeline that loads MED-File v2 data into the **`rxraw`** PostgreSQL schema (raw tables only). It does not use the existing `etl` package.

## What it does

1. **Create schema** — Creates schema `rxraw` and all `rxraw.raw_*` tables (same structure as the project-plan raw layer: `file_id`, `file_date`, `source_file`, `line_number`, `volume_number`, `supplement_number`, `pos1`..`pos80`).
2. **Discover runs** — Finds all runs under the data directory (each run = a directory containing `MF2SUM`). Sorts so the **one full (T)** run is first, then **all incremental (U)** runs by volume.
3. **Load** — For each run in order, loads every MED-File v2 file present into `rxraw.raw_*`. Each run gets a new `file_id`; `file_date` and volume come from `MF2SUM`.

## Configuration

- **`EXTERNAL_DATABASE_URL`** — PostgreSQL connection string (env or `.env`). Same as the main project.
- **`DATA_DIR`** — Optional. Default: project `data/` directory. All MED-File v2 files (full and incrementals) live under this directory or in subdirectories; each subdirectory that contains `MF2SUM` is treated as one run.

## Run

From the project root:

```bash
uv run python -m rxraw
```

## Data layout

- **One run per directory with MF2SUM.** Place the full load in one folder and each incremental in its own folder under `data/`, e.g.:
  - `data/full/MF2SUM`, `data/full/MF2NDC`, ...
  - `data/inc_001/MF2SUM`, `data/inc_001/MF2NDC`, ...
  - `data/inc_002/MF2SUM`, ...
- Or a single directory: put all files in `data/` (one MF2SUM). That counts as one run (full if MF2SUM says T).
- If no MF2SUM is found anywhere, the pipeline treats `data/` as a single full run with default file_date (today) and volume 0.

## Tables

All tables live in schema **`rxraw`**: `rxraw.raw_mf2val`, `rxraw.raw_mf2ndc`, `rxraw.raw_mf2prc`, etc. (26 tables). Column set is the same for each: `file_id`, `file_date`, `source_file`, `line_number`, `volume_number`, `supplement_number`, `pos1`..`pos80`.
