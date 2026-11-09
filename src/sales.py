#!/usr/bin/env python3
"""Paid SantaDraw customers from Stripe (reads STRIPE_SECRET_KEY from env; never prints it).

  python3 src/sales.py                 # list paid checkout sessions, unique customers, revenue
  python3 src/sales.py refund cs_live_...   # full refund of one checkout session

Emails are masked in output because this repo is public.
"""
import base64, json, os, sys, urllib.parse, urllib.request

KEY = os.environ.get('STRIPE_SECRET_KEY', '')
AUTH = 'Basic ' + base64.b64encode((KEY + ':').encode()).decode()


def api(path, data=None):
    req = urllib.request.Request('https://api.stripe.com/v1/' + path,
                                 data=urllib.parse.urlencode(data).encode() if data else None,
                                 headers={'Authorization': AUTH})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return json.load(e)


def mask(email):
    if not email or '@' not in email:
        return '?'
    u, d = email.split('@', 1)
    return u[:1] + '***@' + d


def sessions():
    after = None
    while True:
        q = 'checkout/sessions?limit=100' + (f'&starting_after={after}' if after else '')
        j = api(q)
        if 'error' in j:
            sys.exit('stripe error: ' + j['error'].get('message', ''))
        yield from j['data']
        if not j.get('has_more'):
            return
        after = j['data'][-1]['id']


def report():
    paid = [s for s in sessions() if s.get('payment_status') == 'paid']
    emails, total = set(), 0
    for s in sorted(paid, key=lambda s: s['created']):
        email = (s.get('customer_details') or {}).get('email') or ''
        emails.add(email.lower())
        total += s.get('amount_total') or 0
        import datetime
        ts = datetime.datetime.utcfromtimestamp(s['created']).strftime('%Y-%m-%d %H:%M')
        print(ts, s['id'][:20] + '…', mask(email), s.get('currency'), (s.get('amount_total') or 0) / 100)
    print(f'mode: {"live" if "_live_" in KEY else "test"}  paid sessions: {len(paid)}  unique customers: {len(emails)}  gross: £{total/100:.2f}')


def refund(sid):
    s = api('checkout/sessions/' + sid)
    pi = s.get('payment_intent')
    if not pi:
        sys.exit('no payment for ' + sid)
    r = api('refunds', {'payment_intent': pi})
    print('refund', r.get('status') or r.get('error', {}).get('message'))


if __name__ == '__main__':
    if not KEY:
        sys.exit('STRIPE_SECRET_KEY not set')
    if len(sys.argv) == 3 and sys.argv[1] == 'refund':
        refund(sys.argv[2])
    else:
        report()
