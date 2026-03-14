# Data & Infrastructure Architecture: rx-pricing

**Role:** Definitive architecture for the MED-File v2 ETL pipeline. Covers data layers, infrastructure, security, observability, and evolution. See [Glossary](glossary.md) for terms; file inventory in [schema-validation.md](schema-validation.md) §0.

---

## 1. Design Principles

| Principle | Application |
|-----------|-------------|
| **History is immutable** | Raw intake is append-only; refinement never overwrites or deletes history. |
| **Sequence is sacred** | Volume Number and Supplement drive ordering; out-of-order loads are rejected. |
| **Layered ownership** | Raw (vendor fidelity) → Refined (normalized, SCD2) → Views (consumption). |
| **Metadata as code** | MF2DICT/MF2VAL drive validation and translation; pipeline consumes them like any other file. |
| **Forward compatibility** | New MED-File files or fields are absorbed via schema-on-read or versioned schemas; no hard-coded file counts. |

---

## 2. Data Architecture

### 2.1 Three-Layer Model

```
┌─────────────────────────────────────────────────────────────────────────┐
│  CONSUMPTION LAYER (Custom Views)                                       │
│  • Current-state views (active NDCs, latest price, active DDIDs)        │
│  • Analytics / reporting views (price history, lineage, KPIs)           │
│  • API-ready or warehouse marts                                         │
└─────────────────────────────────────────────────────────────────────────┘
                                      ▲
┌─────────────────────────────────────────────────────────────────────────┐
│  REFINEMENT LAYER (Normalized, SCD2, Append-Only)                        │
│  • Type 2 SCD and effective-date history for dimensions                 │
│  • Price history tables (by Effective Date; no overwrite)               │
│  • Identifier lineage (NDC↔NDC, DDID↔DDID) and Item Status             │
│  • Referential integrity enforced; keys stable across runs               │
└─────────────────────────────────────────────────────────────────────────┘
                                      ▲
┌─────────────────────────────────────────────────────────────────────────┐
│  RAW LAYER (Landing / Intake) — implemented as rxraw                     │
│  • On disk: files in data/ (or DATA_DIR); one run per dir with MF2SUM   │
│  • In DB: rxraw.raw_* (28 tables: raw_mf2dict + 27 from RAW_SOURCE_FILES)│
│  • One row per source line; file_id (UUID), file_date, source_file,     │
│    line_number, volume_number, supplement_number, pos1..pos80 (TEXT)    │
│  • Run tracking: rxraw.loaded_runs (file_id, file_date, volume, etc.)   │
│  • MF2SUM drives run discovery and file_date/volume; immutable load    │
└─────────────────────────────────────────────────────────────────────────┘
```

- **Raw (disk):** Source files under `data/` (or `DATA_DIR`); each directory containing MF2SUM is one run. Preserved for audit, replay, and debugging.
- **Raw (DB) — implemented:** The **rxraw** pipeline loads into schema `rxraw`: tables `rxraw.raw_*` with `file_id`, `file_date`, `source_file`, `line_number`, `volume_number`, `supplement_number`, and `pos1`..`pos80`. Run metadata in `rxraw.loaded_runs`. See [rxraw-pipeline.md](rxraw-pipeline.md) and [schema-validation.md](schema-validation.md) § Raw layer.
- **Refinement (Phase 2+3 implemented):** Schema `medfile`: translation table `mf2val` (MF2VAL) and **25 refinement tables** for all data files except MF2ERR (Phase 4). Load order and dependencies in `refine/load_order.py`; SCD2 / append-only history. See [schema-validation.md](schema-validation.md) §0.
- **Views (planned):** Built from refinement for production reporting; optional views from raw for validation or one-off analysis.

### 2.2 Load and Transaction Semantics

- **Full load (T):** Insert-only baseline; record Volume Number for future sequence checks.
- **Incremental (U):** Enforce Volume Number = last + 1 (or Supplement rules per manual). Apply Transaction CD: **A** = insert, **C** = append new row (history), **D** = end-date/flag, never physically delete from history.
- **MF2ERR (Error Correct):** Only in incrementals. Apply corrections to refinement so historical timeline reflects manufacturer revisions; consider a dedicated “correction log” table keyed by Key Identifier, Unique Key, Data Element Code.

### 2.3 Key Entity Lifecycle

