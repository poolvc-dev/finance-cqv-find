import json
import os

print("Executing master update of LIN (Linde plc) for Q2 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Primary Source Audited Financial Data for LIN (Linde plc - Q2 2026)
lin_data = {
    'ticker': 'LIN',
    'name': 'Linde plc',
    'sector': 'Materials / Industrial Gases & Engineering',
    'quarter': 'Q2 2026',
    'valuation_date': '29/07/2026',
    'price': 455.00,
    'pe': 31.20,
    'pe_forward': 26.50,
    'eps_trailing': 14.58,
    'eps_forward': 17.17,
    'eps_growth_ntm_pct': 17.8,
    'growth_eps': 17.8,
    'market_cap_b': 215.0,
    'ocf_ttm_m': 9850.0,
    'maint_capex_m': 3650.0,
    'owner_earnings_m': 6200.0,
    'fcf_yield_pct': 2.88,
    'score_fcf_yield': 7.20,
    'intrinsic_value': 568.75,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 6.72,
    'score_peg': 6.72,
    'value_score': 6.90,
    'wacc': 8.0,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 9.50,
    'f2': 9.40,
    'f3': 9.10,
    'f4': 9.80,
    'f4_moat': 9.80,
    'f5': 9.60,
    'f6': 9.60,
    'f7': 9.00,
    'f8': 9.70,
    'cqv_v4': 9.50,
    'cqv': 9.50,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 400.00,
        'target_mean_base': 520.00,
        'target_high_bull': 580.00,
        'num_analysts': 28,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 14.3
    },
    'close_history': {
        '2020': 263.51,
        '2021': 346.43,
        '2022': 326.18,
        '2023': 410.71,
        '2024': 442.20,
        '2025': 430.50,
        '2026': 455.00
    }
}

# Update in cqv_list for LIN if present
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'LIN':
        cqv_list[idx].update(lin_data)
        updated = True
        break

if not updated:
    cqv_list.append(lin_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['LIN'] = {
    '2020': {'f1': 9.20, 'f2': 9.10, 'f3': 8.80, 'f4': 9.75, 'f5': 9.30, 'f6': 9.40, 'f7': 8.60, 'f8': 9.60, 'cqv_v1': 9.25, 'cqv_v1_1': 9.25, 'cqv_v2': 9.18, 'cqv_v3': 9.22, 'cqv_v4': 9.26, 'cqv': 9.26, 'pe': 32.50},
    '2021': {'f1': 9.35, 'f2': 9.25, 'f3': 8.95, 'f4': 9.78, 'f5': 9.45, 'f6': 9.50, 'f7': 8.80, 'f8': 9.65, 'cqv_v1': 9.38, 'cqv_v1_1': 9.38, 'cqv_v2': 9.32, 'cqv_v3': 9.36, 'cqv_v4': 9.39, 'cqv': 9.39, 'pe': 36.80},
    '2022': {'f1': 9.38, 'f2': 9.28, 'f3': 8.98, 'f4': 9.78, 'f5': 9.48, 'f6': 9.50, 'f7': 8.85, 'f8': 9.65, 'cqv_v1': 9.40, 'cqv_v1_1': 9.40, 'cqv_v2': 9.34, 'cqv_v3': 9.38, 'cqv_v4': 9.41, 'cqv': 9.41, 'pe': 28.50},
    '2023': {'f1': 9.42, 'f2': 9.32, 'f3': 9.02, 'f4': 9.80, 'f5': 9.52, 'f6': 9.55, 'f7': 8.90, 'f8': 9.68, 'cqv_v1': 9.44, 'cqv_v1_1': 9.44, 'cqv_v2': 9.38, 'cqv_v3': 9.42, 'cqv_v4': 9.45, 'cqv': 9.45, 'pe': 33.20},
    '2024': {'f1': 9.46, 'f2': 9.35, 'f3': 9.05, 'f4': 9.80, 'f5': 9.55, 'f6': 9.58, 'f7': 8.95, 'f8': 9.68, 'cqv_v1': 9.46, 'cqv_v1_1': 9.46, 'cqv_v2': 9.40, 'cqv_v3': 9.44, 'cqv_v4': 9.47, 'cqv': 9.47, 'pe': 34.50},
    '2025': {'f1': 9.48, 'f2': 9.38, 'f3': 9.08, 'f4': 9.80, 'f5': 9.58, 'f6': 9.60, 'f7': 8.98, 'f8': 9.70, 'cqv_v1': 9.48, 'cqv_v1_1': 9.48, 'cqv_v2': 9.42, 'cqv_v3': 9.46, 'cqv_v4': 9.49, 'cqv': 9.49, 'pe': 31.80},
    '2026': {'f1': 9.50, 'f2': 9.40, 'f3': 9.10, 'f4': 9.80, 'f5': 9.60, 'f6': 9.60, 'f7': 9.00, 'f8': 9.70, 'cqv_v1': 9.49, 'cqv_v1_1': 9.49, 'cqv_v2': 9.43, 'cqv_v3': 9.47, 'cqv_v4': 9.50, 'cqv': 9.50, 'pe': 31.20}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

print("SSOT DATASETS UPDATED FOR LIN (LINDE PLC) Q2 2026.")
