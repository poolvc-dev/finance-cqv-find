import json

matches = [
    ('QLYS', '2026-11-09', 1.96, 2.12, 8.4),
    ('HRB', '2026-11-09', -1.44, -1.4, 3.11),
    ('TTWO', '2026-11-09', -0.86, -0.29, 66.38),
    ('NOVT', '2026-11-09', 0.97, 1.05, 8.62),
    ('CEG', '2026-11-09', 3.89, 5.06, 30.08),
    ('NRG', '2026-11-09', 3.03, 4.68, 54.53),
    ('ASTS', '2026-11-09', -0.45, -0.44, 1.77),
    ('HIMS', '2026-11-09', 0.06, -0.14, -348.58),
    ('APPS', '2026-11-09', 0.17, 0.18, 5.88),
    ('DOLE', '2026-11-09', 0.34, 0.16, -53.12),
    ('KKR', '2026-11-09', 1.58, 1.78, 12.48),
    ('TDG', '2026-11-10', 12.21, 12.44, 1.89),
    ('CLFD', '2026-11-10', 0.1, None, -100.0),
    ('RGTI', '2026-11-10', -0.05, -0.06, -17.07),
    ('INMD', '2026-11-11', 0.32, 0.37, 14.91),
    ('CTVA', '2026-11-11', 0.1, 0.06, -37.31),
    ('GIB', '2026-11-11', 2.3, 2.31, 0.35),
    ('OR', '2026-11-11', 0.27, 0.29, 5.96),
    ('AMAT', '2026-11-12', 4.05, 4.16, 2.6),
    ('YETI', '2026-11-12', 0.84, 0.91, 8.1),
    ('NU', '2026-11-12', 0.22, 0.22, 0.32),
    ('TTEK', '2026-11-12', 0.47, 0.49, 4.63)
]

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data_dict = {x['ticker']: x for x in data}

# Sort by date, then ticker
matches.sort(key=lambda x: (x[1], x[0]))

print(f"Total empresas encontradas: {len(matches)}")
print("-" * 135)
print(f"{'Ticker':<6} | {'Fecha':<10} | {'Nombre':<28} | {'Sector':<32} | {'CQV v5':<6} | {'Clasificación':<14} | {'EPS Rep':<7} | {'EPS Est':<7} | {'Sorpresa'}")
print("-" * 135)

for t, dt, est, rep, surp in matches:
    item = data_dict.get(t, {})
    name = str(item.get('name', t))[:28]
    sector = str(item.get('sector', ''))[:32]
    cqv = str(item.get('cqv_v5') or item.get('cqv') or 'N/D')
    cl = str(item.get('clasificacion', 'N/D'))
    est_s = f"{est:.2f}" if est is not None else "N/D"
    rep_s = f"{rep:.2f}" if rep is not None else "N/D"
    surp_s = f"{surp:+.1f}%" if surp is not None else "N/D"
    print(f"{t:<6} | {dt:<10} | {name:<28} | {sector:<32} | {cqv:<6} | {cl:<14} | {rep_s:<7} | {est_s:<7} | {surp_s}")

