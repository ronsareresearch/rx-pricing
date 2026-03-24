# Recommendations — proposed `medfile` views (pharmacy claims intelligence / PCIP-aligned)

**Role:** Product-facing recommendations for **additional** PostgreSQL views and materialized views in schema `medfile`, so a **pharmacy claims intelligence** platform (exemplar: **PCIP** — Pharmacy Claims Intelligence Platform) can **cover all major analytic bases** without re-implementing Medi-Span semantics in the consumer repo.

**Audience:** Product, data engineering, and baseline (`rx-pricing`) owners reviewing scope before implementation.

**Related:** [architecture.md](architecture.md), [schema-validation.md](schema-validation.md), [normalized-view-design.md](normalized-view-design.md), [operations.md](operations.md) (monthly rules), [reference-api-spec.md](reference-api-spec.md).

**Note:** PCIP BRD and agile backlog may live **outside** this repository. This document uses **PCIP-style** capability areas (payer pharmacy audits, waste categories, benchmarks, clinical add-ons) as a **requirements lens**, not as a source-of-truth link.

---

## 1. Principles

| Principle | Implication |
|-----------|-------------|
| **Single semantic source** | Dollar eligibility and drug flags used in audits should come from **versioned `medfile` views** (or monthly matviews), not duplicated logic in the claims app. |
| **Current vs monthly** | **Current** views answer “what is true today.” **Monthly** views answer “what was true for Medi-Span file month *M*” when reproducing historical audits (`reference_month`). |
| **Grain clarity** | Every proposed object has one **primary grain** and a **unique key** suitable for `REFRESH MATERIALIZED VIEW CONCURRENTLY` (where materialized). |
| **Scope boundary** | This repo **does not** store claims, enrollment, or computed savings—only **drug reference** aligned to MED-File. |

---

## 2. PCIP-style capability map → reference needs

The table below maps **typical platform pillars** to what the **baseline** must expose. “Covered” means an existing view (or small join path) is sufficient for many implementations; “Gap” suggests a **new or extended** view.

| Capability area | Examples | Covered today? | Gap / proposal |
|-----------------|----------|----------------|----------------|
| **A. Lite wedge — Data Area 1** (generic / brand) | Brand-when-generic, GFR-style metrics, therapeutic class cuts, prescriber-facing rollups (claims app aggregates) | **Yes** — NDC package + GPI + equivalence current & monthly | Optional: **GPI / GPPC monthly** for class labels as-of month; **modifier monthly** if audits need historical modifier context |
| **B. Lite wedge — Data Area 2** (payment / consistency) | Cost-per-unit outliers vs internal distribution, AWP/WAC/DP benchmarks from reference | **Yes** — current + monthly price slices | Optional: **price history** by month (narrow) if you need “price in effect” audit trail beyond latest-per-code |
| **C. Full tier — deeper waste categories** | Channel, days’ supply, specialty proxies, maintenance flags | **Largely yes** — package view fields + code lookups | Same as A; ensure **TEE / multi-source / maintenance** present on monthly package (already on `v_product_package_monthly`) |
| **D. PBM transparency** (data-gated) | Spread, rebate reconciliation | **Partial** — reference prices help; **no PBM feeds here** | No new medfile views until feed semantics defined; may need **contract-specific** views outside MED-File |
| **E. External benchmarks** | NADAC, licensed AWP, peer percentiles | **NADAC / peer not in MED-File** | **Out of scope** for this pipeline; consumer ETL. **Medi-Span AWP/WAC/DP** already in price views |
| **F. Clinical & quality** (gated) | High-risk lists, Beers-aligned subsets, ingredient-level signals, therapeutic duplication proxies | **Partial** — rich **clinical** and **ingredient** *current* views | **Gap:** **monthly** clinical + ingredient surfaces for retrospective clinical audits |
| **G. Data quality & lineage** | “Which reference run powered this month?” | **Yes** — `refine_runs`, monthly cols `reference_run_id`, `reference_file_date` | Optional: small **metadata** view listing published months + run ids (convenience) |
| **H. Integration** | Thin API, batch NDC enrichment | **Spec only** — [reference-api-spec.md](reference-api-spec.md) | Extend OpenAPI when new matviews exist |

---

## 3. Inventory — implemented today (baseline)

### 3.1 Regular views (current state)

As in [operations.md](operations.md) / [schema-validation.md](schema-validation.md):

- **Family 1:** `v_product_package_current`, `v_product_package_price_current`, `v_product_package_modifier_current`, `v_product_package_price_history`
- **Family 2:** `v_gpi_current`, `v_gppc_current`, `v_gpi_ndc_equivalent_current`
- **Family 3:** `v_drug_name_current`, `v_routed_drug_current`, `v_drug_dose_form_current`, `v_routed_drug_form_current`, `v_dispensable_drug_current`, `v_dispensable_drug_rollup_current`
- **Family 4:** `v_concept_ingredient_set_current`, `v_ingredient_set_member_current`, `v_ingredient_current`, `v_concept_ingredient_current`
- **Family 5:** `v_code_lookup_current`, `v_concept_description_current`, `v_concept_reference_name_current`, `v_alternate_id_current`
- **Audit:** `v_error_corrections`

