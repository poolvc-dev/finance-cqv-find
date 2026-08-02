import os

print("Injecting rich Red Lines section into FICO reports...")

red_lines_block = """
---

### 🚨 Líneas Rojas y Puntos de Atención Post-Resultados Trimestrales (Q3 FY26 / Q2 2026)

Wall Street castigó la cotización de FICO tras los balances debido a cuatro factores de escrutinio operativo y de valoración:

| Punto de Atención / Línea Roja | Diagnóstico Cuantitativo / Cualitativo | Severidad | Mitigación Operativa o Impacto a Largo Plazo |
| :--- | :--- | :---: | :--- |
| **1. Estancamiento de Volumen en Scoring Hipotecario** | El aumento de ingresos de Scores (+15.7% YoY) provino de subidas de precios; el volumen físico de hipotecas en EE.UU. sigue estancado por altas tasas. | Media | Inelasticidad de demanda probada. Al bajar las tasas de la Fed, el volumen rebotará acelerando ingresos de caja. |
| **2. Crecimiento Moderado en Software (SaaS)** | El segmento de Software creció al +8.7% YoY ($202.4M), por debajo de la aceleración esperada del +12% al +15% para FICO Platform. | Media | Los ciclos de venta de grandes plataformas bancarias son de 12-18 meses; la tasa de retención neta se mantiene >110%. |
| **3. Guía de CapEx e Inversiones Cloud** | Inversiones continuas en migración cloud y desarrollo de IA predictiva reducen temporalmente el margen FCF marginal. | Baja | Sinergias y apalancamiento operativo previstos con ROIC del 61.5% ampliamente superior al WACC (9.0%). |
| **4. Escrutinio Regulatorio de la CFPB** | Discusión política en EE.UU. sobre las tarifas de informes de crédito transmitidas a través de los tres burós. | Media | FICO cobra a los burós y prestamistas (b2b), respaldada por el mandato federal de Fannie Mae / Freddie Mac. |

"""

for filename in ['fico_2026_q2.md', 'fico_2026_q1.md']:
    filepath = os.path.join('inform', filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if '### 🚨 Líneas Rojas' not in content:
            # Insert right after Section 4 Tesis de Inversión
            if '## 4. Tesis de Inversión (Toro vs. Oso)' in content:
                parts = content.split('## 5. Owner Earnings, FCF Yield')
                if len(parts) == 2:
                    content = parts[0] + red_lines_block + '\n## 5. Owner Earnings, FCF Yield' + parts[1]
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("SUCCESSFULLY_INJECTED_FICO_RICH_RED_LINES")
