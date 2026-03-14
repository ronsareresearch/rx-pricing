# Transformation specs: casting and translation

**Role:** Rules for data casting (dates, implied decimals) and MF2VAL join pattern. Used by refinement load logic (Phase 3+). See [med-file-manual.md](med-file-manual.md) and MF2DICT (C044, C045) for field-level definitions.

---

## 1. Date casting (YYYYMMDD → DATE)

- **Source:** Numeric fields `N/8` representing YYYYMMDD (Gregorian). Examples: Issue Date (MF2SUM), Effective Date (MF2PRC, MF2NDC), Old/New Effective Date (MF2NDC), Link Date (MF2DRG).
- **Rule:** Parse the 8-digit integer string as `YYYYMMDD`; convert to native `DATE` in Python and store in Postgres `DATE` columns. Invalid or empty → store NULL.
- **Example:** `"20220706"` → `date(2022, 7, 6)` → Postgres `DATE '2022-07-06'`.

---

## 2. Implied decimals (C044, C045 and manual Picture clauses)

- **Source:** MF2DICT: **Implied Decimal Flag** (C044) = 'Y' and **Decimal Places** (C045) = N; or manual Picture (e.g. 9(5)V9(6) = 5 integer + 6 decimal places). Raw value is an integer string; true value = raw / 10^N.
- **Rule:** If C044 = 'Y' or Picture contains V, divide the parsed integer by `10 ** decimal_places` before writing to a `DECIMAL` column. If C044 = 'N', use the value as-is.
- **MF2PRC (NDC Price File)** — manual § NDC Price File uses **M**-codes (not L). Implied decimal from Picture:
  - **M021 Unit Price:** 9(5)V9(6) → divide by 10^6 → `unit_price DECIMAL(11,6)`.
  - **M032 Unit Price - Extended:** 9(8)V9(5) → divide by 10^5 → `unit_price_extended DECIMAL(13,5)`.
  - **M045 Package Price:** 9(8)V9(2) → divide by 10^2 → `package_price DECIMAL(10,2)`.

---

## 3. MF2VAL join pattern (translation layer)

- **Table:** `medfile.mf2val` columns: `field_id`, `field_value`, `language_cd`, `value_description`, `value_abbreviation`.
- **Join pattern:** For any refinement column that holds a **code** defined in MF2VAL (e.g. Route F037, Item Status H074, RX-OTC H022), join to get the human-readable description:

  ```sql
  SELECT r.ndc_upc_hri, r.item_status_flag, v.value_description AS item_status_description
  FROM medfile.refinement_ndc r
  LEFT JOIN medfile.mf2val v
    ON v.field_id = 'H074' AND v.field_value = r.item_status_flag AND v.language_cd = '01'
  ```

- **Common field_id examples:** F037 (Route), F039 (Dose Form), H022 (RX-OTC), H074 (Item Status), L009 (GPPC Price Code). Use MF2VAL or the manual to map refinement columns to `field_id`.
- **Language:** Default `language_cd = '01'` (English). Use the same in joins unless multi-language is required.

---

## 4. Reference

| Topic | Document / source |
|-------|-------------------|
| Field layouts, picture clauses | [med-file-manual.md](med-file-manual.md) |
| Schema vs manual (100% mapping) | [schema-validation.md](schema-validation.md) |
| Implied decimal, length, type | MF2DICT (C044, C045, C041, C040) |
| Code → description | MF2VAL; join on field_id + field_value + language_cd |