- **NDC (MF2NDC):** Item Status (A/I/O/Z); Old/New NDC-UPC-HRI and effective dates for chaining. **Z** (inactive >48 months) appears once with **D**; retain in history forever.
- **DDID (MF2DRG):** Link Value / Link Date for replacement DDIDs; maintain chain in refinement.
- **Prices (MF2PRC, MF2GPR):** New row per Effective Date / Price Effective Date for A or C; never update in place.

### 2.4 Run and file provenance (how we know which data came from which file)

Every pipeline execution is one **run** (one Volume + Supplement per delivery). Run-level metadata and per-row provenance let us answer "which file / which delivery" for any row.

| Layer | How we know "which file" and "which delivery" |
|-------|------------------------------------------------|
| **Run metadata (current)** | **`rxraw.loaded_runs`**: `file_id` (UUID, PK), `file_date` (DATE from MF2SUM), `volume_number`, `supplement_number`, `loaded_at`. One row per run; duplicate (file_date, volume) skipped on load. |
| **Raw (DB) — current** | **Implemented.** All in-scope files load into **`rxraw.raw_*`**. Each row has **`file_id`**, **`file_date`**, **`source_file`**, **`line_number`**, **`volume_number`**, **`supplement_number`**, and **`pos1`..`pos80`** (TEXT). Indexes on `(file_id)` and `(file_date, source_file)`. Query by file_date, volume_number, or source_file for history and maintenance. |
| **Refinement (Phase 2)** | Run metadata in **`medfile.refine_runs`**; refined rows in **`mf2val`**, **`refinement_ndc`**, **`refinement_ndc_price`**, **`refinement_drg`** with **`run_id`**, **`file_date`**, **`source_file`** for traceability. |

**Current implementation (rxraw)**

- **Run discovery:** Directories under `DATA_DIR` (default `data/`) that contain MF2SUM; parsed for file_type (T/U), issue_date, volume, supplement. Sorted: one full (T) first, then incrementals (U) by volume. See [rxraw-pipeline.md](rxraw-pipeline.md).
- **Config:** `EXTERNAL_DATABASE_URL` (required), `DATA_DIR` (optional), `RXRAW_INSERT_BATCH_SIZE` (optional). Run: `uv run python -m rxraw`; `--reset` drops schema and reloads.

---

## 3. Infrastructure Orientation

*Technology-agnostic guidance; concrete stack chosen in implementation.*

