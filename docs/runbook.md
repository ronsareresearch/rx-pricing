# Runbook — `rx-pricing` (greenfield → steady state)

**Role:** End-to-end operational guide when **starting from a blank state** (new environment, new database, or disaster rebuild) through **normal** and **recovery** runs.

**Companion:** [operations.md](operations.md) (command reference, MF2ERR, monitoring checklist), [deployment.md](deployment.md) (production placement, scheduling patterns), [architecture.md](architecture.md) (scope and guardrails).

---

## 1. System overview

| Stage | Module | Schema / output | Purpose |
|-------|--------|-----------------|--------|
| 1 | `rxraw` | `rxraw.*` | Ingest MED-File deliveries into raw tables. |
| 2 | `refine` | `medfile.*` | Normalize raw rows into refinement tables + `refine_runs`. |
| 3 | `view` | `medfile` views + matviews | Publish consumer-facing reference views. |

**Mandatory order:** `rxraw` → `refine` → `view`. Do not skip stages.

---

## 2. Prerequisites (blank state checklist)

### 2.1 Host / runtime

- [ ] **Python** 3.10 or newer.
- [ ] **[uv](https://docs.astral.sh/uv/)** installed (recommended), or another way to install deps from [pyproject.toml](../pyproject.toml).
- [ ] **Git** access to clone this repository.
- [ ] **Shell** with `cd` to repository root for all commands below.

### 2.2 PostgreSQL

- [ ] Empty **database** (or dedicated database) the pipeline may own.
- [ ] **User** with permission to:
  - create and drop schemas (or at least create objects in `rxraw` and `medfile`),
  - create tables, views, materialized views, indexes.
- [ ] **Connection string** ready (TLS parameters per your policy). Store as `EXTERNAL_DATABASE_URL` (never commit to git).

Example shape (adjust for your host):

```text
postgresql://USER:PASSWORD@HOST:5432/DATABASE?sslmode=require
```

### 2.3 MED-File data

- [ ] At least one **MED-File v2** delivery available on disk.
- [ ] Delivery layout: a directory under your data root containing **`MF2SUM`** (required for normal discovery). See [rxraw-pipeline.md](rxraw-pipeline.md).
- [ ] **License / procurement** aligned with your use (Wolters Kluwer Medi-Span).

### 2.4 Secrets and config

- [ ] `EXTERNAL_DATABASE_URL` set in environment or secret store (production).
- [ ] Optional: `DATA_DIR` if data is not in `./data` relative to repo root.
- [ ] Optional: `RXRAW_INSERT_BATCH_SIZE`, `REFINE_INSERT_PAGE_SIZE` (defaults are fine to start).

---

## 3. Greenfield install (from zero)

### 3.1 Clone and dependencies

```bash
git clone <YOUR_REPO_URL> rx-pricing
cd rx-pricing
uv sync
```

Confirm Python packages resolve (uses [uv.lock](../uv.lock) when present).

### 3.2 Configure environment

**Development (local only):**

```bash
export EXTERNAL_DATABASE_URL='postgresql://...'
export DATA_DIR='/path/to/medfile/deliveries'   # optional
```

Or create a **`.env`** file in the repo root (not committed) with the same variables. `python-dotenv` loads it automatically.

**Production:** inject the same variables from your scheduler / orchestrator / secret manager.

### 3.3 Lay out MED-File files

Point `DATA_DIR` at a directory that contains one or more run folders, each with `MF2SUM`:

```text
$DATA_DIR/
  20250314_T_01/          # example run folder
    MF2SUM
    MF2NDC
    ...
```

If **no** `MF2SUM` exists under `DATA_DIR`, `rxraw` may fall back to synthetic behavior—**avoid** that in production; fix layout first ([operations.md](operations.md) — Raw-Load Notes).

### 3.4 First full pipeline (initial load)

For a **truly empty** database, run the three stages **once** without `--reset` (schemas are created as needed):

```bash
cd /path/to/rx-pricing
uv run python -m rxraw
uv run python -m refine
uv run python -m view
```

**Expected:**

- Exit code **0** for each command.
- Logs show raw load, refinement phases, view creation / matview refresh.
- Schemas **`rxraw`** and **`medfile`** exist.

If the database previously contained **partial or corrupted** objects from an old version, use **§5.1 Full rebuild** instead.

### 3.5 Verify (smoke checks)

Run in `psql` or any SQL client connected to the same database:

```sql
-- Raw registry
SELECT COUNT(*) FROM rxraw.loaded_runs;

-- Refinement registry
SELECT COUNT(*) FROM medfile.refine_runs WHERE status = 'done';

-- Sample current reference
SELECT COUNT(*) FROM medfile.v_product_package_current;

-- Monthly matviews exist
SELECT matviewname FROM pg_matviews WHERE schemaname = 'medfile' ORDER BY 1;
```

Expect **non-zero** counts on a successful full delivery (exact numbers depend on Medi-Span content).

---

## 4. Steady state — normal incremental delivery

Use after Medi-Span drops a new delivery under `DATA_DIR`.

1. Ensure new files are visible to the job (sync completed, correct permissions).
2. Run, from repo root:

```bash
uv run python -m rxraw
uv run python -m refine
uv run python -m view
```

3. If **view SQL did not change** since last deploy, you may use faster matview-only refresh after refine:

```bash
uv run python -m view --refresh-only
```

**Sequencing rules** ([operations.md](operations.md) — Incremental Processing):

- **Full** loads (`T`) are allowed.
- **Incremental** loads (`U`) require at least **one** prior successful refined run.
- Do **not** re-ingest the same delivery as a duplicate raw run after a failed refine—use **§5.2** instead.

---

## 5. Recovery procedures

### 5.1 Full rebuild (nuclear option)

Use when schemas are wrong, you need a clean re-load, or after major migration.

**Warning:** Drops **`rxraw`** and **`medfile`** refinement state (raw schema dropped; medfile recreated on refine).

```bash
uv run python -m rxraw --reset
uv run python -m refine --reset
uv run python -m view
```

**Data:** You must still have MED-File files under `DATA_DIR`; raw is re-read from disk.

### 5.2 Refinement failed after raw succeeded

Do **not** load the same files again as a new raw run.

1. Fix root cause (disk, DB, bad file).
2. Clean failed refinement rows:

```bash
uv run python -m refine --clean-failed
```

3. Re-run refine and view:

```bash
uv run python -m refine
uv run python -m view
```

### 5.3 View / matview issues only

- **Definitions changed** (after code deploy): recreate matviews:

```bash
uv run python -m view --reset
uv run python -m view
```

(`--reset` drops managed materialized views; second command recreates and loads them.)

- **Definitions unchanged**, data updated in refine only:

```bash
uv run python -m view --refresh-only
```

### 5.4 Connection / credential failures

| Symptom | Action |
|---------|--------|
| `EXTERNAL_DATABASE_URL not set` | Set env var or `.env`; re-run. |
| Connection refused / timeout | Check network, firewall, DB up, TLS settings. |
| Permission denied on CREATE | Grant DDL on database or use elevated role per policy. |

---

## 6. MF2ERR (error correct file)

Incremental updates may include **MF2ERR**. No separate operator step: refinement processes it in load order. For semantics and audit view, see [operations.md](operations.md) — MF2ERR Correction Processing and `medfile.v_error_corrections`.

---

## 7. Scheduling (production)

- Run **after** each Medi-Span delivery lands in `DATA_DIR`, or on a fixed cadence that matches vendor SLA.
- Use a **dedicated job** (cron, Kubernetes `CronJob`, ECS scheduled task, etc.) with:
  - working directory = repo root (or packaged artifact with same layout),
  - secrets for `EXTERNAL_DATABASE_URL`,
  - shared storage or sync for `DATA_DIR`.
- Capture **exit codes** and **logs** per stage; alert on non-zero exit.

See [deployment.md](deployment.md) for platform patterns.

---

## 8. Monitoring and alerts (minimum)

Track ([operations.md](operations.md) — Monitoring Checklist):

- Success/failure and duration: `rxraw`, `refine`, `view`.
- Row counts or log lines indicating volume loaded/refined.
- Last successful `refine_runs` / latest `reference_month` in monthly matviews if consumers depend on freshness.

**Investigate** when: repeated `--clean-failed` cycles, sudden row-count drops, or view refresh failures.

---

## 9. Escalation template

| Severity | Example | Action |
|----------|---------|--------|
| S1 | Pipeline down > 1 business day | Eng owner + data ops; consider rollback of code deploy. |
| S2 | Single delivery failed | Check logs, §5.2; open ticket with `file_date`, volume, error snippet. |
| S3 | Question on semantics | [architecture.md](architecture.md), [med-file-manual.md](med-file-manual.md), vendor support. |

Fill in **owner contacts** and **ticket system** for your org in your internal copy of this runbook if needed.

---

## 10. Quick reference (commands)

| Goal | Command |
|------|---------|
| Normal full chain | `uv run python -m rxraw && uv run python -m refine && uv run python -m view` |
| Matview refresh only | `uv run python -m view --refresh-only` |
| Full DB rebuild (raw+medfile) | `uv run python -m rxraw --reset && uv run python -m refine --reset && uv run python -m view` |
| After failed refine | `uv run python -m refine --clean-failed && uv run python -m refine && uv run python -m view` |
| Reset matviews then rebuild | `uv run python -m view --reset && uv run python -m view` |

---

## 11. Document control

| Version | Date | Notes |
|---------|------|--------|
| 1.0 | 2026-03-23 | Greenfield runbook from blank state |
