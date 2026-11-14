# STATE: Claude Code

_Rewrite this file at the end of every session so a fresh session can carry on from it alone._

Last updated: 2026-11-14 (end of day 9)

## Business
- Idea: **SantaDraw**, a Secret Santa name-draw web app. No sign-up, no emails: the draw runs in the browser, and each person's result is XOR-scrambled + base64url into their own link (`/reveal#...`), sent by WhatsApp/text.
- Target customer: UK organisers of family, friends and office Secret Santas (Nov to mid-Dec).
- Sharing: after a draw the organiser gets ONE group-chat link (reveal page asks "Who are you?", locks that phone to a name via localStorage `sd_claim_<hash>`) plus individual private links. Group payload = `{p:[[name,to,wish?]...],g,b,d}`.
- Offer and price: Free for up to 6 people. **SantaDraw Pro £2.49 one-off** unlocks groups >6, exclusions (couples), wishlists/gift hints, printable cards. Unlock is stored in the buyer's browser (localStorage `sd_pro`). Full refund on request (support email on /contact).
- **SALES OPEN since 2026-11-12.** OPERATOR.md rule: the support address santadraw.support@gmx.co.uk is an alias that only Lewis reads. NEVER log in to it (no IMAP/SMTP). Lewis answers customer emails and does refunds. Sales may be open only while the SUPPORT_EMAIL env var equals that address (the env value has a trailing newline; compare trimmed). Switch = Pages secret `SALES_OPEN` ("1" open). At the START OF EVERY SESSION run `python3 src/support_check.py`: it checks the env address, the address on terms/privacy/contact, the live key and the Stripe public name, sets SALES_OPEN, then redeploy. If closed: checkout.js returns `{preview:true, closed:true}`, "Unlock Pro" gives Pro free with a "payments paused" note, and `/api/status` = `{sales:false}`.
- Live Stripe key installed 2026-11-09. Pages secret STRIPE_SECRET_KEY = live restricted key (rk_live_, from the session env). Stripe public name "SantaDraw", statement descriptor "SANTADRAW" (done by Lewis, R-012). (Old free-preview code path in checkout.js only triggers for `sk_test_` keys, so it is dormant.)
- Live URLs: https://race-claude-code.pages.dev (+ /secret-santa-whatsapp, /secret-santa-with-exclusions, /office-secret-santa, /virtual-secret-santa, /family-secret-santa, /draw-names-from-a-hat, /how-to-organise-secret-santa, /secret-santa-gift-ideas, /secret-santa-for-kids, /secret-santa-rules, /secret-santa-with-wishlist, /secret-santa-without-email, /secret-santa-for-friends, /printable-secret-santa-cards, /secret-santa-message, /secret-santa-gifts-under-5, /secret-santa-gifts-under-10, /secret-santa-gifts-under-20, /secret-santa-for-large-groups, /secret-santa-name-picker, /secret-santa-for-housemates, /secret-santa-for-teachers, /funny-secret-santa-gifts, /secret-santa-gifts-for-colleagues, /secret-santa-gifts-for-him, /secret-santa-gifts-for-her, /kris-kindle-generator, /secret-santa-app, /secret-santa-for-couples, /secret-santa-gifts-for-teenagers, /christmas-name-draw, /secret-santa-group-chat, /secret-santa-questionnaire (interactive form), /secret-santa-themes, /secret-santa-poems, /secret-santa-clues, /secret-santa-gifts-under-15, /secret-santa-gifts-for-mum, /secret-santa-gifts-for-dad, /secret-santa-gifts-under-25, /secret-santa-gifts-under-30, /secret-santa-gifts-for-boss, /secret-santa-wishlist-template, /secret-santa-gifts-for-grandparents, /secret-santa-gifts-for-kids, /eco-friendly-secret-santa-gifts, /printable-secret-santa-gift-tags (type-and-print tool), /secret-santa-with-3-people, /secret-santa-reveal-ideas, /secret-santa-for-nurses, /secret-santa-for-big-families, /secret-santa-for-clubs, /secret-santa-generator-uk, /secret-santa-budget-calculator (savings calculator), /secret-santa-invitation (invitation generator, INVITE string near top of src/build.py), /secret-santa-for-remote-teams, /secret-santa-exchange, /privacy, /terms, /contact, /reveal)

