# First 30 Days on LinkedIn — Day-by-Day Calendar

**Window:** Monday 2026-09-07 → Tuesday 2026-10-06 (30 days). Post IDs reference `post-bank.json` / `post-bank.md`.
**Posting time:** 7:30–9:00 AM CT (see playbook §8 — weak-evidence lever; never skip a post to hit the slot).
**Daily engagement block (every weekday, ~20 min + reply windows):** 30 targeted connection requests with personalized note · 10 substantive comments on target-audience posts · reply to every comment on our posts within 2 working hours · stay 30–60 min after posting. Abbreviated below as **ENG**.
**Weekends:** off, or a light 10-minute comment pass. No posts (weekend engagement drops 50–70% per B2B studies — playbook §8).

Rules that override this calendar: build-log posts with `[INSERT]` placeholders publish **only when real content exists** — otherwise swap in the listed alternate. Never publish an unfilled placeholder.

---

## Week 1 — Setup and launch (Sep 7–13) · 3 posts

| Date | Day | Post | Pillar / Format | Tasks |
|---|---|---|---|---|
| Sep 7 | Mon | — (Labor Day — feed is quiet; use it) | — | Setup day: founder profile per playbook §10 (headline, About, Featured with pricing page + playbook, banner); create company page; build target list (~150 Houston execs across the 5 sectors + 15 creators to comment on); set up scorecard sheet |
| Sep 8 | Tue | **P051** — "I'm building Houston's fractional EA firm. In public." | build log / build_log_update | ENG. Launch day: personally message (not blast) 10–20 warm contacts asking them to weigh in honestly |
| Sep 9 | Wed | **P021** — "Our pricing is on the website. All of it." | transparency / short_text | ENG. Paste source + pricing link as first comment |
| Sep 10 | Thu | **P001** — "Delegate your calendar before your inbox." | delegation / short_text | ENG |
| Sep 11 | Fri | — | — | ENG. **Weekly review #1:** fill scorecard (baseline week); check invite acceptance %; confirm next week's 4 posts |
| Sep 12–13 | Sat–Sun | — | — | Off / optional 10-min comment pass |

## Week 2 — Full rhythm begins (Sep 14–20) · 4 posts (+1 optional)

| Date | Day | Post | Pillar / Format | Tasks |
|---|---|---|---|---|
| Sep 14 | Mon | **P002** — "Seven handoffs for your first 30 days with an EA." | delegation / listicle | ENG. Playbook download link as first comment |
| Sep 15 | Tue | **P015** — "Hurricane season is an executive continuity problem." | Houston life / listicle | ENG. Topical: mid-September is peak season — pin this one to Featured if it lands |
| Sep 16 | Wed | **P031** — "The biggest name in EA services won't tell you the price." | dirty laundry / contrarian | ENG. **Sources as first comment (required)** |
| Sep 17 | Thu | **P041** — "How we vet an EA before you ever meet them." | bench / listicle | ENG |
| Sep 18 | Fri | *(optional)* **P052** — "We published pricing before we had a single client." | build log | ENG. **Weekly review #2:** scorecard; which posts drew ICP comments; prune/expand target list |
| Sep 19–20 | Sat–Sun | — | — | Off / light |

## Week 3 — All six pillars in play (Sep 21–27) · 4 posts (+1 optional)

| Date | Day | Post | Pillar / Format | Tasks |
|---|---|---|---|---|
| Sep 21 | Mon | **P006** — "Track one week. Sort it into three lists." | delegation / short_text | ENG |
| Sep 22 | Tue | **P012** — "A week with an EA, if you're a physician-executive at TMC." | Houston life (healthcare) / vignette | ENG. Target list focus this week: TMC / physician-executives |
| Sep 23 | Wed | **P024** — "Our contract, in ten plain-English lines." | transparency / short_text | ENG |
| Sep 24 | Thu | **P046** — "AI didn't lower the bar for EAs. It raised it." | bench / contrarian | ENG |
| Sep 25 | Fri | *(optional — only if real numbers exist)* **P055** — "Build log: the real numbers, dated." Alternate if not: skip. | build log | ENG. **Weekly review #3:** scorecard; first read on acceptance-rate trend; decide whether Friday posts continue |
| Sep 26–27 | Sat–Sun | — | — | Off / light |

## Week 4 — Steady state + first poll (Sep 28–Oct 4) · 4 posts (+1 optional)

| Date | Day | Post | Pillar / Format | Tasks |
|---|---|---|---|---|
| Sep 28 | Mon | **P009** — "Five signs you're the bottleneck in your own company." | delegation / listicle | ENG |
| Sep 29 | Tue | **P011** — "A week with an EA, if you run an energy business unit." | Houston life (energy) / vignette | ENG. Target list focus: Energy Corridor / energy VPs |
| Sep 30 | Wed | **P033** — "The $10,000 fee nobody mentions on the sales call." | dirty laundry / short_text | ENG. **Source as first comment (required)** |
| Oct 1 | Thu | **P007** — "What's the hardest thing to hand off?" | delegation / **poll** (runs 1 week) | ENG. Calendar reminder: follow-up post due ~Oct 8 (write fresh from results — not in bank) |
| Oct 2 | Fri | *(optional)* **P056** — "Month-to-month means clients can fire us monthly." | build log | ENG. **Weekly review #4:** scorecard; per-post log complete for all posts to date |
| Oct 3–4 | Sat–Sun | — | — | Off / light |

## Week 5 (partial) — Day 29–30 + retrospective (Oct 5–6)

| Date | Day | Post | Pillar / Format | Tasks |
|---|---|---|---|---|
| Oct 5 | Mon | **P043** — "The best EAs spend week one mostly listening." | bench / story | ENG |
| Oct 6 | Tue | **P010** — "The most underrated EA deliverable: the meeting prep pack." | delegation / short_text | ENG. **30-day retrospective** (below) |

---

## 30-day retrospective checklist (Oct 6)

- [ ] Cadence: ≥12 posts published (target was 15–18 incl. optionals). If missed, diagnose honestly: time, fear, or process?
- [ ] Routine: engagement block executed ≥80% of weekdays?
- [ ] Baselines recorded for every scorecard KPI (these are now the bar — playbook §11)
- [ ] Which 3 posts drew the most **target-audience** comments? Which pillar/format were they? Feed that into weeks 5–8.
- [ ] Connection acceptance rate trend: up, flat, or down? If down, rewrite the note template before increasing volume.
- [ ] Any inbound DMs from ICP? Any fit-call offers made / booked? (Zero is data at day 30, not failure — see day-60/90 gates.)
- [ ] Poll P007 follow-up published?
- [ ] All dirty-laundry posts have their source comment in place?
- [ ] No unfilled placeholders published? No unlabeled composites? (Audit every published post against playbook §12.)
- [ ] Generate weeks 5–8: `node scripts/linkedin/build_calendar.mjs --start 2026-10-12 --weeks 4 --exclude <all published ids>`

## Bank posts intentionally held back (weeks 5+)

Strong openers reserved so the bank doesn't front-load: P013 (OTC — best run in winter, pre-OTC), P019 (NAPE — run January), P022 (pricing-math carousel — run after pricing post has baseline), P028 (objections poll), P040 (fine-print carousel), P045/P047/P048 (bench series), P053/P054/P058 (build-log posts that need real material), P059 (kill criteria — pair with a real milestone), P060 (why founder-profile — good week-6 meta post).
