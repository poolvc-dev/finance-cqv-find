import json
import os

print("Executing master update of V (Visa Inc.) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for V (Visa Inc. - Q2 2026)
v_data = {
    'ticker': 'V',
    'name': 'Visa Inc.',
    'sector': 'Financials / Payment Processing & Financial Networks',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 272.50,
    'pe': 27.80,
    'pe_forward': 23.20,
    'eps_trailing': 9.80,
    'eps_forward': 11.75,
    'eps_growth_ntm_pct': 19.9,
    'growth_eps': 19.9,
    'market_cap_b': 552.0,
    'ocf_ttm_m': 21800.0,
    'maint_capex_m': 1200.0,
    'owner_earnings_m': 20600.0,
    'fcf_yield_pct': 3.73,
    'score_fcf_yield': 9.33,
    'intrinsic_value': 340.63,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 8.58,
    'score_peg': 8.58,
    'value_score': 8.31,
    'wacc': 9.0,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 9.80,
    'f2': 9.60,
    'f3': 9.20,
    'f4': 9.90,
    'f4_moat': 9.90,
    'f5': 9.60,
    'f6': 9.50,
    'f7': 9.00,
    'f8': 9.70,
    'cqv_v4': 9.58,
    'cqv': 9.58,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 245.00,
        'target_mean_base': 315.00,
        'target_high_bull': 355.00,
        'num_analysts': 42,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 15.6
    },
    'close_history': {
        '2020': 218.73,
        '2021': 216.71,
        '2022': 207.76,
        '2023': 260.35,
        '2024': 282.50,
        '2025': 278.10,
        '2026': 272.50
    }
}

# Update in cqv_list for both V and VISA if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] in ['V', 'VISA']:
        cqv_list[idx].update(v_data)
        cqv_list[idx]['ticker'] = 'V'
        updated = True
        break

if not updated:
    cqv_list.append(v_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['V'] = {
    '2020': {'f1': 9.60, 'f2': 9.40, 'f3': 8.90, 'f4': 9.85, 'f5': 9.45, 'f6': 9.30, 'f7': 8.80, 'f8': 9.50, 'cqv_v1': 9.35, 'cqv_v1_1': 9.35, 'cqv_v2': 9.30, 'cqv_v3': 9.35, 'cqv_v4': 9.39, 'cqv': 9.39, 'pe': 38.50},
    '2021': {'f1': 9.70, 'f2': 9.50, 'f3': 9.05, 'f4': 9.88, 'f5': 9.50, 'f6': 9.40, 'f7': 8.90, 'f8': 9.60, 'cqv_v1': 9.45, 'cqv_v1_1': 9.45, 'cqv_v2': 9.38, 'cqv_v3': 9.42, 'cqv_v4': 9.46, 'cqv': 9.46, 'pe': 36.20},
    '2022': {'f1': 9.72, 'f2': 9.52, 'f3': 9.00, 'f4': 9.88, 'f5': 9.52, 'f6': 9.40, 'f7': 8.92, 'f8': 9.60, 'cqv_v1': 9.40, 'cqv_v1_1': 9.40, 'cqv_v2': 9.35, 'cqv_v3': 9.40, 'cqv_v4': 9.44, 'cqv': 9.44, 'pe': 28.50},
    '2023': {'f1': 9.75, 'f2': 9.55, 'f3': 9.10, 'f4': 9.90, 'f5': 9.55, 'f6': 9.45, 'f7': 8.95, 'f8': 9.65, 'cqv_v1': 9.48, 'cqv_v1_1': 9.48, 'cqv_v2': 9.40, 'cqv_v3': 9.45, 'cqv_v4': 9.49, 'cqv': 9.49, 'pe': 31.80},
    '2024': {'f1': 9.78, 'f2': 9.58, 'f3': 9.15, 'f4': 9.90, 'f5': 9.58, 'f6': 9.48, 'f7': 8.98, 'f8': 9.68, 'cqv_v1': 9.50, 'cqv_v1_1': 9.50, 'cqv_v2': 9.44, 'cqv_v3': 9.48, 'cqv_v4': 9.52, 'cqv': 9.52, 'pe': 30.20},
    '2025': {'f1': 9.80, 'f2': 9.60, 'f3': 9.18, 'f4': 9.90, 'f5': 9.60, 'f6': 9.50, 'f7': 9.00, 'f8': 9.70, 'cqv_v1': 9.52, 'cqv_v1_1': 9.52, 'cqv_v2': 9.46, 'cqv_v3': 9.50, 'cqv_v4': 9.55, 'cqv': 9.55, 'pe': 28.90},
    '2026': {'f1': 9.80, 'f2': 9.60, 'f3': 9.20, 'f4': 9.90, 'f5': 9.60, 'f6': 9.50, 'f7': 9.00, 'f8': 9.70, 'cqv_v1': 9.55, 'cqv_v1_1': 9.55, 'cqv_v2': 9.48, 'cqv_v3': 9.52, 'cqv_v4': 9.58, 'cqv': 9.58, 'pe': 27.80}
}

cqv_hist['VISA'] = cqv_hist['V']

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR V (VISA) Q2 2026.")
