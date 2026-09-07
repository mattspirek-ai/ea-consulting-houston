# BUILD BRIEF — Houston Fractional Executive Assistant Website

**Purpose of this file:** a self-contained instruction set for an LLM (or human) builder to design and build the marketing website for a new Houston-based fractional/virtual executive assistant (EA) firm. Everything a builder needs is here or in the referenced workbook. Read fully before writing any code.

**Prepared:** 2026-09-07 · **Companion files:** `EA_Houston_Virtual_Market_Research.xlsx` (competitors, keywords, pricing, buyer signals, sources), Strategy doc, Website Blueprint doc.

---

## 0. Ground rules for the builder

1. **Never fabricate proof.** No invented testimonials, client logos, review counts, press mentions, certifications, or "hours saved" numbers. Use clearly labeled placeholders (`[TESTIMONIAL PLACEHOLDER — replace before launch]`) and keep a list of them in `TODO-BEFORE-LAUNCH.md`.
2. **Every competitor price or claim shown on the site must carry a source URL and a "last verified" date.** Sources are in the workbook `Pricing` and `Competitors` sheets.
3. **Missing data stays missing.** Keyword volumes are unknown (not pulled yet). Do not invent them; do not use them in copy.
4. **Licensing:** only MIT/Apache/BSD (or equivalent) dependencies. No GPL/AGPL/CC-BY-SA assets. No stock imagery without a commercial license.
5. **Stack is Node-first** (Next.js or Astro + Tailwind). No Python in the request path.
6. **Brand name is a placeholder:** `[BrandName]`. Make it a single config constant so it can be swapped in one place.

---

## 1. Business summary (what the site is selling)

- **Category:** Fractional Executive Assistant firm. Use "fractional executive assistant" as the primary phrase and "virtual executive assistant" as the SEO secondary. Avoid leading with "virtual assistant" (drags into the $9/hr offshore comparison set).
- **Offer:** senior (8–15+ yrs), US-based, Houston-rooted executive assistants, matched in ≤5 business days, on month-to-month terms with published pricing, no buyout fees, a 2-week satisfaction guarantee, backup coverage, and an optional in-person day in Houston.
- **Who buys:** Houston founders/CEOs ($2–50M companies), managing partners and practice leaders, PE/family-office principals, physician-executives/clinic owners, energy VPs/GMs. Secondary: national virtual buyers who searched "Belay alternatives" or "executive assistant pricing."
- **Why it wins (the four pillars — each is a verified gap in the market):**
  1. Houston-rooted (no national competitor has local presence or in-person option).
  2. Senior, US-based, industry-fluent (energy, healthcare/TMC, legal, private capital).
  3. Radically transparent terms (published prices; month-to-month; no $10–20K buyout fee like BELAY; hours roll over one month).
  4. Delegation done with you (a 30-Day Delegation Playbook — buyers complain premium services still make them figure out what to delegate).
- **Table-stakes promises that must also appear** (universal in the category, not differentiators): matched in ≤5 business days, backup coverage, cancel anytime, free re-match, background-checked, AI-fluent.

## 2. Pricing to display (from the Strategy doc — Option A, derived from sourced benchmarks)

| Tier | Hours/mo | Monthly | Effective $/hr | For |
|---|---|---|---|---|
| Foundation | 20 | $1,200 | $60.00 | Partner-level individual; first-time delegator |
| Executive | 40 | $2,300 | $57.50 | CEO/founder: calendar, travel, inbox, board prep |
| Chief of Staff | 60 | $3,300 | $55.00 | Leader running a team, events, investor cadence |

Add-ons: Houston in-person day $450/day · extra hours $65/hr · specialist work (deck design, PM) $79/hr · onboarding $299 one-time (waived on Chief of Staff).
Terms block (repeat on Home, Pricing, How It Works): month-to-month · 2-week satisfaction guarantee · unused hours roll over one month · no buyout fee · replacement within 5 business days · confidentiality agreement standard.

Comparison anchors for the calculator and compare pages (sourced; show "last verified 2026-09-07" and link):
- Boldly: $2,600/40h → $6,500/100h, $65/hr flat, W-2 US, cancel anytime — https://boldly.com/pricing-plans/
- Delegate Solutions: $2,299–$3,959/mo for 25–45h ($88–92/hr), $499 onboarding — https://www.delegatesolutions.com/fractional-executive-assistant-pricing
- BELAY: pricing not published; third-party estimates $42–50/hr; 12-month contract; $10–20K buyout fee reported — https://www.usecarly.com/blog/belay-virtual-assistant-review/
- Offshore managed (Wing full-time): ~$1,099/mo (~$7/hr) — https://www.usecarly.com/blog/belay-virtual-assistant-review/
- In-house Houston EA: median salary ~$67–68K (BLS/Indeed), Robert Half range $64.7–96.3K; **derived** fully loaded ≈ $99K/yr ≈ $8,250/mo (salary + ~30% benefits + ~15% overhead). Show the derivation; label as an estimate.

