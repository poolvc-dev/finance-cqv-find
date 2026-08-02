import json
import os

print("Updating Broadcom (AVGO) to Q2 2026 (Reported June 12, 2026) in SSOT datasets...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

avgo_q2_data = {
    'ticker': 'AVGO',
    'name': 'Broadcom Inc.',
    'sector': 'Technology / Custom AI Accelerators, Networking Semiconductors & Enterprise Software',
    'quarter': 'Q2 2026',
    'valuation_date': '12/06/2026',
    'price': 178.00,
    'pe': 35.45,
    'pe_forward': 26.37,
    'eps_trailing': 5.02,
    'eps_forward': 6.75,
    'eps_growth_ntm_pct': 34.5,
    'growth_eps': 34.5,
    'market_cap_b': 833.0,
    'ocf_ttm_m': 23400.0,
    'maint_capex_m': 1600.0,
    'owner_earnings_m': 21800.0,
    'fcf_yield_pct': 2.62,
    'score_fcf_yield': 6.55,
    'intrinsic_value': 222.50,
    'mos_pct': 20.0,
    'score_mos': 6.67,
    'peg_bruto': 13.08,
    'score_peg': 10.00,
    'value_score': 7.62,
    'wacc': 8.0,
    'g_terminal': 3.5,
    'data_confidence': 'Alta',
    'f1': 9.60,
    'f2': 9.50,
    'f3': 9.50,
    'f4': 9.80,
    'f4_moat': 9.80,
    'f5': 9.50,
    'f6': 9.60,
    'f7': 9.40,
    'f8': 9.60,
    'cqv_v4': 9.58,
    'cqv': 9.58,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 150.00,
        'target_mean_base': 210.00,
        'target_high_bull': 245.00,
        'num_analysts': 40,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 18.0
    },
    'close_history': {
        '2020': 43.78,
        '2021': 66.54,
        '2022': 55.91,
        '2023': 111.63,
        '2024': 165.00,
        '2025': 155.00,
        '2026': 178.00
    }
}

# Update in cqv_list for AVGO
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'AVGO':
        cqv_list[idx].update(avgo_q2_data)
        updated = True
        break

if not updated:
    cqv_list.append(avgo_q2_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['AVGO']['2026'] = {
    'f1': 9.60, 'f2': 9.50, 'f3': 9.50, 'f4': 9.80, 'f5': 9.50, 'f6': 9.60, 'f7': 9.40, 'f8': 9.60,
    'cqv_v1': 9.58, 'cqv_v1_1': 9.58, 'cqv_v2': 9.54, 'cqv_v3': 9.56, 'cqv_v4': 9.58, 'cqv': 9.58, 'pe': 35.45
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

# Delete old AVGO files in inform/
inform_dir = 'inform'
for f in os.listdir(inform_dir):
    if 'avgo' in f.lower():
        full_p = os.path.join(inform_dir, f)
        print('Deleting old file:', full_p)
        os.remove(full_p)

print("SSOT DATASETS UPDATED FOR AVGO (BROADCOM INC.) Q2 2026.")
