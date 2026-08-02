import json
import os

print("Executing master update of MCO (Moody's Corporation) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for MCO (Moody's Corporation - Q2 2026)
mco_data = {
    'ticker': 'MCO',
    'name': "Moody's Corporation",
    'sector': 'Financials / Financial Data & Credit Ratings',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 468.20,
    'pe': 36.50,
    'pe_forward': 29.80,
    'eps_trailing': 12.83,
    'eps_forward': 15.71,
    'eps_growth_ntm_pct': 22.4,
    'growth_eps': 22.4,
    'market_cap_b': 85.2,
    'ocf_ttm_m': 2650.0,
    'maint_capex_m': 140.0,
    'owner_earnings_m': 2510.0,
    'fcf_yield_pct': 2.95,
    'score_fcf_yield': 7.38,
    'intrinsic_value': 585.25,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 7.52,
    'score_peg': 7.52,
    'value_score': 7.21,
    'wacc': 9.0,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 9.60,
    'f2': 9.40,
    'f3': 9.10,
    'f4': 9.90,
    'f4_moat': 9.90,
    'f5': 9.40,
    'f6': 9.50,
    'f7': 8.80,
    'f8': 9.60,
    'cqv_v4': 9.48,
    'cqv': 9.48,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 415.00,
        'target_mean_base': 545.00,
        'target_high_bull': 610.00,
        'num_analysts': 22,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 16.4
    },
    'close_history': {
        '2020': 290.24,
        '2021': 393.58,
        '2022': 278.62,
        '2023': 390.56,
        '2024': 485.10,
        '2025': 475.20,
        '2026': 468.20
    }
}

# Update in cqv_list
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'MCO':
        cqv_list[idx].update(mco_data)
        updated = True
        break

if not updated:
    cqv_list.append(mco_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['MCO'] = {
    '2020': {'f1': 9.30, 'f2': 9.10, 'f3': 8.80, 'f4': 9.85, 'f5': 9.20, 'f6': 9.30, 'f7': 8.40, 'f8': 9.40, 'cqv_v1': 9.25, 'cqv_v1_1': 9.25, 'cqv_v2': 9.18, 'cqv_v3': 9.22, 'cqv_v4': 9.26, 'cqv': 9.26, 'pe': 31.50},
    '2021': {'f1': 9.45, 'f2': 9.25, 'f3': 8.95, 'f4': 9.88, 'f5': 9.30, 'f6': 9.40, 'f7': 8.55, 'f8': 9.50, 'cqv_v1': 9.35, 'cqv_v1_1': 9.35, 'cqv_v2': 9.28, 'cqv_v3': 9.32, 'cqv_v4': 9.36, 'cqv': 9.36, 'pe': 34.20},
    '2022': {'f1': 9.35, 'f2': 9.15, 'f3': 8.70, 'f4': 9.85, 'f5': 9.25, 'f6': 9.35, 'f7': 8.50, 'f8': 9.45, 'cqv_v1': 9.20, 'cqv_v1_1': 9.20, 'cqv_v2': 9.15, 'cqv_v3': 9.20, 'cqv_v4': 9.24, 'cqv': 9.24, 'pe': 25.40},
    '2023': {'f1': 9.48, 'f2': 9.30, 'f3': 8.95, 'f4': 9.88, 'f5': 9.32, 'f6': 9.42, 'f7': 8.65, 'f8': 9.52, 'cqv_v1': 9.32, 'cqv_v1_1': 9.32, 'cqv_v2': 9.25, 'cqv_v3': 9.30, 'cqv_v4': 9.35, 'cqv': 9.35, 'pe': 37.80},
    '2024': {'f1': 9.55, 'f2': 9.35, 'f3': 9.05, 'f4': 9.90, 'f5': 9.38, 'f6': 9.48, 'f7': 8.75, 'f8': 9.55, 'cqv_v1': 9.38, 'cqv_v1_1': 9.38, 'cqv_v2': 9.32, 'cqv_v3': 9.36, 'cqv_v4': 9.42, 'cqv': 9.42, 'pe': 41.20},
    '2025': {'f1': 9.58, 'f2': 9.38, 'f3': 9.08, 'f4': 9.90, 'f5': 9.40, 'f6': 9.50, 'f7': 8.78, 'f8': 9.58, 'cqv_v1': 9.40, 'cqv_v1_1': 9.40, 'cqv_v2': 9.35, 'cqv_v3': 9.40, 'cqv_v4': 9.45, 'cqv': 9.45, 'pe': 38.40},
    '2026': {'f1': 9.60, 'f2': 9.40, 'f3': 9.10, 'f4': 9.90, 'f5': 9.40, 'f6': 9.50, 'f7': 8.80, 'f8': 9.60, 'cqv_v1': 9.45, 'cqv_v1_1': 9.45, 'cqv_v2': 9.40, 'cqv_v3': 9.44, 'cqv_v4': 9.48, 'cqv': 9.48, 'pe': 36.50}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR MCO Q2 2026.")
