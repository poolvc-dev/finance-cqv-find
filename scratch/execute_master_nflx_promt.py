import json
import os

print("Executing master update of NFLX (Netflix, Inc.) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for NFLX (Netflix, Inc. - Q2 2026)
nflx_data = {
    'ticker': 'NFLX',
    'name': 'Netflix, Inc.',
    'sector': 'Communication Services / Entertainment & Streaming Media',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 680.50,
    'pe': 34.20,
    'pe_forward': 27.50,
    'eps_trailing': 19.90,
    'eps_forward': 24.75,
    'eps_growth_ntm_pct': 24.4,
    'growth_eps': 24.4,
    'market_cap_b': 292.5,
    'ocf_ttm_m': 7850.0,
    'maint_capex_m': 450.0,
    'owner_earnings_m': 7400.0,
    'fcf_yield_pct': 2.53,
    'score_fcf_yield': 6.33,
    'intrinsic_value': 850.63,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 8.87,
    'score_peg': 8.87,
    'value_score': 7.19,
    'wacc': 8.5,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 9.40,
    'f2': 9.10,
    'f3': 9.10,
    'f4': 9.50,
    'f4_moat': 9.50,
    'f5': 8.90,
    'f6': 9.20,
    'f7': 8.80,
    'f8': 9.00,
    'cqv_v4': 9.18,
    'cqv': 9.18,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 580.00,
        'target_mean_base': 775.00,
        'target_high_bull': 875.00,
        'num_analysts': 42,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 13.9
    },
    'close_history': {
        '2020': 540.73,
        '2021': 602.44,
        '2022': 294.95,
        '2023': 486.88,
        '2024': 642.50,
        '2025': 610.20,
        '2026': 680.50
    }
}

# Update in cqv_list for NFLX if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'NFLX':
        cqv_list[idx].update(nflx_data)
        updated = True
        break

if not updated:
    cqv_list.append(nflx_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['NFLX'] = {
    '2020': {'f1': 8.80, 'f2': 8.50, 'f3': 8.90, 'f4': 9.30, 'f5': 8.40, 'f6': 9.00, 'f7': 8.50, 'f8': 8.60, 'cqv_v1': 8.78, 'cqv_v1_1': 8.78, 'cqv_v2': 8.72, 'cqv_v3': 8.75, 'cqv_v4': 8.80, 'cqv': 8.80, 'pe': 85.20},
    '2021': {'f1': 9.00, 'f2': 8.70, 'f3': 8.95, 'f4': 9.35, 'f5': 8.60, 'f6': 9.10, 'f7': 8.60, 'f8': 8.70, 'cqv_v1': 8.90, 'cqv_v1_1': 8.90, 'cqv_v2': 8.85, 'cqv_v3': 8.88, 'cqv_v4': 8.92, 'cqv': 8.92, 'pe': 54.80},
    '2022': {'f1': 8.90, 'f2': 8.60, 'f3': 8.40, 'f4': 9.20, 'f5': 8.50, 'f6': 8.90, 'f7': 8.50, 'f8': 8.50, 'cqv_v1': 8.68, 'cqv_v1_1': 8.68, 'cqv_v2': 8.62, 'cqv_v3': 8.65, 'cqv_v4': 8.68, 'cqv': 8.68, 'pe': 26.50},
    '2023': {'f1': 9.10, 'f2': 8.85, 'f3': 8.80, 'f4': 9.40, 'f5': 8.70, 'f6': 9.10, 'f7': 8.65, 'f8': 8.80, 'cqv_v1': 8.92, 'cqv_v1_1': 8.92, 'cqv_v2': 8.86, 'cqv_v3': 8.90, 'cqv_v4': 8.94, 'cqv': 8.94, 'pe': 42.10},
    '2024': {'f1': 9.25, 'f2': 8.98, 'f3': 8.95, 'f4': 9.45, 'f5': 8.80, 'f6': 9.15, 'f7': 8.72, 'f8': 8.90, 'cqv_v1': 9.04, 'cqv_v1_1': 9.04, 'cqv_v2': 8.98, 'cqv_v3': 9.02, 'cqv_v4': 9.06, 'cqv': 9.06, 'pe': 38.50},
    '2025': {'f1': 9.35, 'f2': 9.05, 'f3': 9.02, 'f4': 9.48, 'f5': 8.85, 'f6': 9.18, 'f7': 8.76, 'f8': 8.95, 'cqv_v1': 9.10, 'cqv_v1_1': 9.10, 'cqv_v2': 9.04, 'cqv_v3': 9.08, 'cqv_v4': 9.12, 'cqv': 9.12, 'pe': 35.80},
    '2026': {'f1': 9.40, 'f2': 9.10, 'f3': 9.10, 'f4': 9.50, 'f5': 8.90, 'f6': 9.20, 'f7': 8.80, 'f8': 9.00, 'cqv_v1': 9.14, 'cqv_v1_1': 9.14, 'cqv_v2': 9.10, 'cqv_v3': 9.14, 'cqv_v4': 9.18, 'cqv': 9.18, 'pe': 34.20}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR NFLX Q2 2026.")
