# Format Spec — "Athena-style" paid landing page (Concept D)

Purpose: replicate the **format** (structure, section order, layout patterns, rhythm, component shapes) of Athena's paid-search landing page `athena.com/cl/nb-executive-assistant` as observed 2026-09-07, using **our** positioning, pricing, and original copy. Do not copy Athena's copy, logos, photos, client names, or statistics. Their page is the layout reference only.

Observed reference: viewport 1280px; document height ~8,050px; 9 stacked full-width bands alternating dark/light; single primary CTA repeated 6 times ("Find your EA match" → ours: "Book a fit call").

## Design tokens (replicate the system, re-skin the values)

| Token | Athena (observed) | Ours |
|---|---|---|
| Dark band A (hero, footer) | `#062812` deep forest | deep navy `#0b2545` |
| Dark band B (how-it-works, pricing, CTA) | `#041f0e` darker green | darker navy `#071a33` |
| Light band | `#ebece1` limestone | warm paper `#f3efe7` |
| Card on dark | `#264330` / `rgba(255,255,255,.16)` | `#14325a` / `rgba(255,255,255,.14)` |
| Highlight card (battlecard) | `#5f6d64` muted green over photo | muted navy `#2a4466` over placeholder image |
| Accent glyph (4-point star) | gold `#c9a55c`-ish | brass `#b08d57` |
| Muted text on dark | `#b3cbb9` sage | `#9fb6d6` |
| Display font | Playfair Display 400 | Playfair Display 400 (or Fraunces) |
| Body/UI font | Figtree | Figtree (or Inter) |
| Eyebrow | mono-ish uppercase 12–13px, letter-spaced, inside a pill with 1px border | same, IBM Plex Mono |
| H1 | 60px / 1.12 | same |
| Section H2 | 50px serif (dark bands), 30px sans (light "utility" sections) | same pattern |
| Buttons | 8px radius; ghost = `rgba(255,255,255,.1)` + 1px border + arrow →; primary = white bg black text | same shapes; primary = brass bg, navy text |
| Cards | 20px radius (hero widget, pricing), 15px (battlecards), 8px (testimonials) | same |
| Section padding | ~96–120px vertical; 1180–1200px max content width | same |

## Section-by-section (in order)

### 0. Header (transparent over hero, 70px)
Left: wordmark (thin, letter-spaced caps). Right: one ghost button "Book a fit call →". Thin vertical divider lines at container edges. Not sticky.

### 1. Hero — dark band A, 2-column (541px / 389px on desktop)
- Left: eyebrow (mono caps, no pill) "TRUSTED BY …" → ours: **"HOUSTON-BASED · US-BASED SENIOR EAs · PUBLISHED PRICING"** (no invented client counts).
- H1 serif 60px, 3 lines. Ours: **"Reclaim your week with a senior fractional executive assistant."**
- Below H1: a quote card (1px border, 8px radius, transparent bg): testimonial text + 48px round avatar + name + title. Ours: **[TESTIMONIAL PLACEHOLDER — replace before launch]** with a placeholder avatar circle and "[Name] · [Title], [Houston company]".
- Right: **role-picker widget card** (`rgba(255,255,255,.16)` bg, 20px radius, ~389px wide): heading "What best describes your role?", one-line subhead, then 4 stacked ghost buttons with right arrows. Ours: **Founder / CEO · Managing partner or practice leader · PE, family office, or wealth · Physician-executive or clinic owner** (+ 5th "Other / VP or GM"). Clicking a role stores it, scrolls to the booking section, and pre-fills the role field (no backend).
- Bottom of hero: **logo strip** — a horizontally scrolling row of grey logos on a slightly darker band. Ours: **do not fabricate logos.** Replace with a text strip of the five sector words in the same grey ("Energy · Healthcare/TMC · Legal · Private capital · Founders") styled like logos, and an HTML comment "[LOGO STRIP PLACEHOLDER — add real client/partner logos only with permission]".

### 2. "What your EA can do" — light band, 2-column (image left / tabbed list right)
- Left: pill eyebrow "WHAT YOUR EA CAN DO"; H2 in **sans 30px** (not serif) "There's no limit to what you can delegate." → ours: **"Almost everything on your plate can move to theirs."**; below, a 548×400 photo (ours: placeholder block labeled "PHOTO — Houston EA at desk"); below that a **stat callout card** (sage-tinted bg, 4-point star glyph, italic sentence with bold numbers). Ours: use only a sourced figure or a labeled placeholder, e.g. **"[METRIC PLACEHOLDER — publish only measured data]"** or a sourced industry stat with "(source in footer)".
- Right: **vertical tab list** — 4 category headings (large, 22–24px; active one dark, inactive ones muted grey) with the active category expanded into a checkmark list of 10–14 items. Athena's categories: Day-to-day · Business operations · Household & family · Personal wellness. Ours: **Day-to-day · Business operations · Sector-specific (energy/TMC/legal/PE vocabulary from build-brief) · Personal & household**. Ghost button "Book a fit call →" at the bottom.

### 3. How it works — dark band B
- Pill eyebrow "HOW IT WORKS"; serif H2 50px, 2 lines, left; a ghost button "Read FAQs" top-right (anchors to FAQ).
- 3 columns separated by 1px vertical rules, each: serif numeral "01/02/03" in brass, sans H3 22px, body 16px muted. Ours: 01 Tell us about you (20-min fit call) · 02 Meet two EAs within 5 business days · 03 Start with the 30-Day Delegation Playbook (2-week checkpoint, monthly reviews).
- Below: **stat band** — bordered box (1px brass border, 8px radius) with star glyph + italic sentence. Ours: a *terms* statement instead of an invented stat: **"Month-to-month. No buyout fee. Replacement within 5 business days."**

