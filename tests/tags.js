const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  const errs=[]; p.on('pageerror', e => errs.push(e.message));
  await p.goto('https://race-claude-code.pages.dev/printable-secret-santa-gift-tags');
  await p.fill('#tagNames', 'Alice\nBob\n<Carol>');
  await p.click('#tagMake');
  const n = await p.locator('#tagSheet .gtag').count();
  console.log('tags', n, (await p.locator('#tagSheet').innerText()).replace(/\n/g,' | ').slice(0,160));
  for (const path of ['/secret-santa-with-3-people','/secret-santa-reveal-ideas','/eco-friendly-secret-santa-gifts','/secret-santa-gifts-for-kids','/secret-santa-gifts-for-grandparents']) {
    const r = await p.goto('https://race-claude-code.pages.dev'+path); console.log(path, r.status(), await p.locator('h1').first().innerText());
  }
  console.log('errors', errs); await b.close();
})();
