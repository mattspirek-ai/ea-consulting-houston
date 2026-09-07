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
