#!/usr/bin/env python3
"""Builds the landing pages in site/ from src/template.html. Run: python3 src/build.py"""
import os, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://race-claude-code.pages.dev'
T = open(os.path.join(ROOT, 'src/template.html')).read()
SUB = 'Secret Santa names drawn in 30 seconds. No sign-up. No email addresses.<br>Post one link in your WhatsApp group, or send everyone their own private link.'

EXTRA_Q = '<div class="card" id="questionnaire"><h2 style="margin-top:0">Free Secret Santa questionnaire</h2>\n<p>Fill this in (or send the page to your group) and copy your answers into the group chat, an email, or the wishlist box above. Nothing you type here is sent anywhere: it stays on your phone.</p>\n<label for="q_name">Your name</label><input id="q_name" placeholder="e.g. Priya" maxlength="80"><label for="q_colour">Favourite colour</label><input id="q_colour" placeholder="e.g. green" maxlength="80"><label for="q_snack">Favourite sweets or snacks</label><input id="q_snack" placeholder="e.g. salted caramel, crisps" maxlength="80"><label for="q_drink">Favourite drink (hot or otherwise)</label><input id="q_drink" placeholder="e.g. oat latte, ginger beer" maxlength="80"><label for="q_hobby">Hobbies or things you love doing</label><input id="q_hobby" placeholder="e.g. running, baking, gaming" maxlength="80"><label for="q_media">Favourite film, TV show or book</label><input id="q_media" placeholder="e.g. Paddington 2" maxlength="80"><label for="q_collect">Something you collect or always use</label><input id="q_collect" placeholder="e.g. candles, notebooks" maxlength="80"><label for="q_avoid">Anything you DON\'T want</label><input id="q_avoid" placeholder="e.g. no mugs, no smellies" maxlength="80"><label for="q_allergy">Allergies or foods to avoid</label><input id="q_allergy" placeholder="e.g. nuts" maxlength="80"><label for="q_size">Clothes size (if relevant)</label><input id="q_size" placeholder="e.g. M, size 6 shoes" maxlength="80"><label for="q_dream">Your dream gift under the limit</label><input id="q_dream" placeholder="e.g. a nice hot chocolate set" maxlength="80">\n<p style="margin-top:12px"><button id="qCopy">Copy my answers</button> <a class="btn" id="qWa" target="_blank" rel="noopener" href="#">Send on WhatsApp</a> <button class="secondary" id="qWish">Add to the wishlist box above</button></p>\n<p id="qMsg" class="small"></p>\n<h3>The questions (for printing or pasting into a form)</h3>\n<ol><li>Favourite colour</li><li>Favourite sweets or snacks</li><li>Favourite drink (hot or otherwise)</li><li>Hobbies or things you love doing</li><li>Favourite film, TV show or book</li><li>Something you collect or always use</li><li>Anything you DON\'T want</li><li>Allergies or foods to avoid</li><li>Clothes size (if relevant)</li><li>Your dream gift under the limit</li></ol>\n<h3>How to use a questionnaire at work</h3>\n<ul><li>Post this page\'s link in your team chat and ask everyone to send their answers to the organiser, or straight into the draw\'s wishlist box.</li>\n<li>Keep it short: 5 to 8 questions get answered, 25 don\'t.</li>\n<li>Always ask "anything you don\'t want?" and about allergies. It saves the most gifts.</li></ul>\n<p>Once you have everyone\'s answers, draw names above. With SantaDraw Pro (a one-off £2.49), paste each person\'s answers into the wishlist box and their Secret Santa sees them on their private link.</p></div>\n<script>(function(){var L=[[\'colour\',\'Favourite colour\'],[\'snack\',\'Favourite sweets or snacks\'],[\'drink\',\'Favourite drink (hot or otherwise)\'],[\'hobby\',\'Hobbies or things you love doing\'],[\'media\',\'Favourite film, TV show or book\'],[\'collect\',\'Something you collect or always use\'],[\'avoid\',\'Anything you DON\\\'T want\'],[\'allergy\',\'Allergies or foods to avoid\'],[\'size\',\'Clothes size (if relevant)\'],[\'dream\',\'Your dream gift under the limit\']];function txt(){var n=document.getElementById(\'q_name\').value.trim();var out=[];L.forEach(function(x){var v=document.getElementById(\'q_\'+x[0]).value.trim();if(v)out.push(x[1]+\': \'+v)});return {n:n,lines:out}}\nfunction full(){var t=txt();return \'\\uD83C\\uDF85 Secret Santa questionnaire\'+(t.n?\' - \'+t.n:\'\')+\'\\n\'+t.lines.join(\'\\n\')}\nfunction msg(m){document.getElementById(\'qMsg\').textContent=m}\ndocument.getElementById(\'qCopy\').onclick=function(){var s=full();if(navigator.clipboard)navigator.clipboard.writeText(s).then(function(){msg(\'Copied. Paste it into your group chat or email.\')},function(){msg(s)});else msg(s)};\ndocument.getElementById(\'qWa\').onclick=function(e){this.href=\'https://wa.me/?text=\'+encodeURIComponent(full()+\'\\n\\nMade with https://race-claude-code.pages.dev/secret-santa-questionnaire\')};\ndocument.getElementById(\'qWish\').onclick=function(){var t=txt();if(!t.n){msg(\'Add your name first.\');return}var w=document.getElementById(\'wish\');var hint=t.lines.map(function(l){return l.replace(/^[^:]+: /,\'\')}).join(\', \').slice(0,200);w.value=(w.value?w.value.replace(/\\s+$/,\'\')+\'\\n\':\'\')+t.n+\': \'+hint;var nm=document.getElementById(\'names\');if(nm.value.split(\'\\n\').map(function(x){return x.trim()}).indexOf(t.n)<0)nm.value=(nm.value?nm.value.replace(/\\s+$/,\'\')+\'\\n\':\'\')+t.n;msg(\'Added to the draw. Wishlists are a Pro feature; scroll up to see it.\');document.getElementById(\'formCard\').scrollIntoView({behavior:\'smooth\'})};})();</script>'

TAGS = '''<div class="card" id="tags"><h2 style="margin-top:0">Make your printable gift tags</h2>
<p>Type who each present is for (one name per line). We make a sheet of tags signed "From: your Secret Santa 🎅". Print it, cut along the lines, and tie one to each gift. Nothing is uploaded.</p>
<textarea id="tagNames" rows="5" style="width:100%" placeholder="Alice&#10;Bob&#10;Charlie"></textarea>
<p><label>Message: <input id="tagMsg" value="Merry Christmas!" style="width:60%"></label></p>
<p><button type="button" id="tagMake">Make tags</button> <button type="button" id="tagPrint">Print tags</button></p>
<div id="tagSheet" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:8px"></div>
<style>.gtag{border:2px dashed #b22;border-radius:10px;padding:10px;text-align:center;background:#fff;color:#222;page-break-inside:avoid}.gtag b{font-size:1.2em;display:block}@media print{body *{visibility:hidden}#tagSheet,#tagSheet *{visibility:visible}#tagSheet{position:absolute;left:0;top:0;width:100%}}</style>
<script>(function(){function esc(s){return s.replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function make(){var n=document.getElementById('tagNames').value.split(/\\n/).map(function(x){return x.trim()}).filter(Boolean);if(!n.length)n=['','','','','',''];var m=esc(document.getElementById('tagMsg').value);
document.getElementById('tagSheet').innerHTML=n.map(function(x){return '<div class="gtag">🎁<br>To:<b>'+(esc(x)||'&nbsp;')+'</b>'+m+'<br><small>From: your Secret Santa 🎅</small></div>'}).join('')}
document.getElementById('tagMake').onclick=make;document.getElementById('tagPrint').onclick=function(){make();window.print()};make();})();</script>
<p>Tip: after the draw, everyone can print a tag for the person they're buying for, so the handwriting never gives them away.</p></div>'''

