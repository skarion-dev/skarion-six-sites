import { createHash } from 'node:crypto';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { escapeHtml as h } from './pages.mjs';

const shared = 'output/';
const market = `${shared}skarion_niche_market_research_2026-11-24/`;
const procurement = `${shared}skarion_opportunity_search_2026-11-25/`;
const subcontract = `${shared}skarion_subcontract_due_diligence_2026-11-25/`;
const benchmark = `${shared}skarion_six_arenas_2026-11-26/`;
const prime = `${shared}skarion_live_prime_subcontract_search_2026-11-25/`;
const bundle = 'original-bundle/Skarion_Engineering_Research_Archive/';
const repository = `https://github.com/skarion-dev/skarion-six-sites/blob/${encodedPath(process.env.SKARION_RESEARCH_REF ?? 'main')}/`;
const sourceOfferFolders = { drafting: '02_Drafting', lighting: '03_Lighting', gis: '04_GIS_and_Utility_Assets', stormwater: '05_Stormwater' };
const primeSearches = new Map([[8, '01'], [10, '02'], [17, '03'], [16, '04'], [19, '05']]);
const originalNiches = { 1: 'drafting', 2: 'lighting', 3: 'gis', 4: 'stormwater', 15: 'drafting', 23: 'stormwater' };

function encodedPath(value) {
  return value.split('/').map(encodeURIComponent).join('/');
}

function repositoryFile(file, anchor = '') {
  return `${repository}${encodedPath(file)}${anchor ? '#' + encodeURIComponent(anchor) : ''}`;
}

function label(file) {
  return path.posix.basename(file, path.posix.extname(file)).replace(/^\d{2}_/, '').replaceAll('_', ' ');
}

function fileRows(files) {
  return `<ul class="research-files" data-filter-list>${files.map(({ path: file, bytes, title }) => `
    <li data-filter-item>
      <div><a href="${repositoryFile(`research/archive/${file}`)}">${h(title ?? label(file))}</a>
        <span class="file-path">${h(file)}</span></div>
      <a class="file-download" href="/_research_archive/${encodedPath(file)}" download>Download <span>${h(path.extname(file).slice(1).toUpperCase())} · ${Math.max(1, Math.round(bytes / 1024))} KB</span></a>
    </li>`).join('')}</ul>`;
}

function block(title, body, id) {
  return `<section class="research-block"${id ? ` id="${id}"` : ''}><h2>${h(title)}</h2>${body}</section>`;
}

