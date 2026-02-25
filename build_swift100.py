# -*- coding: utf-8 -*-
from pathlib import Path
import re

md = Path('research/crypto/SWIFT_100.md').read_text(encoding='utf-8')
rows = []
for line in md.splitlines():
    if re.match(r'^\|\s*\d+\s*\|', line):
        parts = [p.strip() for p in line.strip('|').split('|')]
        if len(parts) >= 7:
            rows.append(parts[:7])
rows = rows[:100]

def risk_class(r):
    r = r.lower()
    if 'low' in r:
        return 'low'
    if 'med' in r:
        return 'med'
    return 'high'

cards = []
for r, t, n, s, c, k, th in rows[:10]:
    cards.append(f'<article class="card"><div class="row"><span class="rank">{r}</span><div><div class="ticker">{t}</div><div class="name">{n}</div></div><span class="pill {risk_class(k)}">{k} Risk</span></div><p class="thesis">{th}</p></article>')

trs = []
for r, t, n, s, c, k, th in rows:
    trs.append(f'<tr><td>{r}</td><td>{t}</td><td>{n}</td><td>{s}</td><td>{c}</td><td><span class="pill {risk_class(k)}">{k}</span></td><td>{th}</td></tr>')

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>SWIFT 100 - Full Top 100</title>
<style>
:root{{--bg:#0b0f14;--bg2:#101722;--card:#121b28;--muted:#9fb0c3;--text:#e8f0fa;--line:#1f2a3a;--accent:#4da3ff;--r:14px;--max:1180px}}
*{{box-sizing:border-box}}body{{margin:0;font-family:Inter,Segoe UI,Roboto,Arial,sans-serif;background:var(--bg);color:var(--text);line-height:1.5}}
.container{{width:min(var(--max),94%);margin:auto}}.nav{{position:sticky;top:0;background:rgba(11,15,20,.86);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}}
.navin{{display:flex;justify-content:space-between;align-items:center;min-height:62px}}.brand{{font-weight:800}}a{{color:var(--accent);text-decoration:none}}
.hero{{padding:44px 0 20px}}h1{{margin:.2rem 0 .5rem;font-size:clamp(1.7rem,4vw,2.8rem)}}.muted{{color:var(--muted)}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}}.card{{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:14px}}
.row{{display:flex;justify-content:space-between;align-items:center;gap:10px}}.rank{{background:#132033;border:1px solid #213552;border-radius:8px;min-width:30px;height:30px;display:grid;place-items:center;font-weight:800}}
.ticker{{font-weight:900}}.name{{font-size:.92rem;color:var(--muted)}}.thesis{{margin:.5rem 0 0}}
.pill{{font-size:.75rem;font-weight:800;padding:4px 8px;border-radius:999px;border:1px solid transparent}}.low{{color:#b8f7c9;background:rgba(126,231,135,.12);border-color:rgba(126,231,135,.35)}}.med{{color:#ffd9a8;background:rgba(255,184,107,.12);border-color:rgba(255,184,107,.35)}}.high{{color:#ffb8b3;background:rgba(255,123,114,.12);border-color:rgba(255,123,114,.35)}}
.table-wrap{{border:1px solid var(--line);border-radius:12px;overflow:auto;background:var(--bg2);margin-top:16px}}table{{width:100%;border-collapse:collapse;min-width:980px}}th,td{{padding:10px 12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}}th{{position:sticky;top:0;background:#0f1724;color:#bfd0e5}}
.section{{padding:16px 0 26px}}footer{{padding:18px 0 36px;color:var(--muted)}}@media(max-width:900px){{.grid{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<header class="nav"><div class="container navin"><div class="brand">SWIFT 100</div><nav><a href="#top10">Top 10</a> | <a href="#full100">Full 100</a></nav></div></header>
<main class="container">
<section class="hero"><h1>SWIFT 100 - Full Top 100 Presentation</h1><p class="muted">Complete list expanded to rank 1-100 for presentation use.</p></section>
<section id="top10" class="section"><h2>Top 10</h2><div class="grid">{''.join(cards)}</div></section>
<section id="full100" class="section"><h2>Full Top 100 Table</h2><div class="table-wrap"><table><thead><tr><th>Rank</th><th>Ticker</th><th>Name</th><th>Sector</th><th>Conviction</th><th>Risk</th><th>Thesis</th></tr></thead><tbody>{''.join(trs)}</tbody></table></div></section>
</main>
<footer><div class="container">Educational research framework. Not financial advice.</div></footer>
</body>
</html>'''

Path('swift100/index.html').write_text(html, encoding='utf-8')
print('written', len(rows))