### 4. "How we're different" — light band, "battlecards"
- Pill eyebrow; serif H2 50px, 3 lines, left-aligned, max-width ~560px.
- **Battlecards row**: one wide highlighted card (muted-navy tint over a photo placeholder, 15px radius, ~805px wide, ~1000px tall) with the brand's column title top-left and a 9-item list bottom-left in white; to its right, **two collapsed vertical cards** (1px border, 15px radius, ~165px wide) with their titles rotated 90° at the bottom: "AI Assistants" and "Traditional EA/VA". Clicking a collapsed card expands it (accordion) and collapses the others; each has its own 8-item list. Ours: **BRANDNAME Fractional EA** vs **National agency (unpublished pricing)** vs **Offshore VA** — items must be sourced or descriptive facts from build-brief (e.g., "Pricing published on this page" vs "Pricing behind a sales call (source in footer)"; "Month-to-month, no buyout fee" vs "12-month contracts, $10–20K buyout fees reported (source)"; "Houston-based, in-person option" vs "Remote only").
- Below the cards, still in the light band: **"Security & support" 2×2 grid**: pill eyebrow "SECURITY & CONFIDENTIALITY"; sans H2 30px; four text blocks (H3 18px + 2–3 line body): ours — NDA standard on every engagement · Background checks + reference checks + skills assessment · Device and password hygiene policy · Backup coverage and re-match support. No invented certifications (no "SOC 2" unless true).

### 5. Pricing — dark band B, 2-column (pricing card left 416px / text right 518px)
- Left: **pricing card** (`#14325a` bg, 20px radius): small title, one-line descriptor, hairline rule, big serif price "$2,300 / per month" (the Executive tier, as the featured card), **primary white/brass button** full-width, then 4 bullets. Below/around it: a **tier switcher** (3 small pills: Foundation $1,200 · Executive $2,300 · Chief of Staff $3,300) that swaps the card's numbers and bullets — Athena has one card; we keep the single-card format and add the switcher so all three published tiers are visible.
- Right: pill eyebrow "PRICING"; serif H2 50px "Simple, predictable cost" → ours: **"Published pricing. Month-to-month."**; one-line lead; 3 bullets (our three tiers with hours + effective $/hr); small brass italic line (Athena: "Every day you wait…") → ours: **"Add-ons: in-person Houston day $450 · extra hours $65/hr · specialist work $79/hr · onboarding $299 (waived on Chief of Staff)."**; ghost button "Book a fit call →"; then a **bordered stat box** (brass border) → ours: the derived in-house comparison **"A full-time in-house Houston EA runs ≈ $8,250/mo fully loaded (derived estimate — derivation in footer)."**

### 6. Testimonials — light band
- Centered small eyebrow "TESTIMONIALS", centered serif H2 50px. Horizontal **carousel** of white cards (8px radius, ~400px wide) that bleed past both edges, each: quote 20px, name 14px, title 13px grey. Ours: 4 cards, all **"[TESTIMONIAL PLACEHOLDER — replace before launch]"** with the field layout visible; auto-scroll optional, arrows/drag required.
- Below: full-width **dark stat band** (dark green box, white italic text, star glyph) → ours: **"[METRIC PLACEHOLDER — publish only measured data]"** or a sourced stat with source in footer.

### 7. FAQ — same light band, 2-column (serif "FAQ" 70px left / accordion right)
- 5 questions, 1px hairline separators, chevron/plus toggles. Ours (answers from build-brief): How is this different from a virtual assistant? · How do you vet EAs? · What if the fit isn't right? · How do you handle confidentiality? · What does onboarding look like and how long does it take?
- Centered ghost pill button "SCROLL TO TOP" (mono caps).

### 8. Final CTA — full-bleed photo with dark overlay (~575px tall)
- Centered: pill eyebrow "GET STARTED TODAY"; serif H2 60px with **italic emphasis words** (Athena italicizes "thousands" and "stopped") → ours: **"Stop *doing it all* and start *running the week*."**; ghost button "Book a fit call →". Photo: placeholder block "PHOTO — Houston skyline / office" with gradient overlay.
- This section also hosts the **booking form** (Athena links out; we keep the page self-contained): scheduler placeholder + 3-question form (role pre-filled from hero picker, hours needed, Houston or virtual) with in-page confirmation, no backend.

### 9. Footer — dark band A (~344px)
Left: wordmark + "© BRANDNAME 2026". Right: Terms · Privacy · Security & Confidentiality. Add a **"Sources" line**: every competitor claim and the in-house derivation listed with URL + "last verified 2026-09-07" (this is where our transparency rules live on an otherwise Athena-format page).

## Behaviors
- Role picker → stores role, smooth-scrolls to booking, pre-fills field.
- Delegation tabs → vertical accordion, one open at a time.
- Battlecards → click to expand; keyboard accessible.
- Pricing tier switcher → swaps card content; default Executive.
- Testimonial carousel → arrow buttons + drag/scroll-snap.
- FAQ accordion; scroll-to-top.
- Reveal-on-scroll subtle, gated behind prefers-reduced-motion.

## Hard rules (unchanged from build-brief)
No fabricated proof (testimonials, logos, metrics, certifications); every competitor figure sourced with date; pricing strings exact; `BRANDNAME` single JS const; external links `target="_blank" rel="noopener noreferrer"`; all CSS/JS inline; Google Fonts via `<link>` only.
