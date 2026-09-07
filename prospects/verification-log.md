# Verification Log — prospects/

Append-only. Each run adds a dated block; earlier blocks are never edited.

## Run 2026-09-07 18:05 CDT

- Raw research files: 7; enrichment patch files: 1
- Candidates per segment (candidates / researcher-rejected): energy_houston 28/22; growth_funded_houston 25/39; healthcare_houston 28/15; legal_houston 30/21; private_capital_houston 28/21; profservices_houston 28/26; texas_expansion 35/25
- **Verified: 107** · Partially Verified: 86 · Rejected (incl. researcher-rejected and duplicates): 178
- Verified rows by email kind: company_general 73, named_direct 34
- Verified rows where the verifier itself discovered the phone/email on the official site: 19
- Verified rows that needed an enrichment patch: 11; rows confirmed by browser spot-check: 0

### Why rows are Partially Verified (gate failures)

-  37 · G5 no published email
-  22 · G4 no 10-digit phone published
-  18 · G3 title sources insufficient
-  18 · G2 decision-maker surname not found on any fetched official page
-  15 · G4 phone not found on company site or cited source page
-   8 · G6 trigger source not reachable
-   8 · G1 website bot-blocked
-   1 · G5 email domain delta-spine.com has no MX record

### Why rows are Rejected (top reasons)

-   6 · G1 website not reachable 
-   3 · researcher: LinkedIn lists 201-500 employees, above the 150-employee c
-   2 · researcher: Staffing firm — excluded by brief.
-   2 · researcher: Healthcare provider — covered by the healthcare researcher
-   2 · researcher: Headquartered in Austin, not Houston.
-   1 · researcher: Being sold by Warburg Pincus and Kayne Anderson to Magnoli
-   1 · researcher: Acquired by Crescent Energy 
-   1 · researcher: Acquisition by Williams Companies completed 3 September 20
-   1 · researcher: Houston EPC/O&M firm but reported record workforce and rev
-   1 · researcher: Post-merger company reported at 250 employees, above the c
-   1 · researcher: NYSE-listed Houston energy services company far above the 
-   1 · researcher: Merged global offshore services company; far above the 150

### Method notes

- Gates G1–G8 as defined in README.md; a row is Verified only when G1–G6 all pass and G7–G8 are not fatal.
- Email verification = published on an official page (raw HTML incl. mailto: and decoded Cloudflare-protected addresses) + MX present via DNS-over-HTTPS. No SMTP mailbox probing (no SMTP egress from the build environment).
- Phone verification = formatted 10-digit match or tel: link on the company's own pages or the cited source page.
- Values the verifier discovered itself carry `*_discovered_by` = verifier_scan_<date> and the page URL as source.
- Values from enrichment patches carry `patched_fields`; browser confirmations carry `manual_check` with the rendered URL.
- Nothing was estimated. Nulls remain nulls. Rejected and Partially Verified rows are retained with reasons.
