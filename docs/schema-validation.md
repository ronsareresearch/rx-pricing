# Schema validation vs MED-File v2 manual (Phase 2 + Phase 3)

**Source:** [med-file-manual.md](med-file-manual.md). This document maps manual data elements to refinement tables and confirms alignment.

---

## 0. Data tables inventory (all MED-File v2 data files)

Per project scope, there are **25 data files** plus **2 metadata** (MF2DICT, MF2VAL). **Phase 3** implements refinement for all data files except MF2ERR (Phase 4: incremental corrections). Load order and dependencies: [refine/load_order.py](../refine/load_order.py).

| Source file | Description | Refinement table | Status |
|-------------|-------------|------------------|--------|
| **Metadata** | | | |
| MF2VAL | Validation/Translation | `medfile.mf2val` | Implemented |
| MF2DICT | Data Dictionary | — (parsed at runtime; no DB table) | By design |
| **Data – Core and Pricing (12)** | | | |
| MF2NAME | Drug Name File | `medfile.refinement_name` | Implemented (Phase 3) |
| MF2TCGPI | TC-GPI Name File | `medfile.refinement_tcgpi` | Implemented (Phase 3) |
| MF2NDC | NDC File | `medfile.refinement_ndc` | Implemented |
| MF2LAB | Labeler File | `medfile.refinement_lab` | Implemented (Phase 3) |
| MF2GPPC | GPPC File | `medfile.refinement_gppc` | Implemented (Phase 3) |
| MF2ERR | Error Correct File | — | Phase 4 |
| MF2GPR | GPPC Price File | `medfile.refinement_gpr` | Implemented (Phase 3) |
| MF2PRC | NDC Price File | `medfile.refinement_ndc_price` | Implemented |
| MF2MOD | Modifier File | `medfile.refinement_mod` | Implemented (Phase 3) |
| MF2NDCM | NDC Modifier File | `medfile.refinement_ndcm` | Implemented (Phase 3) |
| MF2DRGNM | SDI Drug Name File | `medfile.refinement_drgnm` | Implemented (Phase 3) |
| MF2RTDRG | Routed Drug File | `medfile.refinement_rtdrg` | Implemented (Phase 3) |
| **Data – Clinical / Reference (9)** | | | |
| MF2DFDRG | Drug-Dose Form File | `medfile.refinement_dfdrg` | Implemented (Phase 3) |
| MF2RTDF | Routed Drug Form File | `medfile.refinement_rtdf` | Implemented (Phase 3) |
| MF2DRG | Dispensable Drug File | `medfile.refinement_drg` | Implemented |
| MF2DESC | Description File | `medfile.refinement_desc` | Implemented (Phase 3) |
| MF2RTE | Route File | `medfile.refinement_rte` | Implemented (Phase 3) |
| MF2FRM | Dose Form File | `medfile.refinement_frm` | Implemented (Phase 3) |
| MF2STUOM | Strength-Strength UOM File | `medfile.refinement_stuom` | Implemented (Phase 3) |
| MF2SET | Drug Concept ID to Ingredient Set ID | `medfile.refinement_set` | Implemented (Phase 3) |
| MF2INGS | Ingredient Set ID to Ingredient ID | `medfile.refinement_ings` | Implemented (Phase 3) |
| **Data – Ingredients and Alternate IDs (4)** | | | |
| MF2STR | Ingredient ID to Drug-Strength File | `medfile.refinement_str` | Implemented (Phase 3) |
| MF2IDRG | Ingredient Drug File | `medfile.refinement_idrg` | Implemented (Phase 3) |
| MF2SEC | Secondary Alternate ID File | `medfile.refinement_sec` | Implemented (Phase 3) |
| MF2RNM | Reference Name File | `medfile.refinement_rnm` | Implemented (Phase 3) |

**Phase 3 (current):** All data files above except MF2ERR have refinement tables and rule YAMLs. Entities are processed in **dependency order** (see `refine/load_order.py`): mf2val → lab → rte → frm → stuom → desc → name → tcgpi → gppc → ndc → ndc_price → gpr → mod → ndcm → drgnm → rtdrg → dfdrg → rtdf → drg → set → ings → str → idrg → sec → rnm. MF2ERR is Phase 4 (incremental corrections).

