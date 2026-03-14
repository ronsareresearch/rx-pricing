# Glossary: rx-pricing / MED-File v2

**Role:** Canonical definitions for terms used across architecture, scope, operations, and ETL logic. Keeps documentation and code aligned.

---

## A–D

**AAWP (Average Average Wholesale Price)**  
Calculated average of AWP for products meeting vendor criteria (e.g. same GPI/packaging). Supplied in GPPC Price File (MF2GPR).

**AWP (Average Wholesale Price)**  
List price used as a benchmark for drug pricing. Stored in NDC Price File (MF2PRC) and GPPC Price File (MF2GPR).

**DDID (Dispensable Drug Identifier / Drug Descriptor Identifier)**  
Wolters Kluwer proprietary concept identifying a dispensable drug (distinct combination of drug, route, dose form, strength, etc.). Central to clinical hierarchy. Tracked in Dispensable Drug File (MF2DRG). When a DDID is replaced, the old record has Link Value (new Concept ID) and Link Date; ETL must maintain this lineage.

**Data Dictionary (MF2DICT)**  
MED-File file containing field definitions (identifier, type, length, validation flag). Used for schema generation and validation.

**Effective Date**  
Date associated with a change or price; used for history and SCD2. In NDC File: New/Old Effective Date for NDC changes. In price files: Price Effective Date (MF2PRC) or Effective Date (MF2GPR).

---

## E–G

**Error Correct File (MF2ERR)**  
Incremental-only file signaling retroactive data entry revisions (e.g. corrected or retracted manufacturer data). Key Identifier, Unique Key, and Data Element Code identify the corrected field. ETL must apply corrections so refinement history reflects manufacturer revisions.

**Full load (Total, T)**  
Initial or full refresh: Product File Type = "T" in MF2SUM. All data files have blank Transaction CD. Pipeline inserts all records as baseline and records Volume Number for future sequence checks.

**GEAP (Generic Equivalent Average Price)**  
Vendor-calculated price for generic equivalents; in GPPC Price File (MF2GPR).

**GPI (Generic Product Identifier)**  
Wolters Kluwer hierarchical therapeutic classification (Drug Group, Drug Class, Drug Subclass, etc.). Used in TC-GPI Name File (MF2TCGPI) and elsewhere.

**GPPC (Generic Product Packaging Code)**  
Proprietary code defining a drug and its packaging. In GPPC File (MF2GPPC); prices in GPPC Price File (MF2GPR).

---

## I–N

**Incremental (Update, U)**  
Monthly (or periodic) update: Product File Type = "U" in MF2SUM. Volume Number must increment from last processed. Transaction CD present: A (Add), C (Change), D (Delete), or blank (No Change).

**Item Status Flag (NDC File)**  
Lifecycle of an NDC in MF2NDC: **A** = Active, **I** = Inactive, **O** = Override (reused NDC; treat as new), **Z** = Inactive >48 months (output once with D; retain in history forever).

**MF2**  
Prefix for MED-File v2 filenames (e.g. MF2SUM, MF2NDC). “MED-File v2.”

**NDC (National Drug Code)**  
Standard identifier for drug products in the US. In MED-File, used with UPC and HRI as **NDC-UPC-HRI** (single concept). NDC File (MF2NDC) tracks changes: Old/New NDC-UPC-HRI and effective dates for chaining.

**NDC-UPC-HRI**  
Combined NDC / UPC / Health Related Item concept in MED-File; the atomic product identifier in the NDC File.

---

## P–R

**Price Effective Date**  
Date the manufacturer associates with price data. In MF2PRC (NDC Price) and MF2GPR (GPPC Price); used for price history (new row per effective date, no overwrite).

**Raw layer**  
Immutable landing zone for vendor files. One directory/partition per delivery (e.g. by volume or YYYYMM). No transformation; checksum and validation (e.g. MF2SUM) only.

**Refinement layer**  
Normalized, historical store: SCD2 dimensions, effective-date price history, identifier lineage, soft deletes. Built from raw using Transaction CD and vendor rules; never overwrites or drops history.

**Route**  
Route of administration (e.g. Oral, Topical). Route File (MF2RTE); descriptions in Description File (MF2DESC). MF2VAL translates route codes (e.g. "PO" → "Oral").

---

## S–Z

**SCD2 (Type 2 Slowly Changing Dimension)**  
Dimension history preserved by adding new rows for changes (with effective/end dates or version), not by overwriting. Used for drug concepts, NDC lifecycle, and related entities.

**Supplement Number**  
Vendor field used with Volume Number for sequencing when supplemental updates exist. Pipeline must enforce correct order (see Operations).

**Transaction CD (Transaction Code)**  
In incremental data files: **A** = Add, **C** = Change, **D** = Delete, blank = No Change. Drives insert vs. append history vs. end-date/flag in refinement.

**Validation/Translation File (MF2VAL)**  
MED-File file mapping encoded values to descriptions (e.g. Route "PO" → "Oral"). Used in refinement for lookups and data quality.

**Volume Number**  
Sequence identifier in MF2SUM. For incrementals, must be last processed Volume + 1 (or follow vendor Supplement rules). Loading out of order corrupts history.

**Views (consumption layer)**  
Derived layer built only from refinement: current-state views, analytics, reporting, API-ready marts. No direct query to raw for production reporting.
