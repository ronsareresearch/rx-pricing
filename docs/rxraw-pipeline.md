# rxraw Pipeline

`rxraw` is the raw-ingestion stage of the project. It loads MED-File v2 deliveries into schema `rxraw` and does not perform refinement or view creation.

---

## Command

```bash
uv run python -m rxraw
```

Reset and reload everything in `rxraw`:

```bash
uv run python -m rxraw --reset
```

---

## What `rxraw` Does

1. Creates schema `rxraw` and the raw tables.
2. Discovers MED-File runs under `DATA_DIR`.
3. Loads each discovered run into `rxraw.raw_*`.
4. Records the run in `rxraw.loaded_runs`.
5. Loads `MF2DICT` once when the file is available.

`rxraw` only writes raw data. Refinement and views are separate steps.

---

## Run Discovery

- A run is a directory that contains `MF2SUM`.
- `MF2SUM` provides the file type, issue date, volume number, and supplement number.
- Discovered runs are sorted with one full load (`T`) first and incrementals (`U`) afterward by volume.
- Directories without a valid `MF2SUM` record are ignored during normal discovery.

Fallback behavior:

- If no valid `MF2SUM` is found anywhere under `DATA_DIR`, `rxraw` creates one synthetic full run from `DATA_DIR` itself.
- That fallback uses today's date and volume `0`.
- Treat that path as a convenience for local recovery or ad hoc loading, not the preferred delivery structure.

---

## Configuration

- `EXTERNAL_DATABASE_URL`: required PostgreSQL connection string
- `DATA_DIR`: optional root for MED-File run directories; defaults to `data/`
- `RXRAW_INSERT_BATCH_SIZE`: optional bulk insert page size

---

## Delivery Layout

Recommended layout:

```text
data/
  full_00139/
    MF2SUM
    MF2NDC
    MF2PRC
    ...
  inc_00140/
    MF2SUM
    MF2NDC
    MF2PRC
    ...
```

One directory equals one run.

---

## Raw Tables

Schema `rxraw` contains:

- `loaded_runs`
- `raw_mf2dict`
- 27 additional `raw_*` tables for MED-File source files

Each raw table uses the same base columns:

| Column | Meaning |
|--------|---------|
| `file_id` | UUID for the loaded run |
| `file_date` | Issue date from `MF2SUM` |
| `source_file` | MED-File source filename |
| `line_number` | Source line number |
| `volume_number` | Volume from `MF2SUM` |
| `supplement_number` | Supplement from `MF2SUM` |
| `pos1` .. `pos80` | Raw parsed positions stored as text |

This layer preserves vendor fidelity. It is the replay and traceability source for refinement.

---

## Idempotency and Resume Behavior

- A previously loaded run is skipped by `(file_date, volume_number)`.
- If a run was only partially loaded, `rxraw` can reuse the existing `file_id` and continue instead of duplicating rows.
- `MF2DICT` is treated specially and is loaded once per schema.

---

## Relationship to Later Stages

After `rxraw` finishes:

1. Run `uv run python -m refine`
2. Then run `uv run python -m view`

Those stages read from `rxraw`; `rxraw` does not call them automatically.
