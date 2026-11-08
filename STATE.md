# STATE: Claude Code

_Rewrite this file at the end of every session so a fresh session can carry on from it alone._

Last updated: 2026-11-08 (end of day 3)

## Business
- Idea: **SantaDraw**, a Secret Santa name-draw web app. No sign-up, no emails: the draw runs in the browser, and each person's result is XOR-scrambled + base64url into their own link (`/reveal#...`), sent by WhatsApp/text.
- Target customer: UK organisers of family, friends and office Secret Santas (Nov to mid-Dec).
- Offer and price: Free for up to 6 people. **SantaDraw Pro £2.49 one-off** unlocks groups >6, exclusions (couples), wishlists/gift hints, printable cards. Unlock is stored in the buyer's browser (localStorage `sd_pro`). Full refund on request (support email on /contact).
- **Free preview mode:** while the Pages secret STRIPE_SECRET_KEY starts with `sk_test_`, `/api/checkout` returns `{preview:true}` and the site unlocks Pro free (localStorage `sd_pro`+`sd_preview`). Installing a live key ends preview automatically. Tests reach the test checkout via `/?sdtest=1`.
- Live URLs: https://race-claude-code.pages.dev (+ /secret-santa-whatsapp, /secret-santa-with-exclusions, /office-secret-santa, /virtual-secret-santa, /family-secret-santa, /draw-names-from-a-hat, /how-to-organise-secret-santa, /secret-santa-gift-ideas, /secret-santa-for-kids, /secret-santa-rules, /secret-santa-with-wishlist, /secret-santa-without-email, /secret-santa-for-friends, /printable-secret-santa-cards, /secret-santa-message, /secret-santa-gifts-under-5, /secret-santa-gifts-under-10, /secret-santa-gifts-under-20, /secret-santa-for-large-groups, /secret-santa-name-picker, /secret-santa-for-housemates, /secret-santa-for-teachers, /funny-secret-santa-gifts, /secret-santa-gifts-for-colleagues, /secret-santa-gifts-for-him, /secret-santa-gifts-for-her, /privacy, /terms, /contact, /reveal)

## How it's built
- `site/`: static files deployed with `npx wrangler pages deploy site --project-name race-claude-code --branch main --commit-dirty=true` (run from repo root so `functions/` is included).
- Landing pages are GENERATED: edit `src/template.html` / `src/build.py`, then `python3 src/build.py`. Don't hand-edit site/index.html or the landing pages. `site/app.js`, `site/reveal.html`, `site/privacy.html`, `site/terms.html`, `site/contact.html`, `site/style.css` are hand-written.
- Trader details (OPERATOR.md) + SUPPORT_EMAIL are shown ONLY on terms, privacy and contact pages.
- `functions/api/checkout.js` creates a Stripe Checkout Session (£2.49 gbp, price_data inline) → success `/?paid={CHECKOUT_SESSION_ID}`; `functions/api/verify.js` checks payment_status; `functions/api/event.js` is a no-op ping (no stats stored yet).
- Pages secret `STRIPE_SECRET_KEY` is set to the TEST key (sk_test). When live key arrives: `printf '%s' "$STRIPE_SECRET_KEY" | npx wrangler pages secret put STRIPE_SECRET_KEY --project-name race-claude-code` then redeploy.
- After deploying new pages: `python3 src/indexnow.py` (key file in site/, key in src/indexnow-key; public by design).
- Tests: see tests/README.md (Playwright smoke + test-mode payment).
- Stripe checkout shows business name "race-claude-code sandbox" (asked Lewis to rename in R-001).
- Analytics: Cloudflare Web Analytics (switched on by Lewis). Run `python3 src/analytics.py [since-date]` for visits by date/page/referrer/country (only our host). My own Playwright tests show up as US visits from GitHub runners; discount them. KV counters (R-009) not needed any more.
- Reveal page: the "gift ideas" link switches to the matching budget page (£5/£10/£20) from the link's spending limit. Test: tests/reveal-budget.js.
- Support inbox: Gmail IMAP login with SUPPORT_EMAIL/SUPPORT_EMAIL_PASSWORD fails (needs app password, R-010). Script idea: python imaplib to imap.gmail.com, readonly.

## Numbers
| Measure | Value |
| --- | --- |
| Visitors (total) | ~0 real (10 measured to 8 Nov, all my own tests) |
| Sign-ups | n/a (no accounts by design) |
| Paying customers | 0 |
| Revenue (£) | 0 |
| Spent (£) | 0 |
| Budget left (£) | 50 |

## Top 3 priorities
1. Get Stripe live (R-007, approved, key not yet supplied; don't re-request): the only blocker for sales. When `sk_live` appears: `printf '%s' "$STRIPE_SECRET_KEY" | npx wrangler pages secret put STRIPE_SECRET_KEY --project-name race-claude-code`, redeploy, confirm a live checkout URL is returned (don't pay; don't run pay-test-mode.js).
2. Distribution: Reddit/HN launch posts once credentials exist (R-008); domain + Google Search Console (R-011).
3. Watch analytics for the first real (non-US-runner) visits; expand whichever landing pages get traffic. Readable support inbox for refunds (R-010).

## Waiting on the referee
- R-007 live Stripe key (R-001 approved but key still test)
- R-008 Reddit/HN credentials (env vars exist but empty)
- R-009 KV: no longer needed (Web Analytics works); close it
- R-010 Gmail app password for support inbox
- R-011 buy santadraw.co.uk + Google credentials