---

### Refine layer coverage (rules and tables)

| Layer | Count | Notes |
|-------|--------|--------|
| **Raw (rxraw)** | **28 tables** | `raw_mf2dict` (loaded once) + **27** from `rxraw.schema.RAW_SOURCE_FILES`. Every MED-File source file has a raw table. |
| **Refine (medfile) Phase 2+3** | **25 entity tables + 1 translation** | **Translation:** `medfile.mf2val`. **Refinement:** 25 tables (e.g. `refinement_ndc`, `refinement_lab`, `refinement_name`, … `refinement_rnm`). |
| **Refine rules (YAML)** | **25 entity rule files** | One per entity in `refine/rules/` (e.g. `mf2val.yaml`, `lab.yaml`, `ndc.yaml`, … `gpr.yaml`). `common.yaml` is shared formatting. |
| **Load order** | **25 entities** | Defined in `refine/load_order.py`; ensures parent tables (e.g. Labeler, Route, Dose Form) before dependents (NDC, Drug Name, etc.). |

**Conclusion:** The refine layer accounts for **all 25 data/summary files** (excluding MF2ERR). Rules and refinement tables exist for each; the pipeline runs in dependency order so referential chains are not broken.

---

## 1. MF2VAL (Validation/Translation File)

**Manual:** § Validation/Translation File (MF2VAL) — Record Position, Type/Length, Picture.

| Code | Name               | Position | Type/Length | Picture | medfile.mf2val column   | Type in schema |
|------|--------------------|----------|-------------|---------|-------------------------|----------------|
| D001 | Field Identifier   | 1-4      | C/4         | X(4)    | field_id                | VARCHAR(4)     |
| D005 | Field Value        | 5-19     | C/15        | X(15)   | field_value             | VARCHAR(15)    |
| D020 | Language Code      | 20-21    | N/2         | 9(2)    | language_cd             | CHAR(2)        |
| D022 | Value Description  | 22-61    | C/40        | X(40)   | value_description       | VARCHAR(40)    |
| D062 | Value Abbreviation | 62-76    | C/15        | X(15)   | value_abbreviation      | VARCHAR(15)    |

**Status:** 100% — All MF2VAL data elements mapped. D077 (Reserve 77-96) not stored per [med-file-manual.md](med-file-manual.md) § Validation/Translation File.

---

## 2. MF2NDC (NDC File)

**Manual:** § NDC File (MF2NDC) — Data elements H001 through H121.

