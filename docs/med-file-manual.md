# Table of Contents

Chapter 1: Introduction ... 1-1  
In This Chapter ... 1-1  
Permitted/Intended Use(s) ... 1-1  
Overview of the Database ... 1-1  
Features of the Database ... 1-2

Chapter 2: Editorial Policies ... 2-1  
In This Chapter ... 2-1  
Introduction ... 2-1  
Overview ... 2-1  
Proprietary Drug Concepts ... 2-3  
External Drug Concepts ... 2-22  
Ingredients ... 2-24  
Pricing ... 2-27  
Drug Attributes ... 2-36

Chapter 3: Database Structure ... 3-1  
In This Chapter ... 3-1  
Understanding the Database Structure ... 3-1  
Filenames ... 3-2  
Database Layout ... 3-5  
Reserve Fields ... 3-7  
File Relationships ... 3-8

Chapter 4: Data Elements ... 4-1  
In This Chapter ... 4-1  
Copyright File ... 4-2  
ReadMe File ... 4-2  
Data Dictionary File ... 4-2  
Validation/Translation File ... 4-6  
Summary File ... 4-10  
Drug Name File ... 4-11  
TC-GPI Name File ... 4-29  
NDC File ... 4-32  
Labeler File ... 4-52  
GPPC File ... 4-56  
Error Correct File ... 4-64  
GPPC Price File ... 4-67

NDC Price File... 4-69  
Modifier File... 4-74  
NDC Modifier File... 4-77  
SDI Drug Name File... 4-81  
Routed Drug File... 4-84  
Drug-Dose Form File... 4-87  
Routed Drug Form File... 4-91  
Dispensable Drug File... 4-94  
Description File... 4-100  
Route File... 4-104  
Dose Form File... 4-107  
Strength-Strength Unit of Measure File... 4-110  
Drug Concept ID to Ingredient Set ID File... 4-113  
Ingredient Set ID to Ingredient ID File... 4-116  
Ingredient ID to Drug-Strength File... 4-118  
Ingredient Drug File... 4-121  
Secondary Alternate ID File... 4-123  
Reference Name File... 4-127

# Chapter 5: Applications... 5-1

In This Chapter... 5-1  
Introduction... 5-1  
Storing Terminology... 5-2  
Maintaining Terminology... 5-3  
Processing the Error Correct File... 5-4  
Maintaining Price History... 5-5  
Displaying Drugs and Creating Drug Selection Lists... 5-7  
Retrieving Routed Drug(s) for a Drug Name... 5-10  
Retrieving Routed Dose Form Drug(s) for a Drug Name... 5-11  
Retrieving Dose Form Drug(s) for a Drug Name... 5-13  
Retrieving Dispensable Drug(s) for a Drug Name... 5-14  
Retrieving Routed Dose Form Drug(s) for a Routed Drug... 5-17  
Retrieving Dispensable Drug(s) for a Routed Drug... 5-17  
Retrieving Dispensable Drug(s) for a Routed Dose Form Drug... 5-18  
Retrieving Dispensable Drug(s) for a Dose Form Drug... 5-20  
Associating Brand and Generic Drug Names... 5-23  
Associating Brand and Generic Routed Drugs... 5-26  
Associating Brand and Generic Dispensable Drugs... 5-30  
Constructing Alternative Drug Names... 5-35  
Associating Dosage Form in the Drug Name File to Dose Form in the Description File... 5-41  
Associating Route of Administration in the Drug Name File to Route in the Description File.. 5-44  
Identifying Ingredients for a Dispensable Drug... 5-46  
Identifying Ingredients for an NDC-UPC-HRI... 5-47  
Associating New and Old NDC-UPC-HRIs... 5-49  
Associating New and Old Dispensable Drugs (DDIDs)... 5-51

Retrieving KDCs for a Dispensable Drug ... 5-52  
Retrieving GPIs for a Dispensable Drug ... 5-53  
Identifying Therapeutic Alternatives Using the TC-GPI Name File ... 5-53  
Creating Nine-Character GPPCs ... 5-55

---

---

&nbsp;

# Chapter 1: Introduction

## In This Chapter

- Permitted/Intended Use(s)
- Overview of the Database
- Features of the Database

## Permitted/Intended Use(s)

Medi-Span Electronic Drug File (MED-File) v2 is intended to support customers by providing a codified drug dictionary, drug vocabulary, and drug pricing for prescription drugs and medication-based over-the-counter products in the United States.

MED-File v2 is not intended to support medical supplies, durable medical equipment, non-human drugs (such as veterinary or other products), or health and beauty items.

## Overview of the Database

MED-File v2 provides customers with drug data and terminology that supports the ever-changing world of drug information in healthcare.

MED-File v2 contains Wolters Kluwer Clinical Drug Information proprietary drug name concepts, external drug concepts, ingredient information, drug pricing, and numerous attributes about a drug designed to meet the needs of healthcare across a variety of settings.

In addition, MED-File v2 offers programming flexibility to end-users requiring drug product information. Drug product data elements can be accessed and combined to facilitate the following:

- medication order entry
- formulary development and maintenance
- dispensing activities
- prescription claims processing
- other health care applications requiring drug data

&nbsp;

Introduction

# Features of the Database

The following are features of MED-File v2 :

- includes prescription and over-the-counter drug products in the US using industry standard identifiers, including National Drug Code (NDC), Universal Product Code (UPC), and Health Related Item (HRI)
- provides Wolters Kluwer Clinical Drug Information’s proprietary drug name-based concepts at varying levels of specificity, supporting the needs of healthcare professionals throughout their workflow
- includes Wolters Kluwer Clinical Drug Information's proprietary, hierarchical Therapeutic Classification System (TCS) that allows for identification of drug products at any of several levels including Drug Group, Drug Class, and Drug Subclass
- associates Wolters Kluwer Clinical Drug Information’s proprietary concepts to NDCs, UPCs, and HRIs
- links old concepts to new concepts, enabling patient medication profiles and other applications to accurately depict the defined drug
- associates generic names to brand names
- includes a variety of drug product attributes that aid in drug product substitution (such as Therapeutic Equivalence Evaluation [TEE] Code, Multi-Source Code, and Brand Name Code)
- provides Wolters Kluwer Clinical Drug Information's proprietary Generic Product Packaging Code (GPPC) which generically defines a drug and its packaging
- includes upper and lower case drug names as well as alternative representations for the drug’s dosage form and strength
- defines the drug’s ingredients and their strengths, and indicates whether each ingredient is active or inactive
- includes current drug pricing for Average Wholesale Price (AWP), Direct Price (DP), Wholesale Acquisition Price (WAC), Centers for Medicare and Medicaid Services’ Federal Upper Limit (CMS FUL)
- provides Average Average Wholesale Price (AAWP) and Generic Equivalent Average Price (GEAP) calculated by a proprietary Wolters Kluwer Clinical Drug Information algorithm
- defines manufacturers, labelers, and distributors for drug products
- includes inactive drug products for up to 48 months

1-2 MED-File v2

Published: 11/11

Revised: 02/16

# Chapter 2: Editorial Policies

## In This Chapter

- Introduction
- Overview
- Proprietary Drug Concepts
- External Drug Concepts
- Ingredients
- Pricing
- Drug Attributes

## Introduction

This chapter outlines the editorial policies that guide the development of MED-File v2 by Wolters Kluwer. Information regarding Wolters Kluwer’s proprietary and external concepts as well as data within MED-File v2 is also provided.

**Note** Not all data elements for MED-File v2 have editorial policies. Those that do are described in this chapter.

## Overview

MED-File v2 covers a broad spectrum of pharmaceutical drug products, chemicals, over-the-counter (OTC) products, medical devices, supplies, and related items. Below is a summary of the types of products included in MED-File v2:

- Prescription Drug Products
- Medicated OTC Products
- Devices

### Prescription Drug Products

- Amebicides
- Analgesics
- Anesthetics Agents
- Antimalarials
- Antineoplastics
- Antitubercular(s)
- Gastrointestinal Agents
- Genitourinary Products
- Immunosuppressive

&nbsp;

Editorial Policies

Anthelmintics Antivirals Neuromuscular Drugs  
Antiasthmatics Biologicals Parenteral Solutions  
Antibiotics Cardiovascular Agents Pediculicides  
Anticoagulants Solutions CNS Drugs Peritoneal Dialysis  
Antifungals Cough/Cold/Allergy Agents Prostaglandins  
Antihistamines Decongestants Respiratory Agents  
Antihyperlipidemic Diagnostic Agents Scabicides  
Antihypertensives Diuretics Sclerosing Agents  
Endocrine & Metabolic Drugs Topical Products

## Medicated OTC Products


| Allergy Products           | Contact Lens Solutions    | First Aid Supplies        |
| -------------------------- | ------------------------- | ------------------------- |
| Acne Products              | Cough/Cold Preparations   | Hemorrhoidal Preparations |
| Analgesics                 | Denture Products          | Laxatives                 |
| Antacids                   | Diabetic Supplies         | Minerals                  |
| Anti-Diarrheals            | Diet Products             | Nutrients                 |
| Anti-Emetics               | Dietary Products          | Nutritional               |
| Anti-Fungals Products      | Ear Products              | Oral Hygiene              |
| Asthma Products            | Electrolytes              | Shampoos                  |
| Athletes Foot Preparations | Eye Products              | Sleep Aids                |
| Baby Products              | Family Planning Products  | Toothpaste                |
| Bath Products              | Feminine Hygiene Products | Tube Feedings Vitamins    |


## Devices


| Bandages                   | Female Personal Care Products | Needles              |
| -------------------------- | ----------------------------- | -------------------- |
| Blood Administration Kits  | Heating Pads                  | Optical Supplies     |
| Condoms                    | Incontinence Supplies         | Ostomy Supplies      |
| Diabetic Supplies          | Infusion Pumps                | Respiratory Supplies |
| Diaphragms                 | IUDs                          | Syringes             |
| Elastic Braces             | IV Tubing                     | Thermometers         |
| Enteral Nutrition Supplies | IV Sets                       | Vaporizers           |


A drug product must have an NDC, UPC, or HRI with packaging and ingredient information from the manufacturer/distributor to be added to MED-File v2.

MED-File v2 includes all active items in Wolters Kluwer's internal database as well as information for recently discontinued drug products (up to 48 months from the date the item became inactive).

2-2 MED-File v2  
Published: 11/11  
Revised: 08/21

Proprietary Drug Concepts

# Source of Information

The information Wolters Kluwer uses within MED-File v2 is obtained and/or derived from information provided to Wolters Kluwer by drug manufacturers.

The information contained in MED-File v2 consists of drug product names, current pricing, ingredients, and associated drug product descriptors. Selected fields are discussed in detail on the following pages. Information on other fields is available upon request.

# Proprietary Drug Concepts

MED-File v2 contains various drug concepts that are proprietary to Wolters Kluwer. These concepts are listed below:

- Drug Name
- Dose Form Drug
- Drug Descriptor Identifier (DDID)  
> This concept is also referred to as Dispensable Drug
- Generic Product Identifier (GPI)
- Generic Product Packaging Code (GPPC)
- Routed Dose Form Drug
- Routed Drug

The name-based drug concepts (Drug Name, Dose Form Drug, Routed Drug, Routed Dose Form Drug, and Drug Descriptor Identifier) are based on unique drug trade (brand) names and generic names. These concepts differ in their level of specificity. The functions being performed determine the level of name-based concept that is required.

For more information about using these name-based drug concepts, go to Chapter 5: Applications.

# Drug Name

A Drug Name displays the product name shown by the manufacturer on the package. See below for more information regarding the Drug Name:

- The Drug Name has a maximum of 30 characters and is presented in mixed case.
- For each drug product in the Wolters Kluwer database, there is a generic name and a brand name. Even if a drug is not yet marketed in generic form, a generically-based Drug Name is provided. This generic-based name is derived from the Drug Name and Drug Name Extension (first 10

Documentation Manual 2-3

Published: 11/11

Revised: 08/21

Editorial Policies

characters of the Generic Product Identifier), but has a limit of 30 characters.

- When the product name exceeds 30 characters, Wolters Kluwer’s editorial policy guides how the name is modified to fit in the allotted space. For example, if the dosage form is part of the name, it may be removed. This is especially common with multiple ingredient cough and cold combinations.
- The Drug Name does not include flavors, colors, shapes, repacks, packaging, or other attributes that a manufacturer may include.  
> Exception: Oral contraceptives, such as Ortho-Novum 7/7/7 (28)
- Abbreviations are used only when necessary for space and are restricted to common abbreviations.
- The Drug Name does not include dosage form information unless excluding that information results in a nonsensical name (for example, Baby Oil).
- The Drug Name does not include strength(s) unless the strength is part of the product name (for example, Acetaminophen-Codeine #2), or when necessary to represent therapy packs (for example, Lenvatinib (18 MG Daily Dose)).
- The Drug Name does not include symbols (for example, slashes, dashes, w/, or &) for Brand or Branded Generic names unless represented in the product name by the manufacturer.
- The generic product name includes a hyphen to separate multiple active ingredients, when present.

# Tall Man Letters

Wolters Kluwer includes Tall Man letters to distinguish similar drug names and reduce the potential for medication errors. Tall Man drug letters identified by the following sources are included:

- United States Food and Drug Administration (FDA)
- Institute for Safe Medication Practices (ISMP)

FDA and ISMP are the only sources for Tall Man letters. If the manufacturer has labeled its product with upper and lower case letters that are not recognized as Tall Man by ISMP, they will be included in the Drug Name only if the product name is a Trademarked or Branded Generic product. Generically-named products will follow normal naming policies with the first letter of the generic name in upper case and the remainder of the name in lower case. Only Tall Man letters defined by the FDA or ISMP will be retained when Wolters Kluwer creates all upper case brand names, all lower case generic names, and salt names that are provided in the Description File.

2-4 MED-File v2

Published: 11/11

Revised: 08/21

Proprietary Drug Concepts

Note  
Tall Man letters provided by Wolters Kluwer should be maintained in your application and presented in all instances, whether in a visual display or a hard copy report. An example of drug names with Tall Man letters are vinCRIStine Sulfate and vinBLAStine Sulfate.

Examples:

The table below provides examples with a “Drug Name” Concept Type:


| Drug Name             |
| --------------------- |
| Artificial Tears      |
| vincristine Sulfate   |
| Diltiazem HCl CR      |
| Vytorin               |
| HalfLytely Bowel Prep |


Dose Form Drug

A Dose Form Drug represents the Drug Name and a Dosage Form. The unique combination of Drug Name and Dosage Form is assigned a 10-digit Concept ID.

The same Drug Name may be associated with one or many Dose Form Drugs. The same Dosage Form may be associated with one or many Dose Form Drugs.

Note  
The Dosage Form value should be translated to its Full Textual Description as defined in the Description File. Use of the Abbreviated Textual Description is discouraged. Significant patient safety issues are related to the use of non-standard abbreviations such as those found in the Dose Form ID and its corresponding Abbreviated Textual Descriptions.

Examples:

The table below provides examples with a “Dose Form Drug” Concept Type:


| Dose Form Drug                                    |
| ------------------------------------------------- |
| Artificial Tears Ointment                         |
| vinCRIStine Sulfate Solution                      |
| Diltiazem HCl CR Capsule Extended Release 12 Hour |
| Vytorin Tablet                                    |
| HalfLytely Bowel Prep Kit                         |


Documentation Manual 2-5

Published: 11/11

Revised: 08/21

Editorial Policies

# Routed Drug

A Routed Drug represents the Drug Name and a Route. The unique combination of Drug Name and Route are assigned a 10-digit Concept ID.

The same Drug Name may be associated with one or many Routed Drugs.


| Note | The Route value should be translated to its Full Textual Description as defined in the Description File. Use of the Abbreviated Textual Description is discouraged. Significant patient safety issues are related to the use of non-standard abbreviations such as those found in the Route ID and its corresponding Abbreviated Textual Description. |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


Examples:

The table below provides examples with a “Routed Drug” Concept Type:


| Routed Drug                     |
| ------------------------------- |
| Artificial Tears Ophthalmic     |
| vinCRIStine Sulfate Intravenous |
| Diltiazem HCl CR Oral           |
| Vytorin Oral                    |
| HalfLytely Bowel Prep Oral      |


# Routed Dose Form Drug

A Routed Dose Form Drug represents the Drug Name, Route, and Dosage Form. The unique combination of Drug Name, Route, and Dosage From are assigned a 10-digit Concept ID.

The same Routed Drug may be associated with one or many Routed Dose Form Drugs. The same Route may be associated with one or many Routed Dose Form Drugs. The same Dose Form may be associated with one or many Routed Dose Form Drugs.


| Note | The Route and Dosage Form values should be translated to their Full Textual Description as defined in the Description File. Use of the Abbreviated Textual Description is discouraged. Significant patient safety issues are related to the use of non-standard abbreviations such as those found in the Route ID and Dose Form ID and their corresponding Abbreviated Textual Descriptions. |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


Examples:

2-6 MED-File v2

Published: 11/11

Revised: 08/21

Proprietary Drug Concepts

The table below provides examples with a “Routed Dose Form Drug” Concept Type:


| Routed Dose Form Drug                                  |
| ------------------------------------------------------ |
| Artificial Tears Ophthalmic Ointment                   |
| vinCRISTine Sulfate Intravenous Solution               |
| Diltiazem HCl CR Oral Capsule Extended Release 12 Hour |
| Vytorin Oral Tablet                                    |
| HalfLytely Bowel Prep Oral Kit                         |


# Drug Descriptor Identifier

The Drug Descriptor Identifier (DDID) identifies a unique combination of Drug Name, Route of Administration, Dosage Form, Strength, and Strength Unit of Measure. The DDID is used to identify a unique drug product with respect to these fields alone and does not distinguish between marketed drug products based on the size of their respective packages, prescription or over-the-counter status, bioequivalence codes, or other factors.

## DDID Unique Combinations


| The Same...                                           | May be Associated with... |
| ----------------------------------------------------- | ------------------------- |
| Routed Drug, Dose Form Drug, or Routed Dose Form Drug | one or many DDIDs         |
| Route                                                 | one or many DDIDs         |
| Dose Form                                             | one or many DDIDs         |


**Note**

In the Drug Name File, the DDID is defined as a six-digit number. In the Dispensable Drug File, the DDID is defined as a 10-digit number. They represent the same drug concept. For example, the DDID of “000232” in the Drug Name file and the Concept ID of “0000000232” in the Dispensable Drug File both identify “Accupril Oral Tablet 10 MG”.

The New Drug Descriptor Identifier field in the Drug Name file allows tracking of changes to the Drug Descriptor Identifier by linking the old and new DDIDs.

## Sources of DDID changes include

- Product/Manufacturer
- United States Pharmacopeia (USP) and FDA
- Customer feedback
- Clerical data change revisions

Documentation Manual 2-7

Published: 11/11

Revised: 08/21

Editorial Policies

DDID changes can occur in any one of the five fields. Depending on the type of change that occurs, the existing DDID may be updated or a new DDID may be created.

For more information on the DDID, see below:

- When the Drug Name is changed and a new Drug Name is created, the following applies:  
> If the change results in a one-to-one replacement, and the DDIDs remain the same clinically, the old and new DDIDs are linked.  
> If one DDID is split into multiple new DDIDs, the old and new DDIDs are not linked.
- When the Drug Name is changed and the existing DDID is changed, the following applies:  
> The DDID remains the same clinically.  
> Changes occur for spelling revisions, spacing, abbreviations, or special characters such as hyphens, additional information added to the Drug Name, or casing of letters in the drug name, including those from the manufacturer and from ISMP Tall Man letters.
- When the Route is changed, a new DDID is assigned.  
> If the change results in a one-to-one replacement, and the DDIDs remain the same clinically, the old and new DDIDs are linked.  
> If a one-to-many replacement is made, the old and new DDIDs are not linked.
- When the Dosage Form is changed, a new DDID is assigned.  
> If the change results in a one-to-one replacement, and the DDIDs remain the same clinically, the old and new DDIDs are linked.  
> If a one-to-many replacement is made, the old and new DDIDs are not linked.
- When the Strength and/or Strength Unit of Measure are changed, a new DDID is assigned, the following applies:  
> If a completely new Strength and/or Strength Unit of Measure results, there is a one-to-one replacement, and the DDIDs are clinically the same, the old and new DDIDs are linked.  
> If a one-to-many replacement is made, the old and new DDIDs are not linked.  
> If the DDIDs are not clinically the same, the old and new DDIDs are not linked.
- When the Strength and/or Strength Unit of Measure are changed resulting in changes to the existing DDID, the following applies:  
> Changes occur to correct the order of strengths in multiple ingredient products, spacing, abbreviations, special characters, or to add additional information.

2-8 MED-File v2  
Published: 11/11  
Revised: 08/21

Proprietary Drug Concepts

# Examples:

The table below provides examples of the DDID as presented in the Drug Name File and in the Description file for those data with a "Dispensable Drug" Concept Type.


| Drug Name             | Route       | Dosage Form                      | Strength | Strength Unit of Measure |
| --------------------- | ----------- | -------------------------------- | -------- | ------------------------ |
| Artificial Tears      | Ophthalmic  | Ointment                         | &nbsp;   | &nbsp;                   |
| vinCRIStine Sulfate   | Intravenous | Solution                         | 1        | MG/ML                    |
| Diltiazem HCl CR      | Oral        | Capsule Extended Release 12 Hour | 120      | MG                       |
| Vytorin               | Oral        | Tablet                           | 10-10    | MG                       |
| HalfLytely Bowel Prep | Oral        | Kit                              | 5-210    | MG-GM                    |


# Alternatives for Drug Name and for Strength and Strength Unit of Measure

MED-File v2 includes the below descriptions in the Description File in addition to the full text description for Drug Name, Dose Form, Route, and for Strength and Strength Unit of Measure:

- Abbreviated textual description
- Capitalized Name
- Salt Name
- Alternate Name

These names provide options in your application to meet the needs of your end-users.

Below are listed a few examples you may wish to include:

- All UPPER CASE brand name, in place of a mixed case name
- All lower case generic name, in place of a mixed case name
- Strength and its associated Strength Unit of Measure grouped together for a multiple ingredient product

**Note**

When a Drug Name includes Tall Man letters per FDA and/or ISMP, these letters are maintained. In this case, an all UPPER CASE brand name or an all lower case generic name is not provided; however, Tall Man letters defined only by the manufacturer will not be retained when Wolters Kluwer creates all upper case brand names, all lower case generic names, and salt names that are provided in the Description File.

Documentation Manual 2-9

Published: 11/11

Revised: 08/21

Editorial Policies

Abbreviated textual descriptions enable you to associate the Routes and Dosage Forms in the Validation/Translation File to those in the Description File, and the files that use the Description File.

Note  
Abbreviated Routes and Dose Forms are provided for use by developers. The abbreviated format is not intended for display or print in end-user applications.

Salt names represent the base ingredient, and are provided in lower case. They exclude the salt unless it is integral to differentiating one ingredient from another. For example, hydrocortisone acetate vs. hydrocortisone valerate.

Alternate names are provided for Dose Forms and for Strength/Strength Unit of Measure representations.

The table below illustrates Drug Name, Strength/Strength Unit of Measure, and Dose Form descriptions that are available in MED-File v2.

Examples:


| Concept Type                        | Description Type                | Description             |
| ----------------------------------- | ------------------------------- | ----------------------- |
| Drug Name                           | Full textual description        | FlUoxetine HCl          |
| &nbsp;                              | Salt name                       | FlUoxetine              |
| Drug Name                           | Full textual description        | Atorvastatin Calcium    |
| &nbsp;                              | Salt name                       | atorvastatin            |
| Drug Name                           | Full textual description        | Calcium Carbonate       |
| &nbsp;                              | Salt name                       | calcium carbonate       |
| Drug Name                           | Full textual description        | Crestor                 |
| &nbsp;                              | Capitalized name                | CRESTOR                 |
| Strength & Strength Unit of Measure | Full textual description        | 1000-4-60 MG            |
| &nbsp;                              | Alternate name                  | 1,000 mg - 4 mg - 60 mg |
| Dose Form                           | Full textual description        | Tablet Chewable         |
| &nbsp;                              | Abbreviated textual description | CHEW                    |
| &nbsp;                              | Alternate name                  | Chewable Tablet         |


Generic Product Identifier

Wolters Kluwer's Generic Product Identifier (GPI) defines pharmaceutically equivalent drug products that are identical in terms of:

- active ingredient(s)
- route of administration
- dosage form

2-10 MED-File v2

Published: 11/11

Revised: 08/21

Proprietary Drug Concepts

- strength or concentration
- therapeutic use

Clinical considerations may also enter into the GPI assignment. The GPI does not consider the following:

- manufacturing process
- patent or intellectual property rights
- differences in bioequivalence or therapeutic equivalence
- inactive ingredients
- legal restrictions for substitution

The GPI categorizes drug products by a hierarchical therapeutic classification scheme for use in the following:

- formulary management
- market research
- various reporting applications

The unique and proprietary therapeutic basis of this system is more useful than conventional pharmacological approaches to drug classification. This coding system is based on subsets contained in the GPI structure. Drug product records containing a GPI may be readily manipulated to categorize drug products at various levels of specificity.

A common application and use of Wolters Kluwer’s data is the identification of generic and therapeutic equivalents. Different markets and applications have different definitions of a generic drug product. The GPI is considered a starting point for selecting generic drug products and must be used in conjunction with other data elements for drug product identification. An example is the FDA’s Orange Book Therapeutic Equivalence Evaluation Code (refer to the section entitled “Generic Substitution Versus Therapeutic Alternate Identification”).

Note  
Drug products identified as “pharmaceutical equivalents” are not necessarily bioequivalent or therapeutically equivalent. Differences in bioequivalence and legal restrictions concerning drug product substitution may result from brand interchange or drug product substitution.

Dosage forms considered within the GPI hierarchy are based on Wolters Kluwer’s proprietary dosage form concept.

In assigning the GPI, Wolters Kluwer considers the therapeutic use of the drug. In some instances, drugs may be classified in a common therapeutic area for ease of identification and selection (see also Multiple Indications).

Documentation Manual 2-11  
Published: 11/11  
Revised: 08/21

Editorial Policies

# Wolters Kluwer's Therapeutic Classification System (TCS)

The first 10 characters of the GPI identify the drug product according to Wolters Kluwer's Therapeutic Classification System (TCS). For more information regarding Wolters Kluwer's TCS, see Appendix E, "Wolters Kluwer's Therapeutic Classification System".

# GPI Structure

The 14-character GPI consists of seven subsets, each providing increasingly more specific information about drug products. Asterisks included in the drug product name refer to the position of the product within Wolters Kluwer's TCS. The asterisk before the name indicates the location is within the first three Record Types; the asterisk(s) after the name indicates the level of specificity. Record Types 1 through 3 will always contain asterisks; Record Type 5 will only contain asterisks for partial GPIs. (Refer to Partial GPI Codes later in this chapter for more information.) These subsets are structured and identified below:


| Subset               | Record Type | Number of Characters | Description                              | Example                                 |
| -------------------- | ----------- | -------------------- | ---------------------------------------- | --------------------------------------- |
| 12-xx-xx-xx-xx-xx-   | 1           | 2                    | Drug Group                               | ENDOCRINE AND METABOLIC AGENTS - MISC.* |
| 12-34-xx-xx-xx-xx-   | 2           | 4                    | Drug Class                               | *Posterior Pituitary Hormones***        |
| 12-34-56-xx-xx-xx-   | 3           | 6                    | Drug Subclass                            | *Vasopressin***                         |
| 12-34-56-78-xx-xx-   | 6           | 8                    | Drug Base Name                           | Desmopressin                            |
| 12-34-56-78-90-xx-xx | 4           | 10                   | Drug Name/Drug Name Extension            | Desmopressin Acetate                    |
| 12-34-56-78-90-12-xx | 7           | 12                   | Drug Name and Dosage Form                | Desmopressin Acetate Tablet             |
| 12-34-56-78-90-12-34 | 5           | 14                   | Full GPI with Drug Strength and Strength | Desmopressin Acetate Tablet 0.1 MG      |


# Subsets

## Drug Group

The two-character Drug Group (first subset) classifies general drug products. These 99 Drug Groups include the Drug Classes frequently used in general market research and third-party prescription processing.

2-12 MED-File v2

Published: 11/11

Revised: 08/21

Proprietary Drug Concepts

Examples include:

01 *PENICILLINS*  
25 *CONTRACEPTIVES*  
27 *ANTIDIABETICS*  
36 *ANTIHYPERTENSIVES*  
86 *OPHTHALMIC AGENTS*

## Drug Class

The four-character Drug Class (first and second subset) identifies specific therapeutic drug classes designed to accommodate more detailed market research. The Drug Class also serves as the structural base for most therapeutic drug monitoring applications (such as dosage screening and disease contraindication monitoring). For example, Drug Group 37, DIURETICS, includes the following Drug Classes:

37 *DIURETICS*  
37-10 *Carbonic Anhydrase Inhibitors**  
37-20 *Loop Diuretics**  
37-30 *Mercurial Diuretics**  
37-40 *Osmotic Diuretics**  
37-50 *Potassium Sparing Diuretics**  
37-60 *Thiazides and Thiazide-Like Diuretics**  
37-90 *Diuretics-Miscellaneous**  
37-99 *Diuretic Combinations**

**Note** “99” in the second or third subset is used to identify multiple ingredient (combination) drug products.

## Drug Subclass

The six-character Drug Subclass (first through third subset) is used if further distinction is needed within a Drug Class. For example, the Drug Class 21-40, Antineoplastic - Hormonal Agents, includes the following Drug Subclasses:

21 *ANTINEOPLASTICS AND ADJUNCTIVE THERAPIES*

21-40 *Antineoplastic - Hormonal and Related Agents**  
21-40-20 *Androgens - Antineoplastic***  
21-40-22 *Antiadrenals***

Documentation Manual 2-13  
Published: 11/11  
Revised: 08/21

Editorial Policies

21-40-24 *Antiandrogens***  
21-40-26 *Antiestrogens***  
21-40-28 *Aromatase Inhibitors***  
21-40-30 *Estrogens - Antineoplastic***  
21-40-35 *Estrogen Receptor Antagonist***  
21-40-40 *Progestins - Antineoplastic***  
21-40-50 *LHRH Analogs***  
21-40-55 *Gonadotropin Releasing Hormone (GnRH) Antagonists***  
21-40-60 *Androgen Biosynthesis Inhibitors***

# Drug Base Name

The eight-character Drug Base Name (first through fourth subset) designates the basic drug moiety. The Drug Base Name may represent the therapeutic class and not a specific moiety. This often occurs with combination products. For example, the Drug Subclass 30-04-20, Bisphosphonates, includes the following Drug Base Names:

30-04-20 Bisphosphonates***  
30-04-20-10 Alendronate  
30-04-20-40 Etidronate  
30-04-20-48 Ibandronate  
30-04-20-60 Pamidronate  
30-04-20-65 Risedronate  
30-04-20-70 Tiludronate  
30-04-20-90 Zoledronic Acid

# Drug Name and Drug Name Extension

The 10-character Drug Name and Drug Name Extension (first through fifth subset) designates the specific drug and salt, when applicable. When no salt is present, the Drug Name and Drug Name Extension will be the same as the Drug Base Name. For example, Drug Base Name 22-10-00-20, Dexamethasone, includes the following Drug Names and Drug Name Extensions:

22-10-00-20- Dexamethasone  
22-10-00-20-10 Dexamethasone Acetate  
22-10-00-20-20 Dexamethasone Sodium Phosphate

For combination drug products, the fourth subset generally specifies the number of active ingredient(s) in a multiple ingredient (combination) product. The fifth subset designates the specific combination of ingredients in the drug product.

2-14 MED-File v2  
Published: 11/11  
Revised: 08/21

Proprietary Drug Concepts

For example, Drug Subclass 43-99-30, Decongestant & Antihistamines, includes, but is not limited to, the following combination drug products:

43-99-30  
*Decongestant & Antihistamine***  
43-99-30-02-03  
Acrivastine & Pseudoephedrine  
43-99-30-02-05  
Astemizole & Pseudoephedrine  
43-99-30-02-10  
Azatadine & Pseudoephedrine  
43-99-30-02-25  
Carbinoxamine & Phenylephrine  
43-99-30-02-30  
Chlorpheniramine & Phenylephrine  
43-99-30-02-59  
Loratadine & Pseudoephedrine  
43-99-30-02-70  
Promethazine & Phenylephrine  
43-99-30-02-72  
Promethazine & Pseudoephedrine  
43-99-30-02-80  
Triprolidine & Pseudoephedrine  
43-99-30-03-05  
Brompheniramine-Diphenhydramine-Phenylephrine  
43-99-30-03-24  
Chlorpheniramine-Pyrilamine & Phenylephrine

## Drug Name and Dosage Form

The 12-character Drug Name and Dosage Form (first through sixth subsets) designates the specific drug and its dosage form. For example, Drug Name and Drug Name Extension 67-40-60-70-10, Sumatriptan Succinate, includes the following Drug Name and Dosage Forms:

67-40-60-70-10  
Sumatriptan Succinate  
67-40-60-70-10-03  
Sumatriptan Succinate Tablet  
67-40-60-70-10-20  
Sumatriptan Succinate Solution  
67-40-60-70-10-62  
Sumatriptan Succinate Device  
67-40-60-70-10-64  
Sumatriptan Succinate Kit

## Full GPI with Drug Strength and Strength UOM

The 13th and 14th characters (seventh subset) identify various strengths. For example, Drug Name and Dosage Form 37-20-00-30-00, Furosemide, includes the following:

37-20-00-30-00-03  
Furosemide Tablet  
37-20-00-30-00-03-05  
Furosemide Tab 20 MG  
37-20-00-30-00-03-10  
Furosemide Tab 40 MG  
37-20-00-30-00-03-15  
Furosemide Tab 80 MG  
37-20-00-30-00-20-05  
Furosemide Inj 10 MG/ML  
37-20-00-30-00-20-50  
Furosemide Oral Soln 10 MG/ML

Documentation Manual 2-15  
Published: 11/11  
Revised: 08/21

Editorial Policies


| **Note** | The seventh subset can also imply a route when the first twelve characters of the GPI cannot define the route difference, as illustrated by the last two rows in the table above. |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


When strengths are not specified, the seventh subset may be “00”. For example, Drug Name 90-55-00-75, Hydrocortisone, includes the following dosage forms without strengths:

90-55-00-75-00-29-00  
Hydrocortisone Powder

90-55-00-75-10-29-00  
Hydrocortisone Acetate Powder

## GPI Change Policy

Once assigned to a drug product, a GPI generally does not change for an NDC-UPC-HRI; however, it may be reassigned for one of the following reasons:

- alteration of Wolters Kluwer’s TCS to maintain integrity and usefulness of this system
- refinement of dosage form or strength designations for an ingredient
- data entry revisions to the original GPI assignment


| **Note** | Wolters Kluwer will provide developers and end-users with advance notice for GPI revisions due to the first two reasons above; however, data entry revisions are made without advance notice. Off-cycle GPI revisions are published in weekly DataFacts. Contact Customer Support for more information regarding DataFacts. |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


## Multiple Indications

Drug products that typically have common, yet diverse, therapeutic uses are often classified by pharmacological class. For example, Propranolol is found under Beta-blockers. Beta-blockers are grouped with other cardiovascular drugs because the cardiovascular uses of Beta-blockers are more common than possible therapeutic uses (such as for migraine headaches). Occasionally, multiple GPIs are assigned to an active ingredient. This usually occurs when drug products are packaged and marketed for specific indications. For example, Diphenydramine is found under Antihistamines - Ethanolamines and also under Antihistamine Hypnotics.

## Partial GPI Codes

Only drug products identified with identical 14-character GPIs are pharmaceutically equivalent. A partial GPI refers to a general description of the

2-16 MED-File v2

Published: 11/11

Revised: 08/21

Proprietary Drug Concepts

product based on Wolters Kluwer’s TCS. For example, multiple vitamin products are identified by therapeutic class name as illustrated below:

47-30-00-25-00-01-00  
*Probiotic Product - Cap**  
78-12-00-00-00-03-00  
*B-Complex w/C Tab**  
80-50-00-30-00-01-90  
*Omega-3 Fatty Acids Cap 1000 MG**


| **Note** | Partial GPIs are identified and differentiated from specific GPIs by asterisks before and after the GPI name. Drug products having identical Partial GPIs are not pharmaceutically equivalent drug products. |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |


## Generic Substitution Versus Therapeutic Alternate Identification

MED-File v2 may be used to aid in determining generic and therapeutic equivalents.

Generic substitution involves identifying pharmaceutically equivalent drug products substituted for the originator/trademarked drug products. Pharmaceutically equivalent drug products contain the same active ingredient(s), dosage form, route, and strength or concentration. The GPI can be used to determine pharmaceutical equivalents.

Therapeutic Alternate Identification involves substituting a therapeutically similar drug product for the prescribed drug product. Therapeutic alternates may originate from the same general Drug Grouping (Anti-infective Agents), Drug Group (Cephalosporins), or Drug Class (Cephalosporins - Second Generation). The structure of Wolters Kluwer’s GPI and TCS helps determine different therapeutic equivalents or alternates depending on the number of GPI characters matched.

## Generic Substitution

Drug products identified as pharmaceutically equivalent are not necessarily bioequivalent (drug products entering the patient’s bloodstream at the same rate and in the same amount as the originator drug product) or therapeutically equivalent. Once pharmaceutically equivalent drug products are identified, further restrictions may be necessary to identify generic substitutable alternates for different markets and end-users. Differences in bioequivalence and legal restrictions concerning drug product substitution may result from brand interchange or product substitution. (Refer to the Therapeutic Equivalence Evaluation (TEE) Codes for more information on bioequivalency.)

The following can be used to determine generic substitutable drug products: GPIs, “Generic” drug products, and TEE Codes.

Documentation Manual 2-17  
Published: 11/11  
Revised: 08/21

Editorial Policies

# Generic Product Identifier (GPI)

The GPI identifies pharmaceutically equivalent drug products that are identical in active ingredient(s), dosage form, route, and strength or concentration. Different markets and applications have different definitions of a generic drug product. The GPI is a starting point for selecting generic drug products and should be used in conjunction with other data elements for drug product classification. The GPI does not consider the presence of inactive ingredients. Retrieval of NDCs-UPCs-HRIs with exact 14-character GPI matches (that are not partial GPIs) becomes the starting point for selecting "generic" drug products.

# "Generic" Drug Products

Different markets and applications have different definitions of a "generic" drug product. Wolters Kluwer supplies several codes which, when used with the GPI, determine the following:

- Whether the drug product is available by another source (Multi-Source Code)
- How the drug product is named (Brand Name Code)
- How the Labeler/Manufacturer promotes their drug products (Labeler Type Code)
- Therapeutic Equivalence Evaluation of the drug product (TEE Code)

The Multi-Source Summary Code assigned to a DDID in the Drug Name File is referred to as the Multi-Source Code in the NDC File. The Brand Name Code assigned to a DDID in the Drug Name File is referred to as the Name Type Code in the NDC File.

For more information, see Chapter 4, "MED-File v2 Data Elements" in this manual for details on each code. The table below illustrates how the codes, used together, can determine the best fit for the end-user's requirements.


| Note | The Multi-Source Code is not updated for inactive drug products when generic availability changes. This value is only meaningful in relation to currently marketed (active) drug products. |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |


2-18 MED-File v2

Published: 11/11

Revised: 08/21

Proprietary Drug Concepts

Example:


| Drug Products                                                                                         | Multi-Source Code | Brand Name Code | Description                          |
| ----------------------------------------------------------------------------------------------------- | ----------------- | --------------- | ------------------------------------ |
| Trademarked Products                                                                                  | M, N              | T               | • Generally a tradename drug product |
| • One drug product, or co-licensed drug products, are available for this GPI                          | &nbsp;            | &nbsp;          | &nbsp;                               |
| • Manufactured by a research and development company                                                  | &nbsp;            | &nbsp;          | &nbsp;                               |
| • Sold under a trademarked name                                                                       | &nbsp;            | &nbsp;          | &nbsp;                               |
| Trademarked Products                                                                                  | O                 | T               | • Generally a tradename drug product |
| • More than one company manufactures this drug product                                                | &nbsp;            | &nbsp;          | &nbsp;                               |
| • The manufacturer, usually a research and development company, is the originator of the drug product | &nbsp;            | &nbsp;          | &nbsp;                               |
| • Usually sold under a trademarked name                                                               | &nbsp;            | &nbsp;          | &nbsp;                               |
| Branded Generic or Generic Products Based on End-User Requirements                                    | O                 | B,G             | • Generally a generic drug product   |
| • More than one company manufactures this drug product                                                | &nbsp;            | &nbsp;          | &nbsp;                               |
| • The Manufacturer can be a research and development company or a generic company                     | &nbsp;            | &nbsp;          | &nbsp;                               |
| • Sold under a branded generic or a generic name                                                      | &nbsp;            | &nbsp;          | &nbsp;                               |
| Trademarked or Generic Products Based on End-User Requirements                                        | Y                 | T               | • Generally a tradename drug product |
| • More than one company manufactures this drug product                                                | &nbsp;            | &nbsp;          | &nbsp;                               |
| • The manufacturer is not the originator of the drug product                                          | &nbsp;            | &nbsp;          | &nbsp;                               |
| • Manufactured by a research and development company                                                  | &nbsp;            | &nbsp;          | &nbsp;                               |
| • Sold under a trademarked name                                                                       | &nbsp;            | &nbsp;          | &nbsp;                               |


Documentation Manual 2-19

Published: 11/11

Revised: 08/21

Editorial Policies


| Drug Products                                                | Multi-Source Code | Brand Name Code | Description                                |
| ------------------------------------------------------------ | ----------------- | --------------- | ------------------------------------------ |
| Branded Generic or Generic Products                          | Y                 | B, G            | • Generally a generic drug product         |
| • More than one company manufactures this drug product       | &nbsp;            | &nbsp;          | &nbsp;                                     |
| • The manufacturer is not the originator of the drug product | &nbsp;            | &nbsp;          | &nbsp;                                     |
| • Manufacturer is generally a generic company                | &nbsp;            | &nbsp;          | &nbsp;                                     |
| • Sold under a generic name                                  | &nbsp;            | &nbsp;          | &nbsp;                                     |
| Generic Products                                             | M, N              | G               | • Generally a generic drug product         |
| • Only one company manufactures this drug product            | &nbsp;            | &nbsp;          | &nbsp;                                     |
| • Only one drug product is available for this GPI            | &nbsp;            | &nbsp;          | &nbsp;                                     |
| • Sold under a generic name                                  | &nbsp;            | &nbsp;          | &nbsp;                                     |
| Branded Generic Products                                     | M, N              | B               | • Generally a branded generic drug product |
| • Only one company manufactures this drug product            | &nbsp;            | &nbsp;          | &nbsp;                                     |
| • Only one drug product is available for this GPI            | &nbsp;            | &nbsp;          | &nbsp;                                     |
| • Sold under a generic name                                  | &nbsp;            | &nbsp;          | &nbsp;                                     |


Application of these fields varies; apply your own rules to differentiate between generic and brand drug products. Additionally, the price of the drug product may be more significant than brand or generic status.

Once drug products sharing the same non-partial GPI and the appropriate additional codes values are determined, the TEE Code must then be used to help determine the substitutability of the drug products.

## Therapeutic Equivalence Evaluation (TEE) Codes

When a brand name drug product is prescribed but a generic product is preferred, using the GPI is helpful in determining the alternatives. Retrieval of NDCs-UPCs-HRIs that match all 14 characters of the GPI provides a list of generic alternatives. However, it is often insufficient to select a drug product from a list of NDCs-UPCs-HRIs with matching GPIs. Matching GPIs (not including Partial GPIs) only indicate the same mixture of active ingredients with the same route, strength, and dosage form. A determination of which drug products are

2-20 MED-File v2

Published: 11/11

Revised: 08/21

Proprietary Drug Concepts

bioequivalent is needed. Use of the TEE Code will indicate which drug products are bioequivalent. This is the true measure of drug product activity when considering which drug products are suitable for generic substitution. TEE Codes beginning with "A" (except for TEE Codes "A1" and "A2") represent bioequivalent drug products according to the FDA's Approved Drug Products with Therapeutic Equivalence Evaluations (Orange Book). Using the TEE Code with the GPI enables the end-user to have a list of substitutable drug products sharing the same active ingredients including the same route, strength, and dosage form.

# Generic Product Packaging Code

The Generic Product Packaging Code (GPPC) generically defines a drug product and its packaging similar to how the GPI defines the generic ingredient and therapeutic use.

The GPPC is an eight-character code. The first five characters of the GPPC are random and represent a GPI (GPPC-Core). The last three characters contain the GPPC-Suffix and represent the Package Description, Package Size, Package Size Unit of Measure, Package Quantity, and Unit-Dose/Unit-of-Use Package Code.

The linking of drug products with the same GPPC-Core identifies all drug products with the same GPI which includes generic ingredient, strength, and dosage form. The GPPC-Suffix is alphanumeric to allow for the large number of packaging variations. The GPPC-Suffix represents the same information regardless of the associated GPPC-Core (for example, GPPC-Suffix "003" always represents bottles of 100 eaches, tablets, capsules, etc.). The table below illustrates the structure of the GPPC.


| Description                                            | GPPC  | &nbsp; |
| ------------------------------------------------------ | ----- | ------ |
| &nbsp;                                                 | Core  | Suffix |
| Valium, Tabs, 5 mg, Bottle, 100s ea.                   | 02974 | 003    |
| diazePAM, Tabs, 5 mg, Bottle, 100s ea.                 | 02974 | 003    |
| diazePAM, Tabs, 5 mg, Bottle, 500s ea.                 | 02974 | 027    |
| diazePAM, Tabs, 5 mg, Unit Dose, 100s ea.              | 02974 | 028    |
| diazePAM, Inj., 5 mg/ml, Amp, 2 ml, 50s ea.            | 02978 | A04    |
| Acetaminophen w/Codeine, Caps, 30 mg, Bottle, 100s ea. | 03634 | 003    |


Drug products identified by a Partial GPI are also assigned a GPPC. However, these drug products have the same limitations as Partial GPI Codes.

Documentation Manual 2-21

Published: 11/11

Revised: 08/21

Editorial Policies

The fields defining the GPPC are available in the data elements noted previously. The GPPC can be applied in various ways depending on the practice setting. For example:

- manufacturers can identify comparable drug products from competitors for price comparisons and decisions
- wholesalers can use the data to manage purchasing decisions, control inventory, and reduce overlap between similar drug products from different generic companies
- hospitals can track product use, provide more accurate estimations in bid order purchasing, and reduce or eliminate overlap of same drug products in the formulary
- Third-Party Administrators (TPAs) can control costs by setting a range for reimbursement limits of like GPPCs and investigating those claims falling outside the range
- Pharmacies can use the data to improve purchasing decisions between generic companies and better manage their inventory

# External Drug Concepts

## NDC-UPC-HRI

NDCs and HRIs are 10- or 11-character codes used to identify drug products. Non-prescription drug products may also have a separate UPC according to the standards set forth by the GS1. These codes are converted to eleven characters according to the National Council on Prescription Drugs Program (NCPDP) standards.

Generally, the 11-character NDC is divided into three sections:

- The first five digits indicate the manufacturer
- The next four digits indicate the drug product
- The last two digits indicate the packaging.


| Note | There are instances where a manufacturer/distributor will use the same first nine characters to indicate two distinct drug products. This limitation should be considered in your implementation. |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


The first four or five characters of the NDC or HRI (depending on the format) are assigned by the Food and Drug Administration (FDA) Drug Listing Branch to identify manufacturers. This is the same as the Medi-Span Labeler Identifier, in most cases. The last five or six characters are assigned by manufacturers to identify their product and package designations.

2-22 MED-File v2

Published: 11/11

Revised: 08/21

External Drug Concepts

Drug products regulated by the FDA must use an NDC. Companies that are assigned a four-character labeler code use a 4-4-2 format for their drug products; those who have been assigned a five-character labeler code use either the 5-3-2, 5-4-1, or 5-4-2 format. NDCs in the 5-4-2 format do not follow standard formatting rules and do not convert to a 10-character format.

Surgical supplies and non-prescription drug products may have an NDC and an HRI or UPC.

NDCs-UPCs-HRIs that are repackaged are identified in the NDC File of MED-File v2 by the Repackage Code. Institutional packages are additionally identified by a Modifier Code in the NDC Modifier File.

# ID Number Format Code

In order to assist developers with converting NDCs-UPCs-HRIs, Wolters Kluwer provides an ID Number Format Code. This code enables the developer to

- determine where to place dashes when formatting for display
- convert from the 10- to 11-character format
- convert from the 11- to 10-character format

Example:


| ID Number Format Code | Represents | ID Type |
| --------------------- | ---------- | ------- |
| 1                     | 4-4-2      | NDC     |
| 2                     | 5-3-2      | NDC     |
| 3                     | 5-4-1      | NDC     |
| 4                     | 4-6        | HRI     |
| 5                     | 5-5        | UPC     |
| 6                     | 5-4-2      | NDC     |


Below are examples illustrating the conversion of NDCs-UPCs-HRIs:


| NDC                   | NCPDP Standard 11-character NDC | 11-digit NDC (with hyphens) | ID Format Code |
| --------------------- | ------------------------------- | --------------------------- | -------------- |
| 4-4-2 (9999-9999-99)  | 5-4-2 (09999999999)             | 09999-9999-99               | 1              |
| 5-3-2 (99999-999-99)  | 5-4-2 (99999099999)             | 99999-0999-99               | 2              |
| 5-4-1 (99999-9999-9)  | 5-4-2 (99999999909)             | 99999-9999-09               | 3              |
| 5-4-2 (99999-9999-99) | 5-4-2 (99999999999)             | 99999-9999-99               | 6              |


Documentation Manual 2-23

Published: 11/11

Revised: 08/21

Editorial Policies


| UPC or HRI        | 11-character UPC or HRI | UPC or HRI (with hyphens) | ID Format Code |
| ----------------- | ----------------------- | ------------------------- | -------------- |
| 4-6 (9999-999999) | 5-6 (09999999999)       | 9999-999999               | 4              |
| 5-5 (99999-99999) | 5-6 (99999099999)       | 99999-99999               | 5              |


## Changes to an NDC-UPC-HRI

In the case where an NDC-UPC-HRI has changed for a drug product, two records will be output at the time of the change. The old NDC-UPC-HRI record will be output with an item status of “inactive” and the new NDC-UPC-HRI will be provided for reference. The new NDC-UPC-HRI record will be output with an item status of “active” and the old NDC-UPC-HRI will be provided for reference.

## Secondary Alternate Drug IDs

In cases where a drug product may have more than one ID, MED-File v2 includes secondary IDs for a packaged drug and links them together in the Secondary Alternate ID File. For example, a drug may have both an NDC and a UPC. In some instances, the values for the IDs may be the same; however, the ID Format Codes may be different. Currently, only NDCs-UPCs-HRIs are defined as secondary alternate IDs. Additional ID types may be used in the future.

**Note** In the Secondary Alternate ID File, the NDC-UPC-HRI values are named either the External Drug ID or the Alternate Drug ID. In addition, these fields are 20 characters in length to allow for potential future expansion of the NDC-UPC-HRI.

## Ingredients

MED-File v2 includes both active and inactive ingredients for drugs. Inactive ingredients are generally limited to those that are considered clinically significant, although other inactive ingredients may also be included. Examples of clinically significant inactive ingredients include alcohol and tartrazine due to their potential to elicit drug interactions or an allergic reaction, respectively.

Effective March 1, 2018, Medi-Span will report only active ingredients for compounded products from outsourcing facilities. All inactive ingredients will be excluded. Users of products manufactured by outsourcing facilities should understand that comprehensive allergy screening and alerting for allergenic inactive ingredients will NOT occur.

The following information describes some of the ingredient concepts and their relationship to drug products within MED-File v2.

2-24 MED-File v2

Published: 11/11

Revised: 08/21

Ingredients

# Knowledge Base Drug Code

The Knowledge Base Drug Code (KDC) is a proprietary Wolters Kluwer concept that defines a drug in terms of its ingredients. Single ingredient drugs (for example, acetaminophen) are assigned a KDC. Multiple ingredient drugs (for example, acetaminophen + hydrocodone) are assigned a KDC that represents the ingredient combination.

The KDC is used by some of Wolters Kluwer’s clinical databases, including drug-drug interaction and drug allergy screening.

The KDC is 3-part code that is defined as follows:

- The first five digits represent a single ingredient or combination of ingredients. It is often referred to as the drug “moiety”. For example, “00068” represents Amoxicillin.
- The first seven digits represent the additional ingredient or ingredients (often a salt) that define the specific alternative form of the drug moiety. For example, “0006801” represents Amoxicillin Trihydrate.
- In cases where there are no salt forms for an ingredient, the five-digit and seven-digit values will have the same description. For example, “00231” and “0023101” both represent Carbamazepine.
- The full 10-digit KDC further distinguishes between products with unique characteristics. It is most often used to identify trade (brand) names associated to the ingredients represented by the KDC. For example, “0006801001” represents Amoxil.

**Note** The KDC is not a hierarchical value and the code itself has no meaning.

MED-File includes the full 10-digit KDC as an attribute of the DDID and the NDC-UPC-HRI. The seven-digit KDC is included in the Ingredient Drug File where it can be associated to an ingredient name.

# Association of Ingredients to Drug Concepts

## Ingredient Set

The Ingredient Set is a proprietary Wolters Kluwer concept that uniquely defines the collection of one or more active and significant inactive ingredients of a product formulation.

## Ingredient Name

Each ingredient in the Wolters Kluwer database is assigned a name based on the United States Adopted Name (USAN). When the USAN name is not available, the

Documentation Manual 2-25

Published: 11/11

Revised: 08/21

Editorial Policies

name reflects the name used by the Chemical Abstracts Service (CAS) or other sources such as the manufacturer, if these names are not available.

# Ingredient Strength and Strength Unit of Measure

The strength and strength unit of measure for an ingredient are represented as follows:

- The ingredient strength is a numeric value representing the metric strength, when available. This value may indicate a ratio strength or percentage.
- The strength unit of measure represents the units for the ingredient strength. It can be a percentage or part of a ratio strength.

Examples:


| Drug                                | Ingredient       | Ingredient Strength | Ingredient Strength UOM |
| ----------------------------------- | ---------------- | ------------------- | ----------------------- |
| DDID 47942                          | &nbsp;           | &nbsp;              | &nbsp;                  |
| Lipitor Oral                        | &nbsp;           | &nbsp;              | &nbsp;                  |
| Tablet 10 MG                        | ATORVASTATIN     | &nbsp;              | &nbsp;                  |
| CALCIUM                             | 10               | MG                  | &nbsp;                  |
| DDID 88732                          | &nbsp;           | &nbsp;              | &nbsp;                  |
| Vytorin Oral                        | &nbsp;           | &nbsp;              | &nbsp;                  |
| Tablet 10-10 MG                     | SIMVASTATIN      | 10                  | MG                      |
| &nbsp;                              | EZETIMIBE        | 10                  | MG                      |
| DDID 282                            | &nbsp;           | &nbsp;              | &nbsp;                  |
| Acetaminophen                       | &nbsp;           | &nbsp;              | &nbsp;                  |
| Oral Solution 160                   | &nbsp;           | &nbsp;              | &nbsp;                  |
| MG/5 ML                             | ACETAMINOPHEN    | 160                 | MG/5ML                  |
| DDID 3949 Carmol                    | &nbsp;           | &nbsp;              | &nbsp;                  |
| 10 External                         | &nbsp;           | &nbsp;              | &nbsp;                  |
| Lotion 10%                          | UREA (CARBAMIDE) | 10                  | %                       |
| NDC 00904-3233-52 Calcium           | &nbsp;           | &nbsp;              | &nbsp;                  |
| Carbonate-Vitamin D 600-500 MG-UNIT | CHOLECALCIFEROL  | 400                 | UNIT                    |
| &nbsp;                              | CALCIUM          | &nbsp;              | &nbsp;                  |
| CARBONATE                           | 600              | MG                  | &nbsp;                  |
| &nbsp;                              | FD&C YELLOW #6   | &nbsp;              | &nbsp;                  |
| (SUNSET YELLOW)                     | &nbsp;           | &nbsp;              | &nbsp;                  |


# Representative Ingredient Set

When more than one set of ingredients exists for a drug concept, a representative ingredient set may be assigned. This is especially common for a DDID that represents more than one NDC-UPC-HRI. The formulations of the drug

2-26 MED-File v2

Published: 11/11

Revised: 08/21

Pricing

product by different manufacturer may vary, especially with respect to inactive ingredients. The following guidelines are followed:

- For a generically-named DDID, the representative ingredient set is based on the active ingredients only. Inactive ingredients are not considered.
- For a brand name DDID, the active and inactive ingredients are considered. If more than one ingredient set is possible, the representative ingredient set is the most recently created ingredient set.
- If the DDID is associated with a partial GPI that is not specific to all ingredients, no representative ingredient set is assigned.

Example:


| Drug Concept & Description                       | Ingredient Set | Ingredient      | Ingredient Strength & Strength UOM |
| ------------------------------------------------ | -------------- | --------------- | ---------------------------------- |
| DDID 913                                         | &nbsp;         | &nbsp;          | &nbsp;                             |
| ALPRAZolam Oral Tablet 0.25 MG                   | 1341           | ALPRAZOLAM      | 0.25 MG                            |
| NDC 00228-2027-10 ALPRAZolam Oral Tablet 0.25 MG | 1341           | ALPRAZOLAM      | 0.25 MG                            |
| NDC 00603-2127-21 ALPRAZolam Oral Tablet 0.25 MG | 64871          | ALPRAZOLAM      | 0.25 MG                            |
| &nbsp;                                           | &nbsp;         | SODIUM BENZOATE | &nbsp;                             |


## Chemical Abstracts Service (CAS) Registry Number

MED-File v2 includes the Chemical Abstracts Service (CAS) Registry Number, when available. This number represents a unique external identifier for chemical substances, enabling the use of a non-proprietary means to identify drug ingredients.

## Generic ID

Wolters Kluwer provides its proprietary Generic ID concept value for ingredients with and without CAS Registry Numbers.

## Pricing

This section describes the types of pricing, the pricing policy, and pricing attributes included in MED-File v2.

Documentation Manual 2-27

Published: 11/11

Revised: 08/21

Editorial Policies


| **Note** | Your license agreement will determine whether or not your MED-File v2 product includes drug pricing information. |
| -------- | ---------------------------------------------------------------------------------------------------------------- |


# Average Wholesale Price (AWP)

The Wolters Kluwer Average Wholesale Price (AWP) is intended only to be used by Wolters Kluwer customers. While many customers use this information as a price index, the Wolters Kluwer AWP does not represent an average of wholesale prices from any group of transactions in the marketplace and a wholesaler may agree to sell its products to one or more of its customers at a lower price through the use of any number of methods, such as discounts or rebates.

For a complete explanation of Wolters Kluwer’s AWP Policy, go to [https://www.wolterskluwer.com/en/solutions/medi-span/about/manufacturers-exchange](https://www.wolterskluwer.com/en/solutions/medi-span/about/manufacturers-exchange). You are encouraged to review that AWP Policy carefully and in its entirety, both before using the pricing contained in Wolters Kluwer drug information products and when making ongoing decisions about reasonable and appropriate uses of that information.

As a condition to Wolters Kluwer publishing the AWP of a product, the manufacturer must supply at least one of the following price types:

- Suggested Wholesale Price (SWP)
- Wholesale Acquisition Cost (WAC)
- Direct Price (DP)

In all cases where the manufacturer supplies an SWP, even if accompanied by either or both of a WAC or DP, the AWP value will reflect the manufacturer’s SWP as reported to Wolters Kluwer. In all cases where the manufacturer does not supply an SWP, the AWP results from applying a markup to the manufacturer’s reported WAC or DP. DP is only used to determine AWP when the manufacturer does not supply a WAC. The markup applied to the WAC or DP for active products is based either on a standard markup of 20% or from certain historical, wholesaler-reported data where the historical markup is equal to or less than 20%.

This AWP pricing policy governs pricing information published in documentation manuals of other Wolters Kluwer offerings.


| **Note** | Inactive products prior to September 27, 2009 may have markup factors greater than 20% and were subject to previous Wolters Kluwer AWP Editorial Policies effective at that time. |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


2-28 MED-File v2  
Published: 11/11  
Revised: 08/21

Pricing

# Direct Price (DP)

DP represents the price, as reported to Wolters Kluwer by a manufacturer, at which non-wholesalers and providers may purchase drug products from that manufacturer. DP does not necessarily represent the actual sales price in any single transaction, as any manufacturer may sell its products to one or more non-wholesalers or providers at different prices, which, for example, may be reduced as the result of discounts or rebates. Wolters Kluwer generally does not receive a reported DP for drug products that are sold by a manufacturer exclusively through wholesalers, although in some cases both a DP and a WAC may be provided at the manufacturer's discretion.

# Wholesale Acquisition Cost (WAC)

WAC represents the price, as reported to Wolters Kluwer by a manufacturer, at which wholesalers may purchase drug products from that manufacturer. WAC does not necessarily represent the actual sales price in any single transaction, as any manufacturer may agree to sell its products to one or more wholesalers at a lower price with that wholesaler through the inclusion of any number of methods, such as discounts or rebates.

# Manufacturer's Suggested Wholesale Price (SWP)

SWP is the manufacturer's suggested wholesale price, as reported to Wolters Kluwer by a manufacturer, for its drugs to be sold by wholesalers to their customers. The manufacturer reports this price to Wolters Kluwer. The SWP does not necessarily represent the actual sale price used by a manufacturer in any specific transaction with its own customers. Wholesalers, based on competitive and market factors, determine the actual price they will use to sell the drug product to their customers.

# AWP Indicator Code

The AWP Indicator Code is a proprietary Wolters Kluwer concept that indicates how the AWP was obtained by Wolters Kluwer.

The current values are:


| Value | Description                              |
| ----- | ---------------------------------------- |
| A     | Mark-up ≤ 1.20 mfr. WAC or DP            |
| L     | Std. mark-up of 1.20 mfr. WAC or DP      |
| S     | Mfr. suggested AWP                       |
| K     | Adj. std. mark-up of 1.20 mfr. WAC or DP |
| M     | Std. mark-up of 1.25 mfr. WAC or DP      |


Documentation Manual 2-29

Published: 11/11

Revised: 08/21

Editorial Policies


| **Note** | The codes, descriptions, and definitions above reflect Wolters Kluwer’s current AWP editorial policies. This information may have changed over time with announced changes in our AWP editorial policies. Please refer to current and historical editorial polices or contact Wolters Kluwer Customer Support if you have questions regarding use of these codes, descriptions, and definitions. |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |


The AWP Indicator Code is used as follows:

- Prior to September 26, 2009, AWP Indicator Codes of A, S, and M were in use.
- AWP Indicator Code K was used to make one-time adjustments effective September 26, 2009.
- As of September 27, 2009, AWP Indicator Codes of A, S, and L are used.

## Centers for Medicare and Medicaid Services (CMS) for Federal Upper Limit (FUL) Pricing

MED-File v2 also provides pricing from the Centers for Medicare and Medicaid Services (CMS) for Federal Upper Limit (FUL). This pricing represents the upper price limit established by CMS FUL, when applicable. Data is supplied directly from CMS.

CMS has developed a list of multiple-source drug products with upper price limits for each specific strength and dosage form. They establish ceiling prices for each set of therapeutically equivalent drug products according to the formula in the Medicaid final regulation published July 31, 1987 by CMS’s parent organization, the Department of Health and Human Services (HHS). The rule’s aggregate reimbursement ceiling is set at 150% of the lowest published price for therapeutically equivalent multiple-source drug products. CMS periodically updates the list of covered drug products..

**Note:** On April 1, 2016, CMS replaced CMS FUL pricing with ACA FUL pricing. Wolters Kluwer added a zero price to the current CMS FUL pricing data on that same date. This zero price does not represent a true price.

## Average AWP (AAWP) and Generic Equivalent Average Price (GEAP)

### AAWP

The Average Average Wholesale Price (AAWP) is a proprietary Wolters Kluwer drug pricing concept. Generally, the AAWP represents the average of all AWPs for each multi-source drug product with the same GPPC, not including the

2-30 MED-File v2  
Published: 11/11  
Revised: 08/21

Pricing

originator drug products. This price does not take into consideration the TEE Code assigned to each drug product. When the quantity of manufacturers supplying a generic is insufficient for calculating an average, the AAWP is not calculated. This is a generic price applicable for all drug products sharing the same GPPC; however, all drug products with the same GPPC have not been used in the determination of the AAWP. The AAWP and GEAP Determination section discussed later in this chapter includes the criteria for price determination.

## GEAP

The Generic Equivalent Average Price (GEAP) is a proprietary Wolters Kluwer drug pricing concept. Generally, the GEAP represents the average of AWPs for all multi-source drug products with a TEE Code beginning with "A" (therapeutically equivalent), except for those with TEE Code values of "A1" and "A2", in a given GPPC, not including originator drug products. When a drug product has no approved equivalent or the quantity of manufacturers supplying a generic is insufficient for calculating an average, a GEAP is not calculated. The GEAP is a generic price applicable for all drug products sharing the same GPPC; however, all drug products with the same GPPC have not been used in the determination of the GEAP. The AAWP and GEAP Determination section discussed below includes the criteria for price determination.

**Note** GEAPs are not calculated for drug products that have TEE Codes of "A1" or "A2".

## AAWP and GEAP Determination

The AAWP and GEAP are calculated by Wolters Kluwer and output in the GPPC Price File. The unique key, consisting of the Generic Product Packaging Code, and GPPC Price Code, and Effective Date, is used to identify drug products with the same GPI and packaging used in the calculation. Once drug products meeting the criteria shown below are identified, total the AWPs of the identified drug products and divide by the number of drug products found.

## Criteria for AAWP Calculation

The following is a list of criteria that must be met in order for Wolters Kluwer to calculate AAWPs:

- There must be at least two drug products coded with "Y" Multi-Source Codes. (Originator drug products are not applicable.)
- The drug product's manufacturer (labeler) cannot be a repackager.
- The drug product must be active.
- The drug product cannot be the superseded part of an NDC Change.

Documentation Manual 2-31

Published: 11/11

Revised: 08/21

Editorial Policies

- The drug product's GPI cannot start with "94", "96", "97", "98" (except for GPIs starting with "970510").
- The drug products must have the same Generic Product Packaging Code; however, drug products that have a Unit-Dose/Unit-of-Use Package Code of "U" are in the same calculations as drug products Unit-Dose/Unit-of Use Package Codes of "b" (blank).
- Drug products with "X" Unit-Dose/Unit-of-Use Package Codes are included in a separate calculation, only if all other criteria are met.
- The drug product's GPI cannot be a Partial GPI (GPI Generic Names with asterisks).
- The drug product cannot be a clinic pack.

## Criteria for GEAP Calculation

The following is a list of criteria that must be met in order for Wolters Kluwer to calculate GEAPs:

- The drug products must meet all of the criteria needed for the AAWP calculation.
- The drug products must have TEE Codes beginning with "A" (except for TEE Codes of "A1" and "A2").

## Additional Points to Consider

The following are some additional points to consider regarding AAWP and GEAP

- Since the value of the GPPC represents the Package Description, Package Size, Package Size Unit of Measure, Package Quantity, and Unit-Dose/ Unit-of-Use Package Code, injectable drug products may be subdivided, resulting in an AAWP that is not useful. For example, an Ampicillin injection may come in a single vial, 12 vials, a single ampule, or 12 ampules. Each has a different GPPC and, consequently, a different AAWP and GEAP. Therefore, it may be desirable to average the unit price for GPPCs with the same GPPC-Core and with a Route of Administration of "IV", "IJ", "IM", "SC", or "IT". This price may be more useful for drug products of that generic ingredient and strength.
- The GPPC differentiates drug products with different package sizes. For instance, a pint can be 473 ml or 480 ml. These drug products will have different GPPCs and calculated prices. This same situation occurs for creams and ointments due to the conversion of "ounces" to "grams" when explicit metric sizes are not stated.

2-32 MED-File v2

Published: 11/11

Revised: 08/21

Pricing

# Pricing Attributes and their Relationships

## Unit Price

The Unit Price represents the price of an individual unit as defined by the Package Size Unit of Measure. A unit will represent the lowest common denominator (such as EA, GM, ML) for a given drug product.

The Unit Price can be determined by dividing the Package Price by the product of the Package Size multiplied by the Package Quantity.

$$  
\frac{\text{Package Price}}{(\text{Package Size} \times \text{Package Quantity})} = \text{Unit Price}  
$$

For dry injectable products that may be reconstituted to variable volumes, the Unit Price represents the price per single dry vial, ampule, or syringe.

Within the GPPC Price File, the Unit Price is applicable to the following price types:

- AAWP
- GEAP

Within the NDC Price File, the Unit Price is applicable to the following price types:

- AWP
- DP
- WAC
- CMS FUL

The NDC Price File provides an 11-digit Unit Price with five digits to the left of the decimal and six digits to the right. In addition, a 13-digit Unit Price - Extended value is provided with 8 digits to the left of the decimal and five digits to the right.

When the Unit Price is greater than $99,999,999, the Unit Price is not currently being supplied.

Documentation Manual 2-33

Published: 11/11

Revised: 08/21

Editorial Policies

# Package Price

The Package Price represents the price for the entire package and can be determined by multiplying the Unit Price by the product of multiplying the Package Size by Package Quantity.

Unit Price x (Package Size x Package Quantity) = Package Price

Within the NDC Price File, the Package Price is applicable to the following price types:

- AWP
- DP
- WAC
- CMS FUL

# Price Relationships

The following price relationships exist within the data:

The Package Size multiplied by the Package Quantity equals the Total Package Quantity. The AWP Package Price divided by the Total Package Quantity equals the AWP Unit Price.

Examples:


| Drug Product       | Package Size | Package Size Unit of Measure | Package Quantity | Total Package Quantity | AWP Package Price | AWP Unit Price |
| ------------------ | ------------ | ---------------------------- | ---------------- | ---------------------- | ----------------- | -------------- |
| Crestor            | 90           | EA                           | 1                | 90                     | $470.63           | $5.22922       |
| Gentamicin Sulfate | 2            | ML                           | 25               | 50                     | $94.50            | $1.89000       |


# Unit Price/Package Price Rounding

The following price types are supplied to Wolters Kluwer as package prices with two decimals and the unit prices are determined by Wolters Kluwer to five decimal positions*:

- AWP
- DP
- WAC

In a small number of records, this can result in some precision inconsistencies when converting the Unit Price back to a Package Price. One method to

2-34 MED-File v2

Published: 11/11

Revised: 08/21

Pricing

overcome this is to increase the precision of the Unit Price and determine your own Unit Price to seven decimal positions or greater from the package price:

$$  
\text{Unit Price} = \frac{\text{Package Price}}{\text{Package Size}} \times \text{Package Quantity}  
$$

Example:

## Typical Conversion:

Unit Price = 0.03413 Pack Price = 34.13

Pack Size = 1,000 (GM) Pack Qty = 1

0.03413 x 1,000 = 34.13 (same as pack price)

## Precision Inconsistency:

Unit Price = 0.01606 Pack Price = 473.91

Pack Size = 29,510 (GM) Pack Qty = 1

0.01606 x 29,510 = 473.93 (differs from pack price of 473.91)

**Note** If the Unit Price is determined with greater precision by dividing the Pack Price by the Pack Size, and then times the Pack Quantity, the following result occurs:

$$  
473.91 / 29,510 = 0.0160593  
$$

$$  
0.0160593 \times 29,510 = 473.90994 \text{ or } 473.91 \text{ (same as pack price)}  
$$

The following price type is supplied to Wolters Kluwer as Unit Prices. Precision inconsistencies can occur when converting the Unit Price to Package Prices and then back again:

- CMS FUL

This occurs because only two decimal positions are generally included (dollars and cents) in a package price.

$$  
\text{Package Price} = \text{Unit Price} \times \text{Package Quantity}  
$$

It is possible to determine a Package Price to a greater precision by increasing the number of decimal places, but the price may not be usable as input for many software applications as a result.

Documentation Manual 2-35

Published: 11/11

Revised: 08/21

Editorial Policies

The following price types are determined by Wolters Kluwer as Package Prices. Precision inconsistencies can occur when converting the Package Price to Unit Prices and then back again:

- AAWP
- GEAP

**Note** MED-File included a six-decimal unit price; however, the current prices are determined to five decimals. You may still see a six-decimal unit price within your data.

# Price Effective Date

The Price Effective Date reflects the date that the manufacturer associates to the price information they provide.

# Drug Attributes

# Bioequivalence Code

The Bioequivalence Code is a proprietary Wolters Kluwer concept, assigned to the DDID, that generalizes the Therapeutic Equivalence Evaluation (TEE) Code assigned at the NDC-UPC-HRI level for products sharing a DDID. This code also indicates when the TEE Code cannot be generalized.

For instance, the Bioequivalence Code will be defined as "C" if

- two different packaged drug products (different NDC-UPC-HRI, but share the same DDID) have different TEE Codes (for example: "A1" and "A2")
- when multiple TEE Codes exist for a DDID

Valid Values are:


| Code | Description                             |
| ---- | --------------------------------------- |
| A    | Products in same GPI are equivalent     |
| B    | Products in same GPI are not equivalent |
| C    | Products may or may not be equivalent   |
| N    | Equivalency determination not available |
| U    | Undeterminable (obsolete)               |


2-36 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes

Note  
The value of undeterminable (obsolete) is only applicable in previous versions of this file.

# Brand Name Code

The Brand Name Code is a proprietary Wolters Kluwer concept, assigned to the DDID, that generalizes the Name Type Code assigned at the NDC-UPC-HRI level for products sharing a DDID. The Brand Name Code indicates the type of name used in the Drug Name.

## Valid Values:

- Trademarked Name - any product name that has an associated trademark symbol
- Branded Generic Name - any non-trademarked product name that is not the generic ingredient name
- Generic Name - any product name that is also the generic ingredient name

## Example:


| Trademarked Name (T)            | Branded Generic Name (B)                   | Generically Named (G)                      |
| ------------------------------- | ------------------------------------------ | ------------------------------------------ |
| Adoxa Oral Tablet 100 MG        | Avidoxyl Oral Tablet 100 MG                | Doxycycline Monohydrate Oral Tablet 100 MG |
| Tylenol Oral Tablet 325 MG      | Non-Aspirin Pain Relief Oral Tablet 325 MG | Acetaminophen Oral Tablet 325 MG           |
| Chlor-Trimeton Oral Tablet 4 MG | Aller-Chlor Oral Tablet 4 MG               | Chlorpheniramine Maleate Oral Tablet 4 MG  |


Note  
In this context, the definition of a Branded Generic Name is a name accepted as an industry standard for a specific formulation used by more than one manufacturer/distributor. This name is also used by non-research and development (generic) manufacturers to represent their version of a generic product.

# Clinic Packs

An NDC-UPC-HRI is defined as a Clinic Pack if the drug product is distributed to patients as samples by hospitals, clinics, manufacturers, or physicians. The manufacturer communicates to Wolters Kluwer if a particular NDC-UPC-HRI meets this criteria.

Documentation Manual 2-37  
Published: 11/11  
Revised: 08/21

Editorial Policies

# Controlled Substance Code

The Controlled Substance Code, assigned to the DDID, identifies controlled substances, as classified by the Drug Enforcement Administration (DEA). It generalizes the DEA Class Code assigned at the NDC-UPC-HRI level. If more than one code is possible for a DDID, the value of "Undeterminable" is assigned.

Valid Values:


| Description                             | Definition                                                                                                                                                                                                                                                                       | DEA Class |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| No accepted medical use                 | High abuse potential; medical use not accepted (such as heroin, marijuana, and LSD)                                                                                                                                                                                              | C-I       |
| High abuse, severe dependence liability | High abuse potential with severe dependence liability (such as narcotics, amphetamines, and barbiturates)                                                                                                                                                                        | C-II      |
| Moderate dependence liability           | Less abuse potential than Schedule II drugs and moderate dependence liability (such as nonbarbiturate sedatives, nonamphetamine stimulants, and limited amounts of certain narcotics)                                                                                            | C-III     |
| Limited abuse potential                 | Less abuse potential than Schedule III drugs and limited dependence liability (such as some sedatives, antianxiety agents, and non-narcotic analgesics)                                                                                                                          | C-IV      |
| Limited abuse potential, small amounts  | Limited abuse potential; primarily small amounts of narcotics (codeine) used as antitussives or antidiarrheals; under federal law, limited quantities of certain C-V drugs may be purchased directly from a pharmacist without a prescription; can be either prescription or OTC | C-V       |
| DEA Class Code is not applicable        | A DEA Class Code is not applicable                                                                                                                                                                                                                                               | N/A       |
| Undeterminable                          | A DEA Class Code is undeterminable                                                                                                                                                                                                                                               | Undet     |


2-38 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes

# DEA Class Code

The DEA Class Code, assigned to the NDC-UPC-HRI, identifies federally controlled substances classified by the Drug Enforcement Administration (DEA).


| Description                             | Definition                                                                                                                                                                                                                                                                                   | DEA Class |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| No accepted medical use                 | Schedule I: High abuse potential; medical use not accepted (such as heroin, marijuana, and LSD)                                                                                                                                                                                              | C-I       |
| High abuse, severe dependence liability | Schedule II: High abuse potential with severe dependence liability (such as narcotics, amphetamines, and barbiturates)                                                                                                                                                                       | C-II      |
| Moderate dependence liability           | Schedule III: Less abuse potential than Schedule II drugs and moderate dependence liability (such as nonbarbiturate sedatives, nonamphetamine stimulants, anabolic steroids, and limited amounts of certain narcotics)                                                                       | C-III     |
| Limited abuse potential                 | Schedule IV: Less abuse potential than Schedule III drugs and limited dependence liability (such as some sedatives, anti-anxiety agents, and non-narcotic analgesics)                                                                                                                        | C-IV      |
| Limited abuse potential, small amounts  | Schedule V: Limited abuse potential; primarily small amounts of narcotics (codeine) used as antitussives or antidiarrheals; under federal law, limited quantities of certain C-V drugs may be purchased directly from a pharmacist without a prescription; can be either prescription or OTC | C-V       |
| DEA Class Code is not applicable        | A DEA Class Code is not applicable                                                                                                                                                                                                                                                           | N/A       |


Note  
State laws may be more stringent than federal laws and must also be observed when dispensing controlled substances.

The Controlled Substance Code which is a summarization of the DEA Class Code is assigned to a DDID.

Documentation Manual 2-39  
Published: 11/11  
Revised: 08/21

Editorial Policies

# DESI Code

The Food and Drug Administration (FDA) is responsible for assuring drugs are safe and effective for human use. The DESI Code, assigned to the NDC-UPC-HRI, identifies the stage of review for drugs pending final resolutions of efficacy by the FDA's Drug Efficacy Study Implementation (DESI) program. These drugs are currently rated less than effective (LTE) by the DESI program.

"IRS" refers to drugs that are identical, related, or similar to current DESI drugs. "NOOH" refers to Notice of Opportunity for a Hearing, which is published in the Federal Register.

According to the FDA, the following codes are valid. Additionally, Wolters Kluwer includes the value of “b” (blank) for non-drug and other non-applicable items.

Valid Values:


| Code | Description                              | Definition                                                         |
| ---- | ---------------------------------------- | ------------------------------------------------------------------ |
| b'   | Non-drug and other non-applicable items  | Non-drug and other non-applicable items                            |
| 2    | Determined to be safe and effective      | Non-DESI/IRS drugs or DESI/IRS drugs determined safe and effective |
| 3    | Under review (NOOH has not been issued)  | DESI/IRS drugs under review (NOOH has not been issued)             |
| 4    | Less than effective for some indications | LTE DESI/IRS drugs for some indications                            |
| 5    | Less than effective for all indications  | LTE DESI/IRS drugs for all indications                             |
| 6    | Less than effective, withdrawn           | LTE DESI/IRS drugs withdrawn from the market                       |


CMS is mandated by the Omnibus Budget Reconciliation Act of 1981 banning reimbursement for LTE drug products (DESI Codes 5 and 6) by federal Medicare and Medicaid agencies.

The Federal Drug Rebate program, as part of the Omnibus Budget Reconciliation Act of 1990, requires labelers to submit the DESI status of a drug to CMS.

State Medicaid programs determine coverage of certain drugs based in part on the DESI status of the drug. The CMS FUL is not available to states for specific DESI classes of drugs.

2-40 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes

Medicaid coverage for drug items based on the DESI status of the drug is reflected in the table below:


| Coverage/Rebate/FFP Requirements                                 | DESI Code | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| ---------------------------------------------------------------- | --------- | ------ | ------ | ------ | ------ |
| &nbsp;                                                           | 2         | 3      | 4      | 5      | 6      |
| Mandatory coverage under Medicaid Drug Rebate Program            | X         | &nbsp; | *      | &nbsp; | &nbsp; |
| May be excluded or restricted under Medicaid Drug Rebate Program | &nbsp;    | X      | &nbsp; | &nbsp; | &nbsp; |
| Optional coverage under Medicaid                                 | &nbsp;    | X      | X      | &nbsp; | &nbsp; |
| Subject to rebate payments                                       | X         | X      | *      | &nbsp; | &nbsp; |
| FFP is available                                                 | X         | X      | X      | &nbsp; | &nbsp; |
| FFP is not available                                             | &nbsp;    | &nbsp; | &nbsp; | X      | X      |


Note

- If a drug in this group has an FDA-approved labeled indication for which a NOOH has NOT been issued, the drug is covered for that indication and other medically accepted indications and the drug is subject to rebate.

The Efficacy Code which is a summarization of the DESI code is assigned to a DDID.

# Dollar Rank Code

The Dollar Rank Code is a proprietary Wolters Kluwer concept assigned to the NDC-UPC-HRI that indicates the drug product's annual industry dollar sales rank according to independent survey results. Similar drug products with different strengths or package sizes, thus different NDC-UPC-HRIs, may have different Dollar Rank Codes.

Wolters Kluwer updates this information annually in the spring and notifies customers when the update occurs.

The Dollar Rank is defined as follows:

- Ranked between 1 and 100
- Ranked between 101 and 200
- Ranked between 201 and 300
- Ranked between 301 and 400
- Ranked between 401 and 500

For drugs that are outside the top 500, no ranking is provided.

Documentation Manual 2-41

Published: 11/11

Revised: 08/21

Editorial Policies

# Dosage Form

The Dosage Form is a proprietary Wolters Kluwer concept defining the form in which the drug product is dispensed.

Wolters Kluwer associates dosage forms used by manufacturers to available Wolters Kluwer dosage forms.

For example:


| Manufacturer-described Dosage Form | Wolters Kluwer Dosage Form                        |
| ---------------------------------- | ------------------------------------------------- |
| 12 Hour Extended Release Tablet    | Tablet Extended Release 12 Hour                   |
| 12 Hour Sustained Release Tablet   | &nbsp;                                            |
| 12 Hour Controlled Release Tablet  | &nbsp;                                            |
| Enteric Coated Tablet              | Delayed Release Tablet                            |
| Spray                              | Liquid                                            |
| Drops                              | Liquid, Solutions, or Suspension (as appropriate) |
| Sponge                             | Miscellaneous                                     |
| Therapy Pack                       | Miscellaneous                                     |


A dosage form of Miscellaneous is used when an appropriate Wolters Kluwer dosage form is not available, when the drug product includes a combination of drugs with varying dosage forms (such as tablet and liquid), or in other situations when a dosage form may not be applicable.

The dosage form is included in several places within MED-File v2:

- As an attribute of the DDID in the Drug Name File
- As a component of several of the proprietary Wolters Kluwer drug name concepts
- Within the structure of the Generic Product Identifier (GPI) in the sixth subset (11th and 12th characters).

The same dosage forms are used in all instances, although the codified values used to define them may vary based on the file in which they reside.

2-42 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes


| **Note** | The four-character Dosage Form code is not to be displayed or provided in print form in end-user applications. The code should be translated to its corresponding Value Description as defined in the Validation/Translation File. Use of the Value Abbreviation is also discouraged. Significant patient safety issues are associated with the use of non-standard abbreviations such as those found in the Dosage Form code and its corresponding Value Abbreviation. Similarly, the Description File provides an Abbreviated Textual Description for the Dosage Form. This abbreviated representation of the Dosage Form is not to be displayed or provided in print form in end-user applications. |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |


For a complete list of their current values, go to Appendix D, Dosage Form Codes.

# Efficacy Code

The Food and Drug Administration (FDA) is responsible for assuring drugs are safe and effective for human use. The Efficacy Code, assigned to the DDID, is a generalization of the DESI Code that is assigned to the NDC-UPC-HRI. The DESI Code identifies the stage of review for drugs pending final resolutions of efficacy by the FDA's Drug Efficacy Study Implementation (DES) program. These drugs are currently rated Less Than Effective (LTE) by the FDA's DESI program.

"IRS" refers to drugs that are identical, related, or similar to current DESI drugs. "NOOH" refers to Notice of Opportunity for a Hearing, which is published in the Federal Register.

Documentation Manual 2-43  
Published: 11/11  
Revised: 08/21

Editorial Policies

According to the FDA, the following codes are valid. Additionally, Wolters Kluwer includes the value of “b” (blank) for non-drug and other non-applicable items.

Valid Values:


| Code | Description                              | Definition                                                               |
| ---- | ---------------------------------------- | ------------------------------------------------------------------------ |
| b'   | Non-drug and other non-applicable items  | Non-drug and other non-applicable items                                  |
| 2    | Determined to be safe and effective      | Non-DESI/IRS drugs or DESI/IRS drugs determined to be safe and effective |
| 3    | Under review (NOOH has not been issued)  | DESI/IRS drugs under review (NOOH has not been issued)                   |
| 4    | Less than effective for some indications | LTE DESI/IRS drugs for some indications                                  |
| 5    | Less than effective for all indications  | LTE DESI/IRS drugs for all indications                                   |
| 6    | Less than effective, withdrawn           | LTE DESI/IRS drugs withdrawn from the market                             |
| U    | Undeterminable                           | An Efficacy Code is undeterminable                                       |


CMS is mandated by the Omnibus Budget Reconciliation Act of 1981 banning reimbursement for LTE drug products (DESI Codes 5 and 6) by federal Medicare and Medicaid agencies.

The Federal Drug Rebate program, as part of the Omnibus Budget Reconciliation Act of 1990, requires labelers to submit the DESI status of a drug to CMS.

State Medicaid programs determine coverage of certain drugs based in part on the DESI status of the drug. The CMS FUL is not available to states for specific DESI classes of drugs.

2-44 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes

Medicaid coverage for drug items based on the DESI status of the drug is reflected in the table below:


| Coverage/Rebate/FFP Requirements                                 | DESI Code | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| ---------------------------------------------------------------- | --------- | ------ | ------ | ------ | ------ |
| &nbsp;                                                           | 2         | 3      | 4      | 5      | 6      |
| Mandatory coverage under Medicaid Drug Rebate Program            | X         | &nbsp; | *      | &nbsp; | &nbsp; |
| May be excluded or restricted under Medicaid Drug Rebate Program | &nbsp;    | X      | &nbsp; | &nbsp; | &nbsp; |
| Optional coverage under Medicaid                                 | &nbsp;    | X      | X      | &nbsp; | &nbsp; |
| Subject to rebate payments                                       | X         | X      | *      | &nbsp; | &nbsp; |
| FFP is available                                                 | X         | X      | X      | &nbsp; | &nbsp; |
| FFP is not available                                             | &nbsp;    | &nbsp; | &nbsp; | X      | X      |


Note  
*If a drug in this group has an FDA-approved labeled indication for which a NOOH has NOT been issued, the drug is covered for that indication and other medically accepted indications and the drug is subject to rebate.

## Form Type Code

The Form Type Code is a proprietary Wolters Kluwer concept assigned to the DDID that indicates the form of the drug when the medication is administered to a patient. This form may be different than the form which is packaged and sold by the manufacturer and therefore, may differ from the Dosage Form. The value is generalized to represent all products sharing the same DDID. The Form Type may be:

- Gas
- Liquid
- Solid
- Other

Documentation Manual 2-45

Published: 11/11

Revised: 08/21

Editorial Policies

Examples:


| Drug                            | Form Type | Dosage Form   |
| ------------------------------- | --------- | ------------- |
| Ethyl Chloride External Aerosol | Gas       | Aerosol       |
| Miralax Oral Powder             | Liquid    | Powder        |
| Nexcare Skin Protectant Wipes   | Other     | Miscellaneous |
| Advil PM                        | Solid     | Capsule       |
| Clobetasol Propionate           | Solid     | Ointment      |


## Innerpacks

An NDC-UPC-HRI is defined as an innerpack when the manufacturer reports an internal packaging NDC-UPC-HRI that is associated to the NDC-UPC-HRI on a carton. The manufacturer does not provide pricing on the innerpack. Its pricing is determined from the carton and is updated when a price change occurs to the carton. Innerpacks may not be sold separately by the manufacturer. However, they may be sold individually by the wholesaler.

## Internal-External Code

The Internal-External Code is a proprietary Wolters Kluwer concept, assigned to a DDID, that indicates whether the drug is administered internally, externally, or both. The value is generalized to represent all products sharing a DDID. It complements the Route of Administration for a drug product.

Examples:


| Drug                              | Internal-External                    | Route          |
| --------------------------------- | ------------------------------------ | -------------- |
| Dulcolax Bowel Prep Kit           | Combination of Internal and External | Combination    |
| Dulcolax Oral Tablets 5 MG        | Internally administered              | Oral           |
| Dulcolax Rectal Suppository 10 MG | Externally administered              | Rectal         |
| BD SafetyGlide Insulin Syringe    | Different than above                 | Does not apply |


## Labelers

Within MED-File v2, manufacturers are referred to as labelers. The broader term, labeler, includes those that manufacturer drug products as well as those that repackage or distribute products.

2-46 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes

The following information describes the data associated with labelers.

## Labeler Type Code

The Labeler Type Code is a proprietary Wolters Kluwer concept that helps differentiate among manufacturers that produce products that are promoted as follows:


| Description                      | Definition                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------- |
| Promoted as “Brand”              | Labeler’s products are priced or promoted as “Brand,” “Originator,” or “Innovator” products |
| Promoted as “Generic”            | Labeler’s products are priced or promoted as “Generic” products                             |
| Promoted as “Brand” or “Generic” | Labeler’s products are priced or promoted as either “Brand” or “Generic” products           |


**Note** The Labeler Type Code may change as labelers merge or as market strategies change.

## Medi-Span Labeler Identifier

The Medi-Span Labeler Identifier is a proprietary Wolters Kluwer concept that links the drug product (NDC-UPC-HRI) to its manufacturer or distributor. Most Medi-Span Labeler Identifiers are derived from the labeler code segment of the NDC. However, in some cases, the Medi-Span Labeler Identifier differs from the labeler code segment of the NDC, so that the accurate division name within the manufacturer or distributor can be associated with the drug product. The Medi-Span Labeler Identifier may also differ from the labeler code segment of the NDC when a company purchases another product line and has yet to convert the products to their labeler code.

For example, the Medi-Span Labeler Identifier “00074” for E.E.S. tablets corresponds to the labeler code segment of the NDC. However, for Rondec and Aminosyn, the Medi-Span Labeler Identifier used to assign the manufacturer name is not the same as the labeler portion of their respective NDCs.

Wolters Kluwer has created division-specific Medi-Span Labeler Identifiers to show actual manufacturer names or divisions. A complete list of Medi-Span Labeler Identifiers and Labeler Descriptions is available upon request from Wolters Kluwer’s Customer Support Division.

Documentation Manual 2-47

Published: 11/11

Revised: 08/21

Editorial Policies

# Manufacturer's (Labeler) Name

The Manufacturer's (Labeler) Name indicates the manufacturer, distributor, and/or division whose name is included on the drug product label.

MED-File v2 lists virtually every manufacturer and distributor in the United States. A complete list of Labeler Names and Labeler Abbreviated Names is available upon request.

# Manufacturer's Abbreviated Name

The Manufacturer's Abbreviated Name indicates the shortened name for the manufacturer, distributor, and/or division whose name is included on the label. A complete list of Labeler Names and Labeler Abbreviated Names is available upon request.

Examples:


| Medi-Span Labeler Identifier | Manufacturer's (Labeler) Name | Manufacturer's Abbreviated Name | Labeler Type           |
| ---------------------------- | ----------------------------- | ------------------------------- | ---------------------- |
| 00067                        | NOVARTIS                      | NOV CON HE                      | Brand                  |
| 00078                        | NOVARTIS                      | NOVARTIS                        | Brand                  |
| 00904                        | MAJOR PHARMACEUTICALS         | MAJOR                           | Generic                |
| 17191                        | BAXA CORPORATION              | BAXA CORP                       | Both Brand and Generic |
| 55513                        | AMGEN                         | AMGEN                           | Brand                  |


# Legend Indicator Code

The Legend Indicator Code, assigned to the DDID, indicates Federal Prescription (Rx) (legend) or Over-the-Counter (OTC) (non-legend) status. The Legend Indicator Code generalizes the RX-OTC Indicator Code, assigned at the NDC-UPC-HRI, for all products sharing a DDID. If more than one code is possible for a DDID, the Legend Indicator Code value is "Undeterminable".

# Local/Systemic Code

The Local/Systemic Code is a proprietary Wolters Kluwer concept, assigned to a DDID, that indicates whether the drug product has a local or systemic effect. The value is generalized to represent all products sharing the same DDID. The information is primarily utilized within Wolters Kluwer's drug interactions

2-48 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes

module to allow for interaction alerts to be differentiated based on whether the drug has local or systemic effects.

The values for the Local/Systemic Codes are:

- Local
- Oral
- Parenteral
- Systemic
- Undetermined
- Does Not Apply

Examples:


| Drug                                        | Local/Systemic |
| ------------------------------------------- | -------------- |
| Afrin Nasal Spray Nasal Solution 0.05%      | Local          |
| Morphine Sulfate Injection Solution 8 MG/ML | Parenteral     |
| Morphine Sulfate Oral Tablet 8 MG           | Oral           |
| Morphine Sulfate Rectal Suppository 10 MG   | Systemic       |
| Morphine Sulfate Powder                     | Does Not Apply |


# Maintenance Drug Code

The Maintenance Drug Code is a proprietary Wolters Kluwer concept assigned to a DDID. Third Party Administrators (TPAs) may have provisions to provide maintenance drugs in quantities greater than the standard 30-day supply. Often, a drug's use in a specific patient for a particular indication may be a more relevant determination of a maintenance drug. Consequently, the Maintenance Drug Code is provided as a general guideline. Drugs meeting the following criteria are considered maintenance drugs by Wolters Kluwer:

- The drug is typically a self-administered therapy.
- The drug has low probability for dosage or therapy changes due to side effects, serum drug concentration monitoring, or therapeutic response over a course of prolonged therapy. Therefore, it is cost-effective to dispense the drug in quantities greater than the standard supply.
- The drug's most common use is to treat a chronic disease state when a therapeutic endpoint cannot be determined. Therapy with the drug is not considered curative. A drug may have an indication for maintenance

Documentation Manual 2-49

Published: 11/11

Revised: 08/21

Editorial Policies

therapy but lacks the Maintenance Drug Code if that indication is not the most common.

- The drug is usually administered continuously rather than intermittently (prn or as needed) and typically for a period of 12 months or longer (for example, a diuretic to treat hypertension, but not prenatal vitamins).

These criteria are limited to typical outpatient use of a drug. Dosage forms that are not typical for outpatient dispensing (such as injections that are not self-administered) may be excluded. Non-drug or device products and non-prescription drug products, with the exception of insulin, are generally excluded.

Examples:


| Drug                                                                       | Maintenance Drug Code  |
| -------------------------------------------------------------------------- | ---------------------- |
| Captopril-hydroCHLOROthiazide Oral Tablet 5-25 MG                          | Maintenance Drug       |
| Simvastatin Oral Tablet 10 MG                                              | Maintenance Drug       |
| Amoxicillin-Pot Clavulanate Oral Suspension Reconstituted 125-31.25 MG/5ML | Not a Maintenance Drug |
| HalfLytely with Flavor Packs Oral Kit 5-210 MG-MG                          | Not a Maintenance Drug |


End-users may have special definitions of maintenance drugs. Tables can be created, using the GPI, to allow end-users to define maintenance drugs specific to their patient population or third-party plan.

The Maintenance Drug Code assigned to a DDID can change over time. The change could be the result of:

- Drug Indication change: If it can be determined that the primary use of a drug has changed over time, then the Maintenance Drug Code may change as a result.
- More drug information becomes available: If more information or clarification about the drug and/or its maintenance use becomes available, then the Maintenance Drug Code may change.
- GPI Change to a product: A change to the product's GPI may cause the Maintenance Drug Code to change. This may be the result of incorrect or updated information from the labeler, for example, that may cause the product's GPI to change.

# Modifiers

Modifiers represent a proprietary Wolters Kluwer concept that is assigned to the NDC-UPC-HRI. Modifiers provide supplemental information about the NDC-UPC-

2-50 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes

HRI that is not provided by other drug file attributes. This information can be used to identify unique information about the drug product.

There are three types of Modifiers:

- Package Modifiers
- Product Modifiers
- Trademark Modifiers

Note  
Zero, one, or many modifiers are assigned to an NDC-UPC-HRI.

## Modifier Code

Effective March 1, 2018, Wolters Kluwer will report only active ingredients for compounded products from outsourcing facilities. All other product modifiers will not be applicable for compounded products from outsourcing facilities. Products from outsourcing facilities may be identified by using the Limited Distribution Code of 03.

The Modifier Code is comprised of three two-character subsets. The first subset defines the Modifier Type as follows:


| Value | Description         |
| ----- | ------------------- |
| AA    | Package Modifiers   |
| BB    | Product Modifiers   |
| TT    | Trademark Modifiers |


The first and second subsets define the Modifier Type and Modifier Category.

Documentation Manual 2-51  
Published: 11/11  
Revised: 08/21

Editorial Policies

Examples of Package Modifiers include:


| Values | Description                           |
| ------ | ------------------------------------- |
| AA AA  | Vial Sizes                            |
| AA AB  | Parenteral Packaging Descriptions     |
| AA AC  | Needle Lengths and Gauges             |
| AA AD  | Non-Parenteral Packaging Descriptions |
| AA AE  | Neonatal/Pediatric Packaging          |
| AA AF  | Package Size                          |
| AA AG  | Item Size Description                 |


2-52 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes

Examples of Product Modifiers include:


| Value | Description                                           |
| ----- | ----------------------------------------------------- |
| BB AA | Colors                                                |
| BB AB | Flavors                                               |
| BB AC | Base Types                                            |
| BB AD | Dosage Forms                                          |
| BB AE | Shapes                                                |
| BB AF | Free Descriptions (such as Dye Free and Alcohol Free) |
| BB AG | Fragrance                                             |


**Note** Colors, Flavors, Base Types, Dosage Forms, Shapes, and “Free” Descriptions are included when multiple original drug products are available. These descriptions differentiate generic drug products mimicking original drug products. A color Product Modifier is not present if an NDC-UPC-HRI is available in more than one color.

Examples of Trademark Modifiers include:


| Value | Description               |
| ----- | ------------------------- |
| TT AA | Trademark Packaging Terms |
| TT AB | Trademark Dosage Forms    |


The first, second, and third subsets represent the full Modifier Code, defining the Modifier Type, Modifier Category, and the specific Modifier Code within a category.

## Modifier Description

Each Modifier Code is represented by a description.

Examples of Modifier Codes and their descriptions include:


| Modifier Code | Modifier Description |
| ------------- | -------------------- |
| AAAA28        | 500 ML               |
| AAAA73        | 2 CARTONS OF 30 EACH |
| AAAB38        | W/LUER LOCK          |
| AAAB9D        | W/O DILUENT          |


Documentation Manual 2-53  
Published: 11/11  
Revised: 08/21

Editorial Policies


| Modifier Code | Modifier Description  |
| ------------- | --------------------- |
| AAABN3        | PRECISIONGLIDE NEEDLE |
| AAAC50        | 25G X 5/8             |
| BBAAER        | WHITE/PURPLE          |
| BBAB96        | CHERRY-VANILLA        |
| BBAC7P        | NON-ALKALINE          |
| BBAD37        | SOFTGEL(S)            |
| BBAE23        | RECTANGULAR           |
| BBAF51        | TALK FREE             |
| BBAI01        | MEDICAL FOOD          |
| BBAI03        | AUTHORIZED GENERIC    |
| TTAA64        | CONVENIENCE PACK      |
| TTAAD3        | AMBU-FLEX III         |
| TTAABN4       | DUOTAB                |


For a complete list of Modifier Codes and Modifier Descriptions, refer to the contents of the Modifier File.

# Multi-Source Code

The Multi-Source Code is a proprietary Wolters Kluwer concept assigned to an NDC-UPC-HRI that identifies drug products as either single- or multiple-source original drug products or a generic copy of the standard drug product.

Current values are:


| Code | Description                        | Definition                                                                                                              |
| ---- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| N    | Single-source product              | Single-source product available from one labeler.                                                                       |
| M    | Single-source, co-licensed product | Product is co-licensed and considered a single-source product despite being available from multiple labelers.           |
| O    | Multi-source, originator product   | Product available from multiple labelers; however, this is considered to be the originator (industry standard) product. |
| Y    | Multi-source product               | Multi-source product available from multiple labelers.                                                                  |


2-54 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes

Examples:


| Condition                                                     | N          | M                                                      | O           | Y             |
| ------------------------------------------------------------- | ---------- | ------------------------------------------------------ | ----------- | ------------- |
| Single-Source                                                 | Lantus Inj | -                                                      | -           | -             |
| Co-license                                                    | -          | Adderal XR Oral Capsule Extended Release 24 Hour 10 MG | &nbsp;      | &nbsp;        |
| AND                                                           | &nbsp;     | &nbsp;                                                 | &nbsp;      | &nbsp;        |
| Amphetamine-                                                  | &nbsp;     | &nbsp;                                                 | &nbsp;      | &nbsp;        |
| Dextroamphetamine Oral Capsule Extended Release 24 Hour 10 MG | -          | -                                                      | &nbsp;      | &nbsp;        |
| Original with Generics                                        | -          | -                                                      | Valium 5 mg | diazePAM 5 mg |
| Former Co-licensing with Generics                             | -          | -                                                      | Septra DS   | &nbsp;        |
| Bactrim DS                                                    | SMZ/TMP DS | &nbsp;                                                 | &nbsp;      | &nbsp;        |
| Sulfameth oxazole/                                            | &nbsp;     | &nbsp;                                                 | &nbsp;      | &nbsp;        |
| Trimethop rim DS                                              | &nbsp;     | &nbsp;                                                 | &nbsp;      | &nbsp;        |


This code is provided by Wolters Kluwer as a general guideline. Additional factors such as TEE Code, pricing, and so on may be needed to determine whether generic substitution between drug products is appropriate.

Wolters Kluwer's determination of a multi-source product requires the product to be pharmaceutically equivalent but not necessarily bioequivalent. Repackaged products carry the multi-source code of their brand counterparts and are not considered in the determination of "multi-source" products. Pharmaceutically equivalent products share the same active ingredient(s), route, dosage form, metric strength, and strength unit of measure. Characterizations such as color, shape, flavor, packaging, preservatives, expiration date, and inactive ingredients are not considered in Wolters Kluwer's generic product determination. The GPI can be used to find these pharmaceutical equivalent products. The TEE Code is used to determine bioequivalency of pharmaceutically equivalent drug products.

## Multi-Source Summary Code

The Multi-Source Summary Code is a proprietary Wolters Kluwer concept, assigned to the DDID, that generalizes the Multi-Source Code assigned at the NDC-UPC-HRI level for products sharing a DDID. The values and definitions for the Multi-Source Summary Code are the same as those for the Multi-Source Code, described above.

Documentation Manual 2-55

Published: 11/11

Revised: 08/21

Editorial Policies

# Name Source

The Name Source is a proprietary Wolters Kluwer concept assigned to a DDID that indicates whether the drug name came from the Generic Product, the Product, or both the Generic Product and the Product. When a patented brand name drug is initially marketed, a brand name is created (for example, Crestor). A generically defined drug name is also created (for example, Rosuvastatin Calcium) even though the drug is not marketed in generic form at that time. Thus, the Name Source for Rosuvastatin Calcium is the Generic Product. Conversely, the drug name Simvastatin is marketed as a Product and also represents the Generic Product name for the brand drug Zocor.

Examples:


| Drug                                  | Name Source                 |
| ------------------------------------- | --------------------------- |
| Crestor Oral Tablet 5 MG              | Product                     |
| Rosuvastatin Calcium Oral Tablet 5 MG | Generic Product             |
| Simvastatin Oral Tablet 40 MG         | Generic Product and Product |


# Name Source Code

The Name Source Code indicates if at least one NDC is marketed with this drug description or if a generic drug description has been created.

Examples:


| Drug                                  | Name Source Code                   | Brand Name Code  |
| ------------------------------------- | ---------------------------------- | ---------------- |
| Crestor Oral Tablet 5 MG              | Product does exist in NDC file     | Trademarked Name |
| Rosuvastatin Calcium Oral Tablet 5 MG | Product does not exist in NDC File | Generic Name     |


When generic-named drugs are initially introduced to the market, the Name Source Code will change from a "Product does not exist in NDC File" to "Product does exist in NDC File". When generic-named drugs are removed from the market, this value will change from "Product does exist in NDC File" to "Product does not exist in NDC File".

2-56 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes


| Note | The Name Source Code does not indicate the type of name. Refer to the Brand Name Code for this information. Generic drug product records can have either Name Source Code. |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


# Name Type Code

The Name Type Code is a proprietary Wolters Kluwer concept assigned to the NDC-UPC-HRI that indicates the type of name assigned to the drug.

Values for the Name Type Code are defined as follows:

- Trademarked Name
- Branded Generic Name
- Generic Name

Example:


| Trademarked Name (T)            | Branded Generic Name (B)                   | Generically Named (G)                              |
| ------------------------------- | ------------------------------------------ | -------------------------------------------------- |
| Esgic Oral Capsule 50-325-40 MG | Margesic Oral Capsule 50-325-40 MG         | Butalbital-APAP-Caffeine Oral Capsule 50-325-40 MG |
| Tylenol Oral Tablet 325 MG      | Non-Aspirin Pain Relief Oral Tablet 325 MG | Acetaminophen Oral Tablet 325 MG                   |
| Chlor-Trimeton Oral Tablet 4 MG | Aller-Chlor Oral Tablet 4 MG               | Chlorpheniramine Maleate Oral Tablet 4 MG          |


Note In this context, the definition of a Branded Generic Name is a name accepted as an industry standard for a specific formulation used by more than one manufacturer/distributor. This name is also used by non-research and development (generic) manufacturers to represent their version of a generic product.

The Brand Name code which is a summarization of the Name Type Code is assigned to a DDID.

# Packaging

Drug product packaging is assigned to an NDC-UPC-HRI through the Generic Product Packaging Code (GPPC). There are five packaging-related fields. The unique combination of these fields establishes the GPPC-suffix. All NDC-UPC-HRIs with the same GPPC-suffix will share the same packing.

Documentation Manual 2-57  
Published: 11/11  
Revised: 08/21

Editorial Policies

# Relationship of Packaging Fields


| Drug Product                 | Pkg Size | Package Size Unit of Measure | Package Quantity | Total Package Quantity | Package Description | Unit Dose/ Unit-of-Use |
| ---------------------------- | -------- | ---------------------------- | ---------------- | ---------------------- | ------------------- | ---------------------- |
| Crestor                      | 100      | Each                         | 1                | 100                    | Box                 | Unit Dose              |
| Crestor                      | 90       | Each                         | 1                | 90                     | Bottle              | &nbsp;                 |
| Omnaris                      | 12.5     | Gram                         | 1                | 1                      | Inhaler             | Unit-of-Use            |
| Ampicillin Sodium Injection* | 1        | Each                         | 10               | 10                     | Vial                | Unit Dose              |


**Note**  
*For vials and ampules reconstituted to a variable volume, “1” is used as the Package Size (regardless of the reconstituted volume), and the Package Quantity is the number of vials or ampules in the box or case. The “1” is also used in situations when a metric quantity cannot be expressed.

Each field describes a portion of the packaging. Depending on the needs of the end-user, some applications may require the Package Size and Package Size Unit of Measure, while others may require the Package Size, Package Size Unit of Measure, and Package Quantity.

Additional packaging information is available in the form of Modifiers that do not relate to these standard fields.

# Package Descriptions

The Package Description is a proprietary Wolters Kluwer concept that indicates the container or package used for the drug product. The following is a list of the current package descriptions:


| Description |
| ----------- |
| Ampule      |
| Atomizer    |
| Bag         |
| Blister     |
| Bottle      |
| Box         |
| Can         |


2-58 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes


| Description |
| ----------- |
| Cartridge   |
| Cup         |
| Crtrdg-NDL  |
| Disp Pack   |
| Drum        |
| Flex Cont   |
| Glass Cont  |
| Inhaler     |
| Jar         |
| Pack        |
| Pump Btl    |
| Plas Cont   |
| Punchcard   |
| Package     |
| Packet      |
| Pen         |
| Roll        |
| Spray Btl   |
| Sachet      |
| Strip       |
| Stick       |
| Syringe     |
| Tube        |
| Vial        |


## Package Quantity

The Package Quantity identifies the number of individual containers or units per package as supplied by the manufacturer.

## Package Size

The Package Size represents the total size of the package in volume or number of units contained. In oral suspensions for reconstitution, the Package Size after reconstitution is the number shown in this field, as stated by the manufacturer.

Unit of use packets with quantity of less than one become a quantity of one each. For injectables that can be reconstituted to a variable volume, the Package Size is "1".

Documentation Manual 2-59

Published: 11/11

Revised: 08/21

Editorial Policies

# Package Size Unit of Measure

The Package Size Unit of Measure identifies the unit of measure for the Package Size of the solid, liquid, or gas as dispensed. Wolters Kluwer's assignment of this value is in accordance with the standards set forth by the NCPDP.

Current values are:


| Description |
| ----------- |
| Each        |
| Gram        |
| Milliliter  |


Unit of use packets with a quantity of less than one become a quantity of one each. For injectables that can be reconstituted to a variable volume, the Pack Size Unit of Measure will be "EA".

# Unit-Dose/Unit-of-Use Packaging

Drug products are identified as Unit-Dose or Unit-of-Use based on the following definitions. If the drug product does not meet either of these criteria, it is considered to have standard packaging.

Current values are:


| Description           | Definition                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unit-Dose Packaging   | Any drug product packaged and intended for administration as a single dose at one time. These drug products also maintain complete labeling (UD cup, Strip Packaging tablet/capsule, packet of 2 tablets/capsules that constitute a single dose); this includes all single-dose injections (such as PTV, SDV, amps, syringes, and partial fills). |
| Unit-of-Use Packaging | Any packaged drug product in a standard quantity for a specific therapy suitable for direct dispensing to the patient. Examples include repackaged products, tubes of semisolids, potassium chloride powder packets, nicotine gum, and bulk over-the-counter products.                                                                            |
| Standard Packaging    | Any drug product in which portions are removed for administration and dispensing. This portion does not have labeling for a single-dose unit.                                                                                                                                                                                                     |


2-60 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes

# Repackage Code

The Repackage Code is a proprietary Wolters Kluwer concept, assigned to an NDC-UPC-HRI, that identifies whether products have been repackaged for use by:

- mail order suppliers
- home health care agencies
- nursing homes
- physicians
- others

Repackaged products include both brand name and generic drug products.

Generally, the repackager status is based on the Labeler. However, Wolters Kluwer may override this status at the product level. Repackager status is communicated to Wolters Kluwer by the manufacturer.

Note  
MED-File v2 does not associate a repackaged product to the original source product.

# Reference Brands

The following information outlines the policy for determining reference brands:

- When multiple brand names exist based on the drug's GPI, the originator (multi-source equals "singe source" or "multi-source, originator) is designated as the reference brand.
- Additional brands and/or inactive brands may be designated as the reference brand, based on customer input. Inactive drugs will cease to be the reference brand once they are inactive for > 48 months.
- If there is only one brand name (multi-source equals "single source" or "multi-source, originator), it will be the reference brand, regardless of its active or inactive status.
- Products that are co-licensed may all be designated as the reference brand.
- Branded generics may be considered the representative brand if no trade name products exist.
- Generally, there is no reference brand when  
> All names for a GPI are generic  
> All names have a multi-source equal to "single source" or "multi-source" but no brand names exist  
> The GPI is a partial GPI  
> The item is a bulk chemical

Documentation Manual 2-61

Published: 11/11

Revised: 08/21

Editorial Policies

> The GPI begins with "97"

## Representative GPI

The Representative GPI is a proprietary Wolters Kluwer concept assigned to a DDID. When multiple GPIs are associated to a DDID, a representative is assigned based on the following criteria:

- New formulation
- Active NDC-UPC-HRI
- Most common GPI assigned
- Most appropriate nomenclature between the GPI and DDID description

## Representative KDC

A representative ingredient set may be assigned to a DDID when multiple ingredient sets exists. The Representative KDC is the KDC assigned to that representative ingredient set.

## Route of Administration

The Route of Administration is a proprietary Wolters Kluwer concept that defines how the medication, in the defined dosage form, is administered to the patient.

Wolters Kluwer associates routes uses by manufacturers to available Wolters Kluwer routes.

2-62 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes

Example:


| Manufacturer-defined Route            | Wolters Kluwer Route |
| ------------------------------------- | -------------------- |
| Product can be administered IM or IV  | Injection            |
| Product can be administered SC or IV  | Injection            |
| Product administered outside the body | In Vitro             |
| Device or Not Applicable Route        | Does not apply       |
| Product Kit with Oral and Topical     | Combination          |


The route of administration is included in several places within MED-File v2:

- As an attribute of the DDID in the Drug Name File
- As a component of several of the proprietary Wolters Kluwer drug name concept files
- Implied through the assignment of the GPI

The same routes are used in all instances, although the codified values used to define them may vary based on the file in which they reside.

Current routes are:


| Route          | Comment                                                                                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BUCCAL         | Administered inside the mouth on the mucosa of the cheek                                                                                                                                                              |
| COMBINATION    | More than one route, excluding route combinations that only include injectable sites                                                                                                                                  |
| DENTAL         | Application to teeth or gums                                                                                                                                                                                          |
| DOES NOT APPLY | Use of a route does not apply                                                                                                                                                                                         |
| ENTERAL        | Administered directly into the gastrointestinal tract when the oral route cannot be used (i.e. tube feedings). This route is reserved for commercially available products that are exclusively administered this way. |
| EPIDURAL*      | Injection upon or outside of the dura mater                                                                                                                                                                           |
| EXTERNAL       | Applied externally to the skin or hair                                                                                                                                                                                |
| EXTRACORPOREAL | A procedure that takes place outside of the body (for example, photopheresis, plasmapheresis).                                                                                                                        |
| HEMODIALYSIS   | A process of removing wastes and toxins from the blood. Products having this route are used in the hemodialysis process or added to the hemodialysate as part of the process.                                         |
| IMPLANT        | Placing a drug form, drug delivery device, or other device at the desired administration site by insertion into a body tissue or body cavity by surgical or other appropriate insertion procedures                    |


Documentation Manual 2-63

Published: 11/11

Revised: 08/21

Editorial Policies


| Route            | Comment                                                                                                                    |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| IN VITRO         | Not taken internally or applied externally to a patient’s body                                                             |
| INHALATION       | Drug administration into the lungs (either during a drawn or forced breath)                                                |
| INJECTION        | A set of one or more injectable routes or the route of injection is not specified                                          |
| INTRA-ARTERIAL*  | Injection into an artery or intra-arterial port                                                                            |
| INTRA-ARTICULAR* | Injection into a joint                                                                                                     |
| INTRACARDIAC     | Administered directly to one of the chambers of the heart.                                                                 |
| INTRACAVERNOSAL* | Injection into the corpora cavernosa                                                                                       |
| INTRACAVITARY    | Insertion into a body cavity                                                                                               |
| INTRADERMAL*     | Injection within the epidermis (skin)                                                                                      |
| INTRALESIONAL    | Administered directly into a lesion                                                                                        |
| INTRAMUSCULAR*   | Injection into a muscle group                                                                                              |
| INTRAOCULAR      | Injection, implantation or surgical irrigation within the eyeball                                                          |
| INTRAPERITONEAL  | Administration into the intraperitoneal cavity commonly by injection or instillation into an intraperitoneal catheter port |
| INTRAPLEURAL     | Administration into the pleura or pleural cavity                                                                           |
| INTRASINAL       | Administration of a substance within the nasal or periorbital sinuses                                                      |
| INTRASPINAL      | Administration into the spinal column                                                                                      |
| INTRATHECAL*     | Injection into a subarachnoid or subdural space                                                                            |
| INTRATRACHEAL    | Administered through the trachea (for example, via endotracheal tube or percutaneous injection).                           |
| INTRATYMPANIC    | Administration of a substance directly into the tympanic cavity                                                            |
| INTRAUTERINE     | Administered within the uterus                                                                                             |
| INTRAVENOUS*     | Injection directly into a vein or into a venous line port                                                                  |
| INTRAVENTRICULAR | Administration within a ventricle                                                                                          |
| INTRAVESICAL     | Administered into the bladder                                                                                              |
| INTRAVITREAL     | Administered directly to the vitreous body within the eye.                                                                 |
| IONTOPHORESIS    | Administration of a drug through the skin driven by an electric field.                                                     |
| IRRIGATION       | To flush a body cavity or site with a stream of liquid                                                                     |
| MOUTH/THROAT     | Applied to a mucus membrane of the oral cavity or throat                                                                   |
| NASAL            | Administered via the nose                                                                                                  |
| OPHTHALMIC       | Administered onto the surface of the eyeball or into the conjunctival sac                                                  |
| ORAL             | Taken by mouth                                                                                                             |
| OTIC             | Commonly administered into the external ear canal                                                                          |
| PERFUSION        | Administration (pumping) of a fluid through an organ or tissue                                                             |
| PERIARTICULAR    | Administration around a joint                                                                                              |
| RECTAL           | Administered into the rectum (in the anal canal beyond the anal sphincter)                                                 |


2-64 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes


| Route         | Comment                                                                                                 |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| SUBCUTANEOUS* | Injection through the skin into the loose subcutaneous tissue under the skin                            |
| SUBLINGUAL    | Administered under the tongue                                                                           |
| TRANSDERMAL   | Applied topically (for example, patch or ointment) with absorption through the skin for systemic effect |
| TRANSLINGUAL  | Drug absorption through the tongue into systemic circulation after application on the tongue            |
| TRANSMUCOSAL  | Administration through or across a mucous membrane.                                                     |
| URETHRAL      | Administered via insertion or instillation into the urethra                                             |
| VAGINAL       | Administered into the vagina                                                                            |


- These Codes are used for drug products limited to this particular route. If more than one route of injection is applicable or if the route of injection is not specified, “IJ” is used.

Note  
The comments are for informational purposes only and are not included in the data.

Note  
The 2-character Route of Administration code is not to be displayed or provided in print form in end-user applications. The codes should be translated to its corresponding Value Description as defined in the Validation/Translation File. Use of the Value Abbreviation is also discouraged. Significant patient safety issues are associated with the use of non-standard abbreviations such as those found in the Route of Administration code and its corresponding Value Abbreviation. Similarly, the Description File provides an Abbreviated Textual Description for the Route. This abbreviated representation of the Route is not to be displayed or provided in print form in end-user applications.

# RX-OTC Indicator Code

The RX-OTC Indicator Code, assigned to the NDC-UPC-HRI, indicates Federal Prescription (Rx) (legend) or Over-the-Counter (OTC) (non-legend) status. If coded “R”, the item requires a prescription; if coded “O”, the item is an OTC product. This information is obtained from the manufacturer’s product labeling.

The Legend Indicator Code which is a summarization of the RX-OTC Indicator Code, is assigned to a DDID.

Documentation Manual 2-65  
Published: 11/11  
Revised: 08/21

Editorial Policies

# Rx Rank Code

The Rx Rank Code is a proprietary Wolters Kluwer concept assigned to the NDC-UPC-HRI that indicates the drug product's annual prescription velocity according to independent survey results. Similar drug products with different strengths or package sizes, thus different NDC-UPC-HRIs, may have different Rx Rank Codes.

Wolters Kluwer updates this information annually in the spring and notifies customers when the update occurs.

The Rx Rank is defined as follows:

- Ranked between 1 and 100
- Ranked between 101 and 200
- Ranked between 201 and 300
- Ranked between 301 and 400
- Ranked between 401 and 500

For drugs that are outside the top 500, no ranking is provided.

# Strength

The Strength, in combination with the Strength Unit of Measure, is assigned to the DDID in the Drug Name File. The same Strength and Strength Unit-of-Measure values are also included as attributes in the Dispensable Drug File.

Within the Generic Product Identifier (GPI), the strength and strength-unit-of measure are defined in the seventh subset (13th and 14th characters).

# Strength Unit-of-Measure

The Strength Unit of Measure, when combined with the Strength, represents the dosage strength as provided by the manufacturer. Standards defined by the National Council for Prescription Drug Programs (NCPDP) are applied when establishing the Strength Unit-of-Measure.

Some current values are:


| Strength | Description                | Strength | Description          |
| -------- | -------------------------- | -------- | -------------------- |
| %        | Percent                    | MG       | Milligram            |
| AHFU     | Antihemophilic factor unit | MG-HR    | Milligram/hour       |
| GM       | Gram                       | MG/ML    | Milligram/milliliter |
| GM/ML    | Gram/milliliter            | MINIM    | Minim                |
| MCG/ML   | Microgram/milliliter       | SQ CM    | Square centimeter    |


2-66 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes


| Strength | Description                | Strength | Description     |
| -------- | -------------------------- | -------- | --------------- |
| MEQ      | Milliequivalent            | UNIT     | Unit            |
| MEQ/L    | Milliequivalent/liter      | UNIT/GM  | Unit/gram       |
| MEQ/ML   | Milliequivalent/milliliter | UNIT/ML  | Unit/milliliter |


To view a table of examples, go to the Drug Descriptor Identifier section.

When there is no strength, the Strength and Strength Unit-of-Measure fields will be blanks. Examples include devices and bulk powders used in compounding.

# TEE Code

The Therapeutic Equivalence Evaluation (TEE) Code, assigned to the NDC-UPC-HRI, provides the FDA rating of the therapeutic equivalence of a drug product with other pharmaceutically equivalent drug products, as published in the Orange Book. This code can be used in conjunction with the Generic Product Identifier to isolate equivalent drug products.

In compiling the TEE Code, Wolters Kluwer utilizes the FDA's Orange Book or other sources. The absence of a code does not necessarily imply a product is without New Drug Application (NDA) approval. The FDA can re-evaluate codes for specific NDAs, and those changes will be reflected as they become available.

TEE Codes are included only for multiple-source prescription drug products approved for safety and efficacy by the FDA. Products which do not require FDA approval (for example, those manufactured before 1938) do not have TEE Codes. OTC products are generally not evaluated. Inactive drug products retain the TEE Codes that they had at the time of inactivation.

The Orange Book lists products according to the name of the firm that has obtained the NDA approval. This firm may be the product manufacturer, product labeler, or distributor. The FDA does not correlate the list of approved products with specific products as they are identified in the market.

Interpretation and evaluation of the TEE Code requires an understanding of the specific policies and definitions of the FDA. For this information, the end-user can refer to the introduction in the Orange Book.

Documentation Manual 2-67

Published: 11/11

Revised: 08/21

Editorial Policies

The table below provides a list of the TEE Codes currently in use in MED-File v2:


| Code | Description                   | Definition                                                                                                                                       |
| ---- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| AA   | No Bioequivalence Problems    | Products having no bioequivalence problems in conventional dosage forms                                                                          |
| AB   | Bioequivalence Resolved       | Products meeting necessary bioequivalence requirements                                                                                           |
| AN   | Soln/Powd Aerosol - OK        | Solutions and powders for aerosolization                                                                                                         |
| AO   | Injectable Oil Solutions - OK | Injectable oil solutions (same concentration and vehicle)                                                                                        |
| AP   | Injectable H20 Solutions - OK | Injectable aqueous solutions                                                                                                                     |
| AT   | Topical products - OK         | Topical products                                                                                                                                 |
| A1   | Bioequivalence Resolved       | Equivalent to Orange Book value of “AB1”. Products with this code are only equivalent to other products with the same GPI and the same TEE Code. |
| A2   | Bioequivalence Resolved       | Equivalent to Orange Book value of “AB2”. Products with this code are only equivalent to other products with the same GPI and the same TEE Code. |
| A3   | Bioequivalence Resolved       | Equivalent to Orange Book value of “AB3”. Products with this code are only equivalent to other products with the same GPI and the same TEE Code. |
| A4   | Bioequivalence Resolved       | Equivalent to Orange Book value of “AB4”. Products with this code are only equivalent to other products with the same GPI and the same TEE Code. |
| BC   | CRTB/CRCP/CR - INJS Problems  | Controlled-release dosage forms                                                                                                                  |
| BD   | AI or DF Documented Problems  | Ingredients and dosage forms with documented bioequivalence problems                                                                             |
| BE   | ECTB Oral Problems            | Enteric-coated oral dosage forms                                                                                                                 |
| BN   | Aerosol - Nebulizer Problems  | Products in aerosol-nebulizer drug delivery systems                                                                                              |
| BP   | AI or DF Potential Problems   | Active ingredients and dosage forms with potential bioequivalence problems (for example, injectable suspensions)                                 |
| BR   | Supp/Enem Systemic Problems   | Suppositories or enemas for systemic use                                                                                                         |
| BS   | Drug Standard Problems        | Products having drug standard deficiencies                                                                                                       |
| BT   | Topical Problems              | Topical products with bioequivalence issues                                                                                                      |
| BX   | Insufficient Data             | Drug products for which data are insufficient to determine therapeutic equivalence                                                               |


2-68 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes


| Code | Description                    | Definition                                                                        |
| ---- | ------------------------------ | --------------------------------------------------------------------------------- |
| B*   | Requires Further Investigation | Products requiring further FDA investigation to determine therapeutic equivalence |
| NA   | Not Available                  | Information is not available                                                      |
| NR   | Not Rated                      | Drug product has not yet been rated                                               |


**Note**

TEE Codes beginning with “A” (except values of “A1”, “A2”, “A3” and “A4”) indicate drug products that are therapeutically equivalent to other pharmaceutically equivalent products. Products with an “A” TEE Code are generally considered interchangeable with pharmaceutically equivalent drug products, subject to individual state regulations governing product substitution. In the exception noted above, the full two-character TEE Code is necessary to find therapeutically equivalent drugs (such as when comparing a GPI category containing both “A1”, “A2”, “A3” and “A4” ratings).

If the FDA uses TEE Codes greater than AB4, such as AB5, then similar two-character codes may be adopted by Wolters Kluwer.

In the case where multiple TEE Codes apply to a product, MED-File v2 will only output one value. For example, a product may have both AB1 and AB2 listings in the Orange Book, but MDDB will show only one value and will represent this as 'AB'.

TEE Codes beginning with "B" indicate drug products that the FDA does not consider therapeutically equivalent to other pharmaceutically equivalent drug products. These products are generally prohibited from product substitution by state laws.

The Bioequivalence Code which is a summarization of the TEE Code is assigned to a DDID.

**Drug Product Substitution**

Although FDA guidelines are nationally recognized, specific laws and regulations governing drug product selection are established and enforced by individual states. Therefore, interpreting and applying TEE Codes are the responsibility of the end-user.

**Third-Party Restriction Code**

The Third-Party Restriction Code is a proprietary Wolters Kluwer concept assigned to the NDC-UPC-HRI that provides generalized groupings of drug products. The information may be used by Third Party Administrators (TPAs) or

Documentation Manual 2-69

Published: 11/11

Revised: 08/21

Editorial Policies

others to identify drug products for formulary inclusion or exclusion. This information is provided as a general guideline to follow.

Current values are:


| Code | Description                           | Definition                                                                                                                                                                                                                                                                                                                                 |
| ---- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | Insulin                               | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| 2    | Oral Contraceptives                   | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| 3    | Surgical Supply/Medical Device/Ostomy | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| 4    | Blood Component                       | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| 5    | Diagnostic Agent                      | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| 6    | General Anesthetic                    | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| 7    | Fertility Drugs                       | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| 8    | Anorexic, Anti-obesity                | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| 9    | Multiple Vitamin                      | Single-ingredient vitamins can be selected using the Generic Product Identifier                                                                                                                                                                                                                                                            |
| A    | Used for HIV Infection                | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| B    | Bulk Chemicals                        | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| C    | Cosmetic Alteration Drugs             | Does not include acne agents                                                                                                                                                                                                                                                                                                               |
| D    | Antidepressants                       | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| F    | Multiple Vitamin with Fluoride        | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| G    | Growth Hormones/Biosynthetic Hormones | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| H    | Hypnotics/Sedatives                   | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| I    | Multiple Vitamin with Iron            | Single-ingredient or other iron products not combined                                                                                                                                                                                                                                                                                      |
| J    | Digital Therapy Code                  | This code will be applied to software applications. If the software is approved as a medical device the digital therapy code will be used instead of the device code. If the software/digital therapy is packaged with a drug that has another Third-Party Restriction code, the drug's Third-Party Restriction code will take precedence. |
| K    | Non Oral Systemic Contraceptives      | TD patches, injectables, implants, IUDs                                                                                                                                                                                                                                                                                                    |
| L    | Contraceptives Other                  | Condoms, diaphragms, spermicides                                                                                                                                                                                                                                                                                                           |
| M    | Immunosuppressants                    | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| P    | Antipsychotics                        | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| S    | Smoking Deterrents                    | &nbsp;                                                                                                                                                                                                                                                                                                                                     |
| T    | Antianxiety Agents                    | &nbsp;                                                                                                                                                                                                                                                                                                                                     |


2-70 MED-File v2

Published: 11/11

Revised: 08/21

Drug Attributes


| Code                                                    | Description                                                         | Definition                                      |
| ------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------- |
| V                                                       | Impotence Agents and Hypoactive Sexual Desire Disorder (HSDD) agent | Impotence agent examples: Sildenafil, yohimbine |
| HSDD agent examples: Flibanserin, Bremelanotide Acetate | &nbsp;                                                              | &nbsp;                                          |
| &nbsp;                                                  | Not Applicable                                                      | &nbsp;                                          |


The Third-Party Code assigned to an NDC-UPC-HRI can change over time. The change could be the result of:

- Drug Indication change: If it can be determined that the primary use of a drug has changed over time, then the Third-Party Restriction Code may change as a result.
- More drug information becomes available: If more information or clarification about the drug and/or its use becomes available, then the Third-Party Restriction Code may change.
- GPI Change to a product: A change to the product’s GPI may cause the Third-Party Restriction Code to change. This may be the result of incorrect or updated information from the labeler, for example, that may cause the product’s GPI to change.

Documentation Manual 2-71

Published: 11/11

Revised: 08/21

Editorial Policies

2-72 MED-File v2  
Published: 11/11  
Revised: 08/21

# Chapter 3: Database Structure

## In This Chapter

- Understanding the Database Structure
- Filenames
- Database Layout
- Reserve Fields
- File Relationships

## Understanding the Database Structure

Wolters Kluwer data is organized into multiple files. The files reflect the following information.

> **Note** This information is grouped in categories, not how it appears on the media.

## Copyright Information

A Copyright File is supplied to indicate Wolters Kluwer’s copyright position.

## Marketing/General Technical Information

A ReadMe File is supplied to keep you abreast of the latest news and general technical information.

## Database Control Information

A series of files is supplied with each database to provide information about the database.

- Summary File containing Issue Date, Expiration Date, Volume, and other descriptive information about the database
- Data Dictionary File identifying all the fields that are contained in each of the database-specific files
- Validation/Translation File containing the possible values for fields where applicable

&nbsp;

Database Structure

# Database-Specific Information

Each database has one or more files containing the database's detailed data contents. The data are split across files to allow relational processing of the data.

Database files are available through file transfer protocol (FTP), and through our Web site, wds.medispan.com.

# Filenames

MED-File v2 is available in four file combinations:

- Basic
- Clinical
- Complete
- Pricing

The table on the next page displays the files associated with each option of MED-File v2.

3-2 MED-File v2

Published: 11/11

Revised: 07/21

Filenames

Table 3-1: MED-File v2 Filenames and Options


| Category                                | File Description            | Filename | Basic  | Clinical | Pricing | Complete |
| --------------------------------------- | --------------------------- | -------- | ------ | -------- | ------- | -------- |
| Copyright Information                   | Copyright File              | MF2COPY  | X      | X        | X       | X        |
| Marketing/General Technical Information | ReadMe File                 | MF2READ  | X      | X        | X       | X        |
| Database Control Information            | Summary File                | MF2SUM   | X      | X        | X       | X        |
| &nbsp;                                  | Data Dictionary File        | MF2DICT  | X      | X        | X       | X        |
| &nbsp;                                  | Validation/Translation File | MF2VAL   | X      | X        | X       | X        |
| Database-Specific Information           | Drug Name File              | MF2NAME  | X      | X        | X       | X        |
| &nbsp;                                  | TC-GPI Name File            | MF2TCGPI | X      | X        | X       | X        |
| &nbsp;                                  | NDC File                    | MF2NDC   | X      | X        | X       | X        |
| &nbsp;                                  | Labeler File                | MF2LAB   | X      | X        | X       | X        |
| &nbsp;                                  | GPPC File                   | MF2GPPC  | X      | X        | X       | X        |
| &nbsp;                                  | Error Correct File*         | MF2ERR   | X      | X        | X       | X        |
| &nbsp;                                  | GPPC Price File             | MF2GPR   | &nbsp; | &nbsp;   | X       | X        |
| &nbsp;                                  | NDC Price File              | MF2PRC   | &nbsp; | &nbsp;   | X       | X        |
| &nbsp;                                  | Modifier File               | MF2MOD   | &nbsp; | &nbsp;   | X       | X        |
| &nbsp;                                  | NDC Modifier File           | MF2NDCM  | &nbsp; | &nbsp;   | X       | X        |
| &nbsp;                                  | SDI Drug Name File          | MF2DRGNM | &nbsp; | X        | &nbsp;  | X        |
| &nbsp;                                  | Routed Drug File            | MF2RTDRG | &nbsp; | X        | &nbsp;  | X        |
| &nbsp;                                  | Drug-Dose Form File         | MF2DFDRG | &nbsp; | X        | &nbsp;  | X        |
| &nbsp;                                  | Routed Drug Form File       | MF2RTDF  | &nbsp; | X        | &nbsp;  | X        |
| &nbsp;                                  | Dispensable Drug File       | MF2DRG   | &nbsp; | X        | &nbsp;  | X        |
| &nbsp;                                  | Description File            | MF2DESC  | &nbsp; | X        | &nbsp;  | X        |
| &nbsp;                                  | Route File                  | MF2RTE   | &nbsp; | X        | &nbsp;  | X        |


Documentation Manual 3-3

Published: 11/11

Revised: 07/21

Database Structure


| Category                                 | File Description                          | Filename | Basic  | Clinical | Pricing | Complete |
| ---------------------------------------- | ----------------------------------------- | -------- | ------ | -------- | ------- | -------- |
| Database-Specific Information, continued | Dose Form File                            | MF2FRM   | &nbsp; | ✘        | &nbsp;  | ✘        |
| &nbsp;                                   | Strength-Strength Unit of Measure File    | MF2STUOM | &nbsp; | ✘        | &nbsp;  | ✘        |
| &nbsp;                                   | Drug Concept ID to Ingredient Set ID File | MF2SET   | &nbsp; | ✘        | &nbsp;  | ✘        |
| &nbsp;                                   | Ingredient Set ID to Ingredient ID File   | MF2INGS  | &nbsp; | ✘        | &nbsp;  | ✘        |
| &nbsp;                                   | Ingredient ID to Drug-Strength File       | MF2STR   | &nbsp; | ✘        | &nbsp;  | ✘        |
| &nbsp;                                   | Ingredient Drug File                      | MF2IDRG  | &nbsp; | ✘        | &nbsp;  | ✘        |
| &nbsp;                                   | Secondary Alternate ID File               | MF2SEC   | ✘      | ✘        | ✘       | ✘        |
| &nbsp;                                   | Reference Name File                       | MF2RNM   | &nbsp; | ✘        | &nbsp;  | ✘        |


Note

- The Error Correct File is present only in an Incremental Update when a data entry revision has been made.

Note  
In the future, files may be added to provide information to meet the new needs of end-users.

3-4 MED-File v2  
Published: 11/11  
Revised: 07/21

Database Layout

# Database Layout

The following information is given for each field in MED-File v2:

## Data Element Name

The full name of the field.

## Data Element Code

A code identifying the record and position of the field within the file.

## Field Validation

A flag indicating if values are available in the Validation/Translation File. Wolters Kluwer reserves the right to add values and descriptions for the field.


| Note | The Validation/Translation File contains a list of the most current values for the fields. |
| ---- | ------------------------------------------------------------------------------------------ |


## Record Position

The beginning and ending location in the file for the field.

## Length/Type

The number used to indicate the type and length of the field. For example, 10/N indicates that the field is a 10-digit number. Wolters Kluwer defines data as either character or numeric.

## C = Character

The values for the field contain alphabetic letters, numbers, symbols, or blanks. The field is left-justified. Records without a value for the field will be blank.

## N = Numeric

The values for the field contain numbers or zeros. The values for the field are right-justified or justified at the decimal point. Dates are not distinguished from other numeric fields.

Documentation Manual 3-5

Published: 11/11

Revised: 07/21

Database Structure

# Picture

The COBOL programming representation of the field. The representation includes the length of the field and the type of data. For numeric fields with decimal points, this representation will indicate the location of the fixed decimal point. The values used in the picture are:


| Value | Description                                    |
| ----- | ---------------------------------------------- |
| 9     | Numeric digit                                  |
| X     | Character (alphanumeric, including alphabetic) |
| V     | Implied decimal point                          |


Examples:


| Picture   | Received As | Interpreted |
| --------- | ----------- | ----------- |
| 9(5)V9(3) | 12345123    | 12345.123   |
| 9(6)      | 123456      | 123456.     |
| X(5)      | XXXXX       | XXXXX       |


# Last Change Date

For information about the usage of this record field, see the description for each data file.

# Data Element Description

A brief description of the field.

Note A “b” indicates a blank within a field.

Note Although different programming languages use different representations, the fields remain the same. Wolters Kluwer's database layouts are flexible and not restricted to any particular programming language.

Note Detailed field information is only given for fields that appear in the MED-File v2 Data Dictionary File. Some standard files (such as Summary, ReadMe, and Copyright) do not have fields listed in the Data Dictionary File, therefore only a general discussion of these fields is provided.

3-6 MED-File v2

Published: 11/11

Revised: 07/21

Reserve Fields

# Reserve Fields

Fields marked as “Reserve” may be used by Wolters Kluwer in the future for additional data fields.

Do not assume fields will always be blank. Do not validate these fields during a load. You should ignore all reserve fields.

When we require you to use a reserve field, we will notify you or the end-user with that information.

Documentation Manual 3-7

Published: 11/11

Revised: 07/21

Database Structure

# File Relationships

![img-0.jpeg](img-0.jpeg)

3-8 MED-File v2

Published: 11/11

Revised: 07/21

# Chapter 4: Data Elements

## In This Chapter

- Copyright File
- ReadMe File
- Data Dictionary File
- Validation/Translation File
- Summary File
- Drug Name File
- TC-GPI Name File
- NDC File
- Labeler File
- GPPC File
- Error Correct File
- GPPC Price File
- NDC Price File
- Modifier File
- NDC Modifier File
- SDI Drug Name File
- Routed Drug File
- Drug-Dose Form File
- Routed Drug Form File
- Dispensable Drug File
- Description File
- Route File
- Dose Form File
- Strength-Strength Unit of Measure File
- Drug Concept ID to Ingredient Set ID File
- Ingredient Set ID to Ingredient ID File
- Ingredient ID to Drug-Strength File
- Ingredient Drug File
- Secondary Alternate ID File
- Reference Name File

&nbsp;

Data Elements

# Copyright File

(MF2COPY)

The Copyright File is one record containing the Wolters Kluwer copyright statement.


| Data Element Name                  | Record Position | Type/Length | Picture |
| ---------------------------------- | --------------- | ----------- | ------- |
| UpToDate, Inc. Copyright Statement | 1-55            | C/55        | X(55)   |


# ReadMe File

(MF2READ)

The ReadMe File is a text file that can include the following:

- new release information
- reminders of upcoming changes
- technical information of interest

Note  
Programming for specific values in the ReadMe File is discouraged. The text line is 80 characters for easy printing; however, the content, style, and layout may change without notice. Wolters Kluwer reserves the right to change the format of the information provided in the ReadMe File, but advance notice will be given prior to any changes in field lengths in this file.


| Code | Data Element Name | Record Position | Type/Length | Picture |
| ---- | ----------------- | --------------- | ----------- | ------- |
| B001 | ReadMe Text Line  | 1-80            | C/80        | X(80)   |


# Data Dictionary File

(MF2DICT)

The Data Dictionary File includes data definitions used to generate the physical description of the database files and the remaining files supplied with the offering.

The Data Dictionary File contains the following data elements:


| Code | Data Element Name | Record Position | Type/Length | Picture |
| ---- | ----------------- | --------------- | ----------- | ------- |
| C001 | Field Identifier  | 1-4             | C/4         | X(4)    |
| C005 | Field Description | 5-39            | C/35        | X(35)   |
| C040 | Field Type        | 40-40           | C/1         | X       |


4-2 MED-File v2

Published: 11/11

Revised: 08/21

Data Dictionary File


| Code | Data Element Name       | Record Position | Type/Length | Picture |
| ---- | ----------------------- | --------------- | ----------- | ------- |
| C041 | Field Length            | 41-43           | N/3         | 9(3)    |
| C044 | Implied Decimal Flag    | 44-44           | C/1         | X       |
| C045 | Decimal Places          | 45-46           | N/2         | 9(2)    |
| C047 | Field Validation Flag   | 47-47           | C/1         | X       |
| C048 | Field Abbreviation Flag | 48-48           | C/1         | X       |
| C049 | Reserve                 | 49-64           | C/16        | X(16)   |


Note  
The shaded row represents the unique key into the file.

# Field Identifier

This is a 4-character field.

The Field Identifier specifies the field within the offering by Data Element Code.


| Field Identifier | Field Description     | Field Type | Field Length |
| ---------------- | --------------------- | ---------- | ------------ |
| F039             | Dosage Form           | C          | 4            |
| H022             | RX-OTC Indicator Code | C          | 2            |
| L010             | Effective Date        | N          | 8            |
| Q008             | Concept ID            | N          | 10           |


# Field Description

This is a 35-character field.

The Field Description contains the Data Element Name of the field. This field is mixed case and may be abbreviated to fit into the 35 bytes of space allotted.


| Field Identifier | Field Description     | Field Type | Field Length |
| ---------------- | --------------------- | ---------- | ------------ |
| F039             | Dosage Form           | C          | 4            |
| H022             | RX-OTC Indicator Code | C          | 2            |
| L010             | Effective Date        | N          | 8            |
| Q008             | Concept ID            | N          | 10           |


# Field Type

This is a 1-character field.

The Field Type defines the type of field allowing for automated record layout or table definition.

Documentation Manual 4-3

Published: 11/11

Revised: 08/21

Data Elements

Valid Values:


| Code | Description |
| ---- | ----------- |
| C    | Character   |
| N    | Number      |


Example


| Field Identifier | Field Description     | Field Type | Field Length |
| ---------------- | --------------------- | ---------- | ------------ |
| F039             | Dosage Form           | C          | 4            |
| H022             | RX-OTC Indicator Code | C          | 2            |
| L010             | Effective Date        | N          | 8            |
| Q008             | Concept ID            | N          | 10           |


## Field Length

This is a 3-numeric field.

The Field Length specifies the number of positions representing the data value within the record.


| Field Identifier | Field Description     | Field Type | Field Length |
| ---------------- | --------------------- | ---------- | ------------ |
| F039             | Dosage Form           | C          | 4            |
| H022             | RX-OTC Indicator Code | C          | 2            |
| L010             | Effective Date        | N          | 8            |
| Q008             | Concept ID            | N          | 10           |


## Implied Decimal Flag

This is a 1-character field.

The Implied Decimal Flag indicates an implied decimal in the field.

Valid Values:


| Code | Description                                    |
| ---- | ---------------------------------------------- |
| Y    | Yes, the field has an implied decimal          |
| N    | No, the field does not have an implied decimal |


Note If the Field Type [Data Element Code C040] is "C", this field will always be "N".

4-4 MED-File v2

Published: 11/11

Revised: 08/21

Data Dictionary File

Example:


| Value      | Picture   | Field Type | Field Length | Implied Decimal | Decimal Places |
| ---------- | --------- | ---------- | ------------ | --------------- | -------------- |
| 12.34      | 9(2)V9(2) | N          | 4            | Y               | 02             |
| 12345.1234 | 9(5)V9(4) | N          | 9            | Y               | 04             |
| 1234       | 9(4)      | N          | 4            | N               | 00             |
| ABC        | X(3)      | C          | 3            | N               | 00             |


# Decimal Places

This is a 2-numeric field.

The Decimal Places field shows the number of implied decimal positions in a value if the Implied Decimal Flag [Data Element Code C044] is "Y".

Note If the Implied Decimal Flag is "N", this field is "00".

Example:


| Value      | Picture   | Field Type | Field Length | Implied Decimal | Decimal Places |
| ---------- | --------- | ---------- | ------------ | --------------- | -------------- |
| 12.34      | 9(2)V9(2) | N          | 4            | Y               | 02             |
| 12345.1234 | 9(5)V9(4) | N          | 9            | Y               | 04             |
| 1234       | 9(4)      | N          | 4            | N               | 00             |
| ABC        | X(3)      | C          | 3            | N               | 00             |


# Field Validation Flag

This is a 1-character field.

The Field Validation Flag indicates if the field has associated values in the Validation/Translation File.

Valid Values:


| Flag | Description                                                                                  |
| ---- | -------------------------------------------------------------------------------------------- |
| Y    | Yes, the field has associated validation values in the Validation/Translation File.          |
| N    | No, the field does not have associated validation values in the Validation/Translation File. |


Documentation Manual 4-5

Published: 11/11

Revised: 08/21

Data Elements

# Field Abbreviation Flag

This is a 1-character field.

The Field Abbreviation Flag indicates if the field has associated abbreviation values in the Validation/Translation File.

Valid Values:


| Flag | Description                                                                                      |
| ---- | ------------------------------------------------------------------------------------------------ |
| Y    | Yes, the field has an associated abbreviation field in the Validation/Translation File.          |
| N    | No, the field does not have an associated abbreviation field in the Validation/Translation File. |


# Reserve

This is a 16-character field.

The Reserve field is an unused field that may be used at a future date.

# Validation/Translation File

(MF2VAL)

The Validation/Translation File allows you to design programs that

- validate values and their descriptions for a field
- create pick lists for end-user input
- create alternate values for a field

Using this file makes systems and programs more flexible and easier to maintain. Its use is encouraged in system design. The Validation/Translation File may contain new values for a field without advance notice; therefore, hard coding values is not recommended.

The Validation/Translation File contains the following data elements:


| Code | Name              | Record Position | Type/Length | Picture |
| ---- | ----------------- | --------------- | ----------- | ------- |
| D001 | Field Identifier  | 1-4             | C/4         | X(4)    |
| D005 | Field Value       | 5-19            | C/15        | X(15)   |
| D020 | Language Code     | 20-21           | N/2         | 9(2)    |
| D022 | Value Description | 22-61           | C/40        | X(40)   |


4-6 MED-File v2

Published: 11/11

Revised: 08/21

Validation/Translation File


| Code | Name               | Record Position | Type/Length | Picture |
| ---- | ------------------ | --------------- | ----------- | ------- |
| D062 | Value Abbreviation | 62-76           | C/15        | X(15)   |
| D077 | Reserve            | 77-96           | C/20        | X(20)   |


Note  
The shaded rows represent the unique key into the file.

# Field Identifier

This is a 4-character field.

The Field Identifier specifies the field within the offering by Data Element Code.

Example:


| Field Identifier | Field Value | Language Code | Value Description          | Value Abbreviation |
| ---------------- | ----------- | ------------- | -------------------------- | ------------------ |
| F037             | IJ          | 01            | Injection                  | &nbsp;             |
| F039             | CPCR        | 01            | Capsule Extended Release   | Capsule ER         |
| F069             | 1           | 01            | No accepted medical use    | C-I                |
| H082             | 3           | 01            | Ranked between 201 and 300 | &nbsp;             |


# Field Value

This is a 15-character field.

The Field Value contains the values for the Field Identifier [Data Element Code D001].

Example:


| Field Identifier | Field Value | Language Code | Value Description        | Value Abbreviation |
| ---------------- | ----------- | ------------- | ------------------------ | ------------------ |
| F037             | IJ          | 01            | Injection                | &nbsp;             |
| F039             | CPCR        | 01            | Capsule Extended Release | Capsule ER         |


Documentation Manual 4-7

Published: 11/11

Revised: 08/21

Data Elements


| Field Identifier | Field Value | Language Code | Value Description          | Value Abbreviation |
| ---------------- | ----------- | ------------- | -------------------------- | ------------------ |
| F069             | 1           | 01            | No accepted medical use    | C-I                |
| H082             | 3           | 01            | Ranked between 201 and 300 | &nbsp;             |


# Language Code

This is a 2-numeric field.

The Language Code indicates in which language the Value Description and Value Abbreviation are expressed.

Valid Values:


| Code | Language |
| ---- | -------- |
| 01   | English  |


Example:


| Field Identifier | Field Value | Language Code | Value Description          | Value Abbreviation |
| ---------------- | ----------- | ------------- | -------------------------- | ------------------ |
| F037             | IJ          | 01            | Injection                  | &nbsp;             |
| F039             | CPCR        | 01            | Capsule Extended Release   | Capsule ER         |
| F069             | 1           | 01            | No accepted medical use    | C-I                |
| H082             | 3           | 01            | Ranked between 201 and 300 | &nbsp;             |


# Value Description

This is a 40-character field.

The Value Description provides an interpretation of the Field Value [Data Element Code D005].

4-8 MED-File v2

Published: 11/11

Revised: 08/21

Validation/Translation File

Example:


| Field Identifier | Field Value | Language Code | Value Description          | Value Abbreviation |
| ---------------- | ----------- | ------------- | -------------------------- | ------------------ |
| F037             | IJ          | 01            | Injection                  | &nbsp;             |
| F039             | CPCR        | 01            | Capsule Extended Release   | Capsule ER         |
| F069             | 1           | 01            | No accepted medical use    | C-I                |
| H082             | 3           | 01            | Ranked between 201 and 300 | &nbsp;             |


Note  
The Field Value is not intended for presentation to end-users. To minimize safety concerns and confusion, end-users should be presented with the Value Description. Use of the Value Abbreviation is also discouraged. This applies to all aspects of your application including drop-down lists and field displays in the user interface as well as documents and other printed reports.

## Value Abbreviation

This is a 15-character field.

The Value Abbreviation is a field used for abbreviated Value Descriptions [Data Element Code D022].

Example:


| Field Identifier | Field Value | Language Code | Value Description          | Value Abbreviation |
| ---------------- | ----------- | ------------- | -------------------------- | ------------------ |
| F037             | IJ          | 01            | Injection                  | &nbsp;             |
| F039             | CPCR        | 01            | Capsule Extended Release   | Capsule ER         |
| F069             | 1           | 01            | No accepted medical use    | C-I                |
| H082             | 3           | 01            | Ranked between 201 and 300 | &nbsp;             |


## Reserve

This is a 20-character field.

Documentation Manual 4-9

Published: 11/11

Revised: 08/21

Data Elements

The Reserve field is an unused field that may be used at a future date.

# Summary File

(MF2SUM)

The Summary File provides specific information for use and reference during loading or updating processes. It allows you to check that you have received the proper offering, are using the appropriate update technique, and have not missed updates.

The format of the Summary File allows for easy viewing and printing during loading and verification.

To ensure the proper sequence of updates, a Volume Number and Supplement Number are included. When applicable, Locality Information (country and language identification) is supplied. The Summary File includes

- copyright information
- identification by Database Name
- product issue information (including the Version Number, Volume Number, Create Date, Issue Date, Expiration Date, and Kill Date)
- the File Mode (Production or Test)
- the File Type (incremental update or full replacement database)
- a Table of Contents (listing filenames, location of files, number of files, file sizes, and number of records in each file)

Note  
This file is supplied in its entirety regardless of the type of database ordered.


| Code | Data Element Name | Record Position | Type/Length | Picture |
| ---- | ----------------- | --------------- | ----------- | ------- |
| A001 | Record Type       | 1-3             | C/3         | X(3)    |
| A004 | Reserve 1         | 4-4             | C/1         | X       |
| A005 | Sequence Number   | 5-7             | N/3         | 9(3)    |
| A008 | Reserve 2         | 8-8             | C/1         | X       |
| A009 | Comment Marker    | 9-9             | C/1         | X       |
| A010 | Data or Comment   | 10-96           | C/87        | X(87)*  |


Note

- The length for records within the Summary File is not fixed, and may vary from row to row; however, it will not exceed the value noted in the table above.

4-10 MED-File v2

Published: 11/11

Revised: 08/21

Drug Name File

# Drug Name File

(MF2NAME)

The Drug Name File provides the primary product name used to identify groups of drug and health-related items. It also contains many attributes of the drug name and provides keys to access several of Wolters Kluwer's clinical database offerings.

Note  
The values listed here are generalized to the drug name level. If you need to know the values of a particular drug item, refer to the "NDC File".

The Drug Name File contains the following data elements:


| Code | Data Element Name              | Record Position | Type/Length | Picture |
| ---- | ------------------------------ | --------------- | ----------- | ------- |
| F001 | Drug Descriptor Identifier     | 1-6             | N/6         | 9(6)    |
| F007 | Drug Name                      | 7-36            | C/30        | X(30)   |
| F037 | Route of Administration Code   | 37-38           | C/2         | X(2)    |
| F039 | Dosage Form                    | 39-42           | C/4         | X(4)    |
| F043 | Strength                       | 43-57           | C/15        | X(15)   |
| F058 | Strength Unit-of-Measure       | 58-67           | C/10        | X(10)   |
| F068 | Bioequivalence Code            | 68-68           | C/1         | X       |
| F069 | Controlled Substance Code      | 69-69           | C/1         | X       |
| F070 | Efficacy Code                  | 70-70           | C/1         | X       |
| F071 | Legend Indicator Code          | 71-71           | C/1         | X       |
| F072 | Multi-Source Summary Code      | 72-72           | C/1         | X       |
| F073 | Brand Name Code                | 73-73           | C/1         | X       |
| F074 | Name Source Code               | 74-74           | C/1         | X       |
| F075 | Generic Product Identifier     | 75-88           | C/14        | X(14)   |
| F089 | Knowledge Base Drug Code       | 89-98           | N/10        | 9(10)   |
| F099 | New Drug Descriptor Identifier | 99-104          | N/6         | 9(6)    |
| F105 | Screenable Flag                | 105-105         | C/1         | X       |
| F106 | KDC Flag                       | 106-106         | C/1         | X       |
| F107 | Local/Systemic Code            | 107-107         | C/1         | X       |
| F108 | Maintenance Drug Code          | 108-108         | C/1         | X       |
| F109 | Form Type Code                 | 109-109         | C/1         | X       |
| F110 | Internal-External Code         | 110-110         | C/1         | X       |


Documentation Manual 4-11

Published: 11/11

Revised: 08/21

Data Elements


| Code | Data Element Name       | Record Position | Type/Length | Picture |
| ---- | ----------------------- | --------------- | ----------- | ------- |
| F111 | Single-Combination Code | 111-111         | C/1         | X       |
| F112 | Representative GPI Flag | 112-112         | C/1         | X       |
| F113 | Representative KDC Flag | 113-113         | C/1         | X       |
| F114 | Reserve                 | 114-119         | C/6         | X(6)    |
| F120 | Transaction CD          | 120-120         | C/1         | X       |
| F121 | Last Change Date        | 121-128         | N/8         | 9(8)    |


Note  
The shaded row represents the unique key into the file.

# Drug Descriptor Identifier

This is a 6-digit numeric field.

The Drug Descriptor Identifier (DDID) is a six-digit number that identifies a unique combination of Drug Name, Route, Dosage Form, Strength, and Strength Unit of Measure. The value of the identifier itself has no meaning. It is used to identify a unique drug product with respect to these fields alone. It does not distinguish drug products by Package Size, TEE Code, DESI Code, DEA Class Code, Brand Name, GPI, or Multi-Source Summary Code.

This code is associated to the NDC File in a one-to-many relationship.

Note  
The Drug Descriptor Identifier and Dispensable Drug Identifier are one and the same, and may be used interchangeably in this and other Wolters Kluwer documentation. For more information, go to Drug Descriptor Identifier in Chapter 2, "Editorial Policies".

Example:


| Drug Descriptor ID | Drug Name             | Route | Dosage Form | Strength | SUM    |
| ------------------ | --------------------- | ----- | ----------- | -------- | ------ |
| 001847             | Artificial Tears      | OP    | OINT        | &nbsp;   | &nbsp; |
| 023426             | vinCRISTine Sulfate   | IV    | SOLN        | 1        | MG/ML  |
| 032186             | Diltiazem HCl CR      | PO    | CP12        | 120      | MG     |
| 088732             | Vytorin               | PO    | TABS        | 10-10    | MG     |
| 089216             | HalfLytely Bowel Prep | PO    | KIT         | 5-210    | MG-GM  |


4-12 MED-File v2

Published: 11/11

Revised: 08/21

Drug Name File

# Drug Name

This is a 30-character field.

The Drug Name field reflects the product name shown by the manufacturer on the package. This 30-character name is depicted in upper and lower case. Some drug names are represented using Tall Man letters to distinguish similar drug names and reduce the potential for medication errors. Tall Man letters should be maintained and are not to be changed within your application. An example of drug names with Tall Man letters are vinCRISTine Sulfate and vinBLASTine Sulfate.

For more information, see "Drug Name" in Chapter 2.

Example:


| Drug Descriptor ID | Drug Name             | Route | Dosage Form | Strength | SUM    |
| ------------------ | --------------------- | ----- | ----------- | -------- | ------ |
| 001847             | Artificial Tears      | OP    | OINT        | &nbsp;   | &nbsp; |
| 023426             | vinCRISTine Sulfate   | IV    | SOLN        | 1        | MG/ML  |
| 032186             | Diltiazem HCl CR      | PO    | CP12        | 120      | MG     |
| 088732             | Vytorin               | PO    | TABS        | 10-10    | MG     |
| 089216             | HalfLytely Bowel Prep | PO    | KIT         | 5-210    | MG-GM  |


# Route Of Administration Code

This is a 2-character field.

The Route of Administration Code defines the route of the drug based on the packaging. This route may not represent the clinical route by which the drug is ultimately given to a patient.

Note The Comment column in the table below is for information purposes only. Its contents are not included in the Validation/Translation File.

Note The 2-character Route of Administration Code is not to be displayed or provided in print form in end-user applications. The code should be translated to its corresponding Value Description as defined in the Validation/Translation File. Significant patient safety issues are associated with the use of non-standard abbreviations such as those found in the Route of Administration Code.

Documentation Manual 4-13

Published: 11/11

Revised: 08/21

Data Elements

Example


| Drug Descriptor ID | Drug Name             | Route | Dosage Form | Strength | SUM    |
| ------------------ | --------------------- | ----- | ----------- | -------- | ------ |
| 001847             | Artificial Tears      | OP    | OINT        | &nbsp;   | &nbsp; |
| 023426             | vinCRIStine Sulfate   | IV    | SOLN        | 1        | MG/ML  |
| 032186             | Diltiazem HCl CR      | PO    | CP12        | 120      | MG     |
| 088732             | Vytorin               | PO    | TABS        | 10-10    | MG     |
| 089216             | HalfLytely Bowel Prep | PO    | KIT         | 5-210    | MG-GM  |


The current values are:


| Route            | Code | Description                                                                                                                                                                                                           |
| ---------------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BUCCAL           | BU   | Administered inside the mouth on the mucosa of the cheek                                                                                                                                                              |
| COMBINATION      | CO   | More than one route, excluding route combinations that only include injectable sites                                                                                                                                  |
| DENTAL           | DT   | Application to teeth or gums                                                                                                                                                                                          |
| DOES NOT APPLY   | XX   | Use of a route does not apply                                                                                                                                                                                         |
| ENTERAL          | EN   | Administered directly into the gastrointestinal tract when the oral route cannot be used (i.e. tube feedings). This route is reserved for commercially available products that are exclusively administered this way. |
| EPIDURAL*        | EP   | Injection upon or outside of the dura mater                                                                                                                                                                           |
| EXTERNAL         | EX   | Applied externally to the skin or hair                                                                                                                                                                                |
| EXTRACORPOREAL   | EC   | A procedure that takes place outside the body (i.e. photopheresis, plasmapheresis).                                                                                                                                   |
| HEMODIALYSIS     | HM   | A process of removing wastes and toxins from the blood. Products having this route are used in the hemodialysis process or added to the hemodialysate as part of the process.                                         |
| IMPLANT          | IL   | Placing a drug form, drug delivery device, or other device at the desired administration site by insertion into a body tissue or body cavity by surgical or other appropriate insertion procedures                    |
| IN VITRO         | VI   | Not taken internally or applied externally to a patient’s body                                                                                                                                                        |
| INHALATION       | IN   | Drug administration into the lungs (either during a drawn or forced breath)                                                                                                                                           |
| INJECTION        | IJ   | A set of one or more injectable routes or the route of injection is not specified                                                                                                                                     |
| INTRA-ARTERIAL*  | IA   | Injection into an artery or intra-arterial port                                                                                                                                                                       |
| INTRA-ARTICULAR* | IX   | Injection into a joint                                                                                                                                                                                                |


4-14 MED-File v2

Published: 11/11

Revised: 08/21

Drug Name File


| Route            | Code | Description                                                                                                                |
| ---------------- | ---- | -------------------------------------------------------------------------------------------------------------------------- |
| INTRACARDIAC     | CA   | Administered directly to one of the chambers of the heart.                                                                 |
| INTRACAVERNOSAL* | IC   | Injection into the corpora cavernosa                                                                                       |
| INTRACAVITARY    | CV   | Insertion into a body cavity.                                                                                              |
| INTRADERMAL*     | ID   | Injection within the epidermis (skin)                                                                                      |
| INTRALESIONAL    | LS   | Administered directly into a lesion.                                                                                       |
| INTRAMUSCULAR*   | IM   | Injection into a muscle group                                                                                              |
| INTRAOCULAR      | IO   | Injection, implantation or surgical irrigation within the eyeball                                                          |
| INTRAPERITONEAL  | IP   | Administration into the intraperitoneal cavity commonly by injection or instillation into an intraperitoneal catheter port |
| INTRAPLEURAL     | PL   | Administration into the pleura or pleural cavity.                                                                          |
| INTRASINAL       | SN   | Administration of a substance within the nasal or periorbital sinuses.                                                     |
| INTRATHECAL*     | IT   | Injection into a subarachnoid or subdural space                                                                            |
| INTRATRACHEAL    | TR   | Administered through the trachea (i.e. via endotracheal tube or percutaneous injection).                                   |
| INTRATYMPANIC    | TP   | Administration of a substance directly into the tympanic cavity.                                                           |
| INTRAUTERINE     | IU   | Administered within the uterus                                                                                             |
| INTRAVENOUS*     | IV   | Injection directly into a vein or into a venous line port                                                                  |
| INTRAVESICAL     | IS   | Administered into the bladder                                                                                              |
| INTRAVITREAL     | IZ   | Administered directly to the vitreous body within the eye.                                                                 |
| IONTOPHORESIS    | PH   | Administration of a drug through the skin driven by an electric field.                                                     |
| IRRIGATION       | IR   | To flush a body cavity or site with a stream of liquid                                                                     |
| MOUTH/THROAT     | MT   | Applied to a mucous membrane of the oral cavity or throat                                                                  |
| NASAL            | NA   | Administered via the nose                                                                                                  |
| OPHTHALMIC       | OP   | Administered onto the surface of the eyeball or into the conjunctival sac                                                  |
| ORAL             | PO   | Taken by mouth                                                                                                             |
| OTIC             | OT   | Commonly administered into the external ear canal                                                                          |
| PERFUSION        | PF   | Administration (pumping) of a fluid through an organ or tissue                                                             |
| RECTAL           | PR   | Administered into the rectum (in the anal canal beyond the anal sphincter)                                                 |
| SUBCUTANEOUS*    | SC   | Injection through the skin into the loose subcutaneous tissue under the skin                                               |
| SUBLINGUAL       | SL   | Administered under the tongue                                                                                              |
| TRANSDERMAL      | TD   | Applied topically (e.g., patch or ointment) with absorption through the skin for systemic effect                           |


Documentation Manual 4-15

Published: 11/11

Revised: 08/21

Data Elements


| Route        | Code | Description                                                                                  |
| ------------ | ---- | -------------------------------------------------------------------------------------------- |
| TRANSLINGUAL | TL   | Drug absorption through the tongue into systemic circulation after application on the tongue |
| TRANSMUCOSAL | TM   | Administration through or across a mucous membrane.                                          |
| URETERAL     | UT   | Administration into a ureter                                                                 |
| URETHRAL     | UR   | Administered via insertion or instillation into the urethra                                  |
| VAGINAL      | VA   | Administered into the vagina                                                                 |


- These Codes are used for drug products limited to this particular route. If more than one route of injection is applicable or if the route of injection is not specified, Wolters Kluwer will assign a route of "IJ".

# Dosage Form Code

This is a 4-character field.

The Dosage Form Code indicates the form in which the drug product is dispensed.

Note  
The 4-character Dosage Form Code is not to be displayed or provided in print form in end-user applications. The code should be translated to its corresponding Value Description as defined in the Validation/Translation File. Use of the Value Abbreviation is also discouraged. Significant patient safety issues are associated with the use of non-standard abbreviations such as those found in the Dosage Form Code and its corresponding Value Abbreviation.

For a complete list of their current values, go to Appendix D, "Dosage Form Codes".

Example:


| Drug Descriptor ID | Drug Name             | Route | Dosage Form | Strength | SUM    |
| ------------------ | --------------------- | ----- | ----------- | -------- | ------ |
| 001847             | Artificial Tears      | OP    | OINT        | &nbsp;   | &nbsp; |
| 023426             | vinCRISTine Sulfate   | IV    | SOLN        | 1        | MG/ML  |
| 032186             | Diltiazem HCl CR      | PO    | CP12        | 120      | MG     |
| 088732             | Vytorin               | PO    | TABS        | 10-10    | MG     |
| 089216             | HalfLytely Bowel Prep | PO    | KIT         | 5-210    | MG-GM  |


4-16 MED-File v2

Published: 11/11

Revised: 08/21

Drug Name File

# Strength

This is a 15-character field.

The Strength is a character representation of the product's ingredient strength. When combined with the Strength Unit of Measure, it represents the dosage strength as provided by the manufacturer.

Example:


| Drug Descriptor ID | Drug Name             | Route | Dosage Form | Strength | SUM    |
| ------------------ | --------------------- | ----- | ----------- | -------- | ------ |
| 001847             | Artificial Tears      | OP    | OINT        | &nbsp;   | &nbsp; |
| 023426             | vinCRISTine Sulfate   | IV    | SOLN        | 1        | MG/ML  |
| 032186             | Diltiazem HCI CR      | PO    | CP12        | 120      | MG     |
| 088732             | Vytorin               | PO    | TABS        | 10-10    | MG     |
| 089216             | HalfLytely Bowel Prep | PO    | KIT         | 5-210    | MG-GM  |


# Strength Unit Of Measure

This is a 10-character field.

The Strength Unit of Measure (SUM), when combined with the Strength, represents the dosage strength as provided by the manufacturer. Valid Values:*


| Strength | Description                    | Strength | Description          |
| -------- | ------------------------------ | -------- | -------------------- |
| %        | Percent                        | MG       | Milligram            |
| AHFU     | Antihemophilic factor unit     | MG/HR    | Milligram/hour       |
| GM       | Gram                           | MG/ML    | Milligram/milliliter |
| GM/ML    | Gram/milliliter                | MINIM    | Minim                |
| UNIT     | International unit             | MMOLE    | Millimole            |
| UNIT/ML  | International unit/ milliliter | MMOLE/ML | Millimole/milliliter |
| MCG      | Microgram                      | MU       | Million units        |
| MCG/ML   | Microgram/milliliter           | SQ CM    | Square centimeter    |
| MEQ      | Milliequivalent                | UNIT     | Unit                 |


Documentation Manual 4-17

Published: 11/11

Revised: 08/21

Data Elements


| Strength | Description                | Strength | Description     |
| -------- | -------------------------- | -------- | --------------- |
| MEQ/L    | Milliequivalent/liter      | UNIT/GM  | Unit/gram       |
| MEQ/ML   | Milliequivalent/milliliter | UNIT/ML  | Unit/milliliter |


Example:


| Drug Descriptor ID | Drug Name             | Route | Dosage Form | Strength | SUM    |
| ------------------ | --------------------- | ----- | ----------- | -------- | ------ |
| 001847             | Artificial Tears      | OP    | OINT        | &nbsp;   | &nbsp; |
| 023426             | vinCRISTine Sulfate   | IV    | SOLN        | 1        | MG/ML  |
| 032186             | Diltiazem HCI CR      | PO    | CP12        | 120      | MG     |
| 088732             | Vytorin               | PO    | TABS        | 10-10    | MG     |
| 089216             | HalfLytely Bowel Prep | PO    | KIT         | 5-210    | MG-GM  |


Note

- Due to the dynamic nature of these data, additional values may be added without notice.

# Bioequivalence Code

This is a 1-character field.

The Bioequivalence Code is a generalization of the Therapeutic Equivalence Evaluation (TEE) Code for products sharing a DDID. This code also indicates when the TEE Code cannot be generalized. For instance, the Bioequivalence Code will be set to "C" in this field

- if two different packaged drug products (different NDC-UPC-HRI codes but sharing the same DDID) have different TEE Codes (for example: “A1” and “A2”)
- when multiple TEE Codes exist for a DDID

Valid Values:


| Value | Description                             |
| ----- | --------------------------------------- |
| A     | Products in same GPI are equivalent     |
| B     | Products in same GPI are not equivalent |
| C     | Products may or may not be equivalent   |
| N     | Equivalency determination not available |
| U     | Undeterminable (obsolete)               |


4-18 MED-File v2

Published: 11/11

Revised: 08/21

Drug Name File

Note  
The "U" code is only applicable in previous versions of this file.

# Controlled Substance Code

This is a 1-character field.

The Controlled Substance Code identifies federally controlled substances, as classified by the Drug Enforcement Administration (DEA). The DEA Class Code [Data Element Code H020] is specific for an NDC-UPC-HRI. Here, the Controlled Substance Code is a general DEA Class Code for all products sharing a DDID and is determined by the DEA Class Code for the NDCs in the NDC File (MF2NDC). If more than one code is possible for a DDID, the value of "U" will appear in this field.

Valid Values:


| Value | Description                             | Definition                                                                                                                                                                                                                                                                       | Abbrev |
| ----- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 1     | No accepted medical use                 | High abuse potential; medical use not accepted (such as heroin, marijuana, and LSD)                                                                                                                                                                                              | C-I    |
| 2     | High abuse, severe dependence liability | High abuse potential with severe dependence liability (such as narcotics, amphetamines, and barbiturates)                                                                                                                                                                        | C-II   |
| 3     | Moderate dependence liability           | Less abuse potential than Schedule II drugs and moderate dependence liability (such as nonbarbiturate sedatives, nonamphetamine stimulants, and limited amounts of certain narcotics)                                                                                            | C-III  |
| 4     | Limited abuse potential                 | Less abuse potential than Schedule III drugs and limited dependence liability (such as some sedatives, antianxiety agents, and non-narcotic analgesics)                                                                                                                          | C-IV   |
| 5     | Limited abuse potential, small amounts  | Limited abuse potential; primarily small amounts of narcotics (codeine) used as antitussives or antidiarrheals; under federal law, limited quantities of certain C-V drugs may be purchased directly from a pharmacist without a prescription; can be either prescription or OTC | C-V    |
| b'    | DEA Class Code is not applicable        | A DEA Class Code is not applicable                                                                                                                                                                                                                                               | N/A    |
| U     | Undeterminable                          | A DEA Class Code is undeterminable                                                                                                                                                                                                                                               | Undet  |


Documentation Manual 4-19

Published: 11/11

Revised: 08/21

Data Elements

# Efficacy Code

This is a 1-character field.

The Efficacy Code identifies the stage of review for drugs pending final resolutions of efficacy by the FDA's Drug Efficacy Study Implementation (DESI) program. The DESI Code [Data Element Code H021] is specific for an NDC-UPC-HRI. Here, the Efficacy Code is a general DESI Code for all products sharing a DDID and is determined by the DESI Code for the NDCs in the NDC File (MF2NDC). If more than one code is possible for a DDID, the value of "U" will appear in this field.

According to the FDA, the following codes are valid. Additionally, Wolters Kluwer includes the value of “b” (blank) for non-drug and other non-applicable items.

Valid Values:


| Value | Description                              | Definition                                                               |
| ----- | ---------------------------------------- | ------------------------------------------------------------------------ |
| b     | Non-drug and other non-applicable items  | Non-drug and other non-applicable items                                  |
| 2     | Determined to be safe and effective      | Non-DESI/IRS drugs or DESI/IRS drugs determined to be safe and effective |
| 3     | Under review (NOOH has not been issued)  | DESI/IRS drugs under review (NOOH has not been issued)                   |
| 4     | Less than effective for some indications | LTE DESI/IRS drugs for some indications                                  |
| 5     | Less than effective for all indications  | LTE DESI/IRS drugs for all indications                                   |
| 6     | Less than effective, withdrawn           | LTE DESI/IRS drugs withdrawn from the market                             |
| U     | Undeterminable                           | An Efficacy Code is undeterminable                                       |


# Legend Indicator Code

This is a 1-character field.

The Legend Indicator Code indicates Federal Prescription (legend) or Over-the-Counter (OTC) (non-legend) status. If coded “R”, the item requires a prescription; if coded “O”, the item is an OTC product. The Legend Indicator Code is a general RX-OTC Indicator Code for all products sharing a DDID and is determined by the RX-OTC Indicator Code for NDCs in the NDC File (MF2NDC). If more than one code is possible for a DDID, the value of “U” will appear in this field.

4-20 MED-File v2

Published: 11/11

Revised: 08/21

Drug Name File

Valid Values:


| Value | Description                      |
| ----- | -------------------------------- |
| O     | OTC                              |
| R     | Rx                               |
| U     | Undeterminable (Both Rx and OTC) |


# Multi-Source Summary Code

This is a 1-character field.

The Multi-Source Summary Code identifies drug products as either single- or multiple-source original drug products or a generic copy of the standard drug product. This code is provided by Wolters Kluwer as a general guideline. The drug product price may be needed as a determining factor for generic substitution.

Valid Values:


| Value | Description                        | Definition                                                                                                    |
| ----- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| N     | Single-source product              | Single-source product available from one labeler.                                                             |
| M     | Single-source, co-licensed product | Product is co-licensed and considered a single-source product despite being available from multiple labelers. |
| O     | Multi-source, originator product   | Product available from multiple labelers considered to be the industry standard.                              |
| Y     | Multi-source product               | Multi-source product available from multiple labelers.                                                        |


Note

Products are designated "N" when the Multi-Source Code does not apply. For example, medical devices, partial GPIs, biologicals, and prenatal vitamins.

Example:


| Condition                                                     | N          | M                                                      | O      | Y      |
| ------------------------------------------------------------- | ---------- | ------------------------------------------------------ | ------ | ------ |
| Single-Source                                                 | Lantus Inj | -                                                      | -      | -      |
| Co-license                                                    | -          | Adderal XR Oral Capsule Extended Release 24 Hour 10 MG | &nbsp; | &nbsp; |
| AND                                                           | &nbsp;     | &nbsp;                                                 | &nbsp; | &nbsp; |
| Amphetamine-                                                  | &nbsp;     | &nbsp;                                                 | &nbsp; | &nbsp; |
| Dextroamphetamine Oral Capsule Extended Release 24 Hour 10 MG | -          | -                                                      | &nbsp; | &nbsp; |


Documentation Manual 4-21

Published: 11/11

Revised: 08/21

Data Elements


| Condition                           | N          | M      | O           | Y             |
| ----------------------------------- | ---------- | ------ | ----------- | ------------- |
| Original with Generics              | -          | -      | Valium 5 mg | diazePAM 5 mg |
| Former Co-licensing with Generics   | -          | -      | Septra DS   | &nbsp;        |
| Bactrim DS                          | SMZ/TMP DS | &nbsp; | &nbsp;      | &nbsp;        |
| Sulfameth oxazole/ Trimethop rim DS | &nbsp;     | &nbsp; | &nbsp;      | &nbsp;        |


# Brand Name Code

This is a 1-character field.

The Brand Name Code indicates the type of name used in the Drug Name [Data Element Code F007]. The Brand Name Code is a general Name Type Code for all products sharing a GPI. The value is determined by the Name Type Code [Data Element Code H073] values for the NDCs associated to the DDID.

Valid Values:


| Value | Description          |
| ----- | -------------------- |
| T     | Trademarked Name     |
| B     | Branded Generic Name |
| G     | Generic Name         |


Example:


| Trademarked Name (T)            | Branded Generic Name (B)                   | Generically Named (G)                              |
| ------------------------------- | ------------------------------------------ | -------------------------------------------------- |
| Esgic Oral Capsule 50-325-40 MG | Margesic Oral Capsule 50-325-40 MG         | Butalbital-APAP-Caffeine Oral Capsule 50-325-40 MG |
| Tylenol Oral Tablet 325 MG      | Non-Aspirin Pain Relief Oral Tablet 325 MG | Acetaminophen Oral Tablet 325 MG                   |
| Chlor-Trimeton Oral Tablet 4 MG | Aller-Chlor Oral Tablet 4 MG               | Chlorpheniramine Maleate Oral Tablet 4 MG          |


Note

In this context, the definition of a Branded Generic Name is a name accepted as an industry standard for a specific formulation used by more than one manufacturer/distributor. This name is also used by non-research and development (generic) manufacturers to represent their version of a generic product.

# Name Source Code

This is a 1-character field.

4-22 MED-File v2

Published: 11/11

Revised: 08/21

Drug Name File

The Name Source Code indicates if at least one NDC is marketed with this drug description or if a generic drug description has been created.

Valid Values:


| Value | Description                        |
| ----- | ---------------------------------- |
| P     | Product does exist in NDC File     |
| G     | Product does not exist in NDC File |
| S     | Name from Synonym                  |


Note  
The Value of "S" is not currently available.

Example:


| Drug Name      | Dosage Form | Name Source Code | Multi-Source Code | Brand Name Code |
| -------------- | ----------- | ---------------- | ----------------- | --------------- |
| Afinitor       | Tabs        | P                | N                 | T               |
| Everolimus     | Tabs        | G                | N                 | G               |
| Amoxicillin    | Caps        | P                | Y                 | G               |
| Mexiletine HCI | Caps        | P                | N                 | G               |


When generic-named drugs are initially introduced to the market, this value will change from a “G” to a “P”. When generic-named drugs are removed from the market, this value will change from a “P” to a “G”. To list all generic drug products, the search must find all “G” and “P” Name Source Codes.

Note  
The Name Source Code does not indicate the type of name. Refer to the Brand Name Code for this information. Generic drug product records can have a “G” or “P” Name Source Code.

## Generic Product Identifier

This is a 14-character field.

The Generic Product Identifier (GPI) categorizes drug products by a hierarchical therapeutic classification scheme. The GPI defines pharmaceutically equivalent drug products that are identical in:

- active ingredient(s)
- dosage form
- route
- strength or concentration

Documentation Manual 4-23

Published: 11/11

Revised: 08/21

Data Elements

The DDID for a brand name (for example, Lipitor Oral Tablet 10 MG), and the DDID for its corresponding generic name (for example, Atorvastatin Calcium Oral Tablet 10 MG) will be associated with the same GPI.

For more information, go to Chapter 2, "Editorial Policies".

## Knowledge Base Drug Code

This is a 10-digit numeric field.

The Knowledge Base Drug Code (KDC) is a proprietary Wolters Kluwer concept that defines a drug in terms of its ingredients. Single ingredient drugs (for example, acetaminophen) are assigned a KDC. Multiple ingredient drugs (for example, acetaminophen + hydrocodone) are assigned a KDC that represents the ingredient combination.


| Note | The KDC is not a hierarchical value and does not correlate to the GPI in any way. |
| ---- | --------------------------------------------------------------------------------- |


For more information, go to Retrieving KDCs for a Dispensable Drug in Chapter 5: Applications.

## New Drug Descriptor Identifier

This is a 6-digit numeric field.

The New Drug Descriptor Identifier allows tracking of changes to the DDID.


| Note | This field is only present for records with a Transaction CD of D. “D” is in an Incremental Update and is not present in a Total Database. |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Note | DDIDs that are removed from the Drug Name File will continue to appear in the Dispensable Drug File.                                       |
| ---  | ---                                                                                                                                        |


## Screenable Flag

This is a 1-character field.

The Screenable Flag is used to determine whether the drug name alone has a unique KDC and GPI.

4-24 MED-File v2

Published: 11/11

Revised: 08/21

Drug Name File

Valid Values:


| Value | Description                           |
| ----- | ------------------------------------- |
| Y     | Screenable by name alone              |
| N     | Product has multiple GPIs and/or KDCs |


The below conditions occur when one or both of the following exists when Screenable Flag is "N":

- The Generic Product Identifier [Data Element F075] is blank.
- The KDC Flag [Data Element Code F106] is "U".

# KDC Flag

This is a 1-character field.

The KDC Flag indicates KDC association to a drug product.

Valid Values:


| Value | Description                      |
| ----- | -------------------------------- |
| Y     | Drug product has a KDC           |
| N     | Drug product does not have a KDC |
| U     | Undetermined (under review)      |


# Local/Systemic Code

This is a 1-character field.

The Local/Systemic Code indicates if the drug product has a local or systemic effect. The value is generalized to represent all products sharing a DDID.

Valid Values:


| Code | Description    |
| ---- | -------------- |
| 0    | Undetermined   |
| 1    | Local          |
| 2    | Oral           |
| 3    | Parenteral     |
| 4    | Systemic       |
| 5    | Does Not Apply |


Documentation Manual 4-25

Published: 11/11

Revised: 08/21

Data Elements

# Maintenance Drug Code

This is a 1-character field.

The Maintenance Drug Code indicates whether or not the drug is considered a maintenance drug.

Valid Values:


| Value | Description            |
| ----- | ---------------------- |
| 0     | Undetermined           |
| 1     | Not a Maintenance Drug |
| 2     | Maintenance Drug       |


For more information, go to Chapter 2, "Maintenance Drug Code".

# Form Type Code

This is a 1-character field.

The Form Type Code indicates the form of the medication when administered to a patient. The form may be different at this stage than it is when packaged and sold by the manufacturer. The value is generalized to represent all products sharing a DDID.

The Valid Values and Examples are:


| Value | Description  | Example                            |
| ----- | ------------ | ---------------------------------- |
| 0     | Undetermined | &nbsp;                             |
| 1     | Gas          | NITROUS OXIDE (GAS)                |
| 2     | Liquid       | K-LYTE (EFFERVESCENT TABLETS)      |
| 3     | Other        | FLEET PREP KIT #2 (Bowel Prep kit) |
| 4     | Solid        | VICODIN (TABLETS)                  |


# Internal - External Code

This is a 1-character field.

The Internal-External Code complements the Route of Administration Code. The value is generalized to represent all products sharing a DDID.

4-26 MED-File v2

Published: 11/11

Revised: 08/21

Drug Name File

The Valid Values and Examples are:


| Value | Description                          | Example                 |
| ----- | ------------------------------------ | ----------------------- |
| 0     | Undetermined                         | &nbsp;                  |
| 1     | Combination of Internal and External | Dulcolax Bowel Prep Kit |
| 2     | Externally administered              | Diprolene Ointment      |
| 3     | Internally administered              | Crestor 10 MG Tablet    |
| 4     | Different than above                 | Clinitest Tablets       |


# Single - Combination Code

This is a 1-character field.

The Single-Combination Code distinguishes between products containing a single, active ingredient and a combination of two or more active ingredients. The value is generalized to represent all products sharing a DDID.

The Valid Values and Examples are:


| Value | Description  | Example                           |
| ----- | ------------ | --------------------------------- |
| 0     | Undetermined | Align (*Probiotic Product - Cap*) |
| 1     | Combination  | Vytorin (Ezetimibe-Simvastatin)   |
| 2     | Single       | Zetia (Ezetimibe)                 |


# Representative GPI Flag

This is a 1-character field.

The Representative GPI Flag indicates whether there is an exact match to a GPI or if multiple GPIs exist and a Representative GPI has been assigned.

Valid Values:


| Value | Description        |
| ----- | ------------------ |
| 0     | Unassigned         |
| 1     | Exact Match GPI    |
| 2     | Representative GPI |


# Representative KDC Flag

This is a 1-character field.

The Representative KDC Flag indicates whether there is an exact match to a KDC or if multiple KDCs exist and a Representative KDC has been assigned.

Documentation Manual 4-27

Published: 11/11

Revised: 08/21

Data Elements

Valid Values:


| Value | Description        |
| ----- | ------------------ |
| 0     | Unassigned         |
| 1     | Exact Match KDC    |
| 2     | Representative KDC |


## Reserve

This is a 6-character field.

The Reserve field is an unused field that may be used at a future date.

## Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note All Transaction CDs are blank for Total Databases.

## Last Change Date

This is an 8-digit numeric field.

In the Total database file and Incremental update file, the Last Change Date is the MED-File issue date regardless of Transaction Code value.

This date is in Gregorian format.

4-28 MED-File v2

Published: 11/11

Revised: 08/21

TC-GPI Name File

# TC-GPI Name File

(MF2TCGPI)

The TC-GPI Name File provides Wolters Kluwer's Therapeutic Classification System (TCS) hierarchy and names for each level of the hierarchy, including the GPI.

It may be appropriate in your application to separate Record Type Code 5 (GPI records) from the other Record Type Codes that represent the hierarchical system classification. This may provide efficiencies in storage or processing. Either way, to gain maximum benefit, all records and all fields, with the possible exception of the Transaction CD, should be stored in their entirety.

The TC-GPI Name File contains the following data elements:


| Code | Data Element Name | Record Position | Type/Length | Picture |
| ---- | ----------------- | --------------- | ----------- | ------- |
| G001 | TC-GPI Key        | 1-14            | C/14        | X(14)   |
| G015 | Record Type Code  | 15-15           | C/1         | X       |
| G016 | TC-GPI Name       | 16-75           | C/60        | X(60)   |
| G076 | TC Level Code     | 76-77           | C/2         | X(2)    |
| G078 | Reserve           | 78-87           | C/10        | X(10)   |
| G088 | Transaction CD    | 88-88           | C/1         | X       |
| G089 | Last Change Date  | 89-96           | N/8         | 9(8)    |


Note The shaded rows represent the unique key into the file.

# TC-GPI Key

This is a 14-character field.

The TC-GPI Key allows access to Wolters Kluwer's TCS. Record Types 0, 1, 2, 3, 6, and 4 are represented by a code of increasing specificity that is left-justified. Record Types of 7 are 12 characters long. Record Types of 5 are 14 characters long and are referred to as the Generic Product Identifier (GPI).

The GPI denotes pharmaceutically equivalent drug products. Products having the same 14-character GPI are identical with respect to active ingredient(s), dosage form, route, and strength or concentration. The GPI does not consider the presence of inactive ingredients. Each unique GPI corresponds to a descriptive GPI Generic Name (for example, 65991002050315, Acetaminophen w/ Codeine Tab 300-30 MG).

For more information, go to Chapter 2, "Editorial Policies".

Documentation Manual 4-29

Published: 11/11

Revised: 08/21

Data Elements

# Record Type Code

This is a 1-character field.

The Record Type Code indicates the level of the TC-GPI Name [Data Element Code G016]. When these Therapeutic Classification records are used in addition to the GPI Generic Name, the hierarchy within Wolters Kluwer's TCS is more apparent to the end-user.

Valid Values:


| Value | Description                            | TC Level Code | TC-GPI Key           |
| ----- | -------------------------------------- | ------------- | -------------------- |
| 0     | Therapeutic Class Range                | 00            | 00                   |
| 1     | Drug Group                             | 02            | 12                   |
| 2     | Drug Class                             | 04            | 12-34                |
| 3     | Drug Subclass                          | 06            | 12-34-56             |
| 6     | Drug Base Name                         | 08            | 12-34-56-78          |
| 4     | Drug Name/Drug Name Extension          | 10            | 12-34-56-78-90       |
| 7     | Drug Name and Dosage Form              | 12            | 12-34-56-78-90-12    |
| 5     | Full GPI with Drug Strength and Str UM | 14            | 12-34-56-78-90-12-34 |


# TC-GPI Name

This is a 60-character field.

The Therapeutic Classification-Generic Product Identifier (TC-GPI) file contains the textual descriptions for the various levels of the classification system.

Depending on implementation, it may be desirable to separate Record Type 5 from the other Record Types (to remove the hierarchical system classification records from the GPI records) to gain efficiencies in storage or processing.

# TC Level Code

This is a 2-character field.

4-30 MED-File v2

Published: 11/11

Revised: 08/21

TC-GPI Name File

The TC Level Code defines the level of the therapeutic classification hierarchy based on the number of significant characters that are defined.

Valid Values:


| Value | Description                            |
| ----- | -------------------------------------- |
| 00    | Therapeutic Class Range                |
| 02    | Drug Group                             |
| 04    | Drug Class                             |
| 06    | Drug Subclass                          |
| 08    | Drug Base Name                         |
| 10    | Drug Name/Drug Name Extension          |
| 12    | Drug Name and Dosage Form              |
| 14    | Full GPI with Drug Strength and Str UM |


## Reserve

This is a 10-character field.

The Reserve field is an unused field that may be used at a future date.

## Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

Valid Values:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note All Transaction CDs are blank for Total Database.

## Last Change Date

This is an 8-digit numeric field.

Documentation Manual 4-31

Published: 11/11

Revised: 08/21

Data Elements

For the Total database file, the Last Change Date is the MED-File issue date.

For the Incremental file, the Last Change Date depends upon the type of change, represented by the transaction code, as follows:


| Transaction Code | Last Change Date Representation                                       |
| ---------------- | --------------------------------------------------------------------- |
| Add              | MED-File issue date                                                   |
| Change           | MED-File issue date                                                   |
| Delete           | Previous MED-File issue date, dependent on frequency of file delivery |


This date is in Gregorian format.

# NDC File

(MF2NDC)

The NDC File contains specific information regarding distinct products in the marketplace which are identified by a National Drug Code (NDC). Drug products not identified by an NDC, are identified by Universal Product Codes (UPCs) or Health-Related Items (HRIs).

While the Drug Name File (MF2NAME) groups information and assigns certain attributes for multiple NDC-UPC-HRIs that share a single DDID, the NDC File assigns many of these attributes specific to the unique NDC-UPC-HRI. Use of the NDC File is warranted when the following occurs:

- Specificity at the NDC-UPC-HRI level is needed for certain attributes such as the following:  
> TEE Code  
> DEA Class Code  
> DESI Code  
> RX-OTC Indicator Code  
> Multi-Source Code  
> Name Type Code
- Additional attributes not found in the Drug Name File are needed such as the following:  
> Innerpack Code  
> Storage Condition Code  
> Limited Distribution Code
- Use of drug pricing is planned in your application
- Information on market availability of drug products (inactive/active status) tied to a system involving reimbursement or claims is needed for submission

4-32 MED-File v2

Published: 11/11

Revised: 08/21

NDC File

- When precise documentation of an NDC is essential, and there is no GPI or KDC information in the Drug Name File, and clinical screening is required

The NDC File contains the following data elements:


| Code | Data Element Name              | Record Position | Type/Length | Picture  |
| ---- | ------------------------------ | --------------- | ----------- | -------- |
| H001 | NDC-UPC-HRI                    | 1-11            | C/11        | X(11)    |
| H012 | Drug Descriptor Identifier     | 12-17           | N/6         | 9(6)     |
| H018 | TEE Code                       | 18-19           | C/2         | X(2)     |
| H020 | DEA Class Code                 | 20-20           | C/1         | X        |
| H021 | DESI Code                      | 21-21           | C/1         | X        |
| H022 | RX-OTC Indicator Code          | 22-22           | C/1         | X        |
| H023 | Generic Product Packaging Code | 23-30           | C/8         | X(8)     |
| H031 | Old NDC-UPC-HRI                | 31-41           | C/11        | X(11)    |
| H042 | New NDC-UPC-HRI                | 42-52           | C/11        | X(11)    |
| H053 | Repackage Code                 | 53-53           | C/1         | X        |
| H054 | ID Number Format Code          | 54-54           | C/1         | X        |
| H055 | Third-Party Restriction Code   | 55-55           | C/1         | X        |
| H056 | Knowledge Base Drug Code       | 56-65           | N/10        | 9(10)    |
| H066 | KDC Flag                       | 66-66           | C/1         | X        |
| H067 | Medi-Span Labeler Identifier   | 67-71           | N/5         | 9(5)     |
| H072 | Multi-Source Code              | 72-72           | C/1         | X        |
| H073 | Name Type Code                 | 73-73           | C/1         | X        |
| H074 | Item Status Flag               | 74-74           | C/1         | X        |
| H075 | Innerpack Code                 | 75-75           | C/1         | X        |
| H076 | Clinic Pack Code               | 76-76           | C/1         | X        |
| H077 | Reserve-1                      | 77-78           | C/2         | X(2)     |
| H079 | PPG Indicator Code             | 79-79           | C/1         | X        |
| H080 | HFPG Indicator Code            | 80-80           | C/1         | X        |
| H081 | Dispensing Unit Code           | 81-81           | C/1         | X        |
| H082 | Dollar Rank Code               | 82-82           | C/1         | X        |
| H083 | Rx Rank Code                   | 83-83           | C/1         | X        |
| H084 | Storage Condition Code         | 84-84           | C/1         | X        |
| H085 | Limited Distribution Code      | 85-86           | C/2         | X(2)     |
| H087 | Old Effective Date             | 87-94           | N/8         | YYYYMMDD |
| H095 | New Effective Date             | 95-102          | N/8         | YYYYMMDD |


Documentation Manual 4-33

Published: 11/11

Revised: 08/21

Data Elements


| Code | Data Element Name              | Record Position | Type/Length | Picture |
| ---- | ------------------------------ | --------------- | ----------- | ------- |
| H103 | Next-Smaller NDC Suffix Number | 103-104         | C/2         | X(2)    |
| H105 | Next-Larger NDC Suffix Number  | 105-106         | C/2         | X(2)    |
| H107 | Reserve-2                      | 107-119         | C/13        | X(13)   |
| H120 | Transaction CD                 | 120-120         | C/1         | X       |
| H121 | Last Change Date               | 121-128         | N/8         | 9(8)    |


Note  
The shaded row represents the unique key into the file.

# NDC-UPC-HRI

This is an 11-character field.

NDCs, UPCs, and HRIs are 10-character codes used to identify drug products. Surgical supplies and non-prescription drug products may have an NDC and an HRI or UPC according to the standards set forth by the Uniform Product Code Council, Inc. These codes are converted to eleven characters according to NCPDP standards.

For more information regarding the NDC-UPC-HRI, go to Chapter 2, "NDC-UPC-HRI".

For more information regarding formatting of the NDC-UPC-HRI, see ID Number Format Code.

# Drug Descriptor Identifier

This is a 6-digit numeric field.

The Drug Descriptor Identifier (DDID) is six digits identifying a unique combination of Drug Name, Route, Dosage Form, Strength, and Strength Unit of Measure. The value of the identifier itself has no meaning. It is used to identify a unique product with respect to these fields alone. It does not distinguish products by Package Size, TEE Code, DESI Code, DEA Class Code, Brand Name Code, or various other attributes.

4-34 MED-File v2

Published: 11/11

Revised: 08/21

NDC File

Example:


| Drug Descriptor ID | Drug Name             | Route | Dosage Form | Strength | SUM    |
| ------------------ | --------------------- | ----- | ----------- | -------- | ------ |
| 001847             | Artificial Tears      | OP    | OINT        | &nbsp;   | &nbsp; |
| 023426             | vinCRIStine Sulfate   | IV    | SOLN        | 1        | MG/ML  |
| 032186             | Diltiazem HCl CR      | PO    | CP12        | 120      | MG     |
| 088732             | Vytorin               | PO    | TABS        | 10-10    | MG     |
| 089216             | HalfLytely Bowel Prep | PO    | KIT         | 5-210    | MG-GM  |


## TEE Code

This is a 2-character field.

The Therapeutic Equivalence Evaluation (TEE) Code is a two-character code indicating the FDA rating of the therapeutic equivalence of a drug product with other pharmaceutically equivalent drug products, as published in the Orange Book. This code is used in conjunction with the Generic Product Identifier [Data Element Code F075]. The GPI groups pharmaceutically equivalent drug products, and, in that context, the TEE Code is meaningful.

**Note**

TEE Codes beginning with "A" (except values of "A1", "A2", "A3" and "A4") indicate drug products that are therapeutically equivalent to other pharmaceutically equivalent products. Products with an "A" TEE Code are generally considered interchangeable with pharmaceutically equivalent drug products, subject to individual state regulations governing product substitution. In the exception noted above, the full two-character TEE Code is necessary to find therapeutically equivalent drugs (such as when comparing a GPI category containing both "A1", "A2", "A3" and "A4" ratings).

Valid Values:


| Code | Description                   | Definition                                                              |
| ---- | ----------------------------- | ----------------------------------------------------------------------- |
| AA   | No Bioequivalence Problems    | Products having no bioequivalence problems in conventional dosage forms |
| AB   | Bioequivalence Resolved       | Products meeting necessary bioequivalence requirements                  |
| AN   | Soln/Powd Aerosol - OK        | Solutions and powders for aerosolization                                |
| AO   | Injectable Oil Solutions - OK | Injectable oil solutions (same concentration and vehicle)               |


Documentation Manual 4-35

Published: 11/11

Revised: 08/21

Data Elements


| Code | Description                    | Definition                                                                                                                                       |
| ---- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| AP   | Injectable H2O Solutions - OK  | Injectable aqueous solutions                                                                                                                     |
| AT   | Topical products - OK          | Topical products                                                                                                                                 |
| A1   | Bioequivalence Resolved        | Equivalent to Orange Book value of “AB1”. Products with this code are only equivalent to other products with the same GPI and the same TEE Code. |
| A2   | Bioequivalence Resolved        | Equivalent to Orange Book value of “AB2”. Products with this code are only equivalent to other products with the same GPI and the same TEE Code. |
| A3   | Bioequivalence Resolved        | Equivalent to Orange Book value of “AB3”. Products with this code are only equivalent to other products with the same GPI and the same TEE Code. |
| A4   | Bioequivalence Resolved        | Equivalent to Orange Book value of “AB4”. Products with this code are only equivalent to other products with the same GPI and the same TEE Code. |
| BC   | CRTB/CRCP/CR - INJS Problems   | Controlled-release dosage forms                                                                                                                  |
| BD   | AI or DF Documented Problems   | Ingredients and dosage forms with documented bioequivalence problems                                                                             |
| BE   | ECTB Oral Problems             | Enteric-coated oral dosage forms                                                                                                                 |
| BN   | Aerosol - Nebulizer Problems   | Products in aerosol-nebulizer drug delivery systems                                                                                              |
| BP   | AI or DF Potential Problems    | Active ingredients and dosage forms with potential bioequivalence problems (for example, injectable suspensions)                                 |
| BR   | Supp/Enem Systemic Problems    | Suppositories or enemas for systemic use                                                                                                         |
| BS   | Drug Standard Problems         | Products having drug standard deficiencies                                                                                                       |
| BT   | Topical Problems               | Topical products with bioequivalence issues                                                                                                      |
| BX   | Insufficient Data              | Drug products for which data are insufficient to determine therapeutic equivalence                                                               |
| B*   | Requires Further Investigation | Products requiring further FDA investigation to determine therapeutic equivalence                                                                |
| NA   | Not Available                  | Information is not available                                                                                                                     |
| NR   | Not Rated                      | Drug product has not yet been rated                                                                                                              |


## DEA Class Code

This is a 1-character field.

The DEA Class Code identifies federally controlled substances classified by the Drug Enforcement Administration (DEA).

4-36 MED-File v2

Published: 11/11

Revised: 08/21

NDC File

Valid Values:


| Value | Description                             | Definition                                                                                                                                                                                                                                                                                   | Abbreviation |
| ----- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| 1     | No accepted medical use                 | Schedule I: High abuse potential; medical use not accepted (such as heroin, marijuana, and LSD)                                                                                                                                                                                              | C-I          |
| 2     | High abuse, severe dependence liability | Schedule II: High abuse potential with severe dependence liability (such as narcotics, amphetamines, and barbiturates)                                                                                                                                                                       | C-II         |
| 3     | Moderate dependence liability           | Schedule III: Less abuse potential than Schedule II drugs and moderate dependence liability (such as nonbarbiturate sedatives, nonamphetamine stimulants, anabolic steroids, and limited amounts of certain narcotics)                                                                       | C-III        |
| 4     | Limited abuse potential                 | Schedule IV: Less abuse potential than Schedule III drugs and limited dependence liability (such as some sedatives, anti-anxiety agents, and non-narcotic analgesics)                                                                                                                        | C-IV         |
| 5     | Limited abuse potential, small amounts  | Schedule V: Limited abuse potential; primarily small amounts of narcotics (codeine) used as antitussives or antidiarrheals; under federal law, limited quantities of certain C-V drugs may be purchased directly from a pharmacist without a prescription; can be either prescription or OTC | C-V          |
| b'    | DEA Class Code is not applicable        | A DEA Class Code is not applicable                                                                                                                                                                                                                                                           | &nbsp;       |


For more information, go to Chapter 2, "DEA Class Code".

Documentation Manual 4-37

Published: 11/11

Revised: 08/21

Data Elements

# DESI Code

This is a 1-character field.

The DESI Code identifies the stage of review for drugs pending final resolutions of efficacy by the FDA's Drug Efficacy Study Implementation (DESI) program.

"IRS" refers to drugs that are identical, related, or similar to current DESI drugs. "NOOH" refers to Notice of Opportunity for a Hearing, which is published in the Federal Register.

According to the FDA, the following codes are valid. Additionally, Wolters Kluwer includes the value of “b” (blank) for non-drug and other non-applicable drug products.


| Value | Description                              | Definition                                                         |
| ----- | ---------------------------------------- | ------------------------------------------------------------------ |
| b'    | Non-drug and other non-applicable items  | Non-drug and other non-applicable items                            |
| 2     | Determined to be safe and effective      | Non-DESI/IRS drugs or DESI/IRS drugs determined safe and effective |
| 3     | Under review (NOOH has not been issued)  | DESI/IRS drugs under review (NOOH has not been issued)             |
| 4     | Less than effective for some indications | LTE DESI/IRS drugs for some indications                            |
| 5     | Less than effective for all indications  | LTE DESI/IRS drugs for all indications                             |
| 6     | Less than effective, withdrawn           | LTE DESI/IRS drugs withdrawn from the market                       |


For more information, go to Chapter 2, "DESI Code".

# RX-OTC Indicator Code

This is a 1-character field.

The RX-OTC Indicator Code indicates federal prescription (Rx) or Over-the-Counter (OTC) status. If coded “R” or “S”, the drug product requires a prescription; if coded “O” or “P”, the drug product is an OTC product and does not require a prescription. The “S” and “P” codes also indicate the drug product is available from more than one manufacturer.

4-38 MED-File v2

Published: 11/11

Revised: 08/21

NDC File

Valid Values:


| Value | Description           |
| ----- | --------------------- |
| O     | OTC (single source)   |
| P     | OTC (multiple source) |
| R     | Rx (single source)    |
| S     | Rx (multiple source)  |


The RX-OTC Indicator Code is coded in conjunction with the Multi-Source Code [Data Element Code H072] as follows:


| Value | Description Using Multisource Codes                      |
| ----- | -------------------------------------------------------- |
| O     | OTC product with a Multi-Source Code of “N”              |
| P     | OTC product with a Multi-Source Code of “O”, “M”, or “Y” |
| R     | Rx product with a Multi-Source Code of “N”               |
| S     | Rx product with a Multi-Source Code of “O”, “M”, or “Y”  |


## Generic Product Packaging Code

This is a 8-character field.

The Generic Product Packaging Code (GPPC) identifies unique combinations of the following fields:


| Data Element Name                  | Data Element Code |
| ---------------------------------- | ----------------- |
| Generic Product Identifier         | J028              |
| Package Description Code           | J026              |
| Package Size                       | J009              |
| Package Size Unit of Measure       | J018              |
| Package Quantity                   | J020              |
| Unit-Dose/Unit-of-Use Package Code | J025              |


For more information, go to Chapter 2, "Generic Product Packaging Code".

## Old NDC-UPC-HRI

This is an 11-character field.

When the NDC-UPC-HRI for a product changes, the following occurs:

- Two records are output at the time of the change
- The old NDC-UPC-HRI record will include an Item Status Flag of “I” to indicate the NDC-UPC-HRI is now inactive

Documentation Manual 4-39

Published: 11/11

Revised: 08/21

Data Elements

- A new NDC-UPC-HRI record will be output with a Transaction CD of “A” to indicate the record is a new addition to the file
- The old NDC-UPC-HRI value will be included in the Old NDC-UPC-HRI field of the new record

# New NDC-UPC-HRI

This is an 11-character field.

When the NDC-UPC-HRI for a product changes, the following occurs:

- Two records are output at the time of the change
- The new NDC-UPC-HRI record will be output with a Transaction CD of “A” to indicate the record is a new addition to the file
- The old NDC-UPC-HRI record will include an Item Status Flag of “I” to indicate the NDC-UPC-HRI is now inactive
- The new NDC-UPC-HRI value will be included in the New NDC-UPC-HRI field of the old record

# Repackage Code

This is a 1-character field.

The Repackage Code identifies products that have been repackaged for use by:

- mail order suppliers
- home health care agencies
- nursing homes
- physicians
- others

Repackaged products include both brand name and generic drug products.

Valid Values:


| Code | Description        |
| ---- | ------------------ |
| X    | Repackaged Product |
| b    | Not Repackaged     |


# ID Number Format Code

This is a 1-character field.

4-40 MED-File v2

Published: 11/11

Revised: 08/21

NDC File

The ID Number Format Code identifies the format of the NDC-UPC-HRI [Data Element Code H001, H031, and H042]. Use the ID Number Format Code with an NDC, UPC, or HRI to determine

- where to place dashes when formatting for display
- how to convert from the 10- to 11-digit format
- how to convert from the 11- to 10-digit format

Valid Values:


| Value | Represents | ID Type    |
| ----- | ---------- | ---------- |
| 1     | 4-4-2      | NDC        |
| 2     | 5-3-2      | NDC        |
| 3     | 5-4-1      | NDC        |
| 4     | 4-6        | HRI        |
| 5     | 5-5        | UPC or HRI |
| 6     | 5-4-2      | NDC        |


The codes convert as follows:


| NDC                  | &nbsp;      | NCPDP Standard 11-character NDC | 11-character NDC (with hyphens) | ID Format Code |
| -------------------- | ----------- | ------------------------------- | ------------------------------- | -------------- |
| 4-4-2 (9999-9999-99) | Converts To | 5-4-2 (09999999999)             | 09999-9999-99                   | 1              |
| 5-3-2 (99999-999-99) | &nbsp;      | 5-4-2 (99999099999)             | 99999-0999-99                   | 2              |
| 5-4-1 (99999-9999-9) | &nbsp;      | 5-4-2 (99999999909)             | 99999-9999-09                   | 3              |
| 5-4-2 (99999-9999-99 | &nbsp;      | 5-4-2 (99999999999)             | 99999-9999-99                   | 6              |
| 4-6 (9999-999999)    | &nbsp;      | 5-6 (09999999999)               | 9999-999999                     | 4              |
| 5-5 (99999-99999)    | &nbsp;      | 5-6 (99999099999)               | 99999-99999                     | 5              |


# Third-Party Restriction Code

This is a 1-character field.

The Third-Party Restriction Code can be used by Third Party Administrators (TPAs) for identifying drug products for formulary exclusion (such as oral contraceptives) or inclusion (for example, vitamins).

Documentation Manual 4-41

Published: 11/11

Revised: 08/21

Data Elements

# Knowledge Base Drug Code

This is a 10-digit numeric field.

The Knowledge Base Drug Code (KDC) is a concept used by Wolters Kluwer that defines a drug in terms of its ingredients. Single ingredient drugs (for example, acetaminophen) are assigned a KDC. Multiple ingredient drugs (for example, acetaminophen + hydrocodone) are assigned a KDC that represents the ingredient combination.

When a KDC Flag [Data Element Code H066] is "N" or "U", the KDC will be zero-filled in this field.

Note  
The KDC is not a hierarchical value and does not correlate to the GPI in any way.

For more information, go to Chapter 2, "Knowledge Base Drug Code".

# KDC Flag

This is a 1-character field.

The KDC Flag indicates KDC association to a drug product.

Valid Values:


| Value | Description                      |
| ----- | -------------------------------- |
| Y     | Drug product has a KDC           |
| N     | Drug product does not have a KDC |
| U     | Undetermined (under review)      |


# Medi-Span Labeler Identifier

This is a 5-digit numeric field.

The Medi-Span Labeler Identifier links the drug product to its manufacturer or distributor. Most Medi-Span Labeler Identifiers are derived from the labeler code segment of the NDC-UPC-HRI. However, in some cases, the Medi-Span Labeler Identifier differs from the labeler code segment of the NDC-UPC-HRI, so that the accurate division name within the manufacturer or distributor can be associated with the drug product.

For more information, go to Chapter 2, "Medi-Span Labeler Identifier".

4-42 MED-File v2

Published: 11/11

Revised: 08/21

NDC File

# Multi-Source Code

This is a 1-character field.

The Multi-Source Code identifies drug products as either single- or multiple-source original drug products or a generic copy of the standard drug product. This code is provided by Wolters Kluwer as a general guideline. Drug product price may be needed as a determining factor for generic substitution.

Valid Values:


| Value | Description                        | Definition                                                                                                    |
| ----- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| N     | Single-source product              | Single-source product available from one labeler.                                                             |
| M     | Single-source, co-licensed product | Product is co-licensed and considered a single-source product despite being available from multiple labelers. |
| O     | Multi-source, originator product   | Product available from multiple labelers considered to be the industry standard.                              |
| Y     | Multi-source product               | Multi-source product available from multiple labelers.                                                        |


Note

Products are designated "N" when the Multi-Source Code does not apply. For example, medical devices, partial GPIs, biologicals, and prenatal vitamins.

Example:


| Condition     | N          | M                                                                                                                                    | O   | Y   |
| ------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------ | --- | --- |
| Single-Source | Lantus Inj | -                                                                                                                                    | -   | -   |
| Co-licensed   | -          | Adderal XR Oral Capsule Extended Release 24 Hour 10 MG AND Amphetamine-Dextroamphetamine Oral Capsule Extended Release 24 Hour 10 MG | -   | -   |


Documentation Manual 4-43

Published: 11/11

Revised: 08/21

Data Elements


| Condition                         | N   | M   | O                    | Y                                             |
| --------------------------------- | --- | --- | -------------------- | --------------------------------------------- |
| Original with Generics            | -   | -   | Valium 5 mg          | diazePAM 5 mg                                 |
| Former Co-licensing with Generics | -   | -   | Septra DS Bactrim DS | SMZ/TMP DS Sulfamethox-azole/ Trimethoprim DS |


Note  
These codes are subject to change as more information is made available to Wolters Kluwer.

# Name Type Code

This is a 1-character field.

The Name Type Code indicates the type of name used in the Drug Name [Data Element Code F007].

Valid Values:


| Value | Description          |
| ----- | -------------------- |
| G     | Generic Name         |
| T     | Trademarked Name     |
| B     | Branded Generic Name |


Example:


| Trademarked Name (T)            | Branded Generic Name (B)                   | Generically Named (G)                              |
| ------------------------------- | ------------------------------------------ | -------------------------------------------------- |
| Esgic Oral Capsule 50-325-40 MG | Margesic Oral Capsule 50-325-40 MG         | Butalbital-APAP-Caffeine Oral Capsule 50-325-40 MG |
| Tylenol Oral Tablet 325 MG      | Non-aspirin Pain Relief Oral Tablet 325 MG | Acetaminophen Oral Tablet 325 MG                   |
| Chlor-Trimeton Oral Tablet 4 MG | Aller-Chlor Oral Tablet 4 MG               | Chlorpheniramine Maleate Oral Tablet 4 MG          |


# Item Status Flag

This is a 1-character field.

The Item Status Flag distinguishes between active and inactive NDCs and allows the Transaction CD to clearly reflect the add, change, and delete status of the record.

4-44 MED-File v2

Published: 11/11

Revised: 08/21

NDC File

Additionally, drug products inactive for greater than 48 months do not appear in the Total Database and are output in the Incremental Updates (one time only) with a “D” Transaction CD and a “Z” Item Status Flag. These records can be stored in your historical files.

The "O" Item Status Flag is used when a manufacturer reuses an old NDC-UPC-HRI for a different drug product. The new product has an "O" Item Status Flag to distinguish it from other newly added drug products. These products should not replace the old inactive products without review because dispensing errors could result.

"O" Item Status Flags in Total Database should be treated as "A" Transaction Codes if the drug product does not exist in the end-user's drug files or patient profiles. However, if the end-user already has information on this NDC-UPC-HRI, the information should be reviewed before changing any field in the end-user's system.

Valid Values:


| Value | Description                     |
| ----- | ------------------------------- |
| A     | Active                          |
| I     | Inactive                        |
| O     | Override                        |
| Z     | Inactive Greater than 48 Months |


## Innerpack Code

This is a 1-character field.

The Innerpack Code identifies the NDC that appears on items contained within a large carton. These innerpack NDCs differ slightly from the carton NDC and may not be sold separately by the manufacturer. However, they may be sold individually by the wholesaler. Their prices are calculated from the carton NDC and are updated when a price change occurs to the carton NDC.

Valid Values:


| Value | Description | Definition                                       |
| ----- | ----------- | ------------------------------------------------ |
| Y     | Yes         | Item is an innerpack and is not sold separately. |
| N     | No          | Item is not an innerpack.                        |


## Clinic Pack Code

This is a 1-character field.

Documentation Manual 4-45  
Published: 11/11  
Revised: 08/21

Data Elements

The Clinic Pack Code identifies drug products distributed to patients as samples (such as "clinic packs" and "institutional packs") by hospitals, clinics, manufacturers, and physicians.

Clinic packs generally have no price associated with them.

Valid Values:


| Value | Description | Definition                 |
| ----- | ----------- | -------------------------- |
| Y     | Yes         | Item is a clinic pack.     |
| N     | No          | Item is not a clinic pack. |


# Reserve-1

This is a 2-character field.

The Reserve-1 field is an unused field that may be used at a future date.

# PPG Indicator Code

This is a 1-character field.

The PPG Indicator Code identifies approximately 5,000 of the most commonly stocked prescription drug products in the retail pharmacy environment.

Valid Values:


| Value | Description             |
| ----- | ----------------------- |
| Y     | Included in the PPG     |
| b     | Not included in the PPG |


# HFPG Indicator Code

This is a 1-character field.

The HFPG Indicator Code contains all drug products identified with a PPG Indicator Code of "Y", in addition to unit-dose and injectables needed by hospitals and extended-care facilities - approximately 10,000 drug products.

Valid Values:


| Value | Description              |
| ----- | ------------------------ |
| Y     | Included in the HFPG     |
| b     | Not included in the HFPG |


4-46 MED-File v2

Published: 11/11

Revised: 08/21

NDC File

# Dispensing Unit Code

This is a 1-character field.

The Dispensing Unit Code indicates whether the NDC-UPC-HRI represents the usual dispensing sizes for tablets, capsules, and liquids.

Valid Values:


| Value | Description                      |
| ----- | -------------------------------- |
| U     | Usual Dispensing Size            |
| b     | Other Than Usual Dispensing Size |


Wolters Kluwer uses the following packages for dispensing sizes for tablets, capsules, and liquids only:


| Dosage Form          | Package Size  | Dispensing Unit Code |
| -------------------- | ------------- | -------------------- |
| Tablets and Capsules | 100           | U                    |
| Liquids              | 480 ml (pint) | U                    |


Note Normal dispensing size for liquids is 480 ml. Pints that only contain 473 ml are not coded with a Dispensing Unit Code of U.

# Dollar Rank Code

This is a 1-character field.

The Dollar Rank Code indicates the drug product's annual industry dollar sales rank according to independent research audits.

Valid Values:


| Value | Description                |
| ----- | -------------------------- |
| 0     | Not Ranked                 |
| 1     | Ranked between 1 and 100   |
| 2     | Ranked between 101 and 200 |
| 3     | Ranked between 201 and 300 |
| 4     | Ranked between 301 and 400 |
| 5     | Ranked between 401 and 500 |


Documentation Manual 4-47

Published: 11/11

Revised: 08/21

Data Elements

A Dollar Rank Code exists for the Top 500 drug products at the NDC-UPC-HRI level. Therefore, it is possible for similar products with different strengths or package sizes to have different Dollar Rank Codes.

# Rx Rank Code

This is a 1-character field.

The Rx Rank Code indicates the prescription-velocity rank according to independent research audits. These audits review annual industry prescription volumes.

Valid Values:


| Value | Description                |
| ----- | -------------------------- |
| 0     | Not Ranked                 |
| 1     | Ranked between 1 and 100   |
| 2     | Ranked between 101 and 200 |
| 3     | Ranked between 201 and 300 |
| 4     | Ranked between 301 and 400 |
| 5     | Ranked between 401 and 500 |


An Rx Rank Code exists for the Top 500 drug products at the NDC-UPC-HRI level. Therefore, it is possible for similar products with different strengths or package sizes to have different Rx Rank codes.

# Storage Condition Code

This is a 1-character field.

The Storage Condition Code indicates the conditions under which a drug must be stored, prior to dispensing, as represented by the values and definitions below. Codes are written to accommodate generally defined temperature ranges, therefore it is important to consult and follow manufacturers' recommended storage conditions for individual products; manufacturers' recommendations may differ from the Storage Condition Code by either allowing temperatures outside of the range or by not allowing temperatures within the entire range represented within the Storage Condition Code.

4-48 MED-File v2

Published: 11/11

Revised: 08/21

NDC File

Valid Values:


| Value                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                         | Definition                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Normal (room temperature)                                                                                                                           | For products that are intended to be stored at room temperature, with margins allowed for excursions. The temperatures are generally within the 15° to 30°C (59° to 86°F) range. |
| R                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Refrigerated                                                                                                                                        | For products intended to be stored in a refrigerator, generally defined as temperatures between 2° to 8°C (36° to 46°F).                                                         |
| F                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Frozen                                                                                                                                              | For products intended to be stored in a freezer, generally defined as temperatures between -25° to -15°C (-13° to 5°F).                                                          |
| D                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Deep-Frozen*                                                                                                                                        | &nbsp;                                                                                                                                                                           |
| *Deep-Frozen is not a standardized term within the drug industry. Medi-Span’s generalized usage of the term is intended to represent a product’s storage requirement in temperatures colder than Medi-Span’s Frozen code.                                                                                                                                                                                                                              | For products that are intended to be stored at temperatures near or below -25°C, likely requiring special ultra-low or cryogenic storage equipment. | &nbsp;                                                                                                                                                                           |
| For the sake of extra caution, products which have temperature requirements accompanied with a “less than” (<) or a “less than or equal to” (≤) qualifier that suggests an upper limit that would not be covered within the entire temperature range of the Frozen code will be assigned a Deep-Frozen storage condition code. For example, products with storage temperatures of <-18°C, ≤-18°C, <-20°C, or ≤-20°C will receive the Deep-Frozen code. | &nbsp;                                                                                                                                              | &nbsp;                                                                                                                                                                           |
| b'                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Not Available                                                                                                                                       | &nbsp;                                                                                                                                                                           |


Note  
Drug products subject to reconstitution, such as Amoxicillin and Clavulanate Potassium Powder for Suspension, are coded with the Storage Condition Code N, which represents normal pre-reconstitution storage condition. The end-user would inform the patient of the refrigeration requirements after reconstitution.

## Limited Distribution Code

The Limited Distribution Code is used to denote if there are restricted distributions for a product. For example, this code denotes a private labeler, availability restricted to one region, and so on.

Documentation Manual 4-49  
Published: 11/11  
Revised: 08/21

Data Elements

Valid Values:


| Value | Definition                    |
| ----- | ----------------------------- |
| 00    | NOT APPLICABLE                |
| 01    | PRIVATE LABELER               |
| 02    | AVAILABLE IN PUERTO RICO ONLY |
| 03    | COMPOUNDING LABELER           |


Note  
Additional values may be added in the future.

## Old Effective Date

This is an 8-digit numeric field.

The Old Effective Date is associated to the Old NDC-UPC-HRI and represents its inactive date. The date is populated in the new NDC-UPC-HRI when the Old NDC-UPC-HRI is populated.

The date is in Julian format.

Note  
This field is blank when no data is present.

## New Effective Date

This is an 8-digit numeric field.

The New Effective Date is associated to the New NDC-UPC-HRI and represents the effective date for the new NDC-UPC-HRI. The date is populated in the old NDC-UPC-HRI record when the New NDC-UPC-HRI field is populated.

In some instances, the New NDC-UPC-HRI is replacing an old NDC-UPC-HRI that is replacing an even older NDC-UPC-HRI, all within the same MED-File v2 update. The New Effective Date is associated to the New NDC-UPC-HRI and represents the effective date for the new NDC-UPC-HRI. The date is populated in the old NDC-UPC-HRI record when the New NDC-UPC-HRI field is populated. In addition, the New Effective Date field is populated in the older NDC-UPC-HRI record to reflect the effective date for the old NDC-UPC-HRI, even though the old NDC-UPC-HRI was replaced with the New NDC-UPC-HRI.

The date is in Julian format.

4-50 MED-File v2  
Published: 11/11  
Revised: 08/21

NDC File

Note  
This field is blank when no data is present.

# Next-Smaller NDC Suffix Number

This is a 2-character field.

When available, the Next-Smaller NDC Suffix Number identifies the last one or two-digit suffix for the next smaller size of a drug product. This field is used for products identified by an NDC. UPCs, HRIs, innerpacks, clinic packs, and unit-dose items are not considered.

Example


| Drug Name        | NDC           | Next-Smaller NDC Suffix Number |
| ---------------- | ------------- | ------------------------------ |
| Nexium 20 mg 90s | 00186-5020-54 | 31                             |
| Nexium 20 mg 30s | 00186-5020-31 | &nbsp;                         |


# Next-Larger NDC Suffix Number

This is a 2-character field.

When available, the Next-Larger NDC Suffix Number identifies the last one or two-digit suffix for the next larger size of a drug product. This field is used for products identified by an NDC. UPCs, HRIs, clinic packs, innerpacks, and unit-dose items are not considered.

Example


| Drug Name        | NDC           | Next-Larger NDC Suffix Number |
| ---------------- | ------------- | ----------------------------- |
| Nexium 20 mg 90s | 00186-5020-54 | &nbsp;                        |
| Nexium 20 mg 30s | 00186-5020-31 | 54                            |


# Reserve-2

This is a 13-character field.

The Reserve-2 field is an unused field that may be used at a future date.

# Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

Documentation Manual 4-51

Published: 11/11

Revised: 08/21

Data Elements

Valid Values:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note  
All Transaction CDs are blank for Total Database.

## Last Change Date

This is an 8-digit numeric field.

In the Total database file and Incremental update file, the Last Change Date is the MED-File issue date regardless of Transaction Code value.

This date is in Gregorian format.

## Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

Valid Values:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note  
All Transaction CDs are blank for Total Database.

## Labeler File

(MF2LAB)

The Labeler File provides a textual description for the Medi-Span Labeler Identifier.

4-52 MED-File v2

Published: 11/11

Revised: 08/21

Labeler File

The Labeler File contains the following data elements:


| Code | Data Element Name               | Record Position | Type/Length | Picture |
| ---- | ------------------------------- | --------------- | ----------- | ------- |
| I001 | Medi-Span Labeler Identifier    | 1-5             | N/5         | 9(5)    |
| I006 | Manufacturer's (Labeler) Name   | 6-35            | C/30        | X(30)   |
| I036 | Manufacturer's Abbreviated Name | 36-45           | C/10        | X(10)   |
| I046 | Labeler Type Code               | 46-46           | C/1         | X       |
| I047 | Reserve                         | 47-55           | C/9         | X(9)    |
| I056 | Transaction CD                  | 56-56           | C/1         | X       |
| I057 | Last Change Date                | 57-64           | N/8         | 9(8)    |


Note  
The shaded row represents the unique key into the file.

# Medi-Span Labeler Identifier

This is a 5-digit numeric field.

The Medi-Span Labeler Identifier links the drug product to its manufacturer or distributor. Most Medi-Span Labeler Identifiers are derived from the labeler code segment of the NDC-UPC-HRI. However, in some cases, the Medi-Span Labeler Identifier differs from the labeler code segment of the NDC-UPC-HRI, so that the accurate division name within the manufacturer or distributor can be associated with the drug product.

Example:


| Medi-Span Labeler Identifier | Manufacturer's (Labeler) Name | Manufacturer's Abbreviated Name | Labeler Type Code |
| ---------------------------- | ----------------------------- | ------------------------------- | ----------------- |
| 00067                        | NOVARTIS                      | NOV CON HE                      | B                 |
| 00078                        | NOVARTIS                      | NOVARTIS                        | B                 |
| 00904                        | MAJOR PHARMACEUTICALS         | MAJOR                           | G                 |
| 17191                        | BAX CORPORATION               | BAXA CORP                       | O                 |
| 55513                        | AMGEN                         | AMGEN                           | B                 |


For more information, go to Chapter 2, "Medi-Span Labeler Identifier".

Documentation Manual 4-53  
Published: 11/11  
Revised: 08/21

Data Elements

# Manufacturer's (Labeler) Name

This is a 30-character field.

The Manufacturer's (Labeler) Name indicates the manufacturer, distributor, and/or division whose name is included on the label.

Example:


| Medi-Span Labeler Identifier | Manufacturer's (Labeler) Name | Manufacturer's Abbreviated Name | Labeler Type Code |
| ---------------------------- | ----------------------------- | ------------------------------- | ----------------- |
| 00067                        | NOVARTIS                      | NOV CON HE                      | B                 |
| 00078                        | NOVARTIS                      | NOVARTIS                        | B                 |
| 00904                        | MAJOR PHARMACEUTICALS         | MAJOR                           | G                 |
| 17191                        | BAX CORPORATION               | BAXA CORP                       | O                 |
| 55513                        | AMGEN                         | AMGEN                           | B                 |


# Manufacturer's Abbreviated Name

This is a 10-character field.

The Manufacturer's Abbreviated Name indicates the shortened name for the manufacturer, distributor, and/or division whose name is included on the label.

Example:


| Medi-Span Labeler Identifier | Manufacturer's (Labeler) Name | Manufacturer's Abbreviated Name | Labeler Type Code |
| ---------------------------- | ----------------------------- | ------------------------------- | ----------------- |
| 00067                        | NOVARTIS                      | NOV CON HE                      | B                 |
| 00078                        | NOVARTIS                      | NOVARTIS                        | B                 |
| 00904                        | MAJOR PHARMACEUTICALS         | MAJOR                           | G                 |
| 17191                        | BAX CORPORATION               | BAXA CORP                       | O                 |
| 55513                        | AMGEN                         | AMGEN                           | B                 |


# Labeler Type Code

This is a 1-character field.

4-54 MED-File v2

Published: 11/11

Revised: 08/21

Labeler File

The Labeler Type Code helps differentiate among manufacturers that produce

- innovator products
- generic products
- innovator and generic products

Valid Values:


| Value | Description                      | Definition                                                                                  |
| ----- | -------------------------------- | ------------------------------------------------------------------------------------------- |
| B     | Promoted as “Brand”              | Labeler’s products are priced or promoted as “Brand,” “Originator,” or “Innovator” products |
| G     | Promoted as “Generic”            | Labeler’s products are priced or promoted as “Generic” products                             |
| O     | Promoted as “Brand” or “Generic” | Labeler’s products are priced or promoted as either “Brand” or “Generic” products           |


Note  
The Labeler Type Code may change as labelers merge or as market strategies change.

Example:


| Medi-Span Labeler Identifier | Manufacturer's (Labeler) Name | Manufacturer's Abbreviated Name | Labeler Type Code |
| ---------------------------- | ----------------------------- | ------------------------------- | ----------------- |
| 00067                        | NOVARTIS                      | NOV CON HE                      | B                 |
| 00078                        | NOVARTIS                      | NOVARTIS                        | B                 |
| 00904                        | MAJOR PHARMACEUTICALS         | MAJOR                           | G                 |
| 17191                        | BAXA CORPORATION              | BAXA CORP                       | O                 |
| 55513                        | AMGEN                         | AMGEN                           | B                 |


## Reserve

This is a 9-character field.

The Reserve field is an unused field that may be used at a future date.

## Transaction CD

This is a 1-character field.

Documentation Manual 4-55  
Published: 11/11  
Revised: 08/21

Data Elements

The Transaction CD indicates the file activity that last occurred for a record.

Valid Values:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note All Transaction CDs are blank for Total Database.

# Last Change Date

This is an 8-digit numeric field

For the Total database file, the Last Change Date is the MED-File issue date.

For the Incremental file, the Last Change Date depends upon the type of change, represented by the transaction code, as follows:


| Transaction Code | Last Change Date Representation                                       |
| ---------------- | --------------------------------------------------------------------- |
| Add              | MED-File issue date                                                   |
| Change           | MED-File issue date                                                   |
| Delete           | Previous MED-File issue date, dependent on frequency of file delivery |


This date is in Gregorian format.

# GPPC File

(MF2GPPC)

The Generic Product Packaging Code (GPPC) File defines the packaging fields represented by the Generic Product Packaging Code in the NDC File.

This file is related to the NDC File through the Generic Product Packaging Code in a one-to-many relationship. It is also related to the GPPC Price File through the Generic Product Packaging Code in a one-to-zero or one-to-many relationship.

4-56 MED-File v2

Published: 11/11

Revised: 08/21

GPPC File

Note  
To view an exception to the data contained within the inactives file, go to Appendix F: Inactives File Exceptions.

The GPPC File contains the following data elements:


| Code | Data Element Name                  | Record Position | Type/Length | Picture   |
| ---- | ---------------------------------- | --------------- | ----------- | --------- |
| J001 | Generic Product Packaging Code     | 1-8             | C/8         | X(8)      |
| J009 | Package Size                       | 9-17            | N/9         | 9(6)V9(3) |
| J018 | Package Size Unit of Measure       | 18-19           | C/2         | X(2)      |
| J020 | Package Quantity                   | 20-24           | N/5         | 9(5)      |
| J025 | Unit-Dose/Unit-of-Use Package Code | 25-25           | C/1         | X         |
| J026 | Package Description Code           | 26-27           | C/2         | X(2)      |
| J028 | Generic Product Identifier         | 28-41           | C/14        | X(14)     |
| J042 | Reserve                            | 42-55           | C/14        | X(14)     |
| J056 | Transaction CD                     | 56-56           | C/1         | X         |
| J057 | Last Change Date                   | 57-64           | N/8         | 9(8)      |


Note  
The shaded row represents the unique key into the file.

# Generic Product Packaging Code

This is an 8-character field.

The Generic Product Packaging Code (GPPC) identifies unique combinations of the following fields:


| Data Element Name                  | Data Element Code |
| ---------------------------------- | ----------------- |
| Generic Product Identifier         | J028              |
| Package Description Code           | J026              |
| Package Size                       | J009              |
| Package Size Unit of Measure       | J018              |
| Package Quantity                   | J020              |
| Unit-Dose/Unit-of-Use Package Code | J025              |


The Generic Product Packaging Code (GPPC) defines a drug product and its packaging. The first five characters of the GPPC, referred to as the GPPC-Core, are random and represent the drug's GPI. The last three characters are referred

Documentation Manual 4-57

Published: 11/11

Revised: 08/21

Data Elements

to as the GPPC-Suffix and identify unique combinations of the fields in the table below.

4-58 MED-File v2  
Published: 11/11  
Revised: 08/21

GPPC File

Table 4-1: GPPC File Packaging Field Examples


| GPPC     | Package Size | Package Size Unit of Measure | Package Quantity | Unit-Dose/ Unit-of-Use Package | Package Description | Generic Product Identifier                      |
| -------- | ------------ | ---------------------------- | ---------------- | ------------------------------ | ------------------- | ----------------------------------------------- |
| 09843001 | 100          | Each                         | 1                | Unit-of-Use                    | Bottle              | 60204080100315 Zolpidem Tartrate Tab 10 MG      |
| 09843003 | 100          | Each                         | 1                | &nbsp;                         | Bottle              | 60204080100315 Zolpidem Tartrate Tab 10 MG      |
| 46788027 | 500          | 1                            | &nbsp;           | &nbsp;                         | Bottle              | 60204080100410 Zolpidem Tartrate Tab CR 6.25 MG |
| 46788028 | 100          | Each                         | 1                | Unit-Dose                      | Box                 | 60204080100410 Zolpidem Tartrate Tab CR 6.25 MG |
| 03450583 | 15           | Milliliter                   | 100              | Unit-Dose                      | Cup                 | 642000100002010 Acetaminophen Soln 160 MG/5 ML  |


Note  
The Total Package Quantity can be calculated by multiplying the Package Size by the Package Quantity.

For more information, go to Chapter 2, "Generic Product Packaging Code".

Documentation Manual 4-59

Published: 11/11

Data Elements

# Package Size

This is a 9-digit numeric field.

The Package Size represents the total size of the package in volume or number of units contained. In oral suspensions for reconstitution, the Package Size after reconstitution is the number shown in this field, as stated by the manufacturer.

For specific examples of this field, go to GPPC File Packaging Field Examples.

Note Unit of use packets with a quantity of less than one, have a package size of 1.

Note For injectables that can be reconstituted to a variable volume, the Package Size is "1".

Note The Total Package Quantity can be calculated by multiplying the Package Size by the Package Quantity.

# Package Size Unit of Measure

This is a 2-character field.

The Package Size Unit of Measure identifies the unit of measure for the Package Size of the solid, liquid, or gas as dispensed. Wolters Kluwer's assignment of this value is in accordance with the standards set forth by the National Council for Prescription Drug Programs (NCPDP).

Valid Values:


| Value | Description |
| ----- | ----------- |
| EA    | Each        |
| GM    | Gram        |
| ML    | Milliliter  |


Note Unit of use packets with a quantity of less than one, have a package size unit of measure of EA.

4-60 MED-File v2

Published: 11/11

Revised: 08/21

GPPC File

Note  
For injectables that can be reconstituted to a variable volume, the Package Size Unit of Measure will be “EA”.

For specific examples of this field, go to GPPC File Packaging Field Examples.

# Package Quantity

This is a 5-digit numeric field.

The Package Quantity identifies the number of individual containers or units per package as supplied by the manufacturer.

Note  
The Total Package Quantity can be calculated by multiplying the Package Size by the Package Quantity.

For specific examples of this field, go to GPPC File Packaging Field Examples.

# Unit-Dose/Unit-of-Use Package Code

This is a 1-character field.

The Unit-Dose/Unit-of-Use Package Code identifies drug products which are packaged as “Unit-Dose” or “Unit-of-Use.”

Valid Values:


| Value | Description           | Definition                                                                                                                                                                                                                                                                                                                                        |
| ----- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| X     | Unit-Dose Packaging   | Any drug product packaged and intended for administration as a single dose at one time. These drug products also maintain complete labeling (UD cup, Strip Packaging tablet/capsule, packet of 2 tablets/capsules that constitute a single dose); this includes all single-dose injections (such as PTV, SDV, amps, syringes, and partial fills). |
| U     | Unit-of-Use Packaging | Any packaged drug product in a standard quantity for a specific therapy suitable for direct dispensing to the patient. Examples include repackaged products, tubes of semi-solids, potassium chloride powder packets, nicotine gum, and bulk over-the-counter products.                                                                           |
| b'    | Standard Packaging    | Any drug product in which portions are removed for administration and dispensing. This portion does not have labeling for a single-dose unit.                                                                                                                                                                                                     |


Documentation Manual 4-61

Published: 11/11

Revised: 08/21

Data Elements

For specific examples of this field, go to GPPC File Packaging Field Examples.

# Package Description Code

This is a 2-character field.

The Package Description Code indicates the container or package used for the drug product. The table below lists the current values.

Note  
The two-character Package Description Code is not to be displayed or provided in print form in end-user applications. The code should be translated to its corresponding Value Description as defined in the Validation/Translation File. Significant patient safety issues are associated with the use of non-standard abbreviations such as those found in the Package Description Code.


| Value | Description |
| ----- | ----------- |
| AM    | Ampule      |
| AT    | Atomizer    |
| BG    | Bag         |
| BL    | Blister     |
| BO    | Bottle      |
| BX    | Box         |
| CN    | Can         |
| CT    | Cartridge   |
| CP    | Cup         |
| CR    | Crtrdg-NDL  |
| DP    | Disp Pack   |
| DR    | Drum        |
| FC    | Flex Cont   |
| GC    | Glass Cont  |
| IH    | Inhaler     |
| JR    | Jar         |
| PA    | Pack        |
| PB    | Pump Btl    |
| PC    | Plas Cont   |
| PD    | Punchcard   |
| PG    | Package     |
| PK    | Packet      |
| PN    | Pen         |
| RL    | Roll        |
| SB    | Spray Btl   |
| SH    | Sachet      |


4-62 MED-File v2

Published: 11/11

Revised: 08/21

GPPC File


| Value | Description |
| ----- | ----------- |
| SK    | Stick       |
| ST    | Strip       |
| SR    | Syringe     |
| TB    | Tube        |
| VL    | Vial        |


For specific examples of this field, go to GPPC File Packaging Field Examples.

# Generic Product Identifier

This is a 14-character field.

The Generic Product Identifier (GPI) categorizes drug products by a hierarchical therapeutic classification scheme. The GPI defines pharmaceutically equivalent drug products that are identical in:

- active ingredient(s)
- dosage form
- route
- strength or concentration

For specific examples of this field, go to GPPC File Packaging Field Examples.

For more information, see “Generic Product Identifier” in Chapter 2.

# Reserve

This is a 14-character field.

The Reserve field is an unused field that may be used at a future date.

# Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record. Valid Values:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Documentation Manual 4-63

Published: 11/11

Revised: 08/21

Data Elements

Note  
All Transaction CDs are blank for Total Database.

# Last Change Date

This is an 8-digit numeric field.

For the Total database file, the Last Change Date is the MED-File issue date.

For the Incremental file, the Last Change Date depends upon the type of change, represented by the transaction code, as follows:


| Transaction Code | Last Change Date Representation                                       |
| ---------------- | --------------------------------------------------------------------- |
| Add              | MED-File issue date                                                   |
| Change           | MED-File issue date                                                   |
| Delete           | Previous MED-File issue date, dependent on frequency of file delivery |


This date is in Gregorian format.

# Error Correct File

(MF2ERR)

The Error Correct File contains the unique key and data element code of the field that has data entry revisions.

Data Entry Revisions occur if the data associated when a drug product is adjusted due to:

- Clerical Revisions
- GPI revisions
- NCPDP Billing Unit or Packaging decision changes
- Inaccurate or retracted information received directly from the manufacturer'

An example of the last bullet point is when a manufacturer will inform Wolters Kluwer of a price change which is output. Later the manufacturer may retract the price. Correct processing of the Error Correct File enables the end-user to detect these conditions and update their database accordingly.

Note  
The Error Correct File is present only in an Incremental Update when a data entry revision has been made.

4-64 MED-File v2

Published: 11/11

Revised: 08/21

Error Correct File

The Error Correct File contains the following data elements:


| Code | Data Element Name   | Record Position | Type/Length | Picture |
| ---- | ------------------- | --------------- | ----------- | ------- |
| K001 | Key Identifier      | 1-1             | C/1         | X       |
| K002 | Unique Key          | 2-20            | C/19        | X(19)   |
| K021 | Data Element Code   | 21-24           | C/4         | X(4)    |
| K025 | Data Element Length | 25-27           | N/3         | 9(3)    |
| K028 | Reserve             | 28-32           | C/5         | X(5)    |


Note  
The shaded rows represent the unique key into the file.

# Key Identifier

This is a 1-character field.

The Key Identifier identifies the Unique Key [Data Element Code K002] for the record.

Valid Values:


| Value | Description                |
| ----- | -------------------------- |
| 1     | Drug Descriptor Identifier |
| 2     | NDC-UPC-HRI                |
| 3     | NDC-UPC-HRI and Price Type |


Example:


| Key Identifier                 | Unique Key   | Data Element Code | Data Element Length |
| ------------------------------ | ------------ | ----------------- | ------------------- |
| 2 (NDC-UPC-HRI)                | 50428207688  | H023              | 8                   |
| 3 (NDC-UPC-HRI and Price Type) | 50428207688A | M021              | 11                  |


# Unique Key

This is a 19-character field.

The Unique Key contains the actual value that was used to update the revised information.

Documentation Manual 4-65  
Published: 11/11  
Revised: 08/21

Data Elements

Example:


| Key Identifier                 | Unique Key   | Data Element Code | Data Element Length |
| ------------------------------ | ------------ | ----------------- | ------------------- |
| 2 (NDC-UPC-HRI)                | 50428207688  | H023              | 8                   |
| 3 (NDC-UPC-HRI and Price Type) | 50428207688A | M021              | 11                  |


## Data Element Code

This is a 4-character field.

The Data Element Code identifies the record and position of the field within the file that was revised.

Example:


| Key Identifier                 | Unique Key   | Data Element Code | Data Element Length |
| ------------------------------ | ------------ | ----------------- | ------------------- |
| 2 (NDC-UPC-HRI)                | 50428207688  | H023              | 8                   |
| 3 (NDC-UPC-HRI and Price Type) | 50428207688A | M021              | 11                  |


## Data Element Length

This is a 3-digit numeric field.

The Data Element Length indicates the length of the field which was revised.

Example:


| Key Identifier                 | Unique Key   | Data Element Code | Data Element Length |
| ------------------------------ | ------------ | ----------------- | ------------------- |
| 2 (NDC-UPC-HRI)                | 50428207688  | H023              | 8                   |
| 3 (NDC-UPC-HRI and Price Type) | 50428207688A | M021              | 11                  |


## Reserve

This is a 5-character field.

The Reserve field is an unused field that may be used at a future date.

4-66 MED-File v2

Published: 11/11

Revised: 08/21

GPPC Price File

# GPPC Price File

(MF2GPR)

The GPPC Price File provides AAWPs and GEAPs for drug products, when applicable.

The GPPC Price File may contain multiple prices associated with a specific GPPC. There is one occurrence for a GPPC and GPPC Price Code, but not every GPPC or GPPC and GPPC Price Code has a record in this file. There may be zero, one, or many pricing records for a GPPC; however, there can be no more than one occurrence for a given GPPC and GPPC Price Code combination.

The GPPC Price File contains the following data elements:


| Code | Data Element Name              | Record Position | Type/Length | Picture   |
| ---- | ------------------------------ | --------------- | ----------- | --------- |
| L001 | Generic Product Packaging Code | 1-8             | C/8         | X(8)      |
| L009 | GPPC Price Code                | 9-9             | C/1         | X         |
| L010 | Effective Date                 | 10-17           | N/8         | 9(8)      |
| L018 | Unit Price                     | 18-28           | N/11        | 9(5)V9(6) |
| L029 | Reserve                        | 29-55           | C/27        | X(27)     |
| L056 | Transaction CD                 | 56-56           | C/1         | X(1)      |
| L057 | Last Change Date               | 57-64           | N/8         | 9(8)      |


Note

The shaded rows represent the unique key into the file.

# Generic Product Packaging Code

This is an 8-character field

The Generic Product Packaging Code (GPPC) identifies unique combinations of the following fields:


| Data Element Name                  | Data Element Code |
| ---------------------------------- | ----------------- |
| Generic Product Identifier         | J028              |
| Package Description Code           | J026              |
| Package Size                       | J009              |
| Package Size Unit of Measure       | J018              |
| Package Quantity                   | J020              |
| Unit-Dose/Unit-of-Use Package Code | J025              |


Documentation Manual 4-67

Published: 11/11

Revised: 08/21

Data Elements

# GPPC Price Code

This is a 1-character field.

The GPPC Price Code indicates the type of pricing in the Unit Price [Data Element Code L018] and GPPC Eff Date [Data Element Code L010] fields.

Valid Values:


| Value | Description                   |
| ----- | ----------------------------- |
| 1     | Average AWP (AAWP)            |
| 2     | Generic Equivalent AWP (GEAP) |


At the time when a generic product no longer has therapeutic equivalent drug products or the number of manufacturers is insufficient to calculate an average, a record with a GPPC Price Code of 2 and a price of 00000.000000 is represented in the output on Incremental Updates. After that time, this combination of GPPC and GPPC Price Code continues to be represented in the output on Total Databases with a price of 00000.000000 or until an AAWP or GEAP is calculated again.

# Effective Date

This is an 8-digit numeric field.

The Effective Date is the date the GPPC Unit Price was computed. If a price has not changed since the previous calculation, the date reflects that previous calculation.

This date is in Gregorian (YYYYMMDD) format.

# Unit Price

This is an 11-digit numeric field.

The GPPC Unit Price is defined by the GPPC Price Code [Data Element Code L009].

Note This field outputs as 00000000000 if the unit price is greater than $99,999.

# Reserve

This is a 27-character field.

4-68 MED-File v2

Published: 11/11

Revised: 08/21

NDC Price File

The Reserve field is an unused field that may be used at a future date.

## Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

Valid Values:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note All Transaction CDs are blank for Total Database.

## Last Change Date

This is an 8-digit numeric field.

For the Total database file, the Last Change Date is the MED-File issue date.

For the Incremental file, the Last Change Date depends upon the type of change, represented by the transaction code, as follows:


| Transaction Code | Last Change Date Representation                                       |
| ---------------- | --------------------------------------------------------------------- |
| Add              | MED-File issue date                                                   |
| Change           | MED-File issue date                                                   |
| Delete           | Previous MED-File issue date, dependent on frequency of file delivery |


This date is in Gregorian format.

## NDC Price File

(MF2PRC)

The NDC Price File provides, if available, the current AWP, DP, CMS FUL, and WAC prices and their price effective dates.

Documentation Manual 4-69

Published: 11/11

Revised: 08/21

Data Elements

The NDC Price File may contain multiple records for a specific NDC-UPC-HRI. There will be one occurrence for an NDC-UPC-HRI, a selected Price Code and an effective date, but not every NDC-UPC-HRI will have all Price Codes in this file.

The NDC Price File contains the following data elements:


| Code | Data Element Name     | Record Position | Type/Length | Picture   |
| ---- | --------------------- | --------------- | ----------- | --------- |
| M001 | NDC-UPC-HRI           | 1-11            | C/11        | X(11)     |
| M012 | Price Code            | 12-12           | C/1         | X         |
| M013 | Price Effective Date  | 13-20           | N/8         | 9(8)      |
| M021 | Unit Price            | 21-31           | N/11        | 9(5)V9(6) |
| M032 | Unit Price - Extended | 32-44           | N/13        | 9(8)V9(5) |
| M045 | Package Price         | 45-54           | N/10        | 9(8)V9(2) |
| M055 | AWP Indicator Code    | 55-55           | C/1         | X         |
| M056 | Transaction CD        | 56-56           | C/1         | X         |
| M057 | Last Change Date      | 57-64           | N/8         | 9(8)      |


Note  
The shaded rows represent the unique key into the file.

# NDC-UPC-HRI

This is an 11-character field.

NDCs, UPCs, and HRIs are 10-character codes used to identify drug products. Surgical supplies and nonprescription drug products may have an NDC and an HRI or UPC according to the standards set forth by the Uniform Product Code Council, Inc. These codes are converted to eleven characters according to NCPDP standards.

# Price Code

The Price Code indicates the type of price in the record.

Valid Values:


| Value | Description                  |
| ----- | ---------------------------- |
| A     | AWP                          |
| D     | DP                           |
| H     | HCFA FFP                     |
| U     | HCFA FFP for unit dose items |
| W     | WAC                          |


4-70 MED-File v2

Published: 11/11

Revised: 08/21

NDC Price File

Note  
In this file, “HCFA FFP” represents the Centers for Medicare and Medicaid Services Federal Upper Limit (CMS FUL) and is zero.

## Price Effective Date

The Price Effective Date represents the effective date of the price.

The Price Effective Date is in Gregorian format.

## Unit Price

This is an 11-digit numeric field.

The Unit Price represents the price per each unit (tablet, capsule, lozenge, suppository, etc.), gram, or milliliter, as defined by the Package Size Unit of Measure.

The Unit Price is computed by dividing the Package Price by the product of the Package Size multiplied by the Package Quantity. The cost of the prescription can be calculated by multiplying the Unit Price by the quantity dispensed.

In the case where dry injectable products may be reconstituted to variable volumes, this price represents the price per single dry vial, ampule, or syringe.

$$  
\frac{\text{Package Price}}{(\text{Package Size} \times \text{Package Quantity})} = \text{Unit Price}  
$$

Note  
This field outputs as 00000000000 if the unit price is greater than $99,999.

## Unit Price - Extended

This is a 13-digit numeric field.

The Unit Price - Extended is similar to the Unit Price field in that it represents the price per each unit (tablet, capsule, lozenge, suppository, etc.), gram, or milliliter, as defined by the Package Size Unit of Measure.

The Unit Price - Extended is computed by dividing the Package Price by the product of the Package Size multiplied by the Package Quantity. The cost of the prescription can be calculated by multiplying the Unit Price - Extended by the quantity dispensed.

Documentation Manual 4-71  
Published: 11/11  
Revised: 08/21

Data Elements

In the case where dry injectable products may be reconstituted to variable volumes, this price represents the price per single dry vial, ampule, or syringe.

$$  
\frac {\text {Package Price}}{\text {(Package Size} ^ {*} \text {Package}} = \text {Unit Price - Extended} \text {Quantity)}}  
$$

**Note**

The Unit Price - Extended field allows for additional positions to the left of the decimal point that are not available in the Unit Price field. When the Unit Price exceeds $99,999, the Unit Price field will be output as 00000000000 and only the Unit Price - Extended will be populated.

# Package Price

This is a 10-digit numeric field.

The Package Price represents the price for the entire package of the item. The Package Price is converted to Unit Price by dividing the Package Price by the product of the Package Size multiplied by the Package Quantity. The cost of the prescription can be calculated by multiplying the Unit Price by the quantity dispensed.

In the case where dry injectable products may be reconstituted to variable volumes, this price represents the price per single dry vial, ampule, or syringe.

$$  
\frac {\text {Package Price}}{\text {(Package Size} ^ {*} \text {Package}} = \text {Unit Price} \text {Quantity)}}  
$$

# AWP Indicator Code

The AWP Indicator Code is a proprietary Wolters Kluwer concept that indicates how the AWP was obtained by Wolters Kluwer.

The current values are:


| Value | Description                              |
| ----- | ---------------------------------------- |
| A     | Mark-up ≤ 1.20 mfr. WAC or DP            |
| L     | Std. mark-up of 1.20 mfr. WAC or DP      |
| S     | Mfr. suggested AWP                       |
| K     | Adj. std. mark-up of 1.20 mfr. WAC or DP |
| M     | Std. mark-up of 1.25 mfr. WAC or DP      |


4-72 MED-File v2

Published: 11/11

Revised: 08/21

NDC Price File

Note  
The codes, descriptions, and definitions above reflect Wolters Kluwer's current AWP editorial policies. This information may have changed over time with announced changes in our AWP editorial policies. Please refer to current and historical editorial polices or contact Wolters Kluwer Customer Support if you have questions regarding use of these codes, descriptions, and definitions.

The AWP Indicator Code is used as follows:

- Prior to September 26, 2009, AWP Indicator Codes of A, S, and M were in use.
- AWP Indicator Code K was used to make one-time adjustments effective September 26, 2009.
- As of September 27, 2009, AWP Indicator Codes of A, S, and L are used.

# Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

Valid Values:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note  
All Transaction CDs are blank for Total Database.

# Last Change Date

This is an 8-digit numeric field.

In the Total database file and Incremental update file, the Last Change Date is the Med-File issue date regardless of Transaction Code value.

This date is in Gregorian format.

Documentation Manual 4-73

Published: 11/11

Revised: 08/21

Data Elements

# Modifier File

(MF2MOD)

The Modifier File contains codes and descriptions of supplemental information not included in the package and product description but useful to identify packaging and product types.

Each Modifier Code record is linked to zero, one, or many NDC Modifier File records through the Modifier Code.

The Modifier File contains the following data elements:


| Code | Data Element Name    | Record Position | Type/Length | Picture |
| ---- | -------------------- | --------------- | ----------- | ------- |
| N001 | Modifier Code        | 1-6             | C/6         | X(6)    |
| N007 | Modifier Description | 7-31            | C/25        | X(25)   |
| N032 | Reserve              | 32-55           | C/24        | X(24)   |
| N056 | Transaction CD       | 56-56           | C/1         | X       |
| N057 | Last Change Date     | 57-64           | N/8         | 9(8)    |


Note The shaded row represents the unique key into the file.

# Modifier Code

This is a 6-character field.

Modifier Codes describe supplemental information not included in any other field but can be used to identify unique product or packaging types. Modifier Codes are available in the NDC Modifier File. Modifier Codes include information such as needle length and gauge, vial type (for example, ADD-Vantage and pin-top), product flavors, and more.

Effective March 1, 1018, compounded products from outsourcing facilities will have only one product modifier, "Compounded Product". All other product modifiers will not be applicable for compounded products from outsourcing facilities.

The structure of the Modifier Code and the Modifier Type are illustrated below.

Modifier Codes are comprised of three two-character subsets. The first subset defines the Modifier Type.

4-74 MED-File v2

Published: 11/11

Revised: 08/21

Modifier File

Valid Values:


| Value | Modifier Type       |
| ----- | ------------------- |
| AA    | Package Modifiers   |
| BB    | Product Modifiers   |
| TT    | Trademark Modifiers |


The first and second subsets define the Modifier Type and Modifier Category.

Examples of Package Modifiers include:


| Value | Modifier Category                     |
| ----- | ------------------------------------- |
| AA AA | Vial Sizes                            |
| AA AB | Parenteral Packaging Descriptions     |
| AA AC | Needle Lengths and Gauges             |
| AA AD | Non-Parenteral Packaging Descriptions |
| AA AE | Neonatal/Pediatric Packaging          |
| AA AF | Package Size                          |
| AA AG | Item Size Description                 |


Examples of Product Modifiers include:


| Value | Modifier Category                                     |
| ----- | ----------------------------------------------------- |
| BB AA | Colors                                                |
| BB AB | Flavors                                               |
| BB AC | Base Types                                            |
| BB AD | Dosage Forms                                          |
| BB AE | Shapes                                                |
| BB AF | Free Descriptions (such as Dye Free and Alcohol Free) |
| BB AG | Fragrance                                             |


Note  
Colors, Flavors, Base Types, Dosage Forms, Shapes, and Free Descriptions are included when multiple original drug products are available. These descriptions differentiate generic drug products mimicking original drug products. This information is not included in the GPI. A Modifier Code is only present when relevant to the drug product. A color Product Modifier is not present if two colors are noted for the same NDC-UPC-HRI.

Examples of Trademark Modifiers include:


| Value | Category                  |
| ----- | ------------------------- |
| TT AA | Trademark Packaging Terms |
| TT AB | Trademark Dosage Forms    |


Documentation Manual 4-75  
Published: 11/11  
Revised: 08/21

Data Elements

The first, second, and third subsets define the Modifier Type, Modifier Category, and specific Modifier Code within a category.

## Modifier Description

This is a 25-character field.

The Modifier Description describes what the Modifier Code [N001] represents.

## Example


| Modifier Code | Modifier Description  |
| ------------- | --------------------- |
| AAAA28        | 500 ML                |
| AAAA73        | 2 CARTONS OF 30 EACH  |
| AAAB38        | W/LUER LOCK           |
| AAAB9D        | W/O DILUENT           |
| AAABN3        | PRECISIONGLIDE NEEDLE |
| AAAC50        | 25G X 5/8             |
| BBAAER        | WHITE/PURPLE          |
| BBAB96        | CHERRY-VANILLA        |
| BBAC7P        | NON-ALKALINE          |
| BBAD37        | SOFTGEL(S)            |
| BBAE23        | RECTANGULAR           |
| BBAF51        | TALK FREE             |
| BBAI01        | MEDICAL FOOD          |
| BBAI03        | AUTHORIZED GENERIC    |
| TTAA64        | CONVENIENCE PACK      |
| TTAAD3        | AMBU-FLEX III         |
| TTAABN4       | DUOTAB                |


For a complete list of Modifier Codes and Modifier Descriptions, refer to the contents of the Modifier File.

## Reserve

This is a 24-character field.

The Reserve field is an unused field that may be used at a future date.

## Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

4-76 MED-File v2

Published: 11/11

Revised: 08/21

NDC Modifier File

Valid Values:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note  
All Transaction CDs are blank for Total Database.

# Last Change Date

This is an 8-digit numeric field.

For the Total database file, the Last Change Date is the MED-File issue date.

For the Incremental file, the Last Change Date depends upon the type of change, represented by the transaction code, as follows:


| Transaction Code | Last Change Date Representation                                       |
| ---------------- | --------------------------------------------------------------------- |
| Add              | MED-File issue date                                                   |
| Change           | MED-File issue date                                                   |
| Delete           | Previous MED-File issue date, dependent on frequency of file delivery |


This date is in Gregorian format.

# NDC Modifier File

(MF2NDCM)

The NDC Modifier File contains the NDC-UPC-HRI and the Modifier Codes associated with the NDC-UPC-HRI. These Modifier Codes can be used to provide additional descriptive information or to create a nine-character GPPC.

Note  
For more information regarding creating this nine-character GPPC, see Chapter 5: Applications.

There may be zero, one, or many Modifier Codes associated to an NDC-UPC-HRI.

Documentation Manual 4-77  
Published: 11/11  
Revised: 08/21

Data Elements

The NDC Modifier File contains the following data elements:


| Code | Data Element Name | Record Position | Type/Length | Picture |
| ---- | ----------------- | --------------- | ----------- | ------- |
| O001 | NDC-UPC-HRI       | 1-11            | C/11        | X(11)   |
| O012 | Modifier Code     | 12-17           | C/6         | X(6)    |
| O018 | Reserve           | 18-23           | C/6         | X(6)    |
| O024 | Transaction CD    | 24-24           | C/1         | X       |
| O025 | Last Change Date  | 25-32           | N/8         | 9(8)    |


Note  
The shaded rows represent the unique key into the file.

# NDC-UPC-HRI

This is an 11-character field.

NDCs, UPCs, and HRIs are 10-character codes used to identify drug products. Surgical supplies and nonprescription drug products may have an NDC, and an HRI or UPC according to the standards set forth by the Uniform Product Code Council, Inc. These codes are converted to eleven characters according to NCPDP standards.

# Modifier Code

This is a 6-character field.

Modifier Codes describe supplemental information not included in any other field but can be used to identify unique product or packaging types. Modifier Codes are available in the NDC Modifier File. Modifier Codes include information such as needle length and gauge, vial type (for example, ADD-Vantage and pin-top), product flavors, and more.

The structure of the Modifier Code and the Modifier Type are illustrated below.

Modifier Codes are comprised of three two-character subsets. The first subset defines the Modifier Type.

Valid Values:


| Value | Modifier Type       |
| ----- | ------------------- |
| AA    | Package Modifiers   |
| BB    | Product Modifiers   |
| TT    | Trademark Modifiers |


4-78 MED-File v2

Published: 11/11

Revised: 08/21

NDC Modifier File

The first and second subsets define the Modifier Type and Modifier Category.

Examples of Package Modifiers include:


| Value | Modifier Category                     |
| ----- | ------------------------------------- |
| AA AA | Vial Sizes                            |
| AA AB | Parenteral Packaging Descriptions     |
| AA AC | Needle Lengths and Gauges             |
| AA AD | Non-Parenteral Packaging Descriptions |
| AA AE | Neonatal/Pediatric Packaging          |
| AA AF | Package Size                          |
| AA AG | Item Size Description                 |


Examples of Product Modifiers include:


| Value | Modifier Category                                     |
| ----- | ----------------------------------------------------- |
| BB AA | Colors                                                |
| BB AB | Flavors                                               |
| BB AC | Base Types                                            |
| BB AD | Dosage Forms                                          |
| BB AE | Shapes                                                |
| BB AF | Free Descriptions (such as Dye Free and Alcohol Free) |
| BB AG | Fragrance                                             |


**Note**

Colors, Flavors, Base Types, Dosage Forms, Shapes, and Free Descriptions are included when multiple original drug products are available. These descriptions differentiate generic drug products mimicking original drug products. This information is not included in the GPI. A Modifier Code is only present when relevant to the drug product. A color Product Modifier is not present if two colors are noted for the same NDC-UPC-HRI.

Examples of Trademark Modifiers include:


| Modifier Code | Modifier Description      |
| ------------- | ------------------------- |
| TT AA         | Trademark Packaging Terms |
| TT AB         | Trademark Dosage Forms    |


The first, second, and third subsets define the Modifier Type, Modifier Category, and specific Modifier Code within a category.

Documentation Manual 4-79  
Published: 11/11  
Revised: 08/21

Data Elements

The Package Modifiers Describing Vial Sizes include:


| Modifier Code | Modifier Description |
| ------------- | -------------------- |
| AA AA 01      | 1 ML                 |
| AA AA 02      | 1.5 ML               |


## Reserve

This is a 6-character field.

The Reserve field is an unused field that may be used at a future date.

## Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

Valid Values:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note All Transaction CDs are blank for Total Database.

## Last Change Date

This is an 8-digit numeric field.

For the Total database file, the Last Change Date is the MED-File issue date.

For the Incremental file, the Last Change Date depends upon the type of change, represented by the transaction code, as follows:


| Transaction Code | Last Change Date Representation                                       |
| ---------------- | --------------------------------------------------------------------- |
| Add              | MED-File issue date                                                   |
| Change           | MED-File issue date                                                   |
| Delete           | Previous MED-File issue date, dependent on frequency of file delivery |


4-80 MED-File v2

Published: 11/11

Revised: 08/21

SDI Drug Name File

This date is in Gregorian format.

# SDI Drug Name File

(MF2DRGNM)

The SDI Drug Name File contains the fields associated with a drug name. Specific drug name description data resides in the Description File (MF2DESC). The SDI Drug Name File includes additional historical concepts that are not reflected in the Drug Name File.

The SDI Drug Name File contains the following data elements:


| Code | Data Element Name | Record Position | Type/Length | Picture  |
| ---- | ----------------- | --------------- | ----------- | -------- |
| P001 | Concept Type      | 1-5             | N/5         | 9(5)     |
| P006 | Country Code      | 6-7             | N/2         | 9(2)     |
| P008 | Concept ID        | 8-17            | N/10        | 9(10)    |
| P018 | Transaction CD    | 18-18           | C/1         | X        |
| P019 | Name Type         | 19-19           | C/1         | X        |
| P020 | Status            | 20-20           | N/1         | 9(1)     |
| P021 | Link Value        | 21-30           | N/10        | 9(10)    |
| P031 | Link Date         | 31-38           | N/8         | YYYYMMDD |
| P039 | Reserve           | 39-48           | C/10        | X(10)    |


Note The shaded rows represent the unique key into the file.

# Concept Type

This is a 5-digit numeric field.

The Concept Type defines the type of concept that is represented by the Concept ID. Specific SDI Drug Name description data resides in the Description File (MF2DESC).

Valid Values:


| Value | Description           |
| ----- | --------------------- |
| 00001 | Drug Name             |
| 00002 | Routed Drug           |
| 00003 | Routed Dose Form Drug |
| 00004 | Dispensable Drug      |
| 00005 | GPI                   |


Documentation Manual 4-81

Published: 11/11

Revised: 08/21

Data Elements


| Value | Description           |
| ----- | --------------------- |
| 00006 | GPPC5                 |
| 00007 | NDC-UPC-HRI           |
| 00008 | Route                 |
| 00009 | Dose Form             |
| 00221 | Dose Form Drug        |
| 00222 | Strength-Strength UOM |


Note 00001 (Drug Name) is the only value used in the SDI Drug Name File.

## Country Code

This is a 2-digit numeric field.

The Country Code represents the country to which a Drug Name is specific.

Note 01 (USA) is the only value in use at this time.

## Concept ID

This is a 10-digit numeric field.

The Concept ID identifies the Drug Name.

## Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note All Transaction CDs are blank for Total Databases.

4-82 MED-File v2

Published: 11/11

Revised: 08/21

SDI Drug Name File

# Name Type

This is a 1-character field.

The Name Type identifies whether the Drug Name is a brand name, generic or trademarked drug name.

Valid Values:


| Value | Description |
| ----- | ----------- |
| 1     | Trademarked |
| 2     | Brand Name  |
| 3     | Generic     |


# Status

This is a 1-digit numeric field.

The Status defines the current state of the drug name concept.

Valid Values:


| Value | Description                                    | Abbreviation   |
| ----- | ---------------------------------------------- | -------------- |
| 1     | Active Concept with Active Associated Products | Active w/Prod  |
| 2     | Active w/Assc Prd Inactive <48 Months          | Active w/Inact |
| 3     | Inactive w/Assc Prd Inactive >48 Months        | Inactive w/Prd |
| 4     | Inactive w/no Assc Products                    | Inac w/o Prd   |


Note A Status value of 1 or 2 does not imply that a corresponding NDC-UPC-HRI with this drug name exists in the NDC File.

# Link Value

This is a 10-digit numeric field.

The Link Value identifies the new Concept ID that replaces the Concept ID in this record.

Note The Link Value for this file is not in use at this time. For more information, go to Chapter 5, "Applications".

Documentation Manual 4-83

Published: 11/11

Revised: 08/21

Data Elements

## Link Date

This is an 8-digit numeric field.

The Link Date represents the date the Concept ID was replaced by the Link Value.

**Note** The Link Date for this file is not in use at this time. For more information, go to Chapter 5, “Applications”.

## Reserve

This is a 10-character field.

The Reserve field is an unused field that may be used at a future date.

## Routed Drug File

**(MF2RTDRG)**

The Routed Drug File contains the fields associated with a drug and its route of administration. Specific Routed Drug description data resides in the Description File (MF2DESC). The Routed Drug File includes additional historical concepts that are not reflected in the Drug Name File.

For more information, go to Chapter 2, “Editorial Policies”.

The Routed Drug File contains the following data elements:


| Code | Data Element Name | Record Position | Type/Length | Picture  |
| ---- | ----------------- | --------------- | ----------- | -------- |
| Q001 | Concept Type      | 1-5             | N/5         | 9(5)     |
| Q006 | Country Code      | 6-7             | N/2         | 9(2)     |
| Q008 | Concept ID        | 8-17            | N/10        | 9(10)    |
| Q018 | Transaction CD    | 18-18           | C/1         | X(1)     |
| Q019 | Drug Name ID      | 19-28           | N/10        | 9(10)    |
| Q029 | Route ID          | 29-33           | N/5         | 9(5)     |
| Q034 | Status            | 34-34           | N/1         | 9(1)     |
| Q035 | Link Value        | 35-44           | N/10        | 9(10)    |
| Q045 | Link Date         | 45-52           | N/8         | YYYYMMDD |
| Q053 | Reserve           | 53-80           | C/28        | X(28)    |


**Note** The shaded rows represent the unique key into the file.

4-84 MED-File v2

Published: 11/11

Revised: 08/21

Routed Drug File

# Concept Type

This is a 5-digit numeric field.

The Concept Type defines the type of concept that is represented by the Concept ID.

Valid Values:


| Value | Description           |
| ----- | --------------------- |
| 00001 | Drug Name             |
| 00002 | Routed Drug           |
| 00003 | Routed Dose Form Drug |
| 00004 | Dispensable Drug      |
| 00005 | GPI                   |
| 00006 | GPPC5                 |
| 00007 | NDC-UPC-HRI           |
| 00008 | Route                 |
| 00009 | Dose Form             |
| 00221 | Dose Form Drug        |
| 00222 | Strength-Strength UOM |


Note 00002 (Routed Drug) is the only value used in the Routed Drug File.

# Country Code

This is a 2-digit numeric field.

The Country Code represents the country to which a Routed Drug is specific.

Note 01 (USA) is the only value in use at this time.

# Concept ID

This is a 10-digit numeric field.

The Concept ID identifies the Routed Drug.

# Transaction CD

This is a 1-character field.

Documentation Manual 4-85

Published: 11/11

Revised: 08/21

Data Elements

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note  
All Transaction CDs are blank for Total Databases.

## Drug Name ID

This is a 10-digit numeric field.

The Drug Name ID is a Concept ID representing a Drug Name in the SDI Drug Name File. A description of this value is available in the Description File (MF2DESC).

## Route ID

This is a 5-digit numeric field.

The Route ID is a Concept ID representing a Route in the Route File. A description of this value is available in the Description File (MF2DESC).

## Status

This is a 1-digit numeric field.

The Status defines the current state of the routed drug concept.

Valid Values:


| Value | Description                                    | Abbreviation   |
| ----- | ---------------------------------------------- | -------------- |
| 1     | Active Concept with Active Associated Products | Active w/Prod  |
| 2     | Active w/Assc Prd Inactive <48 Months          | Active w/Inact |
| 3     | Inactive w/Assc Prd Inactive >48 Months        | Inactive w/Prd |
| 4     | Inactive w/no Assc. Products                   | Inac w/o Prd   |


4-86 MED-File v2

Published: 11/11

Revised: 08/21

Drug-Dose Form File

Note  
A Status of 1 or 2 does not imply that a corresponding NDC-UPC-HRI with this drug name and route exists in the NDC File.

# Link Value

This is a 10-digit numeric field.

The Link Value identifies the new Concept ID that replaces the Concept ID in this record.

Note  
The Link Value for this file is not in use at this time. For more information, go to Chapter 5, “Applications”.

# Link Date

This is an 8-digit numeric field.

The Link Date represents the date the Concept ID was replaced by the Link Value.

Note  
The Link Date for this file is not in use at this time. For more information, go to Chapter 5, “Applications”.

# Reserve

This is a 28-character field.

The Reserve field is an unused field that may be used at a future date.

# Drug-Dose Form File

(MF2DFDRG)

The Drug-Dose Form File contains the fields associated with a drug and its dosage form. Specific Dosage Form description data resides in the Description File (MF2DESC). The Drug-Dose Form File includes additional historical concepts that are not reflected in the Drug Name File.

Documentation Manual 4-87

Published: 11/11

Revised: 08/21

Data Elements

The Drug-Dose Form File contains the following data elements


| Code | Data Element Name | Record Position | Type/Length | Picture  |
| ---- | ----------------- | --------------- | ----------- | -------- |
| R001 | Concept Type      | 1-5             | N/5         | 9(5)     |
| R006 | Country Code      | 6-7             | N/2         | 9(2)     |
| R008 | Concept ID        | 8-17            | N/10        | 9(10)    |
| R018 | Transaction CD    | 18-18           | C/1         | X(1)     |
| R019 | Drug Name ID      | 19-28           | N/10        | 9(10)    |
| R029 | Dose Form ID      | 29-33           | N/5         | 9(5)     |
| R034 | Status            | 34-34           | N/1         | 9(1)     |
| R035 | Link Value        | 35-44           | N/10        | 9(10)    |
| R045 | Link Date         | 45-52           | N/8         | YYYYMMDD |
| R053 | Reserve           | 53-80           | C/28        | X(28)    |


Note  
The shaded rows represent the unique key into the file.

## Concept Type

This is a 5-digit numeric field.

The Concept Type defines the type of concept that is represented by the Concept ID.

Valid Values:


| Value | Description           |
| ----- | --------------------- |
| 00001 | Drug Name             |
| 00002 | Routed Drug           |
| 00003 | Routed Dose Form Drug |
| 00004 | Dispensable Drug      |
| 00005 | GPI                   |
| 00006 | GPPC5                 |
| 00007 | NDC-UPC-HRI           |
| 00008 | Route                 |
| 00009 | Dose Form             |
| 00221 | Dose Form Drug        |
| 00222 | Strength-Strength UOM |


Note  
00221 (Dose Form Drug) is the only value used in the Drug-Dose Form File.

4-88 MED-File v2  
Published: 11/11  
Revised: 08/21

Drug-Dose Form File

# Country Code

This is a 2-digit numeric field.

The Country Code represents the country to which a Dose Form Drug is specific.

Note  
01 (USA) is the only value in use at this time.

# Concept ID

This is a 10-digit numeric field.

The Concept ID identifies the Dose Form Drug.

# Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note  
All Transaction CDs are blank for Total Databases.

# Drug Name ID

This is a 10-digit numeric field.

The Drug Name ID is a Concept ID representing a Drug Name in the Drug Name File. A description of this value is available in the Description File (MF2DESC).

# Dose Form ID

This is a 5-digit numeric field.

Documentation Manual 4-89

Published: 11/11

Revised: 08/21

Data Elements

The Dose Form ID is a Concept ID representing a Dose Form in the Dose Form File. A description of this value is available in the Description File (MF2DESC).

## Status

This is a 1-digit numeric field.

The Status defines the current state of the dose form drug concept.

Valid Values:


| Value | Description                                    | Abbreviation   |
| ----- | ---------------------------------------------- | -------------- |
| 1     | Active Concept with Active Associated Products | Active w/Prod  |
| 2     | Active w/Assc Prd Inactive <48 Months          | Active w/Inact |
| 3     | Inactive w/Assc Prd Inactive >48 Months        | Inactive w/Prd |
| 4     | Inactive w/no Assc. Products                   | Inac w/o Prd   |


Note A Status value of 1 or 2 does not imply that a corresponding NDC-UPC-HRI with this drug, name, and dosage form exists in the NDC File.

## Link Value

This is a 10-digit numeric field.

The Link Value identifies the new Concept ID that replaces the Concept ID in this record.

Note The Link Value for this file is not in use at this time. For more information, go to Chapter 5, "Applications".

## Link Date

This is an 8-digit numeric field.

The Link Date represents the date the Concept ID was replaced by the Link Value.

Note The Link Date for this file is not in use at this time. For more information, go to Chapter 5, "Applications".

4-90 MED-File v2

Published: 11/11

Revised: 08/21

Routed Drug Form File

# Reserve

This is a 28-character field.

The Reserve field is an unused field that may be used at a future date.

# Routed Drug Form File

(MF2RTDF)

The Routed Drug Form File contains the fields associated with a drug and its route of administration and dosage form. Specific Routed Dose Form description data resides in the Description File (MF2DESC). The Routed Drug Form File includes additional historical concepts that are not reflected in the Drug Name File.

The Routed Drug Form File contains the following data elements:


| Code | Data Element Name | Record Position | Type/Length | Picture  |
| ---- | ----------------- | --------------- | ----------- | -------- |
| S001 | Concept Type      | 1-5             | N/5         | 9(5)     |
| S006 | Country Code      | 6-7             | N/2         | 9(2)     |
| S008 | Concept ID        | 8-17            | N/10        | 9(10)    |
| S018 | Transaction CD    | 18-18           | C/1         | X        |
| S019 | Routed Drug ID    | 19-28           | N/10        | 9(10)    |
| S029 | Dose Form ID      | 29-33           | N/5         | 9(5)     |
| S034 | Status            | 34-34           | N/1         | 9(1)     |
| S035 | Link Value        | 35-44           | N/10        | 9(10)    |
| S045 | Link Date         | 45-52           | N/8         | YYYYMMDD |
| S053 | Reserve           | 53-80           | C/28        | X(28)    |


Note The shaded rows represent the unique key into the file.

# Concept Type

This is a 5-digit numeric field.

The Concept Type defines the type of concept that is represented by the Concept ID.

Documentation Manual 4-91

Published: 11/11

Revised: 08/21

Data Elements

Valid Values:


| Value | Description           |
| ----- | --------------------- |
| 00001 | Drug Name             |
| 00002 | Routed Drug           |
| 00003 | Routed Dose Form Drug |
| 00004 | Dispensable Drug      |
| 00005 | GPI                   |
| 00006 | GPPC5                 |
| 00007 | NDC-UPC-HRI           |
| 00008 | Route                 |
| 00009 | Dose Form             |
| 00221 | Dose Form Drug        |
| 00222 | Strength-Strength UOM |


Note  
00003 (Routed Dose Form Drug) is the only value used in the Routed Drug Form File.

## Country Code

This is a 2-digit numeric field.

The Country Code represents the country to which a Routed Dose Form Drug is specific.

Note  
01 (USA) is the only value in use at this time.

## Concept ID

This is a 10-digit numeric field.

The Concept ID identifies the Routed Dose Form Drug.

## Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

4-92 MED-File v2

Published: 11/11

Revised: 08/21

Routed Drug Form File

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note All Transaction CDs are blank for Total Databases.

## Routed Drug ID

This is a 10-digit numeric field.

The Routed Drug ID is a Concept ID representing a Routed Drug in a Routed Drug File. A description of this value is available in the Description File (MF2DESC).

## Dose Form ID

This is a 5-digit numeric field.

The Dose Form ID is a Concept ID representing a Dose Form in the Dose Form File. A description of this value is available in the Description File (MF2DESC).

## Status

This is a 1-digit numeric field.

The Status defines the current state of the routed dose form drug concept.

Valid Values:


| Value | Description                                    | Abbreviation   |
| ----- | ---------------------------------------------- | -------------- |
| 1     | Active Concept with Active Associated Products | Active w/Prod  |
| 2     | Active w/Assc Prd Inactive <48 Months          | Active w/Inact |
| 3     | Inactive w/Assc Prd Inactive >48 Months        | Inactive w/Prd |
| 4     | Inactive w/no Assc. Products                   | Inac w/o Prd   |


Note A Status value of 1 or 2 does not imply that a corresponding NDC-UPC-HRI with this drug name, route, and dosage form exists in the NDC File.

Documentation Manual 4-93

Published: 11/11

Revised: 08/21

Data Elements

## Link Value

This is a 10-digit numeric field.

The Link Value identifies the new Concept ID that replaces the Concept ID in this record.

Note  
The Link Value for this file is not in use at this time. For more information, go to Chapter 5, “Applications”.

## Link Date

This is an 8-digit numeric field.

The Link Date represents the date the Concept ID was replaced by the Link Value.

Note  
The Link Date for this file is not in use at this time. For more information, go to Chapter 5, “Applications”.

## Reserve

This is a 28-character field.

The Reserve field is an unused field that may be used at a future date.

## Dispensable Drug File

(MF2DRG)

The Dispensable Drug File contains the fields associated with the Dispensable Drug (DDID). Specific Dispensable Drug description data resides in the Description File (MF2DESC). The Dispensable Drug File includes additional historical concepts that are not reflected in the Drug Name File.

Note  
The Dispensable Drug and the Drug Descriptor are one and the same. The terms may be used interchangeably in this and other Wolters Kluwer documents.

4-94 MED-File v2

Published: 11/11

Revised: 08/21

Dispensable Drug File

The Dispensable Drug File contains the following data elements:


| Code | Data Element Name        | Record Position | Type/Length | Picture  |
| ---- | ------------------------ | --------------- | ----------- | -------- |
| T001 | Concept Type             | 1-5             | N/5         | 9(5)     |
| T006 | Country Code             | 6-7             | N/2         | 9(2)     |
| T008 | Concept ID               | 8-17            | N/10        | 9(10)    |
| T018 | Transaction CD           | 18-18           | C/1         | X        |
| T019 | Routed Drug ID           | 19-28           | N/10        | 9(10)    |
| T029 | Dose Form ID             | 29-33           | N/5         | 9(5)     |
| T034 | Strength                 | 34-48           | C/15        | X(15)    |
| T049 | Strength Unit of Measure | 49-63           | C/15        | X(15)    |
| T064 | Name Source              | 64-64           | N/1         | 9(1)     |
| T065 | Device Flag              | 65-65           | N/1         | 9(1)     |
| T066 | Status                   | 66-66           | N/1         | 9(1)     |
| T067 | Link Value               | 67-76           | N/10        | 9(10)    |
| T077 | Link Date                | 77-84           | N/8         | YYYYMMDD |
| T085 | Routed Drug Form ID      | 85-94           | N/10        | 9(10)    |
| T095 | Drug-Dose Form ID        | 95-104          | N/10        | 9(10)    |
| T105 | Strength-Strength UOM ID | 105-114         | N/10        | 9(10)    |
| T115 | Reserve                  | 115-144         | C/30        | X(30)    |


Note  
The shaded rows represent the unique key into the file.

# Concept Type

This is a 5-digit numeric field.

The Concept Type defines the type of concept that is represented by the Concept ID.

Valid Values:


| Value | Description           |
| ----- | --------------------- |
| 00001 | Drug Name             |
| 00002 | Routed Drug           |
| 00003 | Routed Dose Form Drug |
| 00004 | Dispensable Drug      |
| 00005 | GPI                   |
| 00006 | GPPC5                 |
| 00007 | NDC-UPC-HRI           |
| 00008 | Route                 |


Documentation Manual 4-95  
Published: 11/11  
Revised: 08/21

Data Elements


| Value | Description           |
| ----- | --------------------- |
| 00009 | Dose Form             |
| 00221 | Dose Form Drug        |
| 00222 | Strength-Strength UOM |


Note 00004 (Dispensable Drug) is the only value used in the Dispensable Drug File.

## Country Code

This is a 2-digit numeric field.

The Country Code represents the country to which a Dispensable Drug is specific.

Note 01 (USA) is the only value in use at this time.

## Concept ID

This is a 10-digit numeric field.

The Concept ID identifies the Dispensable Drug.

Note In the Dispensable Drug File, the DDID is defined as a 10-digit number. In the Drug Name File, the DDID is defined as a 6-digit number. They represent the same drug concept. For example, Concept ID "0000000232" in the Dispensable Drug File and Drug Descriptor Identifier "000232" in the Drug Name File both identify "Accupril Oral Tablet 10 MG".

## Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


4-96 MED-File v2

Published: 11/11

Revised: 08/21

Dispensable Drug File

Note  
All Transaction CDs are blank for Total Databases.

# Routed Drug ID

This is a 10-digit numeric field.

The Routed Drug ID is a Concept ID representing a Routed Drug in the Routed Drug File. A description of this value is available in the Description File (MF2DESC).

# Dose Form ID

This is a 5-digit numeric field.

The Dose Form ID is a Concept ID representing a Dose Form in the Dose Form File. A description of this value is available in the Description File (MF2DESC).

# Strength

This is a 15-character field.

The Strength is a character representation of the product's ingredient strength. When combined with the Strength Unit of Measure, it represents the dosage strength as provided by the manufacturer.

# Strength Unit Of Measure

This is a 15-character field.

The Strength Unit Of Measure, when combined with the Strength, represents the dosage strength as provided by the manufacturer.

Example*:


| Strength | Description                | Strength | Description          |
| -------- | -------------------------- | -------- | -------------------- |
| %        | Percent                    | MG       | Milligram            |
| AHFU     | Antihemophilic factor unit | MG/HR    | Milligram/hour       |
| GM       | Gram                       | MG/ML    | Milligram/milliliter |
| GM/ML    | Gram/milliliter            | MINIM    | Minim                |
| UNIT     | International unit         | MMOLE    | Millimole            |


Documentation Manual 4-97

Published: 11/11

Revised: 08/21

Data Elements


| Strength | Description                   | Strength | Description          |
| -------- | ----------------------------- | -------- | -------------------- |
| UNIT/ML  | International unit/milliliter | MMOLE/ML | Millimole/milliliter |
| MCG      | Microgram                     | MU       | Million units        |
| MCG/ML   | Microgram/milliliter          | SQ CM    | Square centimeter    |
| MEQ      | Milliequivalent               | UNIT     | Unit                 |
| MEQ/L    | Milliequivalent/liter         | UNIT/GM  | Unit/gram            |
| MEQ/ML   | Milliequivalent/milliliter    | UNIT/ML  | Unit/milliliter      |


Note

- Due to the dynamic nature of these data, additional values may be added without notice.

Note  
In the Dispensable Drug File, the Strength Unit of Measure is defined as a 15-character field. In the Drug Name File, the Strength Unit of Measure is defined as a 10-character field. They both represent the same concept. The data within these fields is the same.

# Name Source

This is a 1-digit numeric field.

The Name Source field identifies whether the name came from the Generic Product, the Product, or both the Generic Product and the Product.

Valid Values:


| Value | Description               |
| ----- | ------------------------- |
| 0     | Generic                   |
| 1     | Product                   |
| 2     | Generic Product & Product |


# Device Flag

This is a 1-digit numeric field.

The Device Flag field indicates whether or not the Dispensable Drug is a device.

4-98 MED-File v2

Published: 11/11

Revised: 08/21

Dispensable Drug File

Valid Values:


| Value | Description |
| ----- | ----------- |
| 0     | Non Device  |
| 1     | Device      |


# Status

This is a 1-digit numeric field.

The Status defines the current state of the Dispensable Drug concept.

Valid Values:


| Value | Description                                    | Abbreviation   |
| ----- | ---------------------------------------------- | -------------- |
| 1     | Active Concept with Active Associated Products | Active w/Prod  |
| 2     | Active w/Assc Prd Inactive <48 Months          | Active w/Inact |
| 3     | Inactive w/Assc Prd Inactive >48 Months        | Inactive w/Prd |
| 4     | Inactive w/no Assc. Products                   | Inac w/o Prd   |


Note A Status value of 1 or 2 does not imply that a corresponding NDC-UPC-HRI for the Dispensable Drug exists in the NDC File.

# Link Value

This is a 10-digit numeric field.

The Link Value identifies the new Concept ID that replaces the Concept ID in this record.

Note The Link Value for this file is currently in use at this time. For more information, go to Chapter 5, "Applications".

# Link Date

This is an 8-digit numeric field.

The Link Date represents the date the Concept ID was replaced by the Link Value.

Documentation Manual 4-99

Published: 11/11

Revised: 08/21

Data Elements

Note  
The Link Date for this file is currently in use at this time. For more information, go to Chapter 5, “Applications”.

## Routed Drug Form ID

This is a 10-digit numeric field.

The Routed Drug Form ID is a Concept ID representing a Routed Drug Form in the Routed Drug Form File. A description of this value is available in the Description File (MF2DESC).

## Drug-Dose Form ID

This is a 10-digit numeric field.

The Drug-Dose Form ID is a Concept ID representing a drug and its dose form in the Drug-Dose Form File. A description of this value is available in the Description File (MF2DESC).

## Strength-Strength UOM ID

This is a 10-digit numeric field.

The Strength-Strength UOM ID is a Concept ID representing the combination of the strength and the strength unit of measure in the Strength-Strength Unit of Measure File. A description of this value is available in the Description File (MF2DESC).

## Reserve

This is a 30-character field.

The Reserve field is an unused field that may be used at a future date.

## Description File

(MF2DESC)

The Description File contains descriptions for the Concept IDs for the below files:

- SDI Drug Name File
- Routed Drug File
- Drug-Dose Form File

4-100 MED-File v2

Published: 11/11

Revised: 08/21

Description File

- Routed Dose Form File
- Dispensable Drug File
- Route File
- Dose Form File
- Strength-Strength Unit of Measure File
- Drug Concept ID to Ingredient Set ID File

The Description File includes additional historical concepts that are not reflected in the Drug Name File. The Description File contains the following data elements:


| Code | Data Element Name | Record Position | Type/Length | Picture |
| ---- | ----------------- | --------------- | ----------- | ------- |
| U001 | Concept Type      | 1-5             | N/5         | 9(5)    |
| U006 | Country Code      | 6-7             | N/2         | 9(2)    |
| U008 | Concept ID        | 8-17            | N/10        | 9(10)   |
| U018 | Type Code         | 18-18           | N/1         | N(1)    |
| U019 | Transaction CD    | 19-19           | C/1         | X       |
| U020 | Description       | 20-269          | C/250       | X(250)  |
| U270 | Reserve           | 270-336         | C/67        | X(67)   |


Note  
The shaded rows represent the unique key into the file.

# Concept Type

This is a 5-digit numeric field.

The Concept Type defines the type of concept that is represented by the Concept ID.

Valid Values:


| Value | Description           |
| ----- | --------------------- |
| 00001 | Drug Name             |
| 00002 | Routed Drug           |
| 00003 | Routed Dose Form Drug |
| 00004 | Dispensable Drug      |
| 00005 | GPI                   |
| 00006 | GPPC5                 |
| 00007 | NDC-UPC-HRI           |
| 00008 | Route                 |
| 00009 | Dose Form             |
| 00221 | Dose Form Drug        |
| 00222 | Strength-Strength UOM |


Documentation Manual 4-101

Published: 11/11

Revised: 08/21

Data Elements

Note 00005 (GPI), 00006 (GPPC), and 00007 (NDC-UPC-HRI) are currently not used in this file.

## Country Code

This is a 2-digit numeric field.

The Country Code represents the country to which a Concept Type, Concept ID, and Type Code are specific.

Note 01 (USA) is the only value in use at this time.

## Concept ID

This is a 10-digit numeric field.

The Concept ID represents a specific concept for a Concept Type, Country Code, and Type Code.

Example:


| Concept Type          | Concept ID                                             | Type Code | Description |
| --------------------- | ------------------------------------------------------ | --------- | ----------- |
| 1                     | &nbsp;                                                 | &nbsp;    | &nbsp;      |
| Drug Name             | 26124                                                  | 1         | &nbsp;      |
| Full Text Description | Zetia                                                  | &nbsp;    | &nbsp;      |
| 1                     | &nbsp;                                                 | &nbsp;    | &nbsp;      |
| Drug Name             | 26124                                                  | 3         | &nbsp;      |
| Capitalized Name      | ZETIA                                                  | &nbsp;    | &nbsp;      |
| 2                     | &nbsp;                                                 | &nbsp;    | &nbsp;      |
| Routed Drug           | 26124                                                  | 1         | &nbsp;      |
| Full Text Description | Thinlets GP Lancets (Does not apply)                   | &nbsp;    | &nbsp;      |
| 3                     | &nbsp;                                                 | &nbsp;    | &nbsp;      |
| Routed Dose           | &nbsp;                                                 | &nbsp;    | &nbsp;      |
| Form Drug             | 26124                                                  | 1         | &nbsp;      |
| Full Text Description | Melatonin-Pyridoxine Oral Tablet Extended Release      | &nbsp;    | &nbsp;      |
| 4                     | &nbsp;                                                 | &nbsp;    | &nbsp;      |
| Dispensable           | &nbsp;                                                 | &nbsp;    | &nbsp;      |
| Drug                  | 26124                                                  | 1         | &nbsp;      |
| Full Text Description | Chlorpheniramine-Phenylephrine Oral Syrup 1-2.5 MG/5ML | &nbsp;    | &nbsp;      |


## Type Code

This is a 1-digit numeric field.

The Type Code indicates the type of description in the record.

4-102 MED-File v2

Published: 11/11

Revised: 08/21

Description File

Valid Values:


| ID  | Description                     | Abbreviation    |
| --- | ------------------------------- | --------------- |
| 1   | Full Textual Description        | Full Text       |
| 2   | Abbreviated Textual Description | Abbreviated Txt |
| 3   | Capitalized Name                | &nbsp;          |
| 4   | Salt Name                       | &nbsp;          |
| 5   | Alternate Name                  | &nbsp;          |


For more information about the Type Code, go to Chapter 2: Editorial Policies.

# Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note All Transaction CDs are blank for Total Databases.

# Description

This is a 250-character field.

The Description field provides a textual description of the concept as defined by the Concept Type, Country Code, Concept ID, and Type Code.

Example:


| Concept Type          | Concept ID                           | Type Code | Description |
| --------------------- | ------------------------------------ | --------- | ----------- |
| 1                     | &nbsp;                               | &nbsp;    | &nbsp;      |
| Drug Name             | 26124                                | 1         | &nbsp;      |
| Full Text Description | Zetia                                | &nbsp;    | &nbsp;      |
| 1                     | &nbsp;                               | &nbsp;    | &nbsp;      |
| Drug Name             | 26124                                | 3         | &nbsp;      |
| Capitalized Name      | ZETIA                                | &nbsp;    | &nbsp;      |
| 2                     | &nbsp;                               | &nbsp;    | &nbsp;      |
| Routed Drug           | 26124                                | 1         | &nbsp;      |
| Full Text Description | Thinlets GP Lancets (Does not apply) | &nbsp;    | &nbsp;      |


Documentation Manual 4-103

Published: 11/11

Revised: 08/21

Data Elements


| Concept Type            | Concept ID | Type Code               | Description                                            |
| ----------------------- | ---------- | ----------------------- | ------------------------------------------------------ |
| 3 Routed Dose Form Drug | 26124      | 1 Full Text Description | Melatonin-Pyridoxine Oral Tablet Extended Release      |
| 4 Dispensable Drug      | 26124      | 1 Full Text Description | Chlorpheniramine-Phenylephrine Oral Syrup 1-2.5 MG/5ML |


## Reserve

This is a 67-character field.

The Reserve field is an unused field that may be used at a future date.

## Route File

**(MF2RTE)**

The Route File contains the fields associated with the route of administration. Specific route description data resides in the Description File (MF2DESC). The Route File includes additional historical concepts that are not reflected in the Drug Name File.

The Route File contains the following data elements:


| Code | Data Element Name | Record Position | Type/Length | Picture  |
| ---- | ----------------- | --------------- | ----------- | -------- |
| V001 | Concept Type      | 1-5             | N/5         | 9(5)     |
| V006 | Country Code      | 6-7             | N/2         | 9(2)     |
| V008 | Concept ID        | 8-17            | N/10        | 9(10)    |
| V018 | Transaction CD    | 18-18           | C/1         | X(1)     |
| V019 | Status            | 19-19           | N/1         | 9(1)     |
| V020 | Link Value        | 20-29           | N/10        | 9(10)    |
| V030 | Link Date         | 30-37           | N/8         | YYYYMMDD |
| V038 | Reserve           | 38-48           | C/11        | X(11)    |


**Note** The shaded rows represent the unique key into the file.

## Concept Type

This is a 5-digit numeric field.

The Concept Type defines the type of concept that is represented by the Concept ID.

4-104 MED-File v2

Published: 11/11

Revised: 08/21

Route File

Valid Values:


| Value | Description           |
| ----- | --------------------- |
| 00001 | Drug Name             |
| 00002 | Routed Drug           |
| 00003 | Routed Dose Form Drug |
| 00004 | Dispensable Drug      |
| 00005 | GPI                   |
| 00006 | GPPC5                 |
| 00007 | NDC-UPC-HRI           |
| 00008 | Route                 |
| 00009 | Dose Form             |
| 00221 | Dose Form Drug        |
| 00222 | Strength-Strength UOM |


Note  
00008 (Route) is the only value used in this file.

## Country Code

This is a 2-digit numeric field.

The Country Code represents the country to which a Route is specific.

Note  
01 (USA) is the only value in use at this time.

## Concept ID

This is a 10-digit numeric field.

The Concept ID identifies the Route.

## Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |


Documentation Manual 4-105  
Published: 11/11  
Revised: 08/21

Data Elements


| Value | Description |
| ----- | ----------- |
| D     | Delete      |
| b'    | No Change   |


Note  
All Transaction CDs are blank for Total Databases.

# Status

This is a 1-character field.

The Status defines the current state of the Route concept.

Valid Values:


| Value | Description                                    | Abbreviation   |
| ----- | ---------------------------------------------- | -------------- |
| 1     | Active Concept with Active Associated Products | Active w/Prod  |
| 2     | Active w/Assc Prd Inactive <48 Months          | Active w/Inact |
| 3     | Inactive w/Assc Prd Inactive >48 Months        | Inactive w/Prd |
| 4     | Inactive w/no Assc. Products                   | Inac w/o Prd   |


# Link Value

This is a 10-digit numeric field.

The Link Value identifies the new Concept ID that replaces the Concept ID in this record.

Note  
The Link Value for this file is not in use at this time. For more information, go to Chapter 5, "Applications".

# Link Date

This is an 8-digit numeric field.

The Link Date represents the date the Concept ID was replaced by the Link Value.

Note  
The Link Date for this file is not in use at this time. For more information, go to Chapter 5, "Applications".

4-106 MED-File v2

Published: 11/11

Revised: 08/21

Dose Form File

# Reserve

This is an 11-digit numeric field.

The Reserve field is an unused field that may be used at a future date.

# Dose Form File

(MF2FRM)

The Dose Form File contains the fields associated with the dosage form. Specific dosage form description data resides in the Description File (MF2DESC). The Dose Form File includes additional historical concepts that are not reflected in the Drug Name File.

The Dose Form File contains the following data elements:


| Code | Data Element Name | Record Position | Type/Length | Picture  |
| ---- | ----------------- | --------------- | ----------- | -------- |
| W001 | Concept Type      | 1-5             | N/5         | 9(5)     |
| W006 | Country Code      | 6-7             | N/2         | 9(2)     |
| W008 | Concept ID        | 8-17            | N/10        | 9(10)    |
| W018 | Transaction CD    | 18-18           | C/1         | X(1)     |
| W019 | Status            | 19-19           | N/1         | 9(1)     |
| W020 | Link Value        | 20-29           | N/10        | 9(10)    |
| W030 | Link Date         | 30-37           | N/8         | YYYYMMDD |
| W038 | Reserve           | 38-48           | C/11        | X(11)    |


Note The shaded rows represent the unique key into the file.

# Concept Type

This is a 5-digit numeric field.

The Concept Type defines the type of concept that is represented by the Concept ID.

Valid Values:


| Value | Description           |
| ----- | --------------------- |
| 00001 | Drug Name             |
| 00002 | Routed Drug           |
| 00003 | Routed Dose Form Drug |
| 00004 | Dispensable Drug      |


Documentation Manual 4-107

Published: 11/11

Revised: 08/21

Data Elements


| Value | Description           |
| ----- | --------------------- |
| 00005 | GPI                   |
| 00006 | GPPC5                 |
| 00007 | NDC-UPC-HRI           |
| 00008 | Route                 |
| 00009 | Dose Form             |
| 00221 | Dose Form Drug        |
| 00222 | Strength-Strength UOM |


Note 00009 (Dose Form) is the only value used in this file.

## Country Code

This is a 2-digit numeric field.

The Country Code represents the country to which a Dose Form is specific.

Note 01 (USA) is the only value in use at this time.

## Concept ID

This is a 10-digit numeric field.

The Concept ID identifies the Dose Form.

## Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note All Transaction CDs are blank for Total Databases.

4-108 MED-File v2

Published: 11/11

Revised: 08/21

Dose Form File

# Status

This is a 1-digit numeric field.

The Status defines the current state of the Dose Form concept.

Valid Values:


| Value | Description                                    | Abbreviation   |
| ----- | ---------------------------------------------- | -------------- |
| 1     | Active Concept with Active Associated Products | Active w/Prod  |
| 2     | Active w/Assc Prd Inactive <48 Months          | Active w/Inact |
| 3     | Inactive w/Assc Prd Inactive >48 Months        | Inactive w/Prd |
| 4     | Inactive w/no Assc. Products                   | Inac w/o Prd   |


# Link Value

This is a 10-digit numeric field.

The Link Value identifies the new Concept ID that replaces the Concept ID in this record.

Note  
The Link Value for this file is not in use at this time. For more information, go to Chapter 5, "Applications".

# Link Date

This is an 8-digit numeric field.

The Link Date represents the date the Concept ID was replaced by the Link Value.

Note  
The Link Date for this file is not in use at this time. For more information, go to Chapter 5, "Applications".

# Reserve

This is an 11-character field.

The Reserve field is an unused field that may be used at a future date.

Documentation Manual 4-109

Published: 11/11

Revised: 08/21

Data Elements

# Strength-Strength Unit of Measure File

(MF2STUOM)

The Strength-Strength Unit of Measure File contains the fields associated with a strength and strength unit-of-measure. The strength and strength unit-of-measure are included as individual attributes. A description of the Concept ID resides in the Description File (MF2DESC) and represents the combination of the strength and strength unit-of-measure. The Strength-Strength Unit of Measure File includes additional historical concepts that are not reflected in the Drug Name File.

The Strength-Strength Unit of Measure File contains the following data elements:


| Code | Data Element Name        | Record Position | Type/Length | Picture  |
| ---- | ------------------------ | --------------- | ----------- | -------- |
| X001 | Concept Type             | 1-5             | N/5         | 9(5)     |
| X006 | Country Code             | 6-7             | N/2         | 9(2)     |
| X008 | Concept ID               | 8-17            | N/10        | 9(10)    |
| X018 | Transaction CD           | 18-18           | C/1         | X(1)     |
| X019 | Strength                 | 19-33           | C/15        | X(15)    |
| X034 | Strength Unit-of-Measure | 34-48           | C/15        | X(15)    |
| X049 | Status                   | 49-49           | N/1         | 9(1)     |
| X050 | Link Value               | 50-59           | N/10        | 9(10)    |
| X060 | Link Date                | 60-67           | N/8         | YYYYMMDD |
| X068 | Reserve                  | 68-96           | C/29        | X(29)    |


Note

The shaded rows represent the unique key into the file.

# Concept Type

This is a 5-digit numeric field.

The Concept Type defines the type of concept that is represented by the Concept ID.

Valid Values:


| Value | Description           |
| ----- | --------------------- |
| 00001 | Drug Name             |
| 00002 | Routed Drug           |
| 00003 | Routed Dose Form Drug |


4-110 MED-File v2

Published: 11/11

Revised: 08/21

Strength-Strength Unit of Measure File


| Value | Description           |
| ----- | --------------------- |
| 00004 | Dispensable Drug      |
| 00005 | GPI                   |
| 00006 | GPPC5                 |
| 00007 | NDC-UPC-HRI           |
| 00008 | Route                 |
| 00009 | Dose Form             |
| 00221 | Dose Form Drug        |
| 00222 | Strength-Strength UOM |


Note 00222 (Strength-Strength UOM) is the only value used in this file.

# Country Code

This is a 2-digit numeric field.

The Country Code represents the country to which a Strength-Strength UOM is specific.

Note 01 (USA) is the only value in use at this time.

# Concept ID

This is a 10-digit numeric field.

The Concept ID identifies the Strength-Strength Unit of Measure.

# Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Documentation Manual 4-111

Published: 11/11

Revised: 08/21

Data Elements

Note  
All Transaction CDs are blank for Total Databases.

## Strength

This is a 15-character field.

The Strength is a character representation of the product's ingredient strength. When combined with the Strength Unit of Measure, it represents the dosage strength as provided by the manufacturer.

## Strength Unit-Of-Measure

This is a 15-character field.

The Strength Unit Of Measure, when combined with the Strength, represents the dosage strength as provided by the manufacturer.

## Status

This is a 1-digit numeric field.

The Status defines the current state of the Strength-Strength UOM concept.

Valid Values:


| Value | Description                                    | Abbreviation   |
| ----- | ---------------------------------------------- | -------------- |
| 1     | Active Concept with Active Associated Products | Active w/Prod  |
| 2     | Active w/Assc Prd Inactive <48 Months          | Active w/Inact |
| 3     | Inactive w/Assc Prd Inactive >48 Months        | Inactive w/Prd |
| 4     | Inactive w/no Assc. Products                   | Inac w/o Prd   |


## Link Value

This is a 10-digit numeric field.

The Link Value identifies the new Concept ID that replaces the Concept ID in this record.

Note  
The Link Value for this file is not in use at this time. For more information, go to Chapter 5, "Applications".

4-112 MED-File v2

Published: 11/11

Revised: 08/21

Drug Concept ID to Ingredient Set ID File

# Link Date

This is an 8-digit numeric field.

The Link Date represents the date the Concept ID was replaced by the Link Value.

Note  
The Link Date for this file is not in use at this time. For more information, go to Chapter 5, "Applications".

# Reserve

This is a 29-character field.

The Reserve field is an unused field that may be used at a future date.

# Drug Concept ID to Ingredient Set ID File

(MF2SET)

The Drug Concept ID to Ingredient Set ID File associates ingredients to both the Dispensable Drug and to the NDC-UPC-HRI. The Drug Concept ID to Ingredient Set ID File includes additional historical concepts that are not reflected in the Drug Name File.

Note  
The Dispensable Drug and the Drug Descriptor are one and the same. The terms may be used interchangeably in this and other Wolters Kluwer documents.

Note  
In the absence of ingredient information, or when there is conflicting ingredient information, the Ingredient Set ID will be "0000000000".

The Drug Concept ID to Ingredient Set ID File contains the following data elements:


| Code | Data Element Name | Record Position | Type/Length | Picture |
| ---- | ----------------- | --------------- | ----------- | ------- |
| Y001 | Concept Type      | 1-5             | N/5         | 9(5)    |
| Y006 | Country Code      | 6-7             | N/2         | 9(2)    |
| Y008 | Concept ID        | 8-27            | C/20        | X(20)   |
| Y028 | Ingredient Set ID | 28-37           | N/10        | 9(10)   |
| Y038 | Transaction CD    | 38-38           | C/1         | X       |


Documentation Manual 4-113

Published: 11/11

Revised: 08/21

Data Elements


| Code | Data Element Name            | Record Position | Type/Length | Picture |
| ---- | ---------------------------- | --------------- | ----------- | ------- |
| Y039 | Representative Set Indicator | 39-39           | C/1         | X       |
| Y040 | Reserve                      | 40-64           | C/25        | X(25)   |


Note  
The shaded rows represent the unique key into the file.

# Concept Type

This is a 5-digit numeric field.

The Concept Type defines the type of concept that is represented by the Concept ID.

Valid Values:


| Value | Description           |
| ----- | --------------------- |
| 00001 | Drug Name             |
| 00002 | Routed Drug           |
| 00003 | Routed Dose Form Drug |
| 00004 | Dispensable Drug      |
| 00005 | GPI                   |
| 00006 | GPPC5                 |
| 00007 | NDC-UPC-HRI           |
| 00008 | Route                 |
| 00009 | Dose Form             |
| 00221 | Dose Form Drug        |
| 00222 | Strength-Strength UOM |


Note  
00004 (Dispensable Drug), and 00007 (NDC-UPC-HRI) are the only values used in this file.

# Country Code

This is a 2-digit numeric field.

The Country Code represents the country to which a drug concept is specific.

Note  
01 (USA) is the only value in use at this time.

4-114 MED-File v2

Published: 11/11

Revised: 08/21

Drug Concept ID to Ingredient Set ID File

# Concept ID

This is a 20-character field.

The Concept ID identifies the drug concept, either a Dispensable Drug or a NDC-UPC-HRI. A description of the Dispensable Drug value is available in the Description File (MF2DESC).

# Ingredient Set ID

This is a 10-digit numeric field.

The Ingredient Set ID represents the collection of active and significant inactive ingredients of a product formulation.


| Note | In the absence of ingredient information, or when there is conflicting ingredient information, the Ingredient Set ID will be “0000000000”.                                                   |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Note | For outsourcing facility products, the ingredient set ID represents only the active ingredients for a product formulation. Significant inactive ingredients are excluded for these products. |


# Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note All Transaction CDs are blank for Total Databases.

# Representative Set Indicator

This is a 1-character field.

Documentation Manual 4-115

Published: 11/11

Revised: 08/21

Data Elements

The Representative Set Indicator designates whether the Concept ID has a unique Ingredient Set ID or if a representative Ingredient Set ID is assigned.

Valid Values:


| Value | Description            | Definition                                                                 |
| ----- | ---------------------- | -------------------------------------------------------------------------- |
| 0     | Unassigned             | Multiple Ingredient Set IDs exist and no Ingredient Set ID is assigned     |
| 1     | Exact Match Set        | One Ingredient Set ID exists                                               |
| 2     | Representative Set     | Multiple Ingredient Set IDs exist and one Ingredient Set ID is assigned    |
| 3     | Set Cannot be Assigned | Multiple ingredient sets exist and an ingredient set will not be assigned. |


## Reserve

This is a 25-character field.

The Reserve field is an unused field that may be used at a future date.

## Ingredient Set ID to Ingredient ID File

## (MF2INGS)

The Ingredient Set ID to Ingredient ID File contains the individual Ingredient IDs that are associated to the Ingredient Set ID. In addition, this file has a flag that designates each Ingredient Identifier as either an active or inactive ingredient.

The Ingredient Set ID to Ingredient ID File contains the following data elements:


| Code | Data Element Name               | Record Position | Type/Length | Picture |
| ---- | ------------------------------- | --------------- | ----------- | ------- |
| Z001 | Ingredient Set ID               | 1-10            | N/10        | 9(10)   |
| Z011 | Ingredient Identifier           | 11-20           | N/10        | 9(10)   |
| Z021 | Active/Inactive Ingredient Flag | 21-21           | C/1         | X       |
| Z022 | Transaction CD                  | 22-22           | C/1         | X       |
| Z023 | Reserve                         | 23-32           | C/10        | X(10)   |


Note The shaded rows represent the unique key into the file.

## Ingredient Set ID

This is a 10-digit numeric field.

4-116 MED-File v2

Published: 11/11

Revised: 08/21

Ingredient Set ID to Ingredient ID File

The Ingredient Set ID represents the collection of active and significant inactive ingredients of a product formulation.

Note  
For outsourcing facility products, the ingredient set ID represents only the inactive ingredients for a product formulation. Significant inactive ingredients are excluded for these products.

# Ingredient Identifier

This is a 10-digit numeric field.

The Ingredient Identifier represents a unique combination of Ingredient Drug ID, Ingredient Strength Value, and Ingredient Strength UOM (Combined).

Example:


| Ingredient Set ID | Ingredient ID | Drug ID/ Ingredient Drug Name | Ingredient Strength | Ingredient Strength Unit of Measure (Combined) |
| ----------------- | ------------- | ----------------------------- | ------------------- | ---------------------------------------------- |
| 19588             | 30738         | 4004 ATORVASTATIN CALCIUM     | 10                  | MG                                             |
| 43580             | 16722         | 2024 AMLODIPINE BESYLATE      | 5                   | MG                                             |
| &nbsp;            | 30738         | 4004 ATORVASTATIN CALCIUM     | 10                  | MG                                             |


# Active/Inactive Ingredient Flag

This is a 1-character field.

The Active/Inactive Ingredient Flag is a one-character flag that indicates whether the ingredient is an active ingredient or an inactive ingredient.

Valid Values:


| ID  | Description         |
| --- | ------------------- |
| A   | Active Ingredient   |
| I   | Inactive Ingredient |


Documentation Manual 4-117

Published: 11/11

Revised: 08/21

Data Elements

Note  
Only those ingredients that are considered clinically significant are generally included. For example, alcohol and Tartrazine. Other inactive ingredient information is generally not included. A list of significant inactive ingredients is available upon request.

- In compounded products from outsourcing facilities, only active ingredients are included. All inactive ingredients will be excluded. Users of products manufactured by outsourcing facilities should understand that comprehensive allergy screening and alerting for allergenic inactive ingredients will NOT occur. Products from outsourcing facilities may be identified using the limited distribution code of 03.

# Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note  
All Transaction CDs are blank for Total Databases.

# Reserve

This is a 10-character field.

The Reserve field is an unused field that may be used at a future date.

# Ingredient ID to Drug-Strength File

(MF2STR)

The Ingredient ID to Drug-Strength File contains the strengths and strength unit of measure of each Ingredient Identifier. In addition, this file contains the strength unit of measure field in both combined and individual components so that volume unit of measures can be represented.

4-118 MED-File v2

Published: 11/11

Revised: 08/21

Ingredient ID to Drug-Strength File

The Ingredient ID to Drug-Strength File contains the following data elements:.


| Code | Data Element Name                    | Record Position | Type/Length | Picture   |
| ---- | ------------------------------------ | --------------- | ----------- | --------- |
| 1001 | Ingredient Identifier                | 1-10            | N/10        | 9(10)     |
| 1011 | Reserve-1                            | 11-12           | C/2         | X(2)      |
| 1013 | Transaction CD                       | 13-13           | C/1         | X         |
| 1014 | Ingredient Drug ID                   | 14-23           | N/10        | 9(10)     |
| 1024 | Ingredient Strength Value            | 24-36           | N/13        | 9(8)V9(5) |
| 1037 | Ingredient Strength UOM (combined)   | 37-47           | C/11        | X(11)     |
| 1048 | Ingredient Strength UOM (individual) | 48-58           | C/11        | X(11)     |
| 1059 | Volume Value                         | 59-71           | N/13        | 9(8)V9(5) |
| 1072 | Volume Unit of Measure               | 72-82           | C/11        | X(11)     |
| 1083 | Reserve-2                            | 83-112          | C/30        | X(30)     |


Note  
The shaded row represents the unique key into the file.

# Ingredient Identifier

This is a 10-digit numeric field.

The Ingredient Identifier represents a unique combination of Ingredient Drug ID, Ingredient Strength Value, and Ingredient Strength UOM (Combined).

# Reserve-1

This is a 2-character field.

The Reserve-1 field is an unused field that may be used at a future date.

# Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |


Documentation Manual 4-119

Published: 11/11

Revised: 08/21

Data Elements


| Value | Description |
| ----- | ----------- |
| D     | Delete      |
| b'    | No Change   |


Note  
All Transaction CDs are blank for Total Databases.

# Ingredient Drug ID

This is a 10-digit numeric field.

The Ingredient Drug ID represents a unique ingredient description. It is system-generated and contains no logic.

# Ingredient Strength Value

This is a 13-digit numeric field.

The Ingredient Strength Value is a numeric value representing the metric strength for a product, where available. In addition, this value may sometimes indicate a ratio strength or percentage.

# Ingredient Strength UOM (combined)

This is an 11-character field.

The Ingredient Strength UOM (combined) is a combined character representation describing the units of the Ingredient Strength Value. It may be a percentage, or part of a ratio strength. The combined value will include volume units, if applicable, with slashes (for example, MG/5ML).

# Ingredient Strength UOM (individual)

This is an 11-character field.

The Ingredient Strength Unit of Measure (individual) is an individual character representation describing the units of the Ingredient Strength Value. It may be a percentage, or part of a ratio strength.

Note  
The Ingredient Strength UOM (individual) is not in use at this time.

4-120 MED-File v2

Published: 11/11

Revised: 08/21

Ingredient Drug File

# Volume Value

This is a 13-digit numeric field.

The Volume Value is a numeric value representing the volume used in the Ingredient Strength Unit of Measure (combined), when applicable.

Note  
The Volume Value is not in use at this time.

# Volume Unit of Measure

This is an 11-character field.

The Volume Unit of Measure is an individual character representation describing the volume represented in the Ingredient Strength Value, when applicable.

Note  
The Volume Unit of Measure is not in use at this time.

# Reserve-2

This is a 30-character field.

The Reserve-2 field is an unused field that may be used at a future date.

# Ingredient Drug File

(MF2IDRG)

The Ingredient Drug File is a dictionary of generic ingredients with association to common identifiers for the ingredients.

The Ingredient Drug File contains the following data elements:


| Code | Data Element Name     | Record Position | Type/Length | Picture |
| ---- | --------------------- | --------------- | ----------- | ------- |
| 2001 | Ingredient Drug ID    | 1-10            | N/10        | 9(10)   |
| 2011 | Transaction CD        | 11-11           | C/1         | X       |
| 2012 | CAS Number            | 12-31           | C/20        | X(20)   |
| 2032 | Knowledge Base Code 7 | 32-38           | N/7         | 9(7)    |
| 2039 | Reserve-1             | 39-41           | C/3         | X(3)    |
| 2042 | Ingredient Drug Name  | 42-101          | C/60        | X(60)   |
| 2102 | Generic ID            | 102-111         | C/10        | X(10)   |
| 2112 | Reserve-2             | 112-128         | C/17        | X(17)   |


Documentation Manual 4-121

Published: 11/11

Revised: 08/21

Data Elements

Note  
The shaded row represents the unique key into the file.

# Ingredient Drug ID

This is a 10-digit numeric field.

The Ingredient Drug ID represents a unique ingredient. It is system-generated and contains no logic.

# Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note  
All Transaction CDs are blank for Total Databases.

# CAS Number

This is a 20-character field.

When available, the Chemical Abstracts Service (CAS) Registry Numbers are unique identifiers for chemical substances. A CAS Registry Number itself has no inherent chemical significance, but it does provide an unambiguous way to identify a chemical substance or molecular structure when there are many possible systematic, generic, or proprietary names available.

# Knowledge Base Code 7

This is a 7-digit numeric field.

The Knowledge Base Drug Code 7 (KDC-7) is a code that Wolters Kluwer uses that defines ingredients. For an Ingredient Drug ID that does not have a KDC-7, this field will be zero-filled.

4-122 MED-File v2

Published: 11/11

Revised: 08/21

Secondary Alternate ID File

Note  
The KDC is not a hierarchical value and does not correlate to the GPI in any way.

Reserve-1  
This is a 3-character field.  
The Reserve-1 field is an unused field that may be used at a future date.

Ingredient Drug Name  
This is a 60-character field.  
The Ingredient Drug Name field is an upper-case ingredient name.

Generic ID  
This is a 10-character field.  
The Generic ID field is a proprietary Wolters Kluwer value for a specific generic ingredient.

Reserve-2  
This is a 26-character field.  
The Reserve-2 field is an unused field that may be used at a future date.

Secondary Alternate ID File  
(MF2SEC)  
The Secondary Alternate ID File contains the secondary and any alternate marketplace IDs for a packaged drug.

For example, a drug may have an NDC, but may also have a UPC. This file links the IDs together.

Currently, alternate IDs are either NDCs, UPCs, or HRIs. Additional ID types may be used in the future.

Documentation Manual 4-123  
Published: 11/11  
Revised: 08/21

Data Elements

The Secondary Alternate ID File contains the following data elements:


| Code | Data Element Name              | Record Position | Type/Length | Picture |
| ---- | ------------------------------ | --------------- | ----------- | ------- |
| 3001 | External Drug ID (NDC-UPC-HRI) | 1-20            | C/20        | X(20)   |
| 3021 | External Drug ID Format Code   | 21-21           | C/1         | X       |
| 3022 | Alternate Drug ID              | 22-41           | C/20        | X(20)   |
| 3042 | Alternate Drug ID Format Code  | 42-42           | C/1         | X       |
| 3043 | Transaction CD                 | 43-43           | C/1         | X       |
| 3044 | Reserve                        | 44-64           | C/21        | X(21)   |


Note  
The shaded rows represent the unique key into the file.

## External Drug ID (NDC-UPC-HRI)

This is a 20-character field.

NDCs, UPCs, and HRIs are 10-character codes used to identify drug products. Surgical supplies and non-prescription drug products may have an NDC and an HRI or UPC according to the standards set forth by the Uniform Product Code Council, Inc. These codes are converted to eleven characters according to NCPDP standards.

Note  
The External Drug ID and the Alternate Drug ID may be the same value with different format codes.

## External Drug ID Format Code

This is a 1-character field.

The External Drug ID Format Code identifies the format of the NDC-UPC-HRI. Use the External Drug ID Format Code with an NDC, UPC, or HRI to determine the following:

- where to place dashes when formatting for display
- how to convert from the 10- to 11-character format
- how to convert from the 11- to 10-character format

4-124 MED-File v2

Published: 11/11

Revised: 08/21

Secondary Alternate ID File

Valid Values:


| Code | Represents | ID Type |
| ---- | ---------- | ------- |
| 1    | 4-4-2      | NDC     |
| 2    | 5-3-2      | NDC     |
| 3    | 5-4-1      | NDC     |
| 4    | 4-6        | HRI     |
| 5    | 5-5        | UPC     |
| 6    | 5-4-2      | NDC     |


The codes convert as follows:


| NDC                  | &nbsp;      | NCPDP Standard 11-character NDC | 11-character NDC (with hyphens) | ID Format Code |
| -------------------- | ----------- | ------------------------------- | ------------------------------- | -------------- |
| 4-4-2 (9999-9999-99) | Converts To | 5-4-2 (09999999999)             | 09999-9999-99                   | 1              |
| 5-3-2 (99999-999-99) | &nbsp;      | 5-4-2 (99999099999)             | 99999-0999-99                   | 2              |
| 5-4-1 (99999-9999-9) | &nbsp;      | 5-4-2 (99999999909)             | 99999-9999-09                   | 3              |
| 5-4-2 (99999-9999-99 | &nbsp;      | 5-4-2 (99999999999)             | 99999-9999-99                   | 6              |
| 4-6 (9999-999999)    | &nbsp;      | 5-6 (09999999999)               | 9999-999999                     | 4              |
| 5-5 (99999-99999)    | &nbsp;      | 5-6 (99999099999)               | 99999-99999                     | 5              |


## Alternate Drug ID

This is a 20-character field.

NDCs, UPCs, and HRIs are 10-character codes used to identify drug products. Surgical supplies and non-prescription drug products may have an NDC and an HRI or UPC according to the standards set forth by the Uniform Product Code Council, Inc. These codes are converted to eleven characters according to NCPDP standards.

**Note** The External Drug ID and the Alternate Drug ID may be the same value with different format codes.

## Alternate Drug ID Format Code

This is a 1-character field.

Documentation Manual 4-125  
Published: 11/11  
Revised: 08/21

Data Elements

The Alternate Drug ID Format Code identifies the format of the NDC-UPC-HRI [Data Element Code 6001]. Use the Alternate Drug ID Format Code with an NDC, UPC, or HRI to determine:

- where to place dashes when formatting for display
- how to convert from the 10 to 11-character format
- how to convert from the 11 to 10-character format

Valid Values:


| Code | Represents | ID Type |
| ---- | ---------- | ------- |
| 1    | 4-4-2      | NDC     |
| 2    | 5-3-2      | NDC     |
| 3    | 5-4-1      | NDC     |
| 4    | 4-6        | HRI     |
| 5    | 5-5        | UPC     |
| 6    | 5-4-2      | NDC     |


The codes convert as follows:


| NDC                  | &nbsp;      | NCPDP Standard 11-character NDC | 11-character NDC (with hyphens) | ID Type Code | ID Format Code |
| -------------------- | ----------- | ------------------------------- | ------------------------------- | ------------ | -------------- |
| 4-4-2 (9999-9999-99) | Converts to | 5-4-2 (09999999999)             | 09999-9999-99                   | 1            | 1              |
| 5-3-2 (99999-999-99) | &nbsp;      | 5-4-2 (99999099999)             | 99999-0999-99                   | 1            | 2              |
| 5-4-1 (99999-9999-9) | &nbsp;      | 5-4-2 (99999999909)             | 99999-9999-09                   | 1            | 3              |
| 5-4-2 (99999-9999-99 | &nbsp;      | 5-4-2 (99999999999)             | 99999-9999-99                   | 1            | 6              |
| 4-6 (9999-999999)    | &nbsp;      | 5-6 (09999999999)               | 9999-999999                     | 2            | 4              |
| 5-5 (99999-99999)    | &nbsp;      | 5-6 (99999099999)               | 99999-99999                     | 2 or 3       | 5              |


## Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

4-126 MED-File v2  
Published: 11/11  
Revised: 08/21

Reference Name File

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note  
All Transaction CDs are blank for Total Databases.

## Reserve

This is a 21-character field.

The Reserve field is an unused field that may be used at a future date.

## Reference Name File

(MF2RNM)

The Reference Name File associates a Concept ID to its generically-named Concept ID. Concept IDs for brands can have a Medi-Span Reference Flag to indicate that the brand concept can be used to construct a generic name with a brand name reference. For example, Ibuprofen Oral Tablet 400 MG (Motrin).

The Reference Name File contains the following data elements:


| Code | Data Element Name         | Record Position | Type/Length | Picture |
| ---- | ------------------------- | --------------- | ----------- | ------- |
| 4001 | Concept Type              | 1-5             | N/5         | 9(5)    |
| 4006 | Country Code              | 6-7             | N/2         | 9(2)    |
| 4008 | Concept ID                | 8-17            | N/10        | 9(10)   |
| 4018 | ID for Generic Named Drug | 18-27           | N/10        | 9(10)   |
| 4028 | Transaction CD            | 28-28           | C/1         | X       |
| 4029 | Medi-Span Reference Flag  | 29-29           | C/1         | X       |
| 4030 | Reserve                   | 30-48           | C/19        | X(19)   |


Note  
The shaded rows represent the unique key into the file.

Documentation Manual 4-127

Published: 11/11

Revised: 08/21

Data Elements

## Concept Type

This is a 5-digit numeric field.

The Concept Type defines the type of concept that is represented by the Concept ID.

Valid Values:


| Value | Description           |
| ----- | --------------------- |
| 00001 | Drug Name             |
| 00002 | Routed Drug           |
| 00003 | Routed Dose Form Drug |
| 00004 | Dispensable Drug      |
| 00005 | GPI                   |
| 00006 | GPPC5                 |
| 00007 | NDC-UPC-HRI           |
| 00008 | Route                 |
| 00009 | Dose Form             |
| 00221 | Dose Form Drug        |
| 00222 | Strength-Strength UOM |


Note  
00001 (Drug Name), 00002 (Routed Drug), and 00004 (Dispensable Drug) are the only values used in this file.

## Country Code

This is a 2-digit numeric field.

The Country Code represents the country to which a drug concept is specific.

Note  
01 (USA) is the only value in use at this time.

## Concept ID

This is a 10-digit numeric field.

The Concept ID identifies a Drug Name, Routed Drug, or Dispensable Drug.

Note  
The Dispensable Drug and the Drug Descriptor are the same. The terms may be used interchangeably in this and other Wolters Kluwer documents.

4-128 MED-File v2

Published: 11/11

Revised: 08/21

Reference Name File

Note  
The Drug Names, Routed Drugs, and Dispensable Drugs represented in this file reflect those available in the Drug Name File through their association to the DDIDs in the Drug Name File. The SDI Name File, Routed Drug File, and Dispensable Drug File include records that are not included here.

# ID for Generic Named Drug

This is a 10-digit numeric field.

The ID for Generic Named Drug is a Concept ID representing a generically-named Drug Name, Routed Drug, or Dispensable Drug.

# Transaction CD

This is a 1-character field.

The Transaction CD indicates the file activity that last occurred for a record.

The current values are:


| Value | Description |
| ----- | ----------- |
| A     | Add         |
| C     | Change      |
| D     | Delete      |
| b'    | No Change   |


Note  
All Transaction CDs are blank for Total Databases.

# Medi-Span Reference Flag

This is a 1-character field.

The Medi-Span Reference Flag is assigned by Wolters Kluwer to identify a reference brand name drug for the records that have the same 14-character GPI value. There may be zero, one, or many brand names designated as reference brand name drugs even though they share the same 14-character GPI.

Note  
Drugs assigned to partial GPIs are not designated as reference brand name drugs.

Documentation Manual 4-129

Published: 11/11

Revised: 08/21

Data Elements

Valid Values:


| Value | Description                   |
| ----- | ----------------------------- |
| N     | Is not a reference brand name |
| Y     | Is a reference brand name     |


## Reserve

This is a 19-character field.

The Reserve field is an unused field that may be used at a future date.

4-130 MED-File v2

Published: 11/11

Revised: 08/21

# Chapter 5: Applications

## In This Chapter

- Introduction
- Storing Terminology
- Maintaining Terminology
- Processing the Error Correct File
- Maintaining Price History
- Displaying Drugs and Creating Drug Selection Lists
- Retrieving Routed Drug(s) for a Drug Name
- Retrieving Routed Dose Form Drug(s) for a Drug Name
- Retrieving Dose Form Drug(s) for a Drug Name
- Retrieving Dispensable Drug(s) for a Drug Name
- Retrieving Routed Dose Form Drug(s) for a Routed Drug
- Retrieving Dispensable Drug(s) for a Routed Drug
- Retrieving Dispensable Drug(s) for a Routed Dose Form Drug
- Retrieving Dispensable Drug(s) for a Dose Form Drug
- Associating Brand and Generic Drug Names
- Associating Brand and Generic Routed Drugs
- Associating Brand and Generic Dispensable Drugs
- Constructing Alternative Drug Names
- Associating Dosage Form in the Drug Name File to Dose Form in the Description File
- Associating Route of Administration in the Drug Name File to Route in the Description File
- Identifying Ingredients for a Dispensable Drug
- Identifying Ingredients for an NDC-UPC-HRI
- Associating New and Old NDC-UPC-HRIs
- Associating New and Old Dispensable Drugs (DDIDs)
- Retrieving KDCs for a Dispensable Drug
- Retrieving GPIs for a Dispensable Drug
- Identifying Therapeutic Alternatives Using the TC-GPI Name File
- Creating Nine-Character GPPCs

## Introduction

This chapter highlights some of the many algorithms and recommendations for deploying MED-File v2 in your end-user applications. The many and varied functions performed by the user will likely determine what and how certain data is deployed, what data you store in a database or patient record, and what is made available to users in the form of applications and reporting. In some

Applications

instances, the presentation of information to the user is critical to patient safety and is addressed in the chapter, as applicable.


| Note | The terms Drug Descriptor Identifier and Dispensable Drug Identifier, also known as the DDID are used interchangeably in this and other documentation. In some files, the ID is a six digit number. In other files, the DDID is a 10 digit number. The significant digits of the number are the same. |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Note | Examples in this chapter are for illustrative purposes only and may not reflect current data.                                                                                                                                                                                                         |


# Storing Terminology

A critical step in deploying MED-File v2 in your applications is establishing processes to store and maintain terminology. This is especially important when storing information in the patient profile/electronic medical record. However, it is also applicable to other applications, even if the operations are not directly related to patient care.

When the following terminologies are stored, the description should be stored in addition to the code/value/identifier that represents it:

- Dispensable Drug ID (DDID)
- Other name-based drug concepts such as the Drug Name, Routed Drug, Routed Dose Form Drug, and Dose Form Drug
- Generic Product Identifier (GPI)
- Ingredients

Some of Wolters Kluwer clinical screening applications utilize the Knowledge Base Drug Code (KDC). Therefore, storing this value is also recommended.

In some cases, the NDC-UPC-HRI is necessary to uniquely identify the specific drug product that was dispensed and/or administered to the patient.

With proper storage and maintenance of these terminologies:

- the severity or impact of data entry revisions by Wolters Kluwer can be quickly identified and reviewed on a patient-by-patient/time-of-therapy basis.
- removal of a drug product from the Drug Name File when a name is no longer associated with the drug product currently on the market, will not cause a patient profile to become unusable due to an unidentifiable

5-2 MED-File v2

Published: 11/11

Revised: 07/21

Maintaining Terminology

drug. The drug’s generic name or product name will be available in the patient profile for historical reference.

- an additional safety feature can be implemented when reviewing a patient profile by comparing the description generated by the stored value with the stored drug description. If the two descriptions are not the same, the reviewer can determine if an error exists.
- inclusion of the GPI and KDC allows for simplified access to these values for clinical screening and for further review of these values during updating.

# Maintaining Terminology

## Changes to the DDID

Changes to the DDID can occur at any time. It is important to monitor these changes and manage them in your database and in patient records. For more information, see *Associating New and Old Dispensable Drugs (DDIDs)*.

In addition, data entry revisions to the DDID are reflected in the Error Correct File. The file will alert you to DDID data entry revisions so you can determine any terminology maintenance that needs to be made. For more information, see *Processing the Error Correct File*.

## Processing Old DDIDs

DDIDs will remain in the Drug Name file for up to 48 months after all associated drug products linked to that DDID have been inactive. However, DDIDs are not removed from the Dispensable Drug File after that 48 month period. In the event that you need to process records using older DDIDs, use the Dispensable Drug File.

## Changes to the GPI

GPI changes are one of two types. Each type requires you to carefully assess the impact of these changes to your database and to patient records.

Data change revisions are made at any time. MED-File v2 does not provide a new to old link. However, the changes are published by Wolters Kluwer when they occur. Contact Customer Support if you wish to subscribe to this publication.

Wolters Kluwer also performs “planned” GPI changes, usually on a semi-annual basis in April and October. The list of planned changes is published one quarter

Documentation Manual 5-3  
Published: 11/11  
Revised: 07/21

Applications

in advance and made available to all MED-File v2 customers. This list identifies the changes in GPI assignment for drugs.

## Changes to NDC-UPC-HRIs

Changes to NDC-UPC-HRIs can occur at any time. For more information, see *Associating New and Old NDC-UPC-HRIs*.

In addition, data entry revisions associated with attributes of the NDC are reflected in the Error Correct File. This file will alert you to the revisions so you can determine the impact to your applications.

## Processing the Error Correct File

The Error Correct File enables you to identify certain types of revisions that Wolters Kluwer has made to the data. The data change revision itself appears in the appropriate data file within MED-File v2. The purpose of the Error Correct File is to “flag” the data change revisions. The needs of your end-users will determine the impact of the revision and any actions that you or they may take within the application. For example, the manufacturer’s correction of a drug price may or may not be significant to the end-user’s business operations.

The following types of data entry revisions are provided in the Error Correct File:

- Drug Descriptor Identifier (aka Dispensable Drug)
- NDC-UPC-HRI
- NDC-UPC-HRI and Price Type


| Note | Wolters Kluwer recommends that all data entry revisions be reviewed before they are processed. |
| ---- | ---------------------------------------------------------------------------------------------- |


The Error Correct File is provided as part of the Incremental Update. It is not provided with a Total Replacement.

The following example illustrates how to use the Error Correct File to identify the associated record in your database.

5-4 MED-File v2

Published: 11/11

Revised: 07/21

Maintaining Price History

Example:


| Key Identifier | Unique Key  | Data Element Code | Data Element Length |
| -------------- | ----------- | ----------------- | ------------------- |
| 2              | 12345678901 | H023              | 008                 |


- Key Identifier of 2 = NDC-UPC-HRI
- Unique Key = the specific NDC-UPC-HRI
- Date Element Code H023 = Generic Product Packaging Code (GPPC)
- Data Element Length = the length of the Generic Product Packaging Code field

This record in the Error Correct File indicates that a revision has been made to the GPPC assignment for an NDC-UPC-HRI in the NDC File. The presence of this record enables you to evaluate the impact of the change by reviewing the GPPC assignment for the NDC-UPC-HIR currently in your database before applying your Incremental Update to deploy the corrected value.

## Maintaining Price History

### Updating The Price History File

MED-File v2 provides, at most, one current price for each price type supported in the product. The NDC Price File includes AWP, DP, WAC, and CMS FUL pricing information as individual records. The GPPC Price File includes AAWP and GEAP pricing information. An Effective Date is associated with each individual pricing record.

If you receive Incremental Updates, a Transaction Code is provided for each added, changed, or deleted record within that particular Incremental Update. The Transaction Code will reflect only the most recent price change during the update cycle. For example, if you receive weekly updates and the price changed multiple times from one weekly update to another, the Incremental Update that you receive will only reflect the current price at the time of the update.

> **Note** If you receive a Total Replacement, the Transaction Code will be blank.

Use the Transaction Codes as follows to maintain a price history file and to update end-user applications with the current price.

- If the Transaction Code is A (add), add the current price to your price history file.
- If the Transaction Code is C (change)

Documentation Manual 5-5

Published: 11/11

Revised: 07/21

Applications

> If the primary key matches a record in your current file, replace the current information in your file with the new information.  
> If the primary key does not match a record in your current file, add the record to your file.

- If the Transaction Code is D (delete) you may decide whether or not to delete pricing history for that record, depending on your needs and the needs of your end-users.

The Error Correct File can be used along with the NDC Price File to manage the processing of pricing records.

The example below illustrates a chronological sequence of price history maintenance.

# Sample 1

Sample January 1, 2012 Initial Load for AWP price for NDC-UPC-HRI 12345678901


| NDC-UPC-HRI | Price Type | Effective Date | Unit Price  | Transaction Code |
| ----------- | ---------- | -------------- | ----------- | ---------------- |
| 12345678901 | 3          | 20111228       | 00000009966 | A                |


Resulting Local Price History File


| NDC-UPC-HRI | Price Type | Effective Date | Unit Price  |
| ----------- | ---------- | -------------- | ----------- |
| 12345678901 | 3          | 20111228       | 00000009966 |


Sample February 1, 2012 Incremental Update for AWP price for NDC-UPC-HRI 12345678901


| NDC-UPC-HRI | Price Type | Effective Date | Unit Price  | Transaction Code |
| ----------- | ---------- | -------------- | ----------- | ---------------- |
| 12345678901 | 3          | 20120123       | 00000010097 | A                |


Resulting Local Price History File


| NDC-UPC-HRI | Price Type | Effective Date | Unit Price  |
| ----------- | ---------- | -------------- | ----------- |
| 12345678901 | 3          | 20111228       | 00000009966 |
| 12345678901 | 3          | 20120123       | 00000010097 |


Sample March 1, 2012 Incremental Update for AWP price for NDC-UPC-HRI 12345678901

5-6 MED-File v2

Published: 11/11

Revised: 07/21

Displaying Drugs and Creating Drug Selection Lists

Note  
For the purposes of this example, a corresponding record would also appear in the Error Correct File.


| NDC-UPC-HRI | Price Type | Effective Date | Unit Price  | Transaction Code |
| ----------- | ---------- | -------------- | ----------- | ---------------- |
| 12345678901 | 3          | 20120123       | 00000010077 | C                |


Resulting Local Price History File


| NDC-UPC-HRI | Price Type | Effective Date | Unit Price  |
| ----------- | ---------- | -------------- | ----------- |
| 12345678901 | 3          | 20111228       | 00000009966 |
| 12345678901 | 3          | 20120123       | 00000010077 |


Sample April 1, 2012 Incremental Update for AWP price for NDC 12345678901


| NDC-UPC-HRI | Price Type | Effective Date | Unit Price  | Transaction Code |
| ----------- | ---------- | -------------- | ----------- | ---------------- |
| 12345678901 | 3          | 20120315       | 00000010080 | A                |


Resulting Local Price History File


| NDC-UPC-HRI | Price Type | Effective Date | Unit Price  |
| ----------- | ---------- | -------------- | ----------- |
| 12345678901 | 3          | 20112228       | 00000009966 |
| 12345678901 | 3          | 20120123       | 00000010077 |
| 12345678901 | 3          | 20120315       | 00000010080 |


# Displaying Drugs and Creating Drug Selection Lists

There are several options for displaying drugs in end-user applications. The needs of the user will define the type of drug concept that is used and its ultimate formatting.

The Dispensable Drug description can be created using data elements from the Drug Name File as follows:

- Drug Name
- Route of Administration Code
- Dosage Form
- Strength
- Strength Unit-of-Measure

Documentation Manual 5-7

Published: 11/11

Revised: 07/21

Applications

Note  
The two-character Route of Administration Code and four-character Dosage Form are not to be displayed or provided in print form in end-users applications. The values should be translated to their corresponding Value Descriptions as defined in the Validation/Translation File. Significant patient safety issues are associated with the use of non-standard abbreviations such as those found in these data fields.

The fields can be displayed in order of their appearance in the Drug Name File, or they can be reordered or removed, depending on the needs of the end-user.

The Description File also provides the Dispensable Drug, as well as additional descriptions for more generalized name-based concepts. In addition to the Dispensable Drugs in the Drug Name File, the Description File provides concepts for those drugs that have been inactive for more than 48 months. When displaying drugs, especially in selection lists (also referred to as picklists), the Status field on the associated Concept ID enables you to exclude items that are no longer associated to active drug products, if appropriate for your application. For example, the Status for a Dispensable Drug is found in the Dispensable Drug File, while the Status for a Routed Dose Form Drug is found in the Routed Drug Form File.

The descriptions in the Description File exist as text strings. The Country Code is 01 USA. For the purposes of these examples, the Type Code is 1 - Full Textual Description. For example:


| Concept Type & Description  | Example                   |
| --------------------------- | ------------------------- |
| 00001 Drug Name             | Lipitor                   |
| 00002 Routed Drug           | Lipitor Oral              |
| 00003 Routed Dose Form Drug | Lipitor Oral Tablet       |
| 00221 Dose Form Drug        | Lipitor Tablet            |
| 00004 Dispensable Drug      | Lipitor Oral Tablet 10 MG |


Information is provided later in this chapter, enabling you to:

- Associate brand and generic drug names
- Construct alternate drug names, dose forms, and strength/strength unit of measure

The Dispensable Drug File includes the Name Source field. This field can be used to identify those generic name based Dispensable Drug values and descriptions that have been created for which no marketed drug product exists. This occurs when a newly marketed, patented drug is marketed but no generic drug

5-8 MED-File v2

Published: 11/11

Revised: 07/21

Displaying Drugs and Creating Drug Selection Lists

products are available. You may elect to exclude those items from a picklist or otherwise identify them for the end-user.

For example:


| Dispensable Drug Concept ID | Description                            | Name Source | Definition                                          |
| --------------------------- | -------------------------------------- | ----------- | --------------------------------------------------- |
| 0000080693                  | Rosuvastatin Calcium Oral Tablet 10 MG | 0           | Generic name; no products marketed with this name   |
| 0000083314                  | Crestor Oral Tablet 10 MG              | 1           | Product name; products are marketed with this name  |
| 0000030825                  | Simvastatin Oral Tablet 10 MG          | 2           | Generic name; products also marketed with this name |


Similarly, the Drug Name File includes the Name Source Code.

For example:


| Drug Descriptor Identifier | Description                            | Name Source | Definition                           |
| -------------------------- | -------------------------------------- | ----------- | ------------------------------------ |
| 080693                     | Rosuvastatin Calcium Oral Tablet 10 MG | G           | No marketed products with this name  |
| 083314                     | Crestor Oral Tablet 10 MG              | P           | Products are marketed with this name |
| 030825                     | Simvastatin Oral Tablet 10 MG          | P           | Products are marketed with this name |


If you are working with Surescripts on quality electronic prescribing guidelines and would like information about working with Wolters Kluwer Clinical Drug Information drug names, contact Wolters Kluwer Clinical Drug Information for additional information.

# Enabling Name-based Searching

If your applications will enable end-users to search for drugs by name, Wolters Kluwer Clinical Drug Information recommends that searching be done anywhere in the string (such as "contains") and not by names that "begin with". The order of ingredients in drug name may vary; therefore, the user should be presented

Documentation Manual 5-9

Published: 11/11

Revised: 07/21

Applications

with the full complement of results. For example, a search based on “begins with Simvastatin” would not identify the drug name “Ezetimibe-Simvastatin” that would be found in a “contains Simvastatin” search.

# Retrieving Routed Drug(s) for a Drug Name

Follow the steps below to retrieve the Routed Drug(s) associated with a Drug Name.

1. Using the Drug Name and its associated Type Code, retrieve the Concept ID from the Description File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

Example:

Using the Drug Name of "Imitrex", Type Code of "1", Concept Type of "00001", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description |
| ------------ | ------------ | ---------- | --------- | ----------- |
| 00001        | 01           | 0000005749 | 1         | Imitrex     |


2. The Concept ID in the Description File represents a Drug Name. It is treated as the Drug Name ID in the Routed Drug File. Using the Concept ID from Step 1 as the Drug Name ID, retrieve all corresponding records in the Routed Drug File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.

Example:

Using the Drug Name ID of "0000005749", Concept Type of "00002", and Country Code of "01" the following would be retrieved:


| Concept Type | Country Code | Concept ID | Drug Name ID | Route ID | Status |
| ------------ | ------------ | ---------- | ------------ | -------- | ------ |
| 00002        | 01           | 0000005839 | 0000005749   | 00022    | 1      |
| 00002        | 01           | 0000006651 | 0000005749   | 00009    | 4      |
| 00002        | 01           | 0000013643 | 0000005749   | 00024    | 1      |
| 00002        | 01           | 0000025763 | 0000005749   | 00028    | 1      |


3. For each record obtained in Step 2, use the Concept ID and desired Type Code to retrieve the associated Description for the Routed Drug from the

5-10 MED-File v2

Published: 11/11

Revised: 07/21

Retrieving Routed Dose Form Drug(s) for a Drug Name

Description File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.

Example:

Using the Concept IDs of "0000005839", "0000006651", "0000013643", and "0000025763", Concept Type of "00002", Country Code of "01", and Type Code of "1", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description          |
| ------------ | ------------ | ---------- | --------- | -------------------- |
| 00002        | 01           | 0000005839 | 1         | Imitrex Oral         |
| 00002        | 01           | 0000006651 | 1         | Imitrex Injection    |
| 00002        | 01           | 0000013643 | 1         | Imitrex Oral         |
| 00002        | 01           | 0000025763 | 1         | Imitrex Subcutaneous |


# Retrieving Routed Dose Form Drug(s) for a Drug Name

Follow the steps below to retrieve the Routed Dose Form Drug(s) associated with a Drug Name.

1. Using the Drug Name and its associated Type Code, retrieve the Concept ID from the Description File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

Example:

Using the Drug Name of "Imitrex", Type Code of "1", Concept Type of "00001", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description |
| ------------ | ------------ | ---------- | --------- | ----------- |
| 00001        | 01           | 0000005749 | 1         | Imitrex     |


2. The Concept ID in the Description File represents a Drug Name. It is treated as the Drug Name ID in the Routed Drug File. Using the Concept ID from Step 1 as the Drug Name ID, retrieve all corresponding records in the Routed Drug File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.

Example:

Documentation Manual 5-11

Published: 11/11

Revised: 07/21

Applications

Using the Drug Name ID of "0000005749", Concept Type of "00002", and Country Code of "01" the following would be retrieved:


| Concept Type | Country Code | Concept ID | Drug Name ID | Route ID | Status |
| ------------ | ------------ | ---------- | ------------ | -------- | ------ |
| 00002        | 01           | 0000005839 | 0000005749   | 00022    | 1      |
| 00002        | 01           | 0000006651 | 0000005749   | 00009    | 4      |
| 00002        | 01           | 0000013643 | 0000005749   | 00024    | 1      |
| 00002        | 01           | 0000025763 | 0000005749   | 00028    | 1      |


3. The Concept ID in the Routed Drug File represents a Routed Drug. Therefore, it is treated as the Routed Drug ID in the Routed Drug Form File. Using the Concept ID from Step 2 as the Routed Drug ID, retrieve all corresponding records in the Routed Drug Form File. The Concept Type for a Routed Dose Form Drug is 00003. The Country Code is 01 USA.

Example:

Using the Routed Drug IDs of "0000005839", "0000006651", "0000013643", and "0000025763", Concept Type of "00003", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Routed Drug ID | Dose Form ID* | Status |
| ------------ | ------------ | ---------- | -------------- | ------------- | ------ |
| 00003        | 01           | 0000007600 | 0000005839     | 00070         | 1      |
| 00003        | 01           | 0000008607 | 0000006651     | 00070         | 1      |
| 00003        | 01           | 0000017400 | 0000013643     | 00081         | 1      |
| 00003        | 01           | 0000030591 | 0000025763     | 00043         | 3      |
| 00003        | 01           | 0000030592 | 0000025763     | 00070         | 1      |


- The Dose Form ID is not the same value as the Dosage Form in the Drug Name File. Refer to Associating Dosage Form in the Drug Name File to Dose Form in the Description File for information.

4. For each record obtained in Step 3, use the Concept ID and desired Type Code to retrieve the associated Description in the Description File. The Concept Type for a Routed Dose Form Drug is 00003. The Country Code is 01 USA.

Example:

5-12 MED-File v2

Published: 11/11

Revised: 07/21

Retrieving Dose Form Drug(s) for a Drug Name

Using the Concept IDs of "0000007600", "0000008607", "0000017407", "0000030591", and "0000030592", Concept Type of "00003", Country Code of "01", and Type Code of "1", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description                   |
| ------------ | ------------ | ---------- | --------- | ----------------------------- |
| 00003        | 01           | 0000007600 | 1         | Imitrex Nasal Solution        |
| 00003        | 01           | 0000008607 | 1         | Imitrex Injection Solution    |
| 00003        | 01           | 0000017400 | 1         | Imitrex Oral Tablet           |
| 00003        | 01           | 0000030591 | 1         | Imitrex Subcutaneous Kit      |
| 00003        | 01           | 0000030592 | 1         | Imitrex Subcutaneous Solution |


# Retrieving Dose Form Drug(s) for a Drug Name

Follow the steps below to retrieve the Dose Form Drug(s) associated with a Drug Name.

1. Using the Drug Name and its associated Type Code, retrieve the Concept ID from the Description File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

Example:

Using the Drug Name of "Imitrex", Type Code of "1", Concept Type of "00001", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description |
| ------------ | ------------ | ---------- | --------- | ----------- |
| 00001        | 01           | 0000005749 | 1         | Imitrex     |


2. The Concept ID in the Description File represents a Drug Name. Therefore, it is treated as the Drug Name ID in the Drug Dose Form File. Using the Concept ID from Step 1 as the Drug Name ID, retrieve all corresponding records in the Drug Dose Form File. The Concept Type for a Dose Form Drug is 00221. The Country Code is 01 USA.

Example:

Documentation Manual 5-13

Published: 11/11

Revised: 07/21

Applications

Using the Drug Name ID of "0000005749", Concept Type of "00221", and Country Code of "01" the following would be retrieved:


| Concept Type | Country Code | Concept ID | Drug Name ID | Dose Form ID | Status |
| ------------ | ------------ | ---------- | ------------ | ------------ | ------ |
| 00221        | 01           | 0000008314 | 0000005749   | 00043        | 3      |
| 00221        | 01           | 0000008315 | 0000005749   | 00070        | 1      |
| 00221        | 01           | 0000008316 | 0000005749   | 00081        | 1      |


3. For each record obtained in Step 2, use the Concept ID and desired Type Code to retrieve the associated Description for the Dose Form Drug from the Description File. The Concept Type for a Dose Form is 00221. The Country Code is 01 USA.

Example:

Using the Concept IDs of "0000008314", "0000008315", and "0000008316", Concept Type of "00221", Country Code of "01", and Type Code of "1", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description      |
| ------------ | ------------ | ---------- | --------- | ---------------- |
| 00221        | 01           | 0000008314 | 1         | Imitrex Kit      |
| 00221        | 01           | 0000008315 | 1         | Imitrex Solution |
| 00221        | 01           | 0000008316 | 1         | Imitrex Tablet   |


Retrieving Dispensable Drug(s) for a Drug Name

Follow the steps below to retrieve the Dispensable Drug(s) associated with a Drug Name.

1. Using the Drug Name and its associated Type Code, retrieve the Concept ID from the Description File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

Example:

5-14 MED-File v2

Published: 11/11

Revised: 07/21

Retrieving Dispensable Drug(s) for a Drug Name

Using the Drug Name of Imitrex", Type Code of "1", Concept Type of "00001", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description |
| ------------ | ------------ | ---------- | --------- | ----------- |
| 00001        | 01           | 0000005749 | 1         | Imitrex     |


2. The Concept ID in the Description File represents a Drug Name. It is treated as the Drug Name ID in the Routed Drug File. Using the Concept ID from Step 1 as the Drug Name ID, retrieve all corresponding records in the Routed Drug File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.

Example:

Using the Drug Name ID of "0000005749", Concept Type of "00002", and Country Code of "01" the following would be retrieved:


| Concept Type | Country Code | Concept ID | Drug Name ID | Route ID | Status |
| ------------ | ------------ | ---------- | ------------ | -------- | ------ |
| 00002        | 01           | 0000005839 | 0000005749   | 00022    | 1      |
| 00002        | 01           | 0000006651 | 0000005749   | 00009    | 4      |
| 00002        | 01           | 0000013643 | 0000005749   | 00024    | 1      |
| 00002        | 01           | 0000025763 | 0000005749   | 00028    | 1      |


3. The Concept ID in the Routed Drug File represents a Routed Drug. It is treated as the Routed Drug ID in the Dispensable Drug File. Using the Concept ID from Step 2 as the Routed Drug ID, retrieve all corresponding records in the Dispensable Drug File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

Using the Routed Drug IDs of "0000005839", "0000006651", "0000013643", and "0000025763", Concept Type of "00004", and Country Code of "01", the following would be retrieved:

Documentation Manual 5-15

Published: 11/11

Revised: 07/21

Applications


| Concept Type | Country Code | Concept ID | Routed Drug ID | Dose Form ID | Str | Str Uom  | Name Source | Device Flag | Status | Link Value | Link Date |
| ------------ | ------------ | ---------- | -------------- | ------------ | --- | -------- | ----------- | ----------- | ------ | ---------- | --------- |
| 00004        | 01           | 0000052822 | 0000005839     | 00070        | 5   | MG/ACT   | 1           | 0           | 1      | &nbsp;     | &nbsp;    |
| 00004        | 01           | 0000052823 | 0000005839     | 00070        | 20  | MG/ACT   | 1           | 0           | 1      | &nbsp;     | &nbsp;    |
| 00004        | 01           | 0000010586 | 0000006651     | 00070        | 6   | MG/0.5ML | 1           | 0           | 4      | 0000141849 | 20090326  |
| 00004        | 01           | 0000040964 | 0000013643     | 00081        | 25  | MG       | 1           | 1           | 1      | &nbsp;     | &nbsp;    |
| 00004        | 01           | 0000040965 | 0000013643     | 00081        | 50  | MG       | 1           | 0           | 1      | &nbsp;     | &nbsp;    |
| 00004        | 01           | 0000068073 | 0000013643     | 00081        | 100 | MG       | 1           | 0           | 1      | &nbsp;     | &nbsp;    |
| 00004        | 01           | 0000075119 | 0000025763     | 00043        | 6   | MG/0.5ML | 1           | 0           | 3      | &nbsp;     | &nbsp;    |
| 00004        | 01           | 0000141849 | 0000025763     | 00070        | 6   | MG/0.5ML | 1           | 0           | 1      | &nbsp;     | &nbsp;    |


Note  
The Dose Form ID is not the same value as the Dosage Form in the Drug Name File. Refer to *Associating Dosage Form in the Drug Name File to Dose Form in the Description File* for information.

Note  
The Link Value and Link Date indicate that the Concept ID has been replaced by the Concept ID defined by the Link Value. Depending on the needs of your application, retrieval of the Dispensable Drug record for the Concept ID defined by the Link Value may be necessary. In this example, the record was returned.

Note  
Additional attributes are associated with these records, but are excluded here due to space constraints.

5-16 MED-File v2

Published: 11/11

Revised: 07/21

Retrieving Routed Dose Form Drug(s) for a Routed Drug

4. For each record obtained in Step 3, use the Concept ID and desired Type Code to retrieve the associated Description in the Description File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

Using the Concept IDs from Step 3, Concept Type of "00004", Country Code of "01", and Type Code of "1", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description                              |
| ------------ | ------------ | ---------- | --------- | ---------------------------------------- |
| 00004        | 01           | 0000052822 | 1         | Imitrex Nasal Solution 5 MG/ACT          |
| 00004        | 01           | 0000052823 | 1         | Imitrex Nasal Solution 20 MG/ACT         |
| 00004        | 01           | 0000010586 | 1         | Imitrex Injection Solution 6 MG/0.5ML    |
| 00004        | 01           | 0000040964 | 1         | Imitrex Oral Tablet 25 MG                |
| 00004        | 01           | 0000040965 | 1         | Imitrex Oral Tablet 50 MG                |
| 00004        | 01           | 0000068073 | 1         | Imitrex Oral Tablet 100 MG               |
| 00004        | 01           | 0000075119 | 1         | Imitrex Subcutaneous Kit 6 MG/0.5ML      |
| 00004        | 01           | 0000141849 | 1         | Imitrex Subcutaneous Solution 6 MG/0.5ML |


Retrieving Routed Dose Form Drug(s) for a Routed Drug

To retrieve Routed Dose Form Drug(s) for a Routed Drug, refer to Steps 3 and 4 in Retrieving Routed Dose Form Drug(s) for a Drug Name.

Retrieving Dispensable Drug(s) for a Routed Drug

To retrieve Dispensable Drug(s) for a Routed Drug, refer to Steps 3 and 4 in Retrieving Dispensable Drug(s) for a Drug Name.

Documentation Manual 5-17

Published: 11/11

Revised: 07/21

Applications

# Retrieving Dispensable Drug(s) for a Routed Dose Form Drug

Follow the steps below to retrieve the Dispensable Drug(s) associated with a Routed Dose Form Drug.

1. Using the Routed Dose Form Drug and its associated Type Code, retrieve the Concept ID from the Description File. The Concept Type for a Routed Dose Form Drug is 00003. The Country Code is 01 USA.

Example:

Using the Routed Dose Form Drug of "Imitrex Oral Tablet", Type Code of "1", Concept Type of "00003", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description         |
| ------------ | ------------ | ---------- | --------- | ------------------- |
| 00003        | 01           | 0000017400 | 1         | Imitrex Oral Tablet |


2. The Concept ID in the Description File represents a Routed Dose Form Drug. Therefore, it is treated as the Routed Drug Form ID in the Dispensable Drug File. Using the Concept ID from Step 1 as the Routed Drug Form ID, retrieve all corresponding records in the Dispensable Drug File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

Using the Routed Drug ID of "0000017400", Concept Type of "00004", and Country Code of "01", the following would be retrieved:

5-18 MED-File v2

Published: 11/11

Revised: 07/21

Retrieving Dispensable Drug(s) for a Routed Dose Form Drug


| Concept Type | Country Code | Concept ID | Routed Drug ID | Dose Form ID | Str | Str Uom | Name Source | Device Flag | Status | Link Value | Link Date |
| ------------ | ------------ | ---------- | -------------- | ------------ | --- | ------- | ----------- | ----------- | ------ | ---------- | --------- |
| 00004        | 01           | 0000040964 | 0000017400     | 00081        | 25  | MG      | 1           | 1           | 1      | &nbsp;     | &nbsp;    |
| 00004        | 01           | 0000040965 | 0000017400     | 00081        | 50  | MG      | 1           | 0           | 1      | &nbsp;     | &nbsp;    |
| 00004        | 01           | 0000068073 | 0000017400     | 00081        | 100 | MG      | 1           | 0           | 1      | &nbsp;     | &nbsp;    |


Note  
The Dose Form ID is not the same value as the Dosage Form in the Drug Name File. Refer to *Associating Dosage Form in the Drug Name File to Dose Form in the Description File* for information.

Note  
Additional attributes are associated with these records, but are excluded here due to space constraints.

Documentation Manual 5-19  
Published: 11/11  
Revised: 07/21

Applications

3. For each record obtained in Step 2, use the Concept ID and desired Type Code to retrieve the associated Description in the Description File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

Using the Concept IDs from Step 2, Concept Type of "00004", Country Code of "01", and Type Code of "1", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description                |
| ------------ | ------------ | ---------- | --------- | -------------------------- |
| 00004        | 01           | 0000040964 | 1         | Imitrex Oral Tablet 25 MG  |
| 00004        | 01           | 0000040965 | 1         | Imitrex Oral Tablet 50 MG  |
| 00004        | 01           | 0000068073 | 1         | Imitrex Oral Tablet 100 MG |


Retrieving Dispensable Drug(s) for a Dose Form Drug

Follow the steps below to retrieve the Dispensable Drug(s) associated with a Dose Form Drug.

1. Using the Dose Form Drug and its associated Type Code, retrieve the Concept ID from the Description File. The Concept Type for a Dose Form Drug is 00221. The Country Code is 01 USA.

Example:

Using the Dose Form Drug of "Imitrex Tablet", Type Code of "1", Concept Type of "00221", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description    |
| ------------ | ------------ | ---------- | --------- | -------------- |
| 00221        | 01           | 0000008316 | 1         | Imitrex Tablet |


2. The Concept ID in the Description File represents a Dose Form Drug. Therefore, it is treated as the Drug-Dose Form ID in the Dispensable Drug File. Using the Concept ID from Step 1 as the Drug-Dose Form ID, retrieve all corresponding records in the Dispensable Drug File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

5-20 MED-File v2

Published: 11/11

Revised: 07/21

Retrieving Dispensable Drug(s) for a Dose Form Drug

Using the Drug-Dose Form ID of "0000008316", Concept Type of "00004", and Country Code of "01", the following would be retrieved:

Documentation Manual 5-21  
Published: 11/11  
Revised: 07/21

Applications


| Concept Type | Country Code | Concept ID | Routed Drug ID | Dose Form ID | Str | Str Uom | Name Source | Device Flag | Status | Drug-Dose Form ID |
| ------------ | ------------ | ---------- | -------------- | ------------ | --- | ------- | ----------- | ----------- | ------ | ----------------- |
| 00004        | 01           | 0000040964 | 0000013643     | 00081        | 25  | MG      | 1           | 1           | 1      | 0000008316        |
| 00004        | 01           | 0000040965 | 0000013643     | 00081        | 50  | MG      | 1           | 0           | 1      | 0000008316        |
| 00004        | 01           | 0000068073 | 0000013643     | 00081        | 100 | MG      | 1           | 0           | 1      | 0000008316        |


Note  
The Dose Form ID is not the same value as the Dosage Form in the Drug Name File. Refer to *Associating Dosage Form in the Drug Name File to Dose Form in the Description File* for information.

Note  
Additional attributes are associated with these records, but are excluded here due to space constraints.

5-22 MED-File v2  
Published: 11/11  
Revised: 07/21

Associating Brand and Generic Drug Names

3. For each record obtained in Step 2, use the Concept ID and desired Type Code to retrieve the associated Description in the Description File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

Using the Concept IDs from Step 2, Concept Type of "00004", Country Code of "01", and Type Code of "1", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description                |
| ------------ | ------------ | ---------- | --------- | -------------------------- |
| 00004        | 01           | 0000040964 | 1         | Imitrex Oral Tablet 25 MG  |
| 00004        | 01           | 0000040965 | 1         | Imitrex Oral Tablet 50 MG  |
| 00004        | 01           | 0000068073 | 1         | Imitrex Oral Tablet 100 MG |


# Associating Brand and Generic Drug Names

Follow the steps below to associate brand and generic Drug Names.

# Identifying a Generic Name for a Brand Name

1. Drugs names for a "brand" can be identified by their Name Type in the SDI Name File. In this case, Name Types of either 1 - Trademarked or 2 - Brand Name may be considered. Using the available Drug Name (either Trademarked or Brand) and its associated Type Code, retrieve the Concept ID from the Description File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

Example:

Using the Drug Name of "Imitrex", Type Code of "1", Concept Type of "00001", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description |
| ------------ | ------------ | ---------- | --------- | ----------- |
| 00001        | 01           | 0000005749 | 1         | Imitrex     |


2. Using the Concept ID from Step 1, retrieve all corresponding records in the Reference Name File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

Example:

Documentation Manual 5-23

Published: 11/11

Revised: 07/21

Applications

Using the Concept ID of "0000005749", Concept Type of "00001", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | ID for Generic Named Drug | Medi-Span Reference Flag |
| ------------ | ------------ | ---------- | ------------------------- | ------------------------ |
| 00001        | 01           | 0000005749 | 0000000303                | Y                        |


3. The ID for Generic Named Drug represents a Concept ID. Using the ID for Generic Named drugs as a Concept ID, retrieve the associated Description from the Description File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

Example:

Using the Concept ID of "0000000303", Concept Type of "00001", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description |
| ------------ | ------------ | ---------- | --------- | ----------- |
| 00001        | 01           | 0000000303 | 1         | SUMatriptan |


You can now associate the two names as required by your application such as:

- Drug lists or picklists
- Prescription drug labeling
- eMARs
- others

Examples include:

- Imitrex (SUMAtriptan)
- SUMAtriptan (Imitrex)

Note  
The above example includes Tall Man lettering for SUMAtriptan. Tall Man letters provided by Wolters Kluwer should be maintained in your application and presented in all instances, whether in a visual display or a hard copy report.

# Identifying a Brand Name for a Generic Name

1. Drugs names for a "generic" can be identified by their Name Type in the SDI Name File. In this case, Name Type of 3 - Generic is relevant. Using the

5-24 MED-File v2

Published: 11/11

Revised: 07/21

Associating Brand and Generic Drug Names

available Drug Name and its associated Type Code, retrieve the Concept ID from the Description File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

Example:

Using the Drug Name of "Verapamil HCl", Type Code of "1", Concept Type of "00001", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description   |
| ------------ | ------------ | ---------- | --------- | ------------- |
| 00001        | 01           | 0000009666 | 1         | Verapamil HCl |


2. The Concept ID for this generic Drug Name represents the ID for Generic Named Drug in the Reference Name File. Using the Concept ID from Step 1 as the ID for Generic Named Drug, retrieve all corresponding records in the Reference Name File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

Example:

Using the Concept ID of "0000009666" as the ID for Generic Named Drug, Concept Type of "00001", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | ID for Generic Named Drug | Medi-Span Reference Flag |
| ------------ | ------------ | ---------- | ------------------------- | ------------------------ |
| 00001        | 01           | 0000000189 | 0000009666                | N                        |
| 00001        | 01           | 0000000701 | 0000009666                | Y                        |
| 00001        | 01           | 0000000704 | 0000009666                | Y                        |
| 00001        | 01           | 0000008300 | 0000009666                | Y                        |
| ...          | &nbsp;       | &nbsp;     | &nbsp;                    | &nbsp;                   |


3. Using the Concept ID(s) from Step 2, retrieve the associated Description from the Description File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

Example:

Using the Concept IDs above, Concept Type of "00001", and Country Code of "01", the following would be retrieved:

Documentation Manual 5-25

Published: 11/11

Revised: 07/21

Applications


| Concept Type | Country Code | Concept ID | Type Code | Description      |
| ------------ | ------------ | ---------- | --------- | ---------------- |
| 00001        | 01           | 0000000189 | 1         | Verapamil HCl CR |
| 00001        | 01           | 0000000701 | 1         | Calan SR         |
| 00001        | 01           | 0000000704 | 1         | Isoptin SR       |
| 00001        | 01           | 0000008300 | 1         | Verelan          |
| ...          | &nbsp;       | &nbsp;     | &nbsp;    | &nbsp;           |


The Reference Name File includes the Medi-Span Reference Flag, indicating the reference brand names that have the same 14-character GPI value. There may be zero, one, or many brand names designated as the reference name(s). In the example above, Concept ID 0000000189 is not considered a reference brand name. Therefore, you should exclude it from consideration when identifying brand names for a generic name.

You can now associate the two names as required by your application such as:

- Drug lists or picklists
- Prescription drug labeling
- eMARs
- others

Examples include:

- Calan SR (Verapamil HCl)
- Isoptin SR (Verapamil HCl)
- Verelan (Verapamil HCl)
- Verapamil HCl (Calan SR)
- Verapamil HCl (Isoptin SR)
- Verapamil HCl (Verelan)

# Associating Brand and Generic Routed Drugs

Follow the steps below to associate brand and generic Routed Drugs.

5-26 MED-File v2

Published: 11/11

Revised: 07/21

Associating Brand and Generic Routed Drugs

# Identifying a Generic Routed Drug for a Brand Routed Drug

1. Drug names for a "brand" can be identified by their Name Type in the SDI Name File. In this case, Name Types of either 1 - Trademarked or 2 - Brand Name may be considered. Therefore, you must first determine if the Routed Drug you have is considered a "brand". Using the available Routed Drug and its associated Type Code, retrieve the Concept ID from the Description File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.

Example:

Using the Routed Drug of "Vytorin Oral", Type Code of "1", Concept Type of "00002", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description  |
| ------------ | ------------ | ---------- | --------- | ------------ |
| 00002        | 01           | 0000031549 | 1         | Vytorin Oral |


2. Using the Concept ID from Step 1, retrieve the Drug Name ID for the Routed Drug from the Routed Drug File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.

Example:

Using the Concept ID of "0000031549", Concept Type of "00002", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Drug Name ID | Route ID | Status |
| ------------ | ------------ | ---------- | ------------ | -------- | ------ |
| 00002        | 01           | 0000031549 | 0000030139   | 24       | 1      |


3. The Drug Name ID represents the Concept ID in the SDI Drug Name File. Using the Drug Name ID from Step 2 as input, retrieve the Name Type from the SDI Name File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

Example:

Documentation Manual 5-27

Published: 11/11

Revised: 07/21

Applications

Using the Concept ID of "0000031039", Concept Type of "00001", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Name Type | Status |
| ------------ | ------------ | ---------- | --------- | ------ |
| 00001        | 01           | 0000030139 | 1         | 1      |


The Name Type of 1 indicates that the Drug Name is Trademarked. Therefore, it is reasonable to proceed to identify the associated generically-named Routed Drug.

4. Using the Concept ID for the Routed Drug from Step 1 as input, retrieve all corresponding records in the Reference Name File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.

Example:

Using the Concept ID of "0000031549", Concept Type of "00002", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | ID for Generic Named Drug | Medi-Span Reference Flag |
| ------------ | ------------ | ---------- | ------------------------- | ------------------------ |
| 00002        | 01           | 0000031549 | 0000031550                | Y                        |


5. Using the ID for Generic Named drugs as a Concept ID, retrieve the associated Description from the Description File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.

Example:

Using the Concept ID of "0000031550", Concept Type of "00002", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description                |
| ------------ | ------------ | ---------- | --------- | -------------------------- |
| 00002        | 01           | 0000031550 | 1         | Ezetimibe-Simvastatin Oral |


The Reference Name File includes the Medi-Span Reference Flag, indicating the reference brand names that have the same 14-character GPI value. There may be zero, one, or many brand names designated as the reference name(s). In this example, Vytorin Oral (Concept ID 0000031549) is considered a reference brand.

You can now associate the two names as required by your application such as:

5-28 MED-File v2

Published: 11/11

Revised: 07/21

Associating Brand and Generic Routed Drugs

- Drug lists or picklists
- Prescription drug labeling
- eMARs
- others

Examples include:

- Vytorin Oral (Ezetimibe-Simvastatin Oral)
- Ezetimibe-Simvastatin Oral (Vytorin Oral)

# Identifying a Brand Routed Drug for a Generic Routed Drug

1. Drugs names for a "generic" can be identified by their Name Type in the SDI Name File. In this case, Name Type of 3 - Generic is relevant. Therefore, you must first determine if the Routed Drug you have is considered a "generic". Using the available Routed Drug and its associated Type Code, retrieve the Concept ID from the Description File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.
2. Using the Concept ID from Step 1, retrieve the Drug Name ID for the Routed Drug from the Routed Drug File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.
3. The Drug Name ID represents the Concept ID in the SDI Drug Name File. Using the Drug Name ID from Step 2 as input, retrieve the Name Type from the SDI Name File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

The Name Type of 3 indicates that the Drug Name is Generic. Therefore, it is reasonable to proceed to identify the associated brand-named Routed Drug.

4. The Concept ID from Step 1 represents the ID for Generic Named Drug in the Reference Name File. Using the Concept ID as the ID for Generic Named Drug, retrieve all corresponding records in the Reference Name File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.
5. Using the ID for Generic Named drugs as a Concept ID, retrieve the associated Description from the Description File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.

The Reference Name File includes the Medi-Span Reference Flag, indicating the reference brand names that have the same 14-character GPI value. There may be zero, one, or many brand names designated as the reference name(s). You should exclude records with a value of "N - Is not a reference brand name" from consideration when identifying brand Routed Drugs for a generic Routed Drug.

Documentation Manual 5-29  
Published: 11/11  
Revised: 07/21

Applications

You can then proceed to associate the two names as needed in your application, as noted in the previous examples.

# Associating Brand and Generic Dispensable Drugs

Follow the steps below to associate brand and generic Dispensable Drugs.

# Identifying a Generic Dispensable Drug for a Brand Dispensable Drug

1. Drugs names for a "brand" can be identified by their Name Type in the SDI Name File. In this case, Name Types of either 1 - Trademarked or 2 - Brand Name may be considered. Therefore, you must first determine if the Dispensable Drug you have is considered a "brand". Using the available Dispensable Drug and its associated Type Code, retrieve the Concept ID from the Description File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

Using the Dispensable Drug of "Omnaris Nasal Suspension 50 MCG/ACT", Type Code of "1", Concept Type of "00004", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description                         |
| ------------ | ------------ | ---------- | --------- | ----------------------------------- |
| 00004        | 01           | 0000133855 | 1         | Omnaris Nasal Suspension 50 MCG/ACT |


2. Using the Concept ID from Step 1, retrieve the Routed Drug ID from the Dispensable Drug File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

Using the Concept ID of "0000133855", Concept Type of "0004", and Country Code of "01", the following would be retrieved:

5-30 MED-File v2

Published: 11/11

Revised: 07/21

Associating Brand and Generic Dispensable Drugs


| Concept Type | Country Code | Concept ID | Routed Drug ID | Dose Form ID | Str | Str Uom | Name Source | Device Flag | Status | Link Value | Link Date |
| ------------ | ------------ | ---------- | -------------- | ------------ | --- | ------- | ----------- | ----------- | ------ | ---------- | --------- |
| 00004        | 01           | 0000133855 | 0000005688     | 00077        | 50  | MCG/ACT | 1           | 0           | 1      | &nbsp;     | &nbsp;    |


Note  
The Dose Form ID is not the same value as the Dosage Form in the Drug Name File. Refer to Associating Dosage Form in the Drug Name File to Dose Form in the Description File for information.

Note  
Additional attributes are associated with these records, but are excluded here due to space constraints.

Documentation Manual 5-31  
Published: 11/11  
Revised: 07/21

Applications

3. The Routed Drug ID in the Dispensable Drug File represents the Concept ID in the Routed Drug File. Using the Routed Drug ID from Step 2 as the Concept ID, retrieve the Drug Name ID from the Routed Drug File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.

Example:

Using the Routed Drug ID of "0000005688", Concept Type of "00002", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Drug Name ID | Route ID | Status |
| ------------ | ------------ | ---------- | ------------ | -------- | ------ |
| 00002        | 01           | 0000005688 | 0000005602   | 24       | 2      |


4. The Drug Name ID represents the Concept ID in the SDI Drug Name File. Using the Drug Name ID from Step 3 as input, retrieve the Name Type from the SDI Name File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

Example:

Using the Concept ID of "0000005602", Concept Type of "00001", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Name Type | Status |
| ------------ | ------------ | ---------- | --------- | ------ |
| 00001        | 01           | 0000005602 | 2         | 2      |


The Name Type of 2 indicates that the Drug Name is a Brand Name. Therefore, it is reasonable to proceed to identify the associated generically-named Dispensable Drug.

5. Using the Concept ID for the Dispensable Drug from Step 1 as input, retrieve all corresponding records in the Reference Name File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

Using the Concept ID of "00000133855", Concept Type of "00004", and Country Code of "01", the following would be retrieved:

5-32 MED-File v2

Published: 11/11

Revised: 07/21

Associating Brand and Generic Dispensable Drugs


| Concept Type | Country Code | Concept ID  | ID for Generic Named Drug | Medi-Span Reference Flag |
| ------------ | ------------ | ----------- | ------------------------- | ------------------------ |
| 00004        | 01           | 00000133855 | 0000122782                | Y                        |


6. Using the ID for Generic Named Drug from Step 5 as a Concept ID, retrieve the associated Description from the Description File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

Using the Concept ID of "00000122782", Concept Type of "00004", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description                             |
| ------------ | ------------ | ---------- | --------- | --------------------------------------- |
| 00004        | 01           | 0000122782 | 1         | Ciclesonide Nasal Suspension 50 MCG/ACT |


The Reference Name File includes the Medi-Span Reference Flag, indicating the reference brand names that have the same 14-character GPI value. There may be zero, one, or many brand names designated as the reference name(s). In this example, Omnaris Nasal Suspension 50 MCG/ACT (Concept ID 0000133855) is considered a reference brand.

You can now associate the two names as required by your application such as:

- Drug lists or picklists
- Prescription drug labeling
- eMARs
- or others

Examples include:

- Omnaris Nasal Suspension 50 MCG/ACT (Ciclesonide Nasal Suspension 50 MCG/ACT)
- Ciclesonide Nasal Suspension 50 MCG/ACT (Omnaris Nasal Suspension 50 MCG/ACT)

Documentation Manual 5-33

Published: 11/11

Revised: 07/21

Applications

# Identifying a Brand Dispensable Drug for a Generic Dispensable Drug

1. Drugs names for a “generic” can be identified by their Name Type in the SDI Name File. In this case, Name Type of 3 - Generic is relevant. Therefore, you must first determine if the Dispensable Drug you have is considered a “generic”. Using the available Dispensable Drug and its associated Type Code, retrieve the Concept ID from the Description File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.
2. Using the Concept ID from Step 1, retrieve the Routed Drug ID from the Dispensable Drug File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.
3. The Routed Drug ID in the Dispensable Drug File represents the Concept ID in the Routed Drug File. Using the Routed Drug ID from Step 2 as the Concept ID, retrieve the Drug Name ID from the Routed Drug File. The Concept Type for a Routed Drug is 00002. The Country Code is 01 USA.
4. The Drug Name ID represents the Concept ID in the SDI Drug Name File. Using the Drug Name ID from Step 3 as input, retrieve the Name Type from the SDI Name File. The Concept Type for a Drug Name is 00001. The Country Code is 01 USA.

The Name Type of 3 indicates that the Drug Name is Generic. It is reasonable to proceed to identify the associated brand-named Dispensable Drug.

5. The Concept ID from Step 1 represents the ID for Generic Named Drug in the Reference Name File. Using the Concept ID as the ID for Generic Named Drug as input, retrieve all corresponding records in the Reference Name File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.
6. Using the Concept ID from Step 5, retrieve the associated Description from the Description File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

The Reference Name File includes the Medi-Span Reference Flag, indicating the reference brand names that have the same 14-character GPI value. There may be zero, one, or many brand names designated as the reference name(s). You should exclude records with a value of “N - Is not a reference brand name” from consideration when identifying a brand Dispensable Drugs for a generic Dispensable Drug.

You can then proceed to associate the two names as needed in your application, as noted in the previous examples.

5-34 MED-File v2

Published: 11/11

Revised: 07/21

Constructing Alternative Drug Names

# Constructing Alternative Drug Names

There are several alternative drug names that can be constructed using the Reference Name File and the Description File. In some cases, you may also wish to construct drug names with varying degrees of specificity by navigating the Routed Drug File and Dispensable Drug File with the algorithms above to identify the desired Concept ID(s) and then using the Reference Name File and the Description File.

The following information provides a few of several options for constructing Alternative Drug Names.

# Constructing BRAND NAME (generic name)

Follow the steps defined in Identifying a Brand Name for a Generic Name or Identifying a Generic Name for a Brand Name".

1. Using the Description File, retrieve the capitalized name for the Concept ID representing the brand name. The Concept Type for a Drug Name is 00001. The Type Code for Capitalized Name is 3. The Country Code is 01 USA.

Example:

Using the Concept ID "0000005749", Concept Type "00001", Type Code "3", and Country Code "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description |
| ------------ | ------------ | ---------- | --------- | ----------- |
| 00001        | 01           | 0000005749 | 3         | IMITREX     |


2. Using the Description File, retrieve the salt name for the Concept ID representing the generic name. The Concept Type for a Drug Name is 0001. The Type Code for Salt Name is 4. The Country Code is 01 USA.

Example:

Using the Concept ID "0000000303", Concept Type "00001", Type Code "4", and Country Code "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description |
| ------------ | ------------ | ---------- | --------- | ----------- |
| 00001        | 01           | 0000000303 | 4         | SUMAtriptan |


You can now associate the two names as required by your application such as:

Documentation Manual 5-35

Published: 11/11

Revised: 07/21

Applications

- Drug lists or picklists
- Prescription drug labeling
- eMARs
- or others

Examples include:

- IMITREX (SUMAtriptan)
- SUMAtriptan (IMITREX)

Note  
The above example includes Tall Man lettering for SUMAtriptan. Tall Man letters provided by Wolters Kluwer should be maintained in your application and presented in all instances, whether in a visual display or a hard copy report.

# Presenting a Dispensable Drug with an Alternate Dose Form Representation

1. Using the Concept ID for a Dispensable Drug, retrieve the corresponding record from the Dispensable Drug File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

Using the Concept ID of "0000017675", Concept Type of "00004", and Country Code of "01", the following would be retrieved:

5-36 MED-File v2

Published: 11/11

Revised: 07/21

Constructing Alternative Drug Names


| Concept Type | Country Code | Concept ID | Bouted Drug ID | Dose Form ID | Str | Str Uom | Name Source | Device Flag | Status | Link Value | Link Date |
| ------------ | ------------ | ---------- | -------------- | ------------ | --- | ------- | ----------- | ----------- | ------ | ---------- | --------- |
| 00004        | 01           | 0000017675 | 0000009584     | 00014        | 20  | MG      | 1           | 0           | 1      | &nbsp;     | &nbsp;    |


Note  
The Dose Form ID is not the same value as the Dosage Form in the Drug Name File. Refer to *Associating Dosage Form in the Drug Name File to Dose Form in the Description File* for information.

Note  
Additional attributes are associated with these records, but are excluded here due to space constraints.

Documentation Manual 5-37  
Published: 11/11  
Revised: 07/21

Applications

2. The Dose Form ID in the Dispensable Drug File represents a Concept ID in the Description File. Using the Dose Form ID from Step 1 as a Concept ID, retrieve the corresponding description from the Description File. The Concept Type for a Dose Form is 00009. The Country Code is 01 USA.

Note  
The Dose Form in the Dispensable Drug File is five digits. The Concept ID for a Dose Form in the Description File is 10 digits. The significant digits in the two values are the same.

Example:

Using the Dose Form ID of "00014" as the Concept ID of "0000000014", Concept Type of "00009", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description             |
| ------------ | ------------ | ---------- | --------- | ----------------------- |
| 00009        | 01           | 0000000014 | 1         | Capsule Delayed Release |
| 00009        | 01           | 0000000014 | 2         | CPDR                    |
| 00009        | 01           | 0000000014 | 5         | Enteric Coated Capsule  |


The "standard" Dose Form representation associated to a DDID in the Description File is based on Type Code 1.

Note  
The Abbreviated Textual Description (Type Code 2) for a Dose Form is provided to enable developers to associate a Dosage Form value in the Drug Name File to a Dose Form value in the Description File. The Abbreviated Textual Description for a Dose Form is not to be displayed or provided in print form in end-user applications. Significant patient safety issues are associated with the use of non-standard Dose Form abbreviations. An example for Associating Dosage Form in the Drug Name File to Dose Form in the Description File follows later in this chapter.

In this example, the "standard" representation for Dose Form 00014 or 0000000014 is "Capsule Delayed Release". Using the Alternate Name (Type Code 5) to represent the Dose Form, "Enteric Coated Capsule" would result.

Example:

5-38 MED-File v2

Published: 11/11

Revised: 07/21

Constructing Alternative Drug Names


| Concept Type | Drug Name | Route | Dosage Form             | Strength | Strength UOM |
| ------------ | --------- | ----- | ----------------------- | -------- | ------------ |
| 0000017675   | PriLOSEC  | Oral  | Capsule Delayed Release | 20       | MG           |
| 0000017675   | PriLOSEC  | Oral  | Enteric Coated Capsule  | 20       | MG           |


# Presenting a Dispensable Drug with an Alternate Strength-Strength UOM Representation

Using the Concept ID for a Dispensable Drug, retrieve the corresponding record from the Dispensable Drug File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

Using the Concept ID of "0000088732", Concept Type of "00004", and Country Code of "01", the following would be retrieved:

Documentation Manual 5-39

Published: 11/11

Revised: 07/21

Applications


| Concept Type | Country Code | Concept ID | Routed Drug ID | Dose Form ID | Str   | Str Uom | Name Source | Device Flag | Status | Strength-Strength UOM ID |
| ------------ | ------------ | ---------- | -------------- | ------------ | ----- | ------- | ----------- | ----------- | ------ | ------------------------ |
| 00004        | 01           | 0000088732 | 0000031549     | 00081        | 10-10 | MG      | 1           | 0           | 1      | 0000002432               |


**Note** The Dose Form ID is not the same value as the Dosage Form in the Drug Name File. Refer to *Associating Dosage Form in the Drug Name File to Dose Form in the Description File* for information.

**Note** Additional attributes are associated with these records, but are excluded here due to space constraints.

5-40 MED-File v2

Published: 11/11

Revised: 07/21

Associating Dosage Form in the Drug Name File to Dose Form in the Description File

1. The Strength-Strength UOM ID in the Dispensable Drug File represents a Concept ID in the Description File. Using the Strength-Strength UOM ID from Step 1 as a Concept ID, retrieve the corresponding description from the Description File. The Concept Type for a Strength-Strength UOM ID is 00222. The Country Code is 01 USA.

Example:

Using the Concept ID of "0000002432", Concept Type of "00222", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Type Code | Description   |
| ------------ | ------------ | ---------- | --------- | ------------- |
| 00222        | 01           | 0000002432 | 1         | 10-10 MG      |
| 00222        | 01           | 0000002432 | 5         | 10 mg - 10 mg |


The "standard" Strength-Strength UOM representation associated to a DDID in the Description File is based on Type Code 1.

In this example, the "standard" representation for Strength-Strength UOM is "10-10 MG". Using the Alternate Name (Type Code 5) to represent the Strength-Strength UOM, "10 mg - 10 mg" would result.

Example:


| Concept Type | Drug Name | Route | Dosage Form | Strength-Strength UOM |
| ------------ | --------- | ----- | ----------- | --------------------- |
| 0000088732   | Vytorin   | Oral  | Tablet      | 10-10 MG              |
| 0000088732   | Vytorin   | Oral  | Tablet      | 10 mg - 10 mg         |


# Associating Dosage Form in the Drug Name File to Dose Form in the Description File

The Dosage Form field in the Drug Name file is defined by a four-character code. This code is not intended for use in end-user applications and must be translated to its description using the Validation/Translation File.

Documentation Manual 5-41

Published: 11/11

Revised: 07/21

Applications

Examples include:


| Dosage Form | Description                      |
| ----------- | -------------------------------- |
| CAPS        | Capsule                          |
| CHEW        | Tablet Chewable                  |
| CP12        | Capsule Extended Release 12 Hour |
| LQCR        | Liquid Extended Release          |
| PT24        | Patch 24 Hour                    |


The Dose Form ID in the Description File is defined by a five-digit value. The value itself has no meaning. The value must be translated to its description using the Description File. The Concept ID in the Description file is a 10-digit value. The significant digits of the five-digit Dose Form ID are the same as those in the 10-digit Concept ID.

Note  
The five-digit Dose Form ID is an attribute in the Dispensable Drug File, the Drug-Dose Form File, and the Routed Drug Form File.

There are three types of descriptions for Dose Forms in the Description File:

- Full Textual Description (Type Code 1)
- Abbreviated Textual Description (Type Code 2)
- Alternate Name (Type Code 5)

The Concept Type for a Dose Form is 00009. The Country Code is 01 USA.

5-42 MED-File v2  
Published: 11/11  
Revised: 07/21

Associating Dosage Form in the Drug Name File to Dose Form in the Description File

Examples of Dose Form IDs and their associated Concept IDs and descriptions include:


| Dose Form ID | Concept ID | Concept Type | Type Code | Description                      |
| ------------ | ---------- | ------------ | --------- | -------------------------------- |
| 00008        | 0000000008 | 00009        | 01        | Capsule                          |
| 00008        | 0000000008 | 00009        | 02        | CAPS                             |
| 00008        | 0000000008 | 00009        | 05        | Capsule                          |
| 00009        | 0000000009 | 00009        | 01        | Tablet Chewable                  |
| 00009        | 0000000009 | 00009        | 02        | CHEW                             |
| 00009        | 0000000009 | 00009        | 05        | Chewable Tablet                  |
| 00011        | 0000000011 | 00009        | 01        | Capsule Extended Release 12 Hour |
| 00011        | 0000000011 | 00009        | 02        | CP12                             |
| 00011        | 0000000011 | 00009        | 05        | 12 Hour Extended Release Capsule |
| 00049        | 0000000049 | 00009        | 01        | Liquid Extended Release          |
| 00049        | 0000000049 | 00009        | 02        | LQCR                             |
| 00049        | 0000000049 | 00009        | 05        | Extended Release Liquid          |
| 00061        | 0000000061 | 00009        | 01        | Patch 24 Hour                    |
| 00061        | 0000000061 | 00009        | 02        | PT24                             |
| 00061        | 0000000061 | 00009        | 05        | 24 Hour Transdermal Patch        |


The Dosage Form can be associated to the Dose Form in one of two ways:

- By a textual match of the Value Description for the Dosage Form in the Validation/Translation File to the record in the Description File with a Type Code of 01 (Full Textual Description).
- By a match of the Dosage Form value in the Drug Name File or the Validation/Translation File to the record in the Description File with a Type Code of 02 (Abbreviated Textual Description).

Documentation Manual 5-43

Published: 11/11

Revised: 07/21

Applications

Examples include:


| Dose Form | Dose Form ID | Concept ID | Concept Type | Type Code | Description |
| --------- | ------------ | ---------- | ------------ | --------- | ----------- |
| CAPS      | 00008        | 0000000008 | 00009        | 02        | CAPS        |
| CHEW      | 00009        | 0000000009 | 00009        | 02        | CHEW        |
| CP12      | 00011        | 0000000011 | 00009        | 02        | CP12        |
| LQCR      | 00049        | 0000000049 | 00009        | 02        | LQCR        |
| PT24      | 00061        | 0000000061 | 00009        | 02        | PT24        |


As already stated, the Abbreviated Textual Description for a Dose Form is not intended for use in end-user applications. Either the Full Textual Description or the Alternate Name should be used.

# Associating Route of Administration in the Drug Name File to Route in the Description File

The Route of Administration Code in the Drug Name file is defined by a 2-character code. This code is not intended for use in end-user applications and must be translated to its description using the Validation/Translation File.

Examples include:


| Route of Administration Code | Description     |
| ---------------------------- | --------------- |
| CO                           | Combination     |
| IJ                           | Injection       |
| IX                           | Intra-articular |


The Route ID is five-digit value. The value itself has no meaning. The value must be translated to its description using the Description File. The Concept ID in the Description file is a 10-digit value. The significant digits of the five-digit Route ID are the same as those in the 10-digit Concept ID.

Note  
The five-digit Route ID is an attribute in the Routed Drug File.

There are two types of descriptions for Routes in the Description File:

- Full Textual Description (Type Code 1)

5-44 MED-File v2  
Published: 11/11  
Revised: 07/21

Associating Route of Administration in the Drug Name File to Route in the Description File

- Abbreviated Textual Description (Type Code 2)

The Concept Type for a Route is 00008. The Country Code is 01 USA.

Examples of Route IDs and their associated Concept IDs and descriptions include:


| Route ID | Concept ID | Concept Type | Type Code | Description     |
| -------- | ---------- | ------------ | --------- | --------------- |
| 00002    | 0000000002 | 00008        | 01        | Combination     |
| 00002    | 0000000002 | 00008        | 02        | CO              |
| 00009    | 0000000009 | 00008        | 01        | Injection       |
| 00009    | 0000000009 | 00008        | 02        | IJ              |
| 00020    | 0000000020 | 00008        | 01        | Intra-articular |
| 00020    | 0000000020 | 00008        | 02        | IX              |


The Route of Administration can be associated to the Route in one of two ways:

- By a textual match of the Value Description for the Route of Administration in the Validation/Translation File to the record in the Description File with a Type Code of 01 (Full Textual Description)
- By a match of the Route of Administration Code in the Drug Name File or the Validation/Translation to the record in the Description File with a Type Code of 02 (Abbreviated Textual Description)

Examples include:


| Route of Administration Code | Dose Form ID | Concept ID | Concept Type | Type Code | Description |
| ---------------------------- | ------------ | ---------- | ------------ | --------- | ----------- |
| CO                           | 00002        | 0000000002 | 00008        | 02        | CO          |
| IJ                           | 00009        | 0000000009 | 00008        | 02        | IJ          |
| IX                           | 00020        | 0000000020 | 00008        | 02        | IX          |


As already stated, the Abbreviated Textual Description for a Route is not intended for use in end-user applications. The Full Textual Description should be used.

Documentation Manual 5-45

Published: 11/11

Revised: 07/21

Applications

# Identifying Ingredients for a Dispensable Drug

Follow the steps below to identify the ingredients for a Dispensable Drug.

1. Using the Concept ID for the Dispensable Drug, retrieve the Ingredient Set ID from the Drug Concept ID to Ingredient Set ID File. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.

Example:

Using the Concept ID of "089522", Concept Type of "00004", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID | Ingredient Set ID | Representative Set Indicator |
| ------------ | ------------ | ---------- | ----------------- | ---------------------------- |
| 00004        | 01           | 089522     | 0000046458        | 2                            |


2. Using the Ingredient Set ID from Step 1, retrieve the Ingredient Identifier(s) from the Ingredient Set to Ingredient ID File.

Example:

Using the Ingredient Set ID "0000046458", the following would be retrieved:


| Ingredient Set ID | Ingredient Identifier | Active/Inactive Flag |
| ----------------- | --------------------- | -------------------- |
| 0000046458        | 0000005825            | A                    |
| 0000046458        | 0000006913            | A                    |


3. Using the Ingredient Identifier(s) from Step 2, retrieve the Ingredient Drug ID from the Ingredient ID to Drug-Strength File.

Example:

Using the Ingredient Identifiers of "0000005825" and "0000006913", the following would be retrieved:


| Ingredient Identifier | Ingredient Drug ID | Ingredient Strength Value | Ingredient Strength UOM (combined) |
| --------------------- | ------------------ | ------------------------- | ---------------------------------- |
| 0000005825            | 0000000701         | 0000060000000             | MG                                 |
| 0000006913            | 0000000946         | 0000040000000             | UNIT                               |


4. Using the Ingredient Drug ID(s) from Step 3, retrieve the Ingredient Drug Name from the Ingredient Drug File.

5-46 MED-File v2

Published: 11/11

Revised: 07/21

Identifying Ingredients for an NDC-UPC-HRI

Example:

Using the Ingredient IDs of "000000701" and "0000000946", the following would be retrieved:


| Ingredient Drug ID | CAS Number | Knowledge Base Drug Code 7 | Ingredient Drug Name | Generic ID |
| ------------------ | ---------- | -------------------------- | -------------------- | ---------- |
| 0000000701         | 000471341  | 0020401                    | CALCIUM CARBONATE    | C000471341 |
| 0000000946         | 001406162  | 0143501                    | VITAMIN D            | C001406162 |


5. The data obtained in Steps 2, 3, and 4 can be formatted to present the ingredient name(s) and corresponding strength and strength unit of measure. In addition, ingredients can be noted as "Active" or "Inactive", if desired.

Example:


| DDID/Description                                        | Ingredient        | Strength | Strength UOM | Active or Inactive |
| ------------------------------------------------------- | ----------------- | -------- | ------------ | ------------------ |
| 089522                                                  | CALCIUM CARBONATE | 600      | MG           | Active             |
| Calcium Carbonate-Vitamin D Oral Tablet 600-400 MG-UNIT | VITAMIN D         | 400      | UNIT         | Active             |


In this example, a representative Ingredient Set is assigned to this DDID as indicated by the Representative Set Indicator of "2" in Step 1. This usually indicates that there are multiple NDCs sharing this DDID and the NDCs are composed of varying ingredients. The variation is usually due to one or more inactive ingredients. The following example illustrates retrieval of ingredients for an NDC-UPC-HRI.

# Identifying Ingredients for an NDC-UPC-HRI

Follow the steps below to identify the ingredients for an NDC-UPC-HRI.

1. Using the NDC-UPC-HRI as the Concept ID, retrieve the Ingredient Set ID from the Drug Concept ID to Ingredient Set ID File. The Concept Type for an NDC-UPC-HRI is 00007. The Country Code is 01 USA.

Example:

Documentation Manual 5-47

Published: 11/11

Revised: 07/21

Applications

Using the Concept ID of "00904323352", Concept Type of "00007", and Country Code of "01", the following would be retrieved:


| Concept Type | Country Code | Concept ID  | Ingredient Set ID | Representative Set Indicator |
| ------------ | ------------ | ----------- | ----------------- | ---------------------------- |
| 00007        | 01           | 00904323352 | 0000068707        | 1                            |


2. Using the Ingredient Set ID from Step 1, retrieve the Ingredient Identifier(s) from the Ingredient Set to Ingredient ID File.

Example:

Using the Ingredient Set ID "0000068707", the following would be retrieved:


| Ingredient Set ID | Ingredient Identifier | Active/Inactive Flag |
| ----------------- | --------------------- | -------------------- |
| 0000068707        | 0000002563            | A                    |
| 0000068707        | 0000005825            | A                    |
| 0000068707        | 0000052064            | I                    |


3. Using the Ingredient Identifier(s) from Step 2, retrieve the Ingredient Drug ID from the Ingredient ID to Drug-Strength File.

Example:

Using the Ingredient Identifiers of "0000002563", "0000005825" and "0000052064", the following would be retrieved:


| Ingredient Identifier | Ingredient Drug ID | Ingredient Strength Value | Ingredient Strength UOM (combined) |
| --------------------- | ------------------ | ------------------------- | ---------------------------------- |
| 0000002563            | 0000000252         | 0000040000000             | UNIT                               |
| 0000005825            | 0000000701         | 0000060000000             | MG                                 |
| 0000052064            | 0000008882         | 0000000000000             | &nbsp;                             |


4. Using the Ingredient Drug ID(s) from Step 3, retrieve the Ingredient Drug Name from the Ingredient Drug File.

Example:

Using the Ingredient IDs of "000000252", "0000000701" and "0000008882", the following would be retrieved:

5-48 MED-File v2

Published: 11/11

Revised: 07/21

Associating New and Old NDC-UPC-HRIs


| Ingredient Drug ID | CAS Number | Knowledge Base Drug Code 7 | Ingredient Drug Name           | Generic ID |
| ------------------ | ---------- | -------------------------- | ------------------------------ | ---------- |
| 0000000252         | 000067970  | 0298001                    | CHOLECALCIF-EROL               | C000067970 |
| 0000000701         | 000471341  | 0020401                    | CALCIUM CAR-BONATE             | C000471341 |
| 0000008882         | 002783940  | 1652503                    | FD&C YELLOW #6 (SUNSET YELLOW) | C002783940 |


5. The data obtained in Steps 2, 3, and 4 can be formatted to present the ingredient name(s) and corresponding strength and strength unit of measure. In addition, ingredients can be noted as “Active” or “Inactive”, if desired.

Example:


| NDC-UPC-HRI                                             | Ingredient                     | Strength | Strength UOM | Active or Inactive |
| ------------------------------------------------------- | ------------------------------ | -------- | ------------ | ------------------ |
| 00904-3233-52                                           | CALCIUM CARBON-ATE             | 600      | MG           | Active             |
| Calcium Carbonate-Vitamin D Oral Tablet 600-400 MG-UNIT | CHOLECALCIF-EROL               | 400      | UNIT         | Active             |
| &nbsp;                                                  | FD&C YELLOW #6 (SUNSET YELLOW) | &nbsp;   | &nbsp;       | Inactive           |


This example illustrates an NDC-UPC-HRI that shares the same DDID as the previous example. However, the ingredients include those specific to the drug product, including inactive ingredients.

# Associating New and Old NDC-UPC-HRIs

Each NDC-UPC-HRI record in the NDC File includes attributes that enable you to associate it to an old NDC-UPC-HRI and/or a new NDC-UPC-HRI, where appropriate.

Documentation Manual 5-49

Published: 11/11

Revised: 07/21

Applications

When an NDC-UPC-HRI record is added to MED-File v2 for the first time, the following record is provided in the NDC File. These examples include only those fields in the NDC File record that are relevant to this discussion.


| NDC-UPC-HRI | Item Status Flag | Old NDC-UPC-HRI | New NDC-UPC-HRI | Old Effective Date | New Effective Date | Transaction Code |
| ----------- | ---------------- | --------------- | --------------- | ------------------ | ------------------ | ---------------- |
| 12345678901 | A                | &nbsp;          | &nbsp;          | &nbsp;             | &nbsp;             | A                |


Note  
The Transaction Code field is populated only in Incremental Updates. If you receive a Total Replacement, this field will be blank.

If the NDC-UPC-HRI is replaced by another NDC-UPC-HRI, the following records are provided in the NDC File. These examples include only those fields being discussed here.


| NDC-UPC-HRI | Item Status Flag | Old NDC-UPC-HRI | New NDC-UPC-HRI | Old Effective Date | New Effective Date | Transaction Code |
| ----------- | ---------------- | --------------- | --------------- | ------------------ | ------------------ | ---------------- |
| 12345678901 | I                | &nbsp;          | 45678901234     | &nbsp;             | 20081001           | C                |
| 45678901234 | A                | 12345678901     | &nbsp;          | 20081001           | &nbsp;             | A                |


Note  
The Transaction Code field is populated only in Incremental Updates. If you receive a Total Replacement, this field will be blank.

If the NDC-UPC-HRI “45678901234” is subsequently replaced, the following records are provided in the NDC File. These examples include only those fields in the NDC File record that are relevant to this discussion.


| NDC-UPC-HRI | Item Status Flag | Old NDC-UPC-HRI | New NDC-UPC-HRI | Old Effective Date | New Effective Date | Transaction Code |
| ----------- | ---------------- | --------------- | --------------- | ------------------ | ------------------ | ---------------- |
| 12345678901 | I                | &nbsp;          | 45678901234     | &nbsp;             | 200081001          | &nbsp;           |
| 45678901234 | I                | 12345678901     | 78901234567     | 20081001           | 20100825           | C                |
| 78901234567 | A                | 45678901234     | &nbsp;          | 20100825           | &nbsp;             | A                |


5-50 MED-File v2

Published: 11/11

Revised: 07/21

Associating New and Old Dispensable Drugs (DDIDs)

Note  
The Transaction Code field is populated only in Incremental Updates. If you receive a Total Replacement, this field will be blank.

Once an NDC-UPC-HRI has been inactive for 48 months, it will be removed from MED-File v2. The following record would appear for NDC-UPC-HRI "12345678901" on the date 20121001. These examples include only those fields in the NDC File record that are relevant to this discussion.


| NDC-UPC-HRI | Item Status Flag | Old NDC-UPC-HRI | New NDC-UPC-HRI | Old Effective Date | New Effective Date | Transaction Code |
| ----------- | ---------------- | --------------- | --------------- | ------------------ | ------------------ | ---------------- |
| 12345678901 | Z                | &nbsp;          | 45678901234     | &nbsp;             | 200081001          | D                |


Note  
This record will appear only once in an Incremental Update. If you receive a Total Replacement, the NDC-UPC-HRI record will not appear.

In this example, an NDC-UPC-HRI is replaced by another. In that same MED-File v2 update cycle, the replacement NDC-UPC-HRI is also replaced. The following records are provided in the NDC File. These examples include only those fields in the NDC File record that are relevant to this discussion.


| NDC-UPC-HRI | Item Status Flag | Old NDC-UPC-HRI | New NDC-UPC-HRI | Old Effective Date | New Effective Date | Transaction Code |
| ----------- | ---------------- | --------------- | --------------- | ------------------ | ------------------ | ---------------- |
| 12345678901 | I                | &nbsp;          | 45678901234     | &nbsp;             | 200081001          | C                |
| 45678901234 | I                | 12345678901     | 78901234567     | 20081001           | 20081005           | C                |
| 78901234567 | A                | 45678901234     | &nbsp;          | 20081005           | &nbsp;             | A                |


Note  
The Transaction Code field is populated only in Incremental Updates. If you receive a Total Replacement, this field will be blank.

# Associating New and Old Dispensable Drugs (DDIDs)

Note  
The Drug Descriptor Identifier and Dispensable Drug Identifier are one and the same. The terms may be used interchangeably in this and other Wolters Kluwer Clinical Drug Information documentation.

Documentation Manual 5-51  
Published: 11/11  
Revised: 07/21

Applications

Each DDID record In the Dispensable Drug File includes attributes that enable you to associate an old Concept ID (DDID) to a new DDID, where appropriate. The Link Value within a record specifies the new DDID replacement. The Link Date indicates when the new DDID replaced the Concept ID.

This example includes only those fields in the Dispensable Drug File record that are relevant to this discussion.

Example:


| Concept ID | Link Value | Link Date |
| ---------- | ---------- | --------- |
| 0000130242 | 0000164832 | 20110328  |


Using the Description File, you can visually examine the differences between the Concept ID for the old DDID and that for the new DDID. The Concept Type for a Dispensable Drug is 00004. The Country Code is 01 USA.


| Concept Type | Country Code | Concept Value | Type Code | Description                                      |
| ------------ | ------------ | ------------- | --------- | ------------------------------------------------ |
| 00004        | 01           | 0000130242    | 01        | Fragmin Subcutaneous Injectable 15000 UNIT/0.6ML |
| 00004        | 01           | 0000164832    | 01        | Fragmin Subcutaneous Solution 15000 UNIT/0.6ML   |


The new DDID will also appear in the Drug Name File in field F099 as an attribute of the DDID. This only occurs in the Incremental Update and is not present in the Total Database.

# Retrieving KDCs for a Dispensable Drug

The Drug Name File includes the Knowledge Base Drug Code (KDC) and the Representative KDC Flag as attributes of the DDID.

- When the Representative KDC Flag on a DDID is 1 - Exact Match KDC, the KDC in the record can be used to perform clinical screening.
- When the Representative KDC Flag on a DDID is 2 - Representative KDC, the KDC is editorially assigned by Wolters Kluwer Clinical Drug Information. For a generic DDID, it is likely to represent only active ingredients. The KDC can be used to perform clinical screening, but if you have a specific NDC-UPC-HRI and want to perform clinical screening to include inactive ingredients specific to that NDC-UPC-HRI, use the KDC in the NDC File.

5-52 MED-File v2

Published: 11/11

Revised: 07/21

Retrieving GPIs for a Dispensable Drug

- When the Representative KDC Flag on a DDID is 0 - Unassigned, the DDID cannot be screened using a KDC. Use the KDC on a specific NDC-UPC-HRI to perform clinical screening.
- If the KDC on an NDC-UPC-HRI is zero-filled, the NDC-UPC-HRI represents a product such as a device, which is inappropriate to screen.

# Retrieving GPIs for a Dispensable Drug

The Drug Name File includes the Generic Product Identifier (GPI) and the Representative GPI Flag as attributes of the DDID.

- When the Representative GPI Flag on a DDID is 1 - Exact Match GPI, the GPI in the record can be used to perform clinical screening.
- When the Representative GPI Flag on a DDID is 2 - Representative GPI, the GPI is editorially assigned by Wolters Kluwer Clinical Drug Information. The GPI can be used to perform clinical screening, but if you have a specific NDC-UPC-HRI and want to perform clinical screening with GPI specific to that NDC-UPC-HRI. To do so:  
> Retrieve the GPPC for the NDC-UPC-HRI in the NDC File.  
> Using the GPPC, retrieve the associated GPI in the GPPC File.
- When the Representative GPI Flag on a DDID is 0 - Unassigned, the DDID cannot be screened using a GPI. Use the GPI on a specific NDC-UPC-HRI to perform clinical screening.

# Identifying Therapeutic Alternatives Using the TC-GPI Name File

The TC-GPI Name File can be used as a starting point in identifying therapeutic alternatives. This may aid in creating and maintaining a formulary for the purposes of prescribing, defining drug benefit plans, purchasing, and inventory.

The following examples illustrate some of the options you can consider in defining alternatives using the Wolters Kluwer Clinical Drug Information Therapeutic Classification System (TCS) hierarchy. The needs of your end-users will determine whether more specific or more general levels of the GPI hierarchy are more appropriate. Additional data elements in MED-File v2 may be used to further filter the number of results. End-users may wish to limit the drugs by DESI Code, DEA Class Code, TEE Code, packing, route of administration, dosage form, Repackage Code, pricing, inactive status, or other values.

Documentation Manual 5-53  
Published: 11/11  
Revised: 07/21

Applications

# Identifying DDIDs for Drug Class

Example:

1. Using the Drug Class "394000" for HMG CoA Reductase Inhibitors as a wild card input for the GPI field, retrieve all matching records in the Drug Name File.
2. Use the TC-GPI Name File to retrieve the TC-GPI Name for each GPI within the records obtained in Step 1.
3. Use the Drug Descriptor Identifier (DDID) for each record retrieved in Step 1 to retrieve the drug's description from the Description File. The Concept ID in the Description File is a 10-digit representation of the DDID in the Drug Name File. The Concept Type is 00004. The Country Code is 01 USA.

Alternatively, the DDID Description can be built using the Drug Name, Route of Administration, Dose Form, Strength, and Strength Unit-of-Measure fields in the Drug Name File.


| DDID   | GPI            | TC-GPI Name                                      | DDID Description                       |
| ------ | -------------- | ------------------------------------------------ | -------------------------------------- |
| 033801 | 39400030100120 | Fluvastatin Sodium Oral Capsule 20 MG            | Lescol Oral Capsule 20 MG              |
| 047764 | 39400010100310 | Atorvastatin Calcium Tab 10 MG (Base Equivalent) | Atorvastatin Calcium Oral Tablet 10 MG |
| 047942 | 39400010100310 | Atorvastatin Calcium Tab 10 MG (Base Equivalent) | Lipitor Oral Tablet 10 MG              |
| 028392 | 39400050000305 | Lovastatin Tab 10 MG                             | Lovastatin Oral Tablet 10 MG           |
| 013468 | 39400050000305 | Lovastatin Tab 10 MG                             | Mevacor Oral Tablet 10 MG              |
| 083317 | 39400060100305 | Rosuvastatin Calcium Tab 5 MG                    | Crestor Oral Tablet 5 MG               |
| 030827 | 39400075000340 | Simvastatin Tab 10 MG                            | Simvastatin Oral Tablet 40 MG          |
| ...    | &nbsp;         | &nbsp;                                           | &nbsp;                                 |


5-54 MED-File v2

Published: 11/11

Revised: 07/21

Creating Nine-Character GPPCs

# Identifying NDCs for Drug Class

Example:

1. Using the Drug Class "394000" for HMG CoA Reductase Inhibitors as a wild card input for the GPI field, retrieve all matching records in the GPPC File.
2. Using the GPPC for each record retrieved in Step 1 as input to the NDC File, retrieving all matching records.
3. Use the TC-GPI Name File to retrieve the TC-GPI Name for each GPI within the records obtained in Step 1.
4. Use the Drug Descriptor Identifier (DDID) for each record retrieved in Step 1 to retrieve the drug's description from the Description File. The Concept ID in the Description File is a 10-digit representation of the DDID in the NDC File. The Concept Type is 00004. The Country Code is 01 USA.


| GPPC                           | GPI TC-GPI Name                       | NDC-UPC-HRI                           | Description |
| ------------------------------ | ------------------------------------- | ------------------------------------- | ----------- |
| 17603028                       | 39400010100310                        | &nbsp;                                | &nbsp;      |
| Atorvastatin Calcium Tab 10 MG | &nbsp;                                | &nbsp;                                | &nbsp;      |
| (Base Equivalent)              | 00071015540                           | Lipitor Oral Tablet 10 MG             | &nbsp;      |
| 17603A22                       | 39400010100310                        | &nbsp;                                | &nbsp;      |
| Atorvastatin Calcium Tab 10 MG | &nbsp;                                | &nbsp;                                | &nbsp;      |
| (Base Equivalent)              | 51138022045                           | &nbsp;                                | &nbsp;      |
| 54868393404                    | Lipitor Oral Tablet 10 MG             | &nbsp;                                | &nbsp;      |
| 13577070                       | 39400030100120                        | &nbsp;                                | &nbsp;      |
| Fluvastatin Sodium Cap 20 MG   | 00078017615                           | Fluvastatin Sodium Oral Capsule 20 MG | &nbsp;      |
| 13577041                       | 39400030100120                        | &nbsp;                                | &nbsp;      |
| Fluvastatin Sodium Cap 20 MG   | 66105014706                           | &nbsp;                                | &nbsp;      |
| 13411011106                    | Fluvastatin Sodium Oral Capsule 20 MG | &nbsp;                                | &nbsp;      |
| ...                            | &nbsp;                                | &nbsp;                                | &nbsp;      |


# Creating Nine-Character GPPCs

Wolters Kluwer Clinical Drug Information's GPPC enables grouping of drug products with the same packaging criteria for the purpose of making purchasing, inventory, and pricing decisions.

The eight-character GPPC allows grouping of drug products based on their active ingredients, strength, and basic packaging criteria. To enable a specific grouping

Documentation Manual 5-55

Published: 11/11

Revised: 07/21

Applications

of drug products, you can incorporate Wolters Kluwer Clinical Drug Information’s Modifier Codes to further delineate specific packaging, colors, flavors, and so on.

A nine-character GPPC is created by appending a single character of your choosing to an existing eight-character GPPC from Wolters Kluwer Clinical Drug Information. The single character represents a unique combination of Modifier Codes that defines packaging, product, or trademark information.

A nine-character GPPC can be defined at the NDC, GPPC, GPI, or sub-GPI level.

5-56 MED-File v2

Published: 11/11

Revised: 07/21

# Appendix A: Loading and Updating

## In This Chapter

- General Product Unpackaging
- Telecommunications Transport
- File Loading
- File Updating
- Data Definition Language Policy
- Summary File Contents
- Summary File Sample
- Summary File Processing
- Data Dictionary and Validation/Translation Processing
- Validation/Translation Look-ups

## General Product Unpackaging

For your first issue, you will receive a full initial database. Subsequent issues can be provided as incremental updates or full replacement databases.

> **Note**  
> The initial incremental update and full replacement databases are available via File Transfer Protocol (FTP) or can be pulled down via HTTP Web Download.

## Telecommunications Transport

For information on Wolters Kluwer Clinical Drug Information’s two methods of product delivery, FTP Pull and HTTP Download, see below.

### FTP Pull (Pick-up)

If FTP Pull is your method of deliver choice, Wolters Kluwer Clinical Drug Information will place the product files on our FTP site for pick-up. An e-mail notification will be sent once the file transfer is complete. Contact Customer Support to obtain a login and password for our server if you wish to use this method of delivery. You will then be able to log in to pull the files down to your location after they are delivered.

Loading and Updating


| Note | Wolters Kluwer Clinical Drug Information reserves the right to clean old files from customer directories as space is needed. Keep your FTP Pull directory reasonably clean and do not attempt to use it as a file archive. |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


# HTTP Download (Web Download)

HTTP Download is available to all customers as an alternate method of delivery, and as a gateway to our documentation library. This site contains the current total database in addition to the current and two previous incremental updates.


| Note | Contact Customer Support for your login and password, and for additional instructions on using this download site. |
| ---- | ------------------------------------------------------------------------------------------------------------------ |


# Decompressing Files

To reduce the size of the attachment files, Wolters Kluwer Clinical Drug Information compresses them before sending them to you. The options for the compression method are ZIP and UNIX Pack.


| If you are receiving the files... | Wolters Kluwer Clinical Drug Information recommends...                                                                                              | Then...                                                              |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Microsoft Windows-based system,   | using 7-ZIP if you are unable to use the built-in compression/decompression functionality that is built into current versions of Microsoft Windows. | we can provide the link to the 7-Zip Web site.                       |
| on a UNIX system,                 | using unpack, unless your system administrator directs otherwise.                                                                                   | you can find many versions of UNIX included with the unpack utility. |


# ZIP Compression

Many current versions of Microsoft Windows™ have built in ZIP file decompression and compression functionality. Consult your operating system documentation for more details. Access the 7-Zip Web site ([http://www.7-Zip.org](http://www.7-Zip.org)) for the most current version of this software. Instructions for using 7-Zip to extract compressed files are located within the 7-Zip Help information.

A-2 MED-File v2

Published: 11/11

Revised: 01/18

File Loading

# File Loading

When loading your initial database, extract the data and place it into your system. If you need to replace the information in your system, considerations include:

- making a backup copy
- determining processes for deleting current information
- loading the data from your initial database

# File Updating

If you receive incremental updates, you must process records in the product-specific files according to their transaction codes. Transaction codes indicate the type of file modification to perform. Valid values include:


| Code | Description                                                                                                                                           |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| A    | Add the record to your system. No duplicate key should exist.                                                                                         |
| C    | The record that has a matching key changed and must be updated in your system. The data from the incremental update replaces the data on your system. |
| D    | Delete the record that has a matching key from your system.                                                                                           |


Note  
Any file may be empty in the incremental update if no information has changed.

# Updating the Copyright File (MF2COPY)

The Copyright File is to copyright the Wolters Kluwer Clinical Drug Information product only; therefore, it does not require updating.

# Updating the Summary File (MF2SUM)

The Summary File is supplied in its entirety on Incremental Updates. The Summary File contains information on volume, supplement, and expiration, which you will need to process against. (Refer later in this chapter for more information on Summary File Processing.)

# Updating the Read Me File (MF2READ)

The Read Me File is for informational purposes only; therefore, it does not require updating.

Documentation Manual A-3  
Published: 11/11  
Revised: 01/18

Loading and Updating

# Updating the Data Dictionary File (MF2DICT)

The Data Dictionary File is supplied in its entirety on Incremental Updates. Any change to this file requires you to change other programming.

You will receive advanced notification of any changes that affect the definition or length of an existing field or record within a file.

# Updating the Validation/Translation File (MF2VAL)

The Validation/Translation File is supplied in its entirety on Incremental Updates.

The Validation/Translation File may go unchanged from issue to issue. However, new values for a field may be added without advanced notice.

![img-1.jpeg](img-1.jpeg)

 Diagram A.1: Update Using Incremental Updates

A-4 MED-File v2

Published: 11/11

Revised: 01/18

Data Definition Language Policy

# Data Definition Language Policy

Data Definition Language (DDL) files are provided to you as you define the MED-File v2 database structures. MED-File v2 platforms that support DDL are:

- SQL Server
- Oracle

# Supported DDL Properties

Below are the DDL properties Wolters Kluwer Clinical Drug Information supports:


| Supported DDL Property     | Description                                                                                                                                                                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Column Naming              | The column name and its length adheres to standards that are mutually compatible with all supported database platforms. Column names are 30 characters or less.                                                                                   |
| Mandatory Fields           | Constraints for mandatory columns (not null constraints) are supplied for the appropriate columns for the tables within a module when indicated by the design and supported by the target database.                                               |
| Primary Key Index Creation | Primary key indexes are provided for primary key columns for the tables within a module when supported by the target database.                                                                                                                    |
| Table Creation             | The “Create Table” statement is always present for each table delivered within the module. The table name and length adhere to standards mutually compatible with all supported database platforms. Table name lengths are 30 characters or less. |


# Unsupported DDL Properties

Below are the DDL properties Wolters Kluwer Clinical Drug Information does not support:


| Unsupported DDL Property | Description                                                                                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Loading             | Coding and scripts to assist the customer while loading and formatting the flat file databases into the structures that have been established by the DDL are not supplied. |


*Note:* Decimal points will not be included in the data. |  
| Foreign Key Creation | Creation of foreign keys is not supported. This allows customers to load their tables in any order they choose. |

Documentation Manual A-5

Published: 11/11

Revised: 01/18

Loading and Updating


| Unsupported DDL Property | Description                                                                                                                                                                   |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Indexes                  | Indexes are not directly created; however, primary keys may indirectly result in the creation of an index. This is database-specific and foreign key indexes are not created. |
| Permission Information   | Items such as users, grants, and privileges are not defined in the DDL.                                                                                                       |
| Reserve                  | There is no reserved space.                                                                                                                                                   |
| Table Sizing Information | Items such as data volume, storage requirements, and number of records are not defined in the DDL.                                                                            |
| Transaction Code         | Transaction codes, delimiters, and so forth are not supported within the DDL.                                                                                                 |


# Testing and Validation

The DDL files are tested on the following database platforms at Wolters Kluwer Clinical Drug Information:

- SQL Server
- Oracle

# Maintenance

The MED-File v2 DDL files are built according to the documentation contained in this appendix. Updates are in response to enhancements to current MED-File v2 modules and the introduction of new MED-File v2 modules.

# Script Organization

The information below is supplied for each of the four file combinations offered for MED-File v2 and their supported databases:

# Basic


| Script Name                      | Description                                                   |
| -------------------------------- | ------------------------------------------------------------- |
| mf2_oracle_basic_CreateTable.sql | This script creates the tables.                               |
| mf2_oracle_basic_Constraint.sql  | This script creates the Primary key constraints on the table. |
| &nbsp;                           | &nbsp;                                                        |
| mf2_mssql_basic_CreateTable.sql  | This script creates the tables.                               |
| mf2_mssql_basic_Constraint.sql   | This script creates the Primary key constraints on the table. |


A-6 MED-File v2

Published: 11/11

Revised: 01/18

Data Definition Language Policy

## Clinical


| Script Name                         | Description                                                   |
| ----------------------------------- | ------------------------------------------------------------- |
| mf2_oracle_clinical_CreateTable.sql | This script creates the tables.                               |
| mf2_oracle_clinical_Constraint.sql  | This script creates the Primary key constraints on the table. |
| &nbsp;                              | &nbsp;                                                        |
| mf2_mssql_clinical_CreateTable.sql  | This script creates the tables.                               |
| mf2_mssql_clinical_Constraint.sql   | This script creates the Primary key constraints on the table. |


## Complete


| Script Name                         | Description                                                   |
| ----------------------------------- | ------------------------------------------------------------- |
| mf2_oracle_complete_CreateTable.sql | This script creates the tables.                               |
| mf2_oracle_complete_Constraint.sql  | This script creates the Primary key constraints on the table. |
| &nbsp;                              | &nbsp;                                                        |
| mf2_mssql_complete_CreateTable.sql  | This script creates the tables.                               |
| mf2_mssql_complete_Constraint.sql   | This script creates the Primary key constraints on the table. |


## Pricing


| Script Name                        | Description                                                   |
| ---------------------------------- | ------------------------------------------------------------- |
| mf2_oracle_pricing_CreateTable.sql | This script creates the tables.                               |
| mf2_oracle_pricing_Constraint.sql  | This script creates the Primary key constraints on the table. |
| &nbsp;                             | &nbsp;                                                        |
| mf2_mssql_pricing_CreateTable.sql  | This script creates the tables.                               |
| mf2_mssql_pricing_Constraint.sql   | This script creates the Primary key constraints on the table. |


## Naming Standard

For the .sql file type, the naming standard is Structured Query Language.

**Note** The data delivery media will always contain either a Total Database or an Incremental Update file.

Documentation Manual A-7  
Published: 11/11  
Revised: 01/18

Loading and Updating

# Mapping Tables

The table below details the mappings from the file name to the table name.


| File Name                                          | Table Name |
| -------------------------------------------------- | ---------- |
| MF2COPY (Copyright File)                           | MF2COPY    |
| MF2READ (ReadMe File)                              | MF2READ    |
| MF2DICT (Data Dictionary File)                     | MF2DICT    |
| MF2VAL (Validation/Translation File)               | MF2VAL     |
| MF2SUM (Summary File)                              | MF2SUM     |
| MF2NAME (Drug Name File)                           | MF2NAME    |
| MF2TCGPI (TC-GPI Name File)                        | MF2TCGPI   |
| MF2NDC (NDC File)                                  | MF2NDC     |
| MF2LAB (Labeler File)                              | MF2LAB     |
| MF2GPPC (GPPC File)                                | MF2GPPC    |
| MF2ERR (Error Correct File)                        | MF2ERR     |
| MF2GPR (GPPC Price File)                           | MF2GPR     |
| MF2PRC (NDC Price File)                            | MF2PRC     |
| MF2MOD (Modifier File)                             | MF2MOD     |
| MF2NDCM (NDC Modifier File)                        | MF2NDCM    |
| MF2DRGNM (SDI Drug Name File)                      | MF2DRGNM   |
| MF2RTDRG (Routed Drug File)                        | MF2RTDRG   |
| MF2DFDRG (Drug-Dose Form File)                     | MF2DFDRG   |
| MF2RTDF (Routed Dose Form File)                    | MF2RTDF    |
| MF2DRG (Dispensable Drug File)                     | MF2DRG     |
| MF2DESC (Description File)                         | MF2DESC    |
| MF2RTE (Route File)                                | MF2RTE     |
| MF2FRM (Dose Form File)                            | MF2FRM     |
| MF2STUOM (Strength-Strength Unit of Measure File)  | MF2STUOM   |
| MF2SET (Drug Concept ID to Ingredient Set ID File) | MF2SET     |
| MF2INGS (Ingredient Set ID to Ingredient ID File)  | MF2INGS    |
| MF2STR (Ingredient ID to Drug-Strength File)       | MF2STR     |
| MF2IDRG (Drug ID File)                             | MF2IDRG    |
| MF2SEC (Secondary Alternate ID File)               | MF2SEC     |
| MF2RNM (Reference Name File)                       | MF2RNM     |


Note  
Not all customers will receive all files listed in the table above. The files you receive are based on the layout of the MED-File v2 that you have licensed.

A-8 MED-File v2

Published: 11/11

Revised: 01/18

Summary File Contents

# Summary File Contents

The Summary File contains the Issue Date, Expiration Date, and File Mode for a Total Database and Incremental Update. This information can be used to ensure that issues are loaded in the correct order (Issue Checking) and that data being used have not expired (Expiration Checking).

# Summary File Record Types

The Record Type indicates what type of data is contained within each Summary File record. The possible values for Record Type are:


| Record Type | Description                          |
| ----------- | ------------------------------------ |
| CCR         | Copyright Statement                  |
| CDC         | Create Date                          |
| CDE         | Expiration Date                      |
| CDI         | Issue Date                           |
| CDJ         | Grace Message Date                   |
| CDK         | Kill Date                            |
| CFM         | File Mode                            |
| CFT         | File Type                            |
| CPN         | Product Name                         |
| CPV         | Product Version (Issue)              |
| CVL         | Volume Number and Supplement Number  |
| LCC         | Locality Information - Country Code  |
| LLC         | Locality Information - Language Code |
| TOC         | Table of Contents                    |


# Sequence Number

The Sequence Number allows ease of sorting comments and data within a Record Type. No meaning is given to these values, and they may increment by any number (such as 1s, 5s, or 10s). This increment may not be consistent within or among Record Types. (For examples of Sequence Number, refer to "Summary File Sample" later in this chapter.)

# Comment Marker

The Comment Marker helps when viewing the Summary File and enhances readability when the Summary File is printed. When the Comment Marker contains an asterisk (*), the information in the data portion of the record describes the data following. When the Comment Marker contains a blank, actual data is in the remaining data portion of the record. (For examples of Comment Marker, refer to "Summary File Sample" later in this chapter.)

Documentation Manual A-9

Published: 11/11

Revised: 01/18

Loading and Updating

# Data

Data following a Comment Marker containing an asterisk (*) is a text description of the Record Type. Data following a blank Comment Marker is the actual value for that Record Type. (For examples of data, refer to "Summary File Sample" below.)

# Summary File Sample

```txt
CCR 010 Copyright 2011 Clinical Drug Information, LLC
CDC 010 * Create Date
CDC 020 20111027
CDE 010 * Expiration Date
CDE 020 20111109
CDI 010 * Issue Date
CDI 020 20111102
CDJ 010 * Grace Message Date
CDJ 020 20111109
CDK 010 * Kill Date
CDK 020 20111209
CFM 010 * Product File Mode (P-Production, T-Test)
CFM 020 P
CFT 010 * Product File Type (T-Total, U-Update)
CFT 020 T
CFF 010 * Product File Format (F-Fixed, D-Delimited)
CFF 020 F
CPN 010 * Product Name
CPN 020 MEDI-SPAN ELECTRONIC DRUG FILE (TM) V2
CPV 010 * Product Version (Issue)
CPV 020 * YY.Q.F.NNN Year, Quarter Number, Frequency, Publication Number
CPV 030 * Q = 1,2,3,4, F = Blank (Qtrly), 1 Monthly,
CPV 040 * 2 Semi-Monthly,
CPV 050 * 3 Weekly, 4 Daily
CPV 060 11.4.3.005
CVL 010 *
CVL 015 * Volume Number
CVL 020 * Vol Supplement
CVL 022 * No. No.
CVL 025 * ---
CVL 030 00044 00
LCC 010 *
LCC 020 * Country Code and Country
LCC 030 * (01 USA, 02 Canada, 03 Mexico)
LCC 040 * CC Country
LCC 050 * -- ---
LCC 060 01 USA
LLC 010 *
LLC 020 * Language Code and Language
LLC 030 * (01 English, 02 Spanish)
LLC 040 * LC Language
LLC 050 * -- ---
LLC 060 01 English
TOC 010 *
TOC 020 * Table of Contents
TOC 030 * Pt Fil
TOC 040 * ## Num File Name Rec Cnt

```

A-10 MED-File v2

Published: 11/11

Revised: 01/18

Summary File Processing


| TOC 050 * | --  | --- | ---      | ---     |
| --------- | --- | --- | -------- | ------- |
| TOC 110   | 01  | 010 | MF2COPY  | 0000001 |
| TOC 120   | 01  | 020 | MF2SUM   | 0000080 |
| TOC 130   | 01  | 030 | MF2READ  | 0000002 |
| TOC 140   | 01  | 040 | MF2DICT  | 0000272 |
| TOC 150   | 01  | 050 | MF2VAL   | 0000752 |
| TOC 160   | 01  | 060 | MF2NAME  | 0048152 |
| TOC 170   | 01  | 070 | MF2TCGPI | 0034231 |
| TOC 180   | 01  | 080 | MF2NDC   | 0168859 |
| TOC 190   | 01  | 090 | MF2LAB   | 0001547 |
| TOC 200   | 01  | 100 | MF2GPPC  | 0055124 |
| TOC 210   | 01  | 110 | MF2ERR   | 0000108 |
| TOC 220   | 01  | 120 | MF2GPR   | 0014192 |
| TOC 230   | 01  | 130 | MF2PRC   | 0337090 |
| TOC 240   | 01  | 140 | MF2MOD   | 0004118 |
| TOC 250   | 01  | 150 | MF2NDCM  | 0171829 |
| TOC 260   | 01  | 160 | MF2DRGNM | 0047604 |
| TOC 270   | 01  | 170 | MF2RTDRG | 0049766 |
| TOC 280   | 01  | 180 | MF2DFDRG | 0054487 |
| TOC 290   | 01  | 190 | MF2RTDF  | 0055157 |
| TOC 300   | 01  | 200 | MF2DRG   | 0071041 |
| TOC 310   | 01  | 210 | MF2DESC  | 0338994 |
| TOC 320   | 01  | 220 | MF2RTE   | 0000035 |
| TOC 330   | 01  | 230 | MF2FRM   | 0000093 |
| TOC 340   | 01  | 240 | MF2STUOM | 0006493 |
| TOC 350   | 01  | 250 | MF2SET   | 0239900 |
| TOC 360   | 01  | 260 | MF2INGS  | 0126896 |
| TOC 370   | 01  | 270 | MF2STR   | 0028732 |
| TOC 380   | 01  | 280 | MF2IDRG  | 0004529 |
| TOC 390   | 01  | 290 | MF2SEC   | 0007628 |


# Summary File Processing

## Issue Checking Processing

The Summary Record Types of CFT (Product File Type) and CVL (Product Volume Number) allow you to ensure that once the initial load (Total Database) is complete, product updates are used and processed in order.

The Product File Type should be “T” for the Total Database of production data only. All subsequent products received should have a Product File Type of “U”.

When you receive your initial load, record the Volume Number of that product. Each monthly product you receive from that point forward should have a volume number incremented by one from the last Volume Number processed.

In between monthly issue dates, you may receive a supplemental issue of the product with data that should not wait until the next issue date to be distributed. These products will have the same Volume Number as last product issue processed, but the supplement number should be incremented by one for each supplement between normal issues. (Refer to Supplement Processing later in this chapter for more information.)

Documentation Manual A-11

Published: 11/11

Revised: 01/18

Loading and Updating


| Note | Loading data out of sequence for Incremental Updates will corrupt the database and yield incorrect results.                                                                                                                                                                                                                                                                                                                                                                                         |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Note | If you receive a product with a Volume Number incremented by more than one, you have missed an issue. If you receive an issue where the volume number is the same as the last one processed and the supplement number is zero, you have received a duplicate issue or are trying to reload an issue you have already applied. Contact your Wolters Kluwer Clinical Drug Information Customer Support Representative immediately in the case of a missing issue or the receipt of a duplicate issue. |


# Expiration Checking

Expiration Checking is required for the implementation of the database. The Expiration Date is specified in the CDE Record of the Summary File. The Kill Date appears in the CDK Record.


| Note | The database must not be accessible by the end-user after the Kill Date and should remain disabled until the next issue is applied. If a subscription has been canceled, the database must be removed from the end-user's system. |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


You can use the Expiration Date to warn end-users that data has expired indicating a new issue of the product should be applied. This warning can continue to be output throughout the grace period between the Expiration Date and the Kill Date. Once the Kill Date is reached, the database must be updated or disabled.

# Checking for Product Expiration

The following general logic explains how to check for expiration of a product:

1. Check the System Date as the system is initiated each day.
2. If the System Date is later than the Expiration Date, but earlier than the Kill Date, provide the end-user with a warning. We recommend that you identify the number of days remaining to update the product (Kill Date minus the System Date).
3. If the System Date is past the Kill Date, inform the end-user that the system has been disabled and is unavailable for use until the database is updated. Delete any files that are specific to the expired issue if your subscription has been canceled. Otherwise, keep the system disabled until you receive and apply the new issues.

A-12 MED-File v2

Published: 11/11

Revised: 01/18

Copyright and Issue Display

# Copyright and Issue Display

It is required that the Copyright Statement and Version (Issue) Number be listed on all printed reports generated using data from MED-File v2. To do this, select the Copyright Statement from Record Type CCR and the version from Record Type CPV.

Example:

Copyright 2011 Clinical Drug Information, LLC  
Issue 08.1.1.002

# Supplement Processing

When issues are provided as mid-cycle supplements, it is important to understand what you are receiving.

Each supplement contains the entire normal issue's update transactions plus additional ones that could not wait until the next issue of the product. The next issue will contain all changes in the cycle including those that already were distributed in supplements.

Additions, changes, and deletions found in the regular issue may have already been applied if supplements are received and applied in between regularly scheduled issues. Make sure that integrity checks on Transaction Codes are not in effect during the application of the next issue following a supplement; such as an addition ("A" Transaction Code) of something already on file is acceptable if an optional supplemental update has been applied.

# Data Dictionary and Validation/Translation Processing

## Automated Database Import

The product-specific files included in MED-File v2 are relational in nature and can be loaded directly into corresponding tables in a relational database. To set up the import of product files:

1. Cross-match the initial letter of the Field Identifier field in the Data Dictionary File to the file it represents, including the Data Dictionary and Validation/Translation Files, since you will need to reference their information in normal processing.
2. Generate a script or code to create database tables based on the information in the Data Dictionary File. There will be a table "create" for each unique starting letter. Substitute the meaningful names described in

Documentation Manual A-13

Published: 11/11

Revised: 01/18

Loading and Updating

step 1 as the actual table names. Each field definition should have the meaningful name from the Field Description, a type based on the Field Type, and the size indicated in the Field Length.


| Note | To avoid confusion and minimize changes if the layouts of the product files change, do not use the Field Identifier values as field names. |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------ |


3. Prepare for the import process per file by defining the starting location of each field in that file as the number immediately following the initial letter of each Field Identifier field. If the Implied Decimal Flag is "Y" for a particular field, format the input of that field to have the number of decimal places as specified in the Decimal Places field.
4. Execute each import to populate each database table.


| Note | Once the initial database tables are created and populated, you must set up a separate application to read incremental updates and change the database contents based on Transaction Codes. |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


# Validation/Translation Look-ups

Much of the MED-File v2 information is encoded; therefore, numbers represent more meaningful, longer values. This saves room in the transfer files and your internal storage. What this requires is that you translate the encoded value to the more meaningful value at the time you output information to your end-users.

To do this processing, you need to do some initial setup. Set up a cross-reference table of the logical name of a field within a file to its corresponding Field Identifier value in the Data Dictionary File. Make sure you are tracking the Field Validation Flag and Field Abbreviation Flag per Field Identifier value.

You can then set up a standard routine prior to any user output to look up the logical field name and see if it has corresponding values (based on the Field Validation Flag and Field Abbreviation Flag). If a flag is set, look up the corresponding Field Identification value in the Validation/Translation File and obtain the Value Description or Value Abbreviation based on the encoded field value you have to output. If both flags are set, determine which is more appropriate for your application and use that corresponding value.

A-14 MED-File v2

Published: 11/11

Revised: 01/18

# Appendix B: Record Layout Diagrams

## In This Appendix

- Introduction
- Record Layouts

## Introduction

This appendix contains the MED-File v2 record layouts. The shaded fields represent the unique key into the file.

For more information about record layouts, see Chapter 4, "Data Elements".

Record Layout Diagrams

# Record Layouts

## Copyright File (MF2COPY)

![img-2.jpeg](img-2.jpeg)

## ReadMe File (MF2READ)

![img-3.jpeg](img-3.jpeg)

![img-4.jpeg](img-4.jpeg)

B-2 MED-File v2

Published: 04/14

Record Layouts

## Data Dictionary File (MF2DICT)

![img-5.jpeg](img-5.jpeg)

## Validation/Translation File (MF2VAL)

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

Documentation Manual B-3

Published: 04/14

Record Layout Diagrams

# Summary File (MF2SUM)

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

B-4 MED-File v2

Published: 04/14

Record Layouts

# Drug Name File (MF2NAME)


| Drug Des Identifier 9(6) | &nbsp; | Drug Name | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp;                           | &nbsp;                         | R A o d u m t i e n   | Dosage Form X(4) 40 | Strength | &nbsp; | &nbsp; | &nbsp; | &nbsp; | Strength Unit Of Measure X(10) 60 | X(10) 65         |
| ------------------------ | ------ | --------- | ------ | ------ | ------ | ------ | ------ | -------------------------------- | ------------------------------ | --------------------- | ------------------- | -------- | ------ | ------ | ------ | ------ | --------------------------------- | ---------------- |
| 9                        | B      | C         | E      | L      | M      | B      | N      | Generic Product Identifier X(14) | Knowledge Base Drug Code X(10) | New Drug Desc ID 9(6) | S                   | K        | L      | M      | F      | I      | R                                 | Reserve X(6) 115 |
| &nbsp;                   | I      | o         | f      | e      | g      | a      | m      | m                                | m                              | t                     | C                   | D        | C      | d      | a      | n      | e                                 | p                |
| &nbsp;                   | I      | o         | t      | g      | t      | a      | m      | m                                | t                              | t                     | C                   | d        | c      | d      | a      | n      | e                                 | p                |
| &nbsp;                   | I      | o         | t      | 70     | c      | d      | m      | m                                | t                              | t                     | C                   | d        | c      | d      | a      | n      | e                                 | p                |
| &nbsp;                   | I      | o         | c      | d      | d      | c      | d      | m                                | t                              | t                     | F                   | F        | c      | d      | a      | n      | e                                 | p                |


# TC-GPI Name File (MF2TCGPI)


| TC-GPI Key X(14)   | &nbsp;      | R e c 15         | TC-GPI Name | &nbsp;                   | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| ------------------ | ----------- | ---------------- | ----------- | ------------------------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 75                 | 10          | 15               | 20          | 25                       | 30     | 35     | 40     | 45     | 50     | 55     | 60     | 65     |
| &nbsp;             | &nbsp;      | T y              | &nbsp;      | &nbsp;                   | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| TC-GPI Name (cont) | T C C v d e | Reserve X(10) 80 | T r a n C d | Last Change Date 9(8) 90 | 95     | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| ---                | ---         | ---              | ---         | ---                      | ---    | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |


Documentation Manual B-5

Published: 04/14

Record Layout Diagrams

# NDC File (MF2NDC)


| NDC-UPC-HRI | Drug Descriptor Identifier | T C E o E d e     | D D E A I T C     | R X O P A S I T C | Generic Product Packaging Code | Old NDC-UPC-HRI | New NDC-UPC-HRI   | R I T h r d       | T Knowledge Base Drug Code |
| ----------- | -------------------------- | ----------------- | ----------------- | ----------------- | ------------------------------ | --------------- | ----------------- | ----------------- | -------------------------- |
| X(11)       | 9(6)                       | 15                | 20                | 25                | X(8)                           | X(11)           | 45                | 50                | X(10)                      |
| X(10)       | 10                         | 15                | 20                | 25                | X(8)                           | X(11)           | 45                | 50                | X(10)                      |
| X(10)       | 15                         | 15                | 20                | 25                | X(8)                           | X(11)           | 45                | 50                | 60                         |
| K D C F I g | MS Labeler Identifier      | M u l e m e n i t | N u l e m e n i t | I t n i n e m     | C R e s 1 e r v e              | P P O I n d     | H D F I g R a n k | D R e s 1 e r v e | R S t r g R a n k          |
| ---         | ---                        | ---               | ---               | ---               | ---                            | ---             | ---               | ---               | ---                        |
| 9(5)        | 70                         | C d               | C d               | S p k             | P c                            | V               | R                 | R                 | R                          |
| 9(5)        | 10                         | C d               | C d               | S p k             | P c                            | V               | R                 | R                 | R                          |


# Labeler File (MF2LAB)


| Medi-Span Labeler Identifier | Manufacturer's (Labeler) Name | Manufacturer Abbreviated Name | L a b I T y | Reserve | T r a n C d | Last Change Date |
| ---------------------------- | ----------------------------- | ----------------------------- | ----------- | ------- | ----------- | ---------------- |
| 9(5)                         | X(30)                         | X(30)                         | 35          | 40      | 45          | 9(8)             |
| X(9)                         | 50                            | 50                            | 55          | 55      | 55          | 60               |


B-6 MED-File v2

Published: 04/14

Record Layouts

# GPPC File (MF2GPPC)

| Generic Product  
Packaging Code | Package  
Size | P S  
a z  
c k U  
a O  
g M  
e | Package  
Quantity | U  
D  
u  
u  
u  
25  
c  
d | P D  
a e  
c s  
k c  
c  
d | Generic Product  
Identifier | Reserve | T  
r  
a  
n  
55  
c  
d | Last Change

Date |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
| X(8) | 9(6)V9(3)  
10 | 15 | 9(5) | 20 | X(14)  
30 | 35 | 40 | 45 | 9(8)  
60 |

# Error Correct File (MF2ERR)

| Key | Unique Key | | | Data Element Code | D E L  
a l e  
t e n  
a m g  
2' e t  
n h

i | Reserve |  
| --- | --- | --- | --- | --- | --- | --- |  
| ID | X(19) | 10 | 15 | 20 | | X(5) |

# GPPC Price File (MF2GPR)

| Generic Product  
Packaging Code | G P P C  
10 | Effective Date  
9(8) | Unit Price  
9(5)V9(6)  
20 | Reserve  
25 | T r a n  
55 | Last Change Date  
9(8)

60 |  
| --- | --- | --- | --- | --- | --- | --- |

Documentation Manual B-7

Published: 04/14

Record Layout Diagrams

# NDC Price File (MF2PRC)

| NDC-UPC-HRI | | P  
r  
c  
c  
d | Price Effective Date | | Unit Price | | Unit Price - Extended | | Package Price | | A  
W  
P  
i  
n  
d | T  
r  
a  
n  
c

d | Last Change Date |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
| X(11) | 7/5 | $10 | 9(8) | $25 | 9(5)V9(6) | $30 | 9(8)V9(5) | $45 | 9(8)V9(2) | $45 | $50 | | 9(8)V60 |

# Modifier File (MF2MOD)

| Modifier Code | | Modifier Description | | | | | | Reserve | | | | | T  
r  
a  
n  
c

d | Last Change Date |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
| X(6) | 7/5 | $10 | X(25) | $25 | 9(25) | $30 | | X(24) | $35 | 40 | $45 | $50 | | 9(8)V60 |

# NDC Modifier File (MF2NDCM)

| NDC-UPC-HRI | | Modifier Code | | Reserve | | T  
r  
a  
n  
c

d | Last Change Date | |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- |  
| X(11) | 7/5 | $10 | X(6) | $20 | 9(6) | $25 | 9(8) | $25 |

B-8 MED-File v2

Published: 04/14

Record Layouts

# SDI Drug Name File (MF2DRGNM)


| Concept Type | C o u C n d t r y | Concept ID | T r a n e C d | S t a t u s | Link Value | Link Date | Reserve |
| ------------ | ----------------- | ---------- | ------------- | ----------- | ---------- | --------- | ------- |
| 9(5)         | &nbsp;            | 9(10)      | &nbsp;        | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 10           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 15           | &nbsp;            | &nbsp;     | 9(10)         | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 25           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 30           | YYYYMMDD          | &nbsp;     | &nbsp;        | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 35           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 40           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 45           | X(10)             | &nbsp;     | &nbsp;        | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 45           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |


# Routed Drug File (MF2RTDRG)


| Concept Type | C o u C n d t r y | Concept ID | T r a n e C d | Drug Name ID | Route ID | S t a t u s | Link Value | Link Date | Reserve |
| ------------ | ----------------- | ---------- | ------------- | ------------ | -------- | ----------- | ---------- | --------- | ------- |
| 9(5)         | &nbsp;            | 9(10)      | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 10           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 15           | &nbsp;            | &nbsp;     | 9(10)         | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 25           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 30           | 9(5)              | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 30           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 45           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 50           | 9(10)             | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 40           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 55           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 60           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 65           | YYYYMMDD          | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 45           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 50           | X(28)             | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 55           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 60           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 65           | &nbsp;            | &nbsp;     | &nbsp;        | &nbsp;       | &nbsp;   | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |


![img-10.jpeg](img-10.jpeg)

Documentation Manual B-9  
Published: 04/14

Record Layout Diagrams

# Drug-Dose Form File (MF2DFDRG)

![img-11.jpeg](img-11.jpeg)

![img-12.jpeg](img-12.jpeg)

# Routed Drug Form File (MF2RTDF)

![img-13.jpeg](img-13.jpeg)

![img-14.jpeg](img-14.jpeg)

B-10 MED-File v2

Published: 04/14

Record Layouts

# Dispensable Drug File (MF2DRG)


| Concept Type    | C o u C n d t r y | Concept ID | T r a n c d | Routed Drug ID | Dose Form ID        | Strength | Strength Unit of Measure | N D a e w e S F r i c g |
| --------------- | ----------------- | ---------- | ----------- | -------------- | ------------------- | -------- | ------------------------ | ----------------------- |
| 9(5)            | 9(10)             | 9(10)      | 15          | 9(10)          | 9(5)                | X(15)    | X(15)                    | 80                      |
| &nbsp;          | &nbsp;            | &nbsp;     | &nbsp;      | 20             | 35                  | 30       | 35                       | 80                      |
| S t a t u s     | Link Value        | &nbsp;     | Link Date   | &nbsp;         | Routed Drug Form ID | &nbsp;   | Drug-Dose Form ID        | &nbsp;                  |
| ---             | ---               | ---        | ---         | ---            | ---                 | ---      | ---                      | ---                     |
| &nbsp;          | 9(10)             | 70         | 75          | YYYYMMDD       | 9(10)               | 85       | 90                       | 9(10)                   |
| &nbsp;          | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;         | &nbsp;              | &nbsp;   | &nbsp;                   | &nbsp;                  |
| Reserve, (cont) | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;         | &nbsp;              | &nbsp;   | &nbsp;                   | &nbsp;                  |
| ---             | ---               | ---        | &nbsp;      | &nbsp;         | &nbsp;              | &nbsp;   | &nbsp;                   | &nbsp;                  |
| &nbsp;          | 135               | 140        | &nbsp;      | &nbsp;         | &nbsp;              | &nbsp;   | &nbsp;                   | &nbsp;                  |
| &nbsp;          | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;         | &nbsp;              | &nbsp;   | &nbsp;                   | &nbsp;                  |


Documentation Manual B-11

Published: 04/14

Record Layout Diagrams

# Description File (MF2DESC)

![img-15.jpeg](img-15.jpeg)

![img-16.jpeg](img-16.jpeg)

![img-17.jpeg](img-17.jpeg)

continued on next page

B-12 MED-File v2

Published: 04/14

Record Layouts

# Description File (MF2DESC), continued

![img-18.jpeg](img-18.jpeg)

![img-19.jpeg](img-19.jpeg)

![img-20.jpeg](img-20.jpeg)

Documentation Manual B-13

Published: 04/14

Record Layout Diagrams

# Route File (MF2RTE)


| Concept Type | C o u C n d t r y | Concept ID | T r a n c d | Link Value | Link Date | Reserve |
| ------------ | ----------------- | ---------- | ----------- | ---------- | --------- | ------- |
| 9(5)         | &nbsp;            | 9(10)      | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 10           | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 15           | &nbsp;            | 9(10)      | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 20           | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 25           | YYYYMMDD          | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 30           | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 35           | X(11)             | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 40           | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 45           | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |


# Dose Form File (MF2FRM)


| Concept Type | C o u C n d t r y | Concept ID | T r a n c d | Link Value | Link Date | Reserve |
| ------------ | ----------------- | ---------- | ----------- | ---------- | --------- | ------- |
| 9(5)         | &nbsp;            | 9(10)      | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 10           | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 15           | &nbsp;            | 9(10)      | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 20           | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 25           | YYYYMMDD          | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 30           | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 35           | X(11)             | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 40           | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |
| 45           | &nbsp;            | &nbsp;     | &nbsp;      | &nbsp;     | &nbsp;    | &nbsp;  |


B-14 MED-File v2  
Published: 04/14

Record Layouts

# Strength-Strength Unit of Measure File (MF2STUOM)


| Concept Type | C o u C n d t r y | Concept ID | &nbsp; | &nbsp; | T r a n C d | Strength | &nbsp; | &nbsp; | Strength Unit of Measure | &nbsp; | &nbsp; | S t a t u s | Link Value | &nbsp; | &nbsp; | Link Date | &nbsp; |
| ------------ | ----------------- | ---------- | ------ | ------ | ----------- | -------- | ------ | ------ | ------------------------ | ------ | ------ | ----------- | ---------- | ------ | ------ | --------- | ------ |
| &nbsp;       | &nbsp;            | 9(10)      | 15     | 20     | &nbsp;      | x(15)    | 25     | 30     | x(15)                    | 40     | 45     | &nbsp;      | 9(10)      | 55     | 60     | 65        | &nbsp; |


![img-21.jpeg](img-21.jpeg)

# Drug Concept ID to Ingredient Set ID File (MF2SET)


| Concept Type | C o u C n d t r y | Concept ID | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | Ingredient Set ID | &nbsp; | &nbsp; | T r a n C d | R e p i n d | Reserve | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| ------------ | ----------------- | ---------- | ------ | ------ | ------ | ------ | ------ | ----------------- | ------ | ------ | ----------- | ----------- | ------- | ------ | ------ | ------ | ------ | ------ |
| &nbsp;       | &nbsp;            | 10         | 15     | 20     | 25     | 30     | 35     | 9(10)             | 15     | 20     | &nbsp;      | &nbsp;      | 40      | 45     | 50     | 55     | 60     | &nbsp; |


Documentation Manual B-15

Published: 04/14

Record Layout Diagrams

# Ingredient Set ID to Ingredient Set ID File (MF2INGS)

![img-22.jpeg](img-22.jpeg)

# Ingredient ID to Drug-Strength File (MF2STR)

![img-23.jpeg](img-23.jpeg)

![img-24.jpeg](img-24.jpeg)

B-16 MED-File v2

Published: 04/14

Record Layouts

# Ingredient Drug File (MF2IDRG)


| Drug ID                      | T_{r}  | CAS Number | Knowledge Base Code 7 | R_{e}  | Ingredient Drug Name |
| ---------------------------- | ------ | ---------- | --------------------- | ------ | -------------------- |
| 9(10)                        | a      | X(20)      | 9(7)                  | s -1   | X(60)                |
| “5”                          | n      | “20”       | “35”                  | e r 40 | “45”                 |
| “10”                         | C      | “25”       | “30”                  | v e l  | “50”                 |
| “5”                          | d      | &nbsp;     | &nbsp;                | &nbsp; | “55”                 |
| Ingredient Drug Name, (cont) | &nbsp; | &nbsp;     | &nbsp;                | &nbsp; | &nbsp;               |
| ---                          | ---    | ---        | ---                   | ---    | ---                  |
| “70”                         | “75”   | “80”       | “85”                  | “90”   | “95”                 |


# Secondary Alternate ID File (MF2SEC)


| External Drug ID (NDC-UPC-HRI) | &nbsp; | &nbsp; | E     | Alternate Drug ID | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | A      | T   | Reserve | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| ------------------------------ | ------ | ------ | ----- | ----------------- | ------ | ------ | ------ | ------ | ------ | ------ | --- | ------- | ------ | ------ | ------ | ------ |
| &nbsp;                         | &nbsp; | &nbsp; | x     | &nbsp;            | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | I   | r       | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| &nbsp;                         | &nbsp; | &nbsp; | D     | &nbsp;            | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | t   | a       | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| &nbsp;                         | &nbsp; | &nbsp; | r     | &nbsp;            | &nbsp; | &nbsp; | X(20)  | &nbsp; | &nbsp; | &nbsp; | F   | n       | &nbsp; | &nbsp; | X(21)  | &nbsp; |
| “5”                            | “10”   | “15”   | “21g” | “25”              | “30”   | “35”   | “40”   | &nbsp; | &nbsp; | &nbsp; | r   | m       | “45”   | “50”   | “55”   | “60”   |
| &nbsp;                         | &nbsp; | &nbsp; | C     | &nbsp;            | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | d   | t       | d      | &nbsp; | &nbsp; | &nbsp; |


Documentation Manual B-17

Published: 04/14

Record Layout Diagrams

# Reference Name File (MF2RNM)


| Concept Type | C o u C n d t r y | Concept ID | ID for Generic Named Drug | T r a n e C d | M S R e f | Reserve |
| ------------ | ----------------- | ---------- | ------------------------- | ------------- | --------- | ------- |
| 9(5)         | &nbsp;            | 9(10)      | 9(10)                     | &nbsp;        | &nbsp;    | X(19)   |
| &nbsp;       | &nbsp;            | 10         | 15                        | 20            | 25        | 30      |
| &nbsp;       | &nbsp;            | &nbsp;     | &nbsp;                    | &nbsp;        | &nbsp;    | 35      |
| &nbsp;       | &nbsp;            | &nbsp;     | &nbsp;                    | &nbsp;        | &nbsp;    | 40      |
| &nbsp;       | &nbsp;            | &nbsp;     | &nbsp;                    | &nbsp;        | &nbsp;    | 45      |


B-18 MED-File v2

Published: 04/14

Record Layouts

Documentation Manual B-19  
Published: 04/14

Record Layout Diagrams

B-20 MED-File v2  
Published: 04/14  
Revised: 11/09

# Appendix C: GPI Name Abbreviations

# GPI Abbreviation List

Below is the list of GPI names and abbreviations.

Note This list includes, but is not limited to the following abbreviations.


| Abbreviation | Full Name                                |
| ------------ | ---------------------------------------- |
| A            | Vitamin A                                |
| Ace          | Acetate                                  |
| Alk          | Alkaloids                                |
| Alum or Al   | Aluminum                                 |
| AmCl         | Ammonium Chloride                        |
| Amyl         | Amylase                                  |
| APAP         | Acetaminophen                            |
| APC          | Aspirin, Phenacetin, and Caffeine        |
| ASA          | Aspirin                                  |
| Azo          | Phenazopyridine                          |
| B Complex    | Vitamin B1, B2, B3, B5, B6, and B12      |
| B1           | Thiamine HCl                             |
| B2           | Riboflavin                               |
| B3           | Niacin                                   |
| B5           | Calcium Pantothenate or Pantothenic Acid |
| B6           | Pyridoxine HCl                           |
| B12          | Cyanocobalamin                           |
| BAC          | Benzalkonium Chloride                    |
| Bell         | Belladonna                               |
| Bella Alk    | Belladonna Alkaloids                     |
| Benzo        | Benzocaine                               |
| Bicarb       | Bicarbonate                              |
| Biphos       | Biphosphate                              |
| Bis          | Bismuth                                  |
| BPM          | Brompheniramine Maleate                  |
| Bromodiphen  | Bromodiphenhydramine HCl                 |
| Bromphen     | Brompheniramine Maleate                  |


&nbsp;

GPI Name Abbreviations


| Abbreviation       | Full Name                   |
| ------------------ | --------------------------- |
| Butabarb           | Butabarbital                |
| C                  | Ascorbic Acid               |
| Ca                 | Calcium                     |
| Caff               | Caffeine                    |
| Cal                | Calcium                     |
| Carb               | Carbonate                   |
| Carbeta            | Carbetapentane Citrate      |
| Cellu              | Cellulase                   |
| Chlorphen          | Chlorpheniramine Maleate    |
| Cl                 | Chloride                    |
| COD                | Codeine                     |
| Conj               | Conjugated                  |
| CPM                | Chlorpheniramine Maleate    |
| Cr                 | Chromium                    |
| Cu                 | Copper                      |
| D                  | Vitamin D                   |
| D5W                | Dextrose 5% in Water        |
| DES                | Diethylstilbestrol          |
| DHA                | Docosahexaenoic Acid        |
| DM                 | Dextromethorphan HBr        |
| Doxyl              | Doxylamine Succinate        |
| DPH                | Diphenhydramine HCl         |
| DSS                | Docusate Sodium             |
| E                  | Vitamin E                   |
| EPA                | Eicosapentaenoic Acid       |
| Ephed              | Ephedrine HCl               |
| Eth                | Ethinyl                     |
| FA                 | Folic Acid                  |
| Fe                 | Iron                        |
| Fe Asp             | Ferrous Aspartate           |
| Fe Asparto Glyc    | Ferrous Asparto Glycinate   |
| Fe Cbnyl           | Iron Carbonly               |
| Fe Fum             | Ferrous Fumarate            |
| Fe Glyc            | Ferrous Glycinate           |
| Fe Polysacch Cmplx | Polysaccharide Iron Complex |
| Fe Prot Succ       | Iron Protein Succinylate    |
| GG                 | Guaifenesin                 |
| Glyc               | Glycinate                   |
| Guaiacol           | Guaiacolsulfonate           |
| HBr                | Hydrobromide                |
| HC                 | Hydrocortisone              |
| HCl                | Hydrochloride               |


C-2 MED-File v2

Published: 11/11

GPI Abbreviation List


| Abbreviation     | Full Name                    |
| ---------------- | ---------------------------- |
| HCTZ             | Hydrochlorothiazide          |
| Hydrocod         | Hydrocodone                  |
| Hydrox           | Hydroxide                    |
| Hyosc            | Hyoscyamine                  |
| I                | Iodine                       |
| IF               | Intrinsic Factor             |
| IFC              | Intrinsic Factor             |
| K                | Potassium                    |
| KCl              | Potassium Chloride           |
| KI               | Potassium Iodide             |
| Lac              | Lactate                      |
| Lip              | Lipase                       |
| Mag              | Magnesium                    |
| Meth Blue        | Methylene Blue               |
| Methamphet       | Methamphetamine HCl          |
| Methenamine Mand | Methenamine Mandelate        |
| Methyltest       | Methyltestosterone           |
| Mg               | Magnesium                    |
| Min              | Minerals                     |
| Mn               | Manganese                    |
| Multivit         | Multivitamins                |
| Na               | Sodium                       |
| NaCl             | Sodium Chloride              |
| PB               | Phenobarbital                |
| PE               | Phenylephrine HCl            |
| PEG              | Polyethylene Glycol          |
| Pentobarb        | Pentobarbital                |
| PETN             | Pentaerythritol Tetranitrate |
| PG               | Paregoric                    |
| Phenid           | Phenindamine Tartrate        |
| Phenir           | Pheniramine Maleate          |
| Phenyl Sal       | Phenyl Salicylate            |
| Phenyleph        | Phenylephrine HCl            |
| Phenylprop       | Phenylpropanolamine HCl      |
| Phenyltolox      | Phenyltoloxamine             |
| Phos             | Phosphate                    |
| Pot              | Potassium                    |
| Pot Guaiacol     | Potassium Guiacolsulfonate   |
| PPA              | Phenylpropanolamine HCl      |
| Prop             | Propionate                   |
| Propoxyphene-N   | Propoxyphene Napsylate       |
| PSE              | Pseudoephedrine              |


Documentation Manual C-3  
Published: 11/11

GPI Name Abbreviations


| Abbreviation | Full Name                |
| ------------ | ------------------------ |
| Pseudoeph    | Pseudoephedrine          |
| Ptolox       | Phenyltoloxamine Citrate |
| Pyril        | Pyrilamine Maleate       |
| Sal          | Salicylate               |
| Salamide     | Salicylamide             |
| Se           | Selenium                 |
| Simeth       | Simethicone              |
| Sod          | Sodium                   |
| Subgal       | Subgallate               |
| Subsal       | Subsalicylate            |
| Tan          | Tannate                  |
| Theo         | Theophylline             |
| Trisil       | Trisilicate              |
| Val          | Valerate                 |
| w/o          | without                  |
| Zn           | Zinc                     |
| Zn Ph        | Zinc Phenol              |


C-4 MED-File v2

Published: 11/11

# Appendix D: Dosage Form Codes

# In This Appendix

Dosage Form Current Values

# Dosage Form Current Values

The Dosage Form indicates the form (solid, liquid, or gas) in which the drug product is dispensed. Dosage Forms are standard throughout every Drug Group.

For more information, see Dosage Form in Chapter 2: Editorial Policies.

Note

Alpha-numeric dosage form values are included in the table below. These values will be phased in over time in new alpha-numeric GPIs during planned GPI change cycles. Consequently, the alpha-numeric dosage forms may not be all-inclusive of their products until the appropriate GPI changes can be made.

Examples include:


| Dosage Form Description          | Code | Abbreviation    | C6  | Comments                                                                                                                   |
| -------------------------------- | ---- | --------------- | --- | -------------------------------------------------------------------------------------------------------------------------- |
| Aerosol                          | AERO | Aerosol         | 32  | An ingredient that is atomized into a fine mist (form unspecified); includes products under pressure and pump sprays.†     |
| Aerosol Powder, Breath Activated | AEPB | Aero Pow Br Act | 80  | A powder-form aerosol (see aerosol) which is activated to induce atomization of the dose by patient inhalation.            |
| Aerosol, Breath Activated        | AERB | Aero Breath Act | 81  | An unspecified or liquid aerosol (see aerosol) which is activated to induce atomization of the dose by patient inhalation. |
| Aerosol, Powder                  | AERP | Aerosol Powder  | 33  | A powder-form aerosol (see aerosol) that is atomized into a fine mist.                                                     |


&nbsp;

Dosage Form Codes


| Dosage Form Description | Code | Abbreviation    | C6  | Comments                                                                                                                                                                                                                                                            |
| ----------------------- | ---- | --------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Aerosol, Solution       | AERS | Aerosol Soln    | 34  | A solution-form aerosol (see aerosol) that is atomized into a fine mist.†                                                                                                                                                                                           |
| Auto-injector           | AUIJ | Auto-injector   | D4  | A medication in an Auto-injector. An Auto-injector is a device that uses a spring-loaded mechanism to drive a hypodermic needle into a patient to a predetermined depth below the skin surface. Drug form unknown.                                                  |
| Auto-injector Kit       | AJKT | Auto-inj Kit    | F5  | A medication in an Auto-injector (see Auto-injector) that is available as a kit.                                                                                                                                                                                    |
| Bar                     | BAR  | Bar             | 35  | A solid dosage form usually in the form of cake or a rectangle (may have a solid or semi-solid interior).                                                                                                                                                           |
| Beads                   | BEAD | Beads           | 36  | A small, solid dosage form in the shape of a small ball.                                                                                                                                                                                                            |
| Capsule                 | CAPS | Capsule         | 01  | A solid dosage form in which the ingredients are enclosed within either a hard or soft soluble container or “shell”. The shells are usually formed from gelatin, but may be made of other suitable substances.†                                                     |
| Capsule Abuse-Deterrent | CAPA | Cap Abuse Deter | A1  | Capsule (see capsule dose form) with abuse-deterrent properties or labeling that use physical or chemical barriers or delivery systems                                                                                                                              |
| Capsule Chewable        | CPCW | Cap Chewable    | F9  | A capsule that is intended to be chewed and then swallowed. Includes chewable capsules that may be either swallowed whole or chewed, based on patient preference and tolerance, as long as the capsule is designed with an option to be chewed prior to swallowing. |
| Capsule Delayed Release | CPDR | Capsule DR      | 65  | A capsule (see capsule) which is designed to delay the release of ingredients until the capsule has passed into a specific region of the gastrointestinal tract.                                                                                                    |


D-2 MED-File v2  
Published: 11/11  
Revised: 06/20

Dosage Form Current Values


| Dosage Form Description              | Code | Abbreviation    | C6  | Comments                                                                                                                                                                                                                                                                                                             |
| ------------------------------------ | ---- | --------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Capsule Delayed Release Particles    | CPEP | Capsule DR Part | 67  | A capsule (see capsule) in which the ingredient particles (beads, pellets, particles, etc.) enclosed in a capsule are enteric coated.                                                                                                                                                                                |
| Capsule Delayed Release Sprinkle     | CSDR | Cap DR Sprinkle | H1  | A capsule (see capsule) which is designed to delay the release of ingredients until the capsule or its contents has passed into a specific region of the gastrointestinal tract. The capsule may be pulled apart and the contents "sprinkled" on food for oral administration. (Depakote Sprinkle)                   |
| Capsule Delayed Release Therapy Pack | CDPK | CPDR Ther Pack  | B3  | Therapy pack with only capsule delayed release dose form.                                                                                                                                                                                                                                                            |
| Capsule ER 12 Hour Abuse-Deterrent   | C12A | Cap 12HR Deter  | A3  | Capsule Extended Release which is designed to release ingredients at a controlled rate (see capsule extended release 12 hour) with abuse-deterrent properties or labeling that use physical or chemical barriers or delivery systems. The dose form is designed to facilitate a 12 hour dosing frequency (interval). |
| Capsule ER 12 Hour Sprinkle          | CS12 | CP12 Sprinkle   | F2  | A capsule extended release which is designed to release ingredients at a controlled rate. The capsule may be pulled apart and the contents "sprinkled" on food for oral administration. The dose form is designed to facilitate a 12 hour dosing frequency (interval).                                               |
| Capsule ER 12 Hour Therapy Pack      | C2PK | CP12 Ther Pack  | B5  | Therapy pack with only capsule release 12 hour dose form.                                                                                                                                                                                                                                                            |


Documentation Manual D-3

Published: 11/11

Revised: 06/20

Dosage Form Codes


| Dosage Form Description                  | Code | Abbreviation    | C6  | Comments                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------- | ---- | --------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Capsule ER 24 Hour Abuse-Deterrent       | C24A | Cap 24HR Deter  | A4  | Capsule Extended Release which is designed to release ingredients at a controlled rate (see capsule extended release 24 hour) with abuse-deterrent properties or labeling that use physical or chemical barriers or delivery systems. The dose form is designed to facilitate a 24 hour dosing frequency (interval). |
| Capsule ER 24 Hour Sprinkle              | CS24 | CP24 Sprinkle   | F3  | A capsule extended release which is designed to release ingredients at a controlled rate. The capsule may be pulled apart and the contents “sprinkled” on food for oral administration. The dose form is designed to facilitate a 24 hour dosing frequency (interval).                                               |
| Capsule ER 24 Hour Therapy Pack          | C4PK | CP24 Ther Pack  | B6  | Therapy pack with only capsule extended release 24 hour dose form.                                                                                                                                                                                                                                                   |
| Capsule Extended Release 12 Hour         | CP12 | Capsule ER 12HR | 69  | A capsule (see capsule) which is designed to release ingredients at a controlled rate. The dose form is designed to facilitate a 12 hour dosing frequency (interval).                                                                                                                                                |
| Capsule Extended Release 24 Hour         | CP24 | Capsule ER 24HR | 70  | A capsule (see capsule) which is designed to release ingredients at a controlled rate. The dose form is designed to facilitate a 24 hour dosing frequency (interval).                                                                                                                                                |
| Capsule Extended Release Abuse-Deterrent | CPEA | Cap ER Deter    | A2  | Capsule Extended Release (see capsule extended release) which releases any part of a dose over an extended period of time due to the release characteristics of the capsule design with abuse-deterrent properties or labeling that use physical or chemical barriers or delivery systems                            |


D-4 MED-File v2  
Published: 11/11  
Revised: 06/20

Dosage Form Current Values


| Dosage Form Description               | Code | Abbreviation    | C6  | Comments                                                                                                                                                                                                                                              |
| ------------------------------------- | ---- | --------------- | --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Capsule Extended Release Sprinkle     | CSER | Cap ER Sprinkle | F1  | A capsule extended release which is designed to release ingredients at a controlled rate. The capsule may be pulled apart and the contents “sprinkled” on food for oral administration.                                                               |
| Capsule Extended Release Therapy Pack | CEPK | CPER Ther Pack  | B4  | Therapy pack with only capsule extended release dose form.                                                                                                                                                                                            |
| Capsule Extended Release*             | CPCR | Capsule ER      | 02  | A capsule (see capsule) which releases any part of a dose over an extended period of time due to the release characteristics of the capsule design. The release rate allows at least a reduction in dosing frequency (various unspecified intervals). |
| Capsule Sprinkle                      | CPSP | Cap Sprinkle    | 68  | A capsule (see capsule), which may be pulled apart and the contents “sprinkled” on food for oral administration. This dosage form also includes sprinkle capsules that are NOT intended to be swallowed whole.                                        |
| Capsule Sprinkle Therapy Pack         | CSPK | CSPK Ther Pak   | H5  | Therapy pack with only capsule sprinkle dose form.                                                                                                                                                                                                    |
| Capsule Therapy Pack                  | CPPK | Cap Ther Pack   | B2  | Therapy pack with only capsule dose form.                                                                                                                                                                                                             |
| Cartridge                             | CART | Cartridge       | E1  | Medication in a cartridge with or without a needle. Drug form unknown.                                                                                                                                                                                |
| Cartridge Kit                         | CTKT | Cartridge Kit   | F7  | Medication in a cartridge with or without a needle available as a kit.                                                                                                                                                                                |
| Concentrate                           | CONC | Concentrate     | 13  | A liquid dose form that is present in a high concentration that may require dilution prior to administration.†                                                                                                                                        |
| Cream                                 | CREA | Cream           | 37  | A semi-solid dosage form containing one or more ingredients that are dissolved or dispersed in a suitable base. Most commonly oil-in-water emulsions or aqueous microcrystalline dispersions of long chain fatty acids or alcohols that are washable. |


Documentation Manual D-5  
Published: 11/11  
Revised: 06/20

Dosage Form Codes


| Dosage Form Description | Code | Abbreviation | C6  | Comments                                                                                                                                                                                                             |
| ----------------------- | ---- | ------------ | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Crystals                | CRYS | Crystals     | 38  | An angular solid of crystalline form.†                                                                                                                                                                               |
| Device                  | DEVI | Device       | 62  | A non-drug item designed for a specific purpose.†                                                                                                                                                                    |
| Diagnostic Test         | TEST | Test         | 60  | A chemical, biological or other test that may be used in conjunction with other diagnostic evidence to formulate a diagnosis, monitor the health of a patient, or evaluate the status of a patient’s disease state.† |
| Diaphragm               | DPRH | Diaphragm    | 54  | A flexible ring covered with a dome-shaped sheet of elastic material.                                                                                                                                                |
| Disk                    | DISK | Disk         | 98  | A circular, plate-like structure.                                                                                                                                                                                    |
| Elixir                  | ELIX | Elixir       | 10  | A clear, sweetened, hydroalcoholic liquid that is commonly used as a vehicle for ingredients intended for oral use†                                                                                                  |
| Emulsion                | EMUL | Emulsion     | 16  | A two-phase system in which one liquid is dispersed throughout another liquid in the form of small droplets.†                                                                                                        |
| Enema                   | ENEM | Enema        | 51  | A liquid preparation intended for rectal instillation (or a solute that may be diluted) for therapeutic, diagnostic or nutritive purposes.                                                                           |
| Exhaler                 | EXHA | Exhaler      | G3  | A breath activated exhalation drug-device combination that deposits drugs high and deep in the nose where the drug form is unknown.                                                                                  |
| Exhaler Liquid          | EXHL | Exhaler Liq  | G5  | A breath activated exhalation drug-device combination that deposits drugs high and deep in the nose where the drug form is a liquid.                                                                                 |
| Exhaler Powder          | EXHP | Exhaler Powd | G4  | A breath activated exhalation drug-device combination that deposits drugs high and deep in the nose where the drug form is a powder.                                                                                 |


D-6 MED-File v2

Published: 11/11

Revised: 06/20

Dosage Form Current Values


| Dosage Form Description | Code | Abbreviation   | C6  | Comments                                                                                                                                                                                                 |
| ----------------------- | ---- | -------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Exhaler Solution        | EXHS | Exhaler Soln   | G6  | A breath activated exhalation drug-device combination that deposits drugs high and deep in the nose where the drug form is a solution.                                                                   |
| Exhaler Suspension      | EXHU | Exhaler Susp   | G7  | A breath activated exhalation drug-device combination that deposits drugs high and deep in the nose where the drug form is a suspension.                                                                 |
| Film                    | FILM | Film           | 82  | A thin, pliable layer intended for solid dosage forms.                                                                                                                                                   |
| Flakes                  | FLAK | Flakes         | 83  | Small, thin pieces of ingredients or food stuffs, which may be aggregates of smaller particles (powder, grain etc.) or parts of a larger piece which has broken off.                                     |
| Fluid Extract           | EXTR | Fl Extract     | 14  | A concentrated preparation of vegetable or animal drugs, extracted from the source material, concentrated by removal of the solvent, then adjusted to prescribed standards.                              |
| Foam                    | FOAM | Foam           | 39  | A gas-bubble infused liquid or semi-solid vehicle with ingredients.                                                                                                                                      |
| Gas                     | GAS  | Gas            | 26  | A liquid entirely in its vapor phase at one atmosphere of pressure because the ambient temperature is above its boiling point.                                                                           |
| Gel                     | GEL  | Gel            | 40  | A semi-solid system consisting of either a suspension made up of small inorganic particles or large organic molecules interpenetrated by a liquid. May be either single-phase or two-phase gel systems.† |
| Gel Forming Solution    | SOLG | Gel Form Soln  | 76  | A solution when upon administration/instillation forms a gel.                                                                                                                                            |
| Granules                | GRAN | Granules       | 27  | A small particle or grain.†                                                                                                                                                                              |
| Granules Effervescent   | GREF | Granules Effer | 77  | Granules (see granules) in a dry mixture which when placed in contact with water have the capability to release gas and cause effervescence.                                                             |


Documentation Manual D-7  
Published: 11/11  
Revised: 06/20

Dosage Form Codes


| Dosage Form Description       | Code | Abbreviation | C6  | Comments                                                                                                                                                                                                                                                                                                                              |
| ----------------------------- | ---- | ------------ | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gum                           | GUM  | Gum          | 28  | An insoluble plastic material from various plant sources which when chewed, releases ingredients into the oral cavity.                                                                                                                                                                                                                |
| Implant                       | IMPL | Implant      | 23  | A solid drug form that is inserted into intact body tissue.                                                                                                                                                                                                                                                                           |
| Inhaler                       | INHA | Inhaler      | 24  | A dose form that is an inhaler/inhalant but is not adequately described by other available dosage forms.                                                                                                                                                                                                                              |
| Injectable                    | INJ  | Injectable   | 22  | Unspecified injectable dose form.†                                                                                                                                                                                                                                                                                                    |
| Insert                        | INST | Insert       | 99  | A solid or semi-solid drug form intended for insertion into body cavity or site.                                                                                                                                                                                                                                                      |
| Intrauterine Device           | IUD  | IUD          | 53  | A device inserted and left in the uterus to prevent effective conception. This device may contain and release an ingredient as part of its contraceptive design.                                                                                                                                                                      |
| Jet-injector (Needleless)     | JTAJ | Jet-injector | D7  | A medication in a Jet-injector. A Jet-Injector is a non-electrically powered device that gives a hypodermic injection by means of a narrow, high velocity jet of fluid which can penetrate the surface of the skin and deliver the fluid to the body without a needle. Drug form unknown.                                             |
| Jet-injector Kit (Needleless) | JTKT | Jet-inj Kit  | F6  | A medication in a Jet-injector (see Jet-injector) that is available as a kit.                                                                                                                                                                                                                                                         |
| Kit                           | KIT  | Kit          | 64  | Products intended for dispensing as a unit. Packaged unit fulfills one of the following: 1) products with at least two different or discrete items (excluding diluents, syringes, needles, adapters, other activation or delivery devices), or 2) packaged with swabs or alcohol wipes, or 3) test meters packaged with test strips.† |


D-8 MED-File v2  
Published: 11/11  
Revised: 06/20

Dosage Form Current Values


| Dosage Form Description  | Code | Abbreviation    | C6       | Comments                                                                                                                           |
| ------------------------ | ---- | --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Leaves                   | LEAV | Leaves          | 97       | Organic material derived from the leafing parts of a plant or plant.†                                                              |
| Liquid                   | LIQD | Liquid          | 09       | Ingredient(s) present in a fluid state.†                                                                                           |
| Liquid Extended-Release* | LQCR | Liquid ER       | 11       | A liquid (see liquid) that has been formulated to allow for an extended release of the ingredient(s).                              |
| Liquid Therapy Pack      | LQPK | Liqd Ther Pack  | C4       | Therapy pack with only liquid dose form.                                                                                           |
| Lotion                   | LOTN | Lotion          | 41       | An unspecified liquid for external application which is commonly a suspension, emulsion or dispersion.†                            |
| Lozenge                  | LOZG | Lozenge         | 47       | A solid preparation which is intended to dissolve or disintegrate slowly in the mouth (usually in a flavored, sweetened base).†    |
| Lozenge on a Handle      | LPOP | Loz on a Handle | 84       | A medicated lozenge on the end of a handle or stick. Intended for oral administration.                                             |
| Miscellaneous            | MISC | Misc            | 63 or 00 | A dose form not described by other database dose forms. Note: C6 values of “00” may also be used in GPIs having this dosage form.† |
| Nebulization Solution    | NEBU | Nebu Soln       | 25       | A solution (see solution) intended to be atomized into a fine mist for inhalation.                                                 |
| Oil                      | OIL  | Oil             | 17       | A liquid that is readily soluble in ether, but not in water.†                                                                      |
| Ointment                 | OINT | Ointment        | 42       | An oil-based semi-solid preparation intended for external application to the skin or mucous membranes.                             |
| Packet                   | PACK | Packet          | 30       | A packet, sachet or unit-of-use of dry powder (see powder) or granules (see granules).†                                            |
| Pads                     | PADS | Pad             | 43       | A fabric based swath of cloth that may or may not be medicated with ingredients.†                                                  |


Documentation Manual D-9

Published: 11/11

Revised: 06/20

Dosage Form Codes


| Dosage Form Description | Code | Abbreviation | C6  | Comments                                                                                                                                                                                                                                                                                                              |
| ----------------------- | ---- | ------------ | --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Paste                   | PSTE | Paste        | 44  | A semi-solid preparation intended for external application (thicker and stiffer than most ointments) or thick, stiff ointments that do not ordinarily flow at body temperature and therefore serve as protective coatings over the areas to which they are applied.                                                   |
| Patch                   | PTCH | Patch        | 59  | A drug delivery system in the form of a patch that releases an ingredient (or ingredients) over time (frequency not specified).                                                                                                                                                                                       |
| Patch 24 HR             | PT24 | Patch 24HR   | 85  | A patch (see patch) with a 24 hour dosing frequency.                                                                                                                                                                                                                                                                  |
| Patch 72 HR             | PT72 | Patch 72HR   | 86  | A patch (see patch) with a 72 hour dosing frequency.                                                                                                                                                                                                                                                                  |
| Patch Twice Weekly      | PTTW | Patch TW     | 87  | A patch (see patch) with a twice-weekly dosing frequency.                                                                                                                                                                                                                                                             |
| Patch Weekly            | PTWK | Patch Weekly | 88  | A patch (see patch) with a weekly dosing frequency.                                                                                                                                                                                                                                                                   |
| Pellet                  | PLLT | Pellet       | 89  | A small solid mass of ingredients made by compression or molding.                                                                                                                                                                                                                                                     |
| Pen-injector            | PEN  | Pen-injector | D1  | A medication in a Pen-injector. A Pen-injector is a device that provides a non-electrically-powered, mechanically-operated method of accurately injecting a dose of medicinal product from a medicinal cartridge, reservoir, or syringe through a manually-inserted single lumen hypodermic needle. Drug form unknown |
| Pen-injector Kit        | PNKT | Pen-inj Kit  | F4  | A medication in a Pen-injector (see Pen-injector) that is available as a kit.                                                                                                                                                                                                                                         |
| Powder                  | POWD | Powder       | 29  | A mixture of dry, finely divided ingredients and/or chemicals.†                                                                                                                                                                                                                                                       |
| Powder Effervescent     | PDEF | Powder Effer | 78  | Powder (see powder) which when placed in contact with water has the capability to release gas and cause effervescence.                                                                                                                                                                                                |


D-10 MED-File v2

Published: 11/11

Revised: 06/20

Dosage Form Current Values


| Dosage Form Description | Code | Abbreviation    | C6  | Comments                                                                                                                                                                                                                                                             |
| ----------------------- | ---- | --------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prefilled Syringe       | PRSY | Prefilled Syr   | E4  | Medication in a prefilled syringe. Drug form unknown.                                                                                                                                                                                                                |
| Prefilled Syringe Kit   | PSKT | Prefill Syr Kit | F8  | Medication in a prefilled syringe available as a kit.                                                                                                                                                                                                                |
| Pudding                 | PUDG | Pudding         | 79  | A sweet and flavored, thick, semi-solid food.                                                                                                                                                                                                                        |
| Ring                    | RING | Ring            | 90  | A round, circular structure that may be flexible or rigid.                                                                                                                                                                                                           |
| Shampoo                 | SHAM | Shampoo         | 45  | A liquid soap or detergent used to clean the hair and scalp that is often used as a vehicle for dermatologic agents.^{†}                                                                                                                                             |
| Sheet                   | SHEE | Sheet           | 91  | A solid dose form in a relatively thin layer of fiber or fabric.^{†}                                                                                                                                                                                                 |
| Solution                | SOLN | Solution        | 20  | A liquid preparation that contains one or more chemical substances dissolved, i.e., molecularly dispersed, in a suitable solvent or mixture of mutually miscible solvents.^{†}                                                                                       |
| Solution Auto-injector  | SOAJ | Soln Auto-inj   | D5  | A solution in an Auto-injector. An Auto-injector is a device that uses a spring-loaded mechanism to drive a hypodermic needle into a patient to a predetermined depth below the skin surface.                                                                        |
| Solution Cartridge      | SOCT | Soln Cartridge  | E2  | Solution in a cartridge with or without a needle.                                                                                                                                                                                                                    |
| Solution Jet-injector   | SOTJ | Soln Jet-inj    | D8  | A solution in a jet-injector. A Jet-injector is a non-electrically powered device that gives a hypodermic injection by means of a narrow, high velocity jet of fluid which can penetrate the surface of the skin and deliver the fluid to the body without a needle. |


Documentation Manual D-11

Published: 11/11

Revised: 06/20

Dosage Form Codes


| Dosage Form Description    | Code | Abbreviation   | C6  | Comments                                                                                                                                                                                                                                                                                          |
| -------------------------- | ---- | -------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Solution Pen-injector      | SOPN | Soln Pen-inj   | D2  | A solution in a Pen-injector. A Pen-injector is a device that provides a non-electrically-powered, mechanically-operated method of accurately injecting a dose of medicinal product from a medicinal cartridge, reservoir, or syringe through a manually-inserted single lumen hypodermic needle. |
| Solution Prefilled Syringe | SOSY | Soln Pref Syr  | E5  | Solution in a prefilled syringe.                                                                                                                                                                                                                                                                  |
| Solution Reconstituted     | SOLR | For Solution   | 21  | Dry powder (see powder) or granules (see granules) which upon the addition of a suitable vehicle, yields a solution (see solution).†                                                                                                                                                              |
| Solution Therapy Pack      | SOPK | Soln Ther Pack | C5  | Therapy pack with only solution dose form.                                                                                                                                                                                                                                                        |
| Spirit                     | SPRT | Spirit         | 92  | Alcoholic or hydroalcoholic solutions of volatile substances                                                                                                                                                                                                                                      |
| Stick                      | STCK | Stick          | 93  | A dosage form prepared in a relatively long and slender often cylindrical form.†                                                                                                                                                                                                                  |
| Strip                      | STRP | Strip          | 61  | A long, flat, narrow piece of material that may be impregnated or coated with testing reagents.†                                                                                                                                                                                                  |
| Suppository                | SUPP | Suppository    | 52  | A solid body of various weights and shapes, adapted for introduction into the rectal, vaginal or urethral orifice of the human body; they usually melt, soften or dissolve at body temperature.                                                                                                   |
| Suspension                 | SUSP | Suspension     | 18  | A liquid preparation which consists of solid particles dispersed throughout a liquid phase in which the particles are not soluble.†                                                                                                                                                               |
| Suspension Auto-injector   | SUAJ | Susp Auto-inj  | D6  | A suspension in an auto-injector. An Auto-injector is a device that uses a spring-loaded mechanism to drive a hypodermic needle into a patient to a predetermined depth below the skin surface.                                                                                                   |
| Suspension Cartridge       | SUCT | Susp Cartridge | E3  | Suspension in a cartridge with or without a needle.                                                                                                                                                                                                                                               |


D-12 MED-File v2

Published: 11/11

Revised: 06/20

Dosage Form Current Values


| Dosage Form Description      | Code | Abbreviation   | C6  | Comments                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------- | ---- | -------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Suspension Extended Release  | SUER | Suspension ER  | G1  | A suspension which releases any part of a dose over an extended period of time due to the release characteristics of the suspension design. The release rate allows at least a reduction in dosing frequency (various unspecified intervals).                                                                                                            |
| Suspension Jet-injector      | SUTJ | Susp Jet-inj   | D9  | A suspension in a jet-injector. A Jet-Injector is a non-electrically powered device that gives a hypodermic injection by means of a narrow, high velocity jet of fluid which can penetrate the surface of the skin and deliver the fluid to the body without a needle.                                                                                   |
| Suspension Pen-injector      | SUPN | Susp-Pen-inj   | D3  | A suspension in a Pen-injector. A Pen-injector is a device that provides a non-electrically-powered, mechanically-operated method of accurately injecting a dose of medicinal product from a medicinal cartridge, reservoir, or syringe through a manually-inserted single lumen hypodermic needle.                                                      |
| Suspension Prefilled Syringe | SUSY | Susp Pref Syr  | E6  | Suspension in a prefilled syringe.                                                                                                                                                                                                                                                                                                                       |
| Suspension Reconstituted     | SUSR | For Suspension | 19  | A dry powder (see powder) or granules (see granules) which upon the addition of a suitable vehicle, yields a suspension (see suspension).†                                                                                                                                                                                                               |
| Suspension Reconstituted ER  | SRER | For Susp ER    | G2  | A dry powder (see powder) or granules (see granules) which upon the addition of a suitable vehicle yields a suspension which releases any part of a dose over an extended period of time due to the release characteristics of the dosage form design. The release rate allows at least a reduction in dosing frequency (various unspecified intervals). |
| Suspension Therapy Pack      | SUPK | Susp Ther Pack | C6  | Therapy pack with only suspension dose form.                                                                                                                                                                                                                                                                                                             |


Documentation Manual D-13

Published: 11/11

Revised: 06/20

Dosage Form Codes


| Dosage Form Description          | Code | Abbreviation    | C6  | Comments                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------- | ---- | --------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Swab                             | SWAB | Swab            | 94  | A cotton or other fabric applicator that is used alone or attached to (usually wrapped around) the end of a stick.                                                                                                                                                                                                                                                                                                             |
| Syrup                            | SYRP | Syrup           | 12  | An oral solution containing high concentrations of sucrose, other sugars or sorbitol; the term has also been used to include any other liquid dosage form prepared in a sweet and viscid vehicle.†                                                                                                                                                                                                                             |
| Tablet                           | TABS | Tablet          | 03  | A solid dosage form containing ingredients with or without suitable diluents.†                                                                                                                                                                                                                                                                                                                                                 |
| Tablet Abuse-Deterrent           | TABA | Tab Abuse Deter | A5  | Tablet (see tablet dose form) with abuse-deterrent properties or labeling that use physical or chemical barriers or delivery systems.                                                                                                                                                                                                                                                                                          |
| Tablet Chewable                  | CHEW | Tablet Chewable | 05  | A tablet (see tablet) that is intended to be chewed and then swallowed. Includes chewable tablets that may be either swallowed whole or chewed, based on patient preference and tolerance, as long as the tablet is designed with an option to be chewed prior to swallowing.†                                                                                                                                                 |
| Tablet Chewable Extended Release | CHER | Tablet ER Chew  | H2  | A tablet (see tablet) that is intended to be chewed and then swallowed and releases any part of a dose over an extended period of time due to the release characteristics of the chewable tablet design. Includes chewable tablets that may be either swallowed whole or chewed, based on patient preference and tolerance, as long as the tablet is designed with an option to be chewed prior to swallowing. (Quillichew ER) |
| Tablet Delayed Release           | TBEC | Tablet DR       | 06  | A tablet (see tablet) which is coated to prevent release of the ingredient(s) until it passes the low pH environment of the stomach in the gastrointestinal tract.                                                                                                                                                                                                                                                             |


D-14 MED-File v2  
Published: 11/11  
Revised: 06/20

Dosage Form Current Values


| Dosage Form Description               | Code | Abbreviation      | C6  | Comments                                                                                                                                                                                                                                                                                                           |
| ------------------------------------- | ---- | ----------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Tablet Delayed Release Disintegrating | TBDD | Tab DR Disint     | H3  | A tablet (see Tablet) which disintegrates when placed upon the tongue or in the mouth and that utilizes coated particles that prevent release of the ingredient(s) until they pass the low pH environment of the stomach in the gastrointestinal tract.                                                            |
| Tablet Delayed Release Therapy Pack   | TDPK | TBDR Ther Pack    | B8  | Therapy pack with only tablet delayed release dose form.                                                                                                                                                                                                                                                           |
| Tablet Disintegrating                 | TBDP | Tablet Disint     | 72  | A tablet (see tablet) containing a drug (or drugs) which disintegrates when placed upon the tongue or in the mouth.†                                                                                                                                                                                               |
| Tablet Disintegrating Soluble         | TB3D | Tab Disint Sol    | G8  | A tablet designated to disintegrate in the mouth with a sip of liquid or dissolve in a liquid prior to administration (such as a 3-dimensional printed [3DP] tablet).                                                                                                                                              |
| Tablet Disintegrating Soluble ER      | TB3E | Tablet Dis Sol ER | G9  | An extended release tablet designed to disintegrate in the mouth with a sip of liquid prior to administration (such as a 3-dimensional printed [3DP] tablet).                                                                                                                                                      |
| Tablet Disintegrating Therapy Pack    | TPPK | TBDP Ther Pack    | B9  | Therapy pack with only tablet disintegrating dose form.                                                                                                                                                                                                                                                            |
| Tablet Effervescent                   | TBEF | Tablet Effer      | 08  | A tablet (see tablet) which releases gas when dissolved in water causing effervescence; it is intended to be dissolved or dispersed in water before administration.                                                                                                                                                |
| Tablet ER 12 Hour Abuse-Deterrent     | T12A | Tab 12HR Deter    | A7  | Tablet Extended Release which is designed to release ingredients at a controlled rate (see tablet extended release 12 hour) with abuse-deterrent properties or labeling that use physical or chemical barriers or delivery systems. The dose form is designed to facilitate a 12 hour dosing frequency (interval). |


Documentation Manual D-15

Published: 11/11

Revised: 06/20

Dosage Form Codes


| Dosage Form Description                 | Code | Abbreviation   | C6  | Comments                                                                                                                                                                                                                                                                                                           |
| --------------------------------------- | ---- | -------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Tablet ER 12 Hour Therapy Pack          | T2PK | TB12 Ther Pack | C2  | Therapy pack with only tablet extended release 12 hour dose form.                                                                                                                                                                                                                                                  |
| Tablet ER 24 Hour Abuse-Deterrent       | T24A | Tab 24HR Deter | A8  | Tablet Extended Release which is designed to release ingredients at a controlled rate (see tablet extended release 24 hour) with abuse-deterrent properties or labeling that use physical or chemical barriers or delivery systems. The dose form is designed to facilitate a 24 hour dosing frequency (interval). |
| Tablet ER 24 Hour Therapy Pack          | T4PK | TB24 Ther Pack | C3  | Therapy pack with only tablet extended release 24 hour dose form.                                                                                                                                                                                                                                                  |
| Tablet Extended Release 12 HR*          | TB12 | Tablet ER 12HR | 74  | A tablet (see tablet) which is designed to release ingredients at a controlled rate. The dose form is designed to facilitate a 12 hour dosing frequency (interval).                                                                                                                                                |
| Tablet Extended Release 24 HR*          | TB24 | Tablet ER 24HR | 75  | A tablet (see tablet) which is designed to release ingredients at a controlled rate. The dose form is designed to facilitate a 24 hour dosing frequency.                                                                                                                                                           |
| Tablet Extended Release Abuse-Deterrent | TBEA | Tab ER Deter   | A6  | Tablet Extended Release (see tablet extended release) which releases any part of a dose over an extended period of time due to the release characteristics of the tablet design with abuse-deterrent properties or labeling that use physical or chemical barriers or delivery systems.                            |
| Tablet Extended Release Disintegrating  | TBED | Tab ER Disint  | H4  | A tablet (see Tablet) that disintegrates when placed upon the tongue or in the mouth and that utilizes particles that release over an extended period of time due to the release characteristics of the particles.                                                                                                 |
| Tablet Extended Release Therapy Pack    | TEPK | TBER Ther Pack | C1  | Therapy pack with only tablet extended release dose form.                                                                                                                                                                                                                                                          |


D-16 MED-File v2

Published: 11/11

Revised: 06/20

Dosage Form Current Values


| Dosage Form Description | Code | Abbreviation   | C6  | Comments                                                                                                                                                                                                                                           |
| ----------------------- | ---- | -------------- | --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tablet Extended-Release | TBCR | Tablet ER      | 04  | A tablet (see tablet) which releases any part of a dose over an extended period of time due to the release characteristics of the tablet design. The release rate allows at least a reduction in dosing frequency (various unspecified intervals). |
| Tablet Soluble          | TBSO | Tablet Soluble | 73  | A tablet (see tablet) that is usually dissolved in a liquid prior to administration.†                                                                                                                                                              |
| Tablet Sublingual       | SUBL | Tab Sublingual | 07  | A tablet (see tablet) that is administered sublingually.                                                                                                                                                                                           |
| Tablet Therapy Pack     | TBPK | Tab Ther Pack  | B7  | Therapy pack with only tablet dose form.                                                                                                                                                                                                           |
| Tampon                  | TAMP | Tampon         | 58  | Pack or plug made of cotton, sponge or oakum; may contain a drug.                                                                                                                                                                                  |
| Tape                    | TAPE | Tape           | 46  | A narrow woven fabric, or plastic, usually with an adhesive on one or both sides.†                                                                                                                                                                 |
| Tar                     | TAR  | Tar            | 95  | A tarry substance.                                                                                                                                                                                                                                 |
| Therapy Pack            | THPK | Therapy Pack   | B1  | Therapy pack with multiple dose forms.                                                                                                                                                                                                             |
| Tincture                | TINC | Tincture       | 15  | An alcoholic or hydroalcoholic solution prepared from vegetable materials or from chemical substances.                                                                                                                                             |
| Troche                  | TROC | Troche         | 48  | A discoid-shaped solid containing the medicinal agent in a suitable flavored base; troches are placed in the mouth where they slowly dissolve, liberating the active ingredients.                                                                  |
| Wafer                   | WAFR | Wafer          | 31  | A thin slice of material containing a medicinal agent.                                                                                                                                                                                             |
| Wax                     | WAX  | Wax            | 96  | Paraffin from an animal or insect source.                                                                                                                                                                                                          |


Note

- CR and SR designate controlled release dosage forms but do not quantify the type of release mechanism.

† For Dosage Form Descriptions that include a ‘†’, the Dosage Form for the product can differ from the dosage form that can be inferred from the C6 of the GPI. The marked records can change without notice.

Documentation Manual D-17  
Published: 11/11  
Revised: 06/20