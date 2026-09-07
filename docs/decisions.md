# Decision Record — EA Consulting (Houston + Virtual)

Append-only. Each decision gets an ID, date, the decision, the reasoning, and what would cause it to be revisited. Reversals are new entries that reference the original ID.

---

## D-001 · 2026-09-07 · Business model
**Decision:** The business is a fractional/virtual executive assistant *services* firm for executives — not EA training/consulting, not a staffing/placement agency.
**Why:** Owner's stated intent (confirmed in Session 1 clarifying questions). Determines the competitor set (Boldly/BELAY/Delegate Solutions tier, not Murray/Burnett/Robert Half).
**Revisit if:** the owner wants to add placement or training as revenue lines.

## D-002 · 2026-09-07 · Category language
**Decision:** Lead with "fractional executive assistant"; use "virtual executive assistant" as the SEO secondary; avoid leading with "virtual assistant".
**Why:** "Virtual assistant" pulls the brand into the $7–16/hr offshore comparison set (Wing, Magic, Philippines freelance). "Fractional EA" is where Boldly/Delegate Solutions price.
**Revisit if:** keyword volume data (still to be pulled) shows "fractional" is too small to matter for search.

## D-003 · 2026-09-07 · Positioning
**Decision:** Houston-rooted · senior US-based industry-fluent EAs (energy, healthcare/TMC, legal, private capital) · radically transparent terms (published pricing, month-to-month, no buyout fee, 1-month hour rollover) · delegation done with you (30-Day Delegation Playbook). Optional Houston in-person day add-on.
**Why:** Each pillar maps to a gap found empty in Session 1 research: no national player has local presence; buyers complain about pricing opacity (BELAY), 12-month lock-in, $10–20K buyout fees, and lack of industry vocabulary; premium services still leave clients to figure out what to delegate.
**Revisit if:** a national player launches Houston pages/in-person option, or early sales calls show buyers don't value local presence.

## D-004 · 2026-09-07 · Pricing — Option A (premium boutique)
**Decision:** Launch tiers: Foundation 20 hrs $1,200 · Executive 40 hrs $2,300 · Chief of Staff 60 hrs $3,300. Add-ons: in-person day $450, extra hours $65/hr, specialist work $79/hr, onboarding $299 (waived on top tier). Terms: month-to-month, 2-week satisfaction guarantee, 1-month rollover, no buyout fee, replacement in 5 business days.
**Why:** Sits below Boldly ($65/hr) and Delegate Solutions ($88–92/hr), above BELAY's estimated $42–50/hr, and far below the ~$8,250/mo derived cost of an in-house Houston EA. Transparency vs BELAY is the wedge. Option B (mid-market $900/$1,800/$2,600) is documented in the workbook as a fallback only.
**Margin caveat:** 22–40% gross margin with senior 1099 talent at $32–38/hr. If launching W-2, consider $65/hr parity with Boldly instead.
**Revisit if:** <3 paying clients after ≥40 discovery calls by day 90 (kill criterion), or legal review forces a conversion fee in place of "no buyout fee".

## D-005 · 2026-09-07 · Deliverable formats
**Decision:** Spreadsheets are delivered as `.xlsx` (never CSV). Interactive analysis as a published webpage. Strategy and blueprint as editable Hyperagent documents with markdown exports in this repo. Builder handoff as a self-contained markdown brief.
**Why:** Owner's standing preferences and the request for an LLM-readable handoff file.

## D-006 · 2026-09-07 · Data honesty rules
**Decision:** Every estimate is labeled approximate with source URL and pull date. Missing data is `null` / "not available" — never estimated or filled with a neutral value. Recommendations derived from data are labeled as derived. Corrections are appended as dated entries, never silent edits.
**Why:** Owner's standing editorial rules for analytics outputs; keeps claims falsifiable.

## D-007 · 2026-09-07 · Website stack
**Decision:** Node-first: Next.js (App Router) or Astro + Tailwind, MDX content in-repo, Cal.com/Calendly embed, Cloudflare Pages (or Vercel) + Cloudflare DNS/WAF, GA4 + Search Console, client-side pricing calculator. Only MIT/Apache/BSD-licensed dependencies; no GPL/AGPL/CC-BY-SA; no Wix/Ueni/Squarespace.
**Why:** Owner's licensing and stack constraints; the local competitor tier is template builders and the site must clear that bar cheaply.

## D-008 · 2026-09-07 · Archive location and cadence
**Decision:** This private repository (`mattspirek-ai/ea-consulting-houston`) is the durable archive. Every working session ends with a `docs/worklog.md` entry and a commit of changed files. Hyperagent documents remain the editable masters; exports here are re-generated when they change.
**Why:** Owner wants everything built archived as markdown/source in a private GitHub repo in addition to living in the platform.
**Note:** The connected GitHub integration cannot create repositories (403); repo creation is a manual owner step. Pushes and updates work through the integration.
