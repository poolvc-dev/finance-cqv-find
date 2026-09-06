import json

data = json.load(open('cqv_data.json', encoding='utf-8'))

opportunities = []

for item in data:
    ticker = item.get('ticker')
    if not ticker:
        continue
    cqv = item.get('cqv_v5') or item.get('cqv') or 0
    vs = item.get('value_score') or 0
    clas = item.get('clasificacion', '')
    
    if cqv >= 9.00 and vs >= 7.00:
        opportunities.append({
            'ticker': ticker,
            'name': item.get('name', ticker),
            'sector': item.get('sector', 'N/D'),
            'cqv': cqv,
            'clasificacion': 'ÉLITE SUPREMA' if cqv >= 9.50 else 'ÉLITE',
            'value_score': vs,
            'price': item.get('price'),
            'intrinsic_value': item.get('intrinsic_value'),
            'intrinsic_value_expected': item.get('intrinsic_value_expected') or item.get('intrinsic_value'),
            'mos_pct': item.get('mos_pct'),
            'mos_esperado_pct': item.get('mos_esperado_pct') or item.get('mos_pct'),
            'pe': item.get('pe'),
            'pe_forward': item.get('pe_forward'),
            'eps_growth': item.get('eps_growth_ntm_pct') or item.get('growth_eps'),
            'peg_bruto': item.get('score_crecimiento_multiplo_bruto') or item.get('peg_bruto'),
            'verdict': item.get('verdict'),
            'f1': item.get('f1'),
            'f2': item.get('f2'),
            'f3': item.get('f3'),
            'f4': item.get('f4'),
            'f5': item.get('f5'),
            'f6': item.get('f6'),
            'f7': item.get('f7'),
            'f8': item.get('f8')
        })

opportunities.sort(key=lambda x: (x['cqv'], x['value_score']), reverse=True)

print(f"Total Élite opportunities with Value Score >= 7.00: {len(opportunities)}\n")

for o in opportunities:
    print(f"[{o['clasificacion']}] {o['ticker']:<6} | {o['name']} | Sector: {o['sector']}")
    print(f"  CQV: {o['cqv']:.2f} | Value Score: {o['value_score']:.2f} | MoS Esperado: {o['mos_esperado_pct']}%")
    print(f"  Price: ${o['price']} | Intrinsic Expected: ${o['intrinsic_value_expected']} | Intrinsic Base: ${o['intrinsic_value']}")
    print(f"  PER Trailing: {o['pe']}x | PER Forward: {o['pe_forward']}x | EPS Growth NTM: {o['eps_growth']}%")
    print(f"  Verdict: {o['verdict']}")
    print("-" * 80)
