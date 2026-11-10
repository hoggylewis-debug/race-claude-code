const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('https://race-claude-code.pages.dev/'); await p.waitForTimeout(1500);
  console.log('btn:', await p.textContent('#buyBtn'));
  await p.fill('#names', 'A\nB\nC\nD\nE\nF\nG'); await p.click('#drawBtn');
  console.log('upsell:', (await p.textContent('#msg')).slice(0,200));
  await p.click('#msg button'); await p.waitForTimeout(1500);
  console.log('status:', await p.textContent('#proStatus'));
  await p.click('#drawBtn'); await p.waitForTimeout(500);
  console.log('results visible:', await p.isVisible('#results'));
  await b.close();
})();
