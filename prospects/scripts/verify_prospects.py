#!/usr/bin/env python3
"""
verify_prospects.py — maximum-scrutiny verification pass for EA Consulting Houston prospects.

Input : prospects/raw/*.json   (one file per research segment; see SCHEMA.md)
Output: prospects/verify/verified.json          rows that passed every gate
        prospects/verify/partial.json           rows missing one or more gates (with reasons)
        prospects/verify/rejected.json          rows that failed a fatal gate or were duplicates
        prospects/verify/checks.json            raw per-row check results (audit trail)
        prospects/verify/fetch_cache/           cached page bodies keyed by URL hash

Gates (a row is VERIFIED only if every gate is True):
  G1 website_live        final HTTP status < 400 after redirects (403/429/503 bot-blocks are recorded
                         as 'blocked' and handled by the browser spot-check step, not auto-passed)
  G2 name_on_official    decision-maker surname appears on at least one fetched non-LinkedIn source page
  G3 two_title_sources   >= 2 distinct-domain title_sources, at least one fetchable or a well-formed
                         linkedin.com/in/ URL
  G4 phone_verified      a phone is present AND its 10 digits appear on the company website
                         (home/contact) or on the cited phone_source page
  G5 email_verified      an email (contact_email preferred, else company_email) is present AND
                         (a) it appears on the cited source page or company site, and
                         (b) its domain publishes MX records (DNS-over-HTTPS), and
                         (c) it is not a free-mail domain unless the website itself is free-mail based
  G6 trigger_sourced     trigger_source URL fetchable (or LinkedIn/Indeed shape) AND trigger_detail present
  G7 metro_in_scope      metro in {Houston, DFW, Austin, San Antonio}
  G8 icp_size_band       employee_count_estimate parses to a range overlapping 5–150, or is null
                         with a note (null is allowed but flagged, never guessed)

Nothing is ever filled in. Missing values stay null; failures carry a reason string.
"""
import concurrent.futures as cf
import glob
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.parse as up

import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw")
OUT = os.path.join(ROOT, "verify")
CACHE = os.path.join(OUT, "fetch_cache")
os.makedirs(CACHE, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
HEADERS = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.9"}
TIMEOUT = 20
FREE_MAIL = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "icloud.com",
             "me.com", "live.com", "msn.com", "comcast.net", "att.net", "sbcglobal.net"}
METROS = {"Houston", "DFW", "Austin", "San Antonio"}
UNFETCHABLE_OK = ("linkedin.com", "indeed.com", "glassdoor.com", "ziprecruiter.com",
                  "adviserinfo.sec.gov", "texasbar.com", "npiregistry.cms.hhs.gov", "crunchbase.com")

PULL_DATE = time.strftime("%Y-%m-%d")

# Published addresses that are NOT outreach channels — refused even when found on an official page.
NON_OUTREACH_LOCALPARTS = ("privacy", "opt-out", "optout", "unsubscribe", "noreply", "no-reply", "donotreply",
                           "legal", "dmca", "abuse", "compliance", "webmaster", "postmaster", "billing", "careers", "jobs")
EXCLUDED_EMAILS = {
    "verdeir@icrinc.com": "third-party investor-relations agency inbox (icrinc.com), not the company's own channel",
}


# ----------------------------------------------------------------------------- fetch
def _key(url):
    return hashlib.sha1(url.encode()).hexdigest()


def fetch(url):
    """Return dict(status, final_url, text, blocked, error). Cached on disk."""
    if not url or not isinstance(url, str) or not url.startswith("http"):
        return {"status": None, "final_url": None, "text": "", "blocked": False, "error": "no_url"}
    p = os.path.join(CACHE, _key(url) + ".json")
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    res = {"status": None, "final_url": None, "text": "", "blocked": False, "error": None}
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        res["status"] = r.status_code
        res["final_url"] = r.url
        body = r.text if "text" in r.headers.get("content-type", "") or "json" in r.headers.get("content-type", "") else ""
        res["text"] = body[:600000]
        low = body[:30000].lower()
        challenge = ("cf-chl" in low or "just a moment..." in low or "verify you are human" in low
                     or "attention required" in low or "access denied" in low
                     or ("captcha" in low and len(norm_text(body)) < 1500))
        if r.status_code in (401, 403, 429, 503, 999, 202) or challenge:
            res["blocked"] = True
    except requests.RequestException as e:
        res["error"] = type(e).__name__
    with open(p, "w") as f:
        json.dump(res, f)
    return res


