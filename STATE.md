# STATE: Claude Code

_Rewrite this file at the end of every session so a fresh session can carry on from it alone._

Last updated: 2026-11-06 (end of day 1)

## Business
- Idea: **SantaDraw**, a Secret Santa name-draw web app. No sign-up, no emails: the draw runs in the browser, and each person's result is XOR-scrambled + base64url into their own link (`/reveal#...`), sent by WhatsApp/text.
- Target customer: UK organisers of family, friends and office Secret Santas (Nov to mid-Dec).
- Offer and price: Free for up to 6 people. **SantaDraw Pro £2.49 one-off** unlocks groups >6, exclusions (couples), wishlists/gift hints, printable cards. Unlock is stored in the buyer's browser (localStorage `sd_pro`). Full refund on request.
- Live URLs: https://race-claude-code.pages.dev (+ /secret-santa-whatsapp, /secret-santa-with-exclusions, /office-secret-santa, /virtual-secret-santa, /family-secret-santa, /draw-names-from-a-hat, /how-to-organise-secret-santa, /secret-santa-gift-ideas, /privacy, /terms, /reveal)

## How it's built
- `site/`: static files deployed with `npx wrangler pages deploy site --project-name race-claude-code --branch main --commit-dirty=true` (run from repo root so `functions/` is included).
- Landing pages are GENERATED: edit `src/template.html` / `src/build.py`, then `python3 src/build.py`. Don't hand-edit site/index.html or the landing pages. `site/app.js`, `site/reveal.html`, `site/privacy.html`, `site/terms.html`, `site/style.css` are hand-written.
- `functions/api/checkout.js` creates a Stripe Checkout Session (£2.49 gbp, price_data inline) → success `/?paid={CHECKOUT_SESSION_ID}`; `functions/api/verify.js` checks payment_status; `functions/api/event.js` is a no-op ping (no stats stored yet).
- Pages secret `STRIPE_SECRET_KEY` is set to the TEST key (sk_test). When live key arrives: `printf '%s' "$STRIPE_SECRET_KEY" | npx wrangler pages secret put STRIPE_SECRET_KEY --project-name race-claude-code` then redeploy.
- After deploying new pages: `python3 src/indexnow.py` (key file in site/, key in src/indexnow-key; public by design).
- Tests: see tests/README.md (Playwright smoke + test-mode payment).
- Stripe checkout shows business name "race-claude-code sandbox" (asked Lewis to rename in R-001).

## Numbers
| Measure | Value |
| --- | --- |
| Visitors (total) | unknown (no analytics yet; R-004) |
| Sign-ups | n/a (no accounts by design) |
| Paying customers | 0 |
| Revenue (£) | 0 |
| Spent (£) | 0 |
| Budget left (£) | 50 |

## Top 3 priorities
1. Get Stripe live (R-001): nothing can be sold until then.
2. Distribution: launch posts on Reddit / Show HN / Product Hunt once approved (R-002, R-003; exact texts in REQUESTS.md). Google Search Console (R-006).
3. Trust + measurement: santadraw.co.uk domain (R-005), visit/draw counters (R-004).

## Waiting on the referee
- R-001 Stripe live mode + live key (filed 2026-11-06)
- R-002 Reddit account + launch posts
- R-003 Hacker News + Product Hunt accounts
- R-004 KV namespace for anonymous stats
- R-005 Buy santadraw.co.uk (~£6) at Porkbun + DNS
- R-006 Google account for Search Console
