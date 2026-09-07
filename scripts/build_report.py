import json, html
R = "../research/"
nat = json.load(open(R + "national_competitors.json"))
hou = json.load(open(R + "houston_competitors.json"))
dem = json.load(open(R + "demand_keywords_pricing.json"))
e = lambda s: html.escape(str(s)) if s is not None else "—"

# ---- traffic data (only sourced values) ----
traffic = []
for c in nat["competitors"]:
    if c.get("est_monthly_visits"): traffic.append((c["name"], c["est_monthly_visits"], "National"))
for c in hou["competitors"]:
    if c.get("est_monthly_visits"): traffic.append((c["name"].split(" –")[0].split(" (")[0], c["est_monthly_visits"], "Houston"))
traffic.sort(key=lambda x: -x[1])
no_traffic = [c["name"] for c in nat["competitors"] if not c.get("est_monthly_visits")]

# ---- price ladder (effective $/hr where sourced) ----
ladder = [
    ("Wing (offshore FT)", 6.87, "Offshore"), ("Philippines freelance", 11, "Offshore"), ("Time etc (US, low seniority)", 37.5, "US"),
    ("BELAY (US, est., unpublished)", 46, "US"), ("Boldly (US W-2)", 65, "US"), ("Worxbee (US)", 69, "US"),
    ("Delegate Solutions (US team)", 90, "US"), ("In-house Houston EA (derived, loaded)", 47.7, "In-house"),
    ("[BrandName] Executive tier (proposed)", 57.5, "Proposed"),
]
# Worxbee effective: 2760/40=69; sourced from national file price_low 2760 (40 hrs) — note in caption.

# ---- Houston table ----
GROUP = {"A": "Agency / Houston-targeted", "B": "Solo operator", "C": "Staffing / placement"}
hrows = ""
for c in sorted(hou["competitors"], key=lambda x: x["group"]):
    price = "—"
    if c.get("price_low_usd") or c.get("price_high_usd"):
        price = f"${c.get('price_low_usd') or '?'}–{c.get('price_high_usd') or '?'}" if c.get("price_high_usd") else f"from ${c.get('price_low_usd')}"
    q = c.get("website_quality_score_1to5")
    qhtml = f'<span class="q q{q}">{q}/5</span>' if q else '<span class="muted">no site</span>'
    visits = f"{c['est_monthly_visits']:,}" if c.get("est_monthly_visits") else "—"
    hrows += f"<tr><td><span class='grp g{c['group']}'>{c['group']}</span></td><td><a href='{e(c['url'])}' target='_blank' rel='noopener noreferrer'>{e(c['name'])}</a><div class='sub'>{e(c.get('location_specific'))}</div></td><td>{e(c.get('talent_location'))}</td><td>{price}</td><td class='num'>{visits}</td><td>{qhtml}</td><td class='small'>{e(c.get('weaknesses_or_gaps'))}</td></tr>"

# ---- National table ----
nrows = ""
for c in sorted(nat["competitors"], key=lambda x: -(x.get("est_monthly_visits") or 0)):
    if not c.get("positioning_statement"): continue
    price = "—"
    if c.get("price_low_usd"):
        price = f"${c['price_low_usd']:,}" + (f"–{c['price_high_usd']:,}" if c.get("price_high_usd") else "+") + "/mo"
    visits = f"{c['est_monthly_visits']:,}" if c.get("est_monthly_visits") else "—"
    pub = "Public" if c.get("pricing_public") else ("Hidden" if c.get("pricing_public") is False else "—")
    nrows += f"<tr><td><a href='{e(c['url'])}' target='_blank' rel='noopener noreferrer'>{e(c['name'])}</a></td><td>{e(c.get('business_model'))}</td><td>{e(c.get('talent_location'))}</td><td>{price}<div class='sub'>{pub}</div></td><td class='num'>{visits}</td><td class='small'>{e(c.get('weaknesses_or_gaps'))}</td></tr>"