def domain(url):
    try:
        host = up.urlparse(url if "://" in url else "https://" + url).netloc.lower()
        return host[4:] if host.startswith("www.") else host
    except Exception:
        return ""


def mx_present(dom):
    p = os.path.join(CACHE, "mx_" + dom + ".json")
    if os.path.exists(p):
        return json.load(open(p))
    ok = False
    try:
        r = requests.get("https://cloudflare-dns.com/dns-query", params={"name": dom, "type": "MX"},
                         headers={"accept": "application/dns-json"}, timeout=15)
        j = r.json()
        ok = any(a.get("type") == 15 for a in j.get("Answer", []) or [])
        if not ok:  # some domains use only A record mail; treat as unverified (strict)
            ok = False
    except Exception:
        ok = None
    json.dump(ok, open(p, "w"))
    return ok


def norm_text(t):
    t = html.unescape(t or "")
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t).lower()


def digits(phone):
    d = re.sub(r"\D", "", phone or "")
    if len(d) == 11 and d.startswith("1"):
        d = d[1:]
    return d if len(d) == 10 else None


def phone_in(text, d):
    if not d or not text:
        return False
    if d in re.sub(r"\D", "", text):
        # guard: the raw digit stream can accidentally contain the number; require a formatted match too
        pat = r"\(?%s\)?[\s.\-]*%s[\s.\-]*%s" % (d[:3], d[3:6], d[6:])
        return re.search(pat, text) is not None
    return False


def email_in(text, email):
    if not email or not text:
        return False
    e = email.lower()
    if e in text:
        return True
    # obfuscated forms: "name [at] domain", "name(at)domain", entity-encoded
    local, _, dom = e.partition("@")
    obf = re.escape(local) + r"\s*[\[\(\{]?\s*(at|@)\s*[\]\)\}]?\s*" + re.escape(dom)
    return re.search(obf, text) is not None


def contact_pages(site_html, base):
    """Find likely contact/about/team page links on the homepage."""
    links = set()
    for m in re.finditer(r'href=["\']([^"\']+)["\']', site_html or ""):
        href = m.group(1)
        if href.startswith(("mailto:", "tel:", "#", "javascript:")):
            continue
        if re.search(r"contact|about|team|leadership|our-people|people|attorneys|professionals|providers|physicians|locations|firm", href, re.I):
            links.add(up.urljoin(base, href))
    return list(links)[:10]


EMAIL_RE = re.compile(r"[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}", re.I)
TEL_RE = re.compile(r"(?:\(\d{3}\)\s?|\b\d{3}[\s.\-])\d{3}[\s.\-]\d{4}\b")


def decode_cfemail(raw):
    """Decode Cloudflare email-protection tokens (data-cfemail / /cdn-cgi/l/email-protection#hex)."""
    out = []
    for hx in re.findall(r'(?:data-cfemail="|email-protection#)([0-9a-fA-F]{8,})', raw or ""):
        try:
            b = bytes.fromhex(hx)
            out.append("".join(chr(x ^ b[0]) for x in b[1:]))
        except ValueError:
            pass
    return out


