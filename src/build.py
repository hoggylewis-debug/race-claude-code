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
