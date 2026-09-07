# Worklog — EA Consulting (Houston + Virtual)

Append-only. One entry per working session, newest at the bottom. Never edit a past entry; add a correction line in a new entry instead.

Format:
```
## YYYY-MM-DD — Session N — short title
**Requested:** what the owner asked for
**Done:** what actually happened, including dead ends
**Produced:** files/artifacts with paths or IDs
**Data quality notes:** anything approximate, missing, or unverified
**Open items / next steps:** what's pending
```

---

## 2026-09-07 — Session 1 — Market research package + GitHub archive

**Requested:**
1. Research the top administrative/executive assistant websites driving the most traffic; a full Houston-market and virtual-market competitive analysis — "the whole package" for someone starting an EA consulting business who will also build a website.
2. Clarified with the owner: business model = fractional/virtual EA services for executives (not training, not staffing); include both traffic estimates (flagged approximate) and SEO/positioning analysis; deliver as an interactive webpage report, an Excel workbook, an editable strategy document, a website blueprint, and an agent-handoff markdown for a future LLM builder.
3. Then: save everything to a private GitHub repo with clear documentation, and keep documenting all future work there.

**Done:**
- Planned in the Hyperagent working doc; plan approved by owner.
- Ran three parallel research subagents (Exa search/contents; browser only where needed):
  - National virtual/fractional EA competitors — 21 profiled (BELAY, Boldly, Prialto, Zirtual, Athena, Double, Wing, Magic, Worxbee, Persona, MyOutDesk, Virtual Gurus, Squared Away, Time etc, Fancy Hands, Assist World, Viva/ExecViva, Priority VA*, Assistantly*, Equivity*, Great Assistant*). *Not retrievable; Equivity returned 404. Delegate Solutions added later from pricing research.
  - Houston-metro competitors — 17 profiled in three groups: A) Houston agencies / Houston-targeted landing pages (Robert Lee & Associates, EntreAdmin, JDK Virtuals, Sky Virtual Solutions, VirtualEZ, Virtual Synergy, ExecViva Houston page, Vera Outsourcing, Executive Virtual Associates); B) solo operators (BusbyLife/Mickey B., Handled by Halee, Anna Baker, Lara Kuhleman-Valdez); C) staffing/placement (Murray Resources, Burnett Specialists, Frontline Source Group, Robert Half). Google Places API was unavailable — Maps pack not captured.
  - Demand/keywords/pricing/buyer signals — 61 keywords in 7 clusters; BLS/Indeed/Robert Half labor stats; 13 sourced price points; pricing recommendation options A (premium boutique) and B (mid-market); 18 pain points, 7 praise points, 10 objections, 5 guarantees from Trustpilot/Indeed/review articles.
- Normalized into one competitor schema; built the workbook (10 sheets, 39 competitor rows, 123 deduplicated source URLs) with `scripts/build_workbook.py`.
- Wrote the Strategy document and Website Blueprint document on Hyperagent; exported both to `docs/`.
- Wrote `docs/build-brief.md` (LLM builder handoff with acceptance criteria).
- Built and published the interactive report (`report/index.html`); render health check passed (no console errors or failed requests).
- GitHub archive: `github__create_repository` returned **403 "Resource not accessible by integration"** — the connected GitHub app cannot create repositories. Owner widened the app's repository access to "All repositories" (visible repos went from 3 to 13) but creation still failed — the app lacks the Administration permission, which only the app developer can grant. Owner created the empty private repo `ea-consulting-houston` manually at github.com; all files were then pushed through the integration. The .xlsx is committed as a base64 sidecar because the integration only accepts text content.