### 3.2 Materialized monthly views

- `v_product_package_monthly`
- `v_product_package_price_monthly`
- `v_product_package_price_awp_monthly` / `_wac_monthly` / `_dp_monthly`
- `v_gpi_ndc_equivalent_monthly`

### 3.3 Architectural gap (from [architecture.md](architecture.md))

- **Monthly** materialized views for **clinical**, **ingredient**, and **standalone GPI/GPPC** families are **not** implemented yet (equivalence monthly exists).

---

## 4. Proposed views — comprehensive list

Below, **Priority** is a recommendation for sequencing: **P0** = strong fit for PCIP-style MVP + retrospective audits; **P1** = Full tier / clinical prep; **P2** = nice-to-have or low frequency.

### 4.1 Family 2 — GPI / packaging (monthly)

| Proposed name | Type | Grain (unique for CONCURRENTLY) | Priority | Rationale |
|---------------|------|----------------------------------|----------|-----------|
| **`v_gpi_monthly`** | Matview | `(reference_month, gpi)` | **P0** | Therapeutic class and TC-GPI **labels as-of** audit month—avoids applying today’s `v_gpi_current` to historical claims. |
| **`v_gppc_monthly`** | Matview | `(reference_month, gppc_code)` | **P0** | Packaging-level GPI link and package attributes as-of month; supports class/rollups tied to GPPC history. |
| **`v_product_package_modifier_monthly`** | Matview | `(reference_month, ndc_upc_hri, modifier_code)` or appropriate key | **P1** | If audits require **modifier** context by file month (not only current). |

**Implementation note:** Mirror [view/monthly_views.py](view/monthly_views.py): `selected_runs` + `reference_file_date` + SCD2 **as-of** predicates on `refinement_gppc`, `refinement_tcgpi`, `refinement_mod` / `refinement_ndcm` as needed.

---

### 4.2 Family 3 — Clinical hierarchy (monthly)

Each current view in [view/clinical_views.py](view/clinical_views.py) should have a **monthly** counterpart if consumers run **retrospective** clinical or “drug identity as-of” logic.

| Proposed name | Type | Grain | Priority | Rationale |
|---------------|------|-------|----------|-----------|
| **`v_drug_name_monthly`** | Matview | `(reference_month, concept_type, country_code, concept_id)` | **P1** | Drug name concepts as-of month. |
| **`v_routed_drug_monthly`** | Matview | `(reference_month, concept_type, country_code, concept_id)` | **P1** | Routed drug + route labels as-of month. |
| **`v_drug_dose_form_monthly`** | Matview | `(reference_month, concept_type, country_code, concept_id)` | **P2** | DDF layer for deep clinical rules. |
| **`v_routed_drug_form_monthly`** | Matview | `(reference_month, concept_type, country_code, concept_id)` | **P2** | RDF layer. |
| **`v_dispensable_drug_monthly`** | Matview | `(reference_month, concept_type, country_code, concept_id)` | **P1** | DDID as-of month—common anchor for clinical measures. |
| **`v_dispensable_drug_rollup_monthly`** | Matview | `(reference_month, …)` match current rollup grain | **P1** | Pre-flattened hierarchy for BI/API simplicity (wider rows). |

**Implementation note:** Replace `is_current = true` with **as-of** temporal logic (same pattern as `v_product_package_monthly`). Description LATERALs must use **effective** description rows as of `reference_file_date`, not `is_current`.

---

### 4.3 Family 4 — Ingredient composition (monthly)

| Proposed name | Type | Grain | Priority | Rationale |
|---------------|------|-------|----------|-----------|
| **`v_ingredient_monthly`** | Matview | `(reference_month, ingredient_id)` | **P1** | Strength and ingredient drug name as-of month (high-risk ingredient rules, interaction stubs). |
| **`v_concept_ingredient_set_monthly`** | Matview | `(reference_month, concept_type, country_code, concept_id)` | **P2** | Concept → set mapping history. |
| **`v_ingredient_set_member_monthly`** | Matview | `(reference_month, ingredient_set_id, ingredient_id)` | **P2** | Set membership history. |
| **`v_concept_ingredient_monthly`** | Matview | `(reference_month, concept_type, country_code, concept_id, ingredient_id)` | **P1** | Full bridge for “which ingredients for this DDID/name concept in month *M*.” |

---

### 4.4 Family 5 — Terminology & crosswalk (monthly)

