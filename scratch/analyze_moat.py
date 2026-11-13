import json

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_data = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    history = json.load(f)

print(f'Total companies in cqv_data: {len(cqv_data)}')

high_quality = []

for item in cqv_data:
    ticker = item.get('ticker')
    cl = item.get('clasificacion', '').strip().upper()
    cqv = item.get('cqv_v5') or item.get('cqv') or 0
    f4 = item.get('f4') or item.get('f4_moat') or 0
    
    if cqv >= 8.0 or any(tc in cl for tc in ['ALTA CALIDAD', 'ÉLITE', 'ELITE']):
        high_quality.append((ticker, item.get('name'), cl, cqv, f4, item))

print(f'Total high quality companies: {len(high_quality)}')

moat_gainers = []
for ticker, name, cl, cqv, f4_curr, item in high_quality:
    hist_t = history.get(ticker, {})
    f4_points = []
    for yr in ['2023', '2024', '2025', '2026']:
        yd = hist_t.get(yr, {})
        for p in ['P1', 'P2', 'P3', 'P4']:
            if p in yd and yd[p]:
                val = yd[p].get('f4')
                if val:
                    f4_points.append((f'{yr}-{p}', val))
    
    if f4_points:
        first_f4 = f4_points[0][1]
        last_f4 = f4_points[-1][1]
        delta_f4 = round(last_f4 - first_f4, 3)
        recent_points = [x for x in f4_points if x[0].startswith('2024') or x[0].startswith('2025') or x[0].startswith('2026')]
        delta_recent = round(recent_points[-1][1] - recent_points[0][1], 3) if len(recent_points) >= 2 else 0
        moat_gainers.append({
            'ticker': ticker,
            'name': name,
            'clasificacion': cl,
            'cqv': cqv,
            'f4_curr': f4_curr,
            'first_f4': first_f4,
            'last_f4': last_f4,
            'delta_total': delta_f4,
            'delta_recent': delta_recent,
            'points_count': len(f4_points),
            'sector': item.get('sector')
        })

print('\nTop companies with INCREASING MOAT (delta_recent > 0):')
gainers_filtered = [g for g in moat_gainers if g['delta_recent'] > 0]
gainers_filtered.sort(key=lambda x: (x['delta_recent'], x['f4_curr'], x['cqv']), reverse=True)

for g in gainers_filtered[:40]:
    print(f"{g['ticker']} | {g['name']} | f4: {g['last_f4']} (delta: +{g['delta_recent']}) | CQV: {g['cqv']} | {g['clasificacion']} | Sector: {g['sector']}")

print('\n' + '='*80)
print('COMPANIES WITH HIGHEST ABSOLUTE MOAT (f4 >= 9.7):')
top_absolute_moat = [g for g in moat_gainers if g['f4_curr'] >= 9.7]
top_absolute_moat.sort(key=lambda x: (x['f4_curr'], x['cqv']), reverse=True)
for g in top_absolute_moat[:30]:
    print(f"{g['ticker']} | {g['name']} | f4: {g['f4_curr']} | CQV: {g['cqv']} | {g['clasificacion']} | Sector: {g['sector']}")

