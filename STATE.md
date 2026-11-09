# STATE: Claude Code

_Rewrite this file at the end of every session so a fresh session can carry on from it alone._

Last updated: 2026-11-09 (end of day 4)

## Business
- Idea: **SantaDraw**, a Secret Santa name-draw web app. No sign-up, no emails: the draw runs in the browser, and each person's result is XOR-scrambled + base64url into their own link (`/reveal#...`), sent by WhatsApp/text.
- Target customer: UK organisers of family, friends and office Secret Santas (Nov to mid-Dec).
- Offer and price: Free for up to 6 people. **SantaDraw Pro £2.49 one-off** unlocks groups >6, exclusions (couples), wishlists/gift hints, printable cards. Unlock is stored in the buyer's browser (localStorage `sd_pro`). Full refund on request (support email on /contact).
- **LIVE PAYMENTS ON since 2026-11-09.** Pages secret STRIPE_SECRET_KEY = live restricted key (rk_live_, from the session env). Checkout header shows merchant "race-claude-code" until Lewis renames it (R-012); buy-button text explains this. (Old free-preview code path in checkout.js only triggers for `sk_test_` keys, so it is dormant.)
- Live URLs: https://race-claude-code.pages.dev (+ /secret-santa-whatsapp, /secret-santa-with-exclusions, /office-secret-santa, /virtual-secret-santa, /family-secret-santa, /draw-names-from-a-hat, /how-to-organise-secret-santa, /secret-santa-gift-ideas, /secret-santa-for-kids, /secret-santa-rules, /secret-santa-with-wishlist, /secret-santa-without-email, /secret-santa-for-friends, /printable-secret-santa-cards, /secret-santa-message, /secret-santa-gifts-under-5, /secret-santa-gifts-under-10, /secret-santa-gifts-under-20, /secret-santa-for-large-groups, /secret-santa-name-picker, /secret-santa-for-housemates, /secret-santa-for-teachers, /funny-secret-santa-gifts, /secret-santa-gifts-for-colleagues, /secret-santa-gifts-for-him, /secret-santa-gifts-for-her, /kris-kindle-generator, /secret-santa-app, /secret-santa-for-couples, /secret-santa-gifts-for-teenagers, /christmas-name-draw, /privacy, /terms, /contact, /reveal)

## How it's built
- `site/`: static files deployed with `npx wrangler pages deploy site --project-name race-claude-code --branch main --commit-dirty=true` (run from repo root so `functions/` is included).
- Landing pages are GENERATED: edit `src/template.html` / `src/build.py`, then `python3 src/build.py`. Don't hand-edit site/index.html or the landing pages. `site/app.js`, `site/reveal.html`, `site/privacy.html`, `site/terms.html`, `site/contact.html`, `site/style.css` are hand-written.
- Trader details (OPERATOR.md) + SUPPORT_EMAIL are shown ONLY on terms, privacy and contact pages.
- `functions/api/checkout.js` creates a Stripe Checkout Session (£2.49 gbp, price_data inline) → success `/?paid={CHECKOUT_SESSION_ID}`; `functions/api/verify.js` checks payment_status; `functions/api/event.js` is a no-op ping (no stats stored yet).
- Pages secret `STRIPE_SECRET_KEY` is the LIVE restricted key. If the env key ever changes: `printf '%s' "$STRIPE_SECRET_KEY" | npx wrangler pages secret put STRIPE_SECRET_KEY --project-name race-claude-code` then redeploy. NEVER run tests/pay-test-mode.js or preview.js now.
- Sales + refunds: `python3 src/sales.py` (paid sessions, unique customers, revenue; emails masked). Refund: `python3 src/sales.py refund cs_live_...` (key has refund permission). Refunds must never be refused.
- After deploying new pages: `python3 src/indexnow.py` (key file in site/, key in src/indexnow-key; public by design).
- Tests: see tests/README.md (Playwright smoke + test-mode payment).
- Live Stripe checkout shows business name "race-claude-code" (rename requested in R-012).
- Public GitHub README lists links to every landing page (regenerate the list by hand if pages are added).
- Analytics: Cloudflare Web Analytics (switched on by Lewis). Run `python3 src/analytics.py [since-date]` for visits by date/page/referrer/country (only our host). My own Playwright tests show up as US visits from GitHub runners; discount them. KV counters (R-009) not needed any more.
- Reveal page: the "gift ideas" link switches to the matching budget page (£5/£10/£20) from the link's spending limit. Test: tests/reveal-budget.js.
- Support inbox: Gmail IMAP login with SUPPORT_EMAIL/SUPPORT_EMAIL_PASSWORD fails (needs app password, R-010). Script idea: python imaplib to imap.gmail.com, readonly.

## Numbers
| Measure | Value |
| --- | --- |
| Visitors (total) | ~0 real (18 measured to 9 Nov, all my own US test runs) |
| Sign-ups | n/a (no accounts by design) |
| Paying customers | 0 |
| Revenue (£) | 0 |
| Spent (£) | 0 |
| Budget left (£) | 50 (£20 requested for Google Ads in R-013) |

## Top 3 priorities
1. Traffic. The product and live checkout work; nobody visits. R-013 (£20 Google Ads, exact spec in REQUESTS.md): if approved, set it up / check it ran. R-008 Reddit/HN and R-011 domain + Google Search Console still waiting (approved; don't re-request).
2. Check `python3 src/sales.py` and `python3 src/analytics.py <since>` every session; build more of whatever pages get real (non-US-runner) visits. Bing/DDG haven't indexed pages.dev yet (IndexNow submitted daily).
3. Support inbox (R-010): can't read refund emails yet; refunds possible via src/sales.py. When the password works, check the inbox every session.

## Waiting on the referee
- R-008 Reddit/HN credentials (env vars exist but empty)
- R-010 Gmail app password for support inbox (current 10-char password still rejected 9 Nov)
- R-011 buy santadraw.co.uk + Google credentials
- R-012 Stripe public business name → SantaDraw (filed 9 Nov)
- R-013 £20 Google Ads search campaign (filed 9 Nov)
