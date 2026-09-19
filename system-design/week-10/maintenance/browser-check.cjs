// Optional author QA; uses installed Playwright, never downloads dependencies.
// From week-10: PLAYWRIGHT_MODULE=/absolute/path/to/playwright node maintenance/browser-check.cjs
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const path = require('node:path');
const fs = require('node:fs');
const { pathToFileURL } = require('node:url');
const root = path.resolve(__dirname, '..');
(async () => {
  const browser = await chromium.launch({executablePath: process.env.BROWSER_BIN || '/usr/bin/chromium', headless: true, args: ['--no-sandbox']});
  const pages = ['index.html', ...fs.readdirSync(path.join(root, 'lessons')).filter(x => x.endsWith('.html')).map(x => 'lessons/' + x), 'reference/glossary.html', 'reference/review-card.html'];
  const out = path.join(root, 'runtime', 'browser');
  fs.mkdirSync(out, {recursive: true});
  let checks = 0;
  try {
    for (const width of [390, 1280]) {
      const page = await browser.newPage({viewport: {width, height: 900}});
      const errors = [];
      page.on('pageerror', error => errors.push(error.message));
      page.on('requestfailed', request => errors.push(request.url()));
      for (const file of pages) {
        await page.goto(pathToFileURL(path.join(root, file)).href);
        const result = await page.evaluate(() => ({
          overflow: document.documentElement.scrollWidth > innerWidth,
          h1: document.querySelectorAll('h1').length,
          font: getComputedStyle(document.body).fontFamily,
          details: document.querySelectorAll('details').length
        }));
        if (result.overflow || result.h1 !== 1 || !result.font.includes('Georgia')) throw new Error(file + ': ' + JSON.stringify(result));
        if (result.details) {
          await page.locator('summary').first().click();
          if (!await page.locator('details').first().getAttribute('open').then(x => x !== null)) throw new Error('Disclosure failed: ' + file);
        }
        checks++;
      }
      await page.goto(pathToFileURL(path.join(root, 'index.html')).href);
      await page.screenshot({path: path.join(out, 'desk-' + width + '.png'), fullPage: true});
      await page.goto(pathToFileURL(path.join(root, 'lessons/0008-instrumentation.html')).href);
      await page.screenshot({path: path.join(out, 'lesson-' + width + '.png'), fullPage: true});
      await page.emulateMedia({media: 'print'});
      const print = await page.evaluate(() => ({background: getComputedStyle(document.body).backgroundColor, width: document.documentElement.scrollWidth <= innerWidth}));
      if (!print.width || print.background !== 'rgb(255, 255, 255)') throw new Error('Print styling failed');
      if (width === 1280) await page.pdf({path: path.join(out, 'lesson-print.pdf'), preferCSSPageSize: true});
      if (errors.length) throw new Error(errors.join('\n'));
      await page.close();
    }
    console.log(JSON.stringify({pageViewportChecks: checks, widths: [390,1280], screenshots: out, print: 'emulated + PDF generated'}));
  } finally { await browser.close(); }
})().catch(error => {console.error(error); process.exitCode = 1;});
