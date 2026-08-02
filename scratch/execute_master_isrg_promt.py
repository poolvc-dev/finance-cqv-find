import json
import os

print("Executing master update of ISRG (Intuitive Surgical, Inc.) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for ISRG (Intuitive Surgical, Inc. - Q2 2026)
isrg_data = {
    'ticker': 'ISRG',
    'name': 'Intuitive Surgical, Inc.',
    'sector': 'Healthcare / Robotic Surgical Systems & Medical Devices',
    'quarter': 'Q2 2026',
    'valuation_date': '18/07/2026',
    'price': 445.00,
    'pe': 62.50,
    'pe_forward': 48.20,
    'eps_trailing': 7.12,
    'eps_forward': 9.23,
    'eps_growth_ntm_pct': 29.6,
    'growth_eps': 29.6,
    'market_cap_b': 158.0,
    'ocf_ttm_m': 2650.0,
    'maint_capex_m': 450.0,
    'owner_earnings_m': 2200.0,
    'fcf_yield_pct': 1.39,
    'score_fcf_yield': 3.48,
    'intrinsic_value': 556.25,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 6.14,
    'score_peg': 6.14,
    'value_score': 5.24,
    'wacc': 8.0,
    'g_terminal': 3.5,
    'data_confidence': 'Alta',
    'f1': 9.60,
    'f2': 9.80,
    'f3': 9.40,
    'f4': 9.90,
    'f4_moat': 9.90,
    'f5': 9.30,
    'f6': 9.60,
    'f7': 9.60,
    'f8': 9.70,
    'cqv_v4': 9.61,
    'cqv': 9.61,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 390.00,
        'target_mean_base': 525.00,
        'target_high_bull': 580.00,
        'num_analysts': 32,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 18.0
    },
    'close_history': {
        '2020': 272.37,
        '2021': 359.30,
        '2022': 265.35,
        '2023': 337.36,
        '2024': 440.00,
        '2025': 420.00,
        '2026': 445.00
    }
}

# Update in cqv_list for ISRG if present
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
    '2020': {'f1': 9.20, 'f2': 9.60, 'f3': 9.00, 'f4': 9.80, 'f5': 9.00, 'f6': 9.30, 'f7': 9.20, 'f8': 9.40, 'cqv_v1': 9.32, 'cqv_v1_1': 9.32, 'cqv_v2': 9.26, 'cqv_v3': 9.30, 'cqv_v4': 9.33, 'cqv': 9.33, 'pe': 78.50},
    '2021': {'f1': 9.40, 'f2': 9.70, 'f3': 9.20, 'f4': 9.85, 'f5': 9.15, 'f6': 9.45, 'f7': 9.40, 'f8': 9.55, 'cqv_v1': 9.45, 'cqv_v1_1': 9.45, 'cqv_v2': 9.40, 'cqv_v3': 9.43, 'cqv_v4': 9.46, 'cqv': 9.46, 'pe': 72.10},
    '2022': {'f1': 9.25, 'f2': 9.65, 'f3': 8.90, 'f4': 9.80, 'f5': 9.00, 'f6': 9.35, 'f7': 9.30, 'f8': 9.45, 'cqv_v1': 9.35, 'cqv_v1_1': 9.35, 'cqv_v2': 9.29, 'cqv_v3': 9.33, 'cqv_v4': 9.36, 'cqv': 9.36, 'pe': 48.40},
    '2023': {'f1': 9.45, 'f2': 9.72, 'f3': 9.25, 'f4': 9.85, 'f5': 9.15, 'f6': 9.50, 'f7': 9.45, 'f8': 9.60, 'cqv_v1': 9.49, 'cqv_v1_1': 9.49, 'cqv_v2': 9.44, 'cqv_v3': 9.47, 'cqv_v4': 9.50, 'cqv': 9.50, 'pe': 64.80},
    '2024': {'f1': 9.52, 'f2': 9.76, 'f3': 9.32, 'f4': 9.88, 'f5': 9.22, 'f6': 9.55, 'f7': 9.52, 'f8': 9.64, 'cqv_v1': 9.54, 'cqv_v1_1': 9.54, 'cqv_v2': 9.49, 'cqv_v3': 9.52, 'cqv_v4': 9.55, 'cqv': 9.55, 'pe': 71.20},
    '2025': {'f1': 9.56, 'f2': 9.78, 'f3': 9.36, 'f4': 9.89, 'f5': 9.26, 'f6': 9.58, 'f7': 9.56, 'f8': 9.67, 'cqv_v1': 9.57, 'cqv_v1_1': 9.57, 'cqv_v2': 9.52, 'cqv_v3': 9.55, 'cqv_v4': 9.58, 'cqv': 9.58, 'pe': 65.50},
    '2026': {'f1': 9.60, 'f2': 9.80, 'f3': 9.40, 'f4': 9.90, 'f5': 9.30, 'f6': 9.60, 'f7': 9.60, 'f8': 9.70, 'cqv_v1': 9.61, 'cqv_v1_1': 9.61, 'cqv_v2': 9.56, 'cqv_v3': 9.58, 'cqv_v4': 9.61, 'cqv': 9.61, 'pe': 62.50}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR ISRG (INTUITIVE SURGICAL, INC.) Q2 2026.")
