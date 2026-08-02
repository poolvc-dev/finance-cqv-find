import json
import os

print("Updating UNH to Q2 2026 (Reported July 16, 2026) in SSOT datasets...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

unh_q2_data = {
    'ticker': 'UNH',
    'name': 'UnitedHealth Group Incorporated',
    'sector': 'Healthcare / Managed Care, Health Insurance & Optum Healthcare Services',
    'quarter': 'Q2 2026',
    'valuation_date': '16/07/2026',
    'price': 505.00,
    'pe': 19.95,
    'pe_forward': 16.55,
    'eps_trailing': 25.29,
    'eps_forward': 30.50,
    'eps_growth_ntm_pct': 20.6,
    'growth_eps': 20.6,
    'market_cap_b': 465.0,
    'ocf_ttm_m': 32000.0,
    'maint_capex_m': 3600.0,
    'owner_earnings_m': 28400.0,
    'fcf_yield_pct': 6.11,
    'score_fcf_yield': 10.00,
    'intrinsic_value': 631.25,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 12.45,
    'score_peg': 10.00,
    'value_score': 9.00,
    'wacc': 8.0,
    'g_terminal': 3.5,
    'data_confidence': 'Alta',
    'f1': 9.32,
    'f2': 9.40,
    'f3': 9.12,
    'f4': 9.60,
    'f4_moat': 9.60,
    'f5': 9.30,
    'f6': 9.40,
    'f7': 8.80,
    'f8': 9.50,
    'cqv_v4': 9.34,
    'cqv': 9.34,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 440.00,
        'target_mean_base': 600.00,
        'target_high_bull': 665.00,
        'num_analysts': 27,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 18.8
    },
    'close_history': {
        '2020': 350.68,
        '2021': 502.14,
        '2022': 530.18,
        '2023': 526.47,
        '2024': 520.00,
        '2025': 465.00,
        '2026': 505.00
    }
}

# Update in cqv_list for UNH
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'UNH':
        cqv_list[idx].update(unh_q2_data)
        updated = True
        break

if not updated:
    cqv_list.append(unh_q2_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['UNH']['2026'] = {
    'f1': 9.32, 'f2': 9.40, 'f3': 9.12, 'f4': 9.60, 'f5': 9.30, 'f6': 9.40, 'f7': 8.80, 'f8': 9.50,
    'cqv_v1': 9.34, 'cqv_v1_1': 9.34, 'cqv_v2': 9.29, 'cqv_v3': 9.32, 'cqv_v4': 9.34, 'cqv': 9.34, 'pe': 19.95
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

# Delete old UNH_2026_Q1.md file
if os.path.exists('inform/UNH_2026_Q1.md'):
    os.remove('inform/UNH_2026_Q1.md')
    print("Deleted old inform/UNH_2026_Q1.md file.")

print("SSOT DATASETS UPDATED FOR UNH (UNITEDHEALTH GROUP) Q2 2026.")