| Code | Data Element Name              | Position | Type/Length | Picture   | refinement_ndc column   | Type in schema   |
|------|--------------------------------|----------|-------------|-----------|--------------------------|------------------|
| H001 | NDC-UPC-HRI                    | 1-11     | C/11        | X(11)     | ndc_upc_hri             | VARCHAR(11)      |
| H012 | Drug Descriptor Identifier     | 12-17    | N/6         | 9(6)      | drug_descriptor_id      | INTEGER          |
| H018 | TEE Code                       | 18-19    | C/2         | X(2)      | tee_code                | CHAR(2)          |
| H020 | DEA Class Code                 | 20-20    | C/1         | X         | dea_class_code          | CHAR(1)          |
| H021 | DESI Code                      | 21-21    | C/1         | X         | desi_code               | CHAR(1)          |
| H022 | RX-OTC Indicator Code          | 22-22    | C/1         | X         | rx_otc_indicator_code   | CHAR(1)          |
| H023 | Generic Product Packaging Code | 23-30    | C/8         | X(8)      | gppc_code               | VARCHAR(8)       |
| H031 | Old NDC-UPC-HRI                | 31-41    | C/11        | X(11)     | old_ndc_upc_hri         | VARCHAR(11)      |
| H042 | New NDC-UPC-HRI                | 42-52    | C/11        | X(11)     | new_ndc_upc_hri         | VARCHAR(11)      |
| H053 | Repackage Code                 | 53-53    | C/1         | X         | repackage_code          | CHAR(1)          |
| H054 | ID Number Format Code          | 54-54    | C/1         | X         | id_number_format_code   | CHAR(1)          |
| H055 | Third-Party Restriction Code   | 55-55    | C/1         | X         | third_party_restriction_code | CHAR(1)     |
| H056 | Knowledge Base Drug Code       | 56-65    | N/10        | 9(10)     | knowledge_base_drug_code| BIGINT            |
| H066 | KDC Flag                       | 66-66    | C/1         | X         | kdc_flag                | CHAR(1)          |
| H067 | Medi-Span Labeler Identifier   | 67-71    | N/5         | 9(5)      | labeler_id              | INTEGER          |
| H072 | Multi-Source Code              | 72-72    | C/1         | X         | multi_source_code       | CHAR(1)          |
| H073 | Name Type Code                 | 73-73    | C/1         | X         | name_type_code          | CHAR(1)          |
| H074 | Item Status Flag               | 74-74    | C/1         | X         | item_status_flag        | CHAR(1)          |
| H075 | Innerpack Code                 | 75-75    | C/1         | X         | innerpack_code          | CHAR(1)          |
| H076 | Clinic Pack Code               | 76-76    | C/1         | X         | clinic_pack_code        | CHAR(1)          |
| H077 | Reserve-1                      | 77-78    | C/2         | X(2)      | reserve_1               | CHAR(2)          |
| H079 | PPG Indicator Code             | 79-79    | C/1         | X         | ppg_indicator_code      | CHAR(1)          |
| H080 | HFPG Indicator Code            | 80-80    | C/1         | X         | hfpg_indicator_code     | CHAR(1)          |
| H081 | Dispensing Unit Code           | 81-81    | C/1         | X         | dispensing_unit_code    | CHAR(1)          |
| H082 | Dollar Rank Code               | 82-82    | C/1         | X         | dollar_rank_code        | CHAR(1)          |
| H083 | Rx Rank Code                   | 83-83    | C/1         | X         | rx_rank_code            | CHAR(1)          |
| H084 | Storage Condition Code         | 84-84    | C/1         | X         | storage_condition_code  | CHAR(1)          |
| H085 | Limited Distribution Code      | 85-86    | C/2         | X(2)      | limited_distribution_code | CHAR(2)        |
| H087 | Old Effective Date             | 87-94    | N/8         | YYYYMMDD  | old_effective_date      | DATE             |
| H095 | New Effective Date             | 95-102   | N/8         | YYYYMMDD  | new_effective_date     | DATE             |
| H103 | Next-Smaller NDC Suffix Number | 103-104  | C/2         | X(2)      | next_smaller_ndc_suffix | CHAR(2)          |
| H105 | Next-Larger NDC Suffix Number  | 105-106  | C/2         | X(2)      | next_larger_ndc_suffix  | CHAR(2)          |
| H107 | Reserve-2                      | 107-119  | C/13        | X(13)     | reserve_2               | VARCHAR(13)      |
| H120 | Transaction CD                 | 120-120  | C/1         | X         | transaction_cd          | CHAR(1)          |
| H121 | Last Change Date               | 121-128  | N/8         | 9(8)      | last_change_date        | DATE             |

Plus SCD2/provenance: run_id, issue_date, source_file, is_current, effective_start_date, effective_end_date, created_at.

**Status:** 100% — All NDC File data elements mapped.

---

## 3. MF2PRC (NDC Price File)

**Manual:** § NDC Price File (MF2PRC) — Data elements **M001** through **M057** (M-codes, not L-codes).

| Code | Data Element Name     | Position | Type/Length | Picture   | refinement_ndc_price column | Type in schema   |
|------|------------------------|----------|-------------|-----------|-----------------------------|------------------|
| M001 | NDC-UPC-HRI            | 1-11     | C/11        | X(11)     | ndc_upc_hri                 | VARCHAR(11)      |
| M012 | Price Code             | 12-12    | C/1         | X         | price_code                  | CHAR(1)          |
| M013 | Price Effective Date   | 13-20    | N/8         | 9(8)      | price_effective_date        | DATE             |
| M021 | Unit Price             | 21-31    | N/11        | 9(5)V9(6) | unit_price                  | DECIMAL(11,6)    |
| M032 | Unit Price - Extended  | 32-44    | N/13        | 9(8)V9(5) | unit_price_extended         | DECIMAL(13,5)    |
| M045 | Package Price          | 45-54    | N/10        | 9(8)V9(2) | package_price               | DECIMAL(10,2)    |
| M055 | AWP Indicator Code     | 55-55    | C/1         | X         | awp_indicator_code          | CHAR(1)          |
| M056 | Transaction CD         | 56-56    | C/1         | X         | transaction_cd              | CHAR(1)          |
| M057 | Last Change Date       | 57-64    | N/8         | 9(8)      | last_change_date            | DATE             |

