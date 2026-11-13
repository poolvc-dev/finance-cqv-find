import json
import ast
import math
import numpy as np

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

results = []

for item in data:
    ticker = item.get('ticker')
    name = item.get('name')
    sector = item.get('sector')
    cqv = item.get('cqv_v5') or item.get('cqv')
    vs = item.get('value_score')
    cl = item.get('clasificacion', '').strip()
    verdict = item.get('verdict', '').strip()
    f4 = item.get('f4') or item.get('f4_moat')
    
    ch_raw = item.get('close_history')
    ch = {}
    if isinstance(ch_raw, dict):
        ch = ch_raw
    elif isinstance(ch_raw, str):
        try:
            ch = ast.literal_eval(ch_raw)
        except:
            try:
                ch = json.loads(ch_raw.replace("'", '"'))
            except:
                pass
                
    if not isinstance(ch, dict):
        continue
        
    def get_price(key):
        val = ch.get(key)
        if val is None:
            return None
        try:
            val_f = float(val)
            return val_f if val_f > 0 else None
        except:
            return None

    p2020 = get_price('2020')
    p2021 = get_price('2021')
    p2022 = get_price('2022')
    p2024 = get_price('2024')
    p2026 = get_price('2026') or (float(item['price']) if item.get('price') else None)
    
    if cqv and p2020 and p2026 and p2020 > 0 and p2026 > 0:
        # Check for splits or massive outliers if any
        ret_6y = (p2026 / p2020 - 1.0) * 100
        cagr_6y = ((p2026 / p2020) ** (1/6) - 1.0) * 100
        ret_from_2022 = ((p2026 / p2022 - 1.0) * 100) if p2022 and p2022 > 0 else None
        
        results.append({
            'ticker': ticker,
            'name': name,
            'sector': sector,
            'cqv': float(cqv),
            'vs': float(vs) if vs is not None else 0.0,
            'f4': float(f4) if f4 is not None else 0.0,
            'cl': cl,
            'verdict': verdict,
            'p2020': p2020,
            'p2022': p2022,
            'p2026': p2026,
            'ret_6y': ret_6y,
            'cagr_6y': cagr_6y,
            'ret_from_2022': ret_from_2022
        })

print(f'Successfully parsed and analyzed {len(results)} companies with complete 2020-2026 returns.')

# Tiers
tier_suprema = [r for r in results if r['cqv'] >= 9.50]
tier_elite = [r for r in results if 9.00 <= r['cqv'] < 9.50]
tier_alta = [r for r in results if 8.00 <= r['cqv'] < 9.00]
tier_media = [r for r in results if r['cqv'] < 8.00]

print('\n' + '='*80)
print('TABLA 1: DESEMPEÑO EN BOLSA POR TIER CQV v5.0 (2020 - 2026)')
print('='*80)
print(f"{'Tier CQV':<28} | {'N':<4} | {'Mediana Ret':<11} | {'Media Ret':<11} | {'CAGR Med':<9} | {'Tasa >0%':<8} | {'Mult >=100%':<11} | {'Post-2022 Med'}")
print('-'*95)

for name, group in [
    ('ÉLITE SUPREMA (>= 9.50)', tier_suprema),
    ('ÉLITE (9.00 - 9.49)', tier_elite),
    ('ALTA CALIDAD (8.00 - 8.99)', tier_alta),
    ('EN OBSERVACIÓN (< 8.00)', tier_media)
]:
    if not group:
        continue
    rets = [r['ret_6y'] for r in group]
    cagrs = [r['cagr_6y'] for r in group]
    rets_22 = [r['ret_from_2022'] for r in group if r['ret_from_2022'] is not None]
    pos = sum(1 for x in rets if x > 0) / len(rets) * 100
    m100 = sum(1 for x in rets if x >= 100) / len(rets) * 100
    med_22 = f"+{np.median(rets_22):.1f}%" if rets_22 else "N/D"
    print(f"{name:<28} | {len(group):<4} | +{np.median(rets):<10.1f}% | +{np.mean(rets):<10.1f}% | +{np.median(cagrs):<8.1f}% | {pos:<7.1f}% | {m100:<10.1f}% | {med_22}")

# Correlations
def pearson(x, y):
    mx, my = np.mean(x), np.mean(y)
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    den = math.sqrt(sum((xi - mx)**2 for xi in x) * sum((yi - my)**2 for yi in y))
    return num / den if den != 0 else 0

def rank(seq):
    order = sorted(range(len(seq)), key=lambda i: seq[i])
    ranks = [0] * len(seq)
    for r, i in enumerate(order):
        ranks[i] = r
    return ranks

def spearman(x, y):
    return pearson(rank(x), rank(y))

cqvs = [r['cqv'] for r in results]
returns = [r['ret_6y'] for r in results]
f4s = [r['f4'] for r in results]

sp_cqv = spearman(cqvs, returns)
pe_cqv = pearson(cqvs, returns)
sp_moat = spearman(f4s, returns)

print('\n' + '='*80)
print('CORRELACIÓN ESTADÍSTICA (CQV vs RETORNO BURSÁTIL)')
print('='*80)
print(f"Spearman Rank Correlation (CQV Calidad vs Retorno en Bolsa): +{sp_cqv:.4f}")
print(f"Pearson Linear Correlation (CQV Calidad vs Retorno en Bolsa): +{pe_cqv:.4f}")
print(f"Spearman Rank Correlation (F4 MOAT vs Retorno en Bolsa):     +{sp_moat:.4f}")

# Dual Engine: Calidad + Value Score
sweet_spot = [r for r in results if r['cqv'] >= 9.0 and r['vs'] >= 7.0]
fair_quality = [r for r in results if r['cqv'] >= 9.0 and 5.0 <= r['vs'] < 7.0]
expensive_quality = [r for r in results if r['cqv'] >= 9.0 and r['vs'] < 5.0]

print('\n' + '='*80)
print('TABLA 2: EL MOTOR DUAL (CALIDAD CQV >= 9.0 + VALUACIÓN VALUE SCORE)')
print('='*80)
for label, group in [
    ('SWEET SPOT (CQV >= 9.0 + VS >= 7.0 - Comprar/Infravaloradas)', sweet_spot),
    ('CALIDAD JUSTA (CQV >= 9.0 + 5.0 <= VS < 7.0 - Acumular)', fair_quality),
    ('CALIDAD CARA (CQV >= 9.0 + VS < 5.0 - Mantener/Exigentes)', expensive_quality)
]:
    if not group:
        continue
    r_g = [r['ret_6y'] for r in group]
    c_g = [r['cagr_6y'] for r in group]
    pos = sum(1 for x in r_g if x > 0) / len(r_g) * 100
    m100 = sum(1 for x in r_g if x >= 100) / len(r_g) * 100
    print(f"{label} (N={len(group)}):")
    print(f"   Retorno Mediano: +{np.median(r_g):.1f}% | Media: +{np.mean(r_g):.1f}% | CAGR Mediano: +{np.median(c_g):.1f}% | >=+100%: {m100:.1f}%")

# Top individual compounders
top_compounders = sorted(results, key=lambda x: x['ret_6y'], reverse=True)[:10]
print('\n' + '='*80)
print('TOP 10 ACCIONES GANADORAS EN LA BASE DE DATOS')
print('='*80)
for r in top_compounders:
    print(f"{r['ticker']:5} | {r['name'][:25]:25} | CQV: {r['cqv']:.2f} ({r['cl']}) | Retorno 2020-2026: +{r['ret_6y']:.1f}% (CAGR +{r['cagr_6y']:.1f}%) | Sector: {r['sector'][:30]}")
