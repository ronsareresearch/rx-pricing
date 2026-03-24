# MED-File reference API — implementation specification

**Status:** Specification only. **Not implemented** in this repository today ([architecture.md](architecture.md) — Current Gaps). Implement as a **thin, read-only** service in front of PostgreSQL schema `medfile` (views defined by the `view` pipeline).

**Audience:** Engineers building the API service and **downstream applications** (e.g. pharmacy-claims analytics) integrating for claim-line enrichment.

**Related:** [schema-validation.md](schema-validation.md) (view inventory), [operations.md](operations.md) (refresh semantics, `reference_month` rules), [deployment.md](deployment.md), [openapi/medfile-reference-v1.yaml](openapi/medfile-reference-v1.yaml) (machine-readable subset).

---

## 1. Purpose and principles

### 1.1 Goals

- Expose **stable, versioned HTTP** access to **`medfile` normalized views** without granting consumers direct DDL or write access.
- Support **typical early-phase** enrichment: NDC → package attributes, prices, GPI, generic-equivalence signals, **current** and **monthly (`reference_month`)** slices.
- Enable **operational** checks: health, readiness, reference freshness.

### 1.2 Non-goals

- **No** pharmacy **claims** ingest, storage, or audit runs (consumer systems).
- **No** arbitrary SQL or ad hoc reporting from clients.
- **No** Medi-Span **file upload** or **ETL** control plane (remain batch pipeline only).
- **No** end-user **HTML UI** for this API (consumer products own product UI).

### 1.3 Design rules

| Rule | Detail |
|------|--------|
| Read-only | Database role: `SELECT` on approved views only; no `INSERT`/`UPDATE`/`DELETE`. |
| View fidelity | Response fields are **projections** of view columns; names use **snake_case** JSON keys matching SQL aliases where practical. |
| Versioning | URL prefix **`/v1/`**; breaking changes require **`/v2/`**. |
| Determinism | Same path + query + body → same logical result for the same underlying `medfile` snapshot; document **staleness** when refresh lags. |
| Batching | Prefer **bounded batch** endpoints for enrichment jobs to limit round-trips and connection churn. |

---

## 2. Deployment and transport

| Aspect | Requirement |
|--------|-------------|
| TLS | TLS 1.2+ everywhere; HTTPS only in production. |
| Encoding | UTF-8 JSON request/response bodies. |
| Time | Timestamps **RFC 3339** in **UTC** (e.g. `2025-03-15T14:30:00Z`). |
| Dates | Calendar **`reference_month`**: first day of month, date only: `2025-03-01` (aligns with `date_trunc('month', file_date)` in [operations.md](operations.md)). |
| NDC key | `ndc_upc_hri`: **11-digit** string, digits only (no hyphens) in API inputs; API may return `ndc_formatted` with hyphens. |

---

## 3. Authentication and authorization

### 3.1 Recommended: OAuth 2.0 client credentials

- **Token URL:** issuer-specific (e.g. `https://auth.example.com/oauth/token`).
- **Audience / resource:** `https://api.example.com` (or equivalent).
- **Scopes (suggested):**
  - `medfile.reference.read` — all read endpoints below.
  - `medfile.reference.health` — health/live only (optional split for probes).

### 3.2 Acceptable alternative: API keys

- Header: `Authorization: Bearer <api_key>` or `X-API-Key: <key>`.
- Rotate keys via admin process; rate-limit per key.

### 3.3 Optional hardening

- **mTLS** between consumer app tier and reference API (internal CA).
- **IP allow lists** for internal services only.

### 3.4 Rejected clients

- Return **401** if missing/invalid auth; **403** if valid token but insufficient scope.

---

## 4. Common conventions

### 4.1 Headers (client → server)

| Header | Required | Description |
|--------|----------|-------------|
| `Authorization` | Yes (except optional live probe) | Bearer token. |
| `Accept` | No | `application/json` (default). |
| `Content-Type` | Yes on POST | `application/json`. |
| `X-Request-Id` | Recommended | Correlation id; echo in response if provided. |

### 4.2 Headers (server → client)

| Header | Description |
|--------|-------------|
| `X-Request-Id` | Echo or generated uuid. |
| `X-RateLimit-Limit` / `Remaining` / `Reset` | If rate limiting enabled. |
| `Cache-Control` | e.g. `private, max-age=60` for stable reference rows (optional). |

### 4.3 Pagination (list endpoints)

- **Cursor style:** `?limit=100&cursor=<opaque>`  
- **Default limit:** 100; **max:** 500 (configurable).  
- Response envelope includes `next_cursor` (null if end).

### 4.4 Batch limits

| Endpoint family | Max items per request |
|-----------------|----------------------|
| POST batch NDC bodies | **500** `ndc_upc_hri` values (tune with load tests) |

Oversize → **413** or **422** with problem body.

---

## 5. Error model (Problem Details)

Use **RFC 9457** (`application/problem+json`) for all non-2xx responses.

**Example:**

