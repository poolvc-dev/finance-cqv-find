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
            for q in ['P1', 'P2', 'P3', 'P4']:
                if q in yr_data and yr_data[q] and isinstance(yr_data[q], dict):
                    score = yr_data[q].get('cqv_v5') or yr_data[q].get('cqv')
                    clas = yr_data[q].get('clasificacion', '')
                    if score is not None:
                        timeline.append((f"{yr} {q}", float(score), str(clas), yr_data[q]))
    
    if not timeline:
        continue
    
    # Check if ever ELITE (score >= 9.00)
    has_been_elite = any(s >= 9.00 or 'ÉLITE' in str(c).upper() or 'ELITE' in str(c).upper() for _, s, c, _ in timeline)
    
    if has_been_elite:
        scores = [s for _, s, _, _ in timeline]
        max_score = max(scores)
        max_idx = scores.index(max_score)
        latest_score = scores[-1]
        diff_from_peak = latest_score - max_score
        
        # Check if there is a deterioration from peak (e.g. >= 0.10 drop) or general declining trend
        if diff_from_peak <= -0.05 or scores[0] > latest_score:
            # Also get factors comparison (peak vs latest)
            peak_item = timeline[max_idx][3]
            latest_item = timeline[-1][3]
            
            f_changes = {}
            for f_key in ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8']:
                val_peak = peak_item.get(f_key)
                val_latest = latest_item.get(f_key)
                if val_peak is not None and val_latest is not None:
                    f_changes[f_key] = round(val_latest - val_peak, 2)
            
            deteriorating_elite.append({
                'ticker': ticker,
                'name': latest_item.get('name') or current_map.get(ticker, {}).get('name') or ticker,
                'sector': latest_item.get('sector') or current_map.get(ticker, {}).get('sector') or 'N/D',
                'max_score': max_score,
                'max_period': timeline[max_idx][0],
                'latest_score': latest_score,
                'latest_period': timeline[-1][0],
                'diff_from_peak': round(diff_from_peak, 2),
                'timeline': [(t, s) for t, s, _, _ in timeline],
                'f_changes': f_changes,
                'latest_details': current_map.get(ticker, {})
            })

deteriorating_elite.sort(key=lambda x: x['diff_from_peak'])

print(f"Total deteriorating elite companies found: {len(deteriorating_elite)}\n")
for item in deteriorating_elite[:30]:
    print(f"Ticker: {item['ticker']:<6} | Peak: {item['max_score']:.2f} ({item['max_period']}) -> Latest: {item['latest_score']:.2f} ({item['latest_period']}) | Change: {item['diff_from_peak']:+.2f}")
    print(f"  Name: {item['name']} | Sector: {item['sector']}")
    print(f"  Factor Changes: {item['f_changes']}")
    print("-" * 80)
