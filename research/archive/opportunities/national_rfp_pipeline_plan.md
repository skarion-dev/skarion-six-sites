# National county RFP pipeline for Skarion Engineering

## MVP built in this workspace (1 November 2026)

- `opportunities/data/county_source_registry.csv` contains 3,236 Census county/equivalent rows: 3,144 in the 50 states and DC, plus 92 in territories and island areas.
- `scripts/build_county_registry.py` regenerates that registry from the Census public text file.
- `scripts/collect_public_rfps.py` is the first collector. It accepts verified official source rows configured as RSS, Atom, or public HTML and saves discovered notices and run status to SQLite.
- Procurement URLs are blank and coverage is not yet national. No source was added based on a paid RFP site. The registry exposes this as `source_needed` until an official source is mapped and checked.

## What this system can and cannot promise

The goal should be **measured, expanding coverage of county and county-equivalent procurement sources**, not a claim that one feed contains every county RFP. The Census Bureau's county reference file can seed the jurisdiction directory, but procurement authority and portals vary: some counties do not run their own procurements, some post to state or regional systems, and others use different vendor platforms.

SAM.gov is a helpful public API for **federal** notices, including federal work performed in a county. It is not a national county-government RFP feed. The API requires a SAM.gov public API key, supports paginated searches, and exposes current active notice versions.

## Recommended pipeline

```text
Census county / equivalent directory
               |
               v
Official source registry <--- state, county, and regional portal discovery
               |
               v
Collectors: APIs/RSS -> platform feeds -> permitted public HTML -> discovery queue
               |
               v
Normalize + deduplicate + archive source page / attachment metadata
               |
               v
Rules filter -> GPT-6 Luna relevance/risk analysis with citations
               |
               v
SQLite opportunity ledger -> daily OpenClaw digest in chat
               |
               v
Human review (eligibility, pricing, contact, bid decision)
```

## Data to track

### Jurisdictions

Seed a table with state, county or equivalent name, Census GEOID, official county site, procurement-source URL, source owner (county/state/regional/cooperative), known portal vendor, coverage status, last checked date, and discovery notes. Keep records for county equivalents and territories as distinct coverage groups. The Census county adjacency download is a source for the geography list; verify the current 2026 file/schema when building the importer.

### Procurement source registry

Each source entry should include:

- Canonical official source URL and agency owner.
- Collector type: documented API, RSS/Atom, public portal HTML, email alert, or manual/discovery-only.
- Terms/robots check, access restrictions, pagination strategy, and permitted request rate.
- Last successful fetch, last notice date, error state, and next retry.
- Provenance level: primary buyer source, source-derived feed, or discovery lead.

Never use an aggregator's summary as final proof when the buyer's notice or addendum can be checked. Do not bypass logins, paywalls, CAPTCHAs, or access controls. Portal-specific APIs should only be used where documented or authorized.

## Collection strategy

1. **Federal base feed:** SAM.gov Opportunities API. Query multiple relevant NAICS / keywords and locations; paginate, retain notice ID and modification date, and fetch updates for previously known notices. Store the API key in a local environment variable or Windows Credential Manager, never in this repository or a prompt.
2. **State and territory portals:** register the official procurement portal for each state/territory and record whether it includes county buyers. Many contain local government postings but scope differs by state.
3. **County / regional portals:** discover official county purchasing pages and common portal hosts. Map aliases/redirects, because a county may be hosted on a shared portal while the buyer remains the source owner.
4. **Discovery-only search:** scheduled web queries and public notices can find missing portals and ads. These results go into a human-reviewed source-discovery queue until validated against an official procurement page.
5. **Change monitoring:** re-fetch active notices and amendments; compare deadlines, attachments, addenda, cancellation status, and source-modified date. Keep a history rather than overwriting previous versions.

## Skarion filters

