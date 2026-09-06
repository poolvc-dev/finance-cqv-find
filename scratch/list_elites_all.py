import json

data = json.load(open('cqv_data.json', encoding='utf-8'))
history = json.load(open('cqv_history.json', encoding='utf-8'))

elites = [x for x in data if (x.get('cqv_v5') or x.get('cqv') or 0) >= 9.00]

print(f"Total Current Elite companies in cqv_data.json: {len(elites)}\n")

for item in sorted(elites, key=lambda x: x.get('cqv_v5') or 0, reverse=True):
    t = item.get('ticker')
    name = item.get('name')
    cqv = item.get('cqv_v5') or item.get('cqv')
    vs = item.get('value_score')
    pe = item.get('pe')
    pe_f = item.get('pe_forward')
    growth = item.get('eps_growth_ntm_pct') or item.get('growth_eps')
    mos = item.get('mos_pct')
    
    # check history trends
    h = history.get(t, {})
    hist_str = []
    if isinstance(h, dict):
        for yr in ['2020', '2022', '2024', '2025', '2026']:
            if yr in h and isinstance(h[yr], dict):
                p2 = h[yr].get('P2') or h[yr].get('P4') or h[yr].get('annual_legacy')
                if p2 and isinstance(p2, dict):
                    sc = p2.get('cqv_v5') or p2.get('cqv')
                    if sc:
                        hist_str.append(f"{yr}:{sc:.2f}")
    
    print(f"{t:<6} | CQV: {cqv:.2f} | VS: {vs} | PER_T: {pe} | PER_F: {pe_f} | Growth: {growth}% | History: {' -> '.join(hist_str)}")