def discover_contacts(raw_pages, site_dom):
    """Scan raw HTML of company-domain pages for published emails/phones.
    Returns ({email: source_url}, {digits: (formatted, source_url)}) — only same-domain emails."""
    emails, phones = {}, {}
    for url, raw in raw_pages.items():
        if not raw or domain(url) != site_dom:
            continue
        txt = html.unescape(raw) + " " + " ".join("mailto:" + e for e in decode_cfemail(raw))
        for m in re.finditer(r'mailto:([^"\'?\s>]+)', txt, re.I):
            e = m.group(1).strip().lower()
            if EMAIL_RE.fullmatch(e) and (e.split("@")[1] == site_dom or e.split("@")[1].endswith("." + site_dom)):
                emails.setdefault(e, url)
        for e in EMAIL_RE.findall(txt):
            e = e.lower()
            if e.split("@")[1] == site_dom and not re.search(r"\.(png|jpg|gif|svg|webp|js|css)$", e):
                emails.setdefault(e, url)
        for m in re.finditer(r'tel:\+?1?([\d\-\.\(\)\s]{10,16})', txt, re.I):
            d = digits(m.group(1))
            if d:
                phones.setdefault(d, (f"({d[:3]}) {d[3:6]}-{d[6:]}", url))
        for m in TEL_RE.finditer(re.sub(r"<[^>]+>", " ", txt)):
            d = digits(m.group(0))
            if d and d[:3] not in ("000", "555") and not d.startswith("1"):
                phones.setdefault(d, (f"({d[:3]}) {d[3:6]}-{d[6:]}", url))
    return emails, phones


def pick_email(emails):
    """Prefer general business inboxes; fall back to first found. Never pick noreply/webmaster/privacy."""
    bad = NON_OUTREACH_LOCALPARTS + ("hr@", "example")
    cands = [e for e in emails if not any(b in e.split("@")[0] for b in bad)]
    if not cands:
        return None
    pref = ("info@", "contact@", "hello@", "office@", "admin@", "inquiries@", "frontdesk@", "reception@")
    for p in pref:
        for e in cands:
            if e.startswith(p):
                return e
    return sorted(cands)[0]


def parse_range(s):
    if not s:
        return None
    nums = [int(x.replace(",", "")) for x in re.findall(r"\d[\d,]*", str(s))]
    if not nums:
        return None
    if len(nums) == 1:
        return (nums[0], nums[0])
    return (min(nums), max(nums))


