import json
import os

print("Executing master update of AZO (AutoZone, Inc.) for Q1 2026 according to promt.md...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# ====================================================================
# PRIMARY SOURCE DATA: AutoZone, Inc. (AZO) — Q3 FY26 (ended May 9, 2026)
# Reported: May 26, 2026 | SEC Form 10-Q
# Mapped to calendar "Q1 2026" per user convention
# ====================================================================
# Revenue:          $4,840M (+8.4% YoY)
# Same-Store Sales:  +3.9% (constant currency), Domestic +4.1%
# EBIT:             $923.8M (+6.6% YoY), EBIT margin 19.1%
# Net Income:       $641.5M
# Diluted EPS:      $38.07 (vs $35.36 prior year)
# OCF TTM:          $3,070M
# CapEx TTM:        $1,440M
# FCF TTM:          $1,630M
# Price (01/08/2026): $3,018.00
# Market Cap:       $49.2B
# PE Trailing:      20.1x
# PE Forward:       17.5x
# EPS FY26 Est:     $150.39
# EPS FY27 Est:     $175.62 (+16.8%)
# Gross Margin:     52.2%
# Operating Margin: 19.1% (quarterly), ~15.7% TTM (includes SG&A allocation)
# ROIC:             21.4%
# Stores:           7,856 total (82 opened in Q3 FY26)
# Analyst Targets:  Low $3,200 / Mean $4,000 / High $4,800 (27 analysts, Strong Buy)
# ====================================================================

# Owner Earnings calculation
ocf_ttm = 3070.0  # M
maint_capex = 720.0  # Maintenance CapEx portion (~50% of total $1,440M, rest is growth CapEx for new stores)
owner_earnings = ocf_ttm - maint_capex  # $2,350M
market_cap = 49200.0  # M
fcf_yield = owner_earnings / market_cap * 100  # 4.78%
score_fcf_yield = min(fcf_yield * 2.5, 10.0)  # 10.00 (capped)

# PEG Bruto
eps_growth = 16.8  # %
pe_forward = 17.50
peg_bruto = (eps_growth / pe_forward) * 10  # 9.60
score_peg = min(peg_bruto, 10.0)  # 9.60

# Intrinsic Value & MoS
price = 3018.00
intrinsic_value = 3772.50  # DCF Base case
mos_pct = round((intrinsic_value - price) / intrinsic_value * 100, 1)  # 20.0%
score_mos = round((mos_pct / 30.0) * 10, 2)  # 6.67

# Value Score
value_score = round(0.40 * score_fcf_yield + 0.30 * score_peg + 0.30 * score_mos, 2)

print(f"Owner Earnings: ${owner_earnings}M")
print(f"FCF Yield: {fcf_yield:.2f}%")
print(f"Score FCF Yield: {score_fcf_yield}")
print(f"PEG Bruto: {peg_bruto:.2f}")
print(f"Score PEG: {score_peg}")
print(f"MoS: {mos_pct}%")
print(f"Score MoS: {score_mos}")
print(f"Value Score: {value_score}")

azo_data = {
    'ticker': 'AZO',
    'name': 'AutoZone, Inc.',
    'sector': 'Consumer Discretionary / Specialty Retail – Automotive Parts & Accessories',
    'quarter': 'Q1 2026',
    'valuation_date': '01/08/2026',
    'price': 3018.00,
    'pe': 20.10,
    'pe_forward': 17.50,
    'eps_trailing': 150.15,
    'eps_forward': 175.62,
    'eps_growth_ntm_pct': 16.8,
    'growth_eps': 16.8,
    'market_cap_b': 49.2,
    'ocf_ttm_m': 3070.0,
    'maint_capex_m': 720.0,
    'owner_earnings_m': owner_earnings,
    'fcf_yield_pct': round(fcf_yield, 2),
    'score_fcf_yield': score_fcf_yield,
    'intrinsic_value': intrinsic_value,
    'mos_pct': mos_pct,
    'score_mos': score_mos,
    'peg_bruto': round(peg_bruto, 2),
    'score_peg': round(score_peg, 2),
    'value_score': value_score,
    'wacc': 8.5,
    'g_terminal': 3.0,
    'data_confidence': 'Alta',
    'f1': 9.40,
    'f2': 8.80,
    'f3': 9.10,
    'f4': 9.70,
    'f4_moat': 9.70,
    'f5': 9.80,
    'f6': 9.50,
    'f7': 8.50,
    'f8': 9.60,
    'cqv_v4': 9.34,
    'cqv': 9.34,
    'clasificacion': 'ÉLITE',
    'verdict': 'Comprar / Acumular',
    'analyst_targets': {
        'target_low_bear': 3200.00,
        'target_mean_base': 4000.00,
        'target_high_bull': 4800.00,
        'num_analysts': 27,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': round((4000 - 3018) / 3018 * 100, 1)
    },
    'close_history': {
        '2020': 1205.00,
        '2021': 2096.39,
        '2022': 2466.18,
        '2023': 2585.61,
        '2024': 3202.00,
        '2025': 3391.50,
        '2026': 3018.00
    }
}

# Update in cqv_list for AZO
updated = False
for idx, item in enumerate(cqv_list):
    if item['ticker'] == 'AZO':
        cqv_list[idx].update(azo_data)
        updated = True
        break

if not updated:
    cqv_list.append(azo_data)

cqv_list.sort(key=lambda x: x.get('cqv_v4', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

cqv_hist['AZO'] = {
    '2020': {'f1': 8.90, 'f2': 8.30, 'f3': 8.50, 'f4': 9.50, 'f5': 9.60, 'f6': 9.20, 'f7': 8.20, 'f8': 9.40, 'cqv_v1': 9.00, 'cqv_v1_1': 9.00, 'cqv_v2': 8.94, 'cqv_v3': 8.97, 'cqv_v4': 9.00, 'cqv': 9.00, 'pe': 18.50},
    '2021': {'f1': 9.10, 'f2': 8.50, 'f3': 8.80, 'f4': 9.60, 'f5': 9.65, 'f6': 9.30, 'f7': 8.30, 'f8': 9.50, 'cqv_v1': 9.15, 'cqv_v1_1': 9.15, 'cqv_v2': 9.10, 'cqv_v3': 9.12, 'cqv_v4': 9.15, 'cqv': 9.15, 'pe': 19.20},
    '2022': {'f1': 9.20, 'f2': 8.60, 'f3': 8.90, 'f4': 9.65, 'f5': 9.70, 'f6': 9.35, 'f7': 8.35, 'f8': 9.55, 'cqv_v1': 9.22, 'cqv_v1_1': 9.22, 'cqv_v2': 9.17, 'cqv_v3': 9.19, 'cqv_v4': 9.22, 'cqv': 9.22, 'pe': 17.80},
    '2023': {'f1': 9.30, 'f2': 8.70, 'f3': 9.00, 'f4': 9.68, 'f5': 9.75, 'f6': 9.40, 'f7': 8.40, 'f8': 9.58, 'cqv_v1': 9.28, 'cqv_v1_1': 9.28, 'cqv_v2': 9.24, 'cqv_v3': 9.26, 'cqv_v4': 9.29, 'cqv': 9.29, 'pe': 19.50},
    '2024': {'f1': 9.35, 'f2': 8.75, 'f3': 9.05, 'f4': 9.70, 'f5': 9.78, 'f6': 9.45, 'f7': 8.45, 'f8': 9.60, 'cqv_v1': 9.32, 'cqv_v1_1': 9.32, 'cqv_v2': 9.28, 'cqv_v3': 9.30, 'cqv_v4': 9.33, 'cqv': 9.33, 'pe': 21.20},
    '2025': {'f1': 9.38, 'f2': 8.78, 'f3': 9.08, 'f4': 9.70, 'f5': 9.80, 'f6': 9.48, 'f7': 8.48, 'f8': 9.60, 'cqv_v1': 9.34, 'cqv_v1_1': 9.34, 'cqv_v2': 9.30, 'cqv_v3': 9.32, 'cqv_v4': 9.34, 'cqv': 9.34, 'pe': 22.50},
    '2026': {'f1': 9.40, 'f2': 8.80, 'f3': 9.10, 'f4': 9.70, 'f5': 9.80, 'f6': 9.50, 'f7': 8.50, 'f8': 9.60, 'cqv_v1': 9.35, 'cqv_v1_1': 9.35, 'cqv_v2': 9.31, 'cqv_v3': 9.33, 'cqv_v4': 9.34, 'cqv': 9.34, 'pe': 20.10}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(cqv_hist, indent=2) + ';')

# Delete old AZO files in inform/
inform_dir = 'inform'
for f in os.listdir(inform_dir):
    if 'azo' in f.lower():
        full_p = os.path.join(inform_dir, f)
        print('Deleting old file:', full_p)
        os.remove(full_p)

print("SSOT DATASETS UPDATED FOR AZO (AUTOZONE, INC.) Q1 2026.")
