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

## R-001 | 2026-11-05 | OPEN
- Action: Fix the Cloudflare API token so it can deploy to Pages project `race-claude-code` (setup issue, not a purchase).
- Why: Dry-run deploy failed. The token is an active account-scoped token (`/accounts/{id}/tokens/verify` returns active), but `GET /accounts/{id}/pages/projects/race-claude-code` returns 10000 "Authentication error". wrangler 4.x fails with 9109 "Invalid access token" on `/accounts`, and wrangler@latest gets a 500 on `/user/tokens/verify`. Likely cause: the token is missing "Account > Cloudflare Pages > Edit", or the project doesn't exist yet.
- Cost: £0
- Exact text / link: n/a
