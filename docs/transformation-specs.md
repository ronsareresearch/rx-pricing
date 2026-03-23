# Transformation Specs

**Role:** Current casting and translation rules used during refinement and view generation.

---

## Date Casting

MED-File dates are commonly represented as numeric `YYYYMMDD` values.

Rule:

- parse an 8-character numeric value as `YYYYMMDD`
- store it as PostgreSQL `DATE`
- treat empty or invalid values as `NULL`

Common examples:

- issue dates from `MF2SUM`
- old and new effective dates from `MF2NDC`
- price effective dates from `MF2PRC`
- link dates from `MF2DRG`

---

## Implied Decimals

Some MED-File numeric fields are delivered as integer strings with an implied decimal.

Rule:

- when MF2DICT indicates an implied decimal, or the manual picture clause uses `V`, divide by `10 ** decimal_places`
- otherwise store the parsed numeric value as-is

Important `MF2PRC` examples:

| Manual code | Picture | Target column |
|-------------|---------|---------------|
| M021 | `9(5)V9(6)` | `unit_price` |
| M032 | `9(8)V9(5)` | `unit_price_extended` |
| M045 | `9(8)V9(2)` | `package_price` |

`MF2PRC` price code values in use:

- `A` = AWP
- `D` = DP
- `H` = HCFA FFP / CMS FUL
- `U` = HCFA FFP unit dose
- `W` = WAC

---

## MF2VAL Translation Pattern

Refined code columns are translated through `medfile.mf2val`.

Core join pattern:

```sql
SELECT r.ndc_upc_hri, r.item_status_flag, v.value_description AS item_status_description
FROM medfile.refinement_ndc r
LEFT JOIN medfile.mf2val v
  ON v.field_id = 'H074'
 AND v.field_value = r.item_status_flag
 AND v.language_cd = '01';
```

Common field identifiers:

- `F037` route
- `F039` dose form
- `H022` RX or OTC indicator
- `H074` item status
- `M012` NDC price code
- `M055` AWP indicator

Default language:

- `language_cd = '01'`

---

## Rule Sources

Transformation behavior is defined in:

- `refine/rules/*.yaml` for source position, typing, and history behavior
- `refine/rules/common.yaml` for shared formatting rules such as NDC display formatting
- `view/entity_views.py` for view generation that reuses rule lookups and derived fields

When changing a field definition, keep the rule file, the manual, and the docs aligned.

---

## Reference

| Topic | Source |
|-------|--------|
| field layouts and picture clauses | [med-file-manual.md](med-file-manual.md) |
| project coverage and table inventory | [schema-validation.md](schema-validation.md) |
| implied decimal metadata | MF2DICT |
| code-to-description lookups | `medfile.mf2val` |
| NDC hyphenation behavior | `refine/rules/common.yaml` |
