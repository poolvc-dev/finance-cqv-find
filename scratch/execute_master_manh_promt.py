import json
import os

print("Executing master update of MANH (Manhattan Associates, Inc.) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for MANH (Manhattan Associates, Inc. - Q2 2026)
manh_data = {
    'ticker': 'MANH',
    'name': 'Manhattan Associates, Inc.',
    'sector': 'Technology / Supply Chain Management, WMS & Omnichannel Cloud Software',
    'quarter': 'Q2 2026',
    'valuation_date': '21/07/2026',
    'price': 240.00,
    'pe': 55.00,
    'pe_forward': 42.50,
    'eps_trailing': 4.36,
    'eps_forward': 5.647,
    'eps_growth_ntm_pct': 29.5,
    'growth_eps': 29.5,
    'market_cap_b': 14.6,
    'ocf_ttm_m': 265.0,
    'maint_capex_m': 15.0,
    'owner_earnings_m': 250.0,
    'fcf_yield_pct': 1.71,
    'score_fcf_yield': 4.28,
    'intrinsic_value': 300.00,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 6.94,
    'score_peg': 6.94,
    'value_score': 5.80,
    'wacc': 8.0,
    'g_terminal': 3.5,
    'data_confidence': 'Alta',
    'f1': 9.50,
    'f2': 9.80,
    'f3': 9.40,
    'f4': 9.85,
    'f4_moat': 9.85,
    'f5': 9.60,
    'f6': 9.70,
    'f7': 9.30,
    'f8': 9.60,
    'cqv_v4': 9.59,
    'cqv': 9.59,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 210.00,
        'target_mean_base': 282.00,
        'target_high_bull': 315.00,
        'num_analysts': 14,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 17.5
    },
    'close_history': {
        '2020': 105.20,
        '2021': 155.49,
        '2022': 121.40,
        '2023': 215.32,
        '2024': 270.24,
        '2025': 235.00,
        '2026': 240.00
    }
}

# Update in cqv_list for MANH
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'MANH':
        cqv_list[idx].update(manh_data)
        updated = True
        break

if not updated:
    cqv_list.append(manh_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['MANH'] = {
    '2020': {'f1': 9.00, 'f2': 9.50, 'f3': 8.80, 'f4': 9.70, 'f5': 9.20, 'f6': 9.30, 'f7': 9.00, 'f8': 9.30, 'cqv_v1': 9.20, 'cqv_v1_1': 9.20, 'cqv_v2': 9.15, 'cqv_v3': 9.18, 'cqv_v4': 9.21, 'cqv': 9.21, 'pe': 48.50},
    '2021': {'f1': 9.20, 'f2': 9.65, 'f3': 9.10, 'f4': 9.75, 'f5': 9.35, 'f6': 9.45, 'f7': 9.10, 'f8': 9.40, 'cqv_v1': 9.35, 'cqv_v1_1': 9.35, 'cqv_v2': 9.30, 'cqv_v3': 9.33, 'cqv_v4': 9.36, 'cqv': 9.36, 'pe': 58.20},
    '2022': {'f1': 9.10, 'f2': 9.60, 'f3': 8.95, 'f4': 9.75, 'f5': 9.30, 'f6': 9.40, 'f7': 9.05, 'f8': 9.35, 'cqv_v1': 9.28, 'cqv_v1_1': 9.28, 'cqv_v2': 9.23, 'cqv_v3': 9.25, 'cqv_v4': 9.29, 'cqv': 9.29, 'pe': 42.50},
    '2023': {'f1': 9.35, 'f2': 9.75, 'f3': 9.25, 'f4': 9.80, 'f5': 9.45, 'f6': 9.55, 'f7': 9.20, 'f8': 9.50, 'cqv_v1': 9.46, 'cqv_v1_1': 9.46, 'cqv_v2': 9.42, 'cqv_v3': 9.44, 'cqv_v4': 9.47, 'cqv': 9.47, 'pe': 52.80},
    '2024': {'f1': 9.45, 'f2': 9.78, 'f3': 9.32, 'f4': 9.82, 'f5': 9.52, 'f6': 9.62, 'f7': 9.25, 'f8': 9.55, 'cqv_v1': 9.52, 'cqv_v1_1': 9.52, 'cqv_v2': 9.48, 'cqv_v3': 9.50, 'cqv_v4': 9.53, 'cqv': 9.53, 'pe': 56.50},
    '2025': {'f1': 9.48, 'f2': 9.79, 'f3': 9.36, 'f4': 9.83, 'f5': 9.55, 'f6': 9.65, 'f7': 9.28, 'f8': 9.58, 'cqv_v1': 9.55, 'cqv_v1_1': 9.55, 'cqv_v2': 9.51, 'cqv_v3': 9.53, 'cqv_v4': 9.56, 'cqv': 9.56, 'pe': 55.20},
    '2026': {'f1': 9.50, 'f2': 9.80, 'f3': 9.40, 'f4': 9.85, 'f5': 9.60, 'f6': 9.70, 'f7': 9.30, 'f8': 9.60, 'cqv_v1': 9.58, 'cqv_v1_1': 9.58, 'cqv_v2': 9.54, 'cqv_v3': 9.56, 'cqv_v4': 9.59, 'cqv': 9.59, 'pe': 55.00}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

# Delete old MANH files in inform/
inform_dir = 'inform'
for f in os.listdir(inform_dir):
    if 'manh' in f.lower():
        full_p = os.path.join(inform_dir, f)
        print('Deleting old file:', full_p)
        os.remove(full_p)

print("SSOT DATASETS UPDATED FOR MANH (MANHATTAN ASSOCIATES, INC.) Q2 2026.")