```json
{
  "type": "https://api.example.com/problems/invalid-ndc",
  "title": "Invalid NDC",
  "status": 422,
  "detail": "ndc_upc_hri must be exactly 11 digits",
  "instance": "/v1/current/package/123",
  "errors": [
    { "field": "ndc_upc_hri", "message": "expected ^[0-9]{11}$" }
  ]
}
```

| HTTP status | Use |
|-------------|-----|
| 400 | Malformed JSON, unknown query combination. |
| 401 | Unauthenticated. |
| 403 | Forbidden scope. |
| 404 | Unknown resource (e.g. NDC not in reference). |
| 408 | Upstream DB timeout (optional). |
| 429 | Rate limited. |
| 500 | Unexpected server error. |
| 503 | Dependency unavailable (DB down). |

**Note:** **404 vs empty:** For “NDC not found,” prefer **404** for single-resource GET; for **batch** partial success, return **200** with per-item `error` field (see §7.3).

---

## 6. Health and reference status

### 6.1 `GET /v1/health/live`

- **Auth:** none or minimal (platform choice).
- **Response:** `200` body `{ "status": "ok" }` — process is up.

### 6.2 `GET /v1/health/ready`

- **Auth:** `medfile.reference.health` or same as read scope.
- **Behavior:** Check DB connectivity + optional “recent successful refine” predicate.
- **200:** `{ "status": "ready", "database": "ok" }`
- **503:** not ready.

### 6.3 `GET /v1/reference/status`

- **Auth:** `medfile.reference.read`
- **Purpose:** Freshness contract for consumer audit or enrichment jobs.

**Response 200:**

```json
{
  "api_version": "1",
  "medfile_schema": "medfile",
  "latest_completed_refine": {
    "run_id": 12345,
    "file_date": "2025-03-14",
    "volume_number": 3,
    "supplement_number": 0,
    "completed_at": "2025-03-15T02:10:00Z"
  },
  "reference_months_available": {
    "min": "2023-01-01",
    "max": "2025-03-01",
    "count": 27
  },
  "view_build": {
    "git_sha": "optional-from-deploy",
    "spec_revision": "1.0"
  }
}
```

**Implementation notes:**

- `latest_completed_refine` from `medfile.refine_runs` where `status = 'done'` ordered by `completed_at DESC` (or file_date policy documented with ops).
- `reference_months_available` from distinct `reference_month` in e.g. `v_product_package_monthly` or from `refine_runs` month rollup—pick one and document.

---

## 7. Current-state resources (Family 1–2 core for claims enrichment)

### 7.1 `GET /v1/current/package/{ndc_upc_hri}`

- **Maps to:** `medfile.v_product_package_current`
- **Path param:** 11-digit NDC.
- **200:** Single **ProductPackageCurrent** object (schema §9.1).
- **404:** NDC not present.

### 7.2 `GET /v1/current/prices/{ndc_upc_hri}`

- **Maps to:** `medfile.v_product_package_price_current`
- **Query:** `price_code` optional filter (e.g. `A` for AWP family).
- **200:** `{ "ndc_upc_hri": "…", "prices": [ … ] }` each item **ProductPriceCurrent** (§9.2).

### 7.3 `POST /v1/current/package/batch`

- **Body:**

```json
{
  "ndc_upc_hri": ["00123456789", "00999999999"]
}
```

- **200:**

```json
{
  "results": [
    {
      "ndc_upc_hri": "00123456789",
      "data": { },
      "error": null
    },
    {
      "ndc_upc_hri": "00999999999",
      "data": null,
      "error": { "code": "NOT_FOUND", "message": "NDC not in reference" }
    }
  ],
  "meta": {
    "requested": 2,
    "found": 1
  }
}
```

- `data` is **ProductPackageCurrent** when found.

### 7.4 `GET /v1/current/equivalents/{ndc_upc_hri}`

- **Maps to:** `medfile.v_gpi_ndc_equivalent_current` filtered by `ndc_upc_hri`, or join via package to GPI then equivalence set (implementation chooses efficient query; result must match view semantics).
- **200:** `{ "ndc_upc_hri": "…", "gpi": "…", "equivalent_ndcs": [ … ] }` with minimal fields: `ndc_upc_hri`, `gpi`, optional flags present on view.

### 7.5 `GET /v1/current/modifiers/{ndc_upc_hri}`

- **Maps to:** `medfile.v_product_package_modifier_current`
- **200:** list of modifier rows as in view.

---

## 8. Monthly (`reference_month`) resources

### 8.1 `GET /v1/monthly/reference-months`

- **200:** Paginated list of `{ "reference_month": "2025-03-01", "run_id": … }` or simple date list.

### 8.2 `GET /v1/monthly/{reference_month}/package/{ndc_upc_hri}`

- **Maps to:** `medfile.v_product_package_monthly`
- **Path:** `reference_month` = `YYYY-MM-DD` (first of month).
- **200:** Monthly package row shape (projection of materialized view; include `reference_month`, `ndc_upc_hri`, and key clinical/billing attributes required by the consumer’s methodology).
- **404:** No row for that month/NDC.

### 8.3 `GET /v1/monthly/{reference_month}/prices/{ndc_upc_hri}`

