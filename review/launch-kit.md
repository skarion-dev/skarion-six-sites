# Skarion Engineering launch kit

Use Skarion Engineering as the parent company and the lane marks as offer identities. Keep each name in its written form. The contact team, proposal footer and delivery terms should identify the responsible business consistently across sites. Use SkarionGIS without a space.

## Brand system

| Asset | Location | Use |
| --- | --- | --- |
| Primary icon and favicon | `sites/<site>/logo.svg` | Website header, favicon and approved avatar exports |
| Color, type and application | `sites/<site>/brand.md` | Page layouts, proposals, diagrams and social production |
| Upload-ready graphics | `sites/<site>/brand-assets/avatar.png` and `social-card.png` | Square profile image and launch post |
| Editable social artwork | SVG source linked in each `brand.md` | Resizing, localization and future posts |
| References, sample project and approval checklist | `sites/<site>/portfolio-review.md` | Internal design and production review |

Keep artwork readable at avatar size. Preserve logo proportions, and give the mark breathing room equal to at least a quarter of its width. Use the site's high-contrast background and one lead accent in each social graphic. Export square 1080 × 1080 posts, portrait 1080 × 1350 carousels and 1200 × 630 link previews. Ask the delivery lead to clear any recognizable client site, screenshot, field record or yield claim before external use.

## First posts for the parent LinkedIn page

| Lane | Post one | Post two | Ask |
| --- | --- | --- | --- |
| Fiber | An approved route input checklist | A splice reference and how it appears on the plan and schedule | Scope one route |
| Estimating | A worksheet line that links back to a drawing | An addendum changing a bore or duct quantity | Scope one takeoff |
| Drafting | A review-cleared redline and editable CAD panel | The layer and revision checks on an as-built batch | Scope one batch |
| SkarionGIS | An asset ID matched across two records | An exception log for unlinked test or splice files | Scope one closeout package |
| Lighting | A fixture schedule and calculation grid from the same pilot | Two layouts compared against the same assumptions | Discuss the pilot |
| Stormwater | A single basin inventory handoff | An unknown pipe connection kept visible in the GIS exception log | Discuss the pilot |

Use one subject and one visual per post. Start with the four active offers. Keep lighting and stormwater drafts internal until the technical pilot reviewer confirms the scope and approves the sample. Align links to the chosen public destination at launch. Track qualified inquiries, scope calls and paid pilot conversions by lane in the shared CRM. Add a decision for campaign attribution to the publication checklist before enabling any analytics.

## Domains and hosting

| Domain candidate | Backup | Private build directory |
| --- | --- | --- |
| `skarionfiber.com` | `skarionfiberdesign.com` | `dist/fiber/` |
| `skarionestimating.com` | `skariontakeoffs.com` | `dist/estimating/` |
| `skariondrafting.com` | `skarioncad.com` | `dist/drafting/` |
| `skariongis.com` | `skariongisdata.com` | `dist/gis/` |
| `skarionlighting.com` | `skarionphotometrics.com` | `dist/lighting/` |
| `skarionstormwater.com` | `skariondrainage.com` | `dist/stormwater/` |
| Pending Survey CAD jurisdiction and name review | Pending | `dist/surveying/` |

Before registration, check each candidate at the company registrar for availability, first-year and renewal prices, and disputed or similar names. Record the account owner, payment owner, renewal setting and routing decision. Enable account MFA. Keep domain acquisition and production DNS under the company account.

The builds work as individual domain microsites or under service paths on the parent site. Choose one canonical public address per lane. If a short domain forwards to a parent-site service page, send root and `www` requests to that address, over HTTPS. Avoid changing existing OSP and GIS URLs until the web lead has mapped backlinks, search pages, navigation and forms. [Parent website](https://skarionengineering.com/) · [Google redirect guidance](https://developers.google.com/search/docs/crawling-indexing/301-redirects)

For a hosted team review, use an access-controlled preview and deploy the hub and site builds there. For public release, select only an approved `dist/<site>/` directory as the deployment root, change the draft indexing controls in the release build, and configure final canonical, social metadata, HTTPS and redirects. The preview hub and source review docs stay private. Maintain an assigned owner for production access, content changes and uptime.

## Intake triage

1. Assign an inbox owner and lane routing. Confirm who covers the shared inbox and who can scope each offer.
2. Capture buyer type, project state, work product, target deadline and time zone, required format and reviewing party. Confirm deliverable assumptions and acceptance before quoting.
3. Provide an approved file-transfer route after the scope call. Confirm data location and subcontracting permissions for the specific engagement when applicable.
4. Maintain one CRM record per opportunity. Associate cross-sell services with the record so several lanes do not send overlapping follow-ups to the same prospect.
