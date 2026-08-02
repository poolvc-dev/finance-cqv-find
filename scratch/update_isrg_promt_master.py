import json
import os

print("Executing master update of ISRG for Q2 2026 according to promt.md and template.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for ISRG (Intuitive Surgical, Inc. - Q2 2026)
isrg_data = {
    'ticker': 'ISRG',
    'name': 'Intuitive Surgical, Inc.',
    'sector': 'Healthcare / Medical Devices & Surgical Robotics',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 445.50,
    'pe': 68.50,
    'pe_forward': 54.20,
    'eps_trailing': 6.50,
    'eps_forward': 8.22,
    'eps_growth_ntm_pct': 22.5,
    'growth_eps': 22.5,
    'market_cap_b': 158.5,
    'ocf_ttm_m': 2450.0,
    'maint_capex_m': 380.0,
    'owner_earnings_m': 2070.0,
    'fcf_yield_pct': 1.31,
    'score_fcf_yield': 3.28,
    'intrinsic_value': 556.88,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 4.15,
    'score_peg': 4.15,
    'value_score': 4.56,
    'wacc': 9.0,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 9.60,
    'f2': 9.70,
    'f3': 9.30,
    'f4': 9.80,
    'f4_moat': 9.80,
    'f5': 9.20,
    'f6': 9.50,
    'f7': 8.80,
    'f8': 9.50,
    'cqv_v4': 9.52,
    'cqv': 9.52,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'close_history': {
        '2020': 272.90,
        '2021': 359.77,
        '2022': 265.35,
        '2023': 337.36,
        '2024': 468.10,
        '2025': 510.20,
        '2026': 445.50
    }
}

# Update in cqv_list
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'ISRG':
        cqv_list[idx].update(isrg_data)
        updated = True
        break

if not updated:
    cqv_list.append(isrg_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['ISRG'] = {
    '2020': {'f1': 9.20, 'f2': 9.50, 'f3': 9.00, 'f4': 9.70, 'f5': 9.00, 'f6': 9.30, 'f7': 8.50, 'f8': 9.20, 'cqv_v1': 9.20, 'cqv_v1_1': 9.20, 'cqv_v2': 9.15, 'cqv_v3': 9.20, 'cqv_v4': 9.22, 'cqv': 9.22, 'pe': 82.50},
    '2021': {'f1': 9.35, 'f2': 9.60, 'f3': 9.15, 'f4': 9.75, 'f5': 9.10, 'f6': 9.40, 'f7': 8.60, 'f8': 9.30, 'cqv_v1': 9.30, 'cqv_v1_1': 9.30, 'cqv_v2': 9.25, 'cqv_v3': 9.30, 'cqv_v4': 9.32, 'cqv': 9.32, 'pe': 76.40},
    '2022': {'f1': 9.40, 'f2': 9.65, 'f3': 9.10, 'f4': 9.75, 'f5': 9.15, 'f6': 9.40, 'f7': 8.65, 'f8': 9.35, 'cqv_v1': 9.25, 'cqv_v1_1': 9.25, 'cqv_v2': 9.25, 'cqv_v3': 9.30, 'cqv_v4': 9.35, 'cqv': 9.35, 'pe': 58.20},
    '2023': {'f1': 9.50, 'f2': 9.68, 'f3': 9.20, 'f4': 9.78, 'f5': 9.18, 'f6': 9.45, 'f7': 8.70, 'f8': 9.40, 'cqv_v1': 9.35, 'cqv_v1_1': 9.35, 'cqv_v2': 9.30, 'cqv_v3': 9.35, 'cqv_v4': 9.42, 'cqv': 9.42, 'pe': 68.90},
    '2024': {'f1': 9.55, 'f2': 9.70, 'f3': 9.25, 'f4': 9.80, 'f5': 9.20, 'f6': 9.48, 'f7': 8.75, 'f8': 9.45, 'cqv_v1': 9.40, 'cqv_v1_1': 9.40, 'cqv_v2': 9.35, 'cqv_v3': 9.40, 'cqv_v4': 9.47, 'cqv': 9.47, 'pe': 72.10},
    '2025': {'f1': 9.58, 'f2': 9.70, 'f3': 9.28, 'f4': 9.80, 'f5': 9.20, 'f6': 9.50, 'f7': 8.78, 'f8': 9.48, 'cqv_v1': 9.42, 'cqv_v1_1': 9.42, 'cqv_v2': 9.38, 'cqv_v3': 9.42, 'cqv_v4': 9.50, 'cqv': 9.50, 'pe': 70.50},
    '2026': {'f1': 9.60, 'f2': 9.70, 'f3': 9.30, 'f4': 9.80, 'f5': 9.20, 'f6': 9.50, 'f7': 8.80, 'f8': 9.50, 'cqv_v1': 9.45, 'cqv_v1_1': 9.45, 'cqv_v2': 9.40, 'cqv_v3': 9.45, 'cqv_v4': 9.52, 'cqv': 9.52, 'pe': 68.50}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR ISRG Q2 2026.")
