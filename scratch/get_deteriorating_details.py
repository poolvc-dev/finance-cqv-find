import json

data = json.load(open('cqv_data.json', encoding='utf-8'))
history = json.load(open('cqv_history.json', encoding='utf-8'))

target_tickers = ['COST', 'CDNS', 'AAPL', 'ISRG', 'ANET', 'FICO', 'ASML', 'GOOGL', 'META', 'LOTB']

for item in data:
    t = item.get('ticker')
    if t in target_tickers:
        print(f"=== {t}: {item.get('name')} ===")
        print(f"Sector: {item.get('sector')}")
        print(f"CQV Quality: {item.get('cqv_v5') or item.get('cqv')} | Value Score: {item.get('value_score')}")
        print(f"PER Trailing: {item.get('pe')} | PER Forward: {item.get('pe_forward')}")
        print(f"EPS Growth NTM: {item.get('eps_growth_ntm_pct') or item.get('growth_eps')}%")
        print(f"Price: ${item.get('price')} | Intrinsic Value: ${item.get('intrinsic_value')} | MoS: {item.get('mos_pct')}%")
        print(f"Factors: F1={item.get('f1')}, F2={item.get('f2')}, F3={item.get('f3')}, F4={item.get('f4')}, F5={item.get('f5')}, F6={item.get('f6')}, F7={item.get('f7')}, F8={item.get('f8')}")
        
        # History
        h = history.get(t, {})
        if isinstance(h, dict):
            timeline = []
            for yr in sorted(h.keys()):
                if isinstance(h[yr], dict):
                    for q in ['P1', 'P2', 'P3', 'P4']:
                        if q in h[yr] and h[yr][q] and isinstance(h[yr][q], dict):
                            sc = h[yr][q].get('cqv_v5') or h[yr][q].get('cqv')
                            vs = h[yr][q].get('value_score')
                            if sc:
                                timeline.append(f"{yr}_{q}: CQV={sc:.2f}, VS={vs}")
            print(f"History sample (last 6): {timeline[-6:]}")
        print("="*60 + "\n")