- **Maps to:** `medfile.v_product_package_price_monthly` or filtered slice by `price_code`.

### 8.4 `GET /v1/monthly/{reference_month}/price-awp/{ndc_upc_hri}`

- **Maps to:** `medfile.v_product_package_price_awp_monthly`

### 8.5 `GET /v1/monthly/{reference_month}/price-wac/{ndc_upc_hri}`

- **Maps to:** `medfile.v_product_package_price_wac_monthly`

### 8.6 `GET /v1/monthly/{reference_month}/price-dp/{ndc_upc_hri}`

- **Maps to:** `medfile.v_product_package_price_dp_monthly`

### 8.7 `GET /v1/monthly/{reference_month}/equivalents/{ndc_upc_hri}`

- **Maps to:** `medfile.v_gpi_ndc_equivalent_monthly`

### 8.8 `POST /v1/monthly/{reference_month}/package/batch`

- Same pattern as §7.3 but scoped to `reference_month`.

---

## 9. JSON schemas (logical)

*Types are logical; implement with OpenAPI components in [openapi/medfile-reference-v1.yaml](openapi/medfile-reference-v1.yaml).*

### 9.1 ProductPackageCurrent

Aligned with `v_product_package_current` ([view/current_views.py](../view/current_views.py)):

| Field | Type | Required | Notes |
|-------|------|----------|--------|
| `ndc_upc_hri` | string | yes | 11 digits |
| `ndc_formatted` | string | yes | Hyphenated display |
| `drug_descriptor_id` | string | no | |
| `drug_name` | string | no | |
| `maintenance_drug_code` | string | no | |
| `name_gpi` | string | no | From name record |
| `gppc_code` | string | no | |
| `gpi` | string | no | 14-char generic product id |
| `package_size` | string/number | no | |
| `package_size_uom` | string | no | |
| `package_quantity` | string/number | no | |
| `package_description_code` | string | no | |
| `labeler_id` | string | no | |
| `manufacturer_name` | string | no | |
| `manufacturer_abbrev` | string | no | |
| `tee_code` | string | no | |
| `tee_desc` | string | no | |
| `dea_class_code` | string | no | |
| `dea_class_desc` | string | no | |
| `rx_otc_indicator_code` | string | no | |
| `rx_otc_desc` | string | no | |
| `multi_source_code` | string | no | |
| `multi_source_desc` | string | no | |
| `item_status_flag` | string | no | |
| `item_status_desc` | string | no | |
| `name_type_code` | string | no | |
| `name_type_desc` | string | no | |
| `dollar_rank_code` | string | no | |
| `rx_rank_code` | string | no | |
| `limited_distribution_code` | string | no | |
| `specialty_proxy` | boolean | yes | Derived flag |

*Nullable fields: use `null` when SQL NULL.*

### 9.2 ProductPriceCurrent

From `v_product_package_price_current`:

| Field | Type | Notes |
|-------|------|--------|
| `ndc_upc_hri` | string | |
| `price_code` | string | e.g. `A` |
| `price_code_desc` | string | |
| `price_effective_date` | string | date |
| `unit_price` | number/string | Decimal as string recommended for money |
| `unit_price_extended` | number/string | |
| `package_price` | number/string | |
| `awp_indicator_code` | string | |

*(Include remaining view columns in implementation; keep OpenAPI in sync.)*

### 9.3 ProductPackageMonthly

Must include at minimum: `reference_month`, `ndc_upc_hri`, and the semantic columns the consumer needs for retrospective audits—**mirror the materialized view** selected in [view/monthly_views.py](../view/monthly_views.py).

---

## 10. Terminology and code lookup (optional v1)

### 10.1 `GET /v1/current/codes`

- **Query:** `field_id`, `field_value`, `language_cd` (default `01`).
- **Maps to:** `medfile.v_code_lookup_current`
- **200:** single row or 404.

*Defer to v1.1 if not needed for MVP.*

---

## 11. Performance and reliability

| Control | Value (starting point) |
|---------|-------------------------|
| DB statement timeout | 10–30s per request (tune) |
| Connection pool | Sized to concurrent consumer workers + headroom |
| Indexes | Rely on existing `medfile` view indexes ([operations.md](operations.md)) |
| Timeouts | Client 30s; server aborts hung queries |

---

## 12. Security checklist

- [ ] Read-only DB user; no default `postgres` user.
- [ ] No dynamic SQL from client input; parameterized queries only.
- [ ] Validate `ndc_upc_hri` with regex `^[0-9]{11}$` (and reject others).
- [ ] Validate `reference_month` matches `YYYY-MM-01` calendar month.
- [ ] Audit log: optional access log line per request (no PHI—reference only).
- [ ] Rate limit per client id.

---

## 13. Compliance note

MED-File / Wolters Kluwer license terms govern **distribution** of reference data. Ensure API exposure is **allowed** for your subscriber model (internal-only vs customer-facing). This spec does not provide legal advice.

---

## 14. Revision history

| Version | Date | Authoring | Notes |
|---------|------|-----------|--------|
| 1.0 | 2026-03-23 | Engineering | Initial full spec + OpenAPI stub |