# ----------------------------------------------------------------------------- verify one row
def verify_row(row):
    c = {"company_name": row.get("company_name"), "gates": {}, "reasons": [], "evidence": {}}
    site = row.get("website") or ""
    site_dom = domain(site)

    # G1 website live
    home = fetch(site)
    if home["status"] and home["status"] < 400 and not home["blocked"]:
        c["gates"]["G1_website_live"] = True
    elif home["blocked"]:
        c["gates"]["G1_website_live"] = "blocked"
        c["reasons"].append(f"G1 website bot-blocked (HTTP {home['status']}); needs browser spot-check")
    else:
        c["gates"]["G1_website_live"] = False
        c["reasons"].append(f"G1 website not reachable (HTTP {home['status']}, {home['error']})")
    c["evidence"]["website_status"] = home["status"]
    c["evidence"]["website_final_url"] = home["final_url"]

    corpus_pages, raw_pages = {}, {}
    raw_pages[site] = home["text"]
    corpus_pages[site] = norm_text(home["text"])
    if home["text"]:
        for u in contact_pages(home["text"], home["final_url"] or site):
            if domain(u) == site_dom:
                f = fetch(u)
                raw_pages[u] = f["text"]
                corpus_pages[u] = norm_text(f["text"])
    for key in ("phone_source", "contact_email_source", "company_email_source", "address_source"):
        u = row.get(key)
        if u and u not in corpus_pages:
            f = fetch(u)
            raw_pages[u] = f["text"]
            corpus_pages[u] = norm_text(f["text"])
    for u in (row.get("title_sources") or []):
        if u and u not in corpus_pages and not any(x in u for x in ("linkedin.com",)):
            f = fetch(u)
            raw_pages[u] = f["text"]
            corpus_pages[u] = norm_text(f["text"])

    # --- script-side discovery: fill missing phone/email ONLY from the company's own pages, with source
    disc_emails, disc_phones = discover_contacts(raw_pages, site_dom)
    c["evidence"]["discovered_emails"] = list(disc_emails)[:8]
    c["evidence"]["discovered_phones"] = [v[0] for v in disc_phones.values()][:5]
    name0 = (row.get("decision_maker_name") or "").strip()
    sur0 = re.sub(r"[^a-z]", "", name0.split()[-1].lower()) if name0 else ""
    first0 = re.sub(r"[^a-z]", "", name0.split()[0].lower()) if name0 else ""
    # raw-HTML corpus (mailto hrefs + decoded cf-emails) for on-page email checks
    raw_corpus = " ".join((html.unescape(v or "") + " " + " ".join(decode_cfemail(v))).lower() for v in raw_pages.values())
    # (a) surname-matched published address on the company's own site → named contact_email
    if sur0 and len(sur0) > 2 and not row.get("contact_email"):
        for e, src in disc_emails.items():
            local = e.split("@")[0]
            if sur0 in local or (first0 and len(first0) > 3 and local.startswith(first0)):
                row["contact_email"], row["contact_email_source"] = e, src
                row["contact_email_discovered_by"] = "verifier_scan_" + PULL_DATE
                c["reasons"].append("note: named email discovered by verifier on official site (surname match; source recorded)")
                break
    # (b) researcher email not on page but the site publishes a general inbox → substitute, with note
    for fld in ("contact_email", "company_email"):
        e0 = (row.get(fld) or "").lower()
        if e0 and "@" in e0 and e0 not in raw_corpus and not email_in(" ".join(corpus_pages.values()), e0):
            row[fld + "_unconfirmed"] = e0
            row[fld] = None
            c["reasons"].append(f"note: researcher {fld} {e0} not found on any fetched page; set null")
    if not (row.get("contact_email") or row.get("company_email")) and disc_emails:
        e = pick_email(disc_emails)
        if e:
            row["company_email"] = e
            row["company_email_source"] = disc_emails[e]
            row["company_email_discovered_by"] = "verifier_scan_" + PULL_DATE
            c["reasons"].append("note: company email discovered by verifier on official site (source recorded)")
    if not digits(row.get("phone")) and disc_phones:
        d0 = next(iter(disc_phones))
        row["phone"], row["phone_source"] = disc_phones[d0][0], disc_phones[d0][1]
        row["phone_discovered_by"] = "verifier_scan_" + PULL_DATE
        c["reasons"].append("note: phone discovered by verifier on official site (source recorded)")

    # G2 name on an official (non-LinkedIn) page
    name = (row.get("decision_maker_name") or "").strip()
    surname = name.split()[-1].lower() if name else ""
    surname = re.sub(r"[^a-z\-']", "", surname)
    found_on = [u for u, t in corpus_pages.items() if surname and len(surname) > 2 and surname in t and "linkedin.com" not in u]
    c["gates"]["G2_name_on_official"] = bool(found_on)
    c["evidence"]["name_found_on"] = found_on[:3]
    if not found_on:
        c["reasons"].append("G2 decision-maker surname not found on any fetched official page")

    # G3 two title sources
    ts = [u for u in (row.get("title_sources") or []) if isinstance(u, str) and u.startswith("http")]
    doms = {domain(u) for u in ts}
    usable = 0
    for u in ts:
        if "linkedin.com/in/" in u:
            usable += 1
        else:
            f = fetch(u)
            if f["status"] and f["status"] < 400 or f["blocked"] or any(x in u for x in UNFETCHABLE_OK):
                usable += 1
    c["gates"]["G3_two_title_sources"] = len(doms) >= 2 and usable >= 2
    c["evidence"]["title_sources_usable"] = usable
    if not c["gates"]["G3_two_title_sources"]:
        c["reasons"].append(f"G3 title sources insufficient ({len(doms)} domains, {usable} usable)")

    # G4 phone
    d = digits(row.get("phone"))
    if not d:
        c["gates"]["G4_phone_verified"] = False
        c["reasons"].append("G4 no 10-digit phone published")
    else:
        def tel_href(u):
            return any(digits(m) == d for m in re.findall(r'tel:\+?([\d\-\.\(\)\s]{10,16})', raw_pages.get(u) or "", re.I))
        where = [u for u, t in corpus_pages.items() if phone_in(t, d) or tel_href(u)]
        c["gates"]["G4_phone_verified"] = bool(where)
        c["evidence"]["phone_found_on"] = where[:3]
        if not where:
            c["reasons"].append("G4 phone not found on company site or cited source page")

    # G5 email
    email = row.get("contact_email") or row.get("company_email")
    email_kind = "named_direct" if row.get("contact_email") else ("company_general" if row.get("company_email") else None)
    c["evidence"]["email_kind"] = email_kind
    if email and "@" in email and (any(b in email.lower().split("@")[0] for b in NON_OUTREACH_LOCALPARTS) or email.lower() in EXCLUDED_EMAILS):
        c["gates"]["G5_email_verified"] = False
        c["reasons"].append(f"G5 published address {email} is not an outreach channel (privacy/legal alias or third-party inbox)")
    elif not email or "@" not in email:
        c["gates"]["G5_email_verified"] = False
        c["reasons"].append("G5 no published email")
    else:
        edom = email.lower().split("@")[-1]
        on_page = [u for u, t in corpus_pages.items()
                   if email_in(t, email) or email.lower() in (html.unescape(raw_pages.get(u) or "").lower() + " ".join(decode_cfemail(raw_pages.get(u) or "")).lower())]
        mx = mx_present(edom)
        free = edom in FREE_MAIL
        dom_match = (edom == site_dom) or site_dom.endswith(edom) or edom.endswith(site_dom)
        ok = bool(on_page) and mx is True and (not free or edom == site_dom)
        c["gates"]["G5_email_verified"] = ok
        c["evidence"]["email_found_on"] = on_page[:3]
        c["evidence"]["email_mx"] = mx
        c["evidence"]["email_domain_matches_site"] = dom_match
        if not on_page:
            c["reasons"].append("G5 email not found on cited source page or company site")
        if mx is not True:
            c["reasons"].append(f"G5 email domain {edom} has no MX record")
        if free and edom != site_dom:
            c["reasons"].append("G5 free-mail address does not match company domain")
        if not dom_match and ok:
            c["reasons"].append("note: email domain differs from website domain (verified on page, kept)")

    # G6 trigger
    tsrc = row.get("trigger_source") or ""
    if tsrc and row.get("trigger_detail"):
        f = fetch(tsrc)
        okt = (f["status"] and f["status"] < 400) or f["blocked"] or any(x in tsrc for x in UNFETCHABLE_OK)
        c["gates"]["G6_trigger_sourced"] = bool(okt)
        c["evidence"]["trigger_status"] = f["status"]
        if not okt:
            c["reasons"].append(f"G6 trigger source not reachable (HTTP {f['status']})")
    else:
        c["gates"]["G6_trigger_sourced"] = False
        c["reasons"].append("G6 trigger source or detail missing")

    # G7 metro
    c["gates"]["G7_metro_in_scope"] = row.get("metro") in METROS
    if not c["gates"]["G7_metro_in_scope"]:
        c["reasons"].append(f"G7 metro out of scope: {row.get('metro')}")

    # G8 size band
    rng = parse_range(row.get("employee_count_estimate"))
    if rng is None:
        c["gates"]["G8_icp_size_band"] = "null"
        c["reasons"].append("note: employee count not sourced (null kept, not estimated)")
    else:
        lo, hi = rng
        c["gates"]["G8_icp_size_band"] = not (hi < 5 or lo > 150)
        if not c["gates"]["G8_icp_size_band"]:
            c["reasons"].append(f"G8 employee count {row.get('employee_count_estimate')} outside 5–150")
        elif hi > 150:
            c["reasons"].append(f"note: size risk — band {row.get('employee_count_estimate')} upper bound exceeds 150; confirm headcount before pitching")
    if re.search(r"already (has|employs|lists) (a |an )?(dedicated )?(executive assistant|EA\b)", (row.get("notes") or "") + " " + (row.get("icp_fit_rationale") or ""), re.I):
        c["reasons"].append("note: researcher observed an existing EA on the team page — lower fit, pitch as backup/overflow")

    # manual (browser) confirmations — recorded by an enricher who rendered the page; still require MX for email
    mc = row.get("manual_check") or {}
    if mc:
        c["evidence"]["manual_check"] = mc
        if mc.get("website_live_confirmed") and c["gates"]["G1_website_live"] == "blocked":
            c["gates"]["G1_website_live"] = True
            c["reasons"] = [x for x in c["reasons"] if not x.startswith("G1")]
            c["reasons"].append(f"G1 confirmed live by browser spot-check {mc.get('checked_at')}")
        if mc.get("phone_seen") and digits(row.get("phone")) and digits(mc["phone_seen"]) == digits(row.get("phone")) and not c["gates"]["G4_phone_verified"]:
            c["gates"]["G4_phone_verified"] = True
            c["reasons"] = [x for x in c["reasons"] if not x.startswith("G4")]
            c["reasons"].append(f"G4 phone seen on rendered page {mc.get('checked_url')}")
        em = (row.get("contact_email") or row.get("company_email") or "").lower()
        if mc.get("email_seen") and em and mc["email_seen"].lower() == em and not c["gates"]["G5_email_verified"]:
            if mx_present(em.split("@")[-1]) is True:
                c["gates"]["G5_email_verified"] = True
                c["reasons"] = [x for x in c["reasons"] if x.startswith("G5") is False]
                c["reasons"].append(f"G5 email seen on rendered page {mc.get('checked_url')}; MX present")
        if mc.get("name_seen") and not c["gates"]["G2_name_on_official"]:
            c["gates"]["G2_name_on_official"] = True
            c["reasons"] = [x for x in c["reasons"] if not x.startswith("G2")]
            c["reasons"].append(f"G2 decision-maker seen on rendered page {mc.get('checked_url')}")

    # classification
    g = c["gates"]
    fatal = (g["G1_website_live"] is False) or (not g["G7_metro_in_scope"]) or (g["G8_icp_size_band"] is False)
    hard = [g["G1_website_live"] is True, g["G2_name_on_official"], g["G3_two_title_sources"],
            g["G4_phone_verified"], g["G5_email_verified"], g["G6_trigger_sourced"]]
    if fatal:
        c["status"] = "Rejected"
    elif all(hard):
        c["status"] = "Verified"
    else:
        c["status"] = "Partially Verified"
    c["confidence_score"] = round(100 * sum(1 for x in hard if x) / len(hard))
    c["verified_at"] = PULL_DATE
    return c


