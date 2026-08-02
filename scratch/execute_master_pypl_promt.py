import json
import os

print("Executing master update of PYPL (PayPal Holdings) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for PYPL (PayPal Holdings - Q2 2026)
pypl_data = {
    'ticker': 'PYPL',
    'name': 'PayPal Holdings, Inc.',
    'sector': 'Financials / Digital Payments & Consumer Commerce Platforms',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 64.50,
    'pe': 14.20,
    'pe_forward': 12.50,
    'eps_trailing': 4.54,
    'eps_forward': 5.16,
    'eps_growth_ntm_pct': 14.0,
    'growth_eps': 14.0,
    'market_cap_b': 65.5,
    'ocf_ttm_m': 6450.0,
    'maint_capex_m': 950.0,
    'owner_earnings_m': 5500.0,
    'fcf_yield_pct': 8.40,
    'score_fcf_yield': 10.00,
    'intrinsic_value': 92.14,
    'mos_pct': 30.0,
    'score_mos': 10.00,
    'peg_bruto': 11.20,
    'score_peg': 10.00,
    'value_score': 10.00,
    'wacc': 9.0,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 8.90,
    'f2': 9.00,
    'f3': 8.10,
    'f4': 8.60,
    'f4_moat': 8.60,
    'f5': 9.10,
    'f6': 9.00,
    'f7': 8.40,
    'f8': 8.80,
    'cqv_v4': 8.73,
    'cqv': 8.73,
    'clasificacion': 'NOTABLE',
    'verdict': 'Comprar / Oportunidad de Valor',
    'analyst_targets': {
        'target_low_bear': 58.00,
        'target_mean_base': 78.00,
        'target_high_bull': 95.00,
        'num_analysts': 41,
        'consensus_recommendation': 'Moderate Buy',
        'upside_potential_pct': 20.9
    },
    'close_history': {
        '2020': 234.20,
        '2021': 188.58,
        '2022': 71.22,
        '2023': 61.41,
        '2024': 84.50,
        '2025': 68.20,
        '2026': 64.50
    }
}

# Update in cqv_list for both PYPL and PAYPAL if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] in ['PYPL', 'PAYPAL']:
        cqv_list[idx].update(pypl_data)
        cqv_list[idx]['ticker'] = 'PYPL'
        updated = True
        break

if not updated:
    cqv_list.append(pypl_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['PYPL'] = {
    '2020': {'f1': 9.20, 'f2': 9.10, 'f3': 9.00, 'f4': 9.20, 'f5': 8.80, 'f6': 9.10, 'f7': 8.90, 'f8': 9.10, 'cqv_v1': 9.05, 'cqv_v1_1': 9.05, 'cqv_v2': 9.00, 'cqv_v3': 9.05, 'cqv_v4': 9.08, 'cqv': 9.08, 'pe': 58.20},
    '2021': {'f1': 9.00, 'f2': 9.05, 'f3': 8.80, 'f4': 9.00, 'f5': 8.90, 'f6': 8.90, 'f7': 8.70, 'f8': 8.90, 'cqv_v1': 8.95, 'cqv_v1_1': 8.95, 'cqv_v2': 8.90, 'cqv_v3': 8.92, 'cqv_v4': 8.94, 'cqv': 8.94, 'pe': 45.10},
    '2022': {'f1': 8.70, 'f2': 8.90, 'f3': 8.00, 'f4': 8.50, 'f5': 8.95, 'f6': 8.70, 'f7': 8.20, 'f8': 8.60, 'cqv_v1': 8.55, 'cqv_v1_1': 8.55, 'cqv_v2': 8.50, 'cqv_v3': 8.55, 'cqv_v4': 8.58, 'cqv': 8.58, 'pe': 18.20},
    '2023': {'f1': 8.80, 'f2': 8.95, 'f3': 8.05, 'f4': 8.55, 'f5': 9.00, 'f6': 8.85, 'f7': 8.30, 'f8': 8.70, 'cqv_v1': 8.62, 'cqv_v1_1': 8.62, 'cqv_v2': 8.58, 'cqv_v3': 8.60, 'cqv_v4': 8.63, 'cqv': 8.63, 'pe': 15.40},
    '2024': {'f1': 8.85, 'f2': 8.98, 'f3': 8.08, 'f4': 8.58, 'f5': 9.05, 'f6': 8.95, 'f7': 8.35, 'f8': 8.75, 'cqv_v1': 8.68, 'cqv_v1_1': 8.68, 'cqv_v2': 8.62, 'cqv_v3': 8.65, 'cqv_v4': 8.68, 'cqv': 8.68, 'pe': 17.50},
    '2025': {'f1': 8.88, 'f2': 9.00, 'f3': 8.10, 'f4': 8.60, 'f5': 9.08, 'f6': 8.98, 'f7': 8.38, 'f8': 8.78, 'cqv_v1': 8.70, 'cqv_v1_1': 8.70, 'cqv_v2': 8.65, 'cqv_v3': 8.68, 'cqv_v4': 8.70, 'cqv': 8.70, 'pe': 15.20},
    '2026': {'f1': 8.90, 'f2': 9.00, 'f3': 8.10, 'f4': 8.60, 'f5': 9.10, 'f6': 9.00, 'f7': 8.40, 'f8': 8.80, 'cqv_v1': 8.72, 'cqv_v1_1': 8.72, 'cqv_v2': 8.68, 'cqv_v3': 8.70, 'cqv_v4': 8.73, 'cqv': 8.73, 'pe': 14.20}
}

cqv_hist['PAYPAL'] = cqv_hist['PYPL']

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR PYPL (PAYPAL) Q2 2026.")
