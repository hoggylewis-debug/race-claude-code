# Browser tests (Playwright, against the live site)

Setup (outside the repo): `mkdir -p /tmp/pw && cd /tmp/pw && npm init -y && npm i playwright@1 && npx playwright install chromium`
Run: `cp tests/*.js /tmp/pw/ && cd /tmp/pw && node smoke.js && node pay-test-mode.js`

- smoke.js: 4-name draw → WhatsApp link → reveal; 7 names → upsell; buy button reaches Stripe.
- pay-test-mode.js: pays with Stripe test card 4242 and checks Pro unlocks. ONLY works while the Pages secret is a TEST key. Never run with a live key.
- og.js + og.html: regenerate site/og.jpg (`node og.js /path/to/site/og.jpg`; og.html path is hard-coded to /tmp/pw/og.html).
- preview.js: while the Pages secret is a TEST key, "Unlock Pro" gives Pro free ("preview") instead of opening a TEST checkout. smoke.js and pay-test-mode.js open `/?sdtest=1`, which makes the site call `/api/checkout?test=1` to still reach the test checkout. Once the live key is installed, preview stops automatically (checkout.js checks the `sk_test_` prefix).

**Since 2026-11-09 the Pages secret is a LIVE restricted key (rk_live_).** Do NOT run pay-test-mode.js or preview.js (they will fail / would try a real payment). smoke.js is safe: it only opens the live checkout page without paying (the session expires unused after 24h). To check payments use `python3 src/sales.py`.
- questionnaire.js: fills the /secret-santa-questionnaire form, checks 'Add to wishlist' fills the draw form and the WhatsApp link. (smoke.js fails while sales are closed; use sales-closed.js then.)
- tags.js: printable gift tags page makes escaped tags; new pages return 200.
