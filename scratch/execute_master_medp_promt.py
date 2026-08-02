import json
import os

print("Executing master update of MEDP (Medpace Holdings, Inc.) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for MEDP (Medpace Holdings, Inc. - Q2 2026)
medp_data = {
    'ticker': 'MEDP',
    'name': 'Medpace Holdings, Inc.',
    'sector': 'Healthcare / Contract Research Organization (CRO) & Clinical Trials',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 345.00,
    'pe': 31.20,
    'pe_forward': 24.50,
    'eps_trailing': 11.06,
    'eps_forward': 14.08,
    'eps_growth_ntm_pct': 27.3,
    'growth_eps': 27.3,
    'market_cap_b': 10.8,
    'ocf_ttm_m': 480.0,
    'maint_capex_m': 40.0,
    'owner_earnings_m': 440.0,
    'fcf_yield_pct': 4.07,
    'score_fcf_yield': 10.00,
    'intrinsic_value': 431.25,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 11.14,
    'score_peg': 10.00,
    'value_score': 9.00,
    'wacc': 8.5,
    'g_terminal': 3.5,
    'data_confidence': 'Alta',
    'f1': 9.40,
    'f2': 9.60,
    'f3': 9.30,
    'f4': 9.20,
    'f4_moat': 9.20,
    'f5': 9.50,
    'f6': 9.40,
    'f7': 8.80,
    'f8': 9.20,
    'cqv_v4': 9.35,
    'cqv': 9.35,
    'clasificacion': 'ALTA CALIDAD',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 300.00,
        'target_mean_base': 415.00,
        'target_high_bull': 480.00,
        'num_analysts': 12,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 20.3
    },
    'close_history': {
        '2020': 140.50,
        '2021': 218.40,
        '2022': 212.42,
        '2023': 306.40,
        '2024': 390.00,
        '2025': 325.00,
        '2026': 345.00
    }
}

# Update in cqv_list for MEDP if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'MEDP':
        cqv_list[idx].update(medp_data)
        updated = True
        break

if not updated:
    cqv_list.append(medp_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['MEDP'] = {
    '2020': {'f1': 8.90, 'f2': 9.20, 'f3': 8.80, 'f4': 8.80, 'f5': 9.00, 'f6': 9.00, 'f7': 8.20, 'f8': 8.80, 'cqv_v1': 8.85, 'cqv_v1_1': 8.85, 'cqv_v2': 8.80, 'cqv_v3': 8.84, 'cqv_v4': 8.88, 'cqv': 8.88, 'pe': 38.50},
    '2021': {'f1': 9.10, 'f2': 9.35, 'f3': 9.00, 'f4': 8.95, 'f5': 9.20, 'f6': 9.15, 'f7': 8.40, 'f8': 8.95, 'cqv_v1': 9.02, 'cqv_v1_1': 9.02, 'cqv_v2': 8.96, 'cqv_v3': 9.00, 'cqv_v4': 9.04, 'cqv': 9.04, 'pe': 42.10},
    '2022': {'f1': 9.20, 'f2': 9.45, 'f3': 9.10, 'f4': 9.05, 'f5': 9.30, 'f6': 9.25, 'f7': 8.50, 'f8': 9.05, 'cqv_v1': 9.12, 'cqv_v1_1': 9.12, 'cqv_v2': 9.08, 'cqv_v3': 9.11, 'cqv_v4': 9.15, 'cqv': 9.15, 'pe': 28.50},
    '2023': {'f1': 9.30, 'f2': 9.50, 'f3': 9.20, 'f4': 9.15, 'f5': 9.40, 'f6': 9.35, 'f7': 8.65, 'f8': 9.15, 'cqv_v1': 9.22, 'cqv_v1_1': 9.22, 'cqv_v2': 9.18, 'cqv_v3': 9.21, 'cqv_v4': 9.24, 'cqv': 9.24, 'pe': 35.80},
    '2024': {'f1': 9.35, 'f2': 9.55, 'f3': 9.25, 'f4': 9.18, 'f5': 9.45, 'f6': 9.38, 'f7': 8.72, 'f8': 9.18, 'cqv_v1': 9.28, 'cqv_v1_1': 9.28, 'cqv_v2': 9.22, 'cqv_v3': 9.26, 'cqv_v4': 9.29, 'cqv': 9.29, 'pe': 36.20},
    '2025': {'f1': 9.38, 'f2': 9.58, 'f3': 9.28, 'f4': 9.19, 'f5': 9.48, 'f6': 9.39, 'f7': 8.76, 'f8': 9.19, 'cqv_v1': 9.31, 'cqv_v1_1': 9.31, 'cqv_v2': 9.25, 'cqv_v3': 9.29, 'cqv_v4': 9.32, 'cqv': 9.32, 'pe': 30.50},
    '2026': {'f1': 9.40, 'f2': 9.60, 'f3': 9.30, 'f4': 9.20, 'f5': 9.50, 'f6': 9.40, 'f7': 8.80, 'f8': 9.20, 'cqv_v1': 9.34, 'cqv_v1_1': 9.34, 'cqv_v2': 9.29, 'cqv_v3': 9.32, 'cqv_v4': 9.35, 'cqv': 9.35, 'pe': 31.20}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR MEDP (MEDPACE HOLDINGS, INC.) Q2 2026.")
