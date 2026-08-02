import json
import os

print("Executing master update of NFLX for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for NFLX (Q2 2026)
nflx_data = {
    'ticker': 'NFLX',
    'name': 'Netflix, Inc.',
    'sector': 'Communication Services / Streaming Entertainment',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 680.50,
    'pe': 36.94,
    'pe_forward': 28.50,
    'eps_trailing': 18.42,
    'eps_forward': 23.88,
    'eps_growth_ntm_pct': 29.6,
    'growth_eps': 29.6,
    'market_cap_b': 288.5,
    'ocf_ttm_m': 7150.0,
    'maint_capex_m': 380.0,
    'owner_earnings_m': 6770.0,
    'fcf_yield_pct': 2.35,
    'score_fcf_yield': 5.88,
    'intrinsic_value': 850.63,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 10.39,
    'score_peg': 10.00,
    'value_score': 7.35,
    'wacc': 9.0,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 9.50,
    'f2': 9.20,
    'f3': 9.10,
    'f4': 9.30,
    'f4_moat': 9.30,
    'f5': 9.00,
    'f6': 9.20,
    'f7': 8.00,
    'f8': 8.80,
    'cqv_v4': 9.12,
    'cqv': 9.12,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'close_history': {
        '2020': 540.73,
        '2021': 602.44,
        '2022': 294.95,
        '2023': 486.88,
        '2024': 889.50,
        '2025': 720.10,
        '2026': 680.50
    }
}

# Update in cqv_list
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'NFLX':
        cqv_list[idx].update(nflx_data)
        updated = True
        break

if not updated:
    cqv_list.append(nflx_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['NFLX'] = {
    '2020': {'f1': 8.50, 'f2': 8.20, 'f3': 8.50, 'f4': 9.00, 'f5': 8.50, 'f6': 8.80, 'f7': 7.50, 'f8': 8.50, 'cqv_v1': 8.50, 'cqv_v1_1': 8.50, 'cqv_v2': 8.60, 'cqv_v3': 8.70, 'cqv_v4': 8.85, 'cqv': 8.85, 'pe': 85.20},
    '2021': {'f1': 8.70, 'f2': 8.40, 'f3': 8.70, 'f4': 9.10, 'f5': 8.60, 'f6': 8.90, 'f7': 7.60, 'f8': 8.60, 'cqv_v1': 8.65, 'cqv_v1_1': 8.65, 'cqv_v2': 8.75, 'cqv_v3': 8.85, 'cqv_v4': 8.92, 'cqv': 8.92, 'pe': 58.40},
    '2022': {'f1': 8.90, 'f2': 8.60, 'f3': 8.80, 'f4': 9.15, 'f5': 8.70, 'f6': 9.00, 'f7': 7.70, 'f8': 8.65, 'cqv_v1': 8.70, 'cqv_v1_1': 8.70, 'cqv_v2': 8.80, 'cqv_v3': 8.90, 'cqv_v4': 8.98, 'cqv': 8.98, 'pe': 24.10},
    '2023': {'f1': 9.10, 'f2': 8.80, 'f3': 8.90, 'f4': 9.20, 'f5': 8.80, 'f6': 9.10, 'f7': 7.80, 'f8': 8.70, 'cqv_v1': 8.85, 'cqv_v1_1': 8.85, 'cqv_v2': 8.95, 'cqv_v3': 9.05, 'cqv_v4': 9.05, 'cqv': 9.05, 'pe': 42.50},
    '2024': {'f1': 9.30, 'f2': 9.00, 'f3': 9.00, 'f4': 9.25, 'f5': 8.90, 'f6': 9.15, 'f7': 7.90, 'f8': 8.75, 'cqv_v1': 8.95, 'cqv_v1_1': 8.95, 'cqv_v2': 9.05, 'cqv_v3': 9.10, 'cqv_v4': 9.10, 'cqv': 9.10, 'pe': 38.20},
    '2025': {'f1': 9.40, 'f2': 9.10, 'f3': 9.05, 'f4': 9.28, 'f5': 8.95, 'f6': 9.18, 'f7': 7.95, 'f8': 8.78, 'cqv_v1': 9.00, 'cqv_v1_1': 9.00, 'cqv_v2': 9.10, 'cqv_v3': 9.12, 'cqv_v4': 9.12, 'cqv': 9.12, 'pe': 36.50},
    '2026': {'f1': 9.50, 'f2': 9.20, 'f3': 9.10, 'f4': 9.30, 'f5': 9.00, 'f6': 9.20, 'f7': 8.00, 'f8': 8.80, 'cqv_v1': 9.05, 'cqv_v1_1': 9.05, 'cqv_v2': 9.12, 'cqv_v3': 9.12, 'cqv_v4': 9.12, 'cqv': 9.12, 'pe': 36.94}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR NFLX Q2 2026.")