nrows += "<tr><td><a href='https://www.delegatesolutions.com' target='_blank' rel='noopener noreferrer'>Delegate Solutions</a></td><td>agency-team (3-person)</td><td>US-based</td><td>$2,299–3,959/mo<div class='sub'>Public</div></td><td class='num'>—</td><td class='small'>Highest US effective rate ($88–92/hr); ranks #1 in index for 'fractional executive assistant'</td></tr>"

# ---- Keywords ----
krows = ""
for k in sorted(dem["keywords"], key=lambda x: (-x["priority_1to5"], x["cluster"]))[:40]:
    ranks = ", ".join(k["who_ranks_now"][:3]) if k["who_ranks_now"] else "<em>no agency ranking found</em>"
    krows += f"<tr><td>{e(k['term'])}</td><td><span class='pill'>{e(k['cluster'])}</span></td><td>{e(k['intent'])}</td><td class='small'>{ranks}</td><td>{e(k['content_type_needed'])}</td><td class='num'><b>{k['priority_1to5']}</b></td></tr>"

# ---- Pain themes ----
themes = {}
for p in dem["buyer_signals"]["pain_points"]:
    t = (p.get("theme") or "other").replace("_", " ")
    themes[t] = themes.get(t, 0) + 1
themes = sorted(themes.items(), key=lambda x: -x[1])

# ---- SERP ----
serp = ""
for s in hou["serp_snapshot"]:
    names = [r if isinstance(r, str) else (r.get("name") or r.get("domain") or r.get("url")) for r in s["top_results"]]
    serp += f"<div class='serp'><div class='serpq'>“{e(s['query'])}”</div><ol>{''.join(f'<li>{e(n)}</li>' for n in names[:5])}</ol></div>"

gaps = "".join(f"<li>{e(g)}</li>" for g in nat["market_patterns"]["gaps_nobody_fills"])
promises = "".join(f"<li>{e(p)}</li>" for p in nat["market_patterns"]["common_promises"])
demand = "".join(f"<tr><td>{e(d['topic'])}</td><td>{e(d['stat'])}</td><td class='small'><a href='{e(d['url'])}' target='_blank' rel='noopener noreferrer'>{e(d['source'])}</a></td></tr>" for d in hou["demand_context"])
objections = "".join(f"<li>{e(o)}</li>" for o in dem["buyer_signals"]["objections"])
pr = dem["pricing_recommendations"]["option_a_premium_boutique"]

n_sources = len({u for blob in (nat, hou, dem) for u in json.dumps(blob).split('"') if u.startswith("http")})

