import json

history = json.load(open('cqv_history.json', encoding='utf-8'))
data_list = json.load(open('cqv_data.json', encoding='utf-8'))

current_map = {x['ticker']: x for x in data_list if 'ticker' in x}

deteriorating_elite = []

for ticker, years in history.items():
    if not isinstance(years, dict):
        continue
    
    timeline = []
    for yr in sorted(years.keys()):
        yr_data = years[yr]
        if isinstance(yr_data, dict):
            for q in ['P1', 'P2', 'P3', 'P4', 'annual_legacy']:
                if q in yr_data and yr_data[q] and isinstance(yr_data[q], dict):
                    score = yr_data[q].get('cqv_v5') or yr_data[q].get('cqv')
                    clas = yr_data[q].get('clasificacion', '')
                    pe = yr_data[q].get('pe')
                    val_score = yr_data[q].get('value_score')
                    if score is not None:
                        timeline.append((f"{yr}_{q}", float(score), str(clas), pe, val_score, yr_data[q]))
    
    if not timeline:
        continue
    
    scores = [s for _, s, _, _, _, _ in timeline]
    max_score = max(scores)
    
    if max_score >= 8.80:
        max_idx = scores.index(max_score)
        min_after_max = min(scores[max_idx:])
        min_idx = scores.index(min_after_max, max_idx)
        latest_score = scores[-1]
        
        diff_from_peak = latest_score - max_score
        
        deteriorating_elite.append({
            'ticker': ticker,
            'name': timeline[-1][5].get('name') or current_map.get(ticker, {}).get('name') or ticker,
            'sector': timeline[-1][5].get('sector') or current_map.get(ticker, {}).get('sector') or 'N/D',
            'max_score': max_score,
            'max_period': timeline[max_idx][0],
            'min_score': min_after_max,
            'min_period': timeline[min_idx][0],
            'latest_score': latest_score,
            'latest_period': timeline[-1][0],
            'diff_from_peak': round(diff_from_peak, 2),
            'timeline': [(t, s, pe, vs) for t, s, _, pe, vs, _ in timeline],
            'peak_item': timeline[max_idx][5],
            'latest_item': timeline[-1][5],
        })

deteriorating_elite.sort(key=lambda x: x['diff_from_peak'])

print(f"Total analyzed companies with peak >= 8.80: {len(deteriorating_elite)}\n")
for item in deteriorating_elite:
    if item['diff_from_peak'] <= -0.05 or (item['max_score'] - item['latest_score']) >= 0.05:
        print(f"Ticker: {item['ticker']:<6} | Peak: {item['max_score']:.2f} ({item['max_period']}) -> Latest: {item['latest_score']:.2f} ({item['latest_period']}) | Drop: {item['diff_from_peak']:.2f}")
        print(f"  Name: {item['name']} | Sector: {item['sector']}")
        t_str = " -> ".join([f"{t}:{s:.2f}" for t, s, _, _ in item['timeline'] if 'annual' not in t and ('P2' in t or 'P4' in t)])
        print(f"  Timeline summary: {t_str}")
        print("-" * 80)
