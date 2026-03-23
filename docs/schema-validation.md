# Schema Validation and Coverage

**Source of truth:** [med-file-manual.md](med-file-manual.md), `refine/rules/*.yaml`, `refine/load_order.py`, `rxraw.schema`, and `refine.schema`.

This document answers two questions:

1. Which MED-File sources are represented in the project?
2. How do the main raw, refined, and view schemas line up with that source material?

---

## Coverage Summary

The project currently covers all normal MED-File sources in raw ingestion and all refinement entities except MF2ERR correction handling.

| Layer | Coverage |
|-------|----------|
| Raw | 28 tables: `raw_mf2dict` plus 27 MED-File source tables |
| Refine | `medfile.mf2val` plus 25 refinement tables |
| Views | 9 regular views (3 normalized current + 3 legacy entity + 3 legacy PCIP) and 6 materialized monthly views (15 total) |

Load order for refinement:

```text
mf2val -> lab -> rte -> frm -> stuom -> desc -> name -> tcgpi -> gppc -> ndc -> ndc_price -> gpr -> mod -> ndcm -> drgnm -> rtdrg -> dfdrg -> rtdf -> drg -> set -> ings -> str -> idrg -> sec -> rnm
```

MF2ERR status:

- loaded into raw
- not yet applied during refinement

---

## Source File Inventory

| Source file | Description | Raw table | Refinement target | Status |
|-------------|-------------|-----------|-------------------|--------|
| MF2DICT | Data Dictionary | `rxraw.raw_mf2dict` | none by design | Implemented |
| MF2SUM | Summary | `rxraw.raw_mf2sum` | none by design | Implemented |
| MF2VAL | Validation / Translation | `rxraw.raw_mf2val` | `medfile.mf2val` | Implemented |
| MF2NAME | Drug Name | `rxraw.raw_mf2name` | `medfile.refinement_name` | Implemented |
| MF2TCGPI | TC-GPI Name | `rxraw.raw_mf2tcgpi` | `medfile.refinement_tcgpi` | Implemented |
| MF2NDC | NDC | `rxraw.raw_mf2ndc` | `medfile.refinement_ndc` | Implemented |
| MF2LAB | Labeler | `rxraw.raw_mf2lab` | `medfile.refinement_lab` | Implemented |
| MF2GPPC | GPPC | `rxraw.raw_mf2gppc` | `medfile.refinement_gppc` | Implemented |
| MF2ERR | Error Correct | `rxraw.raw_mf2err` | none yet | Raw only |
| MF2GPR | GPPC Price | `rxraw.raw_mf2gpr` | `medfile.refinement_gpr` | Implemented |
| MF2PRC | NDC Price | `rxraw.raw_mf2prc` | `medfile.refinement_ndc_price` | Implemented |
| MF2MOD | Modifier | `rxraw.raw_mf2mod` | `medfile.refinement_mod` | Implemented |
| MF2NDCM | NDC Modifier | `rxraw.raw_mf2ndcm` | `medfile.refinement_ndcm` | Implemented |
| MF2DRGNM | SDI Drug Name | `rxraw.raw_mf2drgnm` | `medfile.refinement_drgnm` | Implemented |
| MF2RTDRG | Routed Drug | `rxraw.raw_mf2rtdrg` | `medfile.refinement_rtdrg` | Implemented |
| MF2DFDRG | Drug-Dose Form | `rxraw.raw_mf2dfdrg` | `medfile.refinement_dfdrg` | Implemented |
| MF2RTDF | Routed Drug Form | `rxraw.raw_mf2rtdf` | `medfile.refinement_rtdf` | Implemented |
| MF2DRG | Dispensable Drug | `rxraw.raw_mf2drg` | `medfile.refinement_drg` | Implemented |
| MF2DESC | Description | `rxraw.raw_mf2desc` | `medfile.refinement_desc` | Implemented |
| MF2RTE | Route | `rxraw.raw_mf2rte` | `medfile.refinement_rte` | Implemented |
| MF2FRM | Dose Form | `rxraw.raw_mf2frm` | `medfile.refinement_frm` | Implemented |
| MF2STUOM | Strength-Strength UOM | `rxraw.raw_mf2stuom` | `medfile.refinement_stuom` | Implemented |
| MF2SET | Concept to Ingredient Set | `rxraw.raw_mf2set` | `medfile.refinement_set` | Implemented |
| MF2INGS | Ingredient Set to Ingredient | `rxraw.raw_mf2ings` | `medfile.refinement_ings` | Implemented |
| MF2STR | Ingredient to Drug Strength | `rxraw.raw_mf2str` | `medfile.refinement_str` | Implemented |
| MF2IDRG | Ingredient Drug | `rxraw.raw_mf2idrg` | `medfile.refinement_idrg` | Implemented |
| MF2SEC | Secondary Alternate ID | `rxraw.raw_mf2sec` | `medfile.refinement_sec` | Implemented |
| MF2RNM | Reference Name | `rxraw.raw_mf2rnm` | `medfile.refinement_rnm` | Implemented |

---

## Raw Schema Shape

Every `rxraw.raw_*` table uses the same base layout:

