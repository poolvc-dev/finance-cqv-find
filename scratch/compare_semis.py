import json

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_data = json.load(f)

tickers_semi_pure = ['NVDA', 'AVGO', 'ASML', 'AMAT', 'MPWR', 'TSM', 'LRCX', 'KLAC']
tickers_adjacent = ['ANET', 'VRT', 'FN', 'FLEX', 'FIX', 'PWR', 'PLTR', 'RS', 'WTS']

all_selected = tickers_semi_pure + tickers_adjacent
items = {x['ticker']: x for x in cqv_data if x['ticker'] in all_selected}

print('=== PURE SEMICONDUCTOR & EQUIPMENT METRICS ===')
for t in tickers_semi_pure:
    d = items[t]
    cqv = d.get('cqv_v5') or d.get('cqv') or 0
    vs = d.get('value_score') or 0
    f4 = d.get('f4') or d.get('f4_moat') or 0
    pe_fwd = d.get('pe_forward') or 0
    growth = d.get('eps_growth_ntm_pct') or 0
    mos = d.get('mos_pct') or d.get('mos_base_pct') or 0
    fcf_y = d.get('fcf_yield_pct') or 0
    verdict = d.get('verdict') or ''
    cl = d.get('clasificacion') or ''
    print(f"{t:5} | CQV: {cqv:4.2f} ({cl:13}) | Moat: {f4:4.2f} | VS: {vs:4.2f} | Growth: {growth:4.1f}% | PE_Fwd: {pe_fwd:5.2f} | MoS: {mos:5.2f}% | FCF_Y: {fcf_y:4.2f}% | {verdict}")

print('\n=== ADJACENT & INFRASTRUCTURE METRICS ===')
for t in tickers_adjacent:
    d = items[t]
    cqv = d.get('cqv_v5') or d.get('cqv') or 0
    vs = d.get('value_score') or 0
    f4 = d.get('f4') or d.get('f4_moat') or 0
    pe_fwd = d.get('pe_forward') or 0
    growth = d.get('eps_growth_ntm_pct') or 0
    mos = d.get('mos_pct') or d.get('mos_base_pct') or 0
    fcf_y = d.get('fcf_yield_pct') or 0
    verdict = d.get('verdict') or ''
    cl = d.get('clasificacion') or ''
    print(f"{t:5} | CQV: {cqv:4.2f} ({cl:13}) | Moat: {f4:4.2f} | VS: {vs:4.2f} | Growth: {growth:4.1f}% | PE_Fwd: {pe_fwd:5.2f} | MoS: {mos:5.2f}% | FCF_Y: {fcf_y:4.2f}% | {verdict}")

