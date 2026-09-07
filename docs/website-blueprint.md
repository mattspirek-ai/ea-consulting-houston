# Website Blueprint — Houston Fractional EA Firm

> Exported from the Hyperagent document of the same name (thread `cmtrpuzu61c3507ad27zn4poq`, document `cmtrqhbjh0syh06ad7l8t4v4v`, v1, 2026-09-07). The platform document is the editable master; this file is the archive copy. For the builder-facing version with acceptance criteria, see `build-brief.md`.

## Design Direction

**Register:** senior, discreet, editorial-corporate — closer to a boutique law or private-wealth firm than a SaaS landing page. The buyer is a Houston executive; the site should feel like something their chief of staff would approve.

**What competitors look like (so you don't):** national players use bright SaaS palettes, 3-step "how it works" blocks, comparison tables vs "others", and stock photos of smiling people with headsets. Local Houston sites are Wix/Ueni templates with no pricing. Clear both bars by being calmer and more specific.

**Palette cue:** deep navy or charcoal base, warm off-white paper, a single restrained accent (oxidized brass or Gulf-Coast teal). No neon, no gradients.

**Typography:** a confident serif for headlines (editorial authority) paired with a neutral grotesk for UI and body. Large, unhurried headline scale; generous whitespace.

**Imagery:** real Houston — skyline at dusk, Energy Corridor glass, TMC campus, a quiet conference room — plus real EA portraits once the bench is hired. Until then, restrained abstract or architectural imagery. No AI-looking people, no headsets.

**Motion:** minimal; a soft reveal on scroll at most. Speed matters more than delight (Core Web Vitals green).

**Voice:** first-person plural, plain, specific. "Your EA is matched in five business days" beats "supercharge your productivity."

## Sitemap

```
/                          Home
/pricing                   Pricing (public tiers + calculator)
/how-it-works              Matching, onboarding playbook, guarantees
/services/
  /executive-assistant     Fractional Executive Assistant (core)
  /chief-of-staff-support  60-hr tier positioning
  /in-person-houston       Hybrid in-person days (Houston only)
/industries/
  /energy                  Energy & oil-and-gas executives
  /healthcare              Physician-executives, TMC, clinic owners
  /legal                   Managing partners, practice leaders
  /private-capital         PE, family office, wealth
  /founders                Founders & CEOs (national virtual)
/houston/                  Houston hub (local SEO)
  /the-woodlands
  /sugar-land
  /katy
  /energy-corridor
  /galleria-uptown
  /downtown
/compare/
  /vs-belay
  /vs-boldly
  /vs-hiring-in-house
  /vs-offshore-va
/our-assistants            Bench bios (years, sectors, certifications)
/about                     Founder story, Houston roots, standards
/resources/                Blog / guides (pillar articles)
  /how-much-does-an-executive-assistant-cost
  /fractional-vs-full-time-executive-assistant
  /executive-assistant-vs-virtual-assistant
  /when-to-hire-an-executive-assistant
  /what-to-delegate-first  (lead magnet: 30-Day Delegation Playbook)
/book                      Discovery call scheduler
/contact
/security-and-confidentiality
/privacy, /terms
```
Every page ends with the same two CTAs: **Book a 20-minute fit call** (primary) and **See pricing** (secondary).

## Page Specs — Core

**Home**
- Purpose: qualify the visitor in 5 seconds (Houston, executive-level, US-based, priced openly) and route to Pricing or Book.
- Hero: headline stating the category and the city; subhead with the four pillars; primary CTA Book, secondary See pricing; a one-line trust strip ("Senior US-based EAs · Published pricing · Month-to-month · Matched in 5 business days").
- Sections in order: Who we serve (4 vertical cards → /industries); How it works (3 steps, but specific: fit call → meet 2 EAs in 5 days → 30-day Delegation Playbook); Pricing preview (3 tiers with real numbers, link to /pricing); Why Houston matters (in-person option, local references); Compare (short table vs in-house hire, national agency, offshore VA); Testimonials (name, title, industry — placeholders until real); Meet the bench (3 bios); FAQ (6 objections answered: contract, quality, confidentiality, hidden fees, timezone, what to delegate); Final CTA.
- SEO: title "Fractional Executive Assistant Firm in Houston | [BrandName]"; H1 contains "Houston" and "executive assistant"; LocalBusiness + Organization JSON-LD.

**Pricing**
- Purpose: the single biggest differentiator vs BELAY — make it the best pricing page in the category.
- Content: 3 tiers with hours, monthly, effective $/hr, what's included; add-ons; terms block (month-to-month, 2-week guarantee, rollover, no buyout fee, replacement in 5 days); an interactive calculator (hours needed → tier + comparison to fully-loaded in-house cost, showing the derivation); "How we compare" table with sourced competitor prices and the date checked; FAQ on billing.
- SEO: targets "executive assistant pricing", "fractional EA cost", "how much does an executive assistant cost" (also served by the resource article; cross-link). Product/Offer JSON-LD with prices.

**How It Works**
- Fit call → shortlist of 2 EAs with bios within 5 business days → chemistry call → start → 30-Day Delegation Playbook (week-by-week) → 2-week satisfaction checkpoint → monthly review. Include backup-coverage explanation and what happens if it isn't working.

**Book**
- Embedded scheduler (Cal.com/Calendly), 20-minute slot, 3 qualifying questions (role, hours needed, Houston or virtual). Confirmation page with the Delegation Playbook PDF.

**Our Assistants**
- Cards: first name, years, sectors, tools, certifications (PACE/CAP if held), a one-line "how I run a week". Filter by industry. Note on vetting (background check, reference checks, skills test).

## Page Specs — Industry, Local, Compare

**Industry pages (/industries/*)** — template, but every one must contain sector-specific detail or it is filler:
- Hero naming the role ("Executive assistants for energy leaders in Houston").
- "A week with your EA" — 6–8 concrete tasks in sector vocabulary (energy: AFE routing, board/JV meeting prep, OTC/NAPE logistics, field-visit travel; healthcare: credentialing paperwork, CME travel, clinic scheduling, payer calls; legal: docket-aware calendaring, CLE, client intake, conflicts forms; private capital: LP communications, deal-room logistics, family calendar, philanthropy boards).
- Confidentiality standard specific to the sector.
- One testimonial slot; bench members with that sector; CTA.
- SEO: "executive assistant for [sector]" terms (workbook priority 4); FAQ JSON-LD.

**Houston hub + suburb pages (/houston/*)**
- Hub: why a Houston firm (in-person days, Central Time, local references, GBP embed with map, service-area list). Suburb pages: 300–500 words of genuinely local content (business districts, typical clients, drive-time for in-person days), same CTA, LocalBusiness JSON-LD with areaServed. Avoid doorway-page thinness — each must add local specifics.
- SEO: "executive assistant Houston", "virtual executive assistant Houston", "fractional executive assistant Houston", "virtual assistant [suburb]" (workbook priority 5 — no national brand has these pages).

**Compare pages (/compare/*)**
- Honest, sourced tables: price (with date checked and link), talent location, contract length, buyout fee, guarantee, match time, local presence. Say what the competitor does well. Update quarterly; show "last verified" dates.
- /vs-hiring-in-house shows the fully-loaded cost derivation (salary + benefits + overhead) with BLS/Indeed/Robert Half sources.
- SEO: "Belay alternatives", "Boldly vs Belay", "fractional vs full time executive assistant", "US-based virtual assistant" (priority 4, currently owned by aggregators).

**Resources**
- Launch with the 5 pillar articles in the sitemap, each 1,500–2,500 words, sourced, with an in-article calculator or checklist and the Playbook lead magnet. Article JSON-LD, author bio.

## Conversion & Trust Features

**Conversion**
- Persistent header CTA "Book a fit call"; sticky mobile CTA bar.
- Pricing calculator (hours → tier → savings vs in-house) on /pricing and embedded on Home.
- Scheduler embedded, not linked out; 3 qualifying questions.
- Lead magnet: 30-Day Delegation Playbook (PDF) gated by email on /resources/what-to-delegate-first and as the post-booking gift.
- Exit-intent (desktop only, once): "See pricing" — never a discount.
- Live chat optional; if used, staffed by a real EA during business hours only.

**Trust**
- Published pricing and terms (the headline trust signal in this category).
- Named testimonials with title + industry + Houston area; video where possible.
- EA bios with years, sectors, certifications.
- Security & Confidentiality page: NDA standard, background checks, device/password policies, data handling, insurance (E&O, cyber).
- Guarantee block repeated on Home, Pricing, How It Works.
- Real Houston address, phone, Google Business Profile reviews embed.
- "Last verified" dates on every competitor price and claim; a public changelog for pricing/terms changes.
- Memberships/affiliations (GHP, IAAP/ASAP, vertical associations) once real — never fabricated logos.

**Accessibility & performance**
- WCAG AA contrast, keyboard-navigable, alt text, semantic headings.
- LCP < 2.5s, CLS < 0.1; images in AVIF/WebP; fonts self-hosted with font-display swap.

## SEO & Technical Plan

**Keyword-to-page map (from workbook 'Keywords' sheet; volumes to be pulled from Google Keyword Planner):**
- Priority 5: virtual executive assistant → /services/executive-assistant; fractional executive assistant → Home + /services/executive-assistant; hire executive assistant → /how-it-works; how much does an executive assistant cost / cost of executive assistant / executive assistant pricing → /pricing + resource article; executive assistant Houston / virtual assistant Houston / executive assistant services Houston TX / virtual executive assistant Houston / fractional executive assistant Houston → /houston hub.
- Priority 4: sector terms → /industries/*; comparison terms → /compare/*; informational → /resources/*; suburb terms → /houston/*.

**Technical**
- Clean URL structure as in sitemap; one canonical per page; trailing-slash policy consistent; www → apex 301.
- JSON-LD: Organization, LocalBusiness (Houston address, areaServed suburbs, sameAs LinkedIn/GBP), Service, Offer (tiers with prices), FAQPage, Article, BreadcrumbList.
- XML sitemap + robots; Search Console + Bing Webmaster; GA4 with events for book_click, pricing_view, calculator_use, playbook_download.
- Open Graph/Twitter cards per page; favicon set.
- Internal linking: every industry and local page links to Pricing and Book; resources link to the relevant service page.
- Publish cadence after launch: 2 resource articles/month; refresh compare pages quarterly.

**Off-page**
- Google Business Profile with weekly posts; Houston directories (GHP member directory, Houston Business Journal Book of Lists submission, Clutch profile); LinkedIn company page mirroring service pages; 3–5 Houston-relevant backlinks in 90 days (partner sites, association pages, a local podcast).

## Tech Stack & Launch Checklist

**Recommended stack (Node-first, commercial-license-safe, near-zero cost):**
- Framework: Next.js (App Router) or Astro — static/SSG pages, fast, SEO-friendly. MIT licensed.
- Styling: Tailwind CSS (MIT). Fonts: Google Fonts self-hosted.
- Content: MDX in-repo for pages/articles (no CMS cost), or Sanity/Contentful free tier if a non-technical editor is needed.
- Forms/scheduling: Cal.com (embedded) or Calendly; forms via the host's serverless functions or Formspree free tier.
- Hosting: Cloudflare Pages or Vercel free tier; Cloudflare DNS + WAF (the user already runs Cloudflare).
- Analytics: GA4 + Google Search Console; Cloudflare Web Analytics as privacy-friendly secondary.
- Email: Resend/Postmark free tier for form notifications; Playbook delivery via the same.
- Calculator: client-side JS only; no backend.
- Avoid: Wix/Ueni/Squarespace (the local competitor tier), GPL-only themes bundled into a paid product, any dataset without a commercial license.

**Launch checklist**
- [ ] Brand name, domain, logo, favicon
- [ ] All Core pages live incl. Pricing with real numbers
- [ ] 4 industry pages + Houston hub + 3 suburb pages minimum
- [ ] 2 compare pages (vs BELAY, vs in-house) with sourced, dated prices
- [ ] 3 resource articles + Playbook PDF
- [ ] Scheduler embedded and tested; confirmation email works
- [ ] JSON-LD validated (Rich Results Test); sitemap submitted; GBP verified
- [ ] Lighthouse ≥ 90 performance/accessibility/SEO on mobile
- [ ] Legal: privacy, terms, NDA standard page reviewed by counsel
- [ ] Testimonial placeholders clearly marked until real ones exist — never fabricated
- [ ] Analytics events firing; weekly KPI sheet linked
