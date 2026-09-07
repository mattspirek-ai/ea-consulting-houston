# EA Consulting — Houston + Virtual Fractional Executive Assistant Business

Private archive for everything produced while planning and building a Houston-based fractional/virtual executive assistant (EA) services business with a national virtual footprint. The live working environment is Hyperagent; this repository is the durable, version-controlled backup and the record of what was done.

**Owner:** mattspirek-ai · **Started:** 2026-09-07 · **Source thread:** https://hyperagent.com/thread/cmtrpuzu61c3507ad27zn4poq

---

## What's in here

| Path | What it is | Regenerate with |
|---|---|---|
| `docs/strategy.md` | Market-entry strategy: ICP, positioning, offer ladder & pricing, competitive summary, GTM channels, 90-day plan, KPIs, risks | Edit the master Hyperagent document, then re-export |
| `docs/website-blueprint.md` | Page-by-page website blueprint: design direction, sitemap, page specs, conversion/trust features, SEO plan, stack, launch checklist | Same as above |
| `docs/build-brief.md` | Self-contained instruction file for an LLM (or human) builder to construct the website — ground rules, pricing to display, final slugs, page specs, acceptance criteria | Hand-authored; edit here |
| `docs/worklog.md` | **Append-only** dated log of every working session: what was asked, what was done, what was produced, what's open | Append a new entry every session |
| `docs/decisions.md` | Decision record so future sessions don't re-litigate settled choices | Append when a decision is made or reversed |
| `research/national_competitors.json` | 21 national virtual/fractional EA competitors with pricing, traffic estimates, positioning, features, weaknesses, sources | Re-run research (see worklog Session 1 for method) |
| `research/houston_competitors.json` | 17 Houston-metro competitors (agencies, solos, staffing firms), SERP snapshot, market observations, demand stats | Same |
| `research/demand_keywords_pricing.json` | 61 keywords, labor stats, 13 pricing benchmarks, pricing recommendations, buyer pain points/praise/objections/guarantees | Same |
| `data/EA_Houston_Virtual_Market_Research.xlsx.b64` | The 10-sheet Excel workbook, base64-encoded (the GitHub integration used to push cannot commit binary files). Decode: `base64 -d data/EA_Houston_Virtual_Market_Research.xlsx.b64 > data/EA_Houston_Virtual_Market_Research.xlsx`. Sheets: Competitors, Keywords, Pricing, Pricing Recommendation, Buyer Signals, Houston Demand, SERP Snapshot, Gaps & Positioning, Sources, README. | `cd scripts && python3 build_workbook.py` |
| `site-concepts/{a-editorial-boutique,b-conversion-landing,c-pricing-first}/index.html` | Three complete single-file website prototypes (different structure and register) built from `docs/build-brief.md`; see `site-concepts/README.md` for the comparison and recommended combination | Hand-built; edit here |
| `docs/linkedin/playbook.md` | LinkedIn operating manual: pillars, formats, hooks, cadence, engagement routine, profile optimization, scorecard, hard rules, sourced algorithm notes | Hand-authored; edit here |
| `docs/linkedin/post-bank.json` + `post-bank.md` | 60 validated, tagged posts (JSON is source of truth; MD is the rendering) | Edit JSON; re-render MD |
| `docs/linkedin/calendar-first-30-days.md` | Day-by-day first-30-days plan | `node scripts/linkedin/build_calendar.mjs --start YYYY-MM-DD --weeks N` |
| `scripts/linkedin/post_scaffold.mjs`, `build_calendar.mjs` | Zero-dependency Node tools to scaffold posts and build calendars from the bank | — |
| `report/index.html` | Self-contained interactive market analysis page (charts via ECharts CDN) | `cd scripts && python3 build_report.py` |
| `scripts/build_workbook.py` | Builds the workbook from `research/*.json` (needs `openpyxl`) | — |
| `scripts/build_report.py` | Builds `report/index.html` from `research/*.json` | — |

## How to regenerate deliverables

```bash
pip install openpyxl          # only dependency
cd scripts
python3 build_workbook.py     # writes ../data/EA_Houston_Virtual_Market_Research.xlsx (identical to decoding the .b64)
python3 build_report.py       # writes ../report/index.html
```
Both scripts read only from `../research/*.json`. If you correct a fact, correct it in the JSON and rebuild — don't hand-edit the workbook or HTML.

## How to read the numbers (important)

- **Traffic figures are approximate** third-party estimates (Exa entity data, ~June 2026 snapshot). Several major brands (Boldly, Zirtual, Athena, Double, Magic) and all Houston-local sites have no estimate.
- **Keyword search volumes are all `null`.** No free public tool returned numbers during research. Pull the 61 terms through Google Keyword Planner before locking SEO priorities. Nothing was guessed.
- **"Who ranks now" is based on the Exa search index**, not a live Google SERP or Maps pack.
- **One stat is flagged unverified:** the "547 employed" Houston EA figure (SalaryMetro citing BLS, SOC 43-6014) looks wrong. Verify against BLS OEWS Houston May 2024 before using anywhere.
- **Pricing recommendations are derived**, not sourced — they're labeled as such in the workbook and strategy.
- Every sourced number carries a URL and pull date. `null` / "not available" means exactly that.

## Working rules for this project

1. **Every session ends with a worklog entry** in `docs/worklog.md` (date, request, actions, outputs, open items) and a commit of any new or changed files.
2. **Decisions go in `docs/decisions.md`** — append, don't rewrite. Reversals get a new dated entry.
3. **Corrections are appended, never silently edited.** If a research fact changes, add a `corrections` note in the relevant JSON and a worklog line.
4. **No fabricated proof, ever** — no invented testimonials, logos, review counts, or statistics in any deliverable or on the website.
5. **Licensing:** dependencies and assets must be MIT/Apache/BSD or equivalent; no GPL/AGPL/CC-BY-SA. Node-first stack for anything in a request path.
6. **Spreadsheets are delivered as `.xlsx`**, never CSV.

## Live artifacts on Hyperagent (masters)

- Skill: "EA LinkedIn Content" (mirrors docs/linkedin + scripts/linkedin)

- Strategy document: `cmtrqfnvz0uiz07adjtaatncl`
- Website Blueprint document: `cmtrqhbjh0syh06ad7l8t4v4v`
- Published report: https://pub.hyperagent.com/p/BLWvqTNIFXo4ZbVFsa2s5ykyBY57TxgGAZ9RjBqrJMk
- Thread: https://hyperagent.com/thread/cmtrpuzu61c3507ad27zn4poq

## Status

See `docs/worklog.md` for the latest session and `docs/decisions.md` for what's settled. Next planned steps are listed at the end of the most recent worklog entry.

---
Private repository. All rights reserved by the owner. Not licensed for redistribution.
