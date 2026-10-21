const { chromium } = require('playwright');
(async()=>{
  const [file,w,h,...times]=process.argv.slice(2);
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:+w,height:+h}});
  await p.goto('file://'+require('path').resolve(file));
  let last=0;
  for(const t of times){ await p.waitForTimeout((+t-last)*1000); last=+t;
    await p.screenshot({path:`${file}.${t}s.png`}); }
  await b.close();
})();