Price Code (M012) valid values: A=AWP, D=DP, H=HCFA FFP (CMS FUL), U=HCFA FFP unit dose, W=WAC.

**Status:** 100% — All NDC Price File data elements mapped; L-codes in MF2DICT refer to GPPC Price File (MF2GPR), not MF2PRC.

---

## 4. MF2DRG (Dispensable Drug File)

**Manual:** § Dispensable Drug File (MF2DRG) — Data elements **T001** through **T115**.

| Code | Data Element Name        | Position | Type/Length | Picture  | refinement_drg column   | Type in schema   |
|------|--------------------------|----------|-------------|----------|--------------------------|------------------|
| T001 | Concept Type             | 1-5      | N/5         | 9(5)     | concept_type             | INTEGER          |
| T006 | Country Code             | 6-7      | N/2         | 9(2)     | country_code             | CHAR(2)          |
| T008 | Concept ID               | 8-17     | N/10        | 9(10)    | concept_id               | BIGINT           |
| T018 | Transaction CD           | 18-18    | C/1         | X        | transaction_cd           | CHAR(1)          |
| T019 | Routed Drug ID           | 19-28    | N/10        | 9(10)    | routed_drug_id           | BIGINT           |
| T029 | Dose Form ID             | 29-33    | N/5         | 9(5)     | dose_form_id             | INTEGER          |
| T034 | Strength                 | 34-48    | C/15        | X(15)    | strength                 | VARCHAR(15)      |
| T049 | Strength Unit of Measure | 49-63    | C/15        | X(15)    | strength_uom             | VARCHAR(15)      |
| T064 | Name Source              | 64-64    | N/1         | 9(1)     | name_source              | SMALLINT         |
| T065 | Device Flag              | 65-65    | N/1         | 9(1)     | device_flag              | SMALLINT         |
| T066 | Status                   | 66-66    | N/1         | 9(1)     | status                   | SMALLINT         |
| T067 | Link Value               | 67-76    | N/10        | 9(10)    | link_value               | BIGINT           |
| T077 | Link Date                | 77-84    | N/8         | YYYYMMDD | link_date                | DATE             |
| T085 | Routed Drug Form ID      | 85-94    | N/10        | 9(10)    | routed_drug_form_id      | BIGINT           |
| T095 | Drug-Dose Form ID        | 95-104   | N/10        | 9(10)    | drug_dose_form_id        | BIGINT           |
| T105 | Strength-Strength UOM ID | 105-114  | N/10        | 9(10)    | strength_strength_uom_id | BIGINT           |
| T115 | Reserve                  | 115-144  | C/30        | X(30)    | reserve                  | VARCHAR(30)      |

Plus SCD2/provenance: run_id, issue_date, source_file, is_current, effective_start_date, effective_end_date, created_at.

**Note:** Concept Type 00004 (Dispensable Drug) is the only value used in the Dispensable Drug File; Country Code 01 (USA) is the only value in use (per manual).

**Status:** 100% — All Dispensable Drug File data elements mapped.

---

## 5. Run metadata (rxraw.loaded_runs, medfile.refine_runs)

Not from a MED-File source. **rxraw:** `loaded_runs` (one row per run; `file_id`, `file_date`, `volume_number`, `supplement_number`, `loaded_at`) — see §7.1. **medfile:** `refine_runs` (one row per refinement run; links to `rxraw.loaded_runs` via `file_id`) — see §7.2. Design in [architecture.md](architecture.md) §2.4.

---

## 6. Raw layer (rxraw.raw_*)

**All** MED-File v2 data and metadata files are loaded into raw tables so every delivery is queryable by file and by date for history true-up and maintenance. Implemented schema: **rxraw** (see `rxraw.schema`).

Each raw table has the same structure:

