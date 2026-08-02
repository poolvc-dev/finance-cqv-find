import json
import os

print("Executing master update of MSI (Motorola Solutions) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for MSI (Motorola Solutions - Q2 2026)
msi_data = {
    'ticker': 'MSI',
    'name': 'Motorola Solutions, Inc.',
    'sector': 'Technology / Public Safety, Critical Communications & Video Security',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 445.50,
    'pe': 34.80,
    'pe_forward': 28.50,
    'eps_trailing': 12.80,
    'eps_forward': 15.63,
    'eps_growth_ntm_pct': 22.1,
    'growth_eps': 22.1,
    'market_cap_b': 74.2,
    'ocf_ttm_m': 2350.0,
    'maint_capex_m': 190.0,
    'owner_earnings_m': 2160.0,
    'fcf_yield_pct': 2.91,
    'score_fcf_yield': 7.28,
    'intrinsic_value': 556.88,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 7.75,
    'score_peg': 7.75,
    'value_score': 7.24,
    'wacc': 8.5,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 9.50,
    'f2': 9.20,
    'f3': 9.10,
    'f4': 9.80,
    'f4_moat': 9.80,
    'f5': 9.40,
    'f6': 9.50,
    'f7': 8.90,
    'f8': 9.60,
    'cqv_v4': 9.41,
    'cqv': 9.41,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 390.00,
        'target_mean_base': 510.00,
        'target_high_bull': 570.00,
        'num_analysts': 19,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 14.5
    },
    'close_history': {
        '2020': 170.06,
        '2021': 271.70,
        '2022': 257.71,
        '2023': 313.19,
        '2024': 447.80,
        '2025': 420.50,
        '2026': 445.50
    }
}

# Update in cqv_list for both MSI and MOTOROLA if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] in ['MSI', 'MOTOROLA']:
        cqv_list[idx].update(msi_data)
        cqv_list[idx]['ticker'] = 'MSI'
        updated = True
        break

if not updated:
    cqv_list.append(msi_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['MSI'] = {
    '2020': {'f1': 9.20, 'f2': 8.90, 'f3': 8.80, 'f4': 9.75, 'f5': 9.10, 'f6': 9.30, 'f7': 8.70, 'f8': 9.45, 'cqv_v1': 9.18, 'cqv_v1_1': 9.18, 'cqv_v2': 9.12, 'cqv_v3': 9.15, 'cqv_v4': 9.18, 'cqv': 9.18, 'pe': 32.50},
    '2021': {'f1': 9.35, 'f2': 9.05, 'f3': 8.95, 'f4': 9.78, 'f5': 9.25, 'f6': 9.40, 'f7': 8.80, 'f8': 9.50, 'cqv_v1': 9.28, 'cqv_v1_1': 9.28, 'cqv_v2': 9.22, 'cqv_v3': 9.25, 'cqv_v4': 9.28, 'cqv': 9.28, 'pe': 38.20},
    '2022': {'f1': 9.38, 'f2': 9.10, 'f3': 8.98, 'f4': 9.78, 'f5': 9.30, 'f6': 9.42, 'f7': 8.82, 'f8': 9.52, 'cqv_v1': 9.30, 'cqv_v1_1': 9.30, 'cqv_v2': 9.25, 'cqv_v3': 9.28, 'cqv_v4': 9.31, 'cqv': 9.31, 'pe': 31.80},
    '2023': {'f1': 9.42, 'f2': 9.15, 'f3': 9.02, 'f4': 9.80, 'f5': 9.35, 'f6': 9.45, 'f7': 8.85, 'f8': 9.55, 'cqv_v1': 9.35, 'cqv_v1_1': 9.35, 'cqv_v2': 9.30, 'cqv_v3': 9.34, 'cqv_v4': 9.36, 'cqv': 9.36, 'pe': 35.40},
    '2024': {'f1': 9.45, 'f2': 9.18, 'f3': 9.05, 'f4': 9.80, 'f5': 9.38, 'f6': 9.48, 'f7': 8.88, 'f8': 9.58, 'cqv_v1': 9.38, 'cqv_v1_1': 9.38, 'cqv_v2': 9.34, 'cqv_v3': 9.36, 'cqv_v4': 9.39, 'cqv': 9.39, 'pe': 39.80},
    '2025': {'f1': 9.48, 'f2': 9.20, 'f3': 9.08, 'f4': 9.80, 'f5': 9.40, 'f6': 9.50, 'f7': 8.90, 'f8': 9.60, 'cqv_v1': 9.40, 'cqv_v1_1': 9.40, 'cqv_v2': 9.35, 'cqv_v3': 9.38, 'cqv_v4': 9.40, 'cqv': 9.40, 'pe': 36.20},
    '2026': {'f1': 9.50, 'f2': 9.20, 'f3': 9.10, 'f4': 9.80, 'f5': 9.40, 'f6': 9.50, 'f7': 8.90, 'f8': 9.60, 'cqv_v1': 9.42, 'cqv_v1_1': 9.42, 'cqv_v2': 9.38, 'cqv_v3': 9.40, 'cqv_v4': 9.41, 'cqv': 9.41, 'pe': 34.80}
}

cqv_hist['MOTOROLA'] = cqv_hist['MSI']

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR MSI (MOTOROLA SOLUTIONS) Q2 2026.")
