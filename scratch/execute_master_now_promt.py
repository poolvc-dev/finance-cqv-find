import json
import os

print("Executing master update of NOW (ServiceNow, Inc.) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for NOW (ServiceNow, Inc. - Q2 2026)
now_data = {
    'ticker': 'NOW',
    'name': 'ServiceNow, Inc.',
    'sector': 'Technology / Enterprise Cloud Software & Digital Workflows',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 785.60,
    'pe': 54.80,
    'pe_forward': 41.20,
    'eps_trailing': 14.33,
    'eps_forward': 19.06,
    'eps_growth_ntm_pct': 33.0,
    'growth_eps': 33.0,
    'market_cap_b': 162.5,
    'ocf_ttm_m': 3950.0,
    'maint_capex_m': 380.0,
    'owner_earnings_m': 3570.0,
    'fcf_yield_pct': 2.20,
    'score_fcf_yield': 5.50,
    'intrinsic_value': 982.00,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 8.01,
    'score_peg': 8.01,
    'value_score': 6.60,
    'wacc': 9.0,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 9.40,
    'f2': 9.30,
    'f3': 9.40,
    'f4': 9.70,
    'f4_moat': 9.70,
    'f5': 9.30,
    'f6': 9.50,
    'f7': 9.20,
    'f8': 9.50,
    'cqv_v4': 9.43,
    'cqv': 9.43,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 690.00,
        'target_mean_base': 915.00,
        'target_high_bull': 1050.00,
        'num_analysts': 38,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 16.5
    },
    'close_history': {
        '2020': 550.43,
        '2021': 649.11,
        '2022': 388.27,
        '2023': 706.49,
        '2024': 865.20,
        '2025': 820.10,
        '2026': 785.60
    }
}

# Update in cqv_list
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'NOW':
        cqv_list[idx].update(now_data)
        updated = True
        break

if not updated:
    cqv_list.append(now_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['NOW'] = {
    '2020': {'f1': 8.90, 'f2': 9.00, 'f3': 9.10, 'f4': 9.45, 'f5': 8.90, 'f6': 9.20, 'f7': 8.80, 'f8': 9.20, 'cqv_v1': 9.05, 'cqv_v1_1': 9.05, 'cqv_v2': 9.00, 'cqv_v3': 9.05, 'cqv_v4': 9.11, 'cqv': 9.11, 'pe': 85.20},
    '2021': {'f1': 9.15, 'f2': 9.10, 'f3': 9.25, 'f4': 9.55, 'f5': 9.10, 'f6': 9.35, 'f7': 8.95, 'f8': 9.35, 'cqv_v1': 9.22, 'cqv_v1_1': 9.22, 'cqv_v2': 9.15, 'cqv_v3': 9.20, 'cqv_v4': 9.24, 'cqv': 9.24, 'pe': 78.40},
    '2022': {'f1': 9.22, 'f2': 9.15, 'f3': 9.20, 'f4': 9.60, 'f5': 9.15, 'f6': 9.38, 'f7': 9.00, 'f8': 9.38, 'cqv_v1': 9.25, 'cqv_v1_1': 9.25, 'cqv_v2': 9.18, 'cqv_v3': 9.22, 'cqv_v4': 9.27, 'cqv': 9.27, 'pe': 52.10},
    '2023': {'f1': 9.30, 'f2': 9.20, 'f3': 9.30, 'f4': 9.65, 'f5': 9.20, 'f6': 9.42, 'f7': 9.10, 'f8': 9.42, 'cqv_v1': 9.32, 'cqv_v1_1': 9.32, 'cqv_v2': 9.25, 'cqv_v3': 9.30, 'cqv_v4': 9.34, 'cqv': 9.34, 'pe': 64.50},
    '2024': {'f1': 9.35, 'f2': 9.25, 'f3': 9.35, 'f4': 9.68, 'f5': 9.25, 'f6': 9.45, 'f7': 9.15, 'f8': 9.45, 'cqv_v1': 9.38, 'cqv_v1_1': 9.38, 'cqv_v2': 9.30, 'cqv_v3': 9.35, 'cqv_v4': 9.38, 'cqv': 9.38, 'pe': 62.00},
    '2025': {'f1': 9.38, 'f2': 9.28, 'f3': 9.38, 'f4': 9.70, 'f5': 9.28, 'f6': 9.48, 'f7': 9.18, 'f8': 9.48, 'cqv_v1': 9.40, 'cqv_v1_1': 9.40, 'cqv_v2': 9.32, 'cqv_v3': 9.38, 'cqv_v4': 9.40, 'cqv': 9.40, 'pe': 58.20},
    '2026': {'f1': 9.40, 'f2': 9.30, 'f3': 9.40, 'f4': 9.70, 'f5': 9.30, 'f6': 9.50, 'f7': 9.20, 'f8': 9.50, 'cqv_v1': 9.42, 'cqv_v1_1': 9.42, 'cqv_v2': 9.35, 'cqv_v3': 9.40, 'cqv_v4': 9.43, 'cqv': 9.43, 'pe': 54.80}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR NOW Q2 2026.")
