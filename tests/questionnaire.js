const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  const errs=[]; p.on('pageerror', e=>errs.push(e.message));
  await p.goto('https://race-claude-code.pages.dev/secret-santa-questionnaire');
  await p.fill('#q_name','Priya'); await p.fill('#q_snack','salted caramel'); await p.fill('#q_avoid','no mugs');
  await p.click('#qWish');
  console.log('names:', JSON.stringify(await p.inputValue('#names')), 'wish:', JSON.stringify(await p.inputValue('#wish')));
  await p.click('#qWa', {noWaitAfter:true}).catch(()=>{});
  console.log('wa href:', (await p.getAttribute('#qWa','href')).slice(0,120));
  console.log('msg:', await p.textContent('#qMsg'), 'errors:', errs);
  await b.close();
})();