page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Executive Assistant Services — Houston & Virtual Market Analysis</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
<style>
:root{{--navy:#0b2545;--blue:#1f5fbf;--red:#c8102e;--ink:#15202b;--mute:#5b6775;--line:#dfe5ee;--paper:#ffffff;--wash:#f4f7fb;--ok:#1c7c4a;--warn:#b7791f}}
*{{box-sizing:border-box}}body{{margin:0;font-family:"IBM Plex Sans",system-ui,sans-serif;color:var(--ink);background:var(--paper);line-height:1.5}}
a{{color:var(--blue);text-decoration:none}}a:hover{{text-decoration:underline}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 40px}}
header{{border-top:6px solid var(--navy);border-bottom:1px solid var(--line);padding:28px 0 22px}}
.kicker{{font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--red)}}
h1{{font-family:"Source Serif 4",Georgia,serif;font-size:40px;line-height:1.1;margin:8px 0 10px;color:var(--navy)}}
.dek{{font-size:17px;color:var(--mute);max-width:820px}}
.meta{{display:flex;gap:24px;flex-wrap:wrap;font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--mute);margin-top:14px}}
.notice{{background:#fff8e6;border:1px solid #f0d58a;border-left:4px solid var(--warn);padding:12px 16px;border-radius:4px;font-size:14px;margin:22px 0}}
section{{padding:44px 0;border-bottom:1px solid var(--line)}}
h2{{font-family:"Source Serif 4",Georgia,serif;font-size:28px;color:var(--navy);margin:0 0 6px}}
.lede{{color:var(--mute);margin:0 0 22px;max-width:860px}}
h3{{font-size:15px;text-transform:uppercase;letter-spacing:.06em;color:var(--navy);margin:26px 0 10px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:14px;margin-top:24px}}
.kpi{{background:var(--wash);border:1px solid var(--line);border-radius:6px;padding:14px 16px}}
.kpi .v{{font-family:"Source Serif 4",Georgia,serif;font-size:30px;color:var(--navy);line-height:1}}
.kpi .l{{font-size:12.5px;color:var(--mute);margin-top:6px}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:28px}}@media(max-width:900px){{.grid2{{grid-template-columns:1fr}}.wrap{{padding:0 20px}}h1{{font-size:30px}}}}
.chart{{width:100%;height:420px;border:1px solid var(--line);border-radius:6px;background:#fff}}
.cap{{font-size:12.5px;color:var(--mute);margin-top:8px}}
table{{width:100%;border-collapse:collapse;font-size:13.5px}}th{{text-align:left;background:var(--navy);color:#fff;padding:9px 10px;font-weight:600;font-size:12.5px;position:sticky;top:0}}
td{{padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}}tr:nth-child(even) td{{background:#fafcff}}
.num{{text-align:right;font-family:"IBM Plex Mono",monospace}}.small{{font-size:12.5px;color:#3d4a58}}.sub{{font-size:12px;color:var(--mute)}}.muted{{color:var(--mute)}}
.tscroll{{overflow:auto;max-height:560px;border:1px solid var(--line);border-radius:6px}}
.pill{{display:inline-block;background:var(--wash);border:1px solid var(--line);border-radius:999px;padding:1px 8px;font-size:11.5px;font-family:"IBM Plex Mono",monospace}}
.grp{{display:inline-block;width:22px;height:22px;border-radius:4px;color:#fff;text-align:center;font-weight:700;font-size:12px;line-height:22px}}.gA{{background:var(--blue)}}.gB{{background:#7a4bd6}}.gC{{background:#4a5568}}
.q{{font-family:"IBM Plex Mono",monospace;font-weight:600}}.q1,.q2{{color:var(--red)}}.q3{{color:var(--warn)}}.q4,.q5{{color:var(--ok)}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}}
.card{{border:1px solid var(--line);border-radius:6px;padding:16px 18px;background:#fff}}.card h4{{margin:0 0 6px;font-size:15px;color:var(--navy)}}.card p{{margin:0;font-size:13.5px;color:#3d4a58}}
.serp{{border:1px solid var(--line);border-radius:6px;padding:12px 14px;background:#fff}}.serpq{{font-weight:600;font-size:13.5px;margin-bottom:6px;color:var(--navy)}}.serp ol{{margin:0;padding-left:18px;font-size:13px}}
.rec{{background:var(--navy);color:#fff;border-radius:8px;padding:28px 30px}}.rec h2{{color:#fff}}.rec .lede{{color:#c9d5e6}}
.tiers{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px}}@media(max-width:700px){{.tiers{{grid-template-columns:1fr}}}}
.tier{{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.18);border-radius:6px;padding:16px}}.tier .n{{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:#9fb6d6}}.tier .p{{font-family:"Source Serif 4",Georgia,serif;font-size:32px;margin:6px 0 2px}}.tier .h{{font-size:13px;color:#c9d5e6}}
ul.tight li{{margin-bottom:6px}}
footer{{padding:28px 0 48px;font-size:12.5px;color:var(--mute)}}
</style></head><body>
<header><div class="wrap">
<div class="kicker">Market analysis · Fractional & virtual executive assistant services</div>
<h1>Houston and the national virtual market: who wins traffic, what they charge, and where the gap is</h1>
<p class="dek">A competitive package for launching a Houston-based fractional executive assistant firm with a national virtual footprint. 39 competitors profiled across national agencies, Houston agencies, solo operators, and staffing firms; 61 keywords; 13 sourced price points; 18 buyer pain points.</p>
<div class="meta"><span>Research pulled 2026-09-07</span><span>{n_sources} source URLs</span><span>Traffic = Exa entity estimates (~Jun 2026)</span><span>Search rankings = Exa index, not live Google</span></div>
<div class="notice"><b>Read the numbers honestly.</b> Traffic figures are approximate third-party estimates and are missing for several major brands (Boldly, Zirtual, Athena, Double, Magic). Keyword search volumes could not be sourced from free tools and are omitted rather than guessed — pull them from Google Keyword Planner before locking SEO priorities. One Houston labor statistic (“547 employed”) is unverified and excluded from this page.</div>
</div></header>

<section><div class="wrap">
<h2>The picture in five numbers</h2>
<div class="kpis">
<div class="kpi"><div class="v">~173K</div><div class="l">Wing Assistant est. monthly visits — the segment's traffic leader is offshore</div></div>
<div class="kpi"><div class="v">~127K</div><div class="l">BELAY est. monthly visits — largest US brand, still hides pricing, 12-month contracts</div></div>
<div class="kpi"><div class="v">$2,600</div><div class="l">Hard monthly floor for US-based premium fractional EA (Boldly 40 hrs); $65–92/hr effective</div></div>
<div class="kpi"><div class="v">2</div><div class="l">Verifiable Houston-native EA agencies with a real website — both on Wix/Ueni, neither publishes pricing</div></div>
<div class="kpi"><div class="v">0</div><div class="l">Competitors positioned as Houston-based, US-talent, transparently priced, industry-fluent fractional EA</div></div>
</div>
</div></section>

<section><div class="wrap">
<h2>National virtual market — who drives traffic</h2>
<p class="lede">Estimated monthly visits for competitors where a figure could be sourced. Bars are order-of-magnitude, not precise. Missing: {e(", ".join(no_traffic[:9]))} and Houston-local sites (no data available).</p>
<div id="traffic" class="chart"></div>
<div class="cap">Source: Exa entity traffic data, approx. June 2026 snapshot, as recorded in the workbook 'Competitors' sheet. Houston staffing firms (Burnett, Murray) included because they compete for the same buyer's attention.</div>
<h3>National competitor roster</h3>
<div class="tscroll"><table><thead><tr><th>Company</th><th>Model</th><th>Talent</th><th>Price / transparency</th><th>Est. visits/mo</th><th>Observed weaknesses</th></tr></thead><tbody>{nrows}</tbody></table></div>
</div></section>

<section><div class="wrap">
<h2>Pricing ladder — effective hourly rate</h2>
<p class="lede">Where a sourced price and hours were both published, the effective $/hr is shown. The proposed Houston tier sits below Boldly and above BELAY's estimated rate, with published pricing as the wedge.</p>
<div class="grid2">
<div><div id="ladder" class="chart"></div><div class="cap">Boldly: boldly.com/pricing-plans ($2,600/40h). Worxbee: $2,760/40h plan. Delegate Solutions: delegatesolutions.com pricing ($2,299/25h–$3,959/45h). BELAY: not published; $42–50/hr third-party estimate. Wing: ~$1,099/mo full-time. In-house: derived from ~$68K median salary + 30% benefits + 15% overhead ÷ 173 hrs — an estimate, not a sourced figure.</div></div>
<div>
<h3>Table-stakes promises (everyone makes them)</h3><ul class="tight small">{promises}</ul>
<h3>Top buyer objections (synthesized from reviews)</h3><ul class="tight small">{objections}</ul>
</div></div>
</div></section>

<section><div class="wrap">
<h2>Houston market — thin on agencies, diffuse on solos, strong on staffing</h2>
<p class="lede">{e(hou['market_observations'].split(chr(10))[0])}</p>
<div class="tscroll"><table><thead><tr><th>Grp</th><th>Competitor</th><th>Talent</th><th>Price</th><th>Est. visits/mo</th><th>Site quality</th><th>Weaknesses / gaps</th></tr></thead><tbody>{hrows}</tbody></table></div>
<div class="cap">A = Houston agency or Houston-targeted landing page · B = solo operator (LinkedIn/Instagram only) · C = staffing/placement firm (W-2 in-person hires, different product, same buyer). Site quality is the researcher's 1–5 assessment.</div>
<h3>Houston search snapshot — who shows up</h3>
<p class="small muted">Exa search-index results for key Houston queries; not a live Google SERP or Maps pack. Note that national brands (BELAY, Boldly, Prialto) appear on none of them.</p>
<div class="cards">{serp}</div>
</div></section>

<section><div class="wrap">
<h2>Houston demand context</h2>
<p class="lede">The buyer pool is large and concentrated in exactly the verticals no competitor serves by name.</p>
<div class="tscroll" style="max-height:420px"><table><thead><tr><th>Topic</th><th>Stat</th><th>Source</th></tr></thead><tbody>{demand}</tbody></table></div>
</div></section>

<section><div class="wrap">
<h2>Keyword landscape — 40 highest-priority terms</h2>
<p class="lede">Volumes intentionally omitted (not sourced). Priority reflects intent, competition, and fit for a new Houston entrant. Full 61-term list with rationale is in the workbook.</p>
<div class="tscroll"><table><thead><tr><th>Keyword</th><th>Cluster</th><th>Intent</th><th>Who ranks now (index)</th><th>Page type</th><th>Priority</th></tr></thead><tbody>{krows}</tbody></table></div>
<div class="cap">Notable: no agency ranks for “virtual executive assistant Houston” or “fractional executive assistant Houston”; job boards and staffing firms fill “executive assistant Houston”. Comparison and pricing SERPs are owned by aggregators (theeaindex.com, outsourcedscale.com, usecarly.com), not by agencies.</div>
</div></section>

<section><div class="wrap">
<h2>What buyers complain about</h2>
<div class="grid2">
<div><div id="pain" class="chart" style="height:360px"></div><div class="cap">Count of 18 sourced pain points by theme (Trustpilot, Indeed, review articles). Full quotes and URLs in the workbook 'Buyer Signals' sheet.</div></div>
<div><h3>Gaps nobody fills</h3><ul class="tight small">{gaps}</ul></div>
</div>
</div></section>

<section><div class="wrap">
<div class="rec">
<h2>Recommended position</h2>
<p class="lede">Houston-rooted, US-based senior fractional EAs for energy, healthcare/TMC, legal, and private-capital leaders. Published pricing. Month-to-month. No buyout fees. Matched in five business days. In the room when you need us.</p>
<div class="tiers">
<div class="tier"><div class="n">{e(pr['entry_tier']['name'])}</div><div class="p">${pr['entry_tier']['monthly']:,}</div><div class="h">{pr['entry_tier']['hours_per_month']} hrs/mo · ${pr['entry_tier']['effective_per_hour']}/hr</div></div>
<div class="tier"><div class="n">{e(pr['growth_tier']['name'])}</div><div class="p">${pr['growth_tier']['monthly']:,}</div><div class="h">{pr['growth_tier']['hours_per_month']} hrs/mo · ${pr['growth_tier']['effective_per_hour']}/hr</div></div>
<div class="tier"><div class="n">{e(pr['full_tier']['name'])}</div><div class="p">${pr['full_tier']['monthly']:,}</div><div class="h">{pr['full_tier']['hours_per_month']} hrs/mo · ${pr['full_tier']['effective_per_hour']}/hr</div></div>
</div>
<p class="small" style="color:#c9d5e6;margin-top:16px">Derived recommendation, not a sourced figure. {e(pr['rationale'])} Margin check before launch: at ~$57/hr effective with senior 1099 talent at $32–38/hr, gross margin is 22–40%; parity with Boldly at $65/hr is the alternative if launching W-2.</p>
</div>
<h3>Why this is defensible</h3>
<div class="cards">
<div class="card"><h4>Local is unclaimed</h4><p>No national player has Houston presence or an in-person option; local agencies don't say it confidently and rank on template sites.</p></div>
<div class="card"><h4>Transparency is traffic</h4><p>The biggest US brand hides pricing behind a sales call and locks in for 12 months. Pricing and comparison SERPs are held by aggregators, not agencies.</p></div>
<div class="card"><h4>Industry fluency is a stated need</h4><p>“My VA doesn't understand oil and gas terminology” is a recorded objection. Houston has 19 energy Fortune 500 HQs, the TMC, 4,215 law offices, and a deep private-capital base.</p></div>
<div class="card"><h4>The bar is low locally</h4><p>Local sites score 2–3/5. A professional site with public pricing and vertical pages clears the Houston field on day one.</p></div>
</div>
</div></section>

<section><div class="wrap">
<h2>Data gaps to close before you rely on this</h2>
<ul class="tight">
<li><b>Keyword volumes:</b> all unknown. Pull the 61 workbook terms through Google Keyword Planner.</li>
<li><b>Traffic:</b> Boldly, Zirtual, Athena, Double, Magic and all Houston-local sites have no estimate; consider a Similarweb/Semrush trial for one month.</li>
<li><b>Domain ratings:</b> none captured; run competitors through a free DR checker.</li>
<li><b>Houston labor stat:</b> “547 employed” (SalaryMetro, SOC 43-6014) is unverified and likely wrong — check BLS OEWS Houston May 2024.</li>
<li><b>Google Maps pack:</b> not captured for Houston queries; check manually from a Houston IP.</li>
<li><b>Not retrieved:</b> Priority VA, Assistantly, Great Assistant; Equivity returned 404 (may be closed).</li>
</ul>
</div></section>

<footer><div class="wrap">Companion deliverables: Excel workbook (competitors, keywords, pricing, buyer signals, sources), Strategy document, Website Blueprint, and build-brief.md for a future builder. All estimates are labeled; nothing missing has been filled in.</div></footer>

<script>
const T={json.dumps([[t[0],t[1],t[2]] for t in traffic])};
const tc=echarts.init(document.getElementById('traffic'));
tc.setOption({{grid:{{left:190,right:60,top:20,bottom:30}},tooltip:{{formatter:p=>p.name+': ~'+p.value.toLocaleString()+' visits/mo (approx.)'}},
xAxis:{{type:'value',axisLabel:{{formatter:v=>(v/1000)+'K'}},splitLine:{{lineStyle:{{color:'#eef2f7'}}}}}},
yAxis:{{type:'category',inverse:true,data:T.map(t=>t[0]),axisLabel:{{fontSize:12}}}},
series:[{{type:'bar',data:T.map(t=>({{value:t[1],itemStyle:{{color:t[2]==='Houston'?'#4a5568':'#1f5fbf'}}}})),barMaxWidth:22,label:{{show:true,position:'right',formatter:p=>'~'+Math.round(p.value/1000)+'K',fontFamily:'IBM Plex Mono',fontSize:11}}}}]}});
const L={json.dumps(ladder)};
const lc=echarts.init(document.getElementById('ladder'));
const col={{Offshore:'#9aa5b1',US:'#1f5fbf','In-house':'#4a5568',Proposed:'#c8102e'}};
lc.setOption({{grid:{{left:230,right:60,top:20,bottom:30}},tooltip:{{formatter:p=>p.name+': $'+p.value+'/hr effective'}},
xAxis:{{type:'value',axisLabel:{{formatter:'${{value}}'}},splitLine:{{lineStyle:{{color:'#eef2f7'}}}}}},
yAxis:{{type:'category',data:L.sort((a,b)=>a[1]-b[1]).map(l=>l[0]),axisLabel:{{fontSize:11.5}}}},
series:[{{type:'bar',data:L.map(l=>({{value:l[1],itemStyle:{{color:col[l[2]]}}}})),barMaxWidth:20,label:{{show:true,position:'right',formatter:p=>'$'+p.value,fontFamily:'IBM Plex Mono',fontSize:11}}}}]}});
const P={json.dumps(themes)};
const pc=echarts.init(document.getElementById('pain'));
pc.setOption({{grid:{{left:170,right:40,top:10,bottom:30}},xAxis:{{type:'value',minInterval:1,splitLine:{{lineStyle:{{color:'#eef2f7'}}}}}},
yAxis:{{type:'category',inverse:true,data:P.map(p=>p[0]),axisLabel:{{fontSize:12}}}},
series:[{{type:'bar',data:P.map(p=>p[1]),itemStyle:{{color:'#c8102e'}},barMaxWidth:18,label:{{show:true,position:'right'}}}}]}});
window.addEventListener('resize',()=>{{tc.resize();lc.resize();pc.resize();}});
</script>
</body></html>"""
open("../report/index.html", "w").write(page)
print("ok", len(page), "traffic rows", len(traffic))
