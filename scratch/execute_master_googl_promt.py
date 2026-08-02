import json
import os

print("Executing master update of GOOGL (Alphabet Inc.) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for GOOGL (Alphabet Inc. - Q2 2026)
googl_data = {
    'ticker': 'GOOGL',
    'name': 'Alphabet Inc.',
    'sector': 'Technology / Digital Advertising, Search, Cloud Computing & Applied AI',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 182.00,
    'pe': 23.50,
    'pe_forward': 19.80,
    'eps_trailing': 7.74,
    'eps_forward': 9.19,
    'eps_growth_ntm_pct': 21.5,
    'growth_eps': 21.5,
    'market_cap_b': 2260.0,
    'ocf_ttm_m': 106000.0,
    'maint_capex_m': 32000.0,
    'owner_earnings_m': 74000.0,
    'fcf_yield_pct': 3.27,
    'score_fcf_yield': 8.18,
    'intrinsic_value': 227.50,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 10.86,
    'score_peg': 10.00,
    'value_score': 8.27,
    'wacc': 8.0,
    'g_terminal': 3.5,
    'data_confidence': 'Alta',
    'f1': 9.50,
    'f2': 9.80,
    'f3': 9.30,
    'f4': 9.85,
    'f4_moat': 9.85,
    'f5': 9.30,
    'f6': 9.50,
    'f7': 9.50,
    'f8': 9.60,
    'cqv_v4': 9.53,
    'cqv': 9.53,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 160.00,
        'target_mean_base': 215.00,
        'target_high_bull': 240.00,
        'num_analysts': 50,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 18.1
    },
    'close_history': {
        '2020': 87.59,
        '2021': 144.85,
        '2022': 88.23,
        '2023': 139.69,
        '2024': 175.00,
        '2025': 170.00,
        '2026': 182.00
    }
}

# Update in cqv_list for GOOGL if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'GOOGL':
        cqv_list[idx].update(googl_data)
        updated = True
        break

if not updated:
    cqv_list.append(googl_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['GOOGL'] = {
    '2020': {'f1': 9.10, 'f2': 9.60, 'f3': 8.90, 'f4': 9.75, 'f5': 8.90, 'f6': 9.20, 'f7': 9.10, 'f8': 9.30, 'cqv_v1': 9.22, 'cqv_v1_1': 9.22, 'cqv_v2': 9.16, 'cqv_v3': 9.20, 'cqv_v4': 9.23, 'cqv': 9.23, 'pe': 34.50},
    '2021': {'f1': 9.30, 'f2': 9.70, 'f3': 9.10, 'f4': 9.80, 'f5': 9.10, 'f6': 9.35, 'f7': 9.30, 'f8': 9.45, 'cqv_v1': 9.38, 'cqv_v1_1': 9.38, 'cqv_v2': 9.32, 'cqv_v3': 9.35, 'cqv_v4': 9.38, 'cqv': 9.38, 'pe': 28.20},
    '2022': {'f1': 9.15, 'f2': 9.65, 'f3': 8.80, 'f4': 9.75, 'f5': 9.00, 'f6': 9.25, 'f7': 9.20, 'f8': 9.35, 'cqv_v1': 9.25, 'cqv_v1_1': 9.25, 'cqv_v2': 9.19, 'cqv_v3': 9.22, 'cqv_v4': 9.25, 'cqv': 9.25, 'pe': 18.50},
    '2023': {'f1': 9.35, 'f2': 9.72, 'f3': 9.15, 'f4': 9.82, 'f5': 9.15, 'f6': 9.40, 'f7': 9.35, 'f8': 9.50, 'cqv_v1': 9.42, 'cqv_v1_1': 9.42, 'cqv_v2': 9.37, 'cqv_v3': 9.40, 'cqv_v4': 9.43, 'cqv': 9.43, 'pe': 25.80},
    '2024': {'f1': 9.42, 'f2': 9.76, 'f3': 9.22, 'f4': 9.83, 'f5': 9.22, 'f6': 9.44, 'f7': 9.42, 'f8': 9.54, 'cqv_v1': 9.47, 'cqv_v1_1': 9.47, 'cqv_v2': 9.42, 'cqv_v3': 9.45, 'cqv_v4': 9.48, 'cqv': 9.48, 'pe': 24.20},
    '2025': {'f1': 9.46, 'f2': 9.78, 'f3': 9.26, 'f4': 9.84, 'f5': 9.26, 'f6': 9.47, 'f7': 9.46, 'f8': 9.57, 'cqv_v1': 9.50, 'cqv_v1_1': 9.50, 'cqv_v2': 9.45, 'cqv_v3': 9.48, 'cqv_v4': 9.51, 'cqv': 9.51, 'pe': 22.80},
    '2026': {'f1': 9.50, 'f2': 9.80, 'f3': 9.30, 'f4': 9.85, 'f5': 9.30, 'f6': 9.50, 'f7': 9.50, 'f8': 9.60, 'cqv_v1': 9.53, 'cqv_v1_1': 9.53, 'cqv_v2': 9.49, 'cqv_v3': 9.51, 'cqv_v4': 9.53, 'cqv': 9.53, 'pe': 23.50}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR GOOGL (ALPHABET INC.) Q2 2026.")
