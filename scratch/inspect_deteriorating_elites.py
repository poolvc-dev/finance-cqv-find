import json

data_list = json.load(open('cqv_data.json', encoding='utf-8'))
history = json.load(open('cqv_history.json', encoding='utf-8'))

print("--- ANALYZING ALL ELITE COMPANIES FOR DETERIORATION ---")

results = []

for item in data_list:
    ticker = item.get('ticker')
    if not ticker:
        continue
    cqv = item.get('cqv_v5') or item.get('cqv')
    clas = item.get('clasificacion', '')
    
    # Check history for this ticker
    h = history.get(ticker, {})
    if not isinstance(h, dict):
        continue
    
    # Extract chronological scores
    timeline = []
    for yr in ['2020', '2021', '2022', '2023', '2024', '2025', '2026']:
        if yr in h and isinstance(h[yr], dict):
            for q in ['P1', 'P2', 'P3', 'P4']:
                if q in h[yr] and h[yr][q] and isinstance(h[yr][q], dict):
                    sc = h[yr][q].get('cqv_v5') or h[yr][q].get('cqv')
                    if sc:
                        timeline.append((f"{yr} {q}", float(sc), h[yr][q]))
    
    if not timeline:
        continue
    
    # Check if ever ELITE (>= 9.00)
    max_sc = max(t[1] for t in timeline)
    if max_sc >= 9.00:
        latest_sc = timeline[-1][1]
        drop = latest_sc - max_sc
        
        # Factors at peak vs latest
        peak_item = [t[2] for t in timeline if t[1] == max_sc][0]
        latest_item = timeline[-1][2]
        
        f_diff = {}
        for f in ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8']:
            p_val = peak_item.get(f)
            l_val = latest_item.get(f)
            if p_val is not None and l_val is not None:
                f_diff[f] = round(l_val - p_val, 2)
        
        results.append({
            'ticker': ticker,
            'name': item.get('name', ticker),
            'sector': item.get('sector', 'N/D'),
            'cqv_current': cqv,
            'max_sc': max_sc,
            'drop': round(drop, 2),
            'f_diff': f_diff,
            'pe': item.get('pe'),
            'pe_forward': item.get('pe_forward'),
            'value_score': item.get('value_score'),
            'timeline': [(t[0], t[1]) for t in timeline]
        })

results.sort(key=lambda x: (x['drop'], x['cqv_current']))

print(f"Total Elite companies: {len(results)}")
print("\nTop deteriorating Elite companies:")
for r in results[:25]:
    print(f"Ticker: {r['ticker']:<6} | Current CQV: {r['cqv_current']} | Peak: {r['max_sc']} | Drop: {r['drop']} | ValScore: {r['value_score']}")
    print(f"  Name: {r['name']} | Sector: {r['sector']}")
    print(f"  Factor Changes: {r['f_diff']}")
    # print timeline
    t_str = " -> ".join([f"{t}:{s:.2f}" for t, s in r['timeline'][-6:]])
    print(f"  Recent timeline: {t_str}")
    print("-" * 80)