| Column | Purpose |
|--------|---------|
| `file_id` | identifies the loaded run |
| `file_date` | issue date from `MF2SUM` |
| `source_file` | MED-File source filename |
| `line_number` | source line number |
| `volume_number` | volume from the summary file |
| `supplement_number` | supplement from the summary file |
| `pos1` .. `pos80` | vendor positions stored as text |

Run registry:

- `rxraw.loaded_runs(file_id, file_date, volume_number, supplement_number, loaded_at)`

This layer is intentionally close to the source data so refinement can be replayed or audited.

---

## Refinement Schema Shape

Run registry:

- `medfile.refine_runs(run_id, file_id, file_type, file_date, volume_number, supplement_number, status, started_at, completed_at)`

Entity table behaviors are determined by `history_type` in each rule file:

| `history_type` | Behavior |
|----------------|----------|
| `replace` | replace current keyed rows |
| `scd2` | maintain current plus historical versions |
| `append_only` | keep append-only active history |

Standard refine provenance columns are added by the schema generator:

- `run_id`
- `issue_date`
- `source_file`
- plus `is_current` and effective dates for `scd2`
- plus `is_active` for `append_only`

Indexes per history type:

- `scd2`: business key + `is_current` index, business key + temporal dates index
- `append_only`: business key index
- `replace`: primary key on business key

The view runner adds additional performance indexes (defined in `view/indexes.py`) for LATERAL join patterns, price ranking queries, and refine_runs status filtering.

---

## Key Entity Mappings

### MF2VAL -> `medfile.mf2val`

| Manual code | Column |
|-------------|--------|
| D001 | `field_id` |
| D005 | `field_value` |
| D020 | `language_cd` |
| D022 | `value_description` |
| D062 | `value_abbreviation` |

### MF2NDC -> `medfile.refinement_ndc`

Representative mappings:

| Manual code | Column |
|-------------|--------|
| H001 | `ndc_upc_hri` |
| H012 | `drug_descriptor_id` |
| H018 | `tee_code` |
| H023 | `gppc_code` |
| H067 | `labeler_id` |
| H072 | `multi_source_code` |
| H074 | `item_status_flag` |
| H082 | `dollar_rank_code` |
| H083 | `rx_rank_code` |
| H085 | `limited_distribution_code` |
| H120 | `transaction_cd` |
| H121 | `last_change_date` |

### MF2PRC -> `medfile.refinement_ndc_price`

Representative mappings:

| Manual code | Column |
|-------------|--------|
| M001 | `ndc_upc_hri` |
| M012 | `price_code` |
| M013 | `price_effective_date` |
| M021 | `unit_price` |
| M032 | `unit_price_extended` |
| M045 | `package_price` |
| M055 | `awp_indicator_code` |
| M056 | `transaction_cd` |
| M057 | `last_change_date` |

### MF2DRG -> `medfile.refinement_drg`

Representative mappings:

| Manual code | Column |
|-------------|--------|
| T001 | `concept_type` |
| T008 | `concept_id` |
| T019 | `routed_drug_id` |
| T029 | `dose_form_id` |
| T034 | `strength` |
| T049 | `strength_uom` |
| T067 | `link_value` |
| T077 | `link_date` |
| T085 | `routed_drug_form_id` |
| T095 | `drug_dose_form_id` |
| T105 | `strength_strength_uom_id` |

For full field-by-field interpretation, use the vendor manual together with the corresponding refine rule file.

---

## View Inventory

Implemented views in schema `medfile` (15 managed views):

Normalized current views (regular):

- `v_product_package_current` — one row per `ndc_upc_hri`
- `v_product_package_price_current` — one row per `(ndc_upc_hri, price_code)`
- `v_product_package_modifier_current` — one row per `(ndc_upc_hri, modifier_code)`

Legacy entity views (regular, deprecated):

- `v_ndc` — **deprecated**, use `v_product_package_current`
- `v_ndc_price` — **deprecated**, use `v_product_package_price_current`
- `v_drg` — active

Monthly historical views (materialized, concurrently refreshable):

- `v_product_package_monthly` — unique on `(reference_month, ndc_upc_hri)`
- `v_product_package_price_monthly` — unique on `(reference_month, ndc_upc_hri, price_code)`
- `v_product_package_price_awp_monthly` — unique on `(reference_month, ndc_upc_hri)`
- `v_product_package_price_wac_monthly` — unique on `(reference_month, ndc_upc_hri)`
- `v_product_package_price_dp_monthly` — unique on `(reference_month, ndc_upc_hri)`
- `v_gpi_ndc_equivalent_monthly` — unique on `(reference_month, gpi, ndc_upc_hri)`

Legacy PCIP-oriented views (regular):

- `v_ndc_pcip_reference` — **deprecated**, use `v_product_package_current` + `v_product_package_price_current`
- `v_gpi_equivalents` — active
- `v_drg_maintenance` — active

Entity views are derived from refine rules and MF2VAL lookups. Monthly views are materialized for query performance and refreshed with `REFRESH MATERIALIZED VIEW CONCURRENTLY` so reads are never blocked. Each materialized view has a unique index (required for concurrent refresh) plus query indexes on NDC, GPI, month, drug name, and labeler for interactive UI use. Price-type monthly views filter to a single price code for a cleaner 1:1 grain per NDC per month. PCIP-oriented views are hand-authored SQL builders over current refinement tables. The view runner maintains a managed-view registry and drops orphaned views (both regular and materialized) on each run.
