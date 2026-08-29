import json

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_data = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_history = json.load(f)

high_growth_elites = []

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
    eps_growth = c.get('eps_growth_ntm_pct') or c.get('f3') or 0.0

    if not ticker or cqv_curr is None:
        continue

    # Must be in ÉLITE range: 9.00 <= CQV < 9.50
    if 9.00 <= cqv_curr < 9.50:
        hist = cqv_history.get(ticker, {})
        history_scores = {}
        for yr in ['2020', '2021', '2022', '2023', '2024', '2025', '2026']:
            if yr in hist:
                q_data = hist[yr].get('Q4') or hist[yr].get('Q2') or hist[yr].get('Q1') or hist[yr].get('annual_legacy')
                if q_data:
                    sc = q_data.get('cqv_v4') or q_data.get('cqv')
                    if sc:
                        history_scores[yr] = sc

        years_sorted = sorted(history_scores.keys())
        first_sc = history_scores[years_sorted[0]] if years_sorted else cqv_curr

        # Check trajectory upwards
        if cqv_curr > first_sc:
            delta = round(cqv_curr - first_sc, 2)
            dist_to_suprema = round(9.50 - cqv_curr, 2)

            high_growth_elites.append({
                'ticker': ticker,
                'name': name,
                'sector': sector,
                'cqv_curr': cqv_curr,
                'clasif_curr': clasif_curr,
                'first_sc': first_sc,
                'first_yr': years_sorted[0] if years_sorted else '2020',
                'delta': delta,
                'dist_to_suprema': dist_to_suprema,
                'eps_growth': eps_growth,
                'price': price,
                'intrinsic_value': iv,
                'mos_pct': mos,
                'verdict': verdict,
                'history': [f"{yr}: {history_scores[yr]}" for yr in years_sorted],
                'is_audited': price != 100.0 or conf == 'Alta'
            })

# Sort by CQV score and EPS Growth
high_growth_elites.sort(key=lambda x: (x['cqv_curr'], x['delta']), reverse=True)

print(f"=== EMPRESAS ÉLITE EN REAL HIPER-CRECIMIENTO CAMINO A ÉLITE SUPREMA: {len(high_growth_elites)} ===\n")
for i, p in enumerate(high_growth_elites, 1):
    hist_str = " -> ".join(p['history'])
    aud_tag = "[AUDITADO 2026]" if p['is_audited'] else "[BASE]"
    print(f"{i}. [{p['ticker']}] {p['name']} | CQV Actual: {p['cqv_curr']} (Falta: {p['dist_to_suprema']} pts para 9.50) {aud_tag}")
    print(f"   Crecimiento / F3: {p['eps_growth']}% | Trayectoria: {p['first_sc']} ({p['first_yr']}) -> {p['cqv_curr']} (2026) | Delta: +{p['delta']} pts")
    print(f"   Precio: ${p['price']} | Valor Intrínseco: ${p['intrinsic_value']} | MoS: {p['mos_pct']}% | Veredicto: {p['verdict']}")
    print(f"   Historial: {hist_str}\n")