# ----------------------------------------------------------------------------- main
def main():
    rows, rejected_by_researchers = [], []
    for p in sorted(glob.glob(os.path.join(RAW, "*.json"))):
        with open(p) as f:
            j = json.load(f)
        seg = j.get("segment") or os.path.basename(p)[:-5]
        for r in j.get("candidates", []):
            r["_segment"] = seg
            rows.append(r)
        for r in j.get("rejected", []):
            r["_segment"] = seg
            r["status"] = "Rejected"
            r["reasons"] = ["researcher: " + (r.get("reason") or "no reason")]
            rejected_by_researchers.append(r)

    # --- apply enrichment patches (raw/patches/*.json). Each patch: {company_name, website, patch:{field: value,...},
    #     manual_check:{checked_url, checked_at, website_live_confirmed, phone_seen, email_seen}, enricher_note}
    #     Patches only ADD sourced values or manual confirmations; they never delete researcher data.
    patches = {}
    for p in sorted(glob.glob(os.path.join(RAW, "patches", "*.json"))):
        for pt in json.load(open(p)):
            k = domain(pt.get("website") or "") or (pt.get("company_name") or "").lower()
            patches.setdefault(k, []).append((os.path.basename(p), pt))
    new_rows = []
    for k, lst in patches.items():
        matched = False
        for r in rows:
            if (domain(r.get("website") or "") or (r.get("company_name") or "").lower()) == k:
                matched = True
                for fname, pt in lst:
                    for f, v in (pt.get("patch") or {}).items():
                        if f in ("contact_email", "company_email") and isinstance(v, str):
                            local = v.lower().split("@")[0]
                            if any(b in local for b in NON_OUTREACH_LOCALPARTS) or v.lower() in EXCLUDED_EMAILS:
                                r.setdefault("notes_verifier", []).append(
                                    f"patch email {v} refused: {EXCLUDED_EMAILS.get(v.lower(), 'privacy/legal alias is not an outreach channel')}")
                                continue
                        if v not in (None, "") and (f.endswith("_source") or r.get(f) in (None, "")):
                            r[f] = v
                            r.setdefault("patched_fields", []).append(f"{f}<-{fname}")
                    if pt.get("manual_check"):
                        r["manual_check"] = pt["manual_check"]
                    if pt.get("enricher_note"):
                        r["notes"] = ((r.get("notes") or "") + " | enricher: " + pt["enricher_note"]).strip(" |")
        if not matched:
            for fname, pt in lst:
                if pt.get("new_row"):
                    nr = dict(pt["new_row"]); nr["_segment"] = "enrichment_" + fname[:-5]
                    if pt.get("manual_check"):
                        nr["manual_check"] = pt["manual_check"]
                    new_rows.append(nr)
    rows.extend(new_rows)
    print(f"patched companies: {len(patches)}  new rows from enrichment: {len(new_rows)}")

    # dedupe by website domain, then by (company_name, decision_maker_name)
    seen, deduped, dupes = {}, [], []
    for r in rows:
        k = domain(r.get("website") or "") or (r.get("company_name") or "").lower()
        if k in seen:
            r["status"] = "Rejected"
            r["reasons"] = [f"duplicate of {seen[k]} (segment {r['_segment']})"]
            dupes.append(r)
        else:
            seen[k] = r.get("company_name")
            deduped.append(r)

    print(f"candidates: {len(rows)}  deduped: {len(deduped)}  dupes: {len(dupes)}  researcher-rejected: {len(rejected_by_researchers)}")
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        checks = list(ex.map(verify_row, deduped))

    verified, partial, rejected = [], [], list(rejected_by_researchers) + dupes
    for r, c in zip(deduped, checks):
        r["verification"] = c
        r["status"] = c["status"]
        r["confidence_score"] = c["confidence_score"]
        r["reasons"] = c["reasons"]
        {"Verified": verified, "Partially Verified": partial, "Rejected": rejected}[c["status"]].append(r)

    json.dump(verified, open(os.path.join(OUT, "verified.json"), "w"), indent=2)
    json.dump(partial, open(os.path.join(OUT, "partial.json"), "w"), indent=2)
    json.dump(rejected, open(os.path.join(OUT, "rejected.json"), "w"), indent=2)
    json.dump(checks, open(os.path.join(OUT, "checks.json"), "w"), indent=2)
    print(f"Verified: {len(verified)}  Partially: {len(partial)}  Rejected: {len(rejected)}")
    # reason histogram
    hist = {}
    for r in partial:
        for reason in r["reasons"]:
            key = reason.split(" ")[0] + " " + " ".join(reason.split(" ")[1:6])
            hist[key] = hist.get(key, 0) + 1
    for k, v in sorted(hist.items(), key=lambda x: -x[1])[:15]:
        print(f"  {v:3d}  {k}")


if __name__ == "__main__":
    main()
