import json

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_data = json.load(f)

elites = [c for c in cqv_data if (c.get('cqv') or c.get('cqv_v4') or 0) >= 9.00]

print(f"TOTAL EMPRESAS ÉLITE Y ÉLITE SUPREMA: {len(elites)}\n")

high_exposure = ['NVDA', 'TSM', 'ASML', 'VRT', 'FN', 'MPWR', 'ETN', 'PWR', 'ANET', 'SMH', 'AVGO', 'AMAT', 'LRCX', 'KLAC', 'MRVL', 'DELL']
software_partial = ['MSFT', 'ORCL', 'CRM', 'CRWD', 'ADBE', 'NOW', 'SNOW', 'DDOG', 'PLTR']
immune_resilient = [c['ticker'] for c in elites if c['ticker'] not in high_exposure and c['ticker'] not in software_partial]

print("=== 1. ALTA EXPOSICIÓN AL CAPEX DE IA (AFECTACIÓN DIRECTA EN INGRESOS/CRECIMIENTO) ===")
for c in elites:
    if c['ticker'] in high_exposure:
        print(f" - [{c['ticker']}] {c['name']} | CQV: {c['cqv']} ({c['clasificacion']}) | Impacto: Directo en pedidos de hardware/infraestructura")

print("\n=== 2. EXPOSICIÓN PARCIAL / SOFTWARE (BENEFICIARIAS DE MENOR CAPEX / APALANCAMIENTO FCF) ===")
for c in elites:
    if c['ticker'] in software_partial:
        print(f" - [{c['ticker']}] {c['name']} | CQV: {c['cqv']} ({c['clasificacion']}) | Impacto: Reducción de CapEx elevaría su FCF instantáneamente")

print("\n=== 3. TOTALMENTE INMUNES / PROTEGIDAS (NEGOCIOS DE CONSUMO, LUJO, SALUD Y FINANZAS) ===")
for c in elites:
    if c['ticker'] in immune_resilient:
        print(f" - [{c['ticker']}] {c['name']} | CQV: {c['cqv']} ({c['clasificacion']}) | Impacto: Cero exposición a la infraestructura de IA")
