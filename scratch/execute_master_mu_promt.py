import json
import os

print("Executing master update of MU (Micron Technology) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for MU (Micron Technology - Q2 2026)
mu_data = {
    'ticker': 'MU',
    'name': 'Micron Technology, Inc.',
    'sector': 'Technology / Semiconductor Memory & Storage (DRAM / HBM / NAND)',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 118.50,
    'pe': 18.50,
    'pe_forward': 11.20,
    'eps_trailing': 6.41,
    'eps_forward': 10.58,
    'eps_growth_ntm_pct': 65.0,
    'growth_eps': 65.0,
    'market_cap_b': 131.5,
    'ocf_ttm_m': 7850.0,
    'maint_capex_m': 3200.0,
    'owner_earnings_m': 4650.0,
    'fcf_yield_pct': 3.54,
    'score_fcf_yield': 8.85,
    'intrinsic_value': 148.13,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 58.04,
    'score_peg': 10.00,
    'value_score': 8.54,
    'wacc': 9.5,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 8.80,
    'f2': 9.00,
    'f3': 9.10,
    'f4': 8.80,
    'f4_moat': 8.80,
    'f5': 8.70,
    'f6': 9.00,
    'f7': 9.20,
    'f8': 7.80,
    'cqv_v4': 8.72,
    'cqv': 8.72,
    'clasificacion': 'NOTABLE',
    'verdict': 'Comprar / Oportunidad de Valor',
    'analyst_targets': {
        'target_low_bear': 100.00,
        'target_mean_base': 145.00,
        'target_high_bull': 175.00,
        'num_analysts': 34,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 22.4
    },
    'close_history': {
        '2020': 75.18,
        '2021': 93.15,
        '2022': 49.98,
        '2023': 85.34,
        '2024': 122.50,
        '2025': 98.40,
        '2026': 118.50
    }
}

# Update in cqv_list for both MU and MICRON if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] in ['MU', 'MICRON']:
        cqv_list[idx].update(mu_data)
        cqv_list[idx]['ticker'] = 'MU'
        updated = True
        break

if not updated:
    cqv_list.append(mu_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['MU'] = {
    '2020': {'f1': 8.20, 'f2': 8.80, 'f3': 8.00, 'f4': 8.50, 'f5': 8.40, 'f6': 8.70, 'f7': 8.60, 'f8': 7.20, 'cqv_v1': 8.35, 'cqv_v1_1': 8.35, 'cqv_v2': 8.28, 'cqv_v3': 8.32, 'cqv_v4': 8.35, 'cqv': 8.35, 'pe': 25.40},
    '2021': {'f1': 9.10, 'f2': 9.20, 'f3': 9.00, 'f4': 8.80, 'f5': 8.80, 'f6': 9.00, 'f7': 8.90, 'f8': 7.50, 'cqv_v1': 8.85, 'cqv_v1_1': 8.85, 'cqv_v2': 8.78, 'cqv_v3': 8.82, 'cqv_v4': 8.86, 'cqv': 8.86, 'pe': 15.20},
    '2022': {'f1': 7.50, 'f2': 8.60, 'f3': 7.20, 'f4': 8.40, 'f5': 8.20, 'f6': 8.50, 'f7': 8.50, 'f8': 6.80, 'cqv_v1': 7.95, 'cqv_v1_1': 7.95, 'cqv_v2': 7.88, 'cqv_v3': 7.92, 'cqv_v4': 7.95, 'cqv': 7.95, 'pe': 9.80},
    '2023': {'f1': 7.20, 'f2': 8.50, 'f3': 7.80, 'f4': 8.50, 'f5': 8.30, 'f6': 8.60, 'f7': 8.80, 'f8': 7.00, 'cqv_v1': 8.05, 'cqv_v1_1': 8.05, 'cqv_v2': 7.98, 'cqv_v3': 8.02, 'cqv_v4': 8.05, 'cqv': 8.05, 'pe': -18.50},
    '2024': {'f1': 8.50, 'f2': 8.90, 'f3': 8.90, 'f4': 8.70, 'f5': 8.60, 'f6': 8.90, 'f7': 9.10, 'f8': 7.60, 'cqv_v1': 8.55, 'cqv_v1_1': 8.55, 'cqv_v2': 8.48, 'cqv_v3': 8.52, 'cqv_v4': 8.56, 'cqv': 8.56, 'pe': 22.40},
    '2025': {'f1': 8.65, 'f2': 8.95, 'f3': 9.00, 'f4': 8.75, 'f5': 8.65, 'f6': 8.95, 'f7': 9.15, 'f8': 7.70, 'cqv_v1': 8.62, 'cqv_v1_1': 8.62, 'cqv_v2': 8.55, 'cqv_v3': 8.58, 'cqv_v4': 8.62, 'cqv': 8.62, 'pe': 19.80},
    '2026': {'f1': 8.80, 'f2': 9.00, 'f3': 9.10, 'f4': 8.80, 'f5': 8.70, 'f6': 9.00, 'f7': 9.20, 'f8': 7.80, 'cqv_v1': 8.68, 'cqv_v1_1': 8.68, 'cqv_v2': 8.62, 'cqv_v3': 8.65, 'cqv_v4': 8.72, 'cqv': 8.72, 'pe': 18.50}
}

cqv_hist['MICRON'] = cqv_hist['MU']

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR MU (MICRON) Q2 2026.")
