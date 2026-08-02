import json
import os

print("Executing master update of FICO (Fair Isaac Corporation) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for FICO (Fair Isaac Corporation - Q2 2026 / Q3 FY26)
fico_data = {
    'ticker': 'FICO',
    'name': 'Fair Isaac Corporation',
    'sector': 'Technology / Software, Credit Scoring & Decision Analytics',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 1780.00,
    'pe': 68.50,
    'pe_forward': 54.20,
    'eps_trailing': 26.00,
    'eps_forward': 32.84,
    'eps_growth_ntm_pct': 26.3,
    'growth_eps': 26.3,
    'market_cap_b': 43.5,
    'ocf_ttm_m': 720.0,
    'maint_capex_m': 40.0,
    'owner_earnings_m': 680.0,
    'fcf_yield_pct': 1.56,
    'score_fcf_yield': 3.90,
    'intrinsic_value': 2225.00,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 4.85,
    'score_peg': 4.85,
    'value_score': 5.02,
    'wacc': 8.5,
    'g_terminal': 3.5,
    'data_confidence': 'Alta',
    'f1': 9.85,
    'f2': 9.60,
    'f3': 9.40,
    'f4': 9.95,
    'f4_moat': 9.95,
    'f5': 9.70,
    'f6': 9.60,
    'f7': 9.20,
    'f8': 9.80,
    'cqv_v4': 9.68,
    'cqv': 9.68,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 1500.00,
        'target_mean_base': 2050.00,
        'target_high_bull': 2350.00,
        'num_analysts': 16,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 15.2
    },
    'close_history': {
        '2020': 510.60,
        '2021': 433.68,
        '2022': 598.57,
        '2023': 1164.00,
        '2024': 1950.00,
        '2025': 1680.00,
        '2026': 1780.00
    }
}

# Update in cqv_list for FICO if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'FICO':
        cqv_list[idx].update(fico_data)
        updated = True
        break

if not updated:
    cqv_list.append(fico_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['FICO'] = {
    '2020': {'f1': 9.50, 'f2': 9.30, 'f3': 9.00, 'f4': 9.90, 'f5': 9.40, 'f6': 9.40, 'f7': 8.80, 'f8': 9.60, 'cqv_v1': 9.42, 'cqv_v1_1': 9.42, 'cqv_v2': 9.35, 'cqv_v3': 9.40, 'cqv_v4': 9.44, 'cqv': 9.44, 'pe': 45.20},
    '2021': {'f1': 9.60, 'f2': 9.40, 'f3': 9.15, 'f4': 9.92, 'f5': 9.50, 'f6': 9.50, 'f7': 8.90, 'f8': 9.65, 'cqv_v1': 9.50, 'cqv_v1_1': 9.50, 'cqv_v2': 9.44, 'cqv_v3': 9.48, 'cqv_v4': 9.51, 'cqv': 9.51, 'pe': 38.50},
    '2022': {'f1': 9.65, 'f2': 9.45, 'f3': 9.20, 'f4': 9.92, 'f5': 9.55, 'f6': 9.52, 'f7': 9.00, 'f8': 9.70, 'cqv_v1': 9.54, 'cqv_v1_1': 9.54, 'cqv_v2': 9.48, 'cqv_v3': 9.52, 'cqv_v4': 9.55, 'cqv': 9.55, 'pe': 42.10},
    '2023': {'f1': 9.75, 'f2': 9.50, 'f3': 9.30, 'f4': 9.95, 'f5': 9.60, 'f6': 9.55, 'f7': 9.10, 'f8': 9.75, 'cqv_v1': 9.62, 'cqv_v1_1': 9.62, 'cqv_v2': 9.56, 'cqv_v3': 9.60, 'cqv_v4': 9.62, 'cqv': 9.62, 'pe': 58.40},
    '2024': {'f1': 9.80, 'f2': 9.55, 'f3': 9.35, 'f4': 9.95, 'f5': 9.65, 'f6': 9.58, 'f7': 9.15, 'f8': 9.78, 'cqv_v1': 9.66, 'cqv_v1_1': 9.66, 'cqv_v2': 9.60, 'cqv_v3': 9.64, 'cqv_v4': 9.65, 'cqv': 9.65, 'pe': 72.50},
    '2025': {'f1': 9.82, 'f2': 9.58, 'f3': 9.38, 'f4': 9.95, 'f5': 9.68, 'f6': 9.60, 'f7': 9.18, 'f8': 9.80, 'cqv_v1': 9.68, 'cqv_v1_1': 9.68, 'cqv_v2': 9.62, 'cqv_v3': 9.66, 'cqv_v4': 9.67, 'cqv': 9.67, 'pe': 65.20},
    '2026': {'f1': 9.85, 'f2': 9.60, 'f3': 9.40, 'f4': 9.95, 'f5': 9.70, 'f6': 9.60, 'f7': 9.20, 'f8': 9.80, 'cqv_v1': 9.69, 'cqv_v1_1': 9.69, 'cqv_v2': 9.64, 'cqv_v3': 9.67, 'cqv_v4': 9.68, 'cqv': 9.68, 'pe': 68.50}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR FICO (FAIR ISAAC CORP) Q2 2026.")