## 3. Sitemap (build exactly this; slugs are final)

```
/  /pricing  /how-it-works  /book  /contact  /about  /our-assistants
/services/executive-assistant  /services/chief-of-staff-support  /services/in-person-houston
/industries/energy  /industries/healthcare  /industries/legal  /industries/private-capital  /industries/founders
/houston  /houston/the-woodlands  /houston/sugar-land  /houston/katy  /houston/energy-corridor  /houston/galleria-uptown  /houston/downtown
/compare/vs-belay  /compare/vs-boldly  /compare/vs-hiring-in-house  /compare/vs-offshore-va
/resources  /resources/how-much-does-an-executive-assistant-cost  /resources/fractional-vs-full-time-executive-assistant
/resources/executive-assistant-vs-virtual-assistant  /resources/when-to-hire-an-executive-assistant  /resources/what-to-delegate-first
/security-and-confidentiality  /privacy  /terms
```
Every page ends with two CTAs: **Book a 20-minute fit call** (primary → /book) and **See pricing** (secondary → /pricing).

## 4. Page specifications

### Home
Hero: H1 = "Houston's fractional executive assistant firm." Subhead = the four pillars in one sentence. CTAs: Book (primary), See pricing (secondary). Trust strip: "Senior US-based EAs · Published pricing · Month-to-month · Matched in 5 business days."
Sections, in order: Who we serve (4 vertical cards → /industries/*) · How it works (fit call → meet 2 EAs within 5 business days → 30-Day Delegation Playbook) · Pricing preview (3 real tiers → /pricing) · Why a Houston firm (in-person days, Central Time, local references) · Compare strip (vs in-house hire, national agency, offshore VA) · Testimonials (PLACEHOLDERS) · Meet the bench (3 bios, PLACEHOLDERS) · FAQ (contract length, quality consistency, confidentiality, hidden fees, timezone, what to delegate) · Final CTA.
SEO: title "Fractional Executive Assistant Firm in Houston | [BrandName]"; JSON-LD Organization + LocalBusiness.

### Pricing
Three tier cards (hours, monthly, effective $/hr, inclusions) · add-ons · terms block · **interactive calculator** (input hours/week needed → recommends tier, shows monthly cost, and compares to the derived in-house fully-loaded cost with the derivation visible) · "How we compare" table with the sourced anchors above and last-verified dates · billing FAQ. JSON-LD Offer for each tier.

### How It Works
Six steps with specifics: 20-min fit call → shortlist of 2 EAs with bios in ≤5 business days → chemistry call → start → 30-Day Delegation Playbook (week-by-week) → 2-week satisfaction checkpoint and monthly reviews. Explain backup coverage and what happens if the match isn't working (re-match in 5 days, or refund under the 2-week guarantee).

### Services (3 pages)
Executive Assistant (core: calendar, inbox, travel, meeting prep, expenses, CRM hygiene, board/investor logistics, personal admin) · Chief of Staff Support (60-hr tier: team cadence, events, OKR tracking, vendor management) · In-Person Houston (what an in-person day covers, service area, $450/day, how scheduling works).

### Industries (5 pages — template, but sector-specific content is mandatory)
Each page: sector H1 ("Executive assistants for energy leaders in Houston") · "A week with your EA" list of 6–8 sector-specific tasks · sector confidentiality note · bench members in that sector (PLACEHOLDER) · testimonial slot (PLACEHOLDER) · FAQ (3 sector questions) · CTAs.
Sector task vocabulary to use: **Energy** — AFE routing, JV/board meeting prep, OTC/NAPE logistics, field-visit travel, rig-schedule-aware calendaring. **Healthcare** — credentialing paperwork, CME travel, clinic and OR schedule coordination, payer/vendor calls, TMC campus logistics. **Legal** — docket-aware calendaring, CLE tracking, client intake, conflicts forms, billing-cycle support. **Private capital** — LP communications, deal-room logistics, family calendar, philanthropy boards, discreet travel. **Founders** (national virtual) — investor updates, hiring logistics, inbox triage, board decks.

### Houston hub + 6 suburb pages
Hub: why a Houston firm, in-person days, Central Time, Google Business Profile map embed, service-area list. Suburb pages: 300–500 words of genuinely local content (business districts, typical client types, drive-time for in-person days). JSON-LD LocalBusiness with `areaServed`. No thin doorway pages.

### Compare (4 pages)
Honest, sourced tables: price (with date + link), talent location, contract length, buyout fee, guarantee, match time, local presence, what they do well. `/compare/vs-hiring-in-house` shows the fully-loaded cost derivation with BLS/Indeed/Robert Half links.

### Our Assistants
Filterable bio cards (first name, years, sectors, tools, certifications, "how I run a week"). PLACEHOLDER cards until real. Vetting note: background check, references, skills assessment.

### Resources
Five pillar articles (1,500–2,500 words each, sourced, with a checklist or calculator). `/resources/what-to-delegate-first` gates the 30-Day Delegation Playbook PDF behind an email form. Article JSON-LD.

### Book / Contact / About / Security
Book: embedded Cal.com or Calendly, 20-minute slot, 3 qualifying questions (role, hours needed, Houston or virtual); confirmation page offers the Playbook. About: founder story, Houston roots, standards. Security & Confidentiality: NDA standard, background checks, device/password policy, data handling, insurance (E&O, cyber).

## 5. Design direction

Register: senior, discreet, editorial-corporate — boutique law / private-wealth firm energy, not SaaS. Deep navy or charcoal base, warm off-white paper, one restrained accent (oxidized brass or Gulf-Coast teal). Confident serif headlines + neutral grotesk body/UI (self-host Google Fonts). Large headline scale, generous whitespace, minimal motion. Imagery: real Houston architecture/skyline; abstract or architectural placeholders until real EA portraits exist. **Do not** use headset stock photos, neon gradients, or a bright SaaS palette — that is what every national competitor does; the local competitors are Wix/Ueni templates. Clear both bars by being calmer and more specific.

## 6. SEO and technical requirements

- Keyword → page map: see Blueprint doc and workbook `Keywords` sheet. Priority-5 terms: "virtual executive assistant", "fractional executive assistant", "hire executive assistant", "how much does an executive assistant cost", "executive assistant pricing", and all Houston-local variants ("executive assistant Houston", "virtual executive assistant Houston", "fractional executive assistant Houston", "executive assistant services Houston TX", "virtual assistant Houston").
- JSON-LD: Organization, LocalBusiness (Houston address, areaServed), Service, Offer (3 tiers), FAQPage, Article, BreadcrumbList. Validate with Rich Results Test.
- One canonical per page; consistent trailing-slash policy; www→apex 301; XML sitemap; robots.txt; Open Graph + Twitter cards per page.
- GA4 events: `book_click`, `pricing_view`, `calculator_use`, `playbook_download`, `compare_view`.
- Performance: Lighthouse ≥90 on mobile for Performance/Accessibility/SEO; LCP <2.5s; CLS <0.1; AVIF/WebP images; `font-display: swap`.
- Accessibility: WCAG AA contrast, keyboard navigation, alt text, semantic headings, focus states.

## 7. Stack

Next.js (App Router, static export where possible) or Astro · Tailwind CSS · MDX content in-repo · Cal.com/Calendly embed · Cloudflare Pages (or Vercel) + Cloudflare DNS/WAF · GA4 + Search Console · Resend/Postmark for form email · client-side calculator (no backend). Single `site.config.ts` holding brand name, address, phone, prices, tier definitions, competitor anchors with `lastVerified` dates.

## 8. Acceptance criteria (the build is done when all are true)

- [ ] All routes in §3 exist and render with real copy per §4 (placeholders only where §0 allows, all listed in `TODO-BEFORE-LAUNCH.md`).
- [ ] Pricing page shows the three tiers, add-ons, terms, working calculator, and sourced comparison table with last-verified dates.
- [ ] Every competitor figure on the site links to its source and shows a date.
- [ ] JSON-LD present and valid on Home, Pricing, Houston pages, Industry pages, Articles.
- [ ] Lighthouse mobile ≥90 across Performance/Accessibility/SEO/Best Practices.
- [ ] Both CTAs present on every page; scheduler embed works; form email delivers.
- [ ] `site.config.ts` is the single source of truth for brand, prices, and anchors.
- [ ] No GPL/AGPL/CC-BY-SA dependencies or assets; license audit output committed.
- [ ] No fabricated proof anywhere.

## 9. Known data gaps to resolve before launch (owner: the business, not the builder)

1. Pull monthly search volumes for the 61 workbook keywords from Google Keyword Planner.
2. Verify Houston EA wage/employment against BLS OEWS Houston May 2024 (the "547 employed" figure in a secondary source is unverified and likely wrong — do not use).
3. Pull domain ratings for competitors (Ahrefs/Moz free checkers) if you want authority benchmarks.
4. Confirm final brand name, domain, address, phone, insurance, and legal review of terms (especially the no-buyout-fee promise).
5. Replace all placeholders with real testimonials, bios, and photos.
