export function escapeHtml(value) {
  return value.replace(/[&<>"']/g, (character) => (
    { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[character]
  ));
}

const h = escapeHtml;

function list(items) {
  return `<ul class="detail-list">${items.map((item) => `<li>${h(item)}</li>`).join('')}</ul>`;
}

function detail(title, items) {
  return `<section class="detail-column"><h3>${h(title)}</h3>${list(items)}</section>`;
}

function projectPath(project) {
  return `projects/${project.id}/`;
}

function projectCard(project, base, lazy = true) {
  return `<article class="project-tile">
    <a class="project-link" href="${base}${projectPath(project)}">
      <img src="${base}${h(project.image)}" alt="" width="720" height="432"${lazy ? ' loading="lazy"' : ''}>
      <div class="project-tile-body">
        <p class="detail-kicker">${h(project.category)}</p>
        <h3>${h(project.title)}</h3>
        <p>${h(project.summary)}</p>
        <span class="detail-meta">${project.files.length} sample ${project.files.length === 1 ? 'file' : 'files'}${project.draft ? ' · Draft' : ''}</span>
      </div>
    </a>
  </article>`;
}

function projectGrid(projects, base = '', lazy = true) {
  return `<div class="project-grid">${projects.map((project) => projectCard(project, base, lazy)).join('')}</div>`;
}

function navLinks(base, current) {
  const section = (path, text) => `<a href="${base}${path}/"${current === path ? ' aria-current="page"' : ''}>${text}</a>`;
  return `${section('capabilities', 'Capabilities')}
        ${section('projects', 'Projects')}
        <a href="${base}#process">Process</a>`;
}

function discussion(site, base, project) {
  const destination = project ? `${base}?project=${encodeURIComponent(project.title)}#contact` : `${base}#contact`;
  return `<section class="detail-discuss" aria-labelledby="discussion-heading">
    <div class="detail-width discussion-inner">
      <div><h2 id="discussion-heading">${project ? 'Planning similar work?' : 'Have a package to scope?'}</h2>
        <p>Tell ${h(site.name)} what records you have, what you need back and when your team needs it.</p></div>
      <a class="detail-button detail-button-solid" href="${destination}">${project ? 'Discuss a similar project' : 'Discuss your scope'}</a>
    </div>
  </section>`;
}

function shell(site, base, current, pageTitle, description, main) {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="${h(description)}">
  <meta name="robots" content="noindex,nofollow">
  <meta name="theme-color" content="${h(site.color)}">
  <link rel="icon" href="${base}logo.svg" type="image/svg+xml">
  <link rel="stylesheet" href="${base}shared/base.css">
  <link rel="stylesheet" href="${base}shared/details.css">
  <title>${h(pageTitle)} | ${h(site.name)}</title>
</head>
<body class="detail-page" data-lane="${site.id}">
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="detail-header">
    <div class="detail-width detail-header-inner">
      <a href="${base}" class="detail-brand"><img src="${base}logo.svg" width="40" height="40" alt=""><strong>${h(site.name)}</strong></a>
      <nav aria-label="Main navigation">${navLinks(base, current)}</nav>
      <a class="detail-button detail-button-outline" href="${base}#contact">Discuss scope</a>
    </div>
  </header>
  <main id="main" tabindex="-1">
  ${main}
  </main>
  <footer class="detail-footer">
    <div class="detail-width detail-footer-inner">
      <a href="${base}" class="detail-brand"><img src="${base}logo.svg" width="34" height="34" alt=""><strong>${h(site.name)}</strong></a>
      <p>A Skarion Engineering service</p>
      <a href="mailto:info@skarion.com">Email Skarion</a>
    </div>
  </footer>
</body>
</html>
`;
}

function breadcrumbs(base, current, insideProjects = false) {
  return `<nav class="detail-crumb" aria-label="Breadcrumb"><ol>
    <li><a href="${base}">Home</a></li>
    ${insideProjects ? `<li><a href="${base}projects/">Projects</a></li>` : ''}
    <li aria-current="page">${h(current)}</li>
  </ol></nav>`;
}

function capabilitiesPage(site, content) {
  const base = '../';
  const capabilitySections = content.capabilities.map((capability, index) => `<article class="capability" id="capability-${index + 1}">
    <div class="capability-heading"><h2>${h(capability.title)}</h2><p>${h(capability.summary)}</p></div>
    <div class="detail-columns">
      ${detail('Inputs we need', capability.inputs)}
      ${detail('What you receive', capability.outputs)}
      ${detail('Checks before handoff', capability.checks)}
    </div>
  </article>`).join('');

  return shell(site, base, 'capabilities', 'Capabilities', content.capabilityIntro, `
    <section class="detail-mast detail-width">
      ${breadcrumbs(base, 'Capabilities')}
      <h1>${h(site.scope)}</h1>
      <p class="detail-lead">${h(content.capabilityIntro)}</p>
      <dl class="role-list"><dt>Who we support</dt><dd>${h(content.buyerRoles.join(' · '))}</dd></dl>
    </section>
    <div class="detail-width capability-layout">
      <nav class="capability-index" aria-label="On this page">
        <p>On this page</p>
        <ul>${content.capabilities.map((item, index) => `<li><a href="#capability-${index + 1}">${h(item.title)}</a></li>`).join('')}
        <li><a href="#handoff">Handoff and responsibilities</a></li></ul>
      </nav>
      <div>
        ${capabilitySections}
        <article class="capability handoff-panel" id="handoff">
          <div class="capability-heading"><h2>Handoff and responsibilities</h2></div>
          <div class="detail-columns">${detail('Formats', content.handoff.formats)}${detail('What to confirm', content.handoff.requirements)}${detail('Review responsibilities', content.handoff.boundaries)}</div>
        </article>
      </div>
    </div>
    <section class="detail-width detail-section project-previews" aria-labelledby="related-projects">
      <div class="detail-section-heading"><h2 id="related-projects">See the work in context</h2><a class="detail-text-link" href="../projects/">Browse project examples</a></div>
      ${projectGrid(content.projects, base)}
    </section>
    ${discussion(site, base)}`);
}

function projectsPage(site, content) {
  const base = '../';
  return shell(site, base, 'projects', 'Example projects', `Illustrative ${site.scope.toLowerCase()} projects, technical workflows and downloadable sample files from ${site.name}.`, `
    <section class="detail-mast detail-width">
      ${breadcrumbs(base, 'Projects')}
      <h1>Example projects</h1>
      <p class="detail-lead">Review the starting records, scope decisions, finished outputs and checks. Each example includes files you can open and inspect.</p>
      <p class="sample-status">Illustrative projects built with synthetic data</p>
    </section>
    <section class="detail-width detail-section library-section" aria-label="Project directory">
      ${projectGrid(content.projects, base, false)}
      <p class="library-link"><a class="detail-text-link" href="../capabilities/">Review ${h(site.name)} capabilities and handoff formats</a></p>
    </section>
    ${discussion(site, base)}`);
}

function caseVisuals(project, base) {
  if (project.comparison) {
    return `<section class="case-comparison" aria-label="Before and after drawings">
      ${project.comparison.map(({ label, image, alt, caption }) => `<figure class="case-figure">
        <h2>${h(label)}</h2>
        <img src="${base}${h(image)}" alt="${h(alt)}" width="1350" height="904">
        <figcaption><span>${h(caption)}</span><a class="detail-text-link" href="${base}${h(image)}" target="_blank" rel="noopener" aria-label="Open full-size drawing, ${h(label)}">Open full-size drawing</a></figcaption>
      </figure>`).join('')}
    </section>`;
  }
  return `<figure class="case-figure"><img src="${base}${h(project.image)}" alt="${h(project.imageAlt)}" fetchpriority="high"><figcaption><span>${h(project.imageAlt)}</span><a class="detail-text-link" href="${base}${h(project.image)}" target="_blank" rel="noopener">Open full-size graphic</a></figcaption></figure>`;
}

function casePage(site, project, others) {
  const base = '../../';
  const files = project.files.map(({ path, label, description }) => {
    const format = path.split('.').at(-1).toUpperCase();
    return `<li><a class="download-link" href="${base}${h(path)}" download>
      <span><strong>${h(label)}</strong><span class="download-description">${h(description)}</span></span>
      <span class="download-format">${h(format)}</span>
    </a></li>`;
  }).join('');

  return shell(site, base, '', project.title, project.summary, `
    <section class="detail-mast case-mast detail-width">
      ${breadcrumbs(base, project.title, true)}
      <div class="case-intro">
        <div><p class="detail-kicker">${h(project.category)}</p><h1>${h(project.title)}</h1><p class="detail-lead">${h(project.summary)}</p></div>
        <div class="case-actions"><p class="sample-status">${project.draft ? 'Draft showcase' : 'Illustrative project'} · Synthetic data</p><a class="detail-button detail-button-solid" href="#sample-files">View sample files</a></div>
      </div>
      ${caseVisuals(project, base)}
    </section>
    <div class="detail-width case-layout">
      <div class="case-story">
        <section aria-labelledby="brief-heading"><h2 id="brief-heading">Project brief</h2><p>${h(project.context)}</p><h3>Scope constraints</h3>${list(project.constraints)}</section>
        <section aria-labelledby="workflow-heading"><h2 id="workflow-heading">Production workflow</h2>
          <ol class="case-steps">${project.approach.map(({ title, text }) => `<li><h3>${h(title)}</h3><p>${h(text)}</p></li>`).join('')}</ol>
        </section>
        <section aria-labelledby="QA-heading"><h2 id="QA-heading">Verification before handoff</h2>${list(project.verification)}<p class="review-note">${h(project.review)}</p></section>
      </div>
      <aside class="case-aside" aria-label="Handoff and sample files">
        <section class="case-outputs"><h2>Deliverables</h2>${list(project.deliverables)}</section>
        <section class="sample-files" id="sample-files" aria-labelledby="sample-files-heading">
          <h2 id="sample-files-heading">Download sample files</h2>
          <ul class="downloads">${files}</ul>
        </section>
      </aside>
    </div>
    <section class="detail-width detail-section project-previews" aria-labelledby="more-projects">
      <div class="detail-section-heading"><h2 id="more-projects">More project examples</h2><a class="detail-text-link" href="${base}projects/">All ${h(site.name)} projects</a></div>
      <div class="project-grid project-grid-pair">${others.map((other) => projectCard(other, base)).join('')}</div>
    </section>
    ${discussion(site, base, project)}`);
}

export function buildPages(site, content) {
  return [
    ['capabilities/index.html', capabilitiesPage(site, content)],
    ['projects/index.html', projectsPage(site, content)],
    ...content.projects.map((project) => [
      `${projectPath(project)}index.html`, casePage(site, project, content.projects.filter(({ id }) => id !== project.id)),
    ]),
  ];
}

export function buildCatalog(sites, contentBySite) {
  const caseCount = sites.reduce((count, { id }) => count + contentBySite.get(id).projects.length, 0);
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Browse technical project demonstrations and sample files across the six Skarion Engineering services.">
  <meta name="robots" content="noindex,nofollow">
  <link rel="stylesheet" href="../catalog-shared/base.css">
  <link rel="stylesheet" href="../catalog-shared/details.css">
  <title>Project library | Skarion Engineering</title>
</head>
<body class="detail-page">
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="detail-header"><div class="detail-width detail-header-inner catalog-header">
    <a class="detail-brand" href="../"><strong>Skarion Engineering</strong></a>
    <a href="../" class="detail-button detail-button-outline">Team preview</a>
  </div></div>
  <main id="main" tabindex="-1">
    <section class="detail-width detail-mast">
      ${breadcrumbs('../', 'Project library')}
      <h1>Project library</h1>
      <p class="detail-lead">Compare ${caseCount} example scopes across six services. Open a project to review the technical workflow and its downloadable files.</p>
      <p class="sample-status">Illustrative projects built with synthetic data</p>
      <nav class="catalog-nav" aria-label="Jump to service">${sites.map(({ id, name }) => `<a href="#${id}">${h(name)}</a>`).join('')}</nav>
    </section>
    ${sites.map(({ id, name, scope }) => `<section class="detail-width detail-section project-previews catalog-group" id="${id}" aria-labelledby="title-${id}">
      <div class="detail-section-heading"><div><p class="detail-kicker">${h(scope)}</p><h2 id="title-${id}">${h(name)}</h2></div><a class="detail-text-link" href="../${id}/capabilities/">View capabilities</a></div>
      ${projectGrid(contentBySite.get(id).projects, `../${id}/`)}
    </section>`).join('')}
  </main>
  <footer class="detail-footer"><div class="detail-width detail-footer-inner"><p>Skarion Engineering · Team preview</p><a href="../">Back to service websites</a></div></footer>
</body>
</html>
`;
}

export function expandHome(html, site, content) {
  const showcase = `<section class="home-work" id="example-projects" data-lane="${site.id}" aria-labelledby="work-heading">
      <div class="detail-width">
        <p class="detail-kicker">Illustrative projects · Synthetic data</p>
        <div class="detail-section-heading"><div><h2 id="work-heading">Example projects</h2><p>See the scope, review steps and sample files for each example.</p></div><a class="detail-text-link" href="projects/">Browse the project library</a></div>
        ${projectGrid(content.projects)}
        <div class="home-capabilities">
          <div><h2>Technical capabilities</h2><p>${h(content.capabilityIntro)}</p><a class="detail-text-link" href="capabilities/">View inputs, outputs and checks</a></div>
          <ul>${content.capabilities.map(({ title }, index) => `<li><a href="capabilities/#capability-${index + 1}">${h(title)}</a></li>`).join('')}</ul>
        </div>
      </div>
    </section>`;

  return html
    .replace('</head>', '  <link rel="stylesheet" href="shared/details.css">\n</head>')
    .replace('<!-- SITE_DETAIL_SHOWCASE -->', () => showcase);
}
