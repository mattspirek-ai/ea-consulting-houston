# LinkedIn Operating Playbook — [BrandName], Houston Fractional EA Firm

**Prepared:** 2026-09-07 · **Owner:** Founder · **Companion files:** `post-bank.json` / `post-bank.md` (60 ready posts), `calendar-first-30-days.md`, `scripts/linkedin/post_scaffold.mjs`, `scripts/linkedin/build_calendar.mjs`
**Ground truth:** `docs/build-brief.md` and `docs/strategy.md`. If this playbook ever conflicts with those, they win.

LinkedIn is GTM channel #1 (strategy doc §Go-to-Market). This document is the operating manual for the founder's 3–5 posts/week cadence and daily engagement routine.

---

## 1. Goal and KPIs

**Goal:** be the visible, trusted voice on executive support in Houston, and convert that trust into fit calls. The strategy doc's day-90 targets that LinkedIn primarily feeds: 40+ discovery calls, 3–8 paying clients.

**We measure only what we can count. We do not adopt anyone else's benchmarks as targets.** External medians exist (e.g., ContentIn's analysis of 100K+ personal-profile posts found a *median* 2.29% engagement rate, ~10 engagements and ~412 impressions per post — contentin.io/blog/linkedin-engagement-benchmarks/, 2025-12-09), and they are useful only as reality checks against inflated expectations, not as goals.

Weekly KPIs (tracked in the scorecard, §11):

| KPI | Source | Why |
|---|---|---|
| Posts published (vs plan) | manual | Consistency is the only lever fully in our control |
| Profile views | LinkedIn analytics | Leading indicator that content reaches the right people |
| Connection requests sent / accepted (acceptance %) | manual + LinkedIn | Measures targeting + note quality |
| Substantive comments made (10/day target) | manual | The distribution lever we control |
| Comments received & replied to within 2h | manual | Conversation depth beats reach |
| Inbound DMs started (by a target-audience person) | manual | First commercial signal |
| Conversations moved to fit-call offer | manual | Pipeline motion |
| Fit calls booked (from LinkedIn) | Cal.com/Calendly source tag | The number that pays rent |

Baseline rule: the first 4 weeks establish OUR baseline. From week 5, "good" means beating our own trailing 4-week average, not an internet number.

---

## 2. Audience

### Primary — Houston decision-makers (from strategy doc ICP)
- Founders/CEOs of $2–50M companies (5–150 employees)
- Managing partners and practice leaders (law, professional services)
- PE / family-office principals
- Physician-executives and clinic owners (TMC orbit)
- Energy VPs/GMs running business units (Energy Corridor, Downtown, The Woodlands)

### Secondary — national virtual buyers
Executives who searched "Belay alternatives" or "executive assistant pricing" and were burned or repelled by opaque pricing, 12-month lock-ins, or offshore mismatch.

### What they scroll past
- Motivational filler and "5 AM routine" content
- Engagement bait ("Agree?", "Tag someone…") — also now algorithmically penalized (see §7)
- Obvious pitches, obvious AI text (one 1.2M-post analysis found AI-sounding posts earn ~57% less engagement — magicpost.in/blog/linkedin-algorithm-2026, 2026-06-05)
- Vague "productivity" advice with no lived detail
- Anything that smells like a funnel

### What they stop for
- **Their own week, described accurately.** AFE routing, credentialing deadlines, docket chaos, LP letters, board prep at 9pm. Recognition is the hook.
- **Numbers nobody else will publish.** Pricing math, contract terms, honest cost comparisons.
- **Sourced industry fine print.** Buyout fees, lock-ins, expiring hours — with receipts.
- **Houston texture.** OTC week, NAPE, hurricane season logistics, TMC parking, I-10 math. Specificity signals "one of us."
- **A founder keeping score in public.** Real numbers, dated, including zeros.

---

## 3. Voice

**Register:** chief-of-staff calm. Specific, plain, unhurried, dry humor allowed, drama not. Write like a senior operator briefing a principal: short sentences, concrete nouns, no adjectives doing a verb's job. (Matches the build brief's design register: boutique law / private wealth, not SaaS.)

