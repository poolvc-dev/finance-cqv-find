import os

print("Injecting rich Prospectivity and Dimensions section into FICO reports...")

prospectivity_block = """

#### 🔮 Diagnóstico de Dimensiones de Riesgo y Prospectiva de Cotización (3-6 meses vs. 12-36 meses)

##### A. Cuadro Diagnóstico por Dimensiones de Negocio

| Dimensión Analizada | Diagnóstico de Salud y Riesgo | ¿Hay Deterioro Estructural? |
| :--- | :--- | :---: |
| **Salud Financiera y Moat** | ROIC del 61.5% y margen operativo del 48.1%. Foso económico de monopolio regulatorio inalterado. | ❌ **NO** |
| **Cuota de Mercado** | Retención neta de clientes clave >110%. Mandato de Fannie Mae y Freddie Mac sin alternativas directas. | ❌ **NO** |
| **Origen de la Fricción** | Tasas de interés altas en EE.UU. (~6.5%-7.0%) que comprimen temporalmente el volumen de hipotecas. | ⚠️ **Factor Temporal** |

##### B. Prospectiva del Comportamiento de la Cotización por Horizontes Temporales

* **📉 Corto Plazo (Próximos 3 a 6 meses) — Consolidación y Volatilidad ($1,300 - $1,550 USD):**  
  La cotización puede experimentar un periodo de compresión de múltiplos PER hacia un nivel más sostenible (PER Forward 25x-28x) y una consolidación en rango lateral mientras el mercado digiere los resultados y ajusta expectativas.
* **📈 Mediano / Largo Plazo (12 a 36 meses) — Recuperación por Catalizadores ($2,075 USD Objetivo):**  
  A medida que la Fed recorte las tasas de interés y se reactiven las originaciones hipotecarias en EE.UU., sumado al despliegue de *FICO Platform* en software, la empresa volverá a acelerar la generación de flujo de caja libre, impulsando la revalorización de la cotización hacia su valor intrínseco de $2,075.00 por acción.

"""

for filename in ['fico_2026_q2.md', 'fico_2026_q1.md']:
    filepath = os.path.join('inform', filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if '#### 🔮 Diagnóstico de Dimensiones' not in content:
            if '| **4. Escrutinio Regulatorio de la CFPB** |' in content:
                parts = content.split('## 5. Owner Earnings, FCF Yield')
                if len(parts) == 2:
                    content = parts[0] + prospectivity_block + '\n## 5. Owner Earnings, FCF Yield' + parts[1]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("SUCCESSFULLY_INJECTED_FICO_PROSPECTIVITY")
