# Operations: Runbooks and Monitoring

**Role:** Operational procedures for the MED-File v2 ETL pipeline. See [Architecture](architecture.md) for observability and recovery, and [Glossary](glossary.md) for terms.

---

## 0. Configuration (required for all runs)

- **`EXTERNAL_DATABASE_URL`** — PostgreSQL connection string for raw load and refinement (e.g. `postgresql://user:password@host:5432/database`). Set in environment or `.env` in project root; **do not commit** (`.env` is in `.gitignore`). See [rxraw-pipeline.md](rxraw-pipeline.md) and [architecture.md](architecture.md).
- **`DATA_DIR`** (optional) — Path to MED-File v2 files for this run; default is project `data/`. Pipeline looks for MF2SUM under this path (including one or two levels of subdirectories).
- **`REFINE_INSERT_PAGE_SIZE`** (optional) — Batch size for refinement INSERT/UPDATE (default 5000, range 500–50_000). Tune for throughput; see [refine-load-optimization-options.md](refine-load-optimization-options.md).

**Empty or delimiter-only incrementals:** Some incremental files may be empty or contain only delimiter (e.g. pipe) lines. The pipeline treats such lines as no record: MF2SUM/MF2DICT parsers skip them; data files (Phase 3+) yield 0 records and do not fail the run. See `rxraw/parse_utils.py`.

---

## 1. Pre-Run Checklist (Monthly Incremental)

- [ ] New delivery available (FTP/HTTP); notification or schedule confirmed.
- [ ] No other run for the same Volume/Supplement in progress.
- [ ] Credentials and secrets (FTP/HTTP, DB, vault) are valid.
- [ ] Sufficient storage and compute quota for raw + refinement.
- [ ] Last successful run’s Volume Number recorded (for sequence check).

---

## 2. Runbook: Control Validation Failure (MF2SUM)

**Symptom:** Pipeline rejects run during MF2SUM validation.

**Causes:** Wrong Product File Type (e.g. expected U, got T); Supplement out of order; missing or malformed Summary file. (Refine allows volume gaps and backfill; see item 3.)

**Actions:**

1. **Do not load any data files** into refinement until MF2SUM is valid.
2. Capture MF2SUM contents (File Type, Volume, Supplement, TOC) and error message.
3. **Volume sequence (refine):** Refine allows normal (volume = last+1), **gap** (volume > last+1; missing volumes skipped), and **backfill** (volume ≤ last). If a delivery (e.g. 144) is missing, refine continues; load 144 into raw later and run refine again to backfill.
4. **Wrong File Type:** Confirm you requested an Incremental but received a Total (or vice versa). Resolve with vendor; do not force-load.
5. Log incident and resolution; update runbooks if a new failure mode is identified.

---

## 3. Runbook: Full Reload (Total Database, T)

**When:** Initial go-live or planned full refresh (e.g. after vendor data correction).

**Steps:**

1. **Prepare:** Ensure no incremental run is in progress; backup or snapshot refinement/views if required by policy.
2. **Validate MF2SUM:** Product File Type = "T"; record Volume Number for future incrementals.
3. **Ingest to raw:** All delivered files into a dedicated raw partition (e.g. `raw/medfile_v2/YYYYMM/vol_T/` or similar). Verify checksums if available.
4. **Refinement:** Run full-load path (insert-only, no Transaction CD logic). Option A: truncate refinement tables and load from this Total. Option B: load into a new schema or partition and switch (zero-downtime). Choose per architecture and downtime tolerance.
5. **Views:** Rebuild or refresh all views from refinement.
6. **Record state:** Persist “last Volume = N” and “last run = Full” for next incremental sequence check.
7. **Notify:** Data consumers and downstream systems that a full refresh completed.

---

## 4. Runbook: Incremental Run (Update, U)

**When:** Regular monthly (or periodic) incremental delivery.

**Steps:**

1. **Validate MF2SUM:** Product File Type = "U"; Volume Number = last_volume + 1 (or valid Supplement per manual). Reject and follow Runbook: Control Validation Failure if not.
2. **Ingest to raw:** All delivered files (including MF2ERR if present) into raw partition for this run (e.g. `raw/medfile_v2/YYYYMM/vol_N/`).
3. **Refinement:** Process in **dependency order** (see `refine/load_order.py`). Refine pipeline runs all 25 entities in that order (mf2val → lab → rte → … → rnm). Apply Transaction CD: A → insert, C → append history, D → end-date/flag; never delete from history. MF2ERR (Phase 4) is processed after affected entities; apply corrections to refinement.
4. **Views:** Refresh materialized views or recompute dependent views.
5. **Record state:** Persist “last Volume = N” and “last run = Incremental.”
6. **Log and metrics:** Record counts (rows per file, rows added/updated in refinement), duration, status.

---

## 5. Runbook: Pipeline Failure After Raw Write

**Symptom:** Raw write succeeded; refinement or views failed (e.g. DB error, timeout, Ctrl+C).

**Actions:**

1. **Do not re-ingest** the same delivery into raw as a new run (raw is immutable for that Volume).
2. Fix root cause (e.g. schema, connectivity, resource limit).
3. **Clean failed-run data before re-running:** Each refine step commits after itself, so a run that failed or was interrupted partway has already written data for completed entities (e.g. mf2val through gppc). Re-running refine would process the same file again and duplicate SCD2/append rows. Delete data for failed runs first:
   ```bash
   uv run python -m refine --clean-failed
   ```
   then run refinement again:
   ```bash
   uv run python -m refine
   ```
4. Document cause and resolution; add alert or guard if this failure mode is recurring.

---

## 6. Runbook: Error Correct File (MF2ERR) Present

**When:** Incremental delivery contains MF2ERR.

**Steps:**

1. Ingest MF2ERR to raw with the rest of the delivery.
2. Parse Key Identifier, Unique Key, Data Element Code per manual.
3. Apply corrections to refinement so the historical timeline matches manufacturer revisions (e.g. correct a price or attribute for a past date). Consider a dedicated “correction log” table for audit.
4. Refresh any views that depend on corrected entities.
5. Log count of corrections applied.

---

## 7. Monitoring and Alerts

**Recommended alerts:**

| Alert | Condition | Severity | Action |
|-------|------------|----------|--------|
| Sequence break | Volume ≠ last_volume + 1 (and not valid Supplement) | Critical | Halt; run Control Validation Failure runbook. |
| Control validation failure | MF2SUM invalid or missing | Critical | Halt; run Control Validation Failure runbook. |
| Pipeline failure | ETL job failed (refinement or views) | High | Run “Pipeline Failure After Raw Write” runbook. |
| Data quality | Referential integrity or row-count check failed | High | Investigate; do not promote to views until resolved. |
| Anomaly (optional) | Record count for key file &gt;2× or &lt;0.5× prior month | Medium | Review before or after run. |

**Metrics to retain:**

- Per run: volume_number, supplement_number, file_type, record counts per file, refinement rows inserted/updated, view refresh duration, pipeline duration, status.
- Over time: data freshness (e.g. max effective date by entity), trend of row counts.

---

## 8. Escalation and Ownership

- **Data/platform team:** First response for pipeline failures, sequence breaks, and DQ failures.
- **Vendor (Wolters Kluwer):** Missed delivery, Volume/Supplement numbering, File Type or format questions, suspected data errors.
- **Security/Compliance:** Any exposure of credentials or MED-File data; access or audit issues.

Document exact escalation paths (tickets, contacts) in your organization’s runbook or wiki and link from here.
