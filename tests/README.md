# Browser tests (Playwright, against the live site)

Setup (outside the repo): `mkdir -p /tmp/pw && cd /tmp/pw && npm init -y && npm i playwright@1 && npx playwright install chromium`
Run: `cp tests/*.js /tmp/pw/ && cd /tmp/pw && node smoke.js && node pay-test-mode.js`

- smoke.js: 4-name draw → WhatsApp link → reveal; 7 names → upsell; buy button reaches Stripe.
- pay-test-mode.js: pays with Stripe test card 4242 and checks Pro unlocks. ONLY works while the Pages secret is a TEST key. Never run with a live key.
- og.js + og.html: regenerate site/og.jpg (`node og.js /path/to/site/og.jpg`; og.html path is hard-coded to /tmp/pw/og.html).
- preview.js: while the Pages secret is a TEST key, "Unlock Pro" gives Pro free ("preview") instead of opening a TEST checkout. smoke.js and pay-test-mode.js open `/?sdtest=1`, which makes the site call `/api/checkout?test=1` to still reach the test checkout. Once the live key is installed, preview stops automatically (checkout.js checks the `sk_test_` prefix).
