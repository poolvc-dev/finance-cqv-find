import json

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_data = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_history = json.load(f)

audited_opps = []

for c in cqv_data:
    ticker = c.get('ticker')
    name = c.get('name')
    sector = c.get('sector')
    cqv = c.get('cqv') or c.get('cqv_v4')
    verdict = c.get('verdict', '')
    mos = c.get('mos_pct')
    price = c.get('price')
    iv = c.get('intrinsic_value')
    clasif = c.get('clasificacion')
    conf = c.get('data_confidence')

    if not ticker or cqv is None or cqv < 8.0:
        continue

    # Must be in buy/accumulate opportunity
    is_opp = ('Comprar' in verdict or 'Acumular' in verdict) and (mos is not None and mos >= 12.0)

    if not is_opp:
        continue

    hist = cqv_history.get(ticker, {})
    sc_2020 = (hist.get('2020', {}).get('Q4') or hist.get('2020', {}).get('annual_legacy') or {}).get('cqv_v4') or (hist.get('2020', {}).get('Q4') or {}).get('cqv')
    sc_2026 = cqv

    if sc_2020 and sc_2026 and sc_2026 > sc_2020:
        delta = round(sc_2026 - sc_2020, 2)
        audited_opps.append({
            'ticker': ticker,
            'name': name,
            'sector': sector,
            'cqv': cqv,
            'clasif': clasif,
            'verdict': verdict,
            'price': price,
            'intrinsic_value': iv,
            'mos_pct': mos,
            'sc_2020': sc_2020,
            'sc_2026': sc_2026,
            'delta': delta,
            'is_high_audited': price != 100.0 or conf == 'Alta'
        })

audited_opps.sort(key=lambda x: (x['cqv'], x['mos_pct']), reverse=True)

print(f"=== SELECCION DE ELITE: EMPRESAS MEJORANDO CQV Y EN OPORTUNIDAD DE COMPRA ({len(audited_opps)}) ===\n")
for i, o in enumerate(audited_opps, 1):
    flag = "[AUDITADO 2026]" if o['is_high_audited'] else "[BASE]"
    print(f"{i}. [{o['ticker']}] {o['name']} | CQV: {o['cqv']} ({o['clasif']}) | Delta: +{o['delta']} (2020: {o['sc_2020']} -> 2026: {o['cqv']})")
    print(f"   Precio: ${o['price']} | Valor Intrinseco: ${o['intrinsic_value']} | MoS: {o['mos_pct']}% | Veredicto: {o['verdict']} | {flag}\n")
