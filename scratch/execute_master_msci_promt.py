import json
import os

print("Executing master update of MSCI (MSCI Inc.) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for MSCI (MSCI Inc. - Q2 2026)
msci_data = {
    'ticker': 'MSCI',
    'name': 'MSCI Inc.',
    'sector': 'Financials / Market Indexes, Data & Financial Analytics',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 545.20,
    'pe': 36.80,
    'pe_forward': 30.20,
    'eps_trailing': 14.82,
    'eps_forward': 18.05,
    'eps_growth_ntm_pct': 21.8,
    'growth_eps': 21.8,
    'market_cap_b': 43.1,
    'ocf_ttm_m': 1450.0,
    'maint_capex_m': 90.0,
    'owner_earnings_m': 1360.0,
    'fcf_yield_pct': 3.16,
    'score_fcf_yield': 7.90,
    'intrinsic_value': 681.50,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 7.22,
    'score_peg': 7.22,
    'value_score': 7.33,
    'wacc': 9.0,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 9.60,
    'f2': 9.40,
    'f3': 9.20,
    'f4': 9.85,
    'f4_moat': 9.85,
    'f5': 9.50,
    'f6': 9.50,
    'f7': 9.10,
    'f8': 9.60,
    'cqv_v4': 9.51,
    'cqv': 9.51,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 480.00,
        'target_mean_base': 625.00,
        'target_high_bull': 690.00,
        'num_analysts': 21,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 14.6
    },
    'close_history': {
        '2020': 446.53,
        '2021': 612.67,
        '2022': 465.17,
        '2023': 565.65,
        '2024': 598.20,
        '2025': 560.10,
        '2026': 545.20
    }
}

# Update in cqv_list for MSCI if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'MSCI':
        cqv_list[idx].update(msci_data)
        updated = True
        break

if not updated:
    cqv_list.append(msci_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['MSCI'] = {
    '2020': {'f1': 9.45, 'f2': 9.20, 'f3': 8.95, 'f4': 9.80, 'f5': 9.35, 'f6': 9.35, 'f7': 8.85, 'f8': 9.45, 'cqv_v1': 9.32, 'cqv_v1_1': 9.32, 'cqv_v2': 9.28, 'cqv_v3': 9.32, 'cqv_v4': 9.36, 'cqv': 9.36, 'pe': 52.10},
    '2021': {'f1': 9.55, 'f2': 9.30, 'f3': 9.10, 'f4': 9.82, 'f5': 9.42, 'f6': 9.42, 'f7': 8.95, 'f8': 9.52, 'cqv_v1': 9.42, 'cqv_v1_1': 9.42, 'cqv_v2': 9.35, 'cqv_v3': 9.40, 'cqv_v4': 9.43, 'cqv': 9.43, 'pe': 58.40},
    '2022': {'f1': 9.50, 'f2': 9.25, 'f3': 9.00, 'f4': 9.82, 'f5': 9.40, 'f6': 9.40, 'f7': 8.98, 'f8': 9.50, 'cqv_v1': 9.38, 'cqv_v1_1': 9.38, 'cqv_v2': 9.32, 'cqv_v3': 9.36, 'cqv_v4': 9.40, 'cqv': 9.40, 'pe': 39.50},
    '2023': {'f1': 9.55, 'f2': 9.32, 'f3': 9.10, 'f4': 9.85, 'f5': 9.45, 'f6': 9.45, 'f7': 9.02, 'f8': 9.55, 'cqv_v1': 9.42, 'cqv_v1_1': 9.42, 'cqv_v2': 9.38, 'cqv_v3': 9.42, 'cqv_v4': 9.45, 'cqv': 9.45, 'pe': 44.80},
    '2024': {'f1': 9.58, 'f2': 9.36, 'f3': 9.15, 'f4': 9.85, 'f5': 9.48, 'f6': 9.48, 'f7': 9.06, 'f8': 9.58, 'cqv_v1': 9.46, 'cqv_v1_1': 9.46, 'cqv_v2': 9.40, 'cqv_v3': 9.44, 'cqv_v4': 9.48, 'cqv': 9.48, 'pe': 42.10},
    '2025': {'f1': 9.60, 'f2': 9.38, 'f3': 9.18, 'f4': 9.85, 'f5': 9.50, 'f6': 9.50, 'f7': 9.08, 'f8': 9.60, 'cqv_v1': 9.48, 'cqv_v1_1': 9.48, 'cqv_v2': 9.42, 'cqv_v3': 9.46, 'cqv_v4': 9.50, 'cqv': 9.50, 'pe': 38.50},
    '2026': {'f1': 9.60, 'f2': 9.40, 'f3': 9.20, 'f4': 9.85, 'f5': 9.50, 'f6': 9.50, 'f7': 9.10, 'f8': 9.60, 'cqv_v1': 9.50, 'cqv_v1_1': 9.50, 'cqv_v2': 9.44, 'cqv_v3': 9.48, 'cqv_v4': 9.51, 'cqv': 9.51, 'pe': 36.80}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR MSCI Q2 2026.")
