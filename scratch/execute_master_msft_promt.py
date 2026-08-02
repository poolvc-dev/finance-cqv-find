import json
import os

print("Executing master update of MSFT (Microsoft Corporation) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for MSFT (Microsoft Corporation - Q2 2026 / Q4 FY26)
msft_data = {
    'ticker': 'MSFT',
    'name': 'Microsoft Corporation',
    'sector': 'Technology / Software, Cloud Infrastructure & AI Platforms',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 448.50,
    'pe': 33.80,
    'pe_forward': 28.40,
    'eps_trailing': 13.27,
    'eps_forward': 15.79,
    'eps_growth_ntm_pct': 19.0,
    'growth_eps': 19.0,
    'market_cap_b': 3330.0,
    'ocf_ttm_m': 118500.0,
    'maint_capex_m': 18500.0,
    'owner_earnings_m': 100000.0,
    'fcf_yield_pct': 3.00,
    'score_fcf_yield': 7.50,
    'intrinsic_value': 560.63,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 6.69,
    'score_peg': 6.69,
    'value_score': 7.01,
    'wacc': 8.0,
    'g_terminal': 3.5,
    'data_confidence': 'Alta',
    'f1': 9.70,
    'f2': 9.85,
    'f3': 9.30,
    'f4': 9.90,
    'f4_moat': 9.90,
    'f5': 9.60,
    'f6': 9.70,
    'f7': 9.60,
    'f8': 9.70,
    'cqv_v4': 9.66,
    'cqv': 9.66,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 410.00,
        'target_mean_base': 515.00,
        'target_high_bull': 600.00,
        'num_analysts': 45,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 14.8
    },
    'close_history': {
        '2020': 222.42,
        '2021': 336.32,
        '2022': 239.82,
        '2023': 376.04,
        '2024': 415.20,
        '2025': 420.50,
        '2026': 448.50
    }
}

# Update in cqv_list for MSFT if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'MSFT':
        cqv_list[idx].update(msft_data)
        updated = True
        break

if not updated:
    cqv_list.append(msft_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['MSFT'] = {
    '2020': {'f1': 9.50, 'f2': 9.75, 'f3': 9.00, 'f4': 9.85, 'f5': 9.40, 'f6': 9.50, 'f7': 9.20, 'f8': 9.55, 'cqv_v1': 9.45, 'cqv_v1_1': 9.45, 'cqv_v2': 9.40, 'cqv_v3': 9.44, 'cqv_v4': 9.48, 'cqv': 9.48, 'pe': 35.20},
    '2021': {'f1': 9.60, 'f2': 9.80, 'f3': 9.15, 'f4': 9.88, 'f5': 9.50, 'f6': 9.60, 'f7': 9.35, 'f8': 9.60, 'cqv_v1': 9.55, 'cqv_v1_1': 9.55, 'cqv_v2': 9.50, 'cqv_v3': 9.54, 'cqv_v4': 9.56, 'cqv': 9.56, 'pe': 38.40},
    '2022': {'f1': 9.62, 'f2': 9.80, 'f3': 9.18, 'f4': 9.88, 'f5': 9.52, 'f6': 9.62, 'f7': 9.40, 'f8': 9.62, 'cqv_v1': 9.56, 'cqv_v1_1': 9.56, 'cqv_v2': 9.52, 'cqv_v3': 9.55, 'cqv_v4': 9.57, 'cqv': 9.57, 'pe': 25.80},
    '2023': {'f1': 9.65, 'f2': 9.82, 'f3': 9.25, 'f4': 9.90, 'f5': 9.55, 'f6': 9.65, 'f7': 9.50, 'f8': 9.65, 'cqv_v1': 9.60, 'cqv_v1_1': 9.60, 'cqv_v2': 9.55, 'cqv_v3': 9.58, 'cqv_v4': 9.61, 'cqv': 9.61, 'pe': 35.50},
    '2024': {'f1': 9.68, 'f2': 9.85, 'f3': 9.28, 'f4': 9.90, 'f5': 9.58, 'f6': 9.68, 'f7': 9.55, 'f8': 9.68, 'cqv_v1': 9.62, 'cqv_v1_1': 9.62, 'cqv_v2': 9.58, 'cqv_v3': 9.61, 'cqv_v4': 9.63, 'cqv': 9.63, 'pe': 36.80},
    '2025': {'f1': 9.69, 'f2': 9.85, 'f3': 9.29, 'f4': 9.90, 'f5': 9.59, 'f6': 9.69, 'f7': 9.58, 'f8': 9.69, 'cqv_v1': 9.64, 'cqv_v1_1': 9.64, 'cqv_v2': 9.59, 'cqv_v3': 9.63, 'cqv_v4': 9.64, 'cqv': 9.64, 'pe': 34.20},
    '2026': {'f1': 9.70, 'f2': 9.85, 'f3': 9.30, 'f4': 9.90, 'f5': 9.60, 'f6': 9.70, 'f7': 9.60, 'f8': 9.70, 'cqv_v1': 9.66, 'cqv_v1_1': 9.66, 'cqv_v2': 9.61, 'cqv_v3': 9.64, 'cqv_v4': 9.66, 'cqv': 9.66, 'pe': 33.80}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR MSFT (MICROSOFT CORP) Q2 2026.")