function layout(base, title, description, body, { filter, site } = {}) {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="${h(description)}">
  <meta name="robots" content="noindex,nofollow">
  <link rel="stylesheet" href="${base}../preview.css">
  <link rel="stylesheet" href="${base}research.css">
  ${filter ? `<script src="${base}filter.js" defer></script>` : ''}
  <title>${h(title)} | Skarion Engineering</title>
</head>
<body class="research">
  <a class="research-skip" href="#main">Skip to content</a>
  <header class="top wrap">
    <a class="name" href="${base}../"><span class="mark" aria-hidden="true"></span> Skarion Engineering</a>
    <a href="${base}archive/">Source archive</a>
  </header>
  <main id="main" class="wrap" tabindex="-1">
    <nav class="research-crumb" aria-label="Breadcrumb">
      <a href="${base}../">Team preview</a>${base === './' ? '' : ` <span aria-hidden="true">/</span> <a href="${base}">Founder’s Research</a>`}
    </nav>
    <div class="research-intro">
      ${site ? `<span class="research-tag">${h(site)}</span>` : '<span class="research-tag">Private research draft</span>'}
      <h1>${h(title)}</h1>
      <p>${h(description)}</p>
    </div>
    ${body}
  </main>
  <footer class="wrap footer">Skarion Engineering · Internal review</footer>
</body>
</html>
`;
}

function filterBox(label) {
  return `<form class="research-filter" role="search" hidden><label for="research-query">${h(label)}</label>
    <input type="search" id="research-query" autocomplete="off">
    <span role="status" data-result-count></span></form>`;
}

function nicheLink(base, niche) {
  return `<li data-filter-item><a href="${base}niches/${niche.id}/">${h(niche.title)}</a></li>`;
}

function roundupNotes(section) {
  return section
    .split(/\r?\n\r?\n/)
    .slice(1, 4)
    .map((paragraph) => {
      const text = paragraph.replace(/\s*\[[^\]]+\]\([^)]+\)/g, '').replaceAll('**', '').trim();
      return `<p>${h(text)}</p>`;
    }).join('');
}

function selectFiles(files, startsWith) {
  return files.filter(({ path: file }) => startsWith.some((prefix) => file.startsWith(prefix)));
}

function numberedFile(files, directory, number) {
  const matches = selectFiles(files, [`${directory}${number}_`]);
  if (matches.length !== 1) throw new Error(`Expected one archive record in ${directory} for niche ${number}`);
  return matches[0];
}

async function writePage(directory, html) {
  await mkdir(directory, { recursive: true });
  await writeFile(path.join(directory, 'index.html'), html);
}

export async function buildFoundersResearch(root, dist, sites) {
  const sources = path.join(root, 'research');
  const archive = path.join(sources, 'archive');
  const files = JSON.parse(await readFile(path.join(sources, 'manifest.json'), 'utf8'));
  const offers = JSON.parse(await readFile(path.join(sources, 'catalog.json'), 'utf8'));
  const destination = path.join(dist, 'founders-research');
  for (const file of files) {
    const parts = file.path.split('/');
    if (parts.some((part) => !part || part.startsWith('.') || /[\\:]/.test(part))) {
      throw new Error(`Invalid archive path: ${file.path}`);
    }
    const content = await readFile(path.join(archive, ...parts));
    if (content.length !== file.bytes || createHash('sha256').update(content).digest('hex') !== file.sha256) {
      throw new Error(`Archive contents changed: ${file.path}`);
    }
  }

  const niches = [];
  const roundup = `${market}Skarion_RFP_and_Prime_Teaming_Report_2026-11-25.md`;
  const roundupText = await readFile(path.join(archive, roundup), 'utf8');
  const roundupSections = new Map(roundupText.split(/^### (?=\d\d )/m).slice(1).map((section) => [section.slice(0, 2), section]));
  for (let index = 1; index <= 25; index++) {
    const number = String(index).padStart(2, '0');
    const section = roundupSections.get(number);
    if (!section) throw new Error(`Missing RFP roundup heading for niche ${number}`);
    const title = section.split(/\r?\n/, 1)[0].slice(3).trim();
    const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/-$/, '');
    niches.push({
      number: index, title, id: slug, notes: roundupNotes(section),
      records: [
        { ...numberedFile(files, `${market}research/`, number), title: 'Market evidence and competition' },
        { ...numberedFile(files, `${procurement}opportunities/`, number), title: 'RFP and opportunity ledger' },
        { ...numberedFile(files, subcontract, number), title: 'Prime and subcontract due diligence' },
        ...selectFiles(files, primeSearches.has(index) ? [`${prime}${primeSearches.get(index)}_`] : []),
      ],
      offers: sites.filter(({ id }) => offers[id].niches.includes(index)),
      roundupAnchor: `${number}-${title.toLowerCase().replace(/[^a-z0-9 -]/g, '').replace(/ /g, '-')}`,
    });
  }
  if (niches.some(({ offers }) => !offers.length)) throw new Error('A research niche is missing its offer mapping');

  const overview = layout('./', 'Founder’s Research', 'Find the market evidence, RFP records, competitor research and source files behind each Skarion offer.', `
    <div class="research-overview">
      <a href="#offers"><strong>${sites.length}</strong> Skarion offers</a>
      <a href="#niches"><strong>${niches.length}</strong> researched niches</a>
      <a href="archive/"><strong>${files.length}</strong> archived files</a>
    </div>
    ${block('Research by offer', `<div class="research-offers">${sites.map((site) => `
      <article class="site-card" style="--lane: ${site.color}">
        <h3><a href="offers/${site.id}/">${h(site.name)}</a></h3>
        <p>${h(site.scope)}</p>
      </article>`).join('')}</div>`, 'offers')}
    ${block('RFPs and pursuit history', `
      <p>Deadlines and statuses reflect the original research dates. Closed, superseded and award-watch records stay in the archive.</p>
      ${fileRows(selectFiles(files, [roundup,
        `${shared}pdf/Skarion_Engineering_All_Opportunities`,
        `${procurement}opportunities/Skarion_25_Niche_Opportunity_Index`,
        `${subcontract}Skarion_25_Niche_Subcontract_Pursuit_Index`,
        `${bundle}06_RFPs_and_Teaming/`,
      ]))}`)}
    ${block('All 25 niches', `${filterBox('Find a niche by name')}<ul class="research-niches" data-filter-list>${niches.map((niche) => nicheLink('./', niche)).join('')}</ul>`, 'niches')}
    `, { filter: true });
  await writePage(destination, overview);

  for (const niche of niches) {
    const original = sourceOfferFolders[originalNiches[niche.number]];
    const supporting = original ? selectFiles(files, [`${bundle}${original}/`])
      .filter(({ path: file }) => !file.includes('/Restricted_Reference/')) : [];
    const sectorAttachments = niche.number === 4 || niche.number === 23
      ? selectFiles(files, ['official-supplements/'])
      : [];
    if (niche.number === 13) supporting.push(...selectFiles(files, offers.surveying.archivePrefixes));
    await writePage(path.join(destination, 'niches', niche.id), layout('../../', niche.title,
      'Market evidence, buyer and prime opportunities, and the subcontract follow-up recorded for this niche.', `
      ${block('Market, RFP and subcontract files', fileRows(niche.records))}
      ${block('November 25 research notes', `${niche.notes}
        <p><a href="${repositoryFile(`research/archive/${roundup}`, niche.roundupAnchor)}">Open the original RFP roundup and its source links</a></p>`)}
      ${supporting.length || sectorAttachments.length ? block('Related source material', fileRows([...supporting, ...sectorAttachments])) : ''}
      ${block('Related Skarion offers', `<ul class="research-niches">${niche.offers.map(({ id, name }) => `<li><a href="../../offers/${id}/">${h(name)}</a></li>`).join('')}</ul>`)}
      `, { site: 'Niche research' }));
  }

  for (const site of sites) {
    const offer = offers[site.id];
    const keys = [offer.watchlist, ...(site.id === 'fiber' || site.id === 'gis' ? ['fiber-closeout'] : [])].filter(Boolean);
    const keyFiles = [
      ...(offer.benchmark ? [`${benchmark}${offer.benchmark}_`] : []),
      ...(offer.archivePrefixes ?? []),
      ...keys.flatMap((key) => [
        `gtm-social/watchlists/${key}.json`, `${shared}gtm-social/${key}/`, `social-source-snapshots/${key}-`,
      ]),
      ...(sourceOfferFolders[site.id] ? [`${bundle}${sourceOfferFolders[site.id]}/`] : []),
      ...(site.id === 'drafting' ? ['drafting-business/', `${shared}pdf/Skarion_Drafting_`, `${shared}pdf/skarion_drafting_linkedin/`] : []),
      ...(site.id === 'stormwater' ? ['official-supplements/'] : []),
    ];
    const offerFiles = selectFiles(files, keyFiles);
    await writePage(path.join(destination, 'offers', site.id), layout('../../', `${site.name} research`,
      'Offer benchmarks, launch plans, source files and related procurement work.', `
      ${offer.researchHighlights?.length ? block('Research and pilot priorities', `<ul>${offer.researchHighlights.map((item) => `<li>${h(item)}</li>`).join('')}</ul>`) : ''}
      ${block('Offer evidence and launch records', fileRows(offerFiles))}
      <p><a href="${repositoryFile(`sites/${site.id}/portfolio-review.md`)}">Open the portfolio and example project research</a></p>
      ${block('Related niches and RFPs', `<ul class="research-niches">${offer.niches.map((number) => nicheLink('../../', niches[number - 1])).join('')}</ul>`)}
      `, { site: 'Offer research' }));
  }

  await writePage(path.join(destination, 'archive'), layout('../', 'Research source archive',
    'Browse original files and frozen research outputs. The repository links require private access. Downloads are available in the local preview.', `
    <div class="archive-tools">
      <a href="${repositoryFile('research/README.md')}">Archive provenance</a>
      <a href="${repositoryFile('research/manifest.json')}">File fingerprints</a>
    </div>
    ${block(`All ${files.length} archived records`, `${filterBox('Search by title, file name or format')}${fileRows(files)}`, 'sources')}
    `, { filter: true }));
  return { files: files.length, niches: niches.length };
}