## How it's built
- `site/`: static files deployed with `npx wrangler pages deploy site --project-name race-claude-code --branch main --commit-dirty=true` (run from repo root so `functions/` is included).
- 58 landing pages. The invitation generator is the INVITE string near the top of src/build.py (test: tests/invite.js). The gift-tag tool is the TAGS string near the top of src/build.py. The questionnaire page's form + script lives in the EXTRA_Q string near the top of src/build.py.
- Landing pages are GENERATED: edit `src/template.html` / `src/build.py`, then `python3 src/build.py`. Don't hand-edit site/index.html or the landing pages. `site/app.js`, `site/reveal.html`, `site/privacy.html`, `site/terms.html`, `site/contact.html`, `site/style.css` are hand-written.
- Trader details (OPERATOR.md) + SUPPORT_EMAIL are shown ONLY on terms, privacy and contact pages.
- `functions/api/checkout.js` creates a Stripe Checkout Session (£2.49 gbp, price_data inline) → success `/?paid={CHECKOUT_SESSION_ID}`; `functions/api/verify.js` checks payment_status; `functions/api/event.js` is a no-op ping (no stats stored yet).
- Pages secret `STRIPE_SECRET_KEY` is the LIVE restricted key. If the env key ever changes: `printf '%s' "$STRIPE_SECRET_KEY" | npx wrangler pages secret put STRIPE_SECRET_KEY --project-name race-claude-code` then redeploy. NEVER run tests/pay-test-mode.js or preview.js now.
- Sales + refunds: `python3 src/sales.py` (paid sessions, unique customers, revenue; emails masked). Refund: `python3 src/sales.py refund cs_live_...` (key has refund permission). Refunds must never be refused.
- After deploying new pages: `python3 src/indexnow.py` (key file in site/, key in src/indexnow-key; public by design).
- Tests: see tests/README.md (Playwright smoke + test-mode payment).
- Public GitHub README lists links to every landing page (regenerate the list by hand if pages are added).
- Analytics: Cloudflare Web Analytics (switched on by Lewis). Run `python3 src/analytics.py [since-date]` for visits by date/page/referrer/country (only our host). My own Playwright tests show up as US visits from GitHub runners; discount them. KV counters (R-009) not needed any more.
- Reveal page: has "Start your own draw" (?ref=reveal), "Send it to another group" WhatsApp share (?ref=share) and a questionnaire link. The "gift ideas" link switches to the matching budget page (£5/£10/£20) from the link's spending limit. Limits of £5/10/15/20/25/30 each map to their own page. Test: tests/reveal-budget.js. tests/questionnaire.js checks the questionnaire form. smoke.js fails at the buy step while sales are closed (expected).
- Support inbox: Lewis-only alias, no login (OPERATOR.md). Tests: tests/smoke.js (passes with sales open; opens the live checkout without paying), tests/tags.js, tests/sales-closed.js (only meaningful while closed), tests/group-link.js, tests/calc.js (new pages + budget calculator) (copy to /tmp/pw).

## Numbers
| Measure | Value |
| --- | --- |
| Visitors (total) | ~0 real (all views 11 to 13 Nov are my own US test runs plus 2 PL bots). Not indexed by Google or Bing yet (checked 14 Nov) |
| Sign-ups | n/a (no accounts by design) |
| Paying customers | 0 |
| Revenue (£) | 0 |
| Spent (£) | 0 |
| Budget left (£) | 50 (£20 requested for Google Ads in R-013) |

## Top 3 priorities
0. Session start: `python3 src/support_check.py`, then redeploy. Wrangler deploys can fail with "malformed response" during Cloudflare outages (13 Nov): retry in a loop, then check the live sitemap really changed. Sales are OPEN while it prints SALES OPEN.
1. Traffic is the only blocker now: the product works and live checkout works (£2.49), but nobody visits. R-013 (£20 Google Ads, approved 9 Nov, exact spec in REQUESTS.md): once credentials or a running campaign appear, set it up or check it. R-008 (Reddit/HN) and R-011 (domain + Google Search Console) are approved but waiting on Lewis. Don't re-request.
2. Every session, run `python3 src/sales.py` and `python3 src/analytics.py <since>`. Build more of whatever pages get real (non-US-runner) visits. IndexNow resubmits daily.
3. Keep adding high-intent pages and spreading features (reveal page CTA, group link) while the traffic channels are blocked. Done 13 Nov: big families, budget calculator, nurses/NHS, generator UK, clubs. Done 14 Nov: invitation generator, remote teams, gift exchange. Next ideas: gifts for teachers from the class, gifts for nurses, a "who has who" organiser checklist, Secret Santa for schools/PTA.

## Waiting on the referee
- R-015 (filed 14 Nov): approval only, to submit the site myself to free no-account directory forms (Launching Next first; exact text in REQUESTS.md). If APPROVED, use Playwright (curl gets 403). Skip any that need an account or payment. If there's no reply by 15 Nov 14:30 UTC it counts as declined.
- R-008 Reddit/HN credentials (env vars exist but empty)
- R-011 buy santadraw.co.uk + Google credentials (Stripe profile URL already says santadraw.co.uk, but the domain doesn't resolve to us yet)
- R-013 £20 Google Ads search campaign (approved 9 Nov, not set up yet)
- Closed 12 Nov: R-010/R-014 (superseded by the new support rule), R-012 (Stripe name done)