**Banned words and patterns:**
- hustle, crush (as in "crush your goals"), game-changer, rockstar, ninja, 10x, unlock, elevate, "level up"
- 🚀 and emoji strings generally (a single plain emoji in a comment is tolerable; none in posts)
- "I'm humbled to announce…" — announce things plainly or not at all
- Rage-bait, dunking on individuals, manufactured outrage
- Fake vulnerability ("I cried in my car, and here's what it taught me about B2B sales")
- Engagement bait: "Agree?", "Thoughts?" as the entire CTA, "Tag someone who…", polls with obvious answers — these are also reach-penalized since LinkedIn's January 2025 update (remery.ai/blog/linkedin-algorithm-changes-2026-founders, 2025-11-14; practitioner-tracked data)
- Fake cliffhangers and "wait for it" hooks
- Unverifiable superlatives: "world-class", "best-in-class", "unmatched"

**Writing about clients without exposing them:**
1. **No real client is ever identifiable** without written permission — no names, no "a well-known Galleria PE firm," no detail combination that narrows to one person.
2. **Composites must be labeled composites, in the post body**, e.g. "a composite drawn from several conversations, not a specific client." A composite presented as a real client is fabrication. Labeled composites may never carry metrics ("saved 11 hours") — composite = qualitative only.
3. **Vignettes are labeled illustrative** ("built from the tasks energy executives tell us they need off their plate — not a specific client").
4. **No fake metrics, ever.** No invented hours-saved, client counts, revenue, or satisfaction figures. This repeats the build brief's rule #1 and it has no exceptions for social media.
5. Real client stories require **written permission**, and get shared with sector + role only ("a physician-executive client"), never named unless they explicitly agree to a named testimonial.

---

## 4. Six content pillars

Mapped to the four positioning pillars (build brief §1) and the documented buyer pains (`research/demand_keywords_pricing.json → buyer_signals`).

| # | Content pillar | JSON key | Maps to positioning pillar | Buyer pain it answers |
|---|---|---|---|---|
| 1 | **Delegation craft** — what to hand off first, playbook excerpts, delegation failure modes | `delegation_craft` | #4 Delegation done with you | "poor_onboarding", "insufficient_delegation", "hard to know what to delegate" objection |
| 2 | **Houston executive life** — energy/TMC/legal/PE week-in-the-life, OTC/NAPE/hurricane logistics, Central Time | `houston_executive_life` | #1 Houston-rooted, #2 industry-fluent | "no industry-specific knowledge", "timezone gaps" objections |
| 3 | **Radical transparency** — pricing math, why we publish, contract terms in plain English. **Cite only our published tiers: $1,200/20h, $2,300/40h, $3,300/60h** + published add-ons ($450 in-person day, $65/hr extra, $79/hr specialist, $299 onboarding waived on Chief of Staff) | `radical_transparency` | #3 Radically transparent terms | "pricing_opacity", "hidden fees" |
| 4 | **The industry's dirty laundry** — unpublished pricing, 12-month lock-ins, $10–20K buyout fees, expiring hours, offshore mismatch, support taper. **Every claim sourced; competitors named only with sourced facts; source URL in the post's `sources` array AND "(source in comments)" in the body** | `industry_dirty_laundry` | #3 (by contrast) | "contract_lock_in", "restrictive_terms", "hours_policy", "quality_inconsistency", "support_degradation", "hidden_total_cost" |
| 5 | **Behind the bench** — how we vet, EA craft, tools, AI stance, confidentiality system, backup coverage | `behind_the_bench` | #2 Senior, US-based, industry-fluent | "quality_inconsistency", "va_performance", "data security" objection |
| 6 | **Founder's build log** — starting the firm in public, decisions with reasoning, **honest numbers only when real** (placeholders otherwise), public kill criteria | `founders_build_log` | All four (trust engine) | "previous bad experience / gun-shy" objection — trust built in public |

