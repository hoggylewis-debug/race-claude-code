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

## R-001 | 2026-11-06 | CLOSED (approved; see R-007)
- Action: Switch Stripe to live mode and set the live secret key as the `STRIPE_SECRET_KEY` session environment variable (I'll then upload it as a Pages secret myself). Also, if possible, set the Stripe public business name to "SantaDraw" (checkout currently shows "race-claude-code sandbox").
- Why: SantaDraw (https://race-claude-code.pages.dev) is live with a working £2.49 Pro checkout, fully tested end-to-end in test mode. Secret Santa season is now: every day in test mode is lost sales.
- Cost: £0 (Stripe fees only, taken from revenue)
- Exact text / link: https://dashboard.stripe.com → activate account → Developers → API keys (live secret key)

## R-002 | 2026-11-06 | CLOSED (approved; see R-008)
- Action: Create a Reddit account for SantaDraw (username e.g. u/SantaDrawApp) and let me post one launch post in r/SideProject and one in r/InternetIsBeautiful (both allow showing off your own free tools). I need the login provided as env vars REDDIT_USERNAME / REDDIT_PASSWORD, or you post the exact text below.
- Why: Distribution. Each draw sends the site link to 4-20 people, so a few organisers early compounds.
- Cost: £0
- Exact text / link: Title: "I built a Secret Santa generator with no sign-up: names are drawn in your browser and everyone gets a private WhatsApp link". Body: "SantaDraw draws names in 30 seconds with no accounts and no email addresses. The draw happens in your browser and each person's result is scrambled inside their own link, so nothing is stored on a server. Free for up to 6 people; a one-off £2.49 Pro adds bigger groups, exclusions for couples, wishlists and printable cards. Disclosure: it's built and run by an AI agent (Claude Code) as part of a public experiment. Feedback very welcome: https://race-claude-code.pages.dev"

## R-003 | 2026-11-06 | CLOSED (approved; see R-008)
- Action: Create a Hacker News account and a Product Hunt account for SantaDraw (credentials as env vars HN_USERNAME/HN_PASSWORD, PH via your login), so I can post a "Show HN" and a Product Hunt launch.
- Why: Free launch channels; the "AI agent runs a business" angle plus a privacy-first tool suits both audiences.
- Cost: £0
- Exact text / link: Show HN: "Show HN: SantaDraw, a Secret Santa draw that stores nothing (run by an AI agent)" linking to https://race-claude-code.pages.dev with the same body as R-002.

## R-004 | 2026-11-06 | CLOSED (approved; see R-009)
- Action: Allow me to create ONE Cloudflare KV namespace named `race-claude-code-stats` and bind it only to the `race-claude-code` Pages project, to count visits, draws and reveals (anonymous counters, no personal data).
- Why: I currently have no way to measure visitors (Pages has no built-in analytics without account-level settings), so I can't report visitor numbers or see which pages work.
- Cost: £0 (free tier)
- Exact text / link: `npx wrangler kv namespace create race-claude-code-stats`

## R-005 | 2026-11-06 | CLOSED (approved; see R-011)
- Action: Buy the domain santadraw.co.uk (checked available today via Nominet RDAP) for 1 year at Porkbun, then add 2 DNS settings there: (1) CNAME record `www` → `race-claude-code.pages.dev`; (2) URL forward of the bare `santadraw.co.uk` → `https://www.santadraw.co.uk` (permanent). I will attach www.santadraw.co.uk to the race-claude-code Pages project myself and update all links.
- Why: The product works by sending private links to everyone in a WhatsApp group. "race-claude-code.pages.dev/reveal#..." looks like spam to a gran in a family chat; "santadraw.co.uk" looks trustworthy and is memorable, so more people open links and come back to start their own draw.
- Cost: about £6 (Porkbun .co.uk first-year price; please decline if over £10)
- Exact text / link: https://porkbun.com/checkout/search?q=santadraw.co.uk

## R-006 | 2026-11-06 | CLOSED (approved; see R-011)
- Action: Create a new Google account for SantaDraw (not one of yours) and give me its login as env vars GOOGLE_USERNAME / GOOGLE_PASSWORD, so I can add the site to Google Search Console (HTML-file verification, which I deploy myself) and submit the sitemap.
- Why: Secret Santa searches peak from mid-November. I've built 9 search-targeted pages and submitted them to Bing via IndexNow, but Google has no equivalent without Search Console, and Google is most UK searches.
- Cost: £0
- Exact text / link: https://search.google.com/search-console

## R-007 | 2026-11-07 | CLOSED (live restricted key installed 2026-11-09; sales open)
- Action: Follow-up to approved R-001. STRIPE_SECRET_KEY in my session is still a TEST key (starts sk_test_). Please put the LIVE secret key (sk_live_..., or a restricted key with Checkout Sessions write + read) into the STRIPE_SECRET_KEY repo secret. Everything else is ready: trader details, support email, refund policy and contact page are now live.
- Why: No real customer can pay until this is done. This is the single blocker for sales.
- Cost: £0
- Exact text / link: https://dashboard.stripe.com/apikeys (live mode)

## R-008 | 2026-11-07 | OPEN
- Action: Follow-up to approved R-002 / R-003. REDDIT_USERNAME, REDDIT_PASSWORD, HN_USERNAME and HN_PASSWORD exist in my session but are EMPTY. Please fill in the repo secrets once the accounts exist (post texts are unchanged from R-002 / R-003). If Reddit's login needs 2FA or a captcha, I can't post: then please post the R-002 text yourself in r/SideProject.
- Why: Launch posts are my only free distribution channel until Google indexes the site.
- Cost: £0
- Exact text / link: see R-002 and R-003.

## R-009 | 2026-11-07 | CLOSED (no longer needed: Cloudflare Web Analytics now gives visitor numbers)
- Action: Follow-up to approved R-004. My CLOUDFLARE_API_TOKEN can't create KV namespaces ("Authentication error 10000"). Please either add "Workers KV Storage: Edit" to the token, or create the namespace `race-claude-code-stats` yourself and bind it to the race-claude-code Pages project (Settings → Bindings → KV, variable name `STATS`, production).
- Why: I still can't count visitors or draws, so I can't tell which pages or channels work.
- Cost: £0
- Exact text / link: https://dash.cloudflare.com → My Profile → API Tokens

## R-010 | 2026-11-07 | OPEN
- Action: SUPPORT_EMAIL_PASSWORD is rejected by Gmail IMAP ("Invalid credentials"). Gmail needs a 16-character App Password (Google account → Security → 2-Step Verification on → App passwords). Please set that as SUPPORT_EMAIL_PASSWORD.
- Why: The support/refund email is now published on the site; I must be able to read and answer refund requests (refusing a refund is a disqualification).
- Cost: £0
- Exact text / link: https://myaccount.google.com/apppasswords

## R-011 | 2026-11-07 | OPEN
- Action: Follow-up to approved R-005 and R-006. (1) santadraw.co.uk doesn't resolve yet: please buy it (Porkbun, ~£6) and add the CNAME `www` → `race-claude-code.pages.dev` plus the forward from the bare domain, as in R-005. (2) No GOOGLE_USERNAME / GOOGLE_PASSWORD variables reach my session: please add them as repo secrets (and pass them to the workflow) for Search Console. If a Google login from a CI server is blocked, alternative: add the site in Search Console yourself with the "HTML tag" method and paste the tag content into a new request reply, I'll deploy it.
- Why: Trustworthy links in family WhatsApp chats, and Google indexing before searches peak in mid-November.
- Cost: about £6 (domain), already approved in R-005
- Exact text / link: https://porkbun.com/checkout/search?q=santadraw.co.uk · https://search.google.com/search-console

## R-012 | 2026-11-09 | OPEN
- Action: In the LIVE Stripe dashboard, set the public business name to "SantaDraw" (Settings → Business → Public details → Public business name) and the statement descriptor to "SANTADRAW". Optionally add the support email as the public support email there.
- Why: Live checkout works (thank you!), but the checkout page header says "race-claude-code". A buyer paying £2.49 to "race-claude-code" may think it's a scam and abandon. Their bank statement would show the same.
- Cost: £0
- Exact text / link: https://dashboard.stripe.com/settings/public

## R-013 | 2026-11-09 | OPEN
- Action: Spend up to £20 total on a Google Ads Search campaign for SantaDraw (purchase + new Google Ads account). If you'd rather I run it myself, put the account login in GOOGLE_USERNAME / GOOGLE_PASSWORD (R-011) and I'll set it up exactly as below.
  - Campaign: Search only (untick Display/Search partners), location United Kingdom, language English, daily budget £2, max CPC £0.30, total cap £20, ends 20 Dec.
  - Keywords (phrase match): "secret santa generator", "secret santa name generator", "secret santa draw", "secret santa picker", "online secret santa", "secret santa whatsapp", "secret santa with exclusions". Negative: "free" is NOT a negative (the free tier is real).
  - Ad: Final URL https://race-claude-code.pages.dev/?utm_source=google&utm_medium=cpc . Headlines: "Secret Santa Draw in 30 Seconds" / "No Sign-Up, No Emails Needed" / "Send Names by WhatsApp". Descriptions: "Draw names in your browser and send everyone a private link. Free for up to 6 people." / "Bigger groups, couples exclusions and wishlists with Pro, £2.49 one-off."
- Why: Day 4, live payments since today, but zero real visitors: the site isn't in Google or Bing yet and the Reddit/HN/Search Console credentials haven't arrived. Paid search on high-intent "secret santa generator" searches is the fastest way to put the product in front of organisers while the season is starting. 
- Cost: £20 maximum (of the £50 budget)
- Exact text / link: https://ads.google.com

## R-014 | 2026-11-11 | OPEN
- Action: One follow-up to approved R-010 (not re-requesting anything else). Gmail still rejects SUPPORT_EMAIL_PASSWORD today ("Invalid credentials"). The value in the secret is 10 characters long; a Gmail App Password is always 16 letters (shown as 4 groups of 4). Please either (a) turn on 2-Step Verification for the support Gmail account, create an App Password at the link below and put the 16 letters (spaces optional) in SUPPORT_EMAIL_PASSWORD, or (b) if that's awkward, point SUPPORT_EMAIL at any mailbox that allows IMAP with an app password (e.g. Yahoo/Outlook) and set its password. I check the login automatically at the start of every session.
- Why: Under OPERATOR.md, sales stay closed until the mailbox login works. Live Stripe checkout is ready and tested; this is the only thing stopping any customer from paying.
- Cost: £0
- Exact text / link: https://myaccount.google.com/apppasswords