PAGES = [
 dict(path='/', file='index.html', nav='Secret Santa generator',
  title='Secret Santa Generator: free draw, private WhatsApp links, no sign-up | SantaDraw',
  desc='Draw names for Secret Santa in 30 seconds. No sign-up, no emails. Everyone gets a private link to send by WhatsApp or text. Add exclusions for couples and wishlists.',
  h1='🎅 Secret Santa Generator', sub=SUB, extra=''),
 dict(path='/secret-santa-whatsapp', file='secret-santa-whatsapp.html', nav='Secret Santa on WhatsApp',
  title='Secret Santa on WhatsApp: draw names and send private links | SantaDraw',
  desc='Run your family or friends Secret Santa in a WhatsApp group. Draw names free, then send each person a private link that reveals only who they are buying for.',
  h1='🎅 Secret Santa for WhatsApp groups',
  sub='Draw names here, then send each person their own private link on WhatsApp.<br>Nobody needs an app, an account or an email address.',
  extra='''<div class="card"><h2 style="margin-top:0">How to do Secret Santa in a WhatsApp group</h2>
<ol><li>Type everyone in the group above and press <strong>Draw names</strong>.</li>
<li>Next to each name, tap <strong>WhatsApp</strong>. It opens a ready-written message with that person's private link. Choose the person and send.</li>
<li>Each person taps their link to see who they're buying for. Their link shows only their own match.</li>
<li>Post the spending limit and date in the group chat, and you're done.</li></ol>
<p><strong>Even quicker: one link for the whole group.</strong> After the draw, tap <strong>Send to WhatsApp group</strong> and post a single link in your group chat. Everyone taps it, chooses their own name and sees only who they're buying for. Each phone can only pick one name, so it works on trust, like pulling names from a hat. For a strictly private draw, send the individual links privately instead.</p></div>'''),
 dict(path='/secret-santa-with-exclusions', file='secret-santa-with-exclusions.html', nav='Secret Santa with exclusions (couples)',
  title='Secret Santa Generator with Exclusions: stop couples drawing each other | SantaDraw',
  desc='A Secret Santa name draw with exclusions, so couples, housemates or last year\'s pairs never draw each other. No sign-up, private links for everyone.',
  h1='🎅 Secret Santa with exclusions',
  sub='Stop couples, siblings or last year\'s pairs drawing each other.<br>Add exclusions, draw, and send everyone a private link.',
  extra='''<div class="card"><h2 style="margin-top:0">Why use exclusions?</h2>
<p>Couples already buy each other presents, so most families make sure partners don't draw each other. Some groups also stop people getting the same person as last year, or keep kids from drawing their own parents.</p>
<p>Type each pair that shouldn't match on its own line in the <strong>Exclusions</strong> box, like <code>Sam, Alex</code>. Exclusions work both ways. If the rules make a draw impossible (for example, too many exclusions in a small group), SantaDraw tells you so instead of quietly breaking a rule.</p>
<p>Exclusions are part of SantaDraw Pro, a one-off £2.49, which also unlocks groups bigger than 6, wishlists and printable cards.</p></div>'''),
 dict(path='/office-secret-santa', file='office-secret-santa.html', nav='Office Secret Santa',
  title='Office Secret Santa Generator: draw names for your team, no sign-up | SantaDraw',
  desc='Organise an office or team Secret Santa in a minute. Draw names, set a budget and date, and send each colleague a private link by Slack, Teams or email.',
  h1='🎅 Office Secret Santa',
  sub='Draw names for your whole team in a minute. Set the budget and date,<br>then send each colleague a private link on Slack, Teams or email.',
  extra='''<div class="card"><h2 style="margin-top:0">Running a work Secret Santa</h2>
<ul><li><strong>Set a clear spending limit</strong> (£10 to £20 is common at work) so nobody feels awkward.</li>
<li><strong>Agree a date</strong>, e.g. the last day before the Christmas break or the team lunch.</li>
<li><strong>Make it opt-in.</strong> Only add people who've said yes.</li>
<li><strong>Use wishlists</strong> so people get something they actually want. Each person sees their recipient's hints.</li>
<li><strong>Remote team?</strong> Ask people to post gifts to each other, or use a gift card with a personal note.</li></ul>
<p>No colleague needs an account, and SantaDraw never stores names or email addresses. Teams bigger than 6 need SantaDraw Pro (£2.49 one-off, often cheaper than one mince pie per person).</p></div>'''),
 dict(path='/virtual-secret-santa', file='virtual-secret-santa.html', nav='Virtual Secret Santa',
  title='Virtual Secret Santa: draw names online for remote friends and teams | SantaDraw',
  desc='Run a virtual Secret Santa for friends or remote colleagues. Draw names online free, send private links, share wishlists and delivery hints.',
  h1='🎅 Virtual Secret Santa',
  sub='For friends and teams in different places. Draw names online,<br>send private links, and share wishlists so gifts arrive right.',
  extra='''<div class="card"><h2 style="margin-top:0">Virtual Secret Santa tips</h2>
<ul><li>Set the exchange date a week before your video call so posted gifts arrive in time.</li>
<li>Ask people to put a gift idea in the wishlist box (Pro), plus whether a digital gift or gift card is fine.</li>
<li>Open presents together on a video call, then guess who your Santa was.</li></ul></div>'''),
 dict(path='/how-to-organise-secret-santa', file='how-to-organise-secret-santa.html', nav='How to organise Secret Santa',
  title='How to Organise Secret Santa: rules, budget and a free name draw | SantaDraw',
  desc='A simple guide to organising Secret Santa for family, friends or work: picking a budget, setting rules, drawing names fairly and keeping it secret.',
  h1='🎅 How to organise Secret Santa',
  sub='Everything you need to run a fair, fun Secret Santa,<br>plus a free name draw right here on the page.',
  extra='''<div class="card"><h2 style="margin-top:0">Secret Santa in 5 steps</h2>
<ol><li><strong>Find out who's in.</strong> Ask in your family or friends chat. 3 people is the minimum, 5 to 15 is ideal.</li>
<li><strong>Agree a spending limit.</strong> £10, £20 and £25 are the most common. A clear limit avoids awkward mismatches.</li>
<li><strong>Pick the exchange date.</strong> Christmas Day, a party, or a video call.</li>
<li><strong>Draw names fairly.</strong> Use the draw above: nobody gets themselves, and with Pro you can stop couples drawing each other.</li>
<li><strong>Keep it secret.</strong> Send each person only their own link. On the day, everyone guesses who their Santa was.</li></ol>
<h3>Popular Secret Santa rules</h3>
<ul><li>Stick to the limit, no going over.</li>
<li>Include a gift receipt.</li>
<li>Theme ideas: "something you can eat", "under £10 and handmade", "a book you love".</li>
<li>Wishlists: everyone writes 2 or 3 ideas so nobody gets a mug they don't want.</li></ul></div>'''),
 dict(path='/family-secret-santa', file='family-secret-santa.html', nav='Family Secret Santa',
  title='Family Secret Santa Generator: draw names for Christmas, no sign-up | SantaDraw',
  desc='Draw names for your family Secret Santa in 30 seconds. Stop couples drawing each other, add wishlists, and send each relative a private link by WhatsApp or text.',
  h1='🎅 Family Secret Santa',
  sub='One good present each instead of a pile of small ones.<br>Draw names for the whole family and send everyone a private link.',
  extra='''<div class="card"><h2 style="margin-top:0">Why families switch to Secret Santa</h2>
<p>Once a family gets big, buying for everyone gets expensive and stressful. With Secret Santa each adult buys one thoughtful present for one person, usually with a £20 to £50 limit.</p>
<ul><li><strong>Couples:</strong> add them as exclusions (Pro) so partners don't draw each other.</li>
<li><strong>Kids:</strong> many families keep buying for all the children and only do Secret Santa between adults. Just leave the kids off the list.</li>
<li><strong>Relatives abroad:</strong> they get their link by WhatsApp like everyone else.</li>
<li><strong>Gran who doesn't do phones?</strong> Print the cards (Pro) and hand them out.</li></ul></div>'''),
 dict(path='/draw-names-from-a-hat', file='draw-names-from-a-hat.html', nav='Draw names from a hat online',
  title='Draw Names From a Hat Online: free random name picker for gift exchanges | SantaDraw',
  desc='The online version of drawing names out of a hat for a gift exchange. Nobody picks themselves, nobody has to be in the same room, and everyone gets a private result.',
  h1='🎩 Draw names from a hat, online',
  sub='Like pulling names from a hat, but nobody needs to be in the same room<br>and nobody ever picks themselves.',
  extra='''<div class="card"><h2 style="margin-top:0">Better than a real hat</h2>
<ul><li><strong>No redraws:</strong> with a real hat someone always pulls their own name. Here it can't happen.</li>
<li><strong>Everyone can join from anywhere:</strong> results go out as private links.</li>
<li><strong>Rules built in:</strong> stop couples drawing each other with exclusions (Pro).</li>
<li><strong>Still want paper?</strong> Print a card for each person (Pro).</li></ul></div>'''),
 dict(path='/secret-santa-gift-ideas', file='secret-santa-gift-ideas.html', nav='Secret Santa gift ideas',
  title='Secret Santa Gift Ideas Under £10, £20 and £30 (plus a free name draw) | SantaDraw',
  desc='Simple Secret Santa gift ideas for every budget: under £10, under £20 and under £30. Plus a free Secret Santa generator with wishlists so you know what they want.',
  h1='🎁 Secret Santa gift ideas',
  sub='Ideas for every budget, and a free draw with wishlists<br>so you know what your person actually wants.',
  extra='''<div class="card"><h2 style="margin-top:0">Under £10</h2>
<ul><li>A nice hot chocolate or tea selection with a mug</li><li>Fancy socks or a novelty hat</li><li>A paperback by an author they like</li><li>A small houseplant or succulent</li><li>Posh chocolate or a bag of their favourite sweets</li><li>A pocket card or travel game</li></ul>
<h2>Under £20</h2>
<ul><li>A cosy blanket or hot water bottle</li><li>A good notebook and pen</li><li>A scented candle</li><li>A cookbook for a cuisine they love</li><li>A jigsaw puzzle</li><li>Local food or drink treats from a market</li></ul>
<h2>Under £30</h2>
<ul><li>Wireless earbuds or a small speaker (look for good-value brands)</li><li>A board game for the family</li><li>An experience voucher: cinema, bowling, a class</li><li>A personalised print or photo book</li><li>Good gloves and a scarf</li></ul>
<p><strong>Best tip:</strong> ask everyone to add 2 or 3 ideas to the wishlist box when you draw (Pro). Whoever draws them sees the hints in their private link, so nobody gets a gift they don't want.</p>
<p>More ideas: <a href="/secret-santa-gifts-under-5">gifts under £5</a> · <a href="/secret-santa-gifts-under-10">gifts under £10</a> · <a href="/secret-santa-gifts-under-20">gifts under £20</a></p></div>'''),
 dict(path='/secret-santa-for-kids', file='secret-santa-for-kids.html', nav='Secret Santa for kids and classes',
  title='Secret Santa for Kids: easy name draw for children, cousins and school classes | SantaDraw',
  desc='Run a Secret Santa for kids, cousins or a school class. Draw names in seconds, set a small budget, and print a card for each child. No accounts or emails needed.',
  h1='🎅 Secret Santa for kids',
  sub='For cousins, Brownies, clubs and classes. Draw names in seconds,<br>then send the links to parents or print a card for each child.',
  extra='''<div class="card"><h2 style="margin-top:0">Tips for a children's Secret Santa</h2>
<ul><li><strong>Keep the budget small and clear:</strong> £5 or £10 works well, so no child feels left out.</li>
<li><strong>Send links to the parents</strong>, not the children, so a grown-up helps with shopping and keeps the secret.</li>
<li><strong>Young children?</strong> Print a card for each child (Pro) and hand them out in sealed envelopes.</li>
<li><strong>Siblings:</strong> add brothers and sisters as exclusions (Pro) so they buy for a cousin or friend instead.</li>
<li><strong>Wishlists:</strong> ask each child for 2 or 3 ideas ("dinosaurs, slime, anything purple") and add them as hints (Pro).</li></ul>
<p>SantaDraw never stores names. Everything happens in your browser, which matters when the names are children's.</p></div>'''),
 dict(path='/secret-santa-rules', file='secret-santa-rules.html', nav='Secret Santa rules',
  title='Secret Santa Rules: the simple rules every group should agree | SantaDraw',
  desc='The Secret Santa rules most groups use: spending limit, keeping it secret, couples, gift receipts and what to do if someone drops out. Plus a free name draw.',
  h1='📜 Secret Santa rules',
  sub='The rules everyone should agree before the draw,<br>and a free name draw to make it fair.',
  extra='''<div class="card"><h2 style="margin-top:0">The classic Secret Santa rules</h2>
<ol><li><strong>Everyone buys for one person</strong>, chosen at random, and never for themselves.</li>
<li><strong>Stick to the spending limit.</strong> Going way over is as awkward as going under.</li>
<li><strong>Keep it secret</strong> until the gifts are opened. Don't tell anyone who you drew.</li>
<li><strong>Partners don't draw each other</strong> (common in families; use exclusions).</li>
<li><strong>Include a gift receipt</strong> where you can.</li>
<li><strong>Give it on the agreed date</strong>, or post it in time for a virtual exchange.</li></ol>
<h3>What if someone drops out after the draw?</h3>
<p>The fairest fix is to redraw: remove their name and draw again (it takes 30 seconds), then send the new links. If only one person is affected, the organiser can quietly buy for the person who's lost their Santa instead.</p>
<h3>What if someone draws themselves?</h3>
<p>With a paper hat it happens all the time. With SantaDraw it can't: nobody is ever matched with themselves.</p></div>'''),
 dict(path='/secret-santa-with-wishlist', file='secret-santa-with-wishlist.html', nav='Secret Santa with wishlists',
  title='Secret Santa Generator with Wishlists: everyone sees their person\'s gift hints | SantaDraw',
  desc='A Secret Santa draw with wishlists. Add a few gift ideas for each person and whoever draws them sees the hints in their private link. No sign-up.',
  h1='🎁 Secret Santa with wishlists',
  sub='Add 2 or 3 gift ideas for each person. Whoever draws them<br>sees the hints in their private link. No more unwanted mugs.',
  extra='''<div class="card"><h2 style="margin-top:0">How wishlists work</h2>
<ol><li>Ask everyone in your group chat for 2 or 3 gift ideas before you draw.</li>
<li>Type them in the <strong>Wishlists</strong> box, one person per line: <code>Alice: books, dark chocolate</code>.</li>
<li>Draw names. Each person's private link shows who they're buying for <em>and</em> that person's hints.</li></ol>
<p>Nobody sees their own wishlist being matched, and nobody else's link shows your hints. Wishlists are part of SantaDraw Pro (£2.49 one-off), with exclusions, bigger groups and printable cards.</p></div>'''),
 dict(path='/secret-santa-without-email', file='secret-santa-without-email.html', nav='Secret Santa without email addresses',
  title='Secret Santa Without Email Addresses or Sign-Up | SantaDraw',
  desc='Most Secret Santa sites make everyone register with an email. SantaDraw doesn\'t: draw names in your browser and send private links by WhatsApp or text.',
  h1='🔒 Secret Santa without emails',
  sub='No accounts, no email addresses, no spam afterwards.<br>Draw in your browser, send private links however you like.',
  extra='''<div class="card"><h2 style="margin-top:0">Why no emails?</h2>
<p>Many Secret Santa sites ask the organiser to type in everyone's email address, then send invitations, reminders and marketing. Half the family never finds the email, and the other half get spam for years.</p>
<p>SantaDraw works differently. The draw runs in your browser, and each person's match is scrambled inside their own link. You send the links by WhatsApp, text, Messenger, Slack or anything else. Nothing is stored on our servers, so there's nothing to leak and nobody to unsubscribe from.</p>
<p>The trade-off: you, the organiser, send the links. It takes about a minute for a family of 8.</p></div>'''),
 dict(path='/secret-santa-for-friends', file='secret-santa-for-friends.html', nav='Secret Santa for friends',
  title='Secret Santa for Friends: draw names for your friendship group | SantaDraw',
  desc='Organise a Secret Santa for your friends in a minute. Draw names free, send private links in the group chat, add wishlists and a spending limit.',
  h1='🎅 Secret Santa for friends',
  sub='Draw names for your friendship group, uni flat or housemates,<br>and send everyone a private link in a minute.',
  extra='''<div class="card"><h2 style="margin-top:0">Making a friends' Secret Santa work</h2>
<ul><li><strong>Pick a budget everyone's comfortable with.</strong> £10 to £20 is typical; students often go for £5.</li>
<li><strong>Choose the date first</strong>, usually a Christmas dinner or night out, and put it in the draw so it shows on everyone's link.</li>
<li><strong>Couples in the group?</strong> Use exclusions (Pro) so they don't draw each other.</li>
<li><strong>Try a theme:</strong> "secondhand only", "something under £10 that's edible", or "a book that changed your life".</li></ul>
<p>Up to 6 friends is free. Bigger groups, exclusions and wishlists are £2.49 once with Pro.</p></div>'''),
 dict(path='/printable-secret-santa-cards', file='printable-secret-santa-cards.html', nav='Printable Secret Santa cards',
  title='Printable Secret Santa Cards: draw names and print a card for each person | SantaDraw',
  desc='Draw Secret Santa names online and print a card for each person, with their match, spending limit, date and gift hints. Great for families and classrooms.',
  h1='🖨️ Printable Secret Santa cards',
  sub='Draw names here, then print one card per person<br>with their match, the budget, the date and any gift hints.',
  extra='''<div class="card"><h2 style="margin-top:0">When paper is better</h2>
<ul><li><strong>Family gatherings:</strong> hand everyone a folded card at the table.</li>
<li><strong>Grandparents without smartphones.</strong></li>
<li><strong>Classrooms and clubs</strong>, where children don't have phones.</li></ul>
<p>After drawing, press <strong>Print cards</strong>. Each card shows the person's name, who they're buying for, the spending limit, the exchange date and their recipient's wishlist hints. Cut along the dashed lines and fold each card so the match is hidden. Printable cards are part of SantaDraw Pro (£2.49 one-off).</p></div>'''),
 dict(path='/secret-santa-message', file='secret-santa-message.html', nav='Secret Santa invite messages',
  title='Secret Santa Message Templates: invite your group on WhatsApp or at work | SantaDraw',
  desc='Copy-and-paste Secret Santa messages for WhatsApp groups, families and work: the invite, the reminder and the "names are drawn" message. Plus a free draw.',
  h1='💬 Secret Santa message templates',
  sub='Copy, paste, send. Messages for inviting your group, announcing the draw<br>and reminding everyone, plus the draw itself right here.',
  extra='''<div class="card"><h2 style="margin-top:0">1. The invite (family or friends)</h2>
<p><em>"Hi all 🎄 Shall we do Secret Santa this year instead of everyone buying for everyone? One present each, £20 limit, swapped on Christmas Day. Reply 🎅 if you're in by Sunday and I'll draw names!"</em></p>
<h2>2. The invite (work)</h2>
<p><em>"Hi team! We're doing an optional Secret Santa this year 🎁 Limit £10, gifts exchanged at the Christmas lunch on the 18th. Reply here or message me by Friday if you'd like to join. No pressure either way."</em></p>
<h2>3. Names are drawn</h2>
<p><em>"Names are drawn! 🎅 I'm sending each of you a private link now. Tap it to see who you're buying for, and keep it to yourself! Limit £20, swap on Christmas Day."</em></p>
<p>SantaDraw writes this one for you: after the draw, each person's <strong>WhatsApp</strong> button opens a ready-written message with their private link.</p>
<h2>4. The reminder</h2>
<p><em>"One week to go until our Secret Santa swap 🎁 Lost your link? Scroll up to my private message to you, it still works. Remember the £20 limit!"</em></p></div>'''),
 dict(path='/secret-santa-gifts-under-5', file='secret-santa-gifts-under-5.html', nav='Secret Santa gifts under £5',
  title='Secret Santa Gifts Under £5: 20 cheap ideas that don\'t feel cheap | SantaDraw',
  desc='Cheap Secret Santa gift ideas under £5 for work, school and students, plus a free Secret Santa generator with private WhatsApp links. No sign-up.',
  h1='🎁 Secret Santa gifts under £5',
  sub='A £5 limit is perfect for offices, classrooms and students.<br>Ideas below, and a free name draw right here.',
  extra='''<div class="card"><h2 style="margin-top:0">Edible (always a safe bet)</h2>
<ul><li>A bar of really good chocolate</li><li>A jar of hot chocolate stirrers or marshmallows</li><li>Homemade biscuits or fudge in a jam jar</li><li>A mini bottle of hot sauce</li><li>Fancy tea bags or a single-origin coffee sachet set</li></ul>
<h2>Useful</h2>
<ul><li>A good pen or a pack of fun highlighters</li><li>A pocket notebook</li><li>Lip balm or hand cream</li><li>A phone stand or cable tidy</li><li>Novelty Christmas socks</li></ul>
<h2>Fun</h2>
<ul><li>A pack of cards or a mini travel game</li><li>A Christmas cracker joke book</li><li>A tiny succulent in a pot</li><li>A secondhand paperback with a note saying why you picked it</li><li>A bath bomb</li></ul>
<h2>Making £5 look generous</h2>
<p>Presentation does most of the work: brown paper, string and a sprig of greenery. Adding a handwritten note costs nothing. With SantaDraw Pro (£2.49 once, for the organiser) everyone can add wishlist hints, so even a £5 gift hits the mark.</p></div>'''),
 dict(path='/secret-santa-gifts-under-10', file='secret-santa-gifts-under-10.html', nav='Secret Santa gifts under £10',
  title='Secret Santa Gifts Under £10: ideas for work, friends and family | SantaDraw',
  desc='Secret Santa gift ideas under £10 for colleagues, friends and family, plus a free Secret Santa generator with private links and wishlists. No sign-up.',
  h1='🎁 Secret Santa gifts under £10',
  sub='£10 is the most popular Secret Santa limit at work.<br>Here are ideas that people actually use, plus a free name draw.',
  extra='''<div class="card"><h2 style="margin-top:0">For colleagues</h2>
<ul><li>A good insulated travel mug</li><li>A desk plant (snake plants are hard to kill)</li><li>A quality notebook and pen set</li><li>A box of nice biscuits for their desk drawer</li><li>A wireless charging pad (look for good-value brands)</li></ul>
<h2>For friends</h2>
<ul><li>A paperback you loved, with a note inside</li><li>A card game like a party quiz game</li><li>A candle in their favourite scent</li><li>A cocktail or mocktail kit</li><li>A cosy pair of bed socks</li></ul>
<h2>For family</h2>
<ul><li>A jigsaw puzzle</li><li>A photo printed and framed</li><li>Local honey, jam or chutney</li><li>A hot water bottle with a knitted cover</li></ul>
<p><strong>Tip:</strong> the easiest way to avoid a dud present is to ask for hints. With wishlists (SantaDraw Pro, £2.49 once for the organiser), everyone's private link shows their person's ideas.</p></div>'''),
 dict(path='/secret-santa-gifts-under-20', file='secret-santa-gifts-under-20.html', nav='Secret Santa gifts under £20',
  title='Secret Santa Gifts Under £20: thoughtful ideas for him, her and anyone | SantaDraw',
  desc='Thoughtful Secret Santa gift ideas under £20 for family and friends, plus a free Secret Santa generator with exclusions, wishlists and private WhatsApp links.',
  h1='🎁 Secret Santa gifts under £20',
  sub='£20 is the usual limit for family and friends Secret Santa.<br>Ideas for anyone on your list, plus a free name draw.',
  extra='''<div class="card"><h2 style="margin-top:0">Cosy</h2>
<ul><li>A chunky knit blanket or throw</li><li>Slipper socks or proper slippers</li><li>A luxury hot chocolate set with a mug</li><li>A big scented candle</li></ul>
<h2>For people who like doing things</h2>
<ul><li>A 1000-piece jigsaw or a strategy board game</li><li>A cookbook for a cuisine they love</li><li>A beginner's craft kit: embroidery, candle making, watercolours</li><li>A bird feeder with a bag of seed</li></ul>
<h2>Food and drink</h2>
<ul><li>A hamper you build yourself from local shops</li><li>A good olive oil and balsamic set</li><li>A coffee grinder or a bag of specialty beans</li></ul>
<h2>Tech and gadgets</h2>
<ul><li>A portable phone charger</li><li>A smart plug or a sunrise alarm clock (check the price, they vary)</li><li>A small Bluetooth speaker</li></ul>
<p><strong>Families:</strong> use exclusions so couples don't draw each other, and wishlists so nobody guesses blind. Both come with SantaDraw Pro (£2.49 once).</p></div>'''),
 dict(path='/secret-santa-for-large-groups', file='secret-santa-for-large-groups.html', nav='Secret Santa for large groups',
  title='Secret Santa Generator for Large Groups (10, 20, 50+ people) | SantaDraw',
  desc='Draw Secret Santa names for a big family, office or club. Any group size, exclusions, wishlists and a private link for everyone. No sign-up, no emails.',
  h1='🎅 Secret Santa for large groups',
  sub='Big family? Whole office? Sports club? Draw names for any group size<br>and send everyone their own private link.',
  extra='''<div class="card"><h2 style="margin-top:0">Running Secret Santa for 10, 20 or 50 people</h2>
<ul><li><strong>Paste the whole list at once.</strong> Copy names from a spreadsheet or group chat, one per line.</li>
<li><strong>Use exclusions</strong> for couples, people in the same household, or last year's pairs.</li>
<li><strong>Copy all links</strong> after the draw and keep them somewhere private, so you can resend a lost link.</li>
<li><strong>Need paper?</strong> Print a card for each person instead.</li></ul>
<p>Groups up to 6 are free. Larger groups need SantaDraw Pro, a one-off £2.49 for the organiser (not per person), which also unlocks exclusions, wishlists and printable cards. Nobody else pays anything or signs up.</p></div>'''),
 dict(path='/secret-santa-name-picker', file='secret-santa-name-picker.html', nav='Secret Santa name picker',
  title='Secret Santa Name Picker: random, fair, nobody gets themselves | SantaDraw',
  desc='A random Secret Santa name picker. Type the names, press draw, and everyone gets a private link with their match. Nobody draws themselves. Free, no sign-up.',
  h1='🎲 Secret Santa name picker',
  sub='Random and fair: nobody picks themselves, and nobody sees anyone else\'s match.<br>Type names, press draw, send the links.',
  extra='''<div class="card"><h2 style="margin-top:0">How the picker works</h2>
<p>SantaDraw shuffles the names in your browser using your device's secure random number generator, then checks that nobody got themselves and every exclusion is respected. If a rule can't be met, it tells you instead of quietly breaking it.</p>
<p>Each match is then scrambled into its own link. Unlike a "show everyone" name picker, the organiser doesn't have to see the results: just send each link to its owner and you can take part too.</p>
<h3>Why not a hat?</h3>
<ul><li>No-one draws their own name and has to redraw (giving the game away).</li>
<li>Works for people who aren't in the room.</li>
<li>Couples can be kept apart with exclusions.</li></ul></div>'''),
 dict(path='/secret-santa-for-housemates', file='secret-santa-for-housemates.html', nav='Secret Santa for housemates and uni',
  title='Secret Santa for Housemates, Uni Flats and Societies | SantaDraw',
  desc='Draw Secret Santa names for your house, uni flat or society in a minute. Free for up to 6, private links in the group chat, a £5 or £10 limit.',
  h1='🏠 Secret Santa for housemates',
  sub='Uni flat, shared house or society social? Draw names in a minute<br>and drop everyone their private link in the group chat.',
  extra='''<div class="card"><h2 style="margin-top:0">Housemate Secret Santa ideas</h2>
<ul><li><strong>Keep the limit low:</strong> £5 or £10 works for most students.</li>
<li><strong>Do it before everyone goes home</strong> for the holidays, at a flat dinner or the last night out of term.</li>
<li><strong>Themes that work:</strong> "something for the house", "charity shop finds only", "the worst gift under £5".</li>
<li><strong>Society socials:</strong> paste the whole member list in, and use exclusions for couples.</li></ul>
<p>Up to 6 people is free. Bigger groups need SantaDraw Pro, £2.49 once, which one person pays, so it's about 30p each in a flat of 8.</p></div>'''),
 dict(path='/secret-santa-for-teachers', file='secret-santa-for-teachers.html', nav='Staff room Secret Santa',
  title='Staff Room Secret Santa: draw names for teachers and school staff | SantaDraw',
  desc='Organise a staff room Secret Santa for teachers and school staff. Draw names, print cards for the pigeonholes or send private links. No sign-up.',
  h1='🍎 Staff room Secret Santa',
  sub='For teachers, TAs and support staff. Draw names, then print cards<br>for the pigeonholes or send private links.',
  extra='''<div class="card"><h2 style="margin-top:0">Tips for a school staff Secret Santa</h2>
<ul><li><strong>Make it opt-in</strong> with a sign-up sheet in the staff room.</li>
<li><strong>Keep the limit modest</strong>, £5 or £10, so everyone can join.</li>
<li><strong>Printable cards</strong> (Pro): print one per person and pop them in pigeonholes. Each card shows their match, the limit, the date and gift hints.</li>
<li><strong>Swap on the last day of term</strong>, at the staff lunch or in the staff room.</li></ul>
<p>Running it for a class of children instead? See <a href="/secret-santa-for-kids">Secret Santa for kids and classes</a>.</p></div>'''),
 dict(path='/funny-secret-santa-gifts', file='funny-secret-santa-gifts.html', nav='Funny Secret Santa gifts',
  title='Funny Secret Santa Gifts: ideas that get a laugh (and still get used) | SantaDraw',
  desc='Funny Secret Santa gift ideas for work and friends that get a laugh without being awkward, plus a free Secret Santa generator. No sign-up.',
  h1='😂 Funny Secret Santa gifts',
  sub='The best funny gifts get a laugh when they\'re opened and still get used in January.<br>Ideas below, and a free name draw right here.',
  extra='''<div class="card"><h2 style="margin-top:0">Funny and actually useful</h2>
<ul><li>A mug with an in-joke from the team or group chat</li><li>A "desk survival kit": a stress ball, emergency biscuits and a tiny violin</li><li>A pizza-shaped blanket</li><li>Socks printed with their pet's face</li><li>A "world's okayest colleague" award</li><li>A rubber duck for their desk (developers will understand)</li></ul>
<h2>Keep it kind</h2>
<ul><li>Joke about situations, never about someone's looks, age or weight.</li><li>At work, if you wouldn't open it in front of your manager, don't buy it.</li><li>If in doubt, pair a silly gift with a small proper one, like good chocolate.</li></ul>
<p>Running a "funny gifts only" theme? Put it in the draw details so it shows on everyone's private link.</p></div>'''),
 dict(path='/secret-santa-gifts-for-colleagues', file='secret-santa-gifts-for-colleagues.html', nav='Secret Santa gifts for colleagues',
  title='Secret Santa Gifts for Colleagues: safe, thoughtful work gift ideas | SantaDraw',
  desc='Secret Santa gift ideas for colleagues you don\'t know well, at £5, £10 and £20. Plus a free office Secret Santa generator with private links.',
  h1='💼 Secret Santa gifts for colleagues',
  sub='Drew someone from another department? These are safe bets for almost anyone,<br>plus a free office Secret Santa draw.',
  extra='''<div class="card"><h2 style="margin-top:0">When you don't know them well</h2>
<ul><li>Good chocolate or biscuits (check for allergies or veganism by asking around)</li><li>A desk plant that's hard to kill</li><li>A quality notebook and pen</li><li>A reusable coffee cup</li><li>A hand cream and lip balm set</li></ul>
<h2>When you know a little about them</h2>
<ul><li>Runner or cyclist: a phone armband or a bike light</li><li>Tea or coffee lover: a specialty selection</li><li>Reader: a paperback in their favourite genre</li><li>Gamer: a small desk toy or a mouse mat with their favourite game</li></ul>
<h2>The easy way</h2>
<p>Let people add gift hints when the organiser draws names. With SantaDraw Pro (£2.49 once, for the organiser), each private link shows the hints for the colleague you drew. See also: <a href="/office-secret-santa">running an office Secret Santa</a>.</p></div>'''),
 dict(path='/secret-santa-gifts-for-him', file='secret-santa-gifts-for-him.html', nav='Secret Santa gifts for him',
  title='Secret Santa Gifts for Him: ideas under £10 and £20 | SantaDraw',
  desc='Secret Santa gift ideas for him, for dads, brothers, friends and colleagues, under £10 and £20. Plus a free Secret Santa generator with wishlists.',
  h1='🎁 Secret Santa gifts for him',
  sub='Ideas for a dad, brother, friend or colleague, at £10 and £20.<br>Plus a free name draw with wishlists.',
  extra='''<div class="card"><h2 style="margin-top:0">Under £10</h2>
<ul><li>A hot sauce trio</li><li>Good socks (people always use them)</li><li>A multi-tool keyring</li><li>A craft beer or alcohol-free beer selection</li><li>A paperback by an author he likes</li></ul>
<h2>Under £20</h2>
<ul><li>A beard or shaving kit</li><li>A good insulated flask</li><li>A board game or a big jigsaw</li><li>A barbecue rub set</li><li>A portable phone charger</li></ul>
<p>Not sure what he's into? Wishlists (SantaDraw Pro) let everyone add 2 or 3 hints before the draw.</p></div>'''),
 dict(path='/secret-santa-gifts-for-her', file='secret-santa-gifts-for-her.html', nav='Secret Santa gifts for her',
  title='Secret Santa Gifts for Her: ideas under £10 and £20 | SantaDraw',
  desc='Secret Santa gift ideas for her, for mums, sisters, friends and colleagues, under £10 and £20. Plus a free Secret Santa generator with wishlists.',
  h1='🎁 Secret Santa gifts for her',
  sub='Ideas for a mum, sister, friend or colleague, at £10 and £20.<br>Plus a free name draw with wishlists.',
  extra='''<div class="card"><h2 style="margin-top:0">Under £10</h2>
<ul><li>A scented candle</li><li>A pretty notebook and pen</li><li>Posh hot chocolate</li><li>A silk scrunchie set</li><li>A paperback by an author she likes</li></ul>
<h2>Under £20</h2>
<ul><li>A cosy throw or bed socks</li><li>A houseplant in a nice pot</li><li>A cookbook or a baking kit</li><li>A beginner's embroidery or watercolour kit</li><li>A photo printed and framed</li></ul>
<p>Not sure what she's into? Wishlists (SantaDraw Pro) let everyone add 2 or 3 hints before the draw.</p></div>'''),
 dict(path='/kris-kindle-generator', file='kris-kindle-generator.html', nav='Kris Kindle generator',
  title='Kris Kindle Generator: draw names online, no sign-up | SantaDraw',
  desc='Free Kris Kindle name generator for family, friends and work. Draw names in 30 seconds and send everyone a private link by WhatsApp or text. No emails needed.',
  h1='🎄 Kris Kindle generator',
  sub='Doing Kris Kindle this year? Draw names here in 30 seconds,<br>then send each person a private link by WhatsApp or text.',
  extra='''<div class="card"><h2 style="margin-top:0">Kris Kindle, Secret Santa: same thing</h2>
<p>In Ireland it's usually called <strong>Kris Kindle</strong> (from the German <em>Christkindl</em>); in the UK it's Secret Santa. Either way, everyone's name goes in the hat, everyone draws one person, and nobody knows who's buying for whom until the day.</p>
<ul><li><strong>Type everyone's names</strong> above, set the budget (€10 or €20 is common) and the date.</li>
<li><strong>Press Draw names.</strong> Each person gets their own private link that shows only their match.</li>
<li><strong>Send the links</strong> one by one on WhatsApp, so nobody can peek.</li></ul>
<p>Free for up to 6 people. For bigger families or offices, couples exclusions and wishlists, SantaDraw Pro is a one-off £2.49 (about €3).</p></div>'''),
 dict(path='/secret-santa-app', file='secret-santa-app.html', nav='Secret Santa without an app',
  title='Secret Santa App? You don\'t need one: draw names in your browser | SantaDraw',
  desc='Looking for a Secret Santa app? SantaDraw works in any phone browser with nothing to install and no accounts. Draw names and send private links by WhatsApp.',
  h1='📱 Secret Santa, no app needed',
  sub='Nothing to download, nobody to sign up. SantaDraw works in any phone browser:<br>draw names and send everyone a private link.',
  extra='''<div class="card"><h2 style="margin-top:0">Why skip the app?</h2>
<ul><li><strong>Gran doesn't have to install anything.</strong> Everyone just taps a link.</li>
<li><strong>No accounts or email addresses.</strong> The draw happens on your phone, and each result is scrambled inside that person's link. Nothing is stored on a server.</li>
<li><strong>Works on iPhone, Android, tablets and laptops.</strong> Tip: on your phone, use "Add to Home Screen" to keep it handy.</li></ul>
<p>Free for up to 6 people. SantaDraw Pro (£2.49 once) adds bigger groups, exclusions, wishlists and printable cards.</p></div>'''),
 dict(path='/secret-santa-for-couples', file='secret-santa-for-couples.html', nav='Secret Santa for couples',
  title='Secret Santa with Couples: make sure partners don\'t draw each other | SantaDraw',
  desc='Running Secret Santa with couples in the group? Stop partners drawing each other with exclusions, or draw couples as pairs. Free name draw, private links.',
  h1='💑 Secret Santa with couples',
  sub='Partners already buy for each other. Add them as exclusions<br>and SantaDraw makes sure they never match.',
  extra='''<div class="card"><h2 style="margin-top:0">Two ways to handle couples</h2>
<ol><li><strong>Exclude partners (most popular).</strong> Everyone is drawn as an individual, but each couple is listed in the Exclusions box (<code>Sam, Alex</code>) so they never get each other. This needs SantaDraw Pro (£2.49 once).</li>
<li><strong>Draw couples as one name.</strong> Enter "Sam &amp; Alex" as a single name. Each couple buys one gift for another couple. Fewer, nicer presents, and it's free for up to 6 names.</li></ol>
<p>Lots of exclusions in a small group can make a fair draw impossible; SantaDraw tells you if so, rather than breaking a rule.</p>
<p>See also: <a href="/secret-santa-with-exclusions">Secret Santa with exclusions</a> and <a href="/family-secret-santa">family Secret Santa</a>.</p></div>'''),
 dict(path='/secret-santa-gifts-for-teenagers', file='secret-santa-gifts-for-teenagers.html', nav='Secret Santa gifts for teenagers',
  title='Secret Santa Gifts for Teenagers: ideas they\'ll actually like | SantaDraw',
  desc='Secret Santa gift ideas for teenagers under £10 and £20, for family Secret Santas where the teens are in the draw too. Plus a free name generator.',
  h1='🎧 Secret Santa gifts for teenagers',
  sub='Drew your teenage nephew or cousin in the family Secret Santa?<br>Ideas that won\'t get an eye-roll, plus a free name draw.',
  extra='''<div class="card"><h2 style="margin-top:0">Under £10</h2>
<ul><li>Fun phone grip or case</li><li>A big bag of their favourite sweets</li><li>LED strip lights for their room</li><li>A gaming gift card (check which console)</li><li>A mini desk fan or hand warmer</li></ul>
<h2>Under £20</h2>
<ul><li>Wireless earbuds (budget brands are fine)</li><li>A hoodie from a brand they like</li><li>A cinema voucher for two</li><li>A board game they can play with friends</li><li>A Polaroid-style film pack</li></ul>
<p>The safest bet is asking: with wishlists (SantaDraw Pro), everyone adds 2 or 3 hints and their Santa sees them on their private link.</p></div>'''),
 dict(path='/christmas-name-draw', file='christmas-name-draw.html', nav='Christmas name draw',
  title='Christmas Name Draw Online: free, fair and private | SantaDraw',
  desc='Do your Christmas name draw online. Type everyone in, press draw, and send each person a private link. Nobody draws themselves, nobody sees the others. Free.',
  h1='🎄 Christmas name draw',
  sub='Like names from a hat, but nobody draws themselves and nobody needs to be in the same room.<br>Free, and done in 30 seconds.',
  extra='''<div class="card"><h2 style="margin-top:0">Why draw names online?</h2>
<ul><li><strong>Nobody gets themselves</strong>, so no redraws.</li>
<li><strong>Works when the family is spread out.</strong> Send each private link by WhatsApp or text.</li>
<li><strong>The organiser can play too.</strong> You only see the links, not who got whom.</li>
<li><strong>Rules built in (Pro):</strong> couples can't draw each other, and wishlists travel with each link.</li></ul></div>'''),

 dict(path='/secret-santa-group-chat', file='secret-santa-group-chat.html', nav='Secret Santa in a group chat (one link)',
  title='Secret Santa in a Group Chat: one link, everyone picks their name | SantaDraw',
  desc='Run Secret Santa with one link in your WhatsApp, Messenger or Teams group chat. Everyone taps it, picks their own name and sees only their match. Free, no sign-up.',
  h1='🎅 Secret Santa with one group-chat link',
  sub='Draw names, post a single link in the group chat, and let everyone tap their own name.<br>No app, no sign-up, no email addresses.',
  extra='''<div class="card"><h2 style="margin-top:0">How the group link works</h2>
<ol><li>Type everyone's names above and press <strong>Draw names</strong>.</li>
<li>Tap <strong>Send to WhatsApp group</strong> (or <strong>Copy group link</strong> for Messenger, Teams, Slack or iMessage) and post it in your group chat.</li>
<li>Each person taps the link, chooses their own name and taps the present to see who they're buying for.</li>
<li>Their phone is then locked to that name, so tapping the link again shows the same match, and nobody can pick a second name on that phone.</li></ol>
<h3>Is it private?</h3>
<p>The draw happens in your browser and the results are scrambled inside the link, so nothing is stored on our servers. The group link works on trust, like pulling names from a hat: someone determined to peek could use a second phone. If your group needs it strictly secret, use the individual private links instead; SantaDraw gives you both after every draw.</p>
<h3>Bigger groups and couples</h3>
<p>Free for up to 6 people. SantaDraw Pro (a one-off £2.49) adds any group size, exclusions so couples don't draw each other, wishlists and printable cards.</p></div>'''),

 dict(path='/secret-santa-questionnaire', file='secret-santa-questionnaire.html', nav='Secret Santa questionnaire',
  title='Secret Santa Questionnaire: free form and questions to copy | SantaDraw',
  desc='A free Secret Santa questionnaire for work, family or friends: favourite snacks, hobbies, things to avoid, allergies. Fill it in on your phone and copy the answers.',
  h1='📝 Secret Santa questionnaire',
  sub='Help your Secret Santa get it right. Fill in the questionnaire below and copy the answers,<br>or draw names for your group first. Free, no sign-up.',
  extra=EXTRA_Q),
 dict(path='/secret-santa-themes', file='secret-santa-themes.html', nav='Secret Santa themes',
  title='Secret Santa Themes: 20 fun ideas for work, family and friends | SantaDraw',
  desc='Fun Secret Santa theme ideas: something you eat, something you read, handmade, charity shop finds, a colour theme and more. Plus a free name draw with private links.',
  h1='🎨 Secret Santa themes',
  sub='A theme makes shopping easier and opening presents funnier.<br>Pick one below, then draw names in 30 seconds.',
  extra='''<div class="card"><h2 style="margin-top:0">Easy themes</h2>
<ul><li><strong>Something to eat or drink</strong>: everyone likes a treat, and it never clutters a shelf.</li>
<li><strong>Something to read</strong>: a book you loved, with a note saying why.</li>
<li><strong>Cosy night in</strong>: socks, hot chocolate, a candle, a film.</li>
<li><strong>Stocking fillers only</strong>: three small things under the limit.</li>
<li><strong>Local</strong>: something from a shop or maker in your town.</li></ul>
<h2>Funny themes (great for the office)</h2>
<ul><li><strong>Charity shop challenge</strong>: £5, second-hand only. Money goes to a good cause and the gifts are always a story.</li>
<li><strong>Starts with their initial</strong>: drew Jess? Jelly beans, jigsaw, jam.</li>
<li><strong>One colour</strong>: everything in the gift must be one colour (the recipient's favourite, if you know it).</li>
<li><strong>As seen on TV</strong>: the strangest gadget you can find under the limit.</li>
<li><strong>Re-gift</strong>: wrap something you already own and never use.</li></ul>
<h2>Thoughtful themes (great for families)</h2>
<ul><li><strong>Handmade</strong>: bake, knit, draw or print something.</li>
<li><strong>Experience</strong>: a voucher for a walk, a meal you'll cook, a cinema trip.</li>
<li><strong>Memory</strong>: a printed photo, a playlist, a letter.</li>
<li><strong>Self-care</strong>: whatever helps them relax.</li>
<li><strong>Last year's wish</strong>: something they mentioned wanting this year.</li></ul>
<p>Tell everyone the theme with the draw: type it into the <strong>Group name</strong> box above (e.g. "Office Secret Santa: charity shop challenge") and it shows on every private link. Unsure what people like? Send round our <a href="/secret-santa-questionnaire">Secret Santa questionnaire</a>.</p></div>'''),

 dict(path='/secret-santa-poems', file='secret-santa-poems.html', nav='Secret Santa poems',
  title='Secret Santa Poems: short rhymes for gift tags and cards | SantaDraw',
  desc='Short Secret Santa poems and rhymes to write on a gift tag or card: funny, sweet and office-safe. Copy one, then draw names free with private links.',
  h1='✍️ Secret Santa poems',
  sub='A little rhyme on the tag makes a small present feel special.<br>Copy one below, or draw names for your group first.',
  extra='''<div class="card"><h2 style="margin-top:0">Short and sweet</h2>
<p>Roses are red,<br>the tinsel is gold,<br>who picked this present<br>will never be told.</p>
<p>From somebody near<br>and somebody dear,<br>your Secret Santa<br>wishes you cheer.</p>
<p>I drew your name<br>and gave it some thought;<br>I hope that you love<br>the present I bought.</p>
<h2>Funny ones</h2>
<p>I stuck to the budget,<br>I didn't go wild,<br>if you don't like it,<br>re-gift it with a smile.</p>
<p>You'll never guess<br>who wrapped this for you,<br>(the sticky tape mess<br>might give you a clue).</p>
<p>Merry Christmas from me,<br>whoever that be:<br>a mystery elf<br>on a tight salary.</p>
<h2>For the office</h2>
<p>For all the coffee runs<br>and the meetings that drag,<br>here's something festive<br>in a Secret Santa bag.</p>
<p>To my favourite colleague<br>(well, the one that I drew):<br>have a lovely Christmas,<br>this one's just for you.</p>
<h2>Tips</h2>
<ul><li>Write in capitals or get someone else to write the tag, so your handwriting doesn't give you away.</li>
<li>Add a <a href="/secret-santa-clues">clue about who you are</a> if your group likes guessing games.</li>
<li>More words for the invite and the reveal: <a href="/secret-santa-message">Secret Santa messages</a>.</li></ul></div>'''),
 dict(path='/secret-santa-clues', file='secret-santa-clues.html', nav='Secret Santa clues',
  title='Secret Santa Clues: fun hints to help them guess who you are | SantaDraw',
  desc='Fun Secret Santa clue ideas for the guessing game: riddles, emoji clues, "two truths and a lie" and treasure hunts. Plus a free name draw with private links.',
  h1='🕵️ Secret Santa clues',
  sub='Make the reveal a game: leave a clue with your present<br>and let them guess who their Secret Santa was.',
  extra='''<div class="card"><h2 style="margin-top:0">Clue ideas</h2>
<ul><li><strong>Three-word clue:</strong> three words that describe you, like "tall, tea, Leeds".</li>
<li><strong>Emoji clue:</strong> 3 to 5 emojis about your hobbies or job, e.g. 🚲☕🐶.</li>
<li><strong>Two truths and a lie</strong> about yourself, written on the tag.</li>
<li><strong>A riddle:</strong> "I sit near the window and never take the last biscuit."</li>
<li><strong>A first-letter hint:</strong> the first letter of your name hidden in the wrapping paper pattern.</li>
<li><strong>A daily clue:</strong> at work, leave one small clue a day in the week before the exchange.</li>
<li><strong>A treasure hunt:</strong> hide the present and leave the first clue on their desk or under the tree.</li></ul>
<h2>Guessing game rules</h2>
<ol><li>Open presents one at a time.</li>
<li>Each person gets one guess for their Santa. Right guess: the Santa owns up.</li>
<li>Wrong guesses are revealed at the end.</li></ol>
<p>The draw keeps it secret until then: each person's private link shows only who <em>they</em> are buying for, so even the organiser can play. Want a rhyme with your clue? See <a href="/secret-santa-poems">Secret Santa poems</a>.</p></div>'''),
 dict(path='/secret-santa-gifts-under-15', file='secret-santa-gifts-under-15.html', nav='Secret Santa gifts under £15',
  title='Secret Santa Gifts Under £15: ideas for work, family and friends | SantaDraw',
  desc='Secret Santa gift ideas under £15 that don\'t feel cheap: treats, cosy things, desk gifts and games. Plus a free Secret Santa name draw with private links.',
  h1='🎁 Secret Santa gifts under £15',
  sub='£15 is the sweet spot: enough for something nice, not enough to stress.<br>Ideas below, plus a free name draw.',
  extra='''<div class="card"><h2 style="margin-top:0">Treats</h2>
<ul><li>A posh hot chocolate set or selection of teas</li><li>Fancy crisps and a craft soda</li><li>A box of local fudge or brownies</li><li>Hot sauce trio for the spice lover</li></ul>
<h2>Cosy</h2>
<ul><li>Thick bed socks plus a chocolate bar</li><li>A scented candle (check they like candles first)</li><li>A hot water bottle with a knitted cover</li></ul>
<h2>Desk and everyday</h2>
<ul><li>A good notebook and a nice pen</li><li>A reusable coffee cup</li><li>A mini desk plant</li><li>A phone stand or cable organiser</li></ul>
<h2>Fun</h2>
<ul><li>A card game like a party quiz</li><li>A 500-piece jigsaw</li><li>A paperback by an author they mention</li></ul>
<p>Not sure what they'd like? Send round the <a href="/secret-santa-questionnaire">Secret Santa questionnaire</a>, or turn on wishlists (Pro) so each person's hints travel with their private link. More budgets: <a href="/secret-santa-gifts-under-10">under £10</a> · <a href="/secret-santa-gifts-under-20">under £20</a>.</p></div>'''),
 dict(path='/secret-santa-gifts-for-mum', file='secret-santa-gifts-for-mum.html', nav='Secret Santa gifts for mum',
  title='Secret Santa Gifts for Mum: ideas under £10, £20 and £30 | SantaDraw',
  desc='Drew your mum (or mother-in-law) in the family Secret Santa? Thoughtful gift ideas at every budget, plus a free name draw with private links for the family.',
  h1='💐 Secret Santa gifts for mum',
  sub='Drew your mum, mother-in-law or gran in the family Secret Santa?<br>Ideas for every budget, plus a free family name draw.',
  extra='''<div class="card"><h2 style="margin-top:0">Under £10</h2>
<ul><li>A printed photo of the family in a simple frame</li><li>Her favourite chocolates and a handwritten card</li><li>A nice hand cream</li><li>Seeds or bulbs for the garden</li></ul>
<h2>Under £20</h2>
<ul><li>A photo calendar for next year</li><li>A cosy throw or slipper socks</li><li>A cookbook from a chef she likes</li><li>A plant for the kitchen windowsill</li></ul>
<h2>Under £30</h2>
<ul><li>Afternoon tea voucher (for her and a friend)</li><li>A personalised mug or chopping board</li><li>A good quality scarf</li><li>A book and a box of her favourite tea</li></ul>
<p>The best family Secret Santas stop couples drawing each other and share wishlists, so mum gets something she asked for. Both come with SantaDraw Pro (a one-off £2.49). See also <a href="/family-secret-santa">family Secret Santa</a> and <a href="/secret-santa-gifts-for-dad">gifts for dad</a>.</p></div>'''),
 dict(path='/secret-santa-gifts-for-dad', file='secret-santa-gifts-for-dad.html', nav='Secret Santa gifts for dad',
  title='Secret Santa Gifts for Dad: ideas under £10, £20 and £30 | SantaDraw',
  desc='Drew your dad (or father-in-law) in the family Secret Santa? Gift ideas he\'ll actually use, at every budget, plus a free name draw with private links.',
  h1='🧦 Secret Santa gifts for dad',
  sub='Drew your dad, father-in-law or grandad in the family Secret Santa?<br>Ideas beyond socks, plus a free family name draw.',
  extra='''<div class="card"><h2 style="margin-top:0">Under £10</h2>
<ul><li>A bag of good coffee or a craft beer from a local brewery</li><li>A multi-tool keyring</li><li>His favourite sweets from when he was young</li><li>Funny socks (go on, it's tradition)</li></ul>
<h2>Under £20</h2>
<ul><li>A head torch for the shed or dog walks</li><li>A puzzle book or a 1000-piece jigsaw</li><li>BBQ rub and sauce set</li><li>A book about his team, hobby or hometown</li></ul>
<h2>Under £30</h2>
<ul><li>A warm beanie and gloves</li><li>A small whisky or gin tasting set</li><li>A football, rugby or cricket ticket voucher towards a match</li><li>A smart plug or phone tripod (and set it up for him)</li></ul>
<p>Use wishlists (SantaDraw Pro, £2.49 one-off) so dad can write "not socks" and his Santa sees it on their private link. See also <a href="/family-secret-santa">family Secret Santa</a> and <a href="/secret-santa-gifts-for-mum">gifts for mum</a>.</p></div>'''),

 dict(path='/secret-santa-gifts-under-25', file='secret-santa-gifts-under-25.html', nav='Secret Santa gifts under £25',
  title='Secret Santa Gifts Under £25: ideas for family and friends | SantaDraw',
  desc='Secret Santa gift ideas under £25 for family and friends Secret Santas: cosy, tasty, useful and fun. Plus a free name draw with private WhatsApp links.',
  h1='🎁 Secret Santa gifts under £25',
  sub='£25 is the classic family Secret Santa limit.<br>Ideas that feel generous, plus a free name draw.',
  extra='<div class="card"><h2 style="margin-top:0">Cosy and treat-yourself</h2>\n<ul><li>A soft fleece throw</li><li>A luxury hot chocolate hamper</li><li>Sheepskin-style slippers</li><li>A bath and body set (only if they like smellies)</li></ul>\n<h2>Food and drink</h2>\n<ul><li>A cheese-making or cocktail kit</li><li>A selection box of local craft beer or alcohol-free drinks</li><li>A good bottle of olive oil and balsamic</li></ul>\n<h2>Fun and useful</h2>\n<ul><li>A board game for the whole family</li><li>A portable phone charger</li><li>A smart reusable water bottle</li><li>A cookbook or hardback novel</li></ul>\n<p>Unsure what they like? Send round the <a href="/secret-santa-questionnaire">questionnaire</a>, or turn on wishlists (Pro) so hints travel with each private link. More budgets: <a href="/secret-santa-gifts-under-15">under £15</a> · <a href="/secret-santa-gifts-under-20">under £20</a> · <a href="/secret-santa-gifts-under-30">under £30</a>.</p></div>'),
 dict(path='/secret-santa-gifts-under-30', file='secret-santa-gifts-under-30.html', nav='Secret Santa gifts under £30',
  title='Secret Santa Gifts Under £30: thoughtful ideas for grown-ups | SantaDraw',
  desc='Secret Santa gift ideas under £30 for adult family Secret Santas: experiences, kitchen gifts, cosy things and hobbies. Plus a free name draw with private links.',
  h1='🎁 Secret Santa gifts under £30',
  sub='One good present instead of lots of small ones.<br>Ideas under £30, plus a free name draw for the family.',
  extra='<div class="card"><h2 style="margin-top:0">Experiences</h2>\n<ul><li>Cinema tickets for two with snacks</li><li>A voucher for a local café or bakery</li><li>A pottery-painting or climbing taster session</li></ul>\n<h2>Home and kitchen</h2>\n<ul><li>A cast-iron pan or a good chef\'s knife</li><li>A pasta maker or bread kit</li><li>A large houseplant</li></ul>\n<h2>Hobbies</h2>\n<ul><li>A gardening tool set</li><li>Watercolour set and sketchbook</li><li>A running belt and head torch</li><li>A 1000-piece jigsaw and a puzzle mat</li></ul>\n<p>Families on a £30 limit usually stop couples drawing each other and share wishlists: both come with SantaDraw Pro (a one-off £2.49). More budgets: <a href="/secret-santa-gifts-under-25">under £25</a> · <a href="/secret-santa-gifts-under-20">under £20</a>.</p></div>'),
 dict(path='/secret-santa-gifts-for-boss', file='secret-santa-gifts-for-boss.html', nav='Secret Santa gifts for your boss',
  title='Secret Santa Gifts for Your Boss: safe, thoughtful ideas | SantaDraw',
  desc="Drew your boss or manager in the office Secret Santa? Safe, thoughtful gift ideas under £10 and £20 that won't be awkward. Plus a free office name draw.",
  h1='💼 Secret Santa gifts for your boss',
  sub='Drew your manager in the office Secret Santa?<br>Ideas that are friendly, not awkward, plus a free team name draw.',
  extra='<div class="card"><h2 style="margin-top:0">Safe bets</h2>\n<ul><li>Good coffee or a tea selection for the office</li><li>A smart notebook and pen</li><li>A desk plant that\'s hard to kill</li><li>Nice chocolates to share with the team (bosses often share!)</li></ul>\n<h2>A bit more personal</h2>\n<ul><li>Something for their known hobby: running socks, a golf ball set, a cookbook</li><li>A book from an author they\'ve mentioned</li><li>A mug from their football team</li></ul>\n<h2>Avoid</h2>\n<ul><li>Jokes about their job or management style</li><li>Anything too personal (clothes, perfume)</li><li>Going over the agreed limit, which can look like sucking up</li></ul>\n<p>Run your team draw above: no colleague needs an account, and everyone gets a private link on Slack, Teams or email. See also <a href="/office-secret-santa">office Secret Santa</a> and <a href="/secret-santa-gifts-for-colleagues">gifts for colleagues</a>.</p></div>'),
 dict(path='/secret-santa-wishlist-template', file='secret-santa-wishlist-template.html', nav='Secret Santa wishlist template',
  title='Secret Santa Wishlist Template: what to write, with examples | SantaDraw',
  desc='A simple Secret Santa wishlist template with examples: three ideas, sizes, likes and things to avoid. Copy it into your group chat, or share wishlists with the draw.',
  h1='📋 Secret Santa wishlist template',
  sub='Help your Secret Santa with a short wishlist.<br>Copy the template below, or add wishlists straight into the draw.',
  extra='<div class="card"><h2 style="margin-top:0">Copy this template</h2>\n<pre style="white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:8px">🎅 My Secret Santa wishlist\nName:\n3 things I\'d love:\n1.\n2.\n3.\nI like: (colours, snacks, hobbies)\nPlease no: (things I don\'t want)\nAllergies:\nSizes (if needed):</pre>\n<h2>Example</h2>\n<pre style="white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:8px">Name: Sam\n3 things I\'d love: a crime novel, salted caramel anything, warm gloves\nI like: green, walking, board games\nPlease no: mugs, candles\nAllergies: none\nSizes: gloves M</pre>\n<h2>Tips</h2>\n<ul><li>Give 3 ideas at different prices so your Santa can choose within the limit.</li>\n<li>"Please no" is the most useful line: it saves a lot of unwanted mugs.</li>\n<li>Want more detail? Use the full <a href="/secret-santa-questionnaire">Secret Santa questionnaire</a>.</li></ul>\n<p><strong>Skip the copying:</strong> with SantaDraw Pro (a one-off £2.49), type each person\'s wishlist into the draw and their Secret Santa sees it on their private link. See <a href="/secret-santa-with-wishlist">Secret Santa with wishlists</a>.</p></div>'),


 dict(path='/secret-santa-gifts-for-grandparents', file='secret-santa-gifts-for-grandparents.html', nav='Secret Santa gifts for grandparents',
  title='Secret Santa Gifts for Grandparents: ideas under £10 and £20 | SantaDraw',
  desc='Drew Grandma or Grandad in the family Secret Santa? Thoughtful gift ideas for grandparents under £10 and £20, plus a free family name draw with private WhatsApp links.',
  h1='👵 Secret Santa gifts for grandparents',
  sub='Drew Nan, Grandma or Grandad in the family Secret Santa?<br>Ideas they will actually use, plus a free family name draw.',
  extra='''<div class="card"><h2 style="margin-top:0">Under £10</h2>
<ul><li>A photo printed and framed from a recent family day</li><li>Posh tea, hot chocolate or their favourite biscuits</li><li>A large-print puzzle book or crossword collection</li><li>Bird food and a simple feeder for the garden</li><li>Cosy bed socks or a hot water bottle cover</li></ul>
<h2>Under £20</h2>
<ul><li>A small photo book of the year (many sites have offers in November)</li><li>A bulb kit or herb planter for the windowsill</li><li>A jigsaw made from a family photo</li><li>A "letters from the grandkids" jar: notes or drawings from every child</li></ul>
<h2>Making it easy for older relatives</h2>
<p>Many grandparents don't want another app or an account. With SantaDraw everyone just taps a link in WhatsApp or a text to see who they're buying for. No downloads, no passwords, no email addresses. If they're not on WhatsApp, read their result out on a call: the link still only shows one name.</p></div>'''),
 dict(path='/secret-santa-gifts-for-kids', file='secret-santa-gifts-for-kids.html', nav='Secret Santa gifts for kids',
  title='Secret Santa Gifts for Kids by Age: ideas under £10 | SantaDraw',
  desc='Secret Santa gift ideas for children by age (3 to 5, 6 to 8, 9 to 12) under £10 and £15, plus a free family name draw that keeps siblings apart.',
  h1='🧸 Secret Santa gifts for kids',
  sub='Ideas by age for the family or class Secret Santa,<br>plus a free name draw with private links for each child.',
  extra='''<div class="card"><h2 style="margin-top:0">Ages 3 to 5</h2>
<ul><li>Chunky crayons and a big colouring pad</li><li>Bath toys or bath crayons</li><li>A picture book with flaps or sounds</li><li>Play dough set with cutters</li></ul>
<h2>Ages 6 to 8</h2>
<ul><li>Make-your-own slime or crystal-growing kit</li><li>A joke book</li><li>Pocket card games (Uno, Dobble)</li><li>Torch or glow-in-the-dark stars</li></ul>
<h2>Ages 9 to 12</h2>
<ul><li>A sketchbook with fineliners</li><li>Mini Lego or building set</li><li>Puzzle cube or brain teasers</li><li>A book from a series they're reading (ask the parents which one)</li></ul>
<h2>Kids in the family draw</h2>
<p>Many families run a separate kids' draw so children buy for each other, with a parent helping. Use <a href="/secret-santa-with-exclusions">exclusions</a> so siblings don't draw each other, and the wishlist box so each child can add an idea. See also <a href="/secret-santa-for-kids">Secret Santa for kids</a>.</p></div>'''),
 dict(path='/eco-friendly-secret-santa-gifts', file='eco-friendly-secret-santa-gifts.html', nav='Eco-friendly Secret Santa gifts',
  title='Eco-Friendly Secret Santa Gifts: sustainable ideas under £10 | SantaDraw',
  desc='Sustainable Secret Santa gift ideas under £10 and £20: reusable, plastic-free, second-hand and experience gifts. Plus a paper-free name draw with private links.',
  h1='🌱 Eco-friendly Secret Santa gifts',
  sub='Sustainable, low-waste gift ideas for any budget,<br>and a paper-free name draw: no slips of paper, no emails.',
  extra='''<div class="card"><h2 style="margin-top:0">Under £10</h2>
<ul><li>Beeswax food wraps</li><li>A solid shampoo or soap bar</li><li>Seed paper or a pack of wildflower seeds</li><li>A bamboo or metal straw set</li><li>A second-hand book you loved, with a note inside</li></ul>
<h2>Under £20</h2>
<ul><li>A good reusable coffee cup or water bottle</li><li>A refill kit from a local refill shop</li><li>A potted herb or a small house plant</li><li>Locally made food: jam, honey, chutney</li></ul>
<h2>Low-waste swap ideas</h2>
<ul><li>Wrap in fabric (furoshiki), newspaper or brown paper instead of glossy paper</li><li>Agree a "second-hand only" rule for the whole group: it's a fun challenge</li><li>Use wishlists so nobody gets something they'll never use</li></ul></div>'''),
 dict(path='/printable-secret-santa-gift-tags', file='printable-secret-santa-gift-tags.html', nav='Printable Secret Santa gift tags',
  title='Printable Secret Santa Gift Tags: free, type names and print | SantaDraw',
  desc='Free printable Secret Santa gift tags. Type the names, print a sheet of tags signed "From your Secret Santa", cut and attach. Plus a free name draw.',
  h1='🏷️ Printable Secret Santa gift tags',
  sub='Type the names, print, cut, done. Tags signed "From: your Secret Santa".<br>Need to draw names first? Use the free draw above.',
  extra=TAGS),
 dict(path='/secret-santa-with-3-people', file='secret-santa-with-3-people.html', nav='Secret Santa with 3 people',
  title='Secret Santa with 3 People (or 4): does it work? Free draw | SantaDraw',
  desc='Can you do Secret Santa with just 3 or 4 people? Yes. How to keep it secret in a small group, fun rules for small groups, and a free name draw with private links.',
  h1='🎅 Secret Santa with 3 people',
  sub='Small group? It still works.<br>Draw names free and send each person a private link.',
  extra='''<div class="card"><h2 style="margin-top:0">Does Secret Santa work with 3 people?</h2>
<p>Yes. With 3 people there are only two possible draws (A→B→C→A or A→C→B→A), so once you know who you're buying for, you can work out who's buying for you. That's fine: the fun is in the surprise gift, not the mystery. If you want more mystery:</p>
<ul><li><strong>Add a "mystery" rule:</strong> everyone also brings a small anonymous gift for a lucky dip.</li>
<li><strong>Go to 4 or more:</strong> with 4 people there are 9 possible draws, so it's genuinely secret.</li>
<li><strong>Do two rounds:</strong> each person draws twice (run the draw twice with a lower budget each).</li></ul>
<h2>Small group ideas</h2>
<ul><li>Theme it: "something red", "a book and a snack", "under £5 and homemade"</li><li>Do a reveal: everyone guesses their Santa before opening</li><li>Add <a href="/secret-santa-gift-ideas">gift ideas</a> or a <a href="/secret-santa-wishlist-template">wishlist</a> so small budgets go further</li></ul>
<p>Groups of up to 6 are free on SantaDraw.</p></div>'''),
 dict(path='/secret-santa-reveal-ideas', file='secret-santa-reveal-ideas.html', nav='Secret Santa reveal ideas',
  title='Secret Santa Reveal Ideas: fun ways to reveal who your Santa was | SantaDraw',
  desc='Fun Secret Santa reveal ideas for family, friends and the office: guessing games, clue cards, Zoom reveals and more. Plus a free name draw with private links.',
  h1='🎉 Secret Santa reveal ideas',
  sub='The gifts are wrapped. Now the fun bit: who was whose Santa?<br>Ideas for the big reveal, plus a free name draw.',
  extra='''<div class="card"><h2 style="margin-top:0">Reveal games</h2>
<ul><li><strong>Guess first:</strong> before opening, everyone writes down who they think their Santa is. A point for each right guess.</li>
<li><strong>Clue cards:</strong> each Santa writes three clues about themselves on the tag (see <a href="/secret-santa-clues">Secret Santa clues</a>).</li>
<li><strong>Stand up when...:</strong> the organiser reads out each gift; the Santa stands up only when their recipient guesses right.</li>
<li><strong>Chain reveal:</strong> the first person opens, guesses, and then their real Santa opens next, until the chain closes.</li>
<li><strong>Video call reveal:</strong> for remote groups, open together on camera and guess in the chat (see <a href="/virtual-secret-santa">virtual Secret Santa</a>).</li></ul>
<h2>Keeping it secret until then</h2>
<p>With SantaDraw each person's link shows only their own match, so not even the organiser knows the pairs unless they peek. Ask everyone to sign tags "from your Secret Santa" (here are <a href="/printable-secret-santa-gift-tags">printable tags</a>) so handwriting doesn't give it away.</p></div>'''),
]

nav_html = ' · '.join('<a href="%s">%s</a>' % (p['path'], p['nav']) for p in PAGES)
for p in PAGES:
    s = T
    for k, v in [('{{TITLE}}', p['title']), ('{{DESC}}', p['desc']), ('{{PATH}}', p['path']), ('{{H1}}', p['h1']),
                 ('{{SUB}}', p['sub']), ('{{EXTRA}}', p['extra']), ('{{NAV}}', nav_html)]:
        s = s.replace(k, v)
    assert '{{' not in s, p['file']
    open(os.path.join(ROOT, 'site', p['file']), 'w').write(s)

today = datetime.date.today().isoformat()
urls = ''.join('<url><loc>%s%s</loc><lastmod>%s</lastmod></url>' % (BASE, p['path'], today) for p in PAGES)
urls += ''.join('<url><loc>%s/%s</loc></url>' % (BASE, x) for x in ('contact', 'terms', 'privacy'))
open(os.path.join(ROOT, 'site/sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>\n' % urls)
open(os.path.join(ROOT, 'site/robots.txt'), 'w').write('User-agent: *\nAllow: /\nDisallow: /reveal\nSitemap: %s/sitemap.xml\n' % BASE)
print('built', len(PAGES), 'pages')