Use deterministic filters first, then Luna for semantic screening. High-value terms include outside plant, fiber-optic design, broadband engineering, telecom, GIS, ArcGIS, mapping, Civil 3D, utility mapping, construction inspection, and engineering services. Treat words as candidates, not automatic qualification.

Every scored notice should retain:

- Buyer, source URL, notice ID, county/state, posted and due dates with timezone.
- Scope and deliverables, contract type/value if explicitly stated, and amendments.
- Eligibility gates: PE/license, geographic authorization, set-aside, registrations, references, insurance/bonding, mandatory site visit, work-location rules, and submission method.
- Fit score separated from bid readiness. A strong technical fit can still be a no-bid due to a hard gate.
- Short rationale, unknowns, source citations, source-check timestamp, and confidence.

Default automation should **only collect, update, rank, and draft a digest**. Do not let it create procurement accounts, contact buyers, submit bids, commit prices, or represent Skarion.

## OpenClaw scheduling

OpenClaw's Gateway scheduler supports recurring cron jobs. Example daily research digest (adjust agent name after checking the local agent registry). Run from the project root after sources are populated:

```powershell
.\scripts\openclaw.ps1 automations create "0 7 * * 1-5" `
  "Run the Skarion RFP collector, review only new or materially changed notices, verify each against the buyer source, and post a concise digest with links, deadlines and unknown eligibility gates. Do not contact anyone or submit anything." `
  --name "Skarion RFP morning digest" `
  --agent research-synthesist `
  --tz America/New_York
```

This schedule should be created **after** the collector and source registry exist; otherwise it only asks an agent to search the web and cannot guarantee county coverage. The local OpenClaw Gateway must be online when the scheduled job fires. For continuous collection when the PC is off, run the collector and Gateway on an always-on server and protect API keys there.

## Rollout plan

### Phase 1 — reliable pilot

- Import the national county/equivalent jurisdiction list.
- Inventory all 50 state procurement systems and tag which ones expose county/local solicitations.
- Add sources for the counties in Skarion's current service footprint and any counties where relevant OSP/GIS notices have already been found.
- Implement the SAM.gov connector and a generic source-registry format.
- Run collection on demand and review false positives, duplicate handling, and missed notices before scheduling.

### Phase 2 — expand sources

- Add official county portals in batches, prioritizing counties with fiber, broadband, utility, GIS, and engineering activity.
- Add platform adapters only after confirming allowed access and stable public endpoints.
- Publish a coverage dashboard showing known counties, official source found, collector active, last successful check, and known limitations. Unknown coverage must stay visible.

### Phase 3 — daily operations

- Schedule deterministic collection before the agent digest.
- Keep a change log for amendments and deadline changes.
- Alert only on new, changed, closing-soon, or collector-failure events.
- Review coverage gaps monthly and rotate on failures/rate limits.

## First secrets and decisions needed for implementation

- Obtain a SAM.gov public API key and store it locally; never paste the key into chat or commit it.
- Decide whether the first rollout covers all 50 states only or also territories and tribal procurement systems.
- Provide Skarion's actual service footprint / target states, since that determines the first county batch.
- Confirm the delivery surface: OpenClaw chat digest is the default; email notifications would need a separately configured and approved integration.

## Official references

- [SAM.gov Get Opportunities Public API](https://open.gsa.gov/api/get-opportunities-public-api/) — API key, date parameters, pagination, daily updates, and active-notice version behavior.
- [Census Bureau County Adjacency File](https://www.census.gov/geographies/reference-files/time-series/geo/county-adjacency.2024.html) — geographic list includes counties and equivalents in the states, DC, Puerto Rico, and Island Areas; use the latest available file for production.
- [OpenClaw automation CLI](https://docs.openclaw.ai/cli/cron) — create/list/run/manage Gateway scheduled jobs.
- [OpenClaw automation schedules](https://docs.openclaw.ai/automation/cron-jobs/schedules) — cron timezone and schedule behavior.
