import json

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_data = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_history = json.load(f)

transitions = []

for c in cqv_data:
    ticker = c.get('ticker')
    name = c.get('name')
    sector = c.get('sector')
    cqv_curr = c.get('cqv') or c.get('cqv_v4')
    verdict = c.get('verdict', '')
    mos = c.get('mos_pct')
    price = c.get('price')
    iv = c.get('intrinsic_value')
    clasif_curr = c.get('clasificacion')
    conf = c.get('data_confidence')

    if not ticker or cqv_curr is None or cqv_curr < 9.00:
        continue

    hist = cqv_history.get(ticker, {})
    
    history_scores = {}
    for yr in ['2020', '2021', '2022', '2023', '2024', '2025', '2026']:
        if yr in hist:
            q_data = hist[yr].get('Q4') or hist[yr].get('Q2') or hist[yr].get('Q1') or hist[yr].get('annual_legacy')
            if q_data:
                sc = q_data.get('cqv_v4') or q_data.get('cqv')
                if sc:
                    history_scores[yr] = sc

    was_solid = any(score < 9.00 for yr, score in history_scores.items() if yr in ['2020', '2021', '2022', '2023', '2024'])

    if was_solid:
        years_sorted = sorted(history_scores.keys())
        first_solid_yr = next((yr for yr in years_sorted if history_scores[yr] < 9.00), None)
        first_solid_sc = history_scores[first_solid_yr] if first_solid_yr else None

        crossed_yr = next((yr for yr in years_sorted if history_scores[yr] >= 9.00), '2026')
        
        delta = round(cqv_curr - (first_solid_sc or 8.50), 2)

        transitions.append({
            'ticker': ticker,
            'name': name,
            'sector': sector,
            'cqv_curr': cqv_curr,
            'clasif_curr': clasif_curr,
            'first_solid_yr': first_solid_yr,
            'first_solid_sc': first_solid_sc,
            'crossed_yr': crossed_yr,
            'delta': delta,
            'price': price,
            'intrinsic_value': iv,
            'mos_pct': mos,
            'verdict': verdict,
            'history': [f"{yr}: {history_scores[yr]}" for yr in years_sorted],
            'is_audited': price != 100.0 or conf == 'Alta'
        })

transitions.sort(key=lambda x: (x['cqv_curr'], x['mos_pct'] if x['mos_pct'] else -999), reverse=True)

print(f"=== EMPRESAS QUE ASCENDIERON DE SOLIDO (< 9.00) A ELITE (>= 9.00): {len(transitions)} ===\n")
for i, t in enumerate(transitions, 1):
    hist_str = " -> ".join(t['history'])
    aud_tag = "[AUDITADO 2026]" if t['is_audited'] else "[BASE]"
    print(f"{i}. [{t['ticker']}] {t['name']} | CQV Actual: {t['cqv_curr']} ({t['clasif_curr']}) {aud_tag}")
    print(f"   Transicion: Ascendio a Elite en {t['crossed_yr']} (Punto de partida: {t['first_solid_sc']} en {t['first_solid_yr']} -> Delta: +{t['delta']})")
    print(f"   Precio: ${t['price']} | Valor Intrinseco: ${t['intrinsic_value']} | MoS: {t['mos_pct']}% | Veredicto: {t['verdict']}")
    print(f"   Historial: {hist_str}\n")