| Column            | Type         | Purpose |
|-------------------|--------------|--------|
| file_id           | UUID         | Which load run (one per run). |
| file_date         | DATE         | Delivery issue date (from MF2SUM). |
| source_file       | VARCHAR(30)  | Filename (e.g. MF2NDC). **Identifies file.** |
| line_number       | BIGINT       | Line number in the source file. |
| volume_number     | VARCHAR(10)  | Volume from MF2SUM. **History true-up / sequence.** |
| supplement_number | VARCHAR(10)  | Supplement from MF2SUM. **History true-up.** |
| pos1 .. pos80     | TEXT         | Pipe-delimited positions (no type conversion). |

**Indexes:** `(file_id)`, `(file_date, source_file)` for filtering by run or by date+file.

**Tables (28 total):** One table per MED-File source. **27** from `RAW_SOURCE_FILES` (below); plus **`raw_mf2dict`** (Data Dictionary, loaded once per schema). Naming: `raw_` + lowercase filename (e.g. MF2NDC → raw_mf2ndc).

| Source file | Raw table    | Source file | Raw table    |
|-------------|--------------|-------------|--------------|
| MF2DICT     | raw_mf2dict  | MF2DRG      | raw_mf2drg    |
| MF2SUM      | raw_mf2sum   | MF2DESC     | raw_mf2desc   |
| MF2VAL      | raw_mf2val   | MF2RTE      | raw_mf2rte    |
| MF2NAME     | raw_mf2name  | MF2FRM      | raw_mf2frm    |
| MF2TCGPI    | raw_mf2tcgpi | MF2STUOM    | raw_mf2stuom  |
| MF2NDC      | raw_mf2ndc   | MF2SET      | raw_mf2set    |
| MF2LAB      | raw_mf2lab   | MF2INGS     | raw_mf2ings   |
| MF2GPPC     | raw_mf2gppc  | MF2STR      | raw_mf2str    |
| MF2ERR      | raw_mf2err   | MF2IDRG     | raw_mf2idrg   |
| MF2GPR      | raw_mf2gpr   | MF2SEC      | raw_mf2sec    |
| MF2PRC      | raw_mf2prc   | MF2RNM      | raw_mf2rnm    |
| MF2MOD      | raw_mf2mod   | MF2RTDRG    | raw_mf2rtdrg  |
| MF2NDCM     | raw_mf2ndcm  | MF2DFDRG    | raw_mf2dfdrg  |
| MF2DRGNM    | raw_mf2drgnm | MF2RTDF     | raw_mf2rtdf   |

Position-to-manual mapping for refined entities: §1 (MF2VAL), §2 (MF2NDC), §3 (MF2PRC), §4 (MF2DRG). Other files: use [med-file-manual.md](med-file-manual.md) and pos1 = first pipe field, etc.

**Example: query by file and date for true-up**

```sql
SELECT file_id, file_date, source_file, volume_number, supplement_number, COUNT(*) AS row_count
FROM rxraw.raw_mf2ndc
WHERE file_date >= '2022-01-01'
GROUP BY file_id, file_date, source_file, volume_number, supplement_number
ORDER BY file_date, source_file;
```

**Example: custom view from raw**

```sql
CREATE VIEW my_ndc_raw AS
SELECT file_id, file_date, source_file, volume_number, line_number,
       pos1 AS ndc_upc_hri, pos2 AS drug_descriptor_id, pos3 AS tee_code
FROM rxraw.raw_mf2ndc;
```

---

## 7. Schema DDL (all tables)

Canonical DDL for the **rxraw** and **medfile** schemas. Full DDL is generated by code: `rxraw.schema.get_raw_ddl()` and `refine.schema.get_ddl()`.

### 7.1 rxraw schema

**Run metadata: `rxraw.loaded_runs`**

```sql
CREATE SCHEMA IF NOT EXISTS rxraw;

CREATE TABLE IF NOT EXISTS rxraw.loaded_runs (
    file_id           UUID NOT NULL PRIMARY KEY,
    file_date         DATE NOT NULL,
    volume_number     VARCHAR(10) NOT NULL,
    supplement_number VARCHAR(10) NOT NULL DEFAULT '',
    loaded_at         TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX IF NOT EXISTS ix_loaded_runs_file_date_volume ON rxraw.loaded_runs (file_date, volume_number);
```

