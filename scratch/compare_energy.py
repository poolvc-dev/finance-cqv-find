import json

with open('cqv_data.json', encoding='utf-8') as f:
    data = json.load(f)

energy_companies = []
for d in data:
    sector = str(d.get('sector', '')).lower()
    name = str(d.get('name', '')).lower()
    ticker = d.get('ticker')
    if any(k in sector or k in name for k in ['energy', 'oil', 'gas', 'petroleum', 'pipeline', 'solar', 'renewable']):
        energy_companies.append(d)

print(f"Total Energy companies found in dataset: {len(energy_companies)}\n")

# Filter for CQV >= 7.50 ("de sólido hacia arriba")
solid_plus = [c for c in energy_companies if (c.get('cqv_v4') or c.get('cqv') or 0) >= 7.50]
solid_plus.sort(key=lambda x: x.get('cqv_v4') or x.get('cqv') or 0, reverse=True)

print(f"Found {len(solid_plus)} Energy companies with CQV >= 7.50:\n")

for c in solid_plus:
    ticker = c.get('ticker')
    name = c.get('name')
    sector = c.get('sector')
    cqv = c.get('cqv_v4') or c.get('cqv')
    clas = c.get('clasificacion')
    vs = c.get('value_score')
    price = c.get('price')
    iv = c.get('intrinsic_value')
    mos = c.get('mos_pct')
    verdict = c.get('verdict')
    f1 = c.get('f1')
    f2 = c.get('f2')
    f3 = c.get('f3')
    f4 = c.get('f4')
    f5 = c.get('f5')
    f6 = c.get('f6')
    f7 = c.get('f7')
    f8 = c.get('f8')
    fcf_yield = c.get('fcf_yield_pct')
    peg = c.get('peg_bruto')
    pe_fwd = c.get('pe_forward')
    
    print(f"=== {ticker}: {name} ===")
    print(f"  Sector: {sector}")
    print(f"  CQV v4.0: {cqv} ({clas})")
    print(f"  Factores: F1={f1}, F2={f2}, F3={f3}, F4={f4}, F5={f5}, F6={f6}, F7={f7}, F8={f8}")
    print(f"  Value Score: {vs} | MoS: {mos}% | FCF Yield: {fcf_yield}% | PEG Bruto: {peg} | PER Fwd: {pe_fwd}x")
    print(f"  Precio: ${price} | Valor Intrínseco: ${iv} | Veredicto: {verdict}")
    print("-" * 60)
