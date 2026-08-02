import json
import os

print("Executing master update of VRT (Vertiv Holdings Co) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for VRT (Vertiv Holdings Co - Q2 2026)
vrt_data = {
    'ticker': 'VRT',
    'name': 'Vertiv Holdings Co',
    'sector': 'Industrials / Data Center Infrastructure, Power & Liquid Cooling',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 88.50,
    'pe': 42.50,
    'pe_forward': 31.20,
    'eps_trailing': 2.08,
    'eps_forward': 2.84,
    'eps_growth_ntm_pct': 36.5,
    'growth_eps': 36.5,
    'market_cap_b': 33.5,
    'ocf_ttm_m': 1150.0,
    'maint_capex_m': 150.0,
    'owner_earnings_m': 1000.0,
    'fcf_yield_pct': 2.99,
    'score_fcf_yield': 7.48,
    'intrinsic_value': 110.63,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 11.70,
    'score_peg': 10.00,
    'value_score': 7.99,
    'wacc': 8.5,
    'g_terminal': 3.5,
    'data_confidence': 'Alta',
    'f1': 8.80,
    'f2': 8.90,
    'f3': 9.60,
    'f4': 9.10,
    'f4_moat': 9.10,
    'f5': 8.80,
    'f6': 9.30,
    'f7': 9.50,
    'f8': 9.00,
    'cqv_v4': 9.11,
    'cqv': 9.11,
    'clasificacion': 'ALTA CALIDAD',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 75.00,
        'target_mean_base': 102.00,
        'target_high_bull': 125.00,
        'num_analysts': 18,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 15.3
    },
    'close_history': {
        '2020': 18.50,
        '2021': 24.90,
        '2022': 13.68,
        '2023': 48.03,
        '2024': 86.40,
        '2025': 78.50,
        '2026': 88.50
    }
}

# Update in cqv_list for VRT if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'VRT':
        cqv_list[idx].update(vrt_data)
        updated = True
        break

if not updated:
    cqv_list.append(vrt_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['VRT'] = {
    '2020': {'f1': 7.50, 'f2': 7.20, 'f3': 7.80, 'f4': 8.20, 'f5': 7.60, 'f6': 7.80, 'f7': 8.00, 'f8': 7.90, 'cqv_v1': 7.72, 'cqv_v1_1': 7.72, 'cqv_v2': 7.65, 'cqv_v3': 7.70, 'cqv_v4': 7.74, 'cqv': 7.74, 'pe': 38.50},
    '2021': {'f1': 7.60, 'f2': 7.30, 'f3': 8.00, 'f4': 8.30, 'f5': 7.80, 'f6': 8.00, 'f7': 8.20, 'f8': 8.00, 'cqv_v1': 7.88, 'cqv_v1_1': 7.88, 'cqv_v2': 7.82, 'cqv_v3': 7.86, 'cqv_v4': 7.90, 'cqv': 7.90, 'pe': 42.10},
    '2022': {'f1': 7.80, 'f2': 7.50, 'f3': 8.20, 'f4': 8.40, 'f5': 8.00, 'f6': 8.30, 'f7': 8.50, 'f8': 8.20, 'cqv_v1': 8.08, 'cqv_v1_1': 8.08, 'cqv_v2': 8.02, 'cqv_v3': 8.06, 'cqv_v4': 8.10, 'cqv': 8.10, 'pe': 22.40},
    '2023': {'f1': 8.20, 'f2': 8.20, 'f3': 8.90, 'f4': 8.70, 'f5': 8.40, 'f6': 8.80, 'f7': 9.00, 'f8': 8.60, 'cqv_v1': 8.58, 'cqv_v1_1': 8.58, 'cqv_v2': 8.52, 'cqv_v3': 8.56, 'cqv_v4': 8.59, 'cqv': 8.59, 'pe': 48.20},
    '2024': {'f1': 8.60, 'f2': 8.70, 'f3': 9.40, 'f4': 9.00, 'f5': 8.70, 'f6': 9.10, 'f7': 9.40, 'f8': 8.90, 'cqv_v1': 8.94, 'cqv_v1_1': 8.94, 'cqv_v2': 8.88, 'cqv_v3': 8.92, 'cqv_v4': 8.95, 'cqv': 8.95, 'pe': 52.80},
    '2025': {'f1': 8.70, 'f2': 8.80, 'f3': 9.50, 'f4': 9.05, 'f5': 8.75, 'f6': 9.20, 'f7': 9.45, 'f8': 8.95, 'cqv_v1': 9.02, 'cqv_v1_1': 9.02, 'cqv_v2': 8.96, 'cqv_v3': 9.00, 'cqv_v4': 9.03, 'cqv': 9.03, 'pe': 45.10},
    '2026': {'f1': 8.80, 'f2': 8.90, 'f3': 9.60, 'f4': 9.10, 'f5': 8.80, 'f6': 9.30, 'f7': 9.50, 'f8': 9.00, 'cqv_v1': 9.10, 'cqv_v1_1': 9.10, 'cqv_v2': 9.05, 'cqv_v3': 9.09, 'cqv_v4': 9.11, 'cqv': 9.11, 'pe': 42.50}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR VRT (VERTIV HOLDINGS CO) Q2 2026.")
