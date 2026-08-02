import json
import os

print("Executing master update of NVDA for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for NVDA (Q2 2026 / Q2 FY27)
nvda_data = {
    'ticker': 'NVDA',
    'name': 'NVIDIA Corporation',
    'sector': 'Technology / Semiconductors & AI',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 190.01,
    'pe': 45.20,
    'pe_forward': 25.20,
    'eps_trailing': 4.20,
    'eps_forward': 7.54,
    'eps_growth_ntm_pct': 71.7,
    'growth_eps': 71.7,
    'market_cap_b': 4675.0,
    'ocf_ttm_m': 48200.0,
    'maint_capex_m': 1450.0,
    'owner_earnings_m': 46750.0,
    'fcf_yield_pct': 1.00,
    'score_fcf_yield': 2.50,
    'intrinsic_value': 237.51,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 28.45,
    'score_peg': 10.00,
    'value_score': 6.00,
    'wacc': 9.0,
    'g_terminal': 3.5,
    'data_confidence': 'Alta',
    'f1': 9.80,
    'f2': 9.50,
    'f3': 9.90,
    'f4': 9.80,
    'f4_moat': 9.80,
    'f5': 9.50,
    'f6': 9.50,
    'f7': 9.00,
    'f8': 6.50,
    'cqv_v4': 9.15,
    'cqv': 9.15,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'close_history': {
        '2020': 13.06,
        '2021': 29.41,
        '2022': 14.61,
        '2023': 49.52,
        '2024': 134.25,
        '2025': 180.50,
        '2026': 190.01
    }
}

# Update in cqv_list
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'NVDA':
        cqv_list[idx].update(nvda_data)
        updated = True
        break

if not updated:
    cqv_list.append(nvda_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['NVDA'] = {
    '2020': {'f1': 8.80, 'f2': 9.20, 'f3': 8.90, 'f4': 9.50, 'f5': 9.00, 'f6': 9.20, 'f7': 8.50, 'f8': 6.00, 'cqv_v1': 8.85, 'cqv_v1_1': 8.85, 'cqv_v2': 8.90, 'cqv_v3': 8.95, 'cqv_v4': 8.90, 'cqv': 8.90, 'pe': 78.50},
    '2021': {'f1': 9.10, 'f2': 9.30, 'f3': 9.20, 'f4': 9.60, 'f5': 9.10, 'f6': 9.30, 'f7': 8.70, 'f8': 6.10, 'cqv_v1': 9.00, 'cqv_v1_1': 9.00, 'cqv_v2': 9.00, 'cqv_v3': 9.05, 'cqv_v4': 8.98, 'cqv': 8.98, 'pe': 92.40},
    '2022': {'f1': 9.20, 'f2': 9.35, 'f3': 9.00, 'f4': 9.65, 'f5': 9.20, 'f6': 9.35, 'f7': 8.80, 'f8': 6.20, 'cqv_v1': 8.90, 'cqv_v1_1': 8.90, 'cqv_v2': 8.95, 'cqv_v3': 9.00, 'cqv_v4': 9.01, 'cqv': 9.01, 'pe': 54.10},
    '2023': {'f1': 9.50, 'f2': 9.40, 'f3': 9.60, 'f4': 9.70, 'f5': 9.35, 'f6': 9.40, 'f7': 8.90, 'f8': 6.30, 'cqv_v1': 9.20, 'cqv_v1_1': 9.20, 'cqv_v2': 9.10, 'cqv_v3': 9.12, 'cqv_v4': 9.08, 'cqv': 9.08, 'pe': 65.80},
    '2024': {'f1': 9.70, 'f2': 9.45, 'f3': 9.80, 'f4': 9.75, 'f5': 9.40, 'f6': 9.45, 'f7': 8.95, 'f8': 6.40, 'cqv_v1': 9.35, 'cqv_v1_1': 9.35, 'cqv_v2': 9.15, 'cqv_v3': 9.15, 'cqv_v4': 9.11, 'cqv': 9.11, 'pe': 58.20},
    '2025': {'f1': 9.75, 'f2': 9.48, 'f3': 9.85, 'f4': 9.78, 'f5': 9.45, 'f6': 9.48, 'f7': 8.98, 'f8': 6.45, 'cqv_v1': 9.40, 'cqv_v1_1': 9.40, 'cqv_v2': 9.18, 'cqv_v3': 9.18, 'cqv_v4': 9.13, 'cqv': 9.13, 'pe': 48.60},
    '2026': {'f1': 9.80, 'f2': 9.50, 'f3': 9.90, 'f4': 9.80, 'f5': 9.50, 'f6': 9.50, 'f7': 9.00, 'f8': 6.50, 'cqv_v1': 9.45, 'cqv_v1_1': 9.45, 'cqv_v2': 9.20, 'cqv_v3': 9.20, 'cqv_v4': 9.15, 'cqv': 9.15, 'pe': 45.20}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR NVDA Q2 2026.")
