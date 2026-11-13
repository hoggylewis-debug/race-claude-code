const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  for (const s of ['secret-santa-for-nurses','secret-santa-for-big-families','secret-santa-for-clubs','secret-santa-generator-uk']) {
    const r = await p.goto('https://race-claude-code.pages.dev/' + s); if (r.status() !== 200) throw s;
    if (!(await p.locator('#names').count())) throw 'no draw form ' + s;
  }
  await p.goto('https://race-claude-code.pages.dev/secret-santa-budget-calculator');
  let t = await p.textContent('#c_out'); console.log(t);
  if (!t.includes('£90') || !t.includes('£700')) throw 'calc default wrong';
  await p.fill('#c_lim', '100'); t = await p.textContent('#c_out'); console.log(t);
  if (!t.includes('save money')) throw 'calc branch';
  if (errs.length) throw errs.join(';');
  console.log('OK'); await b.close();
})().catch(e => { console.error('FAIL', e); process.exit(1); });