Fair-play rule for pillar 4: criticize documented practices, credit documented strengths (e.g., Boldly's lifetime guarantee and meet-before-you-subscribe are praised in our own research — say so). We attack terms, not people.

---

## 5. Eight post formats

Median data says any media beats text-only ~3x on engagement rate, and document/carousel posts lead most 2025–2026 studies (ContentIn benchmarks, 2025-12-09; Socialinsider via Social Media Today, 2025-04-14; meikuio.com/linkedin-algorithm-2026, 2026-06-06). But text is fastest to produce at quality — so the mix below trades some reach for sustainable volume, and reserves carousels for the highest-value ideas.

### 5.1 Short text insight (workhorse — ~2/week)
> Hook (first line, ≤12 words) → context in 1–2 lines → the insight, concretely → one worked example or checklist fragment → soft CTA/genuine question.
Length: 120–200 words (multiple 2025–2026 datasets favor longer, substantive posts: 900–1,700 characters carried the highest median engagement counts in ContentIn's corpus; a 1.2M-post analysis found 400+ word posts outperform very short ones — treat both as directional, not law).
Use for: single sharp ideas. Delegation craft, transparency, bench.

### 5.2 Story → lesson
> Hook → scene (labeled composite or permissioned real story) → the turn → lesson in 1–2 lines → CTA.
Use for: failure modes, buyer-objection stories, craft. The lesson must survive without the story — no fake vulnerability.

### 5.3 Listicle / checklist
> Hook stating the payoff → 4–8 numbered items, each one line + one specific detail → who it's for → CTA ("save this").
Use for: delegation sequences, contract-clause checklists, hurricane prep. High save-rate content.

### 5.4 Contrarian take with evidence
> The common belief, stated fairly → why it fails → **sourced** evidence → our position → what to do instead.
Use for: dirty laundry, transparency, AI-and-EAs. Rule: no contrarianism without a citation or clearly-flagged reasoning. Never manufactured controversy.

### 5.5 Document carousel (PDF) — 1–2/month
> Post body: 2–3 line setup + slide-by-slide value. Carousel: title slide → one idea per slide (≤25 words/slide) → sourced facts get on-slide citations → final slide CTA. 8–12 slides.
Use for: pricing math, playbook week-by-week, industry fine print. Carousels/documents lead engagement in Socialinsider's 1M-post company-page study (2025-04-14) and Metricool's 2026 study; they maximize dwell time (see §7).

### 5.6 Poll + follow-up — max 1–2/month
> 2–3 line genuine setup (a question we actually don't know the answer to) → 4 options, no obvious winner → explicit promise: results + full post on the winning option within a week.
Metricool's 2026 study: polls are <1% of posts but earn the highest average impressions on company pages — underused, and fine when genuine. Obvious-answer polls are penalized engagement bait (Remery, 2025). The follow-up post is mandatory — a poll without a follow-up is farming.

### 5.7 "A week with your EA" vignette
> Hook naming the persona → Mon–Fri, one beat per day, sector vocabulary doing the work (AFE routing, credentialing, docket, LP letters) → closing line contrasting "none of this needs you / all of it has you" → CTA.
Always labeled illustrative. Use for: Houston executive life; the sector pages of LinkedIn, effectively.

### 5.8 Founder build-log update
> What happened (real or `[INSERT]` placeholder) → the decision + reasoning → what it costs us / what it buys → what's next → ask.
Use for: pillar 6. Numbers only when real, always dated. Corrections are new posts, never edits.

---

## 6. Hook library — 40 first lines (≤12 words, no clickbait)

### Delegation craft
1. Delegate your calendar before your inbox.
2. The only-you list is smaller than you fear.
3. Track one week. Sort it into three lists.
4. Approvals queue at your name? You're the bottleneck.
5. Delegation is a system, not a personality trait.
6. Your EA's first week decides the next year.
7. Board prep at 9pm is a systems gap.

### Houston executive life
8. OTC week is won in February.
9. A docket doesn't care about your calendar.
10. Hurricane season is an executive continuity problem.
11. Central Time is an underrated operating advantage.
12. TMC parking is a calendar problem.
13. NAPE fills a February calendar in one afternoon.
14. Schedule around I-10, not through it.

### Radical transparency
15. Our pricing is on the website. All of it.
16. Publishing prices costs us deals. We'll take the trade.
17. Our contract fits in ten plain-English lines.
18. Expiring hours are a quiet margin trick.
19. The honest math on a full-time Houston EA.
20. Six questions to ask any EA service. Including us.
21. If you hire your EA away from us, we did our job.

### The industry's dirty laundry
22. The biggest name in EA services won't tell you the price.
23. Twelve months is a long time to be wrong.
24. The $10,000 fee nobody mentions on the sales call.
25. Your unused hours may be their best product.
26. "Hit or miss" shouldn't describe a premium service.
27. The invoice is not the total cost.
28. Offshore VAs aren't the problem. The mismatch is.

### Behind the bench
29. How we vet an EA before you ever meet them.
30. What "senior" means when we say it.
31. AI drafts. Your EA decides.
32. Discretion has a checklist.
33. The best EAs spend week one mostly listening.
34. One document decides whether an EA match survives.

### Founder's build log
35. I'm building Houston's fractional EA firm. In public.
36. We published pricing before we had a single client.
37. We set public kill criteria for this firm.
38. Month-to-month means clients can fire us monthly.
39. Build log: the real numbers, dated.
40. The firm we're building was written in complaint threads.

Hook craft notes: front-load the noun; LinkedIn truncates around the first ~150 characters, so line one carries the click (remery.ai, 2025-11-14). One 1.2M-post analysis found opening with a question correlates with worse engagement (magicpost.in, 2026-06-05) — prefer declarative hooks; save genuine questions for the CTA.

---

## 7. What the algorithm rewards in 2025–2026 (sourced)

Facts we plan around — each with source and date; anecdotal/practitioner items marked:

1. **Dwell time is a confirmed ranking signal.** LinkedIn's own engineering blog defines feed-dwell (counting once ≥half a post is visible) and after-click dwell. [LinkedIn-confirmed, via postiv.ai/blog/linkedin-algorithm-2026, 2026-03-14] → longer substantive posts, carousels, scannable structure.
2. **Engagement-bait is penalized; "knowledge and advice" rewarded** since the January 2025 update. [remery.ai, 2025-11-14 — practitioner tracking of 47 founder profiles; directionally consistent across sources] → no "Agree?", no tag-bait, genuine questions only.
3. **Topic consistency ("fingerprint") matters; reach dropped ~50% platform-wide in 2025 as relevance replaced reach.** [contentin.io/blog/linkedin-algorithm-2025…, 2025-12-27 — practitioner analysis] → six pillars, one theme: executive support. We do not post about anything else.
4. **Personal profile > company page.** Metricool (673K posts, 2026-04-14): personal profiles average 63% higher engagement; one 2026 analysis attributes ~31% of feed impressions to personal profiles vs ~2% to company pages [meikuio.com, 2026-06-06, practitioner]. → founder posts; page is a shell (see §10).
5. **Formats:** carousels/documents lead engagement across Socialinsider (1M posts, 2025-04-14), Metricool 2026, and meikuio 2026; any media beats text ~3x on median engagement [ContentIn, 2025-12-09]. Video is widely used but underperforming carousels in 2026 [Metricool, 2026-04-14]. → carousel for flagship ideas; no video requirement for launch (founder time is the constraint); revisit at day 60.
6. **External links:** LinkedIn has never confirmed a link penalty; large studies consistently find linked posts reach less (19–50% across studies), most likely a dwell-time side effect; the penalty appears to attach mainly to the preview card, and hits company pages harder than profiles [tryordinal.com/blog/linkedin-link-penatly-study, 2026-08-08; magicpost.in, 2026-06-05; meikuio.com, 2026-06-06 — all practitioner data, findings genuinely split]. → our convention: sources and links go in the first comment ("source in comments"), both for reach hygiene and because it keeps post bodies clean. Exception: if a link is the point (pricing page), put it in the body without preview and accept the cost.
7. **Hashtags are de-emphasized:** hashtag pages disabled Oct 2024, hashtag following removed; 2025–2026 analyses find no reach benefit and possible harm beyond ~3 tags [authoredup.com/blog/linkedin-algorithm, updated 2025–2026; postiv.ai, 2026-03-14]. → we use 0–1 hashtags, usually 0.
8. **Early engagement window:** multiple practitioner analyses treat the first 60–90 minutes as the test window for wider distribution [meikuio.com, 2026-06-06; anecdotal consensus]. → post, then stay for 30–60 min replying; never post-and-vanish.
9. **Comment adjacency:** commenting on someone's post is widely reported to raise the odds your next post reaches them (one practitioner puts it at "+70%") [contentin.io, 2025-12-27 — **anecdotal, unverified magnitude**]. Directionally safe: comments are distribution.
10. **AI-sounding text underperforms** (~57% less engagement in one 1.2M-post analysis) [magicpost.in, 2026-06-05, practitioner]. → drafts may start anywhere; every post ships in the founder's voice, edited by the founder.

---

## 8. Cadence and weekly rhythm

**Cadence: 4 posts/week baseline (Mon–Thu), optional 5th on Friday.** Within the 3–5×/week band the strategy doc mandates; consistent-cadence accounts outperform sporadic ones in practitioner data [contentin.io, 2025-12-27], and >1 post/day is counterproductive [meikuio.com, 2026-06-06].

| Day | Pillar (alternate by week) | Default format |
|---|---|---|
| Monday | Delegation craft | short text / checklist |
| Tuesday | Houston executive life (rotate sector: energy → healthcare → legal → private capital → founders) | vignette / story |
| Wednesday | Radical transparency ↔ Industry dirty laundry (alternate weeks) | contrarian / carousel |
| Thursday | Behind the bench ↔ Founder build log (alternate weeks) | story / build-log |
| Friday (optional) | Founder build log (real numbers) or poll | build-log / poll |

Rationale: Tuesday–Thursday are the strongest engagement days across studies; the boldest content (transparency/dirty laundry) gets the strongest mid-week slots.

**Posting time (Houston / Central audience):** default **7:30–9:00 AM CT, Tue–Thu**, Monday similar. Sources: Hootsuite's 2025 data puts overall peaks Tue–Wed 8–9 AM local (blog.hootsuite.com/best-time-to-post-on-linkedin/, 2025-11-19); a synthesis of B2B studies lands on Tue–Thu mid-morning local time with Wednesday strongest and weekends down 50–70% (reachly.co/blogs/best-time-to-post-on-linkedin-b-2-b, 2026-06-08). Honest caveat: ContentIn's controlled test found posting-hour effects did **not** survive within-account controls (2025-12-09) — so treat timing as a weak lever, consistency as the strong one. Our audience skews early (energy and medicine start early in this city — anecdotal, ours), so early morning also simply fits their scroll window before the day starts. Never sacrifice a post to hit a time slot.

**30-day ramp** (detail in `calendar-first-30-days.md`):
- Week 1: profile overhaul + company page + 3 posts (launch, pricing, first delegation post). Engagement routine starts day 1 — it matters more than posting early on.
- Week 2–3: 4 posts/week, all six pillars introduced, first poll, first carousel.
- Week 4: 4–5 posts/week steady state; first build-log numbers post **only if real numbers exist**; 30-day retrospective against the scorecard.

---

## 9. Engagement routine — the daily 20-minute block (plus post-day windows)

Do this every weekday, ideally right after posting. Split: ~10 min connections, ~10 min comments; replies happen throughout the day.

### a) 30 targeted connection requests/day
Targets, in priority order: Houston founders/CEOs ($2–50M), managing partners, PE/family-office principals, physician-executives, energy VPs/GMs; then engaged commenters on our posts and on peers' posts; then national execs active on EA/delegation topics.

**Note template (non-salesy, never a pitch):**
> Hi [Name] — I write about delegation and executive support for Houston leaders ([their world: energy / TMC / legal / PE] included). Your post on [specific thing] was sharp / We share [mutual, group, event]. Connecting to follow your work — no pitch, no deck.

Rules: personalize one concrete detail or send fewer requests; never mention our pricing/service in an invite; skip the note only for warm cases (they engaged with us first).
**Caveat:** LinkedIn caps weekly invitations and doesn't publish the number (community-observed range is roughly 100–200/week). At 30/day × 5 days we may hit it; if LinkedIn warns, drop to 20/day and prioritize post-engagers. Acceptance rate on the scorecard tells us if notes are working — falling acceptance means fix targeting/note, not push volume.

### b) 10 substantive comments/day on target-audience posts
"Substantive" = adds a fact, a framework, a genuinely useful question, or a respectful counterpoint. 2+ sentences. Never "Great post!", never a pitch, never a link.
Where: a curated list of ~50 Houston executives, 10 EA/operations voices, 5 competitor-adjacent creators; plus whatever the feed surfaces from targets. Comments are distribution (§7.9) and they're also simply how a chief-of-staff brain proves itself in public.
Timing: cluster some comments in the 15 minutes before and after our own post goes live [practitioner advice — contentin.io, 2025-12-27; anecdotal].

### c) Reply to every comment on our posts within 2 hours (working hours)
Replies count as engagement and extend a post's life [meikuio.com, 2026-06-06]. Substantive replies only; ask one question back where natural. Post-day: stay 30–60 minutes after publishing.

### d) DM etiquette
- **Never pitch on connect.** Nothing commercial in a first message, ever.
- After connecting: one genuine message referencing their world, or nothing. Silence is fine; a template blast is not.
- Let them raise the business first when possible. If a conversation is clearly about their support needs, offer value first (send the delegation playbook or the three-lists exercise, free, no gate).
- **Moving to a fit call — the only approved motion:** when they describe a pain we solve, name it back, then: "Happy to talk it through properly if useful — we do a 20-minute fit call, no charge and no obligation. Or I can just send you our pricing page; everything's published." Giving the self-serve option every time is the transparency brand *in the DM*.
- If they say no or go quiet: one graceful close, no follow-up sequence.

### e) Weekly (Friday, 20 min)
Fill the scorecard (§11), prune the target list, log which posts drew target-audience comments (not just volume), pick next week's posts from the bank (`build_calendar.mjs` proposes; founder disposes).

---

## 10. Profile and page optimization

### Founder headline — formulas (pick one, A/B at day 30)
- `Founder, [BrandName] — Houston's fractional executive assistant firm | Senior, US-based EAs for energy, healthcare, legal & private capital | Published pricing`
- `Fractional executive assistants for Houston leaders | 20/40/60 hrs/mo, month-to-month, pricing on the site | Founder, [BrandName]`
- `I match Houston executives with senior EAs — published pricing, no lock-in | Founder, [BrandName]`

Principles: category + city + differentiator ("published pricing" is the pattern-break); no "helping X achieve Y" filler; searchable terms ("fractional executive assistant", "Houston") because the headline is indexed.

### About section outline (first 3 lines carry the fold)
1. The gap, in one line: national EA firms treat Houston like a zip code; local options are thin.
2. What we do: senior (8–15+ yrs), US-based, Houston-rooted EAs — energy, healthcare/TMC, legal, private capital — matched in ≤5 business days.
3. The terms, because they're the point: $1,200/20h · $2,300/40h · $3,300/60h · month-to-month · no buyout fee · 2-week guarantee.
4. How it works (fit call → meet 2 EAs → 30-Day Delegation Playbook).
5. Who it's for / not for (honest anti-ICP line: <10 hrs/mo task work isn't us).
6. Founder line: why Houston, why this firm, in first person.
7. CTA: pricing page (self-serve) + book a 20-minute fit call.

### Featured section
1. **Pricing page** (the differentiator as a permanent exhibit)
2. **30-Day Delegation Playbook** (lead magnet → /resources/what-to-delegate-first)
3. Best-performing build-log or dirty-laundry post (rotate monthly)

### Banner
Design register per build brief §5 (deep navy/charcoal, serif headline, no headset stock photos). Text: **"Houston's fractional executive assistant firm — senior EAs, published pricing, month-to-month."** Sub-line: "Energy · Healthcare · Legal · Private Capital". Skyline imagery, licensed.

### Company page basics (a shell, kept honest)
Complete profile (logo, banner, About using the positioning statement, website, Houston HQ, services listed); posts = weekly repost of the founder's best post + firm announcements; no separate content strategy at launch. Rationale: §7.4 — the founder profile is the engine. Employees (EAs, as hired) linked to the page for legitimacy. Page follower count is explicitly not a KPI.

---

## 11. Measurement

### Weekly scorecard (copy into a sheet; one row per week)

| Week of | Posts planned/published | Profile views | Connect sent | Accepted | Accept % | Comments made | Comments received | Median 2h reply hit? | Inbound DMs (target-audience) | Fit-call offers made | Fit calls booked | Notes: best post / worst post / one change |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Plus per-post log: id, date, format, pillar, impressions, comments-from-targets (count actual ICP humans — 5 target comments beat 50 random likes).

### What "working" looks like — without invented numbers
- **Day 30:** cadence held (≥12 posts published); routine held (connects + comments ≥80% of days); baseline established for every KPI; ≥1 organic conversation with a target-audience executive that we didn't start. If acceptance rate is falling week-over-week, fix targeting before scaling anything.
- **Day 60:** every KPI has a 4-week trailing baseline and ≥2 KPIs trending up vs it; inbound DMs from targets are happening at all (any nonzero, sustained); at least one post generated a fit-call booking we can trace. Poll follow-ups and carousel experiments evaluated against our own medians.
- **Day 90:** LinkedIn is measurably feeding the strategy-doc funnel (40+ discovery calls across all channels): we can name which posts/conversations produced which calls. If LinkedIn-sourced fit calls are zero at day 90 with the routine genuinely executed, the content strategy gets rebuilt — that's a real kill criterion, stated now.

### The public-claim rule (from the strategy doc, verbatim in spirit)
Any number we state publicly — hours saved, match time, acceptance rates, "what's working" — must be **measured, with the measurement window stated, and dated**. Corrections are appended as new dated posts, never silent edits. If we don't have the number, we say we don't have the number.

---

## 12. Hard rules

1. **Never fabricate proof.** No invented clients, testimonials, metrics, engagement stats, or "results." Placeholders stay placeholders until reality fills them.
2. **Composites are labeled composites, in the body, every time.** Composites never carry metrics.
3. **Real client material requires written permission**; identifying detail requires explicit sign-off.
4. **Every competitor claim carries a source** (URL in `sources`, "(source in comments)" in body, link pasted as first comment with a last-verified date). No sourced fact, no claim. Competitors are named only with sourced facts, and their documented strengths get credited.
5. **Pricing appears exactly as published:** $1,200/20h · $2,300/40h · $3,300/60h (+add-ons as listed). Any change is announced with reasoning the week it happens.
6. **Public numbers are measured and dated; corrections are new posts,** never quiet edits.
7. **No engagement bait:** no "Agree?", no tag-bait, no fake cliffhangers, no obvious-answer polls. Every poll gets its promised follow-up.
8. **Never pitch on connect; never pitch in a first DM.** Fit-call offers only after a real conversation, always alongside the self-serve pricing link.
9. **No posting about clients' industries' confidential matters** — sector fluency, never sector gossip. Nothing under NDA ever appears in content or goes into AI tools.
10. **Stay in the lane:** every post belongs to one of the six pillars. No politics, no off-topic virality, no commentary outside executive support.
11. **Reply to every comment within 2 working hours**; every commenter is treated as a future client, referrer, or EA candidate.
12. **Founder's voice, founder's edit.** AI may draft; nothing ships unread or sounding machine-made.
13. **Banned-word list is enforced** (§3), including in comments and DMs.
14. **Weekends off** (light commenting optional). Sustainable beats heroic; the cadence is the strategy.

---

## Appendix: research sources relied on in this playbook

- ContentIn — LinkedIn Engagement Benchmarks (100K+ posts, medians): https://contentin.io/blog/linkedin-engagement-benchmarks/ (2025-12-09)
- ContentIn — LinkedIn Algorithm 2025/2026 (reach drop, topic fingerprint, comments; practitioner): https://contentin.io/blog/linkedin-algorithm-2025-why-your-reach-dropped-how-to-win-in-2026/ (2025-12-27)
- Metricool — 2026 LinkedIn Study press release (673K posts; profiles vs pages; formats; polls): https://metricool.com/press-release-linkedin-study-2026/ (2026-04-14)
- Social Media Today — Socialinsider company-page report (1M posts; carousels lead): https://www.socialmediatoday.com/news/linkedin-company-pages-best-practices-2025-socialinsider/745350/ (2025-04-14)
- Remery — January 2025 algorithm update, engagement bait vs knowledge content (practitioner, small sample): https://remery.ai/blog/linkedin-algorithm-changes-2026-founders (2025-11-14)
- Postiv — 360Brew / dwell time (LinkedIn-confirmed portions flagged), hashtags: https://postiv.ai/blog/linkedin-algorithm-2026 (2026-03-14)
- Ordinal — link-penalty study synthesis (contested; company pages vs profiles): https://www.tryordinal.com/blog/linkedin-link-penatly-study (2026-08-08)
- MagicPost — 1.2M-post analysis (length, links/preview cards, hashtags, AI-sounding text; practitioner): https://magicpost.in/blog/linkedin-algorithm-2026 (2026-06-05)
- Meiku — algorithm myths vs data (formats, first-comment links weakening, cadence; practitioner): https://meikuio.com/linkedin-algorithm-2026/ (2026-06-06)
- AuthoredUp — algorithm guide (hashtag pages disabled Oct 2024; link handling): https://authoredup.com/blog/linkedin-algorithm (updated 2025–2026)
- Hootsuite — best time to post 2025 data: https://blog.hootsuite.com/best-time-to-post-on-linkedin/ (2025-11-19)
- Reachly — B2B posting-time synthesis + test protocol: https://www.reachly.co/blogs/best-time-to-post-on-linkedin-b-2-b (2026-06-08)

Anecdotal/practitioner claims are marked as such where cited. No engagement statistic in this playbook is invented; where magnitude is unverified (e.g., the "+70% comment adjacency" claim), it is flagged.
