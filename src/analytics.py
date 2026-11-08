#!/usr/bin/env python3
"""Visitor numbers from Cloudflare Web Analytics (RUM) for OUR host only.
Run: python3 src/analytics.py [since-date]   (needs CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID; never prints them)
Note: our own Playwright tests also count as visits; subtract test runs when reporting."""
import json, os, sys, urllib.request, datetime, collections
since = sys.argv[1] if len(sys.argv) > 1 else '2026-11-06'
today = datetime.date.today().isoformat()
q = '''query($a:String!,$s:Date!,$e:Date!){viewer{accounts(filter:{accountTag:$a}){
rumPageloadEventsAdaptiveGroups(limit:1000,filter:{date_geq:$s,date_leq:$e,requestHost:"race-claude-code.pages.dev"}){
count sum{visits} dimensions{date requestPath refererHost countryName}}}}}'''
body = json.dumps({'query': q, 'variables': {'a': os.environ['CLOUDFLARE_ACCOUNT_ID'], 's': since, 'e': today}}).encode()
req = urllib.request.Request('https://api.cloudflare.com/client/v4/graphql', body,
      {'Authorization': 'Bearer ' + os.environ['CLOUDFLARE_API_TOKEN'], 'Content-Type': 'application/json'})
d = json.load(urllib.request.urlopen(req))
if d.get('errors'): sys.exit(d['errors'])
rows = d['data']['viewer']['accounts'][0]['rumPageloadEventsAdaptiveGroups']
pv = lambda f: sum((collections.Counter({f(r): r['count']}) for r in rows), collections.Counter())
print('Total visits:', sum(r['sum']['visits'] for r in rows), ' page views:', sum(r['count'] for r in rows))
for name, f in [('date', lambda r: r['dimensions']['date']), ('path', lambda r: r['dimensions']['requestPath']),
                ('referrer', lambda r: r['dimensions']['refererHost'] or '(direct)'), ('country', lambda r: r['dimensions']['countryName'])]:
    print(f'\nPage views by {name}:')
    for k, v in sorted(pv(f).items(), key=lambda x: -x[1])[:15]: print(f'  {v:5}  {k}')
