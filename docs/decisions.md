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

## D-009 · 2026-09-07 · Website: three concept formats before committing to a build
**Decision:** Build three complete single-file prototypes with different structure and register — A editorial boutique (multi-section home), B single-page conversion landing (calculator-first), C pricing-first transparency site — from the same `build-brief.md`, then choose or combine. Intended combination: A as the site shell, B's calculator-first pattern on the Houston hub/ad landing, C's comparison table and changelog as `/pricing`.
**Why:** Owner asked for multiple website formats; the research shows two distinct buyer entry points (local trust vs price-comparison intent) that a single page serves poorly.
**Revisit if:** early traffic shows one entry point dominates.

## D-010 · 2026-09-07 · LinkedIn is the primary launch channel and gets a content system
**Decision:** Founder-led LinkedIn posting 3–5×/week is the #1 GTM channel for the first 90 days (per strategy.md). A repeatable content system lives in `docs/linkedin/` (playbook, 60-post bank as JSON + markdown, 30-day calendar) with zero-dependency Node scripts in `scripts/linkedin/`, and is mirrored as a Hyperagent skill so future sessions can generate posts consistently.
**Content rules:** no invented client stories or metrics — composites must be labeled composites; competitor claims only with sourced facts (source in comments); pricing mentions match the published tiers exactly; chief-of-staff voice, no influencer filler.
**Why:** The Houston fractional-EA conversation currently lives on LinkedIn among solo operators; national brands are absent locally; the founder's credibility is the product's proof until real client metrics exist.
**Revisit if:** 60 days of consistent posting yields no fit calls — then shift weight to referral partners.

## D-011 · 2026-09-07 · Subagent model
**Decision:** All delegated work (research, builds, writing) runs on the owner's default subagent model, Fable. Session 2's first three website concept builds were dispatched on Sonnet by mistake; they were discarded and rebuilt on Fable at the owner's instruction.
**Why:** Owner's explicit preference; judgment quality on design and copy is the point of these builds.

## D-012 · 2026-09-07 · Concept D: replicate Athena's paid-landing-page format
**Decision:** Build a fourth website concept that copies the *format* of athena.com/cl/nb-executive-assistant almost exactly — section order, layout patterns, component shapes, alternating dark/light band rhythm, single repeated CTA — re-skinned to our tokens (navy/paper/brass) and filled with our positioning, published pricing, and original copy. Reference captured 2026-09-07 (full-page screenshot, computed styles, component inventory) and translated in `docs/athena-format-spec.md`.
**Boundaries:** layout and structure only. No Athena copy, logos, photos, client names, statistics, or certifications. Their client-logo strip and stat bands become labeled placeholders, terms statements, or sourced/derived figures with sources in the footer. Testimonials remain placeholders until real.
**Why:** Owner's explicit instruction ("make it like this site, copy almost exactly the same format"). Athena is the traffic-and-conversion benchmark in the category; its paid landing page is a proven conversion structure. Our advantage over it (Houston presence, US talent, published month-to-month pricing, no lock-in) is expressed inside their proven format.
**Revisit if:** legal review flags trade-dress concerns about the visual resemblance — in which case keep the section order and swap the component styling further.
