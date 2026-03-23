# Glossary

**Role:** Shared project terms used across the docs and codebase.

---

## A-D

**AAWP (Average Average Wholesale Price)**  
Vendor-calculated average price value from the GPPC Price file (`MF2GPR`).

**AWP (Average Wholesale Price)**  
Reference price carried in MED-File price sources such as `MF2PRC` and `MF2GPR`.

**DDID (Dispensable Drug Identifier / Drug Descriptor Identifier)**  
Wolters Kluwer concept for a dispensable drug. In this repo it is primarily carried through `medfile.refinement_drg` and downstream reference joins.

**Data Dictionary (MF2DICT)**  
Vendor metadata file that describes MED-File elements and formats. Loaded into raw only and used as reference for mapping and validation.

**DP (Direct Price)**  
Manufacturer-to-pharmacy price carried in `MF2PRC` with `price_code = 'D'`. Exposed in `v_product_package_price_dp_monthly`.

---

## E-G

**Effective Date**  
Date attached to a vendor change or price record. Used to model historical versions in refinement.

**Error Correct File (MF2ERR)**  
Incremental-only vendor file for retroactive corrections. The repo currently loads it into raw, but refinement does not process it yet.

**Full load (`T`)**  
A total delivery identified by `MF2SUM`. Used as a baseline run.

**GPI (Generic Product Identifier)**  
Wolters Kluwer therapeutic hierarchy code. In this project, current GPI values come from `medfile.refinement_gppc.generic_product_identifier`.

**GPPC (Generic Product Packaging Code)**  
Vendor packaging code used to join NDC records to generic product attributes and pricing.

---

## I-N

**Incremental (`U`)**  
Update delivery identified by `MF2SUM`. In current code, refinement allows normal sequencing, gaps, and backfills as long as a prior refined run exists.

**Item Status Flag**  
NDC lifecycle status from `MF2NDC`, such as active or inactive.

**Materialized View**  
A PostgreSQL view whose results are stored on disk and refreshed on demand. Monthly views in this project are materialized with `REFRESH MATERIALIZED VIEW CONCURRENTLY` so reads are never blocked during refresh.

**MED-File v2**  
The Wolters Kluwer source format this repo ingests and refines.

**MF2VAL**  
Validation and translation source that maps coded values to descriptions. Refined into `medfile.mf2val`.

**NDC (National Drug Code)**  
Drug product identifier represented in MED-File as `NDC-UPC-HRI`.

**NDC-UPC-HRI**  
The project's atomic product identifier for NDC-level records.

---

## P-R

**Price Effective Date**  
Date associated with a price row, especially in `MF2PRC` and `MF2GPR`.

**Raw layer**  
Schema `rxraw`, which stores vendor-fidelity rows with shared provenance columns and `pos1` through `pos80`.

**Refinement layer**  
Schema `medfile`, which stores translated, typed, and history-aware tables produced from raw MED-File data.

**Route**  
Route of administration from MED-File reference sources such as `MF2RTE`, with descriptions translated through `MF2VAL`.

---

## S-Z

**Price Code**  
Single-character code in `MF2PRC` that identifies the price type: `A` = AWP, `D` = DP, `H` = HCFA FFP / CMS FUL, `U` = HCFA FFP unit dose, `W` = WAC.

**SCD2 (Type 2 Slowly Changing Dimension)**  
History-preserving table pattern that creates new versions instead of overwriting old values.

**Supplement Number**  
Supplement identifier from `MF2SUM` that is stored alongside volume metadata for each run.

**Transaction CD**  
Vendor transaction code used during incremental refinement logic, typically `A`, `C`, `D`, or blank.

**Volume Number**  
Vendor run sequence from `MF2SUM`. Stored in both raw and refine run tracking tables.

**Views**  
Reference outputs created by the separate `view` process from `medfile` refinement tables only. The view runner maintains a managed-view registry and drops orphaned views on each run.

**WAC (Wholesale Acquisition Cost)**  
Manufacturer-to-wholesaler price carried in `MF2PRC` with `price_code = 'W'`. Exposed in `v_product_package_price_wac_monthly`.
