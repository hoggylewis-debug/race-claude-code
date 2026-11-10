#!/usr/bin/env python3
"""Session-start check required by OPERATOR.md.

1. Tests IMAP login to the SUPPORT_EMAIL mailbox (SUPPORT_EMAIL_PASSWORD).
2. Checks the published support address on terms/privacy/contact matches SUPPORT_EMAIL.
3. Sets the Pages secret SALES_OPEN to 1 (login OK) or 0 (login failed).
   Redeploy afterwards so the secret takes effect.
Never prints the address or password.
"""
import imaplib, os, subprocess, sys

HOSTS = {'gmail.com': 'imap.gmail.com', 'googlemail.com': 'imap.gmail.com', 'yahoo.com': 'imap.mail.yahoo.com',
         'yahoo.co.uk': 'imap.mail.yahoo.com', 'outlook.com': 'outlook.office365.com', 'hotmail.com': 'outlook.office365.com',
         'hotmail.co.uk': 'outlook.office365.com', 'live.com': 'outlook.office365.com', 'icloud.com': 'imap.mail.me.com',
         'aol.com': 'imap.aol.com', 'gmx.com': 'imap.gmx.com', 'zoho.com': 'imap.zoho.eu', 'proton.me': None}

email, pw = os.environ.get('SUPPORT_EMAIL', ''), os.environ.get('SUPPORT_EMAIL_PASSWORD', '')
ok = False
if not email or not pw:
    print('SUPPORT_EMAIL or SUPPORT_EMAIL_PASSWORD missing')
else:
    domain = email.split('@')[-1].lower()
    host = HOSTS.get(domain, 'imap.' + domain)
    try:
        m = imaplib.IMAP4_SSL(host, 993, timeout=20)
        m.login(email, pw)
        m.select('INBOX', readonly=True)
        typ, data = m.search(None, 'UNSEEN')
        print('IMAP login OK on', host, '- unseen messages:', len(data[0].split()) if data and data[0] else 0)
        m.logout(); ok = True
    except Exception as ex:
        print('IMAP login FAILED on', host, '-', type(ex).__name__, str(ex)[:120])

root = os.path.join(os.path.dirname(__file__), '..', 'site')
for f in ('terms.html', 'privacy.html', 'contact.html'):
    t = open(os.path.join(root, f)).read()
    print(f, 'shows current SUPPORT_EMAIL:', bool(email) and email in t)

if '--no-secret' not in sys.argv:
    val = '1' if ok else '0'
    r = subprocess.run(['npx', 'wrangler', 'pages', 'secret', 'put', 'SALES_OPEN', '--project-name', 'race-claude-code'],
                       input=val, text=True, capture_output=True)
    print('SALES_OPEN set to', val, '(ok)' if r.returncode == 0 else '(FAILED: ' + r.stderr[-200:] + ')')
    print('Now redeploy so it takes effect.')
print('SALES', 'OPEN' if ok else 'CLOSED')
