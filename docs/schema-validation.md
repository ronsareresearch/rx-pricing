# Phase 2 schema validation vs MED-File v2 manual

**Source:** [med-file-manual.md](med-file-manual.md). This document maps manual data elements to refinement tables and confirms 100% alignment.

---

## 0. Data tables inventory (all MED-File v2 data files)

Per [scope.md](scope.md), there are **25 data files** plus **2 metadata** (MF2DICT, MF2VAL). Phase 2 created refinement tables for **3 data entities** (NDC, NDC Price, Dispensable Drug) and the **translation table** (MF2VAL). The rest are deferred to Phase 3+ by product tier and load order.

| Source file | Description | Refinement table (Phase 2) | Status |
|-------------|-------------|----------------------------|--------|
| **Metadata** | | | |
| MF2VAL | Validation/Translation | `medfile.mf2val` | Implemented |
| MF2DICT | Data Dictionary | — (parsed at runtime; no DB table) | By design |
| **Data – Core and Pricing (12)** | | | |
| MF2NAME | Drug Name File | — | Deferred |
| MF2TCGPI | TC-GPI Name File | — | Deferred |
| MF2NDC | NDC File | `medfile.refinement_ndc` | Implemented |
| MF2LAB | Labeler File | — | Deferred |
| MF2GPPC | GPPC File | — | Deferred |
| MF2ERR | Error Correct File | — | Deferred (Phase 4) |
| MF2GPR | GPPC Price File | — | Deferred |
| MF2PRC | NDC Price File | `medfile.refinement_ndc_price` | Implemented |
| MF2MOD | Modifier File | — | Deferred |
| MF2NDCM | NDC Modifier File | — | Deferred |
| MF2DRGNM | SDI Drug Name File | — | Deferred |
| MF2RTDRG | Routed Drug File | — | Deferred |
| **Data – Clinical / Reference (9)** | | | |
| MF2DFDRG | Drug-Dose Form File | — | Deferred |
| MF2RTDF | Routed Drug Form File | — | Deferred |
| MF2DRG | Dispensable Drug File | `medfile.refinement_drg` | Implemented |
| MF2DESC | Description File | — | Deferred |
| MF2RTE | Route File | — | Deferred |
| MF2FRM | Dose Form File | — | Deferred |
| MF2STUOM | Strength-Strength UOM File | — | Deferred |
| MF2SET | Drug Concept ID to Ingredient Set ID | — | Deferred |
| MF2INGS | Ingredient Set ID to Ingredient ID | — | Deferred |
| **Data – Ingredients and Alternate IDs (4)** | | | |
| MF2STR | Ingredient ID to Drug-Strength File | — | Deferred |
| MF2IDRG | Ingredient Drug File | — | Deferred |
| MF2SEC | Secondary Alternate ID File | — | Deferred |
| MF2RNM | Reference Name File | — | Deferred |

**Phase 2 scope:** Run metadata (`etl_run`, `etl_run_files`), translation (`mf2val`), and refinement for **MF2NDC**, **MF2PRC**, and **MF2DRG** only.  
**Phase 3 scope:** The remaining refinement tables (all deferred rows above except MF2ERR) are created and loaded during baseline construction so that all in-scope files can be loaded in dependency order. MF2ERR is handled in Phase 4 (incremental corrections).

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

**Status:** 100% — All MF2VAL data elements mapped; D077 (Reserve 77-96) not stored (not needed for translation).

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

**Status:** 100% — All Dispensable Drug File data elements mapped.

---

## 5. Run metadata (etl_run, etl_run_files)

Not from a MED-File source; defined in [architecture.md](architecture.md) §2.4. No manual mapping required.

---

## 6. Raw layer (medfile.raw_*)

**All** MED-File v2 data and metadata files are loaded into raw tables so every delivery is queryable by file and by date for history true-up and maintenance.

Each raw table has the same structure:

| Column            | Type         | Purpose |
|--------------------|--------------|--------|
| run_id             | UUID         | Which pipeline run (FK to etl_run). |
| issue_date         | DATE         | Delivery issue date (from MF2SUM). |
| source_file        | VARCHAR(30)  | Filename (e.g. MF2NDC). **Identifies file.** |
| line_number        | BIGINT       | Line number in the source file. |
| volume_number      | VARCHAR(10)  | Volume from MF2SUM. **History true-up / sequence.** |
| supplement_number  | VARCHAR(10)  | Supplement from MF2SUM. **History true-up.** |
| pos1 .. pos80      | TEXT         | Pipe-delimited positions (no type conversion). |

**Indexes:** `(run_id)`, `(issue_date, source_file)` for filtering by run or by date+file.

**Tables (26):** One table per in-scope file. Naming: `raw_` + lowercase filename (e.g. MF2NDC → raw_mf2ndc).

| Source file | Raw table    | Source file | Raw table    |
|-------------|--------------|-------------|--------------|
| MF2VAL      | raw_mf2val   | MF2DRG      | raw_mf2drg    |
| MF2NAME     | raw_mf2name  | MF2DESC     | raw_mf2desc   |
| MF2TCGPI    | raw_mf2tcgpi | MF2RTE      | raw_mf2rte    |
| MF2NDC      | raw_mf2ndc   | MF2FRM      | raw_mf2frm    |
| MF2LAB      | raw_mf2lab   | MF2STUOM    | raw_mf2stuom  |
| MF2GPPC     | raw_mf2gppc  | MF2SET      | raw_mf2set    |
| MF2ERR      | raw_mf2err   | MF2INGS     | raw_mf2ings   |
| MF2GPR      | raw_mf2gpr   | MF2STR      | raw_mf2str    |
| MF2PRC      | raw_mf2prc   | MF2IDRG     | raw_mf2idrg   |
| MF2MOD      | raw_mf2mod   | MF2SEC      | raw_mf2sec    |
| MF2NDCM     | raw_mf2ndcm  | MF2RNM      | raw_mf2rnm    |
| MF2DRGNM    | raw_mf2drgnm | MF2RTDRG    | raw_mf2rtdrg  |
| MF2DFDRG    | raw_mf2dfdrg | MF2RTDF     | raw_mf2rtdf   |

Position-to-manual mapping for refined entities: §1 (MF2VAL), §2 (MF2NDC), §3 (MF2PRC), §4 (MF2DRG). Other files: use [med-file-manual.md](med-file-manual.md) and pos1 = first pipe field, etc.

**Example: query by file and date for true-up**

```sql
SELECT run_id, issue_date, source_file, volume_number, supplement_number, COUNT(*) AS row_count
FROM medfile.raw_mf2ndc
WHERE issue_date >= '2022-01-01'
GROUP BY run_id, issue_date, source_file, volume_number, supplement_number
ORDER BY issue_date, source_file;
```

**Example: custom view from raw**

```sql
CREATE VIEW my_ndc_raw AS
SELECT run_id, issue_date, source_file, volume_number, line_number,
       pos1 AS ndc_upc_hri, pos2 AS drug_descriptor_id, pos3 AS tee_code
FROM medfile.raw_mf2ndc;
```
