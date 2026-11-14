// Invitation generator on /secret-santa-invitation + new pages return 200. Usage: node invite.js [base]
const { chromium } = require('playwright');
const BASE = process.argv[2] || 'https://race-claude-code.pages.dev';
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto(BASE + '/secret-santa-invitation');
  await p.fill('#i_group', 'the Smith family'); await p.fill('#i_limit', '20');
  await p.fill('#i_by', 'Friday 28 November'); await p.fill('#i_day', 'Christmas Eve'); await p.fill('#i_from', 'Sam');
  let t = await p.inputValue('#i_out');
  if (!/the Smith family/.test(t) || !/£20/.test(t) || !/28 November/.test(t) || !/Christmas Eve/.test(t)) throw new Error('friendly text wrong: ' + t);
  await p.selectOption('#i_tone', 'work'); t = await p.inputValue('#i_out');
  if (!/^Hi all/.test(t)) throw new Error('work text wrong: ' + t);
  await p.selectOption('#i_tone', 'funny'); t = await p.inputValue('#i_out');
  if (!/naughty list/.test(t)) throw new Error('funny text wrong');
  await p.evaluate(() => document.getElementById('iWa').addEventListener('click', e => e.preventDefault()));
  await p.click('#iWa'); const href = await p.getAttribute('#iWa', 'href');
  if (!href.startsWith('https://wa.me/?text=') || !decodeURIComponent(href).includes('Smith')) throw new Error('wa href ' + href);
  if (!(await p.$('#names'))) throw new Error('draw form missing');
  if (errs.length) throw new Error('page errors: ' + errs.join('; '));
  for (const path of ['/secret-santa-for-remote-teams', '/secret-santa-exchange']) {
    const r = await p.goto(BASE + path); if (r.status() !== 200) throw new Error(path + ' ' + r.status());
  }
  console.log('invite.js OK'); await b.close();
})().catch(e => { console.error('FAIL', e.message); process.exit(1); });
