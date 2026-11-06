const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630}});
await p.goto('file:///tmp/pw/og.html');await p.screenshot({path:process.argv[2],type:'jpeg',quality:85});await b.close();})();