**Produced:**
- `data/EA_Houston_Virtual_Market_Research.xlsx`
- `docs/strategy.md`, `docs/website-blueprint.md`, `docs/build-brief.md`, `docs/decisions.md`, this worklog
- `research/national_competitors.json`, `research/houston_competitors.json`, `research/demand_keywords_pricing.json`
- `report/index.html` (published copy: https://pub.hyperagent.com/p/BLWvqTNIFXo4ZbVFsa2s5ykyBY57TxgGAZ9RjBqrJMk)
- `scripts/build_workbook.py`, `scripts/build_report.py`

**Key findings (short):**
- Traffic leaders (approx. monthly visits, Exa ~Jun 2026): Wing ~173K (offshore), BELAY ~127K (US, unpublished pricing, 12-mo contracts), ExecViva ~60K, Burnett Specialists (Houston staffing) ~50K, Prialto ~36K, MyOutDesk ~29K, Assist World ~22K, Murray Resources ~21K.
- US-based premium fractional EA has a hard floor ~$2,600/mo (Boldly $65/hr flat); Delegate Solutions $88–92/hr; BELAY est. $42–50/hr; offshore managed $7–16/hr effective.
- Houston: only two verifiable local EA agencies with real websites (both template builders, no pricing); solos are LinkedIn-only; staffing firms are strong but place W-2 in-person hires. No competitor is positioned as Houston-based + US talent + published pricing + industry-fluent.
- Recommended position and Option A pricing ($1,200 / $2,300 / $3,300 for 20/40/60 hrs) recorded in `docs/decisions.md`.

**Data quality notes:**
- All keyword volumes null (no free tool returned numbers) — pull via Google Keyword Planner.
- Domain ratings null throughout.
- "547 employed" Houston EA stat (SalaryMetro, SOC 43-6014) unverified and likely wrong — excluded from the report, flagged in workbook.
- Traffic missing for Boldly, Zirtual, Athena, Double, Magic, and all Houston-local sites.

**Open items / next steps:**
- Pull Google Keyword Planner volumes for the 61 keywords; update `research/demand_keywords_pricing.json` and rebuild.
- Verify Houston BLS OEWS wage/employment figures.
- Decide brand name; replace `[BrandName]` placeholder across docs.
- Build the website from `docs/build-brief.md` (Home, Pricing with calculator, Houston hub first).
- Optional: set up a live-mode agent to re-check competitor pricing pages and Houston SERPs periodically and append dated changes here.

---

## 2026-09-07 — Session 2 — Website concept formats (×3) + LinkedIn content system

**Requested:**
1. "Build multiple types of website formats" — several genuinely different website concepts for the same business so the owner can choose a direction.
2. Owner correction: the first three concept builds ran on Sonnet; redo them on Fable (owner's default subagent model). Done — Sonnet builds discarded, all three rebuilt on Fable.
3. "Include LinkedIn posting content skills for EA — they will be looking to post a lot of content on LinkedIn." A repeatable content system, not a one-off list.

**Done:**
- Three complete single-file website prototypes built on Fable from `docs/build-brief.md`, each with a working pricing calculator (hours/week × 4.33 → smallest covering tier, else Chief of Staff + $65/hr overflow), sourced competitor comparison with "last verified 2026-09-07", JSON-LD, labeled placeholders only (no fabricated proof), single `BRANDNAME` const:
  - A `site-concepts/a-editorial-boutique/index.html` (1,225 lines) — navy/paper/brass, Fraunces + Inter, full multi-section home page per brief §4. Published; render check passed.
  - B `site-concepts/b-conversion-landing/index.html` (1,052 lines) — single long scroll, calculator directly under hero, teal accent, Manrope + Inter, sticky mobile CTA, GA4 event hooks. Published; render check passed. Builder note: with the brief's exact formula, 5 hrs/wk = 21.65 hrs/mo so the slider never recommends Foundation; consider starting the slider at 4.
  - C `site-concepts/c-pricing-first/index.html` (1,089 lines) — the home page IS the pricing page: 12-column sourced comparison table, ECharts effective-$/hr chart with CDN-failure fallback, cost model with breakeven (~136 hrs/mo → hire in-house), pricing changelog. Published; render check passed. Builder flagged the Worxbee $2,760/40h figure — it is sourced in `research/national_competitors.json` (price_low_usd 2760, 40-hr plan), so it stands; re-verify on worxbee.com before launch.
  - `site-concepts/README.md` compares the three and recommends the combination: A as site shell, B pattern for Houston hub / ad landing, C table + changelog as `/pricing`.
- LinkedIn content system (Fable subagent; short sourced research pass on 2025–2026 LinkedIn format/algorithm evidence):
  - `docs/linkedin/playbook.md` (355 lines): KPIs, audience, voice + banned patterns, six pillars mapped to positioning pillars and buyer pain points, eight formats with templates, 40-hook library, sourced algorithm notes, cadence/weekly rhythm, daily 20-minute engagement routine, profile/page optimization, weekly scorecard, hard rules, source appendix.
  - `docs/linkedin/post-bank.json` + `post-bank.md`: 60 posts (10/pillar; 20 Houston-specific; 13 sector-specific), every dirty-laundry post carries source URLs and "(source in comments)"; anecdotes are `[INSERT: … do not invent]` placeholders or labeled composites; pricing strings match the brief exactly (validated programmatically).
  - `docs/linkedin/calendar-first-30-days.md`: day-by-day Sep 7 → Oct 6 with engagement tasks and weekly reviews.
  - `scripts/linkedin/post_scaffold.mjs` (--list / --pillar / --format / --sector / --seed) and `scripts/linkedin/build_calendar.mjs` (--start / --weeks / --posts-per-week / --exclude / --json), Node ≥18, zero deps, tested. Patched to resolve the post bank via env `POST_BANK`, a sibling copy, or the repo path — so the same files run inside the Hyperagent skill.
  - Mirrored as Hyperagent skill "EA LinkedIn Content" (playbook as documentation; scripts + post bank attached).
- Decisions appended: D-009 (three concept formats), D-010 (LinkedIn primary channel + content rules), D-011 (Fable for all subagent work).

**Produced:** files listed above; published artifacts for concepts A, B, C on Hyperagent (see thread).

**Data quality notes:**
- LinkedIn algorithm/format claims are from third-party studies and practitioner posts (2025–2026), cited with dates in the playbook appendix; anecdotal items are flagged as such. Posting-time guidance is explicitly labeled a weak-evidence lever.
- No engagement benchmarks were invented; "working" at 30/60/90 days is defined against the founder's own baseline.
- Worxbee $2,760/40h: sourced in national_competitors.json; re-verify on worxbee.com before it appears on a live page.

**Open items / next steps:**
- Owner picks a concept (or the recommended combination) → build the full multi-page site from `docs/build-brief.md`.
- Replace `BRANDNAME` and all `[PLACEHOLDER]`s; decide slider floor (4 vs 5 hrs/wk) for concept B.
- Still open from Session 1: Google Keyword Planner volumes; BLS OEWS Houston verification; brand name.
- Start the LinkedIn calendar (Week 1 setup tasks are dated Sep 7; shift dates with `build_calendar.mjs --start` if launch slips).

---

## 2026-09-07 — Session 3 — Concept D: Athena-format paid landing page

**Requested:** "Make it like this site, copy almost exactly the same format" — athena.com/cl/nb-executive-assistant (their paid-search landing page). Then: wrap up (owner low on tokens).

**Done:**
- Captured the reference in a real browser: full-page screenshot (1265×8051), section offsets, computed styles (Playfair Display + Figtree; deep-forest/limestone bands; pill eyebrows; ghost arrow buttons; 20/15/8px card radii), component inventory (role-picker widget, logo strip, tabbed delegation list, 3-step columns, battlecards, security grid, pricing card, testimonial carousel, FAQ, full-bleed CTA). Crops kept locally in /agent/workspace/ref/ (not committed — binaries).
- Wrote `docs/athena-format-spec.md`: section-by-section format translation to our tokens (navy pair + warm paper + brass) and content rules. Format only — no Athena copy, logos, photos, names, stats, or certifications.
- Built `site-concepts/d-athena-format/index.html` on Fable (1,141 lines): all 10 sections matched to the reference; deviations logged by the builder (hero left column widened for our longer H1; battlecard ~900px vs ~1000px; logo strip = sector words placeholder; stat bands = terms statement / derived $8,250 comparison / metric placeholders; added self-hosted booking form and a Sources footer with last-verified dates). Interaction-tested at 1280px and 390px; JS and JSON-LD validated. Published as a Hyperagent artifact.
- Decision D-012 appended; `site-concepts/README.md` extended to four concepts.

**Produced:** `docs/athena-format-spec.md`, `site-concepts/d-athena-format/index.html`, updated `site-concepts/README.md`, `docs/decisions.md` (D-012), this entry.

**Data quality notes:** No new data. Competitor anchors unchanged (last verified 2026-09-07). Trade-dress caution recorded in D-012.

**Open items / next steps:**
- Owner chooses: D as the paid landing + A as the organic site (recommended), or D alone to start.
- Fill placeholders (brand, address/phone, testimonials, photos, logos with permission, scheduler embed, legal pages).
- Carry-overs: Keyword Planner volumes; BLS OEWS verification; brand name; concept B slider floor; Worxbee price re-verify.

---

## 2026-09-07 — Session 4 — Verified ICP prospect list (100+) in `prospects/`

**Requested:** "Based on the ea-consulting-houston research, find 100+ verified ICP clients with contact information that need this type of work… verified to maximum scrutiny… expand outside Houston metro if needed… save a subfolder in the repo." Clarified with the owner: contacts must be verified emails **and** phone numbers; expansion geography = DFW, Austin, San Antonio only if Houston falls short. Session closed under a budget cap at the owner's instruction ($70 remaining); wrap-up plan approved.

**Done:**
- Wrote `prospects/SCHEMA.md` (ICP from strategy.md, hard data rules, row schema) and dispatched eight parallel research segments on the owner's default subagent model: Houston EA-hiring signals, legal, healthcare/TMC, private capital, energy, growth/funded, professional services, Texas expansion. Seven wrote output (202 candidate rows, 169 researcher-rejected with reasons); the **Houston EA-hiring segment was stopped before writing** and is the top follow-up.
- Built a deterministic verifier (`prospects/scripts/verify_prospects.py`) that re-fetches every cited page and applies eight gates (website live; surname on an official page; two independent title sources; phone found on the company's own pages incl. `tel:` links; email published on an official page + MX via DNS-over-HTTPS + not free-mail; trigger URL reachable; metro in scope; size band 5–150). Added script-side discovery of `mailto:`/`tel:` links and Cloudflare-obfuscated emails on company pages (recorded with page URL as source, tagged `verifier_scan_2026-09-07`), and a patch-merge step for enrichment that can only add sourced values.
- First full pass: 96 Verified / 199 deduped. Ran one bounded contact-enrichment subagent (≈23 tool calls) on the 48 rows failing only the phone/email gates → 24 patches (12 phones, mostly SEC Form ADV Item 1.F and company sites; 16 emails, 4 named). Verifier refused 4 patched addresses as non-outreach channels (privacy/opt-out aliases, one third-party IR-agency inbox).
- Final: **107 Verified · 86 Partially Verified · 178 Rejected** (incl. 169 researcher rejections and 3 duplicates). Verified mix — metro: Houston 86, Austin 9, DFW 8, San Antonio 4; vertical: legal 31, private capital 18, healthcare 17, professional services 15, energy 11, other 9, tech 6; trigger: growth_list 23, new_launch 18, leadership_expansion 15, funding 11, hiring_ea 10, acquisition 5, other 25; tier: Executive 56, Chief of Staff 26, Foundation 25; named decision-maker email published on 34 rows, general business inbox on the rest.
- Built the workbook (`build_workbook.py`: README, Verified, Partially Verified, Rejected, Sources, Segments) and generated `verification-log.md` (append-only) and `outreach-segments.md` (Wave 1 hiring-EA → Wave 2 named email → Wave 3 general inbox + LinkedIn; by tier) with `write_reports.py`.
- Skipped under budget (logged in `prospects/README.md` → Coverage note): browser spot-check of 8 bot-blocked sites + 6 JS-only Houston law firms; source-corroboration enrichment for rows failing G2/G3/G6; the Houston EA-hiring segment.
- Decision D-013 appended (signal-led sourcing + eight-gate verification standard + contact-data policy).

**Produced:** `prospects/README.md`, `prospects/SCHEMA.md`, `prospects/prospects.xlsx.b64` (+ `prospects.json`), `prospects/raw/*.json` (7 segments), `prospects/raw/patches/contacts.json`, `prospects/verify/{verified,partial,rejected,checks}.json`, `prospects/verification-log.md`, `prospects/outreach-segments.md`, `prospects/scripts/{verify_prospects.py,build_workbook.py,write_reports.py}`, `prospects/scripts/researcher_helpers/energy_build.py`, `docs/decisions.md` (D-013), this entry.

**Data quality notes:**
- "Verified email" = published on an official page + MX present. **No SMTP mailbox probing** (no SMTP egress from the build environment). Run a deliverability check before any campaign and append results as a dated column.
- 39 Verified/Partial rows have `null` employee counts (not published; not estimated). 7 Verified rows carry a `size risk` note (LinkedIn band 51–200) — confirm headcount before pitching.
- Trigger `other` (25 Verified rows) means no dated 2024–2026 event was found; fit rests on the ICP profile alone.
- Two Verified emails are on a different domain than the website (legacy/hyphenated mail domains) — verified on-page, flagged in Verification notes.
- 21 Texas-expansion rows in Verified are virtual-only prospects; do not offer the in-person add-on.
- Prospect data decays fast; treat anything older than 60 days as unverified and re-run the two scripts.

**Open items / next steps:**
- Re-run the `hiring_ea_houston` segment (highest intent; only 10 hiring_ea rows made Verified, most from Texas expansion).
- Browser spot-check the bot-blocked/JS-only sites (targets in `prospects/verify/targets_browser.json`); source-corroboration pass on `targets_sources.json`.
- Optional: deliverability check on the 107 emails; Google Business Profile phone cross-check.
- Carry-overs from Sessions 1–3: Keyword Planner volumes; BLS OEWS verification; brand name; concept choice and placeholder fill.
