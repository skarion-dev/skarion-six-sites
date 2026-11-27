import { createServer } from 'node:http';
import { createReadStream } from 'node:fs';
import { readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../dist/', import.meta.url));
const archive = fileURLToPath(new URL('../research/archive/', import.meta.url));
const manifest = JSON.parse(await readFile(new URL('../research/manifest.json', import.meta.url), 'utf8'));
const archivePaths = new Set(manifest.map(({ path: file }) => file));
const port = Number(process.env.SKARION_PREVIEW_PORT ?? 4173);
const types = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.avif': 'image/avif',
  '.webp': 'image/webp',
  '.gif': 'image/gif',
  '.ico': 'image/x-icon',
  '.woff2': 'font/woff2',
  '.txt': 'text/plain; charset=utf-8',
  '.csv': 'text/csv; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.geojson': 'application/geo+json; charset=utf-8',
  '.dxf': 'application/dxf',
  '.pdf': 'application/pdf',
};

createServer(async (request, response) => {
  try {
    if (!['GET', 'HEAD'].includes(request.method)) {
      response.writeHead(405, { Allow: 'GET, HEAD' }).end();
      return;
    }
    const url = new URL(request.url, 'http://127.0.0.1');
    const segments = decodeURIComponent(url.pathname).split('/').filter(Boolean);
    if (segments.some((segment) => segment.startsWith('.') || /[\\:\x00]/.test(segment))) {
      response.writeHead(404).end('Not found');
      return;
    }
    if (segments[0] === '_research_archive') {
      const name = segments.slice(1).join('/');
      if (!archivePaths.has(name)) {
        response.writeHead(404).end('Not found');
        return;
      }
      const file = path.join(archive, ...segments.slice(1));
      const details = await stat(file);
      response.writeHead(200, {
        'Content-Type': 'application/octet-stream',
        'Content-Length': details.size,
        'Content-Disposition': `attachment; filename*=UTF-8''${encodeURIComponent(path.basename(file))}`,
        'Cache-Control': 'no-store',
        'Cross-Origin-Resource-Policy': 'same-origin',
        'X-Robots-Tag': 'noindex, nofollow',
      });
      if (request.method === 'HEAD') response.end();
      else createReadStream(file).pipe(response);
      return;
    }
    let file = path.join(root, ...segments);
    const entry = await stat(file);
    if (entry.isDirectory()) {
      if (!url.pathname.endsWith('/')) {
        response.writeHead(308, { Location: `${url.pathname}/${url.search}` }).end();
        return;
      }
      file = path.join(file, 'index.html');
    }
    const details = await stat(file);
    const type = types[path.extname(file)];
    if (!details.isFile() || !type) {
      response.writeHead(404).end('Not found');
      return;
    }
    response.writeHead(200, {
      'Content-Type': type,
      'Content-Length': details.size,
      'Cache-Control': 'no-store',
      'X-Robots-Tag': 'noindex, nofollow',
    });
    if (request.method === 'HEAD') response.end();
    else createReadStream(file).pipe(response);
  } catch {
    response.writeHead(404).end('Not found');
  }
}).listen(port, '127.0.0.1', () => {
  console.log(`Local preview: http://127.0.0.1:${port}/`);
});