| Proposed name | Type | Grain | Priority | Rationale |
|---------------|------|-------|----------|-----------|
| **`v_alternate_id_monthly`** | Matview | `(reference_month, external_drug_id, alternate_drug_id)` or current grain + month | **P2** | Crosswalk audits when vendor corrections shift IDs month-to-month. |
| **`v_concept_reference_name_monthly`** | Matview | `(reference_month, concept_type, country_code, concept_id)` | **P2** | Brand/generic naming as-of month for reporting. |
| **`v_code_lookup_monthly`** | Usually **not needed** | — | **Defer** | MF2VAL-driven lookups often stable; build only if proven drift breaks audits. |

---

### 4.5 Family 1 — Packaged drug (incremental)

| Proposed name | Type | Grain | Priority | Rationale |
|---------------|------|-------|----------|-----------|
| **`v_product_package_price_history_monthly`** (or narrow “snapshot”) | Matview or regular | Depends on definition | **P2** | Only if audits need **multiple** active price rows per NDC/code **as-of** a month boundary (today’s monthly views pick **latest** per code). |

**Caution:** Avoid exploding row counts; prefer keeping “latest as-of month” as default and add history only for defined price types if needed.

---

### 4.6 Convenience / composite (optional, regular views)

These are **not** always required; consumers can JOIN. Add only if repeated join complexity justifies maintenance.

| Proposed name | Type | Priority | Rationale |
|---------------|------|----------|-----------|
| **`v_ndc_clinical_bridge_current`** | Regular view | **P2** | NDC → DDID (and key clinical ids) in one place—**high join cost** to maintain; document preferred join path instead unless demand is clear. |
| **`v_reference_publication_index`** | Regular view | **P3** | Distinct `reference_month` + `reference_run_id` + `reference_file_date` from monthly matviews or `refine_runs` for UI/API “picker.” |

---

## 5. Phased build plan (recommended)

| Phase | Scope | Proposed views | Outcome |
|-------|--------|----------------|---------|
| **Phase 0 — No new views** | MVP PCIP-style DA1/DA2 with retrospective NDC + prices + equivalence | Use existing 6 matviews + current views | Validates consumer join contract ([reference-api-spec.md](reference-api-spec.md)). |
| **Phase 1 — GPI packaging monthly (P0)** | Class rollups and GPPC-stable audits by `reference_month` | `v_gpi_monthly`, `v_gppc_monthly` | Closes largest **non-NDC** monthly gap for payer analytics. |
| **Phase 2 — Clinical monthly (P1)** | Retrospective clinical / DDID rules | `v_dispensable_drug_monthly`, `v_drug_name_monthly`, `v_routed_drug_monthly`, rollup monthly | Supports clinical-quality modules without misapplying current hierarchy. |
| **Phase 3 — Ingredient monthly (P1–P2)** | Ingredient-level and bridge rules | `v_ingredient_monthly`, `v_concept_ingredient_monthly`, then set/member if needed | Supports high-risk / overlap-style analytics. |
| **Phase 4 — Modifiers / crosswalk / history (P2)** | Edge audits | Modifier monthly, `v_alternate_id_monthly`, optional price-history snapshot | Only after concrete use cases. |

---

## 6. API alignment

When the **thin reference API** is implemented, extend [openapi/medfile-reference-v1.yaml](openapi/medfile-reference-v1.yaml) with:

- Paths for **monthly GPI/GPPC** (e.g. `GET /v1/monthly/{reference_month}/gpi/{gpi}`, batch variants).
- Paths for **monthly clinical** entities (by concept keys) as consumers adopt Phase 2+.

Keep **batch NDC package** endpoints as the **primary** enrichment path for claims engines.

---

## 7. Risks and constraints

| Risk | Mitigation |
|------|------------|
| **Refresh duration** | Add matviews incrementally; measure `REFRESH MATERIALIZED VIEW CONCURRENTLY` after each. |
| **Storage** | Clinical monthly set is wide; consider starting with **DDID + drug name** only. |
| **Duplicate business logic** | Views expose **reference state** only; substitution **eligibility** rules stay in the consumer rule engine with explicit methodology IDs. |
| **Licensing** | MED-File distribution rules still apply to any API exposing these fields. |

---

## 8. Decision checklist (for your review)

- [ ] Confirm **Phase 1** (`v_gpi_monthly`, `v_gppc_monthly`) is in scope for next baseline release.
- [ ] Confirm **clinical monthly** is required before any **clinical module GA** in the consumer product.
- [ ] Confirm **modifier monthly** is needed or defer.
- [ ] Align **unique indexes** with expected query patterns (NDC vs GPI vs concept keys).
- [ ] Update [architecture.md](architecture.md) **Current Gaps** when a phase ships.

---

## 9. Document control

| Version | Date | Notes |
|---------|------|--------|
| 1.0 | 2026-03-23 | Initial comprehensive recommendations (PCIP-aligned pharmacy claims intelligence) |
