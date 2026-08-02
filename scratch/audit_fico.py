import json
import os
import re

print("==========================================================================")
print("       AUDIT EN PROFUNDIDAD DE INFORME FICO_2026_Q2.MD VS SSOT & METODO v4.0")
print("==========================================================================")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_data = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

with open('inform/fico_2026_q2.md', 'r', encoding='utf-8') as f:
    report = f.read()

fico_json = [x for x in cqv_data if x['ticker'] == 'FICO'][0]
fico_history = cqv_hist.get('FICO', {})

print("\n--- 1. DATOS DE FICO EN SSOT (cqv_data.json) ---")
print(f"Ticker:                 {fico_json.get('ticker')}")
print(f"Name:                   {fico_json.get('name')}")
print(f"Quarter:                {fico_json.get('quarter')}")
print(f"Precio Actual ($):      ${fico_json.get('price')}")
print(f"PER Trailing:           {fico_json.get('pe')}x")
print(f"PER Forward:            {fico_json.get('pe_forward')}x")
print(f"EPS Growth NTM (%):     {fico_json.get('eps_growth_ntm_pct')}%")
print(f"Owner Earnings ($M):    ${fico_json.get('owner_earnings_m')}M")
print(f"Market Cap ($B):        ${fico_json.get('market_cap_b')}B")
print(f"Valor Intrínseco ($):   ${fico_json.get('intrinsic_value')}")
print(f"Margen de Seguridad (%): {fico_json.get('mos_pct')}%")
print(f"CQV Calidad v4.0:       {fico_json.get('cqv_v4')} / 10")
print(f"Value Score:            {fico_json.get('value_score')} / 10")
print(f"PEG Bruto:              {fico_json.get('peg_bruto')}")
print(f"Score PEG:              {fico_json.get('score_peg')} / 10")
print(f"Score FCF Yield:        {fico_json.get('score_fcf_yield')} / 10")
print(f"Score MoS:              {fico_json.get('score_mos')} / 10")
print(f"Veredicto:              {fico_json.get('verdict')}")

print("\n--- 2. DESGLOSE F1-F8 EN SSOT VS METODO v4.0 ---")
f_weights = {'f1': 0.20, 'f2': 0.15, 'f3': 0.15, 'f4': 0.15, 'f5': 0.10, 'f6': 0.10, 'f7': 0.05, 'f8': 0.10}
f_values = {k: fico_json[k] for k in f_weights if k in fico_json}
calc_cqv = sum(fico_json[k] * f_weights[k] for k in f_weights)
print("Factores individuales:")
for k, v in f_values.items():
    print(f"  {k.upper()}: {v:.2f} (peso {f_weights[k]*100:.0f}%) -> contribución = {v * f_weights[k]:.4f}")
print(f"SUMA PONDERADA CALCULADA (CQV v4.0): {calc_cqv:.4f} -> Redondeado: {calc_cqv:.2f}")

print("\n--- 3. VERIFICACIÓN MATEMÁTICA DE LA CAPA DE VALORACIÓN (VALUE SCORE) ---")
price = fico_json['price']
mcap_m = fico_json.get('market_cap_b', 33.7) * 1000.0
oe_m = fico_json.get('owner_earnings_m', 616.7)
fcf_yield_pct = (oe_m / mcap_m) * 100.0
score_fcf = min(10.0, fcf_yield_pct * 2.5)

eps_growth = fico_json['eps_growth_ntm_pct']
pe_fwd = fico_json['pe_forward']
peg_bruto = (eps_growth / pe_fwd) * 10.0
score_peg = min(10.0, max(0.0, peg_bruto))

iv = fico_json['intrinsic_value']
mos_pct = ((iv - price) / iv) * 100.0
score_mos = min(10.0, max(0.0, (mos_pct / 30.0) * 10.0))

value_score_calc = (0.40 * score_fcf) + (0.30 * score_peg) + (0.30 * score_mos)

print(f"Owner Earnings:        ${oe_m}M")
print(f"Market Cap:            ${mcap_m}M (${fico_json.get('market_cap_b')}B)")
print(f"FCF Yield Calculado:   {fcf_yield_pct:.2f}% | Score FCF Yield: {score_fcf:.2f}/10")
print(f"PEG Bruto Calculado:   {peg_bruto:.2f} | Score PEG Normalizado: {score_peg:.2f}/10 (Acotado a 10)")
print(f"Margen de Seguridad:   {mos_pct:.2f}% | Score MoS: {score_mos:.2f}/10 (Acotado a 10)")
print(f"Value Score Calculado: 0.40({score_fcf:.2f}) + 0.30({score_peg:.2f}) + 0.30({score_mos:.2f}) = {value_score_calc:.2f}/10")

print("\n--- 4. INSPECION DE COHERENCIA EN EL INFORME (inform/fico_2026_q2.md) ---")

# Extract table values from report
cqv_in_report = re.findall(r'CQV Calidad.*?:?\s*\*?\*?([\d\.]+)', report)
value_score_report = re.findall(r'Value Score.*?:?\s*\*?\*?([\d\.]+)', report)
peg_bruto_report = re.findall(r'PEG Bruto.*?:?\s*\*?\*?([\d\.]+)', report)
iv_report = re.findall(r'Valor Intrínseco.*?:?\s*\*?\$?([\d\.]+)', report)
mos_report = re.findall(r'Margen de Seguridad.*?:?\s*\*?([\d\.]+)\%', report)
price_report = re.findall(r'Precio Actual.*?:?\s*\*?\$?([\d\.]+)', report)

print(f"Report Price found:         {price_report}")
print(f"Report CQV found:           {cqv_in_report}")
print(f"Report Value Score found:   {value_score_report}")
print(f"Report PEG Bruto found:     {peg_bruto_report}")
print(f"Report Intrinsic Val found: {iv_report}")
print(f"Report MoS % found:         {mos_report}")

print("\n==========================================================================")
