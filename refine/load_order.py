"""
Refinement load order: dependency order for MED-File v2 entities.
Ensures referential integrity: parents before children (e.g. Labeler before NDC, Drug Name before Routed Drug).
Phase 4 (MF2ERR) runs last — flags corrections in other entities.
"""

# Order: translation first; then reference/dimension tables; then core (NDC, prices);
# then clinical hierarchy; then ingredients/alternate IDs; finally error corrections.
REFINEMENT_LOAD_ORDER: list[str] = [
    # Phase 1 – translation / reference
    "mf2val",       # Validation/Translation – no deps
    "lab",          # Labeler – NDC references labeler_id
    "rte",          # Route – concept reference
    "frm",          # Dose Form – concept reference
    "stuom",        # Strength-Strength UOM – concept reference
    "desc",         # Description – descriptions for all concept types
    # Phase 2 – core entities
    "name",         # Drug Name – primary drug concepts
    "tcgpi",        # TC-GPI Name – therapeutic hierarchy
    "gppc",         # GPPC – NDC references gppc_code
    "ndc",          # NDC File
    "ndc_price",    # NDC Price File
    "gpr",          # GPPC Price File
    "mod",          # Modifier File
    "ndcm",         # NDC Modifier File – links NDC to Modifier
    # Phase 3 – clinical hierarchy / ingredients
    "drgnm",        # SDI Drug Name
    "rtdrg",        # Routed Drug
    "dfdrg",        # Drug-Dose Form File
    "rtdf",         # Routed Drug Form File
    "drg",          # Dispensable Drug File
    "set",          # Drug Concept ID to Ingredient Set ID
    "ings",         # Ingredient Set ID to Ingredient ID
    "str",          # Ingredient ID to Drug-Strength File
    "idrg",         # Ingredient Drug File
    "sec",          # Secondary Alternate ID File
    "rnm",          # Reference Name File
    # Phase 4 – error corrections (audit trail, no deps on other entities)
    "err",          # Error Correct File – flags data entry revisions
]


def get_load_order() -> list[str]:
    """Return entity names in refinement load order."""
    return list(REFINEMENT_LOAD_ORDER)
