import json

with open('cqv_data.json', encoding='utf-8') as f:
    data = json.load(f)

target_tickers = ['LIN', 'ETN', 'MPWR', 'VRT', 'PWR', 'FSLR', 'TPL', 'VLO', 'CNQ', 'MPC', 'CEG']

records = [d for d in data if d.get('ticker') in target_tickers]
records.sort(key=lambda x: x.get('cqv_v4') or x.get('cqv') or 0, reverse=True)

print(f"{'Ticker':<6} | {'CQV':<5} | {'Class':<14} | {'ValueScore':<10} | {'MoS%':<6} | {'PER Fwd':<8} | {'PEG':<6} | {'FCF Yield':<9} | {'Verdict'}")
print("-" * 95)
for r in records:
    cqv = r.get('cqv_v4') or r.get('cqv')
    vs = r.get('value_score')
    mos = r.get('mos_pct')
    pe_fwd = r.get('pe_forward')
    peg = r.get('peg_bruto')
    fcf_y = r.get('fcf_yield_pct')
    print(f"{r.get('ticker'):<6} | {cqv:<5} | {r.get('clasificacion','N/D'):<14} | {str(vs):<10} | {str(mos):<6} | {str(pe_fwd):<8} | {str(peg):<6} | {str(fcf_y):<9} | {r.get('verdict')}")

print("\n=== Detailed Factor Breakdown (F1-F8) ===")
for r in records:
    print(f"\n{r.get('ticker')} - {r.get('name')} ({r.get('sector')})")
    print(f"  F1 (Rentabilidad):  {r.get('f1')} | F2 (Solidez):     {r.get('f2')} | F3 (Crecimiento): {r.get('f3')} | F4 (Moat): {r.get('f4')}")
    print(f"  F5 (Asig. Capital): {r.get('f5')} | F6 (Dirección):   {r.get('f6')} | F7 (Opcionalidad):{r.get('f7')} | F8 (Antifragilidad): {r.get('f8')}")
    print(f"  Price: ${r.get('price')} | IV: ${r.get('intrinsic_value')} | MoS: {r.get('mos_pct')}% | MarketCap: ${r.get('market_cap_b') or (r.get('market_cap')/1000 if r.get('market_cap') else 'N/D')}B")
