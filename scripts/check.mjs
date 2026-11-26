import { readFile, readdir, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('..', import.meta.url));
const dist = path.join(root, 'dist');
const sites = JSON.parse(await readFile(path.join(root, 'sites.json'), 'utf8'));
const failures = [];

function expect(result, message) {
  if (!result) failures.push(message);
}

async function exists(file) {
  return Boolean(await stat(file).catch(() => null));
}

function fragments(html) {
  return [...html.matchAll(/\bid\s*=\s*["']([^"']+)["']/gi)].map((match) => match[1]);
}

async function checkReference(reference, page, html) {
  if (/^(?:https:|mailto:|tel:|data:)/i.test(reference)) return;
  const base = new URL(page, 'https://preview.invalid/');
  const url = new URL(reference, base);
  expect(url.origin === base.origin, `${page}: unsupported URL ${reference}`);
  if (url.origin !== base.origin) return;
  const location = decodeURIComponent(url.pathname);
  let target = path.join(dist, location);
  if (location.endsWith('/')) target = path.join(target, 'index.html');
  const found = await exists(target);
  expect(found, `${page}: missing local target ${reference}`);
  if (found && url.hash && target.endsWith('.html')) {
    const targetHtml = url.pathname === base.pathname ? html : await readFile(target, 'utf8');
    expect(fragments(targetHtml).includes(decodeURIComponent(url.hash.slice(1))), `${page}: unresolved anchor ${reference}`);
  }
}

async function checkPage(page) {
  const html = (await readFile(path.join(dist, page), 'utf8')).replace(/<!--[\s\S]*?-->/g, '');
  expect(/<html\b[^>]*\blang=["']en/i.test(html), `${page}: missing document language`);
  expect(/<title>[^<]+<\/title>/i.test(html), `${page}: missing title`);
  expect(/name=["']viewport["']/i.test(html), `${page}: missing viewport`);
  expect(/name=["']description["']/i.test(html), `${page}: missing search description`);
  expect(/name=["']robots["'][^>]*noindex/i.test(html), `${page}: preview can be indexed`);
  expect((html.match(/<h1[\s>]/gi) ?? []).length === 1, `${page}: expected one h1`);
  const ids = fragments(html);
  expect(ids.length === new Set(ids).size, `${page}: duplicate ids`);
  for (const [, reference] of html.matchAll(/\b(?:href|src)\s*=\s*["']([^"']+)["']/gi)) {
    await checkReference(reference, page, html);
  }
  for (const [image] of html.matchAll(/<img\b[^>]*>/gi)) {
    expect(/\balt\s*=\s*["']/i.test(image), `${page}: image needs alt text or an empty alt for decoration`);
  }
  return html;
}

const hub = await checkPage('/index.html');
const catalog = await checkPage('/catalog/index.html');
let projectCount = 0;
let fileCount = 0;
for (const { id, name } of sites) {
  const page = `/${id}/index.html`;
  const html = await checkPage(page);
  expect(hub.includes(`href="${id}/"`), `Preview is missing ${name}`);
  for (const anchor of ['main', 'services', 'process', 'contact']) {
    expect(fragments(html).includes(anchor), `${name}: missing ${anchor} section`);
  }
  expect(/<form\b[^>]*\bdata-intake\b/i.test(html), `${name}: missing intake form`);
  expect(/data-recipient=["']info@skarion\.com["']/i.test(html), `${name}: unexpected intake inbox`);
  expect(/\bdata-intake-status\b/i.test(html), `${name}: missing intake status`);
  expect(html.includes('mailto:info@skarion.com'), `${name}: missing direct email fallback`);
  expect(html.includes('shared/site.js'), `${name}: missing intake script`);
  expect(fragments(html).includes('example-projects'), `${name}: missing home project gallery`);
  expect(html.includes('href="./capabilities/"') && html.includes('href="./projects/"'), `${name}: missing primary navigation`);
  const original = path.join(root, 'sites', id);
  for (const file of ['logo.svg', 'brand.md', 'portfolio-review.md']) {
    expect(await exists(path.join(original, file)), `${name}: missing ${file}`);
  }

  const built = path.join(dist, id);
  expect(!(await readdir(built)).some((entry) => entry.endsWith('.md')), `${name}: review document leaked into build`);
  expect(!(await exists(path.join(built, 'content.json'))), `${name}: source content metadata leaked into build`);
  const css = await readFile(path.join(built, 'site.css'), 'utf8');
  for (const [, reference] of css.matchAll(/url\(\s*["']?([^"')]+)["']?\s*\)/gi)) {
    await checkReference(reference.trim(), `/${id}/site.css`, '');
  }

  const content = JSON.parse(await readFile(path.join(original, 'content.json'), 'utf8'));
  const capabilities = await checkPage(`/${id}/capabilities/index.html`);
  const library = await checkPage(`/${id}/projects/index.html`);
  expect(fragments(capabilities).includes('handoff'), `${name}: missing handoff specifications`);
  expect(capabilities.includes('Checks before handoff'), `${name}: missing capability checks`);
  expect(library.includes('synthetic data'), `${name}: library needs example disclosure`);
  for (const project of content.projects) {
    const example = await checkPage(`/${id}/projects/${project.id}/index.html`);
    expect(library.includes(`projects/${project.id}/`), `${name}: project missing from library`);
    expect(catalog.includes(`../${id}/projects/${project.id}/`), `${name}: project missing from team catalog`);
    expect(example.includes('Synthetic data'), `${name}/${project.id}: missing case disclosure`);
    expect(example.includes('Verification before handoff'), `${name}/${project.id}: missing verification`);
    expect(example.includes(`?project=${encodeURIComponent(project.title)}#contact`), `${name}/${project.id}: missing intake reference`);
    expect((example.match(/\sdownload>/g) ?? []).length === project.files.length, `${name}/${project.id}: incorrect download count`);
    projectCount++;
    fileCount += project.files.length;
  }
}

if (failures.length) {
  console.error(failures.map((message) => `- ${message}`).join('\n'));
  process.exitCode = 1;
} else {
  console.log(`Checked ${sites.length} sites, ${projectCount} project case studies, ${fileCount} sample downloads, and the preview hub.`);
}