**Raw tables: `rxraw.raw_*` (28 tables)**

Each raw table has the same column set. Example for `rxraw.raw_mf2ndc`:

```sql
CREATE TABLE IF NOT EXISTS rxraw.raw_mf2ndc (
    file_id           UUID NOT NULL,
    file_date         DATE NOT NULL,
    source_file       VARCHAR(30) NOT NULL DEFAULT 'MF2NDC',
    line_number       BIGINT NOT NULL,
    volume_number     VARCHAR(10) NOT NULL DEFAULT '',
    supplement_number VARCHAR(10) NOT NULL DEFAULT '',
    pos1 TEXT, pos2 TEXT, pos3 TEXT, ... , pos80 TEXT
);
CREATE INDEX IF NOT EXISTS ix_raw_mf2ndc_file_id ON rxraw.raw_mf2ndc (file_id);
CREATE INDEX IF NOT EXISTS ix_raw_mf2ndc_file_date_source ON rxraw.raw_mf2ndc (file_date, source_file);
```

**All rxraw tables:** Run metadata: `loaded_runs`. Raw data (28 tables): `raw_mf2dict`, `raw_mf2sum`, `raw_mf2val`, `raw_mf2name`, `raw_mf2tcgpi`, `raw_mf2ndc`, `raw_mf2lab`, `raw_mf2gppc`, `raw_mf2err`, `raw_mf2gpr`, `raw_mf2prc`, `raw_mf2mod`, `raw_mf2ndcm`, `raw_mf2drgnm`, `raw_mf2rtdrg`, `raw_mf2dfdrg`, `raw_mf2rtdf`, `raw_mf2drg`, `raw_mf2desc`, `raw_mf2rte`, `raw_mf2frm`, `raw_mf2stuom`, `raw_mf2set`, `raw_mf2ings`, `raw_mf2str`, `raw_mf2idrg`, `raw_mf2sec`, `raw_mf2rnm`.

---

### 7.2 medfile schema (refinement)

**Run metadata: `medfile.refine_runs`**

```sql
CREATE SCHEMA IF NOT EXISTS medfile;

CREATE TABLE IF NOT EXISTS medfile.refine_runs (
    run_id              UUID NOT NULL PRIMARY KEY,
    file_id             UUID NOT NULL,
    file_type           CHAR(1) NOT NULL,
    file_date           DATE NOT NULL,
    volume_number       VARCHAR(10) NOT NULL,
    supplement_number   VARCHAR(10) NOT NULL DEFAULT '',
    status              VARCHAR(20) NOT NULL DEFAULT 'in_progress',
    started_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at        TIMESTAMPTZ
);
```

**Entity tables (25):** Structure depends on `history_type` in `refine/rules/<entity>.yaml`:

| history_type | Purpose | Extra columns (besides rule-defined) |
|--------------|---------|--------------------------------------|
| **replace** | Replace whole row per run (e.g. mf2val) | `run_id UUID NOT NULL`; PK = business_key |
| **scd2** | Type 2 slowly changing dimension | `id BIGSERIAL PRIMARY KEY`, `run_id`, `issue_date`, `source_file`, `is_current`, `effective_start_date`, `effective_end_date`, `created_at` |
| **append_only** | Append-only (e.g. ndc_price, gpr) | `id BIGSERIAL PRIMARY KEY`, `run_id`, `issue_date`, `source_file`, `is_active`, `created_at` |

**All 25 refinement tables:** `mf2val` (translation), then `refinement_lab`, `refinement_rte`, `refinement_frm`, `refinement_stuom`, `refinement_desc`, `refinement_name`, `refinement_tcgpi`, `refinement_gppc`, `refinement_ndc`, `refinement_ndc_price`, `refinement_gpr`, `refinement_mod`, `refinement_ndcm`, `refinement_drgnm`, `refinement_rtdrg`, `refinement_dfdrg`, `refinement_rtdf`, `refinement_drg`, `refinement_set`, `refinement_ings`, `refinement_str`, `refinement_idrg`, `refinement_sec`, `refinement_rnm`. Column definitions come from `refine/rules/*.yaml`; load order from `refine/load_order.py`.
