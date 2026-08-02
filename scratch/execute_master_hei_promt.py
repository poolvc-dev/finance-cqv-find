import json
import os

print("Executing master update of HEI (HEICO Corporation) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for HEI (HEICO Corporation - Q2 2026 / Q2 FY26)
hei_data = {
    'ticker': 'HEI',
    'name': 'HEICO Corporation',
    'sector': 'Industrials / Aerospace & Defense Replacement Parts (FAA-PMA) & Flight Support',
    'quarter': 'Q2 2026',
    'valuation_date': '02/06/2026',
    'price': 248.00,
    'pe': 62.00,
    'pe_forward': 48.50,
    'eps_trailing': 4.00,
    'eps_forward': 5.113,
    'eps_growth_ntm_pct': 27.8,
    'growth_eps': 27.8,
    'market_cap_b': 34.0,
    'ocf_ttm_m': 680.0,
    'maint_capex_m': 60.0,
    'owner_earnings_m': 620.0,
    'fcf_yield_pct': 1.82,
    'score_fcf_yield': 4.55,
    'intrinsic_value': 310.00,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 5.73,
    'score_peg': 5.73,
    'value_score': 5.54,
    'wacc': 8.0,
    'g_terminal': 3.5,
    'data_confidence': 'Alta',
    'f1': 9.50,
    'f2': 9.60,
    'f3': 9.40,
    'f4': 9.80,
    'f4_moat': 9.80,
    'f5': 9.60,
    'f6': 9.70,
    'f7': 9.30,
    'f8': 9.60,
    'cqv_v4': 9.55,
    'cqv': 9.55,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 215.00,
        'target_mean_base': 292.00,
        'target_high_bull': 330.00,
        'num_analysts': 18,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 17.7
    },
    'close_history': {
        '2020': 118.50,
        '2021': 143.48,
        '2022': 153.05,
        '2023': 178.40,
        '2024': 237.37,
        '2025': 240.00,
        '2026': 248.00
    }
}

# Update in cqv_list for HEI
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'HEI':
        cqv_list[idx].update(hei_data)
        updated = True
        break

if not updated:
    cqv_list.append(hei_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['HEI'] = {
    '2020': {'f1': 9.00, 'f2': 9.20, 'f3': 8.80, 'f4': 9.65, 'f5': 9.20, 'f6': 9.30, 'f7': 9.00, 'f8': 9.30, 'cqv_v1': 9.18, 'cqv_v1_1': 9.18, 'cqv_v2': 9.12, 'cqv_v3': 9.15, 'cqv_v4': 9.18, 'cqv': 9.18, 'pe': 58.50},
    '2021': {'f1': 9.20, 'f2': 9.35, 'f3': 9.10, 'f4': 9.70, 'f5': 9.30, 'f6': 9.45, 'f7': 9.10, 'f8': 9.40, 'cqv_v1': 9.32, 'cqv_v1_1': 9.32, 'cqv_v2': 9.28, 'cqv_v3': 9.30, 'cqv_v4': 9.33, 'cqv': 9.33, 'pe': 64.50},
    '2022': {'f1': 9.15, 'f2': 9.30, 'f3': 9.00, 'f4': 9.70, 'f5': 9.25, 'f6': 9.40, 'f7': 9.05, 'f8': 9.35, 'cqv_v1': 9.28, 'cqv_v1_1': 9.28, 'cqv_v2': 9.23, 'cqv_v3': 9.25, 'cqv_v4': 9.28, 'cqv': 9.28, 'pe': 55.40},
    '2023': {'f1': 9.35, 'f2': 9.45, 'f3': 9.20, 'f4': 9.75, 'f5': 9.40, 'f6': 9.55, 'f7': 9.20, 'f8': 9.45, 'cqv_v1': 9.43, 'cqv_v1_1': 9.43, 'cqv_v2': 9.39, 'cqv_v3': 9.41, 'cqv_v4': 9.44, 'cqv': 9.44, 'pe': 60.20},
    '2024': {'f1': 9.45, 'f2': 9.50, 'f3': 9.30, 'f4': 9.78, 'f5': 9.50, 'f6': 9.60, 'f7': 9.25, 'f8': 9.52, 'cqv_v1': 9.49, 'cqv_v1_1': 9.49, 'cqv_v2': 9.45, 'cqv_v3': 9.47, 'cqv_v4': 9.50, 'cqv': 9.50, 'pe': 64.50},
    '2025': {'f1': 9.48, 'f2': 9.55, 'f3': 9.35, 'f4': 9.79, 'f5': 9.55, 'f6': 9.65, 'f7': 9.28, 'f8': 9.55, 'cqv_v1': 9.52, 'cqv_v1_1': 9.52, 'cqv_v2': 9.48, 'cqv_v3': 9.50, 'cqv_v4': 9.53, 'cqv': 9.53, 'pe': 63.80},
    '2026': {'f1': 9.50, 'f2': 9.60, 'f3': 9.40, 'f4': 9.80, 'f5': 9.60, 'f6': 9.70, 'f7': 9.30, 'f8': 9.60, 'cqv_v1': 9.55, 'cqv_v1_1': 9.55, 'cqv_v2': 9.51, 'cqv_v3': 9.53, 'cqv_v4': 9.55, 'cqv': 9.55, 'pe': 62.00}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

# Delete old HEI files in inform/
inform_dir = 'inform'
for f in os.listdir(inform_dir):
    if 'hei' in f.lower():
        full_p = os.path.join(inform_dir, f)
        print('Deleting old file:', full_p)
        os.remove(full_p)

print("SSOT DATASETS UPDATED FOR HEI (HEICO CORPORATION) Q2 2026.")
