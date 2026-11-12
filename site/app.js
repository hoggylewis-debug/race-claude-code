(function(){
'use strict';
var FREE_MAX = 6;
var KEY = 'santadraw-2026';
var $ = function(id){ return document.getElementById(id); };

// ---- encoding (shared with reveal.html) ----
function enc(obj){
  var bytes = new TextEncoder().encode(JSON.stringify(obj));
  var k = new TextEncoder().encode(KEY);
  var out = '';
  for (var i=0;i<bytes.length;i++) out += String.fromCharCode(bytes[i] ^ k[i % k.length]);
  return btoa(out).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
}

function isPro(){ try { return localStorage.getItem('sd_pro') === '1'; } catch(e){ return false; } }

function parseNames(){
  var seen = {}, out = [];
  $('names').value.split('\n').forEach(function(l){
    var n = l.trim().slice(0,40);
    if (n && !seen[n.toLowerCase()]) { seen[n.toLowerCase()] = 1; out.push(n); }
  });
  return out;
}
function lookup(names){ var m={}; names.forEach(function(n){ m[n.toLowerCase()] = n; }); return m; }

function parseExcl(names){
  var m = lookup(names), pairs = [], bad = [];
  $('excl').value.split('\n').forEach(function(l){
    if (!l.trim()) return;
    var p = l.split(/[,&+\/]| and /i).map(function(s){ return s.trim().toLowerCase(); }).filter(Boolean);
    if (p.length !== 2 || !m[p[0]] || !m[p[1]]) { bad.push(l.trim()); return; }
    pairs.push([m[p[0]], m[p[1]]]);
  });
  return {pairs:pairs, bad:bad};
}
function parseWish(names){
  var m = lookup(names), w = {};
  $('wish').value.split('\n').forEach(function(l){
    var i = l.indexOf(':'); if (i < 0) return;
    var n = m[l.slice(0,i).trim().toLowerCase()];
    if (n) w[n] = l.slice(i+1).trim().slice(0,200);
  });
  return w;
}

function draw(names, pairs){
  var blocked = {};
  names.forEach(function(n){ blocked[n] = {}; blocked[n][n] = 1; });
  pairs.forEach(function(p){ blocked[p[0]][p[1]] = 1; blocked[p[1]][p[0]] = 1; });
  for (var attempt=0; attempt<5000; attempt++){
    var pool = names.slice();
    for (var i=pool.length-1;i>0;i--){ var j = Math.floor(rand()*(i+1)); var t=pool[i]; pool[i]=pool[j]; pool[j]=t; }
    var ok = true;
    for (var x=0;x<names.length;x++){ if (blocked[names[x]][pool[x]]) { ok=false; break; } }
    if (ok){ var r={}; names.forEach(function(n,ix){ r[n]=pool[ix]; }); return r; }
  }
  return null;
}
function rand(){ var a = new Uint32Array(1); crypto.getRandomValues(a); return a[0] / 4294967296; }

var lastResult = null;
var groupUrl = '';
function groupMsg(){
  var g = lastResult && lastResult[0].meta.g;
  return '🎅 Our Secret Santa' + (g ? ' for ' + g : '') + ' has been drawn! Tap the link, choose your own name and see who you\'re buying for. No peeking at anyone else\'s! ' + groupUrl;
}
var SALES_CLOSED = false;
function checkSales(){
  fetch('/api/status').then(function(r){ return r.json(); }).then(function(j){
    if (j.sales) return;
    SALES_CLOSED = true;
    if (!isPro()){ $('buyBtn').textContent = 'Unlock Pro free for now'; $('proStatus').textContent = 'Card payments are paused at the moment, so Pro is free in this browser for now.'; }
  }).catch(function(){});
}

function upsell(text){
  var m = $('msg'); m.textContent = text + ' ';
  var b = document.createElement('button'); b.className = 'pro'; b.style.marginTop = '8px';
  b.textContent = SALES_CLOSED ? 'Unlock Pro free for now' : 'Unlock Pro for £2.49 (one-off)'; b.onclick = buy;
  m.appendChild(document.createElement('br')); m.appendChild(b);
  var s = document.createElement('div'); s.className = 'small'; s.style.fontWeight = '400';
  s.textContent = SALES_CLOSED ? 'Card payments are paused at the moment, so Pro is free in this browser. Your names are kept.' : 'Your names are kept while you pay. Secure checkout by Stripe. Full refund if it doesn\'t work for you.'; m.appendChild(s);
}

function doDraw(){
  $('msg').textContent = '';
  var names = parseNames();
  var pro = isPro();
  if (names.length < 3) { $('msg').textContent = 'Add at least 3 names, one per line.'; return; }
  if (!pro && names.length > FREE_MAX) {
    upsell('The free draw is for up to ' + FREE_MAX + ' people. You have ' + names.length + '. Pro unlocks any group size, plus exclusions and wishlists.'); return;
  }
  var ex = parseExcl(names), wish = parseWish(names);
  if (!pro && (ex.pairs.length || ex.bad.length || Object.keys(wish).length)) {
    upsell('Exclusions and wishlists are Pro features. Unlock Pro, or clear those boxes for a free draw.'); return;
  }
  if (ex.bad.length) { $('msg').textContent = 'Couldn\'t read these exclusions (names must match the list): ' + ex.bad.join('; '); return; }
  var res = draw(names, ex.pairs);
  if (!res) { $('msg').textContent = 'No valid draw is possible with those exclusions. Try removing one.'; return; }
  var meta = { g: $('group').value.trim().slice(0,60), b: $('budget').value.trim().slice(0,20), d: $('date').value.trim().slice(0,40) };
  var base = location.origin + '/reveal#';
  lastResult = names.map(function(n){
    var o = { f:n, t:res[n], g:meta.g, b:meta.b, d:meta.d };
    if (wish[res[n]]) o.w = wish[res[n]];
    return { name:n, to:res[n], url: base + enc(o), meta: meta, wish: wish[res[n]] || '' };
  });
  var gp = { p: lastResult.map(function(r){ var a=[r.name, r.to]; if (r.wish) a.push(r.wish); return a; }), g:meta.g, b:meta.b, d:meta.d };
  groupUrl = base + enc(gp);
  renderLinks();
  try { localStorage.removeItem('sd_form'); } catch(e){}
  if (window.plausible) plausible('draw', {props:{n:names.length, pro:pro}});
  fetch('/api/event?e=draw&n=' + names.length + '&pro=' + (pro?1:0)).catch(function(){});
}

function renderLinks(){
  var box = $('links'); box.innerHTML = '';
  var gb = $('groupLink');
  if (gb){
    $('groupWa').href = 'https://wa.me/?text=' + encodeURIComponent(groupMsg());
    $('groupCopy').onclick = function(){ copy(groupMsg(), $('groupCopy')); };
    if (navigator.share){ $('groupShare').hidden = false; $('groupShare').onclick = function(){ navigator.share({text: groupMsg()}).catch(function(){}); }; }
  }
  lastResult.forEach(function(r){
    var row = document.createElement('div'); row.className = 'link-row';
    var s = document.createElement('strong'); s.textContent = r.name; row.appendChild(s);
    var c = document.createElement('button'); c.className='secondary'; c.textContent='Copy link';
    c.onclick = function(){ copy(msgFor(r), c); }; row.appendChild(c);
    var w = document.createElement('a'); w.className='btn'; w.textContent='WhatsApp'; w.target='_blank'; w.rel='noopener';
    w.href = 'https://wa.me/?text=' + encodeURIComponent(msgFor(r)); row.appendChild(w);
    if (navigator.share){
      var sh = document.createElement('button'); sh.className='secondary'; sh.textContent='Share…';
      sh.onclick = function(){ navigator.share({text: msgFor(r)}).catch(function(){}); }; row.appendChild(sh);
    }
    box.appendChild(row);
  });
  $('results').hidden = false;
  $('results').scrollIntoView({behavior:'smooth'});
}
function msgFor(r){
  return 'Hi ' + r.name + '! 🎅 Your Secret Santa' + (r.meta.g ? ' for ' + r.meta.g : '') + ' is ready. Tap to see who you\'re buying for (keep it secret!): ' + r.url;
}
function copy(text, btn){
  var done = function(){ if (btn){ var o = btn.textContent; btn.textContent='Copied ✓'; setTimeout(function(){ btn.textContent=o; },1500);} };
  if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function(){ prompt('Copy this:', text); });
  else { prompt('Copy this:', text); }
}

function printCards(){
  if (!isPro()) { $('proCard').scrollIntoView({behavior:'smooth'}); $('proStatus').textContent='Printable cards are a Pro feature.'; return; }
  if (!lastResult) return;
  var pa = $('printArea'); pa.innerHTML='';
  lastResult.forEach(function(r){
    var d = document.createElement('div'); d.className='card';
    var h = document.createElement('h3'); h.textContent = '🎁 ' + r.name + ', you are Secret Santa for:'; d.appendChild(h);
    var n = document.createElement('div'); n.className='name-big'; n.textContent = r.to; d.appendChild(n);
    var p = document.createElement('p');
    p.textContent = [r.meta.g, r.meta.b && ('Limit: ' + r.meta.b), r.meta.d && ('Exchange: ' + r.meta.d), r.wish && ('Hints: ' + r.wish)].filter(Boolean).join(' · ');
    d.appendChild(p); pa.appendChild(d);
  });
  ['formCard','proCard','results'].forEach(function(id){ $(id).classList.add('noprint'); });
  pa.hidden = false; window.print();
  setTimeout(function(){ pa.hidden = true; }, 500);
}

// ---- payments ----
function saveForm(){
  try { localStorage.setItem('sd_form', JSON.stringify({g:$('group').value,b:$('budget').value,d:$('date').value,n:$('names').value,e:$('excl').value,w:$('wish').value})); } catch(e){}
}
function restoreForm(){
  try {
    var f = JSON.parse(localStorage.getItem('sd_form') || 'null'); if (!f) return;
    $('group').value=f.g||''; $('budget').value=f.b||''; $('date').value=f.d||''; $('names').value=f.n||''; $('excl').value=f.e||''; $('wish').value=f.w||'';
  } catch(e){}
}
function buy(){
  saveForm();
  $('buyBtn').disabled = true; $('proStatus').textContent = 'Opening secure checkout…';
  fetch('/api/checkout' + (/sdtest=1/.test(location.search) ? '?test=1' : ''), {method:'POST'}).then(function(r){ return r.json(); }).then(function(j){
    if (j.preview){ try { localStorage.setItem('sd_pro','1'); localStorage.setItem('sd_preview','1'); } catch(e){} updateProUI(); $('msg').textContent=''; $('proStatus').innerHTML = '<span class="ok">✓ Card payments are paused at the moment, so Pro is free in this browser for now. Enjoy, and tell a friend!</span>'; return; }
    if (j.url) location.href = j.url; else throw new Error(j.error || 'checkout failed');
  }).catch(function(){ $('buyBtn').disabled=false; $('proStatus').textContent='Sorry, checkout is unavailable right now. Please try again in a minute.'; });
}
function updateProUI(){
  var pro = isPro();
  $('proSection').classList.toggle('locked', !pro);
  if (pro){ $('buyBtn').hidden = true; var pv=false; try{pv=localStorage.getItem('sd_preview')==='1';}catch(e){} $('proStatus').innerHTML = '<span class="ok">✓ Pro is unlocked in this browser' + (pv ? ' (free preview).' : '. Thank you!') + '</span>'; }
}
function checkReturn(){
  var p = new URLSearchParams(location.search), sid = p.get('paid');
  restoreForm();
  if (p.get('cancelled')) $('proStatus').textContent = 'Checkout cancelled. Your names are still here.';
  if (!sid) return;
  $('proStatus').textContent = 'Confirming payment…';
  fetch('/api/verify?session_id=' + encodeURIComponent(sid)).then(function(r){ return r.json(); }).then(function(j){
    if (j.paid){ try { localStorage.setItem('sd_pro','1'); localStorage.removeItem('sd_preview'); } catch(e){} updateProUI(); }
    else $('proStatus').textContent = 'We couldn\'t confirm that payment yet. Refresh in a moment.';
    history.replaceState(null,'','/');
  }).catch(function(){ $('proStatus').textContent = 'Couldn\'t confirm payment. Refresh to retry.'; });
}

$('drawBtn').onclick = doDraw;
$('buyBtn').onclick = buy;
checkSales();
$('printBtn').onclick = printCards;
$('redraw').onclick = function(){ $('results').hidden = true; $('formCard').scrollIntoView({behavior:'smooth'}); };
$('copyAll').onclick = function(){ if (lastResult) copy(lastResult.map(function(r){ return r.name + ': ' + r.url; }).join('\n'), $('copyAll')); };
updateProUI();
checkReturn();
})();
