# Website Concepts — four formats for the same business

Four complete, self-contained HTML prototypes of the public website, built from the same `docs/build-brief.md` (same positioning, same pricing, same competitor anchors, same no-fabricated-proof rule) but with deliberately different **structure** and **visual register**. Open any `index.html` in a browser; no build step, no dependencies beyond Google Fonts (and ECharts CDN in concept C).

All four share: the exact tiers ($1,200 / $2,300 / $3,300 for 20 / 40 / 60 hrs), add-ons, terms (month-to-month, 2-week guarantee, 1-month rollover, no buyout fee, replacement in 5 business days), sourced competitor prices with "last verified 2026-09-07", a working client-side pricing calculator (A–C) or tier switcher (D), clearly labeled placeholders for brand name / testimonials / bios / address, and JSON-LD.

| | A — Editorial boutique | B — Conversion landing | C — Pricing-first transparency | D — Athena-format paid landing |
|---|---|---|---|---|
| Folder | `a-editorial-boutique/` | `b-conversion-landing/` | `c-pricing-first/` | `d-athena-format/` |
| Structure | Multi-section home page; the top of a full multi-page site (Pricing, Industries, Houston hub, etc. as separate pages later) | One long scroll with a single job: book a fit call; calculator directly under the hero | The home page *is* the pricing page and the comparison table; everything else is secondary | Athena's paid-search landing structure replicated section for section: hero with role-picker widget, logo strip (placeholder), tabbed delegation list, 3-step columns, battlecard comparison, security grid, single pricing card + tier switcher, testimonial carousel, FAQ, full-bleed CTA with booking |
| Register | Navy/charcoal + warm paper, serif headlines, law-firm / private-wealth calm | Light canvas, one decisive accent, crisp sans, big numbers, short sentences | White, monochrome, hairline rules, tabular numerals, one signal color for our own row; Bloomberg/FT data-page feel | Athena's system re-skinned: deep navy pair + warm paper bands, Playfair Display + Figtree, pill eyebrows, ghost arrow buttons, brass star glyph |
| Best for | Building brand authority with Houston executives; the "front door" of the full site in the blueprint | LinkedIn posts and Houston-only Google Ads traffic; fastest path to booked calls | Capturing "executive assistant pricing / cost / Belay alternatives" search intent; buyers burned by opaque national brands | Paid search and paid social landing where the buyer is already comparing national agencies; proven conversion structure |
| Trade-offs | Most pages to build and maintain; slower to first conversion | Less depth for skeptical buyers; weaker SEO surface on its own | Feels analytical rather than warm; leans on data as proof, so weak until real client metrics exist | Visual resemblance to a competitor's page (format only; copy/assets original) — see D-012; depends on real testimonials/logos to reach its potential |
| Calculator placement | Inside the pricing section | Hero-adjacent centerpiece | Integrated cost model with derivation and annualized view | No calculator; single pricing card with a 3-tier switcher (format fidelity over features) |
| Proof style | Testimonials + bench bios (placeholders) | Testimonials + metric counter (placeholders) | Sourced comparison data + buyer-complaint citations; no testimonials | Testimonial carousel + stat bands — all placeholders or sourced/derived until real metrics exist |

## How to choose (or combine)

Concept D is the paid-traffic landing page; A/B/C remain the organic site options. D replaces B as the ad landing if paid search becomes the main channel.

The blueprint's intent is **A as the site, B as the paid/social landing page, C as the `/pricing` + `/compare/*` pages.** They are not mutually exclusive — the strongest launch uses A's shell, embeds B's calculator-first hero pattern on the Houston hub page, and lifts C's comparison table and changelog into `/pricing`. If only one can ship first, ship **B** for the fastest first clients, then grow into A.

## What is placeholder (replace before launch)

Search each file for `PLACEHOLDER` and `BRANDNAME`. Nothing marked placeholder is real: no testimonials, bios, metrics, addresses, or phone numbers exist yet. Competitor prices are real and sourced; re-verify quarterly and update the "last verified" dates.

## Provenance

Built 2026-09-07 (Session 2) from `docs/build-brief.md`. Design decisions per concept are recorded in `docs/worklog.md` Session 2.
