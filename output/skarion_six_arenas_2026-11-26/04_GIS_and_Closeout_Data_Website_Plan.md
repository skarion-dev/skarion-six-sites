# SkarionGIS website and social plan

**Manual review draft · November 26, 2026 · Pursue now**

SkarionGIS is the GIS and closeout offer within Skarion Engineering. Start with two services that can be defined and accepted as batches. For fiber builders, turn approved redlines, field records and test references into owner-ready GIS. For utility teams, convert and clean up asset records against the owner's data schema. The two services share a review process and an editable handoff.

The current GIS/VETRO page describes GIS processing with Esri, QGIS and VETRO, parcel and ROW context, and converting records into a client schema. The proposed primary page is `/services/gis-closeout`. After the team approves the new page and the new route is live, update navigation and internal links and redirect `/gis-vetro-support`. Keep the group domain decision in the portfolio domain plan. [Current Skarion Engineering GIS/VETRO page](https://skarionengineering.com/gis-vetro-support)

## Buyer and offer

| Buyer | Trigger | First scoped package | Acceptance |
| --- | --- | --- | --- |
| Fiber prime project manager, ISP construction coordinator or GIS lead | An area is ready to close, mapping backlog is holding up turnover, or handoff files lack common IDs | Convert one map area or roughly 30 features from approved source records. Deliver editable line and point features, agreed attributes, a source-to-asset crosswalk and an exception log. Link photos, splice references and tests when supplied and approved. | Client can open and import the agreed data format, trace features to sources, and review exceptions against the closeout checklist. |
| Utility GIS manager, operations lead or utility engineering prime | A batch of legacy CAD or PDFs needs conversion, or field edits and asset IDs disagree | Convert one defined asset class or small batch of water or sewer records. Deliver an editable layer, a data dictionary or source-to-target field crosswalk, an edit log and issues for client review. | Client can validate attributes, record provenance, agreed geometry rules and the fields that require owner or field review. |
| Repeat buyers with a steady update queue | Accepted pilot reveals recurring as-built edits or migration preparation | Propose recurring batch updates, ID remediation and migration readiness after the pilot. | Each batch has an intake cutoff, approved schema and validation criteria. Changes with operational implications route to the owner. |

The first quote should state the batch boundary, source revisions, expected feature types and count, coordinate reference system, target format and schema version, reviewer, and exclusions. Price complex tracing and exception remediation after sampling. Final survey, locating, engineering approval, full network implementation and production edits each require their own scope, access and responsible party.

## Website structure and copy

| Page block | Draft content and team action |
| --- | --- |
| Hero | **GIS and closeout data your team can edit and audit.** Turn approved redlines, asset records and field files into editable GIS, a source crosswalk and a QA exception log. Primary CTA **Scope a GIS batch**. Secondary CTA **Review a sample handoff** once a sample has passed review. |
| Route users by job | **Fiber closeout** for a network area, route or build package. **Utility asset data** for converting, cleaning and reconciling one asset class or work area. |
| What you receive | Show an annotated handoff manifest with editable layers, ID and attribute crosswalk, exception register and a map PDF. Confirm export format from the intake, such as a file geodatabase, GeoPackage, CSV or KMZ. Put ArcGIS, QGIS and VETRO under **Supported workflows**, once the team confirms which native import and export jobs it can support. |
| How the batch works | **Agree the template → Map and attribute → Review exceptions → Hand off for acceptance.** Show both the production action and the buyer's approval checkpoint for each step. |
| Sample handoffs | Two draft sample cards below, with a stable “sample data” label, annotated files and a short review checklist. Keep competitor references in this internal plan. Use a third sample only if a common intake problem calls for it. |
| QA and access | State how the team records uncertain inputs, checks IDs and geometry against the owner specification, validates an import and shares through client-approved storage. Add a short FAQ on input types, standards, open exceptions and buyer approval. |
| Contact | Put **Scope a GIS batch** above the footer. Keep general contact, service navigation and parent brand in the shared Skarion Engineering interface. |

The form can collect company, work email, owner or prime role, location, asset types and approximate count, available source types, target system or format, desired deadline and time zone, and who approves acceptance. Ask whether an owner template or data residency requirement applies. Offer a client-approved secure exchange after scoping. Keep sensitive utility maps and field evidence out of the public form.

## Third-party projects for review

These cases document specific workflows buyers already encounter. Review scope and presentation for the SkarionGIS samples and keep external attribution in draft review materials.

| Reference project | Documented scope and what to take into review |
| --- | --- |
| Snoqualmie Pass Utility District · FLO Analytics | Built a water and sewer infrastructure GIS database using field collection and configured its ArcGIS Online environment. Show the asset-to-source path and how staff can use the layer after handoff. [FLO project](https://flo-analytics.com/projects/infrastructure-database-development-snoqualmie-pass-utility-district) |
| OWASA · Timmons Group and Esri | Migrated to ArcGIS Utility Network and maintained connections with work management and other operational tools. For the sample, make the owner workflow and test import explicit. [Esri case](https://www.esri.com/en-us/industries/blog/articles/owasa-arcgis-utility-network-implementation) |
| Greer Commission of Public Works · SSP Innovations | Described a staged natural gas migration with separate testing before production. Adapt the staging and review step for smaller GIS batches. [SSP project](https://sspinnovations.com/projects/greer-cpw-preserves-47-years-of-institutional-knowledge-through-utility-network-migration/) |
| ImOn Duluth Phase II · HR Green | Disclosed GIS engineering, field data collection and easement support in a planned fiber expansion. Borrow the separation of each delivery role so a closeout customer can tell where GIS production begins. [HR Green project update](https://www.hrgreen.com/news/imon-advances-fiber-expansion-across-northeastern-minnesota/) |
| Sandisfield · CAI Technologies | Described updating map layers and configuring a Field Maps workflow to collect assets. Show how changes made to one source propagate to a new batch and retain their provenance. [CAI project](https://www.cai-tech.com/sandisfield-ma-axisgis-assessing-dynamic-map-layers-and-editor-service/) |
| Lubbock County · Halff | Helped implement an asset management system connecting roadway and sign inventory to field work and work orders. Use one concrete downstream task to explain why an accurate asset ID matters. [Halff project](https://halff.com/project/lubbock-asset-mgmt-software-implementation/) |
| Cumberland Connect · VETRO | Showed a fiber operator using the FiberMap platform across engineering and network operations. Adapt the idea of a clearly labeled editable inventory and scope any VETRO import against the customer's access and schema. [VETRO customer case](https://vetrofibermap.com/case-study-cumberland-connect-bridging-the-digital-divide-with-vetro-fibermap/) |
| San Antonio Water System · Safe Software case | Described CAD and tabular source conversion with interoperability tooling. Explain which fields transfer, which require a decision and who reviews them. [Safe Software case PDF](https://cdn.safe.com/resources/case-studies/CaseStudy_SAWS.pdf) |
| Detroit DWSD · Technology Digest contract 6007082 | An owner-side award record documents as-needed GIS support, including prior creation of water and sewer asset as-builts using field references. Use this as a buyer scope precedent when reviewing the utility offer. [DWSD award record](https://dwsd.legistar.com/LegislationDetail.aspx?FullText=1&GUID=B03CFC69-29C8-460E-BA01-8FAD409AC75F&ID=7294137&Options=&Search=) |
| City of Novi · OHM Advisors | The client had digitized as-built drawings and GPS records of uneven or undocumented quality. OHM describes updating that GIS and collecting new field data. The sample should make source confidence and field verification status visible at the feature level. [OHM project](https://www.ohm-advisors.com/projects/city-novi-gis-asset-data-collection-mapping) |

The clearest closeout wording in the peer set names the handoff files, field evidence, asset attributes and what the buyer still has to review. The Fiber Construction Company as-built page and GDRS telecom page are useful for this review. GEO Jobe's tiered utility support is a separate pattern for handling a repeat batch queue. [Fiber Construction Company](https://fiberconstructioncompany.com/engineering/as-built-documentation.html) · [GDRS](https://gdrsgeo.com/telecom-broadband.html) · [GEO Jobe](https://geo-jobe.com/professional-services/gis-services/utilities/)

## Team sample projects

| Draft sample | Team build | Acceptance and manual review |
| --- | --- | --- |
| **Fiber closeout from redline to owner inventory** · Synthetic data · Internal review | Make a simulated FTTH segment of about 30 assets, an approved-redline substitute, line and point layers, sample splice and photo-reference records, and an editable handoff with a static map PDF. Include a source ID and revision on each edited asset, a source-to-GIS crosswalk and contrasting examples of an accepted edit and an open discrepancy. | GIS reviewer checks unique IDs, approved coordinate reference system, schema, trace to source records and test import. OSP reviewer checks the feature classifications and makes sure an open source discrepancy stays open. Website reviewer checks the sample label and public file contents. |
| **Utility asset records from drawings to an editable layer** · Synthetic data · Internal review | Create a small municipal water or sewer example with about 25 records. Include sample asset IDs, duplicate or conflicting evidence, incomplete attributes, an attribute dictionary and a logged reviewer decision. Deliver editable layers, an asset crosswalk, an issue register and the export version. | Utility reviewer validates the chosen attributes and how an unresolved location or classification is shown. GIS reviewer confirms record counts and asset ID traceability and tests the target import. Website reviewer checks that the map and file metadata carry synthetic-data labels. |
| **Recurring update queue** · Optional after pilot review | Create a follow-up mini batch from the same synthetic sample. Show how a new revision changes the asset, how edits are reconciled and how unresolved records are carried forward. | A second reviewer verifies the delta against the previous export and can reproduce the changed feature list. |

The producer builds each sample, a second technical reviewer tests the handoff, and the website owner approves wording and attachments for use. Check sample labels, basemap and imagery permissions, app/tool claims, file metadata and downloads for publication. Use third-party project images or client work only with permission and an accurate description of Skarion's role.

## Delivery QA and access

1. Agree source revisions, field definitions, spatial reference, precision requirements, hierarchy for conflicting evidence and who can accept the package.
2. Preserve originals and link edits to source file and feature or sheet identifier. Preserve unknown and conflicting records for review with status, question and responsible reviewer.
3. Check unique IDs, required fields, valid codes, geometry and topology against owner rules, relationship keys and existence of approved attachments. Compare areas with the supplied drawing or field evidence through a visual spot check.
4. Test the target import in a staging environment or validate the agreed exchange export. Record issue counts, decisions and final revision in a manifest, then send approval through the agreed review channel.
5. Use client-approved exchange and permissions scoped to named reviewers. Confirm licensing for basemap/context material and retention or deletion terms for project data.

## Social first month

Start with two Skarion Engineering LinkedIn posts in Week 1. Continue with two weekly slots as the team clears the corresponding assets. The first audience is fiber and utility delivery leads and the second is prime PMs and GIS managers. A technical owner approves each graphic and claim.

| Week | Hook and asset | CTA |
| --- | --- | --- |
| 1 | **One redline, three records your closeout team can trace.** Annotate a synthetic as-built sample. **Can your owner open your closeout file?** Share a short checklist for schema, format and reviewer. | Review sample or ask about a batch. |
| 2 | **What we log when the GIS and the drawing disagree.** Share a synthetic exception card. **What it takes to quote a 30-feature batch.** List sources, asset count, schema and approval owner. | Request an intake checklist. |
| 3 | **A utility layer your operations team can update.** Show a before/after water or sewer record. **How a source revision follows an asset.** Walk through one ID and attachment trail. | Discuss a utility records batch. |
| 4 | **How an owner checks a GIS export.** Show the staging review and acceptance summary. **Which edits belong in a recurring queue?** Share a small version and delta example. | Scope a batch or discuss repeat work. |

Timmons pairs a specific client story with a project link. Cloudpoint opens with a data-readiness question and points to a concrete assessment. CCI and VETRO are references for language aimed at operators and engineering teams. Use these as format references and review any borrowed facts or imagery before publishing. Benchmark links cover examples and public profiles. Posting cadence and engagement metrics were outside the comparison. [Timmons LinkedIn example](https://www.linkedin.com/posts/timmons-group_gis-utilities-equityinaction-activity-7271923678030794752-RhyA) · [Cloudpoint LinkedIn example](https://www.linkedin.com/posts/cloudpointgeospatial_is-your-data-ready-for-the-arcgis-utility-activity-7468014740448034817-okOe) · [CCI Systems](https://www.linkedin.com/company/ccisystems/) · [VETRO](https://www.linkedin.com/company/vetrofibermap/)

Track qualified batch inquiries, sample-to-inquiry clicks where tracking is available, accepted paid pilots and repeat batch requests. For each pilot, record feature count, time by intake/production/QA, open defects at first review and measured rework. Review which offer creates repeat batches and which scopes need owner decisions earlier.

The [GIS comparison register](04_gis_closeout.json) contains 50 delivery businesses and primes plus 11 adjacent platforms or data vendors. It includes 18 named project or award references and 11 public profile or post links. Use the segment field when comparing capabilities and offers.
