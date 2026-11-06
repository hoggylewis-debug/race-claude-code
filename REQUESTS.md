# REQUESTS: Claude Code

_Anything gated in BRIEF.md goes here. Add the request, then keep working on something else._
_Lewis answers from his phone. His answers appear in REPLIES.md, not in this file. No answer within 24 hours means declined._
_Once an answer is in and you have acted on it, change OPEN to CLOSED in the request's heading._

```
## R-001 | YYYY-MM-DD | OPEN
- Action:
- Why:
- Cost: £
- Exact text / link:
```

## R-001 | 2026-11-06 | OPEN
- Action: Switch Stripe to live mode and set the live secret key as the `STRIPE_SECRET_KEY` session environment variable (I'll then upload it as a Pages secret myself). Also, if possible, set the Stripe public business name to "SantaDraw" (checkout currently shows "race-claude-code sandbox").
- Why: SantaDraw (https://race-claude-code.pages.dev) is live with a working £2.49 Pro checkout, fully tested end-to-end in test mode. Secret Santa season is now: every day in test mode is lost sales.
- Cost: £0 (Stripe fees only, taken from revenue)
- Exact text / link: https://dashboard.stripe.com → activate account → Developers → API keys (live secret key)

## R-002 | 2026-11-06 | OPEN
- Action: Create a Reddit account for SantaDraw (username e.g. u/SantaDrawApp) and let me post one launch post in r/SideProject and one in r/InternetIsBeautiful (both allow showing off your own free tools). I need the login provided as env vars REDDIT_USERNAME / REDDIT_PASSWORD, or you post the exact text below.
- Why: Distribution. Each draw sends the site link to 4-20 people, so a few organisers early compounds.
- Cost: £0
- Exact text / link: Title: "I built a Secret Santa generator with no sign-up: names are drawn in your browser and everyone gets a private WhatsApp link". Body: "SantaDraw draws names in 30 seconds with no accounts and no email addresses. The draw happens in your browser and each person's result is scrambled inside their own link, so nothing is stored on a server. Free for up to 6 people; a one-off £2.49 Pro adds bigger groups, exclusions for couples, wishlists and printable cards. Disclosure: it's built and run by an AI agent (Claude Code) as part of a public experiment. Feedback very welcome: https://race-claude-code.pages.dev"

## R-003 | 2026-11-06 | OPEN
- Action: Create a Hacker News account and a Product Hunt account for SantaDraw (credentials as env vars HN_USERNAME/HN_PASSWORD, PH via your login), so I can post a "Show HN" and a Product Hunt launch.
- Why: Free launch channels; the "AI agent runs a business" angle plus a privacy-first tool suits both audiences.
- Cost: £0
- Exact text / link: Show HN: "Show HN: SantaDraw, a Secret Santa draw that stores nothing (run by an AI agent)" linking to https://race-claude-code.pages.dev with the same body as R-002.

## R-004 | 2026-11-06 | OPEN
- Action: Allow me to create ONE Cloudflare KV namespace named `race-claude-code-stats` and bind it only to the `race-claude-code` Pages project, to count visits, draws and reveals (anonymous counters, no personal data).
- Why: I currently have no way to measure visitors (Pages has no built-in analytics without account-level settings), so I can't report visitor numbers or see which pages work.
- Cost: £0 (free tier)
- Exact text / link: `npx wrangler kv namespace create race-claude-code-stats`

## R-005 | 2026-11-06 | OPEN
- Action: Buy the domain santadraw.co.uk (checked available today via Nominet RDAP) for 1 year at Porkbun, then add 2 DNS settings there: (1) CNAME record `www` → `race-claude-code.pages.dev`; (2) URL forward of the bare `santadraw.co.uk` → `https://www.santadraw.co.uk` (permanent). I will attach www.santadraw.co.uk to the race-claude-code Pages project myself and update all links.
- Why: The product works by sending private links to everyone in a WhatsApp group. "race-claude-code.pages.dev/reveal#..." looks like spam to a gran in a family chat; "santadraw.co.uk" looks trustworthy and is memorable, so more people open links and come back to start their own draw.
- Cost: about £6 (Porkbun .co.uk first-year price; please decline if over £10)
- Exact text / link: https://porkbun.com/checkout/search?q=santadraw.co.uk

## R-006 | 2026-11-06 | OPEN
- Action: Create a new Google account for SantaDraw (not one of yours) and give me its login as env vars GOOGLE_USERNAME / GOOGLE_PASSWORD, so I can add the site to Google Search Console (HTML-file verification, which I deploy myself) and submit the sitemap.
- Why: Secret Santa searches peak from mid-November. I've built 9 search-targeted pages and submitted them to Bing via IndexNow, but Google has no equivalent without Search Console, and Google is most UK searches.
- Cost: £0
- Exact text / link: https://search.google.com/search-console
