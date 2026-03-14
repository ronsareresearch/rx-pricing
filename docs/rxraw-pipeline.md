# Rxraw pipeline

ETL pipeline that loads MED-File v2 data into the **`rxraw`** PostgreSQL schema (raw tables only). Refinement (medfile schema) is a separate pipeline (`refine`); see [schema-validation.md](schema-validation.md) §7 for all schemas.

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

## Runs and volume numbers (139, 140, …)

- **One “run”** = one delivery = one directory that contains **MF2SUM** (and its data files). When you load that directory into raw, you get **one row** in `rxraw.loaded_runs` with a unique `file_id`, plus `file_date` and **volume_number**.
- **Volume number** comes from the **MF2SUM** control file (vendor field CVL). The vendor (Wolters Kluwer) assigns it; it is **not** “run #139” but the **volume identifier** for that delivery (e.g. 00139, 00140).
- **Full (T)** = one delivery with Product File Type **T** in MF2SUM (e.g. July 2022 full). That delivery has one volume number (e.g. **00139**).
- **Incrementals (U)** = later deliveries with Product File Type **U**. Each has the **next** volume number: 00140, 00141, … through 01/2024.
- **Refine** processes **unrefined** rows from `loaded_runs` in order (file_date, volume_number): first the full (e.g. 00139), then 00140, 00141, … So you get: **one full load refined first, then each incremental in sequence.** The sequence check (e.g. “expected 140, got 00140”) ensures volume numbers are consecutive; we compare them numerically so 00140 and 140 are treated the same.

## Data layout

- **One run per directory with MF2SUM.** Place the full load in one folder and each incremental in its own folder under `data/`, e.g.:
  - `data/full/MF2SUM`, `data/full/MF2NDC`, ...
  - `data/inc_001/MF2SUM`, `data/inc_001/MF2NDC`, ...
  - `data/inc_002/MF2SUM`, ...
- Or a single directory: put all files in `data/` (one MF2SUM). That counts as one run (full if MF2SUM says T).
- If no MF2SUM is found anywhere, the pipeline treats `data/` as a single full run with default file_date (today) and volume 0.

## Tables

All tables live in schema **`rxraw`**: `rxraw.raw_mf2dict` (loaded once), plus `rxraw.raw_mf2sum`, `rxraw.raw_mf2val`, `rxraw.raw_mf2ndc`, `rxraw.raw_mf2prc`, … `rxraw.raw_mf2rnm` (**28 tables** total: 1 dict + 27 from `rxraw.schema.RAW_SOURCE_FILES`). Column set is the same for each: `file_id`, `file_date`, `source_file`, `line_number`, `volume_number`, `supplement_number`, `pos1`..`pos80`.
