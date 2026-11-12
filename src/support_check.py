#!/usr/bin/env python3
"""Session-start check required by OPERATOR.md (support inbox rule, 12 Nov 2026 version).

The support address is an alias read only by Lewis. We must NOT log in to it (no IMAP/SMTP).
Sales may open only when the SUPPORT_EMAIL env var equals the published support address,
the live Stripe key is present and the Stripe public profile is ready.

1. Compares SUPPORT_EMAIL (surrounding whitespace ignored) with the published address.
2. Checks terms/privacy/contact show that address.
3. Checks STRIPE_SECRET_KEY is live and the Stripe public business name is set.
4. Sets the Pages secret SALES_OPEN to 1 (all OK) or 0. Redeploy afterwards.
Never prints secrets.
"""
import json, os, subprocess, sys, urllib.request

PUBLISHED = 'santadraw.support@gmx.co.uk'
env_email = os.environ.get('SUPPORT_EMAIL', '').strip().lower()
email_ok = env_email == PUBLISHED
print('SUPPORT_EMAIL matches published address:', email_ok)

root = os.path.join(os.path.dirname(__file__), '..', 'site')
pages_ok = True
for f in ('terms.html', 'privacy.html', 'contact.html'):
    shown = PUBLISHED in open(os.path.join(root, f)).read()
    pages_ok &= shown
    print(f, 'shows support address:', shown)

key = os.environ.get('STRIPE_SECRET_KEY', '')
stripe_ok = key.startswith(('sk_live_', 'rk_live_'))
print('Live Stripe key present:', stripe_ok)
if stripe_ok:
    try:
        req = urllib.request.Request('https://api.stripe.com/v1/account', headers={'Authorization': 'Bearer ' + key})
        acct = json.load(urllib.request.urlopen(req, timeout=20))
        name = (acct.get('business_profile') or {}).get('name')
        print('Stripe public name:', name, '| charges enabled:', acct.get('charges_enabled'))
        stripe_ok = bool(name) and bool(acct.get('charges_enabled'))
    except Exception as ex:
        print('Could not read Stripe account:', type(ex).__name__)
        stripe_ok = False

ok = email_ok and pages_ok and stripe_ok
if '--no-secret' not in sys.argv:
    val = '1' if ok else '0'
    r = subprocess.run(['npx', 'wrangler', 'pages', 'secret', 'put', 'SALES_OPEN', '--project-name', 'race-claude-code'],
                       input=val, text=True, capture_output=True)
    print('SALES_OPEN set to', val, '(ok)' if r.returncode == 0 else '(FAILED: ' + r.stderr[-200:] + ')')
    print('Now redeploy so it takes effect.')
print('SALES', 'OPEN' if ok else 'CLOSED')
