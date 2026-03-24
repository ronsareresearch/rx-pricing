# Deployment — `rx-pricing` (MED-File baseline pipeline)

**Role:** How to **deploy and operate** this repository in production-like environments. For **blank-state** setup and verification, see [runbook.md](runbook.md). For day-to-day commands and recovery, see [operations.md](operations.md).

**Scope:** The **batch ETL** (`rxraw` → `refine` → `view`) and the **PostgreSQL** database that holds `rxraw` and `medfile`. This repo does **not** ship a customer-facing **UI** or claims analytics; those belong to **downstream applications** (separate repos). A **thin read API** in front of `medfile` (optional, often a separate small service) is a common integration pattern when consumers should not use direct database credentials—see **§5**.

---

## 1. What you are deploying

| Component | Type | Notes |
|-----------|------|--------|
| **Pipeline jobs** | Batch / scheduled | Three steps in order: `rxraw`, `refine`, `view` ([operations.md](operations.md) — Standard Run Order). |
| **PostgreSQL** | Managed or self-hosted | Single logical database; schemas `rxraw` and `medfile` owned by this pipeline. |
| **MED-File inputs** | Files on disk or mounted volume | Discovered under `DATA_DIR`; each delivery includes `MF2SUM`. |
| **Thin reference API** | Optional future service | **Not implemented in this repo today** ([architecture.md](architecture.md) — Current Gaps). Deploy as a small read-only layer when consumers must not hold `medfile` write-capable credentials or need an HTTP boundary. |

There is **no** web application, BFF, or end-user frontend in this project.

---

## 2. Prerequisites

- **Python** 3.10+ and **[uv](https://docs.astral.sh/uv/)** (recommended) or an equivalent venv with dependencies from [pyproject.toml](../pyproject.toml).
- **PostgreSQL** compatible with `psycopg2` (version per your org standard; test in non-prod first).
- **Network** from the job runner to PostgreSQL (TLS to DB if required by policy).
- **Storage** for MED-File drops: durable volume or object store **synced to a path** visible as `DATA_DIR` before `rxraw` runs.
- **Secrets** store (e.g. cloud secret manager, Vault, or CI secrets) for `EXTERNAL_DATABASE_URL`—never commit credentials.

---

## 3. Configuration

| Variable | Required | Purpose |
|----------|----------|---------|
| `EXTERNAL_DATABASE_URL` | Yes | PostgreSQL connection string for `rxraw`, `refine`, `view`. |
| `DATA_DIR` | No | Root directory for MED-File runs; default `data/` relative to cwd. |
| `RXRAW_INSERT_BATCH_SIZE` | No | Raw load batch size. |
| `REFINE_INSERT_PAGE_SIZE` | No | Refine write page size. |

Load from the environment or a **local** `.env` for development only; production should inject env vars from your platform.

---

## 4. Deployment pattern (recommended)

### 4.1 Artifact

- **Source:** pinned commit (Git tag or release branch).
- **Install:** `uv sync` (or `pip install` from lock/export if you vendor dependencies).
- **Working directory:** repository root (or a copy that includes `refine/rules/` and packages `rxraw`, `refine`, `view`).

### 4.2 Scheduler

Run after each Medi-Span delivery (or on your agreed cadence):

```bash
uv run python -m rxraw
uv run python -m refine
uv run python -m view
```

For **incremental** deliveries where **view definitions are unchanged**, prefer faster view refresh:

```bash
uv run python -m view --refresh-only
```

Map this to:

- **Cron** on a VM or bare metal,
- **Kubernetes CronJob**,
- **ECS scheduled task** / **Azure Container Apps job** / **GCP Cloud Run job**,
- **CI pipeline** only if a **private runner** has `DATA_DIR`, DB access, and acceptable secrets handling (often better to run jobs in your data plane, not shared CI).

**Idempotency:** Re-running after partial failure has specific recovery steps—see [operations.md](operations.md) (Failed Refinement Run, Full Reload).

### 4.3 Resource guidance

- **CPU / memory:** Scale with Medi-Span volume; start from a medium instance and tune using run duration and DB load.
- **Disk:** Enough space for expanded MED-File trees under `DATA_DIR` plus logs.
- **Database:** Ensure connection limits and statement timeouts suit long-running batch writes; index creation during `view` can be heavy—run in a maintenance window if needed.

### 4.4 Observability

Minimum signals (align with [operations.md](operations.md) — Monitoring Checklist):

- Exit code and duration per stage (`rxraw`, `refine`, `view`).
- Log capture (stdout/stderr) with run id or delivery date in context.
- Optional: row counts from DB or structured logs if you extend the pipeline.

Alert on failure; page only for repeated failures or stale `medfile` beyond SLA.

---

## 5. Downstream integration (thin API vs database)

**Thin read API** is a good default when:

- Consumers should not use **broad database credentials** for `medfile`.
- You want **stable, versioned JSON** contracts, **rate limits**, and **audit** at the reference boundary.
- Network policy allows **HTTP** from the app tier but not direct SQL.

**Direct read replica** (or read-only role on same DB) is simpler when:

- Consumers and this baseline share a **VPC** and a **Postgres read replica** is already standard.
- Analytics need **ad hoc SQL** and **join** performance without an API middle tier.

Either way, document **view names**, **grains**, and **`reference_month`** semantics in a **consumer ↔ baseline integration spec** (owned by the consuming team; align with [architecture.md](architecture.md) and [operations.md](operations.md)). Implementing the API is **not** part of this repo today; plan it as a small service with read-only DB user, query timeouts, and no Medi-Span file-drop secrets on the consumer side. **Full HTTP contract:** [reference-api-spec.md](reference-api-spec.md) and [openapi/medfile-reference-v1.yaml](openapi/medfile-reference-v1.yaml).

---

## 6. Security and compliance

- **Least privilege:** Pipeline DB user needs DDL/DML appropriate for batch loads; a future API user should be **read-only** on `medfile` (and optionally limited to specific views).
- **Secrets:** Rotate `EXTERNAL_DATABASE_URL` on compromise; restrict who can read job definitions.
- **Medi-Span / WK license:** Treat raw and refined files as **licensed**; scope storage access and backups to policy.
- **No PHI in this pipeline:** MED-File is drug reference; plan **claims PHI** stays in consumer systems—separate environments if required by BAA boundaries.

---

## 7. Backups and disaster recovery

- **PostgreSQL:** Use your platform’s backup/PITR for the database that hosts `rxraw` and `medfile`.
- **MED-File source files:** Retain per license and operational need; pipeline can rebuild `medfile` from `rxraw` if raw tables are intact.
- **Recovery order:** Follow [operations.md](operations.md) — Full Reload when rebuilding schemas from scratch.

---

## 8. Document map

| Document | Relationship |
|----------|----------------|
| [operations.md](operations.md) | Commands, incremental vs full, view modes, monitoring checklist |
| [architecture.md](architecture.md) | Repo boundaries, downstream consumers, current gaps |
| [schema-validation.md](schema-validation.md) | View inventory and MED-File coverage |

---

## 9. Revision

| Version | Date | Notes |
|---------|------|--------|
| 1.0 | 2026-03-23 | Initial deployment guide for batch pipeline; thin API as downstream integration option |
| 1.1 | 2026-03-23 | Removed in-repo product doc links; generic downstream consumer wording |
