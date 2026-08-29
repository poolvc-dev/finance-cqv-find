import json

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_data = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_history = json.load(f)

deteriorating = []

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

    if not ticker or cqv_curr is None:
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

    # Must be or have been Elite (>= 8.80) at some point
    max_hist_sc = max(history_scores.values()) if history_scores else cqv_curr

    if max_hist_sc >= 8.80:
        years_sorted = sorted(history_scores.keys())
        first_yr = years_sorted[0] if years_sorted else '2020'
        first_sc = history_scores.get(first_yr, cqv_curr)
        
        # Check peak score and current score
        peak_sc = max(history_scores.values()) if history_scores else cqv_curr
        peak_yr = next((y for y in years_sorted if history_scores[y] == peak_sc), first_yr)

        # Check if score dropped from peak or dropped from first_sc
        if cqv_curr < peak_sc - 0.05 or cqv_curr < first_sc - 0.05:
            delta_peak = round(cqv_curr - peak_sc, 2)
            deteriorating.append({
                'ticker': ticker,
                'name': name,
                'sector': sector,
                'cqv_curr': cqv_curr,
                'clasif_curr': clasif_curr,
                'peak_yr': peak_yr,
                'peak_sc': peak_sc,
                'first_sc': first_sc,
                'delta_peak': delta_peak,
                'price': price,
                'intrinsic_value': iv,
                'mos_pct': mos,
                'verdict': verdict,
                'history': [f"{yr}: {history_scores[yr]}" for yr in years_sorted],
                'is_audited': price != 100.0 or conf == 'Alta'
            })

deteriorating.sort(key=lambda x: x['delta_peak'])

print(f"=== EMPRESAS ÉLITE / ALTA CALIDAD EN DETERIORO O CAÍDA DE CQV: {len(deteriorating)} ===\n")
for i, d in enumerate(deteriorating, 1):
    hist_str = " -> ".join(d['history'])
    aud_tag = "[AUDITADO 2026]" if d['is_audited'] else "[BASE]"
    print(f"{i}. [{d['ticker']}] {d['name']} | CQV Actual: {d['cqv_curr']} ({d['clasif_curr']}) {aud_tag}")
    print(f"   Deterioro: Caída de {d['peak_sc']} (Pico en {d['peak_yr']}) a {d['cqv_curr']} (Caída: {d['delta_peak']} pts)")
    print(f"   Precio: ${d['price']} | Valor Intrínseco: ${d['intrinsic_value']} | MoS: {d['mos_pct']}% | Veredicto: {d['verdict']}")
    print(f"   Historial: {hist_str}\n")
