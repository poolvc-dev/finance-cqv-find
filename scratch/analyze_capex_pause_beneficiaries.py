import json

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_data = json.load(f)

print("=== ANÁLISIS DE BENEFICIARIOS FINANCIEROS ANTE UNA PAUSA EN CAPEX DE IA ===\n")

beneficiaries = [
    {'ticker': 'AMZN', 'name': 'Amazon.com, Inc.', 'type': 'Hiperescalador', 'cqv': 8.48, 'impact': 'Mayor beneficiado en FCF: de $40B a $90B+ Owner Earnings (+125% FCF expansion). CQV rebotaría a >9.30.'},
    {'ticker': 'META', 'name': 'Meta Platforms, Inc.', 'type': 'Hiperescalador', 'cqv': 9.57, 'impact': 'Ahorro directo de ~$35B en CapEx. FCF explotaría a >$65B, acelerando recompras masivas.'},
    {'ticker': 'GOOGL', 'name': 'Alphabet Inc.', 'type': 'Hiperescalador', 'cqv': 9.56, 'impact': 'Ahorro de ~$40B en CapEx. FCF Yield subiría del 3.5% al 6.5%, re-rating de múltiplo.'},
    {'ticker': 'MSFT', 'name': 'Microsoft Corporation', 'type': 'Hiperescalador', 'cqv': 9.68, 'impact': 'Eliminación del riesgo de compresión de caja. Conversión FCF superaría el 85% del ingreso operativo.'},
    {'ticker': 'CRM', 'name': 'Salesforce, Inc.', 'type': 'SaaS Enterprise', 'cqv': 9.07, 'impact': 'Caída en costes de infraestructura cloud / GPU cloud renting. Expansión de margen bruto en Agentforce.'},
    {'ticker': 'NOW', 'name': 'ServiceNow, Inc.', 'type': 'SaaS Enterprise', 'cqv': 9.53, 'impact': 'Reducción de COGS cloud. Mayor margen FCF al estancarse las tarifas de alquiler de IA.'},
    {'ticker': 'SAP', 'name': 'SAP SE', 'type': 'SaaS Enterprise', 'cqv': 9.41, 'impact': 'Ahorro en costes de infraestructura cloud de terceros (Azure/AWS/GCP).'},
    {'ticker': 'RMS', 'name': 'Hermès / Lujo Élite', 'type': 'Refugio Defensivo', 'cqv': 9.69, 'impact': 'Rotación masiva de capital de Wall Street desde Tech volátil hacia lujo indestructible.'},
    {'ticker': 'V', 'name': 'Visa Inc. / Finanzas', 'type': 'Refugio Defensivo', 'cqv': 9.60, 'impact': 'Buscado por su FCF Yield del 5%+ y cero dependencia de infraestructura tecnológica.'}
]

for b in beneficiaries:
    print(f"[{b['ticker']}] {b['name']} ({b['type']}) | CQV: {b['cqv']}")
    print(f"   Efecto Financiero: {b['impact']}\n")
