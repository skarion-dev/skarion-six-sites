# Skarion Engineering service websites

Seven standalone static websites with a common intake workflow and an internal review hub. Each site includes capabilities, an example project library, downloadable sample deliverables and a brand kit. Drafting has seven examples and Surveying has four. The websites are drafts for Skarion's team to review.

## Preview

Use Node.js 22 or later. No package installation or credentials are needed.

```sh
npm run preview
```

Open [the local review hub](http://127.0.0.1:4173/). On a Windows shell that blocks npm's PowerShell shim, use `npm.cmd run preview`. Stop the server with `Ctrl+C`. To pass a different port, set `SKARION_PREVIEW_PORT` before starting the server.

The [combined project library](http://127.0.0.1:4173/catalog/) and the service cards give direct access to every case and capability page. Each project describes the scope, production steps, deliverables and checks. Its sample files use synthetic data.

| Site | Preview path | Proposed domain | Phase | Brand and project reviews |
| --- | --- | --- | --- | --- |
| Skarion Fiber | `/fiber/` | `skarionfiber.com` | Active offer | [Brand](sites/fiber/brand.md) · [Projects](sites/fiber/portfolio-review.md) |
| Skarion Estimating | `/estimating/` | `skarionestimating.com` | Active offer | [Brand](sites/estimating/brand.md) · [Projects](sites/estimating/portfolio-review.md) |
| Skarion Drafting | `/drafting/` | `skariondrafting.com` | Active offer | [Brand](sites/drafting/brand.md) · [Projects](sites/drafting/portfolio-review.md) |
| SkarionGIS | `/gis/` | `skariongis.com` | Active offer | [Brand](sites/gis/brand.md) · [Projects](sites/gis/portfolio-review.md) |
| Skarion Lighting | `/lighting/` | `skarionlighting.com` | Pilot | [Brand](sites/lighting/brand.md) · [Projects](sites/lighting/portfolio-review.md) |
| Skarion Stormwater | `/stormwater/` | `skarionstormwater.com` | Pilot | [Brand](sites/stormwater/brand.md) · [Projects](sites/stormwater/portfolio-review.md) |
| Skarion Surveying | `/surveying/` | Pending | Desktop support pilot | [Brand](sites/surveying/brand.md) · [Projects](sites/surveying/portfolio-review.md) |

## Build and review

```sh
npm run check
```

`dist/index.html` is the review hub. The cross-service library is `dist/catalog/`. Each `dist/<site>/` is self-contained and can be served at a domain root or a path. The build includes synthetic examples and excludes Markdown and portfolio research. All output uses draft indexing controls.

`sites.json` lists the offers. Edit `sites/<site>/index.html`, `site.css`, `logo.svg` and `assets/` for the home page and identity. `sites/<site>/content.json` controls the capability sections, project pages and sample downloads. Keep approved-for-preview files under `assets/samples/`, and illustrations under `assets/projects/`. `shared/` contains accessibility defaults, detail page styles and intake behavior. `preview/` contains the hub.

The intake form builds a draft addressed to `info@skarion.com` in the visitor's email application. A project-page inquiry carries the example title into that draft. Buyers should send a summary first and arrange a transfer channel for project files with Skarion.

## Team handoff

- [Brand, domain and social launch plan](review/launch-kit.md)
- [Technical and publication review sheet](review/site-review.md)
- [Founder’s Research and archive provenance](research/README.md) · [Open in the local preview](http://127.0.0.1:4173/founders-research/)
