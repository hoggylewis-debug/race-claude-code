#!/usr/bin/env python3
"""Submit every URL in site/sitemap.xml to IndexNow (Bing, Yandex, etc). Run after deploying."""
import json, re, urllib.request, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
k = open(os.path.join(ROOT, 'src/indexnow-key')).read().strip()
B = 'https://race-claude-code.pages.dev'
urls = re.findall(r'<loc>([^<]+)</loc>', open(os.path.join(ROOT, 'site/sitemap.xml')).read())
d = json.dumps({"host": "race-claude-code.pages.dev", "key": k, "keyLocation": f"{B}/{k}.txt", "urlList": urls}).encode()
r = urllib.request.urlopen(urllib.request.Request('https://api.indexnow.org/indexnow', d, {'Content-Type': 'application/json; charset=utf-8'}))
print('IndexNow', r.status, len(urls), 'urls')
