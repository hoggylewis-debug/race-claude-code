#!/usr/bin/env python3
"""Builds the landing pages in site/ from src/template.html. Run: python3 src/build.py"""
import os, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://race-claude-code.pages.dev'
T = open(os.path.join(ROOT, 'src/template.html')).read()
SUB = 'Secret Santa names drawn in 30 seconds. No sign-up. No email addresses.<br>Everyone gets a private link you can send by WhatsApp, text or Messenger.'

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
<p>Tip: don't post the links in the group chat itself, send each one privately, or everyone could open everyone's link.</p></div>'''),
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
<p><strong>Best tip:</strong> ask everyone to add 2 or 3 ideas to the wishlist box when you draw (Pro). Whoever draws them sees the hints in their private link, so nobody gets a gift they don't want.</p></div>'''),
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
open(os.path.join(ROOT, 'site/sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>\n' % urls)
open(os.path.join(ROOT, 'site/robots.txt'), 'w').write('User-agent: *\nAllow: /\nDisallow: /reveal\nSitemap: %s/sitemap.xml\n' % BASE)
print('built', len(PAGES), 'pages')
