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
