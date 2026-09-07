# Prospect Research Brief & Schema — EA Consulting Houston

You are sourcing prospects for a Houston-based **fractional executive assistant firm** (senior, US-based EAs; published tiers $1,200 / $2,300 / $3,300 per month for 20/40/60 hrs; month-to-month; optional Houston in-person day). The firm sells to the executive who has outgrown self-management but can't justify a ~$99K fully-loaded EA hire.

## Ideal Customer Profile (from docs/strategy.md)

| Attribute | Profile |
|---|---|
| Decision-maker title | Founder/CEO of a $2–50M company; managing partner or practice leader; PE / family-office principal; physician-executive or clinic owner; energy VP/GM running a business unit |
| Company size | 5–150 employees, or a partner-level individual inside a larger firm without dedicated support |
| Geography | Houston metro first (Downtown, Galleria/Uptown, Energy Corridor, TMC, The Woodlands, Sugar Land, Katy, Pearland, Clear Lake); DFW / Austin / San Antonio only for the Texas-expansion segment |
| Trigger events (record the one you found) | Currently hiring an Executive Assistant (strongest); new funding or acquisition (2025–2026); fast-growth list (HBJ Fast 100, Inc 5000, HBJ Largest/Best Places); new firm/practice/fund launched 2024–2026; leadership expansion; travel-heavy or board-heavy role |
| Vertical tracks | energy, healthcare/TMC, legal, private capital (PE, family office, RIA), professional services (consulting, engineering, architecture, accounting), tech/founder-led |
| Anti-ICP (exclude) | solopreneurs; companies >500 employees with an existing EA pool; anyone whose primary need is bookkeeping/marketing; Fortune 500 HQs; staffing agencies; virtual-assistant companies (competitors) |

## Hard rules (data honesty — repo decision D-006)

1. **Every field has a source URL and a pull date.** If you cannot source a value, write `null`. Never estimate, infer, or fill with a neutral value.
2. **Contact information must be published on an official or authoritative source** — company website (contact page, team/attorney/provider bio), press release, Texas State Bar member directory, TMB/NPI registry, SEC Form ADV (for RIAs/PE), Texas SOS filing, Google Business Profile. **Do not guess email patterns.** If only `info@`/`contact@` is published, record that in `company_email` and leave `contact_email` null.
3. **Phone numbers must be the company's published main line** (or the direct line published on the person's official bio). No personal cell numbers, no home addresses.
4. Decision-maker **name and title need two independent sources** (e.g., company team page + LinkedIn / press / bar directory / Form ADV). Put both URLs in `title_sources`.
5. Prefer ExaSearch + ExaContents. Do **not** open browser sessions (other agents are using the browser quota). Use `curl -sL` from Bash if you need a raw page.
6. Do not include competitors (virtual-assistant / EA agencies / staffing firms) or companies obviously outside the size band.
7. Quantity target is stated in your task; quality outranks quantity. A row you can't source belongs in `rejected` with a reason, not in `candidates`.

## Output

Write **one JSON file** at the path given in your task with this exact shape:

```json
{
  "segment": "string — segment id you were given",
  "pulled_at": "2026-09-07",
  "researcher_notes": "string — sources swept, what was thin, anything the verifier should know",
  "candidates": [
    {
      "company_name": "string",
      "website": "https://...",
      "vertical": "energy | healthcare | legal | private_capital | professional_services | tech | other",
      "sub_vertical": "string or null",
      "headquarters_city": "string",
      "metro": "Houston | DFW | Austin | San Antonio",
      "address": "string or null",
      "address_source": "url or null",
      "employee_count_estimate": "string range like '25-50' or null",
      "employee_count_source": "url or null",
      "revenue_estimate": "string or null",
      "revenue_source": "url or null",
      "decision_maker_name": "string",
      "decision_maker_title": "string",
      "title_sources": ["url", "url"],
      "linkedin_url": "https://www.linkedin.com/in/... or null",
      "contact_email": "named person's published email or null",
      "contact_email_source": "url or null",
      "company_email": "published general email or null",
      "company_email_source": "url or null",
      "phone": "published main line, format (713) 555-0100, or null",
      "phone_source": "url or null",
      "trigger_signal": "hiring_ea | funding | acquisition | growth_list | new_launch | leadership_expansion | other",
      "trigger_detail": "one sentence, factual",
      "trigger_source": "url",
      "trigger_date": "YYYY-MM-DD or YYYY-MM or null",
      "icp_fit_rationale": "one or two sentences tying this row to the ICP table",
      "suggested_tier": "Foundation | Executive | Chief of Staff",
      "notes": "string or null"
    }
  ],
  "rejected": [
    { "company_name": "string", "reason": "string", "source": "url or null" }
  ]
}
```

Validate the JSON parses (`node -e "JSON.parse(require('fs').readFileSync(process.argv[1],'utf8'))" <file>`) before you finish. Your final message should be a short summary: counts of candidates and rejected, how many have a named `contact_email`, how many have `phone`, and which sources were most productive.
