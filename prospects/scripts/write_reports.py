#!/usr/bin/env python3
"""
write_reports.py — generate prospects/verification-log.md and prospects/outreach-segments.md
from prospects/verify/*.json. Reproducible: never hand-edit the generated files; re-run instead.
Appends a dated run block to verification-log.md (append-only history) and fully regenerates
outreach-segments.md (it is a view, not a record).
"""
import glob
import json
import os
import time
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "verify")
NOW = time.strftime("%Y-%m-%d %H:%M %Z")
TODAY = time.strftime("%Y-%m-%d")


def load(n):
    p = os.path.join(V, n)
    return json.load(open(p)) if os.path.exists(p) else []


def main():
    ver, par, rej = load("verified.json"), load("partial.json"), load("rejected.json")
    raw_files = sorted(glob.glob(os.path.join(ROOT, "raw", "*.json")))
    patch_files = sorted(glob.glob(os.path.join(ROOT, "raw", "patches", "*.json")))
    seg_counts = {}
    for p in raw_files:
        j = json.load(open(p))
        seg_counts[j.get("segment", os.path.basename(p))] = (len(j.get("candidates", [])), len(j.get("rejected", [])))

    # ---------------- verification log (append-only)
    hist = Counter()
    for r in par:
        for reason in r.get("reasons", []):
            if not reason.startswith("note:"):
                hist[reason.split("(")[0].strip()[:70]] += 1
    rej_hist = Counter()
    for r in rej:
        rs = r.get("reasons") or []
        rej_hist[(rs[0] if rs else "unknown").split("(")[0][:70]] += 1
    email_kind = Counter((r.get("verification") or {}).get("evidence", {}).get("email_kind") for r in ver)
    discovered = sum(1 for r in ver if r.get("company_email_discovered_by") or r.get("contact_email_discovered_by") or r.get("phone_discovered_by"))
    patched = sum(1 for r in ver if r.get("patched_fields"))
    manual = sum(1 for r in ver if r.get("manual_check"))

    block = [f"\n## Run {NOW}\n",
             f"- Raw research files: {len(raw_files)}; enrichment patch files: {len(patch_files)}",
             "- Candidates per segment (candidates / researcher-rejected): " + "; ".join(f"{k} {a}/{b}" for k, (a, b) in seg_counts.items()),
             f"- **Verified: {len(ver)}** · Partially Verified: {len(par)} · Rejected (incl. researcher-rejected and duplicates): {len(rej)}",
             f"- Verified rows by email kind: " + ", ".join(f"{k or 'none'} {v}" for k, v in email_kind.most_common()),
             f"- Verified rows where the verifier itself discovered the phone/email on the official site: {discovered}",
             f"- Verified rows that needed an enrichment patch: {patched}; rows confirmed by browser spot-check: {manual}",
             "", "### Why rows are Partially Verified (gate failures)", ""]
    block += [f"- {v:3d} · {k}" for k, v in hist.most_common()]
    block += ["", "### Why rows are Rejected (top reasons)", ""]
    block += [f"- {v:3d} · {k}" for k, v in rej_hist.most_common(12)]
    block += ["", "### Method notes", "",
              "- Gates G1–G8 as defined in README.md; a row is Verified only when G1–G6 all pass and G7–G8 are not fatal.",
              "- Email verification = published on an official page (raw HTML incl. mailto: and decoded Cloudflare-protected addresses) + MX present via DNS-over-HTTPS. No SMTP mailbox probing (no SMTP egress from the build environment).",
              "- Phone verification = formatted 10-digit match or tel: link on the company's own pages or the cited source page.",
              "- Values the verifier discovered itself carry `*_discovered_by` = verifier_scan_<date> and the page URL as source.",
              "- Values from enrichment patches carry `patched_fields`; browser confirmations carry `manual_check` with the rendered URL.",
              "- Nothing was estimated. Nulls remain nulls. Rejected and Partially Verified rows are retained with reasons."]
    log_path = os.path.join(ROOT, "verification-log.md")
    if not os.path.exists(log_path):
        with open(log_path, "w") as f:
            f.write("# Verification Log — prospects/\n\nAppend-only. Each run adds a dated block; earlier blocks are never edited.\n")
    with open(log_path, "a") as f:
        f.write("\n".join(block) + "\n")

    # ---------------- outreach segments (regenerated view)
    by_tier = defaultdict(list)
    for r in ver:
        by_tier[r.get("suggested_tier") or "Unassigned"].append(r)
    by_vert = Counter(r.get("vertical") for r in ver)
    by_metro = Counter(r.get("metro") for r in ver)
    by_trig = Counter(r.get("trigger_signal") for r in ver)
    hot = [r for r in ver if r.get("trigger_signal") == "hiring_ea"]
    named = [r for r in ver if r.get("contact_email")]

    def row(r):
        who = f"{r.get('decision_maker_name')} ({r.get('decision_maker_title')})"
        ch = r.get("contact_email") or r.get("company_email") or "—"
        return f"| {r.get('company_name')} | {who} | {r.get('metro')} | {r.get('vertical')} | {r.get('trigger_signal')} | {ch} | {r.get('phone') or '—'} |"

    hdr = "| Company | Decision-maker | Metro | Vertical | Trigger | Email | Phone |\n|---|---|---|---|---|---|---|"
    out = [f"# Outreach Segments — generated {NOW}", "",
           f"View over the **{len(ver)} Verified** rows in `prospects.xlsx` (sheet: Verified). Regenerate with `python3 prospects/scripts/write_reports.py`. Nothing here has been contacted; outreach is a human action per the founder-led LinkedIn + referral plan (strategy.md, GTM channels 1–2).", "",
           "## Counts", "",
           "**By metro:** " + ", ".join(f"{k} {v}" for k, v in by_metro.most_common()), "",
           "**By vertical:** " + ", ".join(f"{k} {v}" for k, v in by_vert.most_common()), "",
           "**By trigger:** " + ", ".join(f"{k} {v}" for k, v in by_trig.most_common()), "",
           "**By suggested tier:** " + ", ".join(f"{k} {len(v)}" for k, v in sorted(by_tier.items())), "",
           f"**Named decision-maker email published:** {len(named)} of {len(ver)}", "",
           "## Wave 1 — actively hiring an EA right now", "",
           "Highest intent. Pitch: senior support matched in 5 business days, month-to-month, versus a 4–8 week W-2 search. Lead with the tier that matches the posted role's scope.", "",
           hdr] + [row(r) for r in hot] + ["",
           "## Wave 2 — named decision-maker email published (direct outreach possible)", "",
           "These executives publish their own address on an official page; a short, specific note referencing the trigger event is appropriate. Pair with a LinkedIn connection request.", "",
           hdr] + [row(r) for r in named if r not in hot] + ["",
           "## Wave 3 — general inbox + LinkedIn (warm the founder first)", "",
           "Company publishes only a general inbox. Use LinkedIn founder-led outreach first; the inbox is for the follow-up with the Delegation Playbook attached.", "",
           hdr] + [row(r) for r in ver if r not in hot and r not in named] + ["",
           "## By suggested tier", ""]
    for tier in ("Chief of Staff", "Executive", "Foundation", "Unassigned"):
        rows = by_tier.get(tier, [])
        if rows:
            out += [f"### {tier} ({len(rows)})", "", hdr] + [row(r) for r in rows] + [""]
    out += ["## Handling notes", "",
            "- Rows carrying a `size risk` note in the workbook's Verification notes column need a headcount confirmation before pitching (LinkedIn band upper bound > 150).",
            "- Rows noting an existing EA on the team page: pitch backup coverage / overflow, not replacement.",
            "- Texas-expansion rows (DFW, Austin, San Antonio) are virtual-only prospects; do not offer the in-person day add-on.",
            "- Re-verify any row older than 60 days before use; EA postings close within weeks."]
    with open(os.path.join(ROOT, "outreach-segments.md"), "w") as f:
        f.write("\n".join(out) + "\n")
    print(f"verification-log.md appended; outreach-segments.md written ({len(ver)} verified, {len(hot)} hiring_ea, {len(named)} named emails)")


if __name__ == "__main__":
    main()
