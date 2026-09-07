# prospects/ — Verified ICP Prospect List

> Session 3 deliverable (2026-09-07). A sourced, script-verified list of companies and decision-makers matching the ICP in `docs/strategy.md`, for founder-led LinkedIn and referral outreach (GTM channels 1–2). **Nothing here has been contacted.** Outreach is a human action.

## What is in this folder

| Path | What it is |
|---|---|
| `prospects.xlsx.b64` | The deliverable workbook (base64 sidecar — see decode command below). Sheets: README, Verified, Partially Verified, Rejected, Sources, Segments |
| `prospects.json` | Same data as the workbook, machine-readable, with the full per-row verification block |
| `SCHEMA.md` | The research brief and row schema every researcher worked from |
| `raw/*.json` | Untouched researcher output, one file per segment, with per-field source URLs |
| `verify/verified.json`, `verify/partial.json`, `verify/rejected.json` | Verifier output by status |
| `verify/checks.json` | Per-row gate results and evidence (audit trail) |
| `verification-log.md` | What the verifier did, counts, failure histogram, spot-check results |
| `outreach-segments.md` | Who to pitch first, by vertical, trigger, and suggested tier |
| `scripts/verify_prospects.py` | The verification pass (Python 3, `requests` only) |
| `scripts/build_workbook.py` | Builds the .xlsx, .json and .b64 from `verify/` (Python 3, `openpyxl`) |

Decode the workbook:

```bash
base64 -d prospects/prospects.xlsx.b64 > prospects/prospects.xlsx
```

Regenerate everything from raw research:

```bash
python3 prospects/scripts/verify_prospects.py && python3 prospects/scripts/build_workbook.py
```

## How prospects were sourced

Signal-led, not directory-scraped. Eight parallel research segments, each with a quantity target and a source list:

| Segment | Signal / population | Why it fits the ICP |
|---|---|---|
| `hiring_ea_houston` | Houston companies currently advertising an EA / EA-to-CEO role | Strongest possible signal: they need the work now and face a 4–8 week W-2 search |
| `legal_houston` | Boutique and mid-size law firms, managing / founding partners | Partner-level individuals without dedicated support; attorney bios publish direct email + phone |
| `healthcare_houston` | Physician-owned groups, ASCs, DPC, med-spa, TMC health-tech founders | Physician-executive / clinic-owner ICP row |
| `private_capital_houston` | LMM PE, independent sponsors, family offices, RIAs (Form ADV) | PE / family-office principal ICP row; Form ADV is an authoritative source |
| `energy_houston` | 10–150-employee E&P, minerals, midstream, OFS, energy-transition startups | Energy VP/GM ICP row; the "my VA doesn't understand oil and gas" complaint |
| `growth_funded_houston` | HBJ Fast 100, Inc 5000 Houston, funded founder-led companies | Trigger events: funding, acquisition, growth |
| `profservices_houston` | CPA, consulting, engineering, architecture, CRE, boutique IB principals | Managing-partner ICP row; partner bios publish contact data |
| `texas_expansion` | Same mix across DFW, Austin, San Antonio | Approved fallback geography (user decision 2026-09-07) |

Anti-ICP exclusions were applied at research time: solopreneurs, >150 employees, Fortune 500 HQs, staffing agencies, virtual-assistant firms (competitors), bookkeeping/marketing-primary needs.

## Verification standard ("maximum scrutiny")

A row is **Verified** only when all six hard gates pass; G7–G8 are fatal filters.

| Gate | Test | Method |
|---|---|---|
| G1 | Website live | GET with redirects, final status < 400. Bot-blocked responses (401/403/429/503/CAPTCHA) are marked `blocked` and sent to a browser spot-check — never auto-passed |
| G2 | Decision-maker is real and current | Surname found on at least one fetched official (non-LinkedIn) page: company team page, bio, Form ADV, bar directory, press |
| G3 | Title corroborated | ≥2 `title_sources` on distinct domains, each fetchable or a well-formed `linkedin.com/in/` URL |
| G4 | Phone verified | 10-digit number, in formatted form, found on the company website (home/contact/about/team pages) or the cited source page |
| G5 | Email verified | Address (named direct preferred, else published company address) found on the cited page or company site **and** the domain publishes MX records (DNS-over-HTTPS to 1.1.1.1) **and** not a free-mail domain unless the company itself runs on one |
| G6 | Trigger sourced | Trigger URL reachable and trigger detail present |
| G7 | Metro in scope | Houston, DFW, Austin, San Antonio |
| G8 | Size band | Employee estimate overlaps 5–150; `null` allowed and flagged, never estimated |

**Known limit:** the build environment has no SMTP egress, so mailbox-level verification (SMTP RCPT probing) was not performed. G5 is publication + MX evidence. If a bounce-tested list is needed, run the Verified emails through a deliverability service before a campaign and append the result as a new dated column — do not overwrite.

**Contact-data policy:** only publicly published business channels — company main lines, direct lines and emails printed on official bios, general contact addresses, public LinkedIn profile URLs. No personal cell numbers, no home addresses, no pattern-guessed emails.

**Data honesty (D-006):** every value carries a source URL (Sources sheet); missing values are `null`; rows that fail are kept in Rejected / Partially Verified with the reason, never dropped or filled.

## Counts

See `verification-log.md` for the final counts, the failure histogram, and the spot-check record for this pull.

## Coverage note for the 2026-09-07 pull (read before relying on the list)

The session was closed under a budget cap. Seven of the eight planned research segments completed. What did **not** run, and is therefore an open follow-up rather than a finding:

- **`hiring_ea_houston` segment never wrote output.** Houston companies currently advertising an EA role — the highest-intent population — are represented only by the `hiring_ea` rows that other segments happened to find (healthcare, legal, professional services, and the Texas-expansion segment). Re-run this segment first in the next session.
- **Browser spot-check did not run.** Rows whose sites bot-blocked the HTTP verifier (HTTP 202/403/challenge pages) remain Partially Verified with a `G1 website bot-blocked` reason; six JS-only Houston law firms flagged by the legal researcher (Markovich Grover, HTX Venture Legal, Smyser Kaplan & Veselka, Schiffer Hicks Johnson, Diggs & Sadler, Hoover Slovacek) are in Rejected awaiting a browser read.
- **Source-corroboration enrichment did not run.** Rows failing only G2/G3/G6 (name not found on an official page, one title source, or a dead trigger URL) were not worked; they sit in Partially Verified with the gate named.
- **Contact enrichment ran once, bounded** (≈40 tool calls) on rows failing only the phone/email gates; its patches are in `raw/patches/contacts.json`.

None of these gaps affects the Verified sheet's integrity — every Verified row passed all gates on re-fetch — but they cap the count and skew the mix toward segments whose sources publish contact data (legal, private capital, professional services).

## Refreshing

Prospect data decays fast (EA postings close in weeks; funding triggers age out). Re-run the two scripts after any research refresh; append a dated entry to `verification-log.md` and `docs/worklog.md`. Treat anything older than 60 days as unverified.
