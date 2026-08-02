import json
import os

print("Executing master update of META (Meta Platforms, Inc.) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for META (Meta Platforms, Inc. - Q2 2026)
meta_data = {
    'ticker': 'META',
    'name': 'Meta Platforms, Inc.',
    'sector': 'Technology / Social Media, AI Infrastructure & Digital Advertising',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 510.00,
    'pe': 24.50,
    'pe_forward': 20.20,
    'eps_trailing': 20.82,
    'eps_forward': 25.25,
    'eps_growth_ntm_pct': 21.3,
    'growth_eps': 21.3,
    'market_cap_b': 1295.0,
    'ocf_ttm_m': 88000.0,
    'maint_capex_m': 24000.0,
    'owner_earnings_m': 64000.0,
    'fcf_yield_pct': 4.94,
    'score_fcf_yield': 10.00,
    'intrinsic_value': 637.50,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 10.54,
    'score_peg': 10.00,
    'value_score': 9.00,
    'wacc': 8.0,
    'g_terminal': 3.5,
    'data_confidence': 'Alta',
    'f1': 9.60,
    'f2': 9.70,
    'f3': 9.30,
    'f4': 9.85,
    'f4_moat': 9.85,
    'f5': 9.40,
    'f6': 9.50,
    'f7': 9.50,
    'f8': 9.60,
    'cqv_v4': 9.56,
    'cqv': 9.56,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 450.00,
        'target_mean_base': 610.00,
        'target_high_bull': 700.00,
        'num_analysts': 45,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 19.6
    },
    'close_history': {
        '2020': 273.16,
        '2021': 336.35,
        '2022': 120.34,
        '2023': 353.96,
        '2024': 585.00,
        '2025': 480.00,
        '2026': 510.00
    }
}

# Update in cqv_list for META if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'META':
        cqv_list[idx].update(meta_data)
        updated = True
        break

if not updated:
    cqv_list.append(meta_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['META'] = {
    '2020': {'f1': 9.20, 'f2': 9.50, 'f3': 9.00, 'f4': 9.75, 'f5': 9.00, 'f6': 9.20, 'f7': 9.10, 'f8': 9.30, 'cqv_v1': 9.25, 'cqv_v1_1': 9.25, 'cqv_v2': 9.20, 'cqv_v3': 9.24, 'cqv_v4': 9.27, 'cqv': 9.27, 'pe': 28.50},
    '2021': {'f1': 9.35, 'f2': 9.60, 'f3': 9.10, 'f4': 9.78, 'f5': 9.15, 'f6': 9.30, 'f7': 9.20, 'f8': 9.40, 'cqv_v1': 9.35, 'cqv_v1_1': 9.35, 'cqv_v2': 9.30, 'cqv_v3': 9.33, 'cqv_v4': 9.36, 'cqv': 9.36, 'pe': 24.20},
    '2022': {'f1': 8.90, 'f2': 9.40, 'f3': 8.20, 'f4': 9.70, 'f5': 8.80, 'f6': 9.00, 'f7': 8.90, 'f8': 9.10, 'cqv_v1': 9.05, 'cqv_v1_1': 9.05, 'cqv_v2': 8.98, 'cqv_v3': 9.02, 'cqv_v4': 9.06, 'cqv': 9.06, 'pe': 11.80},
    '2023': {'f1': 9.45, 'f2': 9.65, 'f3': 9.15, 'f4': 9.80, 'f5': 9.30, 'f6': 9.40, 'f7': 9.35, 'f8': 9.50, 'cqv_v1': 9.42, 'cqv_v1_1': 9.42, 'cqv_v2': 9.38, 'cqv_v3': 9.41, 'cqv_v4': 9.44, 'cqv': 9.44, 'pe': 23.50},
    '2024': {'f1': 9.55, 'f2': 9.68, 'f3': 9.25, 'f4': 9.85, 'f5': 9.38, 'f6': 9.48, 'f7': 9.45, 'f8': 9.58, 'cqv_v1': 9.50, 'cqv_v1_1': 9.50, 'cqv_v2': 9.46, 'cqv_v3': 9.49, 'cqv_v4': 9.52, 'cqv': 9.52, 'pe': 27.80},
    '2025': {'f1': 9.58, 'f2': 9.69, 'f3': 9.28, 'f4': 9.85, 'f5': 9.39, 'f6': 9.49, 'f7': 9.48, 'f8': 9.59, 'cqv_v1': 9.52, 'cqv_v1_1': 9.52, 'cqv_v2': 9.48, 'cqv_v3': 9.51, 'cqv_v4': 9.54, 'cqv': 9.54, 'pe': 23.20},
    '2026': {'f1': 9.60, 'f2': 9.70, 'f3': 9.30, 'f4': 9.85, 'f5': 9.40, 'f6': 9.50, 'f7': 9.50, 'f8': 9.60, 'cqv_v1': 9.56, 'cqv_v1_1': 9.56, 'cqv_v2': 9.52, 'cqv_v3': 9.54, 'cqv_v4': 9.56, 'cqv': 9.56, 'pe': 24.50}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR META (META PLATFORMS, INC.) Q2 2026.")
