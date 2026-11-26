# Skarion Engineering service websites

Six standalone static websites with a common intake workflow and an internal review hub. Each site has its own logo, visual identity, service copy, social directions and a project review brief. The websites are drafts for Skarion's team to review.

## Preview

Use Node.js 22 or later. No package installation or credentials are needed.

```sh
npm run preview
```

Open [the local review hub](http://127.0.0.1:4173/). On a Windows shell that blocks npm's PowerShell shim, use `npm.cmd run preview`. Stop the server with `Ctrl+C`. To pass a different port, set `SKARION_PREVIEW_PORT` before starting the server.

| Site | Preview path | Proposed domain | Phase | Brand and project reviews |
| --- | --- | --- | --- | --- |
| Skarion Fiber | `/fiber/` | `skarionfiber.com` | Active offer | [Brand](sites/fiber/brand.md) · [Projects](sites/fiber/portfolio-review.md) |
| Skarion Estimating | `/estimating/` | `skarionestimating.com` | Active offer | [Brand](sites/estimating/brand.md) · [Projects](sites/estimating/portfolio-review.md) |
| Skarion Drafting | `/drafting/` | `skariondrafting.com` | Active offer | [Brand](sites/drafting/brand.md) · [Projects](sites/drafting/portfolio-review.md) |
| SkarionGIS | `/gis/` | `skariongis.com` | Active offer | [Brand](sites/gis/brand.md) · [Projects](sites/gis/portfolio-review.md) |
| Skarion Lighting | `/lighting/` | `skarionlighting.com` | Pilot | [Brand](sites/lighting/brand.md) · [Projects](sites/lighting/portfolio-review.md) |
| Skarion Stormwater | `/stormwater/` | `skarionstormwater.com` | Pilot | [Brand](sites/stormwater/brand.md) · [Projects](sites/stormwater/portfolio-review.md) |

## Build and review

```sh
npm run check
```

`dist/index.html` is the review hub. Each `dist/<site>/` is self-contained and can be served at a domain root or a path. The build excludes Markdown and review materials. All output uses draft indexing controls. Internal project references remain with the site sources.

`sites.json` lists the six offers. Edit `sites/<site>/index.html`, `site.css`, `logo.svg` and `assets/` for each site's copy, identity and portable assets. `shared/` contains the accessibility defaults and intake behavior. `preview/` contains the hub.

The intake form builds a draft in the visitor's email application addressed to `info@skarion.com`. The visitor sends it themselves. The site has no backend, analytics, tracking, form storage or file upload. Buyers should send a summary first and arrange a transfer channel for project files with Skarion.

## Team handoff

- [Brand, domain and social launch plan](review/launch-kit.md)
- [Technical and publication review sheet](review/site-review.md)
