// While the Pages secret is a TEST key, "Unlock Pro" (without ?sdtest=1) should unlock Pro free and allow a 7-person draw.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('https://race-claude-code.pages.dev/');
  await p.fill('#names', 'A\nB\nC\nD\nE\nF\nG');
  await p.click('#buyBtn');
  await p.waitForSelector('#proStatus .ok');
  console.log('status:', await p.textContent('#proStatus'));
  await p.click('#drawBtn');
  await p.waitForSelector('#results:not([hidden])');
  console.log('preview ok');
  await b.close();
})();
