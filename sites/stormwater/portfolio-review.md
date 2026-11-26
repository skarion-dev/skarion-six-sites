# Skarion Stormwater portfolio review

**Stage:** Internal manual review. The portfolio owner keeps technical acceptance and rights approval for every publication candidate.

## Peer projects to inspect

| Source | What to study | Implication for the Skarion sample |
| --- | --- | --- |
| [Weston & Sampson, Bowie stormwater GIS build-out](https://www.westonandsampson.com/projects/stormwater-gis-build-out) | As-built sheets, image indexing and digitized drainage asset scope. | Build a manifest with input, accepted and exception counts. |
| [SAM, Topeka storm sewer inspection and mapping](https://www.sam.biz/projects/topeka-storm-sewer-inspection-and-mapping/) | Facility IDs linking the GIS inventory to Cityworks. | Include an owner identifier and retain source keys. Test a duplicate and legacy alias. |
| [Gradient, Henderson asset inventory and condition assessment](https://gradientnc.com/case-study/stormwater-asset-inventory-and-condition-assessment-city-of-henderson/) | Condition methodology tied to the owner platform. | Keep the observation, applied rule version and reviewer decision in separate fields. |
| [McAdams, Apex stormwater system condition assessment](https://mcadamsco.com/projects/stormwater-system-condition-assessment) | Phased field mapping and dashboards for priority areas. | Prototype decision views after validating the map and source data. |
| [TREKK, Columbia stormwater asset inventory](https://trekkllc.com/columbia-stormwater-asset-inventory/) | Identification of features previously marked unknown. | Retain an unresolved example and document the evidence needed to change it. |
| [volerGROUP, Seminole County East Basins](https://www.voler.group/projects-1/seminole-county-east-basins) | Survey and GIS production within a wider prime-led basin study. | Describe Skarion's work package, the prime's review and the accepted handoff. |
| [WSB, Tulsa storm sewer assessment program](https://www.wsbeng.com/projects/tulsa-storm-sewer-assessment-program/) | A single-basin pilot that informed phased delivery. | Name deliverable checks and the decision to expand the scope. |
| [Halff, Sheppard Air Force Base stormwater survey](https://halff.com/news-insights/insights/case-study-sheppard-afb-stormwater-survey/) | Field confirmation and GIS information prepared for further analysis. | Distinguish input accuracy, record gaps and reviewer-approved updates. |

These are public peer references from the stormwater comparison research. Keep firm names, source imagery and claims attributed to their owners. Use original work in Skarion portfolio examples.

## Original samples to build

| Sample | Build owner and output | Acceptance |
| --- | --- | --- |
| Basin 07 inventory | GIS production lead. Prepare 40 fictional features with source records, a map PDF, editable layers, a data dictionary and an exception register. Reuse IN-104, MH-208 and P-209 as crosswalk examples. | No duplicate released IDs. Correct geometry and schema. Source key or documented exception for every feature. Unresolved P-209 stays flagged. |
| CCTV record reconciliation | Closeout data lead. Build a fictional relationship table with an alias, an orphan and a contradictory observation. Add a short change report. | Exact and uncertain matches are traceable. Attachments can be reopened. Inspection grades and their source remain visible. |
| Rural culvert register | Drainage GIS lead. Prepare 25 fictional culverts with photo keys and owner-approved attribute lists. Include one unknown outlet and a mismatched road reference. | No invented field confirmation. The prime's reviewer owns the missing outlet and road decision. |

The current [map exhibit](assets/basin-map.svg) and crosswalk are an original visual sketch. They show fictional records and require review before use on a public website.

## Manual review

1. The GIS lead checks geometry, coordinate system, field names, IDs and asset-to-source links.
2. The civil reviewer checks terms, connection states, condition provenance and the boundary between inventory production and engineering analysis.
3. The delivery lead signs off on the agreement for feature count, source types, destination format, review round and acceptance.
4. The content lead checks source attribution, redactions, image rights, title blocks and the synthetic label.
5. The portfolio owner records the decision and confirms scope before release.
