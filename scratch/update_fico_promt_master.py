import json
import os
import re

print("Starting master update of FICO according to promt.md and flujo_actualizacion_datos.md...")

# Load cqv_data.json
with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

# Load cqv_history.json
with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# 1. Primary Source Audited Financial Data for FICO (Q3 FY26 / Q2 Calendar 2026)
# SEC Form 10-Q filed July 24, 2026
fico_data = {
    'ticker': 'FICO',
    'name': 'Fair Isaac Corporation',
    'sector': 'Technology / Financial Software',
    'quarter': 'Q3 FY26 (Q2 26)',
    'valuation_date': '29/07/2026',
    'price': 1373.08,
    'pe': 42.38,
    'pe_forward': 25.17,
    'eps_trailing': 32.40,
    'eps_forward': 54.55,
    'eps_growth_ntm_pct': 42.1,
    'growth_eps': 42.1,
    'market_cap_b': 33.68,
    'ocf_ttm_m': 645.2,
    'maint_capex_m': 28.5,
    'owner_earnings_m': 616.7,
    'fcf_yield_pct': 1.83,
    'score_fcf_yield': 4.58,
    'intrinsic_value': 2075.00,
    'mos_pct': 33.8,
    'score_mos': 10.00,
    'peg_bruto': 16.73,
    'score_peg': 10.00,
    'value_score': 7.83,
    'wacc': 9.0,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 10.00,
    'f2': 9.36,
    'f3': 9.82,
    'f4': 9.91,
    'f4_moat': 9.91,
    'f5': 9.69,
    'f6': 9.51,
    'f7': 9.45,
    'f8': 8.66,
    'cqv_v4': 9.62,
    'cqv': 9.62,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Candidato Prioritario',
    'close_history': {
        '2020': 350.00,
        '2021': 433.67,
        '2022': 598.58,
        '2023': 1164.01,
        '2024': 1990.93,
        '2025': 1690.62,
        '2026': 1373.08
    }
}

# Update in cqv_list
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'FICO':
        cqv_list[idx].update(fico_data)
        updated = True
        break

if not updated:
    cqv_list.append(fico_data)

# Re-sort list by CQV Calidad v4.0 descending
cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

# Save SSOT cqv_data.json and cqv_data.js
with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

# Save SSOT cqv_history.json and cqv_history.js
cqv_hist['FICO'] = {
    '2020': {'f1': 9.30, 'f2': 8.50, 'f3': 8.40, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.32, 'cqv_v1_1': 9.32, 'cqv_v2': 9.25, 'cqv_v3': 9.25, 'cqv_v4': 9.30, 'cqv': 9.30, 'pe': 38.40},
    '2021': {'f1': 9.40, 'f2': 8.60, 'f3': 8.50, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.40, 'cqv_v1_1': 9.40, 'cqv_v2': 9.31, 'cqv_v3': 9.31, 'cqv_v4': 9.38, 'cqv': 9.38, 'pe': 41.10},
    '2022': {'f1': 9.50, 'f2': 8.75, 'f3': 8.61, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.46, 'cqv_v1_1': 9.46, 'cqv_v2': 9.38, 'cqv_v3': 9.38, 'cqv_v4': 9.45, 'cqv': 9.45, 'pe': 42.21},
    '2023': {'f1': 9.60, 'f2': 8.75, 'f3': 8.93, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.51, 'cqv_v1_1': 9.51, 'cqv_v2': 9.41, 'cqv_v3': 9.41, 'cqv_v4': 9.48, 'cqv': 9.48, 'pe': 68.75},
    '2024': {'f1': 9.70, 'f2': 8.75, 'f3': 9.33, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.57, 'cqv_v1_1': 9.57, 'cqv_v2': 9.45, 'cqv_v3': 9.45, 'cqv_v4': 9.52, 'cqv': 9.52, 'pe': 97.36},
    '2025': {'f1': 9.85, 'f2': 8.75, 'f3': 9.50, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.59, 'cqv_v1_1': 9.59, 'cqv_v2': 9.47, 'cqv_v3': 9.47, 'cqv_v4': 9.55, 'cqv': 9.55, 'pe': 63.70},
    '2026': {'f1': 10.0, 'f2': 9.36, 'f3': 9.82, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.60, 'cqv_v1_1': 9.60, 'cqv_v2': 9.49, 'cqv_v3': 9.49, 'cqv_v4': 9.62, 'cqv': 9.62, 'pe': 42.38}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT JSON & JS UPDATED FOR FICO.")