**Current stack (rxraw):** Python 3.x, [uv](https://docs.astral.sh/uv/) for runs and dependencies, PostgreSQL (connection via `EXTERNAL_DATABASE_URL`), local filesystem for MED-File data (`DATA_DIR`). Orchestration, refinement, and views are not yet implemented.

### 3.1 Compute

- **Orchestration:** Scheduled jobs (monthly) with idempotent runs; optional DAG (e.g. Airflow, Dagster, Step Functions) for: validate MF2SUM → load raw → refine (order by referential dependencies) → refresh views.
- **Execution:** Stateless workers; no in-memory state across runs. Prefer one “run id” (e.g. volume + supplement) per pipeline execution for traceability.

### 3.2 Storage

- **Raw:** Object store or network-attached landing (e.g. S3, GCS, Azure Blob) with versioning enabled; path convention `raw/medfile_v2/YYYYMM/vol_<N>/` (and optional `supp_<M>/`). Lifecycle: retain per compliance (e.g. 7 years for audit).
- **Refinement + Views:** Database or lakehouse (RDBMS, Snowflake, BigQuery, Delta/Iceberg). Refinement tables should support efficient range scans on effective dates and volume/run id for incremental and replay.

### 3.3 Networking and Access

- **Source ingestion:** Support both FTP pull and HTTP download (per vendor); credentials in secrets manager; no credentials in code or in repo.
- **Egress:** Only to internal storage and processing; no MED-File data to public internet.

### 3.4 Security and Compliance

- **Secrets:** All credentials (FTP, HTTP, DB, API) in a vault or cloud secrets manager; pipeline retrieves at runtime.
- **Data at rest:** Prefer encryption (e.g. bucket/DB encryption); align with organizational policy (e.g. PHI if applicable).
- **Access control:** Least privilege: ingestion identity can write to raw only; refinement identity can read raw and read/write refinement; view consumers read-only to refinement/views. Separate roles for ops (run/retry) vs. read-only analytics.
- **Audit:** Log who ran which load, volume/supplement, and success/failure; retain logs for compliance.

---

## 4. Observability and Reliability

### 4.1 Logging and Metrics

- **Structured logs:** Every run logs: run_id, volume_number, supplement_number, file_type (T/U), file count, record counts per file, duration, status (success/fail), and error code/message on failure.
- **Metrics:** Per run: records ingested per file; rows added/updated in refinement; view refresh duration; pipeline wall-clock time. Optional: data freshness (max effective date by entity).
- **Alerts:** Sequence break (volume not last+1); control validation failure (e.g. wrong File Type); job failure; optionally, anomaly in row counts vs. prior month.

### 4.2 Data Quality (DQ)

- **Pre-refinement:** Validate MF2SUM (File Type, Volume, Supplement); reject run if invalid. Optional: row-count vs. MF2SUM table-of-contents if present.
- **Post-refinement:** Referential integrity checks (e.g. NDC references existing Labeler); optional row-count reconciliation (raw vs. refined for that run). Use MF2VAL for coded fields where applicable.
- **Ongoing:** Optional DQ dashboard (nulls, duplicates, valid code lookups); trend vs. prior runs.

### 4.3 Idempotency and Recovery

- **Idempotency:** A given (Volume, Supplement) should be processable exactly once into raw; refinement should be idempotent for that run (e.g. “upsert” keyed by run_id + business key so re-runs don’t duplicate).
- **Failure handling:** On failure after raw write: retain raw; fix cause; re-run from refinement step (read from raw for that run). Never re-ingest same volume into raw as new data (treat as same run).
- **Replay:** To reprocess a past month, use retained raw for that volume; clear or version refinement for that run and re-run refinement + views so history stays consistent.

---

## 5. Forward-Looking and Evolution

### 5.1 New Files or Fields

- **New MED-File files:** Add to file inventory (see [schema-validation.md](schema-validation.md) §0); extend raw landing to accept new filenames; add refinement models and views as needed. Prefer configuration-driven file list (e.g. from MF2SUM or config in `rxraw.schema`) so new files don’t require code changes for “accept and store.”
- **New fields in existing files:** Prefer schema-on-read or versioned schemas (e.g. add columns or new schema version); backfill not required for net-new optional fields; backfill only if business requires them for history.

### 5.2 Delivery and Cadence Changes

- **More frequent than monthly:** Architecture supports it; ensure sequence checks use Volume + Supplement and any new sequence semantics from the vendor.
- **Vendor format change (e.g. Fixed vs. Delimited):** Summary file (CFF) indicates format; pipeline should branch on format or delegate to a parser abstraction so both Fixed and Delimited are supported without duplicating business logic.

### 5.3 Scalability and Cost

- **Larger volumes:** Scale workers or partitions by file (e.g. one task per file); avoid single-threaded bottlenecks. Use bulk load APIs for refinement DB where possible.
- **Retention and cost:** Define retention for raw (e.g. 7 years) and refinement (indefinite); archive raw to cold storage after N months if needed; views are derived and need no separate retention beyond refinement.

### 5.4 Future-Proofing

- **MED-File v3 or new product:** Treat as new pipeline or new “source” in same repo; reuse patterns (raw → refinement → views), control validation, and DQ approach; share glossary and ops playbooks where applicable.
- **Downstream consumers:** Expose only views (or approved refinement tables) via APIs or warehouse; keep MED-File semantics behind a clear boundary so future sources (e.g. other drug data) can be integrated without breaking consumers.

---

## 6. Document Map

| Document | Purpose |
|----------|---------|
| [architecture.md](architecture.md) | This document: data layers, infra, security, observability, evolution. |
| [rxraw-pipeline.md](rxraw-pipeline.md) | Rxraw ETL: run discovery, load into `rxraw` schema, config, and data layout. |
| [schema-validation.md](schema-validation.md) | File inventory (§0), refinement table mapping, raw layer column set. |
| [transformation-specs.md](transformation-specs.md) | Casting (dates, implied decimals) and MF2VAL join pattern for refinement. |
| [glossary.md](glossary.md) | Terms: DDID, NDC-UPC-HRI, GPPC, SCD2, Transaction CD, etc. |
| [operations.md](operations.md) | Runbooks: sequence break, full reload, MF2ERR, monitoring. |
| [med-file-manual.md](med-file-manual.md) | Vendor manual: field layouts, data elements, editorial policies. |
