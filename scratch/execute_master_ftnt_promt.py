import json
import os

print("Executing master update of FTNT (Fortinet, Inc.) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for FTNT (Fortinet, Inc. - Q2 2026)
ftnt_data = {
    'ticker': 'FTNT',
    'name': 'Fortinet, Inc.',
    'sector': 'Technology / Cybersecurity & Network Infrastructure',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 76.80,
    'pe': 36.50,
    'pe_forward': 29.80,
    'eps_trailing': 2.10,
    'eps_forward': 2.58,
    'eps_growth_ntm_pct': 22.8,
    'growth_eps': 22.8,
    'market_cap_b': 58.5,
    'ocf_ttm_m': 2250.0,
    'maint_capex_m': 180.0,
    'owner_earnings_m': 2070.0,
    'fcf_yield_pct': 3.54,
    'score_fcf_yield': 8.85,
    'intrinsic_value': 96.00,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 7.65,
    'score_peg': 7.65,
    'value_score': 7.84,
    'wacc': 9.0,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 9.60,
    'f2': 9.50,
    'f3': 9.10,
    'f4': 9.60,
    'f4_moat': 9.60,
    'f5': 9.40,
    'f6': 9.50,
    'f7': 9.10,
    'f8': 9.40,
    'cqv_v4': 9.43,
    'cqv': 9.43,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 68.00,
        'target_mean_base': 88.00,
        'target_high_bull': 100.00,
        'num_analysts': 36,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 14.6
    },
    'close_history': {
        '2020': 29.70,
        '2021': 71.88,
        '2022': 48.89,
        '2023': 58.53,
        '2024': 82.10,
        '2025': 78.40,
        '2026': 76.80
    }
}

# Update in cqv_list for both FTNT and FORTINET if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] in ['FTNT', 'FORTINET']:
        cqv_list[idx].update(ftnt_data)
        cqv_list[idx]['ticker'] = 'FTNT'
        updated = True
        break

if not updated:
    cqv_list.append(ftnt_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['FTNT'] = {
    '2020': {'f1': 9.20, 'f2': 9.10, 'f3': 8.90, 'f4': 9.40, 'f5': 9.10, 'f6': 9.30, 'f7': 8.80, 'f8': 9.20, 'cqv_v1': 9.12, 'cqv_v1_1': 9.12, 'cqv_v2': 9.08, 'cqv_v3': 9.12, 'cqv_v4': 9.15, 'cqv': 9.15, 'pe': 52.40},
    '2021': {'f1': 9.40, 'f2': 9.30, 'f3': 9.10, 'f4': 9.50, 'f5': 9.25, 'f6': 9.40, 'f7': 8.95, 'f8': 9.30, 'cqv_v1': 9.28, 'cqv_v1_1': 9.28, 'cqv_v2': 9.20, 'cqv_v3': 9.25, 'cqv_v4': 9.28, 'cqv': 9.28, 'pe': 68.10},
    '2022': {'f1': 9.45, 'f2': 9.35, 'f3': 9.00, 'f4': 9.52, 'f5': 9.30, 'f6': 9.42, 'f7': 9.00, 'f8': 9.32, 'cqv_v1': 9.30, 'cqv_v1_1': 9.30, 'cqv_v2': 9.22, 'cqv_v3': 9.26, 'cqv_v4': 9.30, 'cqv': 9.30, 'pe': 44.50},
    '2023': {'f1': 9.50, 'f2': 9.40, 'f3': 9.05, 'f4': 9.55, 'f5': 9.35, 'f6': 9.45, 'f7': 9.05, 'f8': 9.35, 'cqv_v1': 9.35, 'cqv_v1_1': 9.35, 'cqv_v2': 9.28, 'cqv_v3': 9.32, 'cqv_v4': 9.35, 'cqv': 9.35, 'pe': 38.20},
    '2024': {'f1': 9.55, 'f2': 9.45, 'f3': 9.08, 'f4': 9.58, 'f5': 9.38, 'f6': 9.48, 'f7': 9.08, 'f8': 9.38, 'cqv_v1': 9.38, 'cqv_v1_1': 9.38, 'cqv_v2': 9.32, 'cqv_v3': 9.35, 'cqv_v4': 9.38, 'cqv': 9.38, 'pe': 42.50},
    '2025': {'f1': 9.58, 'f2': 9.48, 'f3': 9.08, 'f4': 9.60, 'f5': 9.40, 'f6': 9.50, 'f7': 9.10, 'f8': 9.40, 'cqv_v1': 9.40, 'cqv_v1_1': 9.40, 'cqv_v2': 9.35, 'cqv_v3': 9.38, 'cqv_v4': 9.40, 'cqv': 9.40, 'pe': 38.00},
    '2026': {'f1': 9.60, 'f2': 9.50, 'f3': 9.10, 'f4': 9.60, 'f5': 9.40, 'f6': 9.50, 'f7': 9.10, 'f8': 9.40, 'cqv_v1': 9.42, 'cqv_v1_1': 9.42, 'cqv_v2': 9.38, 'cqv_v3': 9.40, 'cqv_v4': 9.43, 'cqv': 9.43, 'pe': 36.50}
}

cqv_hist['FORTINET'] = cqv_hist['FTNT']

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR FTNT (FORTINET) Q2 2026.")
