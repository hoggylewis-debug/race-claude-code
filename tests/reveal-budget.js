const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
const enc=o=>{const k=Buffer.from('santadraw-2026');const d=Buffer.from(JSON.stringify(o));for(let i=0;i<d.length;i++)d[i]^=k[i%k.length];return d.toString('base64').replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'')};
for(const bud of ['£5','£25','']){const p=await b.newPage();await p.goto('https://race-claude-code.pages.dev/reveal#'+enc({f:'Ann',t:'Bob',b:bud}));await p.click('#gift');
console.log(bud||'(none)', await p.getAttribute('#gifts','href'), await p.textContent('#gifts'), await p.textContent('#to'));}
await b.close();})();
