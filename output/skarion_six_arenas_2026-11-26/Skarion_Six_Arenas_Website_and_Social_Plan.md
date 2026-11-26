# Skarion Engineering six-arena website and social plan

**Internal planning handoff · November 26, 2026**

Use **one Skarion Engineering website, six branded landing pages and six matching `.com` domains**. The existing `skarionengineering.com` site already presents OSP design, GIS, permitting and multidisciplinary drafting. Extend those services into clear buyer-facing offers with one navigation, one intake form and one shared delivery process. Each service domain can redirect to its matching page once that page is approved. Use **SkarionGIS** exactly as the GIS brand name. [Existing Skarion Engineering website](https://skarionengineering.com/) · [Google guidance on permanent redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

The four active lanes are OSP fiber design, utility bid estimating, CAD drafting and as-builts, and GIS and closeout data. Lighting and stormwater are 30-day pilots. The website briefs contain third-party projects for benchmarking and separate Skarion sample project briefs for manual review.

## The six offers

| Arena and working name | Phase | First package | Conversion action | Proposed parent-site route |
|---|---|---|---|---|
| **OSP fiber design · Skarion Fiber** | Pursue now | One approved fiber route converted into review-ready low-level design plans, construction details and materials schedules. | Request a route design pilot | `/services/osp-fiber-design` |
| **OSP and utility bid estimating · Skarion Estimating** | Pursue now | One bid package with traceable quantities, annotated bid sheets, exclusions and an addendum log. Offer priced estimates after an experienced estimator verifies local labor, equipment, productivity and supplier inputs. | Scope a takeoff | `/services/utility-bid-estimating` |
| **CAD drafting and as-builts · Skarion Drafting** | Pursue now | A batch of approved field redlines converted into native CAD, review PDFs and a checked record set. | Request a drawing batch | `/services/cad-drafting-as-builts` |
| **GIS and closeout data · SkarionGIS** | Pursue now | One route or asset layer reconciled against source records, with editable GIS, source references and an exception log. | Scope a GIS or closeout batch | `/services/gis-closeout` |
| **Lighting and photometrics · Skarion Lighting** | 30-day pilot | One site layout, photometric calculation plots and fixture schedule from approved geometry, IES files and performance criteria. | Join the lighting pilot review | `/services/lighting-photometrics` |
| **Stormwater support · Skarion Stormwater** | 30-day pilot | A stormwater asset inventory and record reconciliation batch with mapped structures, photos and a missing-data register. | Scope a stormwater inventory pilot | `/services/stormwater-support` |

## Domain decision and registration plan

Verisign’s public `.com` registry returned **HTTP 404** for the six primary candidates during the November 26 checks. That means the lookup returned no public registration record. Confirm availability, premium status and the final renewal price in the registrar’s search immediately before purchase. The `.com` list price checked at Porkbun was **$11.81** per name for a standard non-premium registration and renewal, or **$70.86** for six at that price. Cloudflare Registrar is another at-cost option if the team wants to use Cloudflare nameservers. [ICANN RDAP guidance](https://www.icann.org/en/contracted-parties/registry-operators/resources/registration-data-access-protocol) · [Porkbun .com pricing](https://porkbun.com/products/domains/com) · [Cloudflare nameserver requirement](https://developers.cloudflare.com/registrar/get-started/register-domain/)

| Working name | First choice | Backup | Registration decision |
|---|---|---|---|
| Skarion Fiber | `skarionfiber.com` | `skarionfiberdesign.com` | Pick one for the OSP design page. |
| Skarion Estimating | `skarionestimating.com` | `skariontakeoffs.com` | Pick one for the estimating page. The broader name leaves room for approved priced-bid services. |
| Skarion Drafting | `skariondrafting.com` | `skarioncad.com` | Pick one for the CAD and record drawing page. |
| **SkarionGIS** | `skariongis.com` | `skariongisdata.com` | Prioritize the exact spelling the owner selected. |
| Skarion Lighting | `skarionlighting.com` | `skarionphotometrics.com` | Reserve for the pilot, then point to the approved lighting page. |
| Skarion Stormwater | `skarionstormwater.com` | `skariondrainage.com` | Reserve for the pilot, then point to the approved stormwater page. |

Use the company registrar account, enable MFA and auto-renew, and record the registrant, billing owner, renewal price and final redirect in the workbook. Have the owner sign off on the displayed names and check for confusingly similar brands before committing. Purchase one name per arena after the price and ownership check. Test HTTPS and the root and `www` redirect after the corresponding parent page is ready. [ICANN lookup](https://lookup.icann.org/en) · [USPTO trademark search](https://www.uspto.gov/trademarks/search)

## Parent website structure

1. **Home.** Put OSP fiber design, bid takeoffs, CAD production and GIS closeout in the first service grid. An opening line to review is “Production support for fiber, utility and civil teams.” Use primary action “Scope a project” and secondary action “View work samples.” Label lighting and stormwater as pilots if the team approves showing them publicly.
2. **Services.** Give each lane its own page. Start with the buyer and the result, show accepted inputs and file types, list the handoff and technical review, then show a clearly labeled example package and a lane-specific action. Use the common components so projects and standards are updated in one place.
3. **Work examples.** Use a project list with service filters and an individual project template. Keep third-party references and synthetic pack drafts in the *internal* project queue. Publish an actual Skarion project after the project owner confirms Skarion’s role, outputs, permission and any redactions. If approved for public use, label synthetic examples as **sample deliverables using synthetic inputs**.
4. **Process and quality.** Show intake, first-pass production, peer checking, client approval and revision control. Identify when the responsible professional, contract owner or local field team reviews a deliverable. Confirm the permitted data location before receiving customer files or committing to any restricted work.
5. **Project intake.** Use one form with lane, buyer type, project state, scope, deadline and time zone, expected format and reviewing party. Ask only for a project summary at intake. Arrange an approved transfer channel for source files after review. Route estimating submissions to the estimating lead and public contracts with restricted delivery to the appropriate reviewer.

Before settling on the proposed routes, map the current OSP, GIS, permitting and redline pages in the site's repository. Reuse a working URL where its purpose is unchanged. If the team moves a page, map its old address to the approved destination and test existing service cards, quote links and analytics events. [Current navigation and service links](https://skarionengineering.com/) · [Redirect guidance](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

### Service page template for the team

| Page block | What to write or prepare | Review before moving forward |
|---|---|---|
| Headline and overview | Buyer, work package and finished handoff in one screen | Sales lead confirms buyers use these terms and the team can deliver the advertised package. |
| Scope and inputs | 3-5 deliverables, input checklist, file formats, role boundaries | Technical reviewer verifies quantities, assumptions, reviewer role and software claims. |
| Example project | Problem, approved inputs, Skarion’s role, outputs, visual proof, QA and known limits | Assign owner, verify authorship and permission, and label mock or synthetic material correctly. |
| Fit and exclusions | Typical buyer, location, deadline and what requires a licensed/local specialist | Delivery lead confirms jurisdiction, data access and subcontract limits for the actual opportunity. |
| CTA and workflow | Lane-specific action, named internal intake owner and response flow | Test form routing, acknowledgment, attribution fields and private project intake. |

## Internal website project queue

Each item below is a **proposed Skarion sample**, awaiting team review. Build new artifacts from synthetic, public-domain or explicitly approved inputs. The lane briefs and workbook link to real projects by other firms as references for the format and depth of evidence.

| Arena | Draft project page | Team artifact to build | Technical review |
|---|---|---|---|
| OSP fiber | **Fiber corridor design package** | One-mile synthetic corridor, route map, three sample plan sheets, splice detail, quantities and a redline log | OSP lead verifies field assumptions, constructability flags and review responsibilities. |
| Estimating | **Wet and dry utility bid takeoff** | Annotated plan extract, editable BOQ, sheet and item references, addendum delta and exclusions register | Estimator spot-checks lengths, units, work classifications and assumptions. Publish priced examples only after local assumptions are reviewed. |
| Drafting | **Field redlines to an as-built set** | Five synthetic markup sheets, native CAD and PDF before-and-after excerpts, layer and revision checklist | CAD lead checks title blocks, sheet cross-references, markup traceability and editable output. |
| SkarionGIS | **Fiber route closeout data pack** | Sample GIS schema, 30 synthetic features, source-to-feature crosswalk, splice and test references, exception log | GIS lead checks IDs, topology, projection, metadata and reconciliation of the submitted files. |
| Lighting | **Small parking area photometric pilot** | Approved or synthetic base plan, IES fixture inputs, calculation grid, schedule and two layout options | Lighting reviewer checks calculation settings, units, mounting assumptions and what the package demonstrates. |
| Stormwater | **Subdivision drainage inventory pilot** | Synthetic inventory of 40 inlets, structures and pipes, photo links, map layers and condition-data exceptions | Stormwater/GIS reviewer checks connectivity and classification, reserves modeling and professional approval for the assigned project lead. |

Track each draft through **Draft → Technical review → Rights and claims review → Approved for publish**. Keep a reviewer name and decision in the workbook. A reference project can move to “Study” for the team. Only Skarion-owned, approved work or clearly labeled samples can move into a public Skarion project card.

## What to learn from peer websites

- **OSP design.** HR Green's Duluth Phase II case connects field verification, GIS route design and construction-ready documentation to a named buyer. A Skarion case should likewise say who supplied the inputs, what Skarion produced and who approved the output. [HR Green's ImOn case](https://www.hrgreen.com/news/imon-advances-fiber-expansion-across-northeastern-minnesota/)
- **Estimating.** StatLab shows the buyer an editable workbook alongside marked plans. OCMI's Port of Long Beach case explains the stage of estimate and what it reviewed line by line. Bring both ideas into the synthetic Skarion sample with sheet references, addendum deltas and clearly marked assumptions. [StatLab's utility offer](https://statlabllc.com/trades/utilities/) · [OCMI's Port of Long Beach case](https://www.ocmi.com/portfolio/civic/port-of-long-beach/)
- **CAD and as-builts.** Scan2Plan's Gray Space example identifies a 55-page drawing conversion and invites the reader to inspect the source-to-output change. For Skarion, pair a review-cleared before-and-after sheet with a short QA and revision summary. [Scan2Plan's special projects](https://www.scan2plan.io/projects/special-projects)
- **SkarionGIS.** GDRS describes the actual fiber turnover files it produces, then explains where the prime's review starts. Woolpert's ReWa project shows a different GIS route, converting legacy CAD and hard-copy as-builts into an asset network. Create two portfolio cards with distinct deliverables for fiber closeout and utility records QA. [GDRS fiber closeout scope](https://gdrsgeo.com/telecom-broadband.html) · [Woolpert's ReWa case](https://woolpert.com/case-studies/rewa-utility-network-modernization/)
- **Lighting.** Summit credits its photometric site plan as one output within a wider electrical project. Wi-Skies explains how roadway elevations changed its lighting calculations. Show the pilot buyer two options on a common calculation grid, with the fixture assumptions and technical review clearly visible. [Summit's The Luxe case](https://summitmep.com/portfolio-item/the-luxe/) · [Wi-Skies project examples](https://wi-skies.com/projects/)
- **Stormwater.** SAM's Topeka case tells the reader how a facility ID kept the handoff usable in Cityworks. McAdams' Apex case shows how a limited pilot informed a wider condition assessment. Start Skarion's pilot with a buyer's schema, source references, asset IDs and an exception log that a prime can review on a single basin. [SAM's Topeka case](https://www.sam.biz/projects/topeka-storm-sewer-inspection-and-mapping/) · [McAdams' Apex case](https://mcadamsco.com/projects/stormwater-system-condition-assessment)

## Social media structure

Start with the parent LinkedIn company page and six recurring topics. Each topic points to its matching service page when that page has been approved. A shared publishing calendar prevents the same company being approached with several overlapping offers. Use short screen recordings and swipeable PDFs for diagrams, checklists and before-and-after production. Teams can build pilot posts internally while the evidence packages are under review.

| Topic | Recurring content | First example | Call to action |
|---|---|---|---|
| OSP fiber | Plan sheet walkthroughs, splice details, HLD-to-LLD review | What a prime should send before a one-route design pilot | Request a route pilot |
| Estimating | Bid addendum deltas, takeoff traceability, exclusions | Three things to check when a bore length changes after Addendum 2 | Scope a takeoff |
| Drafting | Redline-to-CAD before and after, CAD QA, file formats | A redline that changes both the plan and profile | Request a drawing batch |
| SkarionGIS | Data schema, topology, field-to-office closeout | How one missing asset ID can stall a closeout handoff | Ask for a sample data package |
| Lighting | Fixture schedules, calculation assumptions, model reviews | How mounting height changes the calculation grid | Join the pilot review |
| Stormwater | Inventory QA, photo linking, structures and culverts | How to distinguish an unmapped pipe from an unknown connection | Scope an inventory pilot |

Plan three posts per week on the parent channel. Give each active lane two initial posts. Stage two lighting and two stormwater posts for approval, using project artifacts the technical reviewers have checked. Track qualified inquiries, requested pilot scopes and proposals by lane using consistent URL campaign attribution. Review which examples prompt buyer conversations before adding a separate account for any service.

## 30-day team handoff

| Window | Work | Owner role | Ready when |
|---|---|---|---|
| Days 1-5 | Review benchmarks, confirm names and registrar prices, assign draft pages and sample owners | Portfolio lead and operations | Six domain choices and six page owners recorded. Estimating lead and pilot reviewers assigned. |
| Days 6-12 | Draft the active-lane pages and production packs. Build the shared intake and review checklist. | Web lead and production leads | Four page drafts and sample outlines ready for technical review. |
| Days 13-21 | Build first sample files and social drafts. Test the shared form and staging links. | Technical leads and content lead | Scope, file format, data location and role checked for each active lane. |
| Days 22-30 | Review lighting and stormwater pilot scope, compare buyer responses, approve public proof and routing | Portfolio lead and reviewers | A documented launch or further-validation decision for each pilot and a short list of improvements based on buyer responses. |

## Detailed lane plans

| Plan | Companies | Project references | Public social links |
|---|---:|---:|---:|
| [OSP fiber design](01_OSP_Fiber_Design_Website_Plan.md) | 52 | 19 | 14 |
| [OSP and utility bid estimating](02_Utility_Bid_Estimating_Website_Plan.md) | 55 | 11 | 13 |
| [CAD drafting and as-builts](03_CAD_Drafting_and_As_Builts_Website_Plan.md) | 54 | 18 | 12 |
| [SkarionGIS and closeout data](04_GIS_and_Closeout_Data_Website_Plan.md) | 61 | 18 | 11 |
| [Lighting and photometrics](05_Lighting_and_Photometrics_Website_Plan.md) | 60 | 21 | 14 |
| [Stormwater support](06_Stormwater_Support_Website_Plan.md) | 54 | 33 | 13 |
| **Total comparison entries** | **336** | **120** | **77** |

Companies are distinct within each arena. A firm can recur across arenas when its service evidence supports the comparison. The social links support qualitative review of what firms post and how they present it. The public examples establish the scope attributed to each firm.

Use the [benchmark and review workbook](Skarion_Six_Arenas_Benchmark_and_Review.xlsx) to filter the company research by arena, open the source evidence, and record the team’s decisions on examples, domains and initial social content.
