import json
import os

print("Executing master update of META for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for META (Q2 2026)
meta_data = {
    'ticker': 'META',
    'name': 'Meta Platforms, Inc.',
    'sector': 'Communication Services / Interactive Media',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 585.61,
    'pe': 21.60,
    'pe_forward': 15.90,
    'eps_trailing': 27.11,
    'eps_forward': 36.83,
    'eps_growth_ntm_pct': 37.3,
    'growth_eps': 37.3,
    'market_cap_b': 1485.0,
    'ocf_ttm_m': 72500.0,
    'maint_capex_m': 14200.0,
    'owner_earnings_m': 58300.0,
    'fcf_yield_pct': 3.93,
    'score_fcf_yield': 9.83,
    'intrinsic_value': 735.00,
    'mos_pct': 20.3,
    'score_mos': 6.77,
    'peg_bruto': 23.46,
    'score_peg': 10.00,
    'value_score': 8.96,
    'wacc': 9.0,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 9.30,
    'f2': 9.50,
    'f3': 9.80,
    'f4': 9.80,
    'f4_moat': 9.80,
    'f5': 9.50,
    'f6': 9.50,
    'f7': 8.50,
    'f8': 9.50,
    'cqv_v4': 9.46,
    'cqv': 9.46,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'close_history': {
        '2020': 273.16,
        '2021': 333.42,
        '2022': 119.29,
        '2023': 350.88,
        '2024': 582.63,
        '2025': 658.91,
        '2026': 585.61
    }
}

# Update in cqv_list
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'META':
        cqv_list[idx].update(meta_data)
        updated = True
        break

if not updated:
    cqv_list.append(meta_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['META'] = {
    '2020': {'f1': 9.00, 'f2': 9.30, 'f3': 9.10, 'f4': 9.60, 'f5': 9.00, 'f6': 9.20, 'f7': 8.00, 'f8': 9.00, 'cqv_v1': 9.10, 'cqv_v1_1': 9.10, 'cqv_v2': 8.95, 'cqv_v3': 9.00, 'cqv_v4': 9.12, 'cqv': 9.12, 'pe': 31.40},
    '2021': {'f1': 9.15, 'f2': 9.40, 'f3': 9.20, 'f4': 9.65, 'f5': 9.10, 'f6': 9.30, 'f7': 8.10, 'f8': 9.10, 'cqv_v1': 9.20, 'cqv_v1_1': 9.20, 'cqv_v2': 9.05, 'cqv_v3': 9.10, 'cqv_v4': 9.22, 'cqv': 9.22, 'pe': 24.10},
    '2022': {'f1': 8.20, 'f2': 9.00, 'f3': 8.00, 'f4': 9.50, 'f5': 8.50, 'f6': 8.50, 'f7': 8.00, 'f8': 8.80, 'cqv_v1': 8.50, 'cqv_v1_1': 8.50, 'cqv_v2': 8.60, 'cqv_v3': 8.70, 'cqv_v4': 8.91, 'cqv': 8.91, 'pe': 11.80},
    '2023': {'f1': 9.10, 'f2': 9.35, 'f3': 9.40, 'f4': 9.70, 'f5': 9.30, 'f6': 9.40, 'f7': 8.30, 'f8': 9.30, 'cqv_v1': 9.10, 'cqv_v1_1': 9.10, 'cqv_v2': 9.05, 'cqv_v3': 9.10, 'cqv_v4': 9.16, 'cqv': 9.16, 'pe': 26.50},
    '2024': {'f1': 9.25, 'f2': 9.45, 'f3': 9.60, 'f4': 9.75, 'f5': 9.40, 'f6': 9.45, 'f7': 8.40, 'f8': 9.40, 'cqv_v1': 9.25, 'cqv_v1_1': 9.25, 'cqv_v2': 9.20, 'cqv_v3': 9.25, 'cqv_v4': 9.32, 'cqv': 9.32, 'pe': 28.20},
    '2025': {'f1': 9.28, 'f2': 9.48, 'f3': 9.70, 'f4': 9.78, 'f5': 9.45, 'f6': 9.48, 'f7': 8.45, 'f8': 9.45, 'cqv_v1': 9.30, 'cqv_v1_1': 9.30, 'cqv_v2': 9.22, 'cqv_v3': 9.28, 'cqv_v4': 9.40, 'cqv': 9.40, 'pe': 24.50},
    '2026': {'f1': 9.30, 'f2': 9.50, 'f3': 9.80, 'f4': 9.80, 'f5': 9.50, 'f6': 9.50, 'f7': 8.50, 'f8': 9.50, 'cqv_v1': 9.37, 'cqv_v1_1': 9.37, 'cqv_v2': 9.25, 'cqv_v3': 9.30, 'cqv_v4': 9.46, 'cqv': 9.46, 'pe': 21.60}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR META Q2 2026.")
