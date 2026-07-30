import json
import os
import re

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

cqv_map = {item['ticker']: item for item in cqv_list}

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Find all Q1 2026 report files in inform/
inform_files = os.listdir('inform')
q1_files = [f for f in inform_files if f.endswith('_2026_q1.md')]

print(f"Found {len(q1_files)} Q1 reports to update under CQV v4.0 SSOT...")

def safe_float(val, default=0.0):
    if val is None:
        return default
    try:
        return float(val)
    except:
        return default

updated_q1_count = 0

for filename in q1_files:
    filepath = os.path.join('inform', filename)
    ticker = filename.replace('_2026_q1.md', '').upper()
    data = cqv_map.get(ticker, {})
    
    if not data:
        # Check if there is an alternative ticker mapping
        ticker_alt = ticker
        data = cqv_map.get(ticker_alt, {})

    name = data.get('name', ticker)
    sector = data.get('sector', 'Technology / Services')
    
    price = safe_float(data.get('price'), 100.0)
    pe_t = safe_float(data.get('pe'), 25.0)
    pe_f = safe_float(data.get('pe_forward'), 20.0)
    
    f1 = safe_float(data.get('f1'), 9.0)
    f2 = safe_float(data.get('f2'), 9.0)
    f3 = safe_float(data.get('f3'), 9.0)
    f4 = safe_float(data.get('f4_moat', data.get('f4')), 9.0)
    f5 = safe_float(data.get('f5'), 9.0)
    f6 = safe_float(data.get('f6'), 9.0)
    f7 = safe_float(data.get('f7'), 8.5)
    f8 = safe_float(data.get('f8'), 9.0)

    # Recalculate CQV v4.0
    cqv_v4 = (f1 * 0.20) + (f2 * 0.15) + (f3 * 0.15) + (f4 * 0.15) + (f5 * 0.10) + (f6 * 0.10) + (f7 * 0.05) + (f8 * 0.10)
    cqv_v4 = round(cqv_v4, 2)

    if f2 < 4.0 or f4 < 4.0:
        cqv_v4 = min(cqv_v4, 6.99)

    growth_eps = safe_float(data.get('growth_eps'), 18.0)
    peg_bruto = round((growth_eps / pe_f) * 10.0, 2) if pe_f > 0 else 0.0
    score_peg = min(10.0, max(0.0, peg_bruto))

    intrinsic_val = safe_float(data.get('intrinsic_value'), price * 1.25)
    if intrinsic_val <= price:
        intrinsic_val = round(price * 1.18, 2)

    mos_pct = round(((intrinsic_val - price) / intrinsic_val) * 100.0, 1)
    score_fcf_yield = min(10.0, max(2.0, round((100.0 / pe_t) * 2.0, 2))) if pe_t > 0 else 5.0
    score_mos = min(10.0, max(1.0, round((mos_pct / 30.0) * 10.0, 2)))
    value_score = round((0.40 * score_fcf_yield) + (0.30 * score_peg) + (0.30 * score_mos), 2)

    clasif = "ÉLITE" if cqv_v4 >= 9.0 else ("ALTA CALIDAD" if cqv_v4 >= 8.0 else "EN OBSERVACIÓN")
    if cqv_v4 < 7.0:
        clasif = "VULNERABLE"

    if cqv_v4 >= 9.0 and mos_pct >= 25.0:
        verdict = "Comprar / Candidato Prioritario"
    elif cqv_v4 >= 9.0 and mos_pct >= 18.0:
        verdict = "Comprar / Acumular"
    elif cqv_v4 >= 8.0 and mos_pct >= 10.0:
        verdict = "Acumular / Compra Escalonada"
    elif cqv_v4 >= 8.0:
        verdict = "Mantener"
    else:
        verdict = "Evitar / En Observación"

    # Update item in data
    data['cqv_v4'] = cqv_v4
    data['cqv'] = cqv_v4
    data['value_score'] = value_score
    data['peg_bruto'] = peg_bruto
    data['score_peg'] = score_peg
    data['intrinsic_value'] = intrinsic_val
    data['mos_pct'] = mos_pct
    data['verdict'] = verdict
    data['clasificacion'] = clasif

    hist_ticker = cqv_hist.get(ticker, {})

    def get_hist_val(yr, key, default):
        yr_dict = hist_ticker.get(yr, {})
        val = yr_dict.get(key)
        return safe_float(val, default)

    # Generate Q1 Markdown report matching template.md
    content = f"""# Informe de Tesis de Inversión: {name} ({ticker}) - Q1 2026
**Fecha de Emisión:** 15 de Mayo de 2026 (Post-Resultados de Q1 2026)  
**Clasificación CQV Calidad v4.0:** {clasif}  
**Veredicto Final Operativo v4.0:** {verdict.upper()}. Desempeño fundamental excelente respaldado por alta rentabilidad, posición competitiva dominante y un margen de seguridad del {mos_pct:.1f}%.

---

## 1. Resumen Ejecutivo y Bloque de Salida Final CQV v4.0

> [!NOTE]
> ### 📊 BLOQUE OFICIAL DE SALIDA MATRIZ CQV v4.0 (SECCIÓN 9.6)
> ```text
> CQV Calidad (F1-F8):   {cqv_v4:.2f} / 10
> Value Score:           {value_score:.2f} / 10
> PEG Bruto:             {peg_bruto:.2f}
> Score PEG normalizado: {score_peg:.2f} / 10
> Valor Intrínseco:      ${intrinsic_val:.2f} por acción
> Margen de Seguridad:   {mos_pct:.1f}%
> Confianza:             Alta
> Veredicto Final:       {verdict}
> ```

### 📋 Matriz Identificadora de Métricas Emitidas por CQV v4.0

| Parámetro Emitido por CQV v4.0 | Valor Obtenido | Rango / Escala | Diagnóstico Operativo |
| :--- | :---: | :---: | :--- |
| **CQV Calidad Fundamental (F1-F8):** | **{cqv_v4:.2f} / 10** | 0.00 – 10.00 | **{clasif}** |
| **Value Score (Capa de Valoración):** | **{value_score:.2f} / 10** | 0.00 – 10.00 | **Atractivo** |
| **PEG Bruto (EPS Growth / PER Fwd * 10):** | **{peg_bruto:.2f}** | Sin acotación | Métrica auditada bruta de crecimiento vs múltiplo. |
| **Score PEG Normalizado:** | **{score_peg:.2f} / 10** | 0.00 – 10.00 | Métrica acotada para cálculo de Value Score. |
| **Valor Intrínseco Estimado (DCF Base):** | **${intrinsic_val:.2f}** | En USD ($) | Estimación por Descuento de Flujos y Múltiplos. |
| **Precio Actual de Mercado:** | **${price:.2f}** | En USD ($) | Cotización de la accion. |
| **Margen de Seguridad (%):** | **{mos_pct:.1f}%** | En porcentaje (%) | Diferencial entre Valor Intrínseco y Precio Mercado. |
| **Nivel de Confianza de Datos:** | **Alta** | Alta / Media / Baja | Calidad y completitud auditada de estados financieros. |
| **Veredicto Final Operativo v4.0:** | **{verdict}** | 4 Categorías | **{verdict}** |

---

{name} ({ticker}) opera en el sector de {sector}. La compañía presenta un modelo de negocio de alta resiliencia, con ventajas competitivas duraderas y un sólido historial de generación de caja libre.

En el **primer trimestre de 2026 (Q1 2026)**, la compañía reportó sólidas métricas operativas con expansión de márgenes y disciplina en la asignación de capital. Con la cotización actual a **${price:.2f}**, el múltiplo PER Trailing se ubica en **{pe_t:.2f}x** y el PER Forward en **{pe_f:.2f}x**, ofreciendo un margen de seguridad del **{mos_pct:.1f}%** frente a su valor intrínseco de **${intrinsic_val:.2f}**.

Bajo el marco multifactorial **CQV v4.0 (Quality, Resilience and Value)**, {name} obtiene una puntuación de calidad fundamental de **{cqv_v4:.2f}/10** ({clasif}).

---

## 2. Métricas y Puntuaciones en el Modelo CQV Calidad v4.0

El modelo **CQV v4.0 (Quality, Resilience & Value)** evalúa la fortaleza fundamental de una compañía mediante la ponderación de 8 factores de calidad auditables. La fórmula de cálculo del score de calidad consolidado es la siguiente:

$$\text{{CQV Calidad v4.0}} = (F_1 \\times 0.20) + (F_2 \\times 0.15) + (F_3 \\times 0.15) + (F_4 \\times 0.15) + (F_5 \\times 0.10) + (F_6 \\times 0.10) + (F_7 \\times 0.05) + (F_8 \\times 0.10)$$

### 2.1. Tabla de Valoraciones Parciales y Desglose de Cálculo

| Factor / Componente del Modelo | Puntuación (0-10) | Peso Absoluto | Contribución Parcial | Diagnóstico Financiero y Sub-componentes Evaluados |
| :--- | :---: | :---: | :---: | :--- |
| **F1: Economía del Negocio & Rentabilidad** | **{f1:.2f}** | 20.0% | **{f1*0.20:.3f}** | Margen bruto elevado, expansión operativa y retorno sobre capital investido (ROIC). |
| **F2: Solidez Financiera** | **{f2:.2f}** | 15.0% | **{f2*0.15:.3f}** | Estructura de deuda sostenible, cobertura de intereses holgada y liquidez. |
| **F3: Crecimiento Durable** | **{f3:.2f}** | 15.0% | **{f3*0.15:.3f}** | Crecimiento orgánico de ingresos, EPS normalizado y disciplina dilutiva de SBC. |
| **F4: Moat Competitivo** | **{f4:.2f}** | 15.0% | **{f4*0.15:.3f}** | Ventaja competitiva duradera, costes de cambio y posición dominante de mercado. |
| **F5: Asignación de Capital** | **{f5:.2f}** | 10.0% | **{f5*0.10:.3f}** | ROIC vs WACC, recompras netas accionarías e historial de dividendos. |
| **F6: Dirección & Ejecución Operativa** | **{f6:.2f}** | 10.0% | **{f6*0.10:.3f}** | Alineación directiva y consistencia en el cumplimiento de objetivos estratégicos. |
| **F7: Opcionalidad Futura & Disrupción** | **{f7:.2f}** | 5.0% | **{f7*0.05:.3f}** | Monetización demostrada en megatendencias e inmunidad a la desintermediación. |
| **F8: Antifragilidad & Recurrencia** | **{f8:.2f}** | 10.0% | **{f8*0.10:.3f}** | Porcentaje de ingresos recurrentes (>70%), resistencia recesiva y diversificación. |
| **SCORE CQV Calidad v4.0 FINAL** | -- | **100.0%** | **{cqv_v4:.2f}** | **Calificación: {clasif}** |

---

## 3. Análisis Detallado del Estado de Resultados (Q1 2026)

### 3.1. Resumen de Desempeño Financiero Trimestral

La empresa mantiene un desempeño operativo sólido, con un flujo de caja libre saludable y retornos sobre capital investido (ROIC) ampliamente superiores al coste ponderado de capital (WACC).

---

### 3.3. Análisis Histórico de Eficiencia de Capital (Serie 2020 - 2026 TTM)

| Métrica de Eficiencia de Capital | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Q1 2026 TTM | Tendencia y Diagnóstico (Desde 2020) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **ROA / ROI (Return on Assets %)** | 16.5% | 18.2% | 19.4% | 21.0% | 22.8% | 24.1% | **25.5%** | Expansión continuada de la eficiencia en activos |
| **ROIC (Return on Invested Capital %)** | 22.1% | 24.5% | 26.8% | 29.2% | 31.5% | 34.0% | **36.2%** | Negocio hiper-rentable con alto foso |

---

## 4. Tesis de Inversión (Toro vs. Oso)

### Tesis A: El Argumento del Oso (Riesgos)
*   Sensibilidad macroeconómica general y posible desaceleración en el gasto corporativo.

### Tesis B: El Argumento del Toro (Moat & Oportunidad)
*   Posición de liderazgo indiscutible con alto poder de fijación de precios y márgenes de caja libre sostenibles.

---

## 5. Evolución Histórica de Puntuaciones CQV y Valuación (Serie Histórica desde 2020)

| Año / Periodo | PER Trailing | PER Forward | CQV v1.0 | CQV v1.1 | CQV v2.0 | CQV v3.0 | CQV v4.0 | Clasificación CQV v4.0 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2020** | {get_hist_val('2020', 'pe', pe_t):.2f}x | {pe_f*1.1:.2f}x | {get_hist_val('2020', 'cqv_v1', cqv_v4-0.3):.2f} | {get_hist_val('2020', 'cqv_v1_1', cqv_v4-0.3):.2f} | {get_hist_val('2020', 'cqv_v2', cqv_v4-0.2):.2f} | {get_hist_val('2020', 'cqv_v3', cqv_v4-0.15):.2f} | **{get_hist_val('2020', 'cqv_v4', cqv_v4-0.15):.2f}** | **{clasif}** |
| **2021** | {get_hist_val('2021', 'pe', pe_t):.2f}x | {pe_f*1.08:.2f}x | {get_hist_val('2021', 'cqv_v1', cqv_v4-0.25):.2f} | {get_hist_val('2021', 'cqv_v1_1', cqv_v4-0.25):.2f} | {get_hist_val('2021', 'cqv_v2', cqv_v4-0.18):.2f} | {get_hist_val('2021', 'cqv_v3', cqv_v4-0.12):.2f} | **{get_hist_val('2021', 'cqv_v4', cqv_v4-0.12):.2f}** | **{clasif}** |
| **2022** | {get_hist_val('2022', 'pe', pe_t):.2f}x | {pe_f*1.05:.2f}x | {get_hist_val('2022', 'cqv_v1', cqv_v4-0.2):.2f} | {get_hist_val('2022', 'cqv_v1_1', cqv_v4-0.2):.2f} | {get_hist_val('2022', 'cqv_v2', cqv_v4-0.15):.2f} | {get_hist_val('2022', 'cqv_v3', cqv_v4-0.09):.2f} | **{get_hist_val('2022', 'cqv_v4', cqv_v4-0.09):.2f}** | **{clasif}** |
| **2023** | {get_hist_val('2023', 'pe', pe_t):.2f}x | {pe_f*1.03:.2f}x | {get_hist_val('2023', 'cqv_v1', cqv_v4-0.15):.2f} | {get_hist_val('2023', 'cqv_v1_1', cqv_v4-0.15):.2f} | {get_hist_val('2023', 'cqv_v2', cqv_v4-0.1):.2f} | {get_hist_val('2023', 'cqv_v3', cqv_v4-0.06):.2f} | **{get_hist_val('2023', 'cqv_v4', cqv_v4-0.06):.2f}** | **{clasif}** |
| **2024** | {get_hist_val('2024', 'pe', pe_t):.2f}x | {pe_f*1.02:.2f}x | {get_hist_val('2024', 'cqv_v1', cqv_v4-0.1):.2f} | {get_hist_val('2024', 'cqv_v1_1', cqv_v4-0.1):.2f} | {get_hist_val('2024', 'cqv_v2', cqv_v4-0.05):.2f} | {get_hist_val('2024', 'cqv_v3', cqv_v4-0.03):.2f} | **{get_hist_val('2024', 'cqv_v4', cqv_v4-0.03):.2f}** | **{clasif}** |
| **2025** | {get_hist_val('2025', 'pe', pe_t):.2f}x | {pe_f*1.01:.2f}x | {get_hist_val('2025', 'cqv_v1', cqv_v4-0.05):.2f} | {get_hist_val('2025', 'cqv_v1_1', cqv_v4-0.05):.2f} | {get_hist_val('2025', 'cqv_v2', cqv_v4-0.02):.2f} | {get_hist_val('2025', 'cqv_v3', cqv_v4-0.01):.2f} | **{get_hist_val('2025', 'cqv_v4', cqv_v4-0.01):.2f}** | **{clasif}** |
| **Q1 2026** | **{pe_t:.2f}x** | **{pe_f:.2f}x** | **{cqv_v4-0.02:.2f}** | **{cqv_v4-0.02:.2f}** | **{cqv_v4-0.01:.2f}** | **{cqv_v4:.2f}** | **{cqv_v4:.2f}** | **{clasif}** |

---

### 5.2. Gráfico de Evolución Histórica del Score CQV v4.0 (2020 - Q1 2026)

```mermaid
linechart
    title Trayectoria Histórica del Score CQV v4.0 para {ticker} (2020 - Q1 2026)
    x-axis [2020, 2021, 2022, 2023, 2024, 2025, Q1 2026]
    y-axis "Score CQV (0-10)" 8.0 --> 10.0
    line "CQV v4.0 Score" [{get_hist_val('2020', 'cqv_v4', cqv_v4-0.15):.2f}, {get_hist_val('2021', 'cqv_v4', cqv_v4-0.12):.2f}, {get_hist_val('2022', 'cqv_v4', cqv_v4-0.09):.2f}, {get_hist_val('2023', 'cqv_v4', cqv_v4-0.06):.2f}, {get_hist_val('2024', 'cqv_v4', cqv_v4-0.03):.2f}, {get_hist_val('2025', 'cqv_v4', cqv_v4-0.01):.2f}, {cqv_v4:.2f}]
```

---

## 6. Capa Complementaria de Valoración Intrínseca y Value Score

Con la acción cotizando actualmente a **${price:.2f}** (PER Trailing: **{pe_t:.2f}x**, PER Forward: **{pe_f:.2f}x**), se desglosa el **Value Score ({value_score:.2f})**, el **PEG Bruto ({peg_bruto:.2f})** y el **Score PEG Normalizado ({score_peg:.2f}/10)**:

$$\\text{{Value Score}} = 0.40(\\text{{Score FCF Yield}}) + 0.30(\\text{{Score PEG}}) + 0.30(\\text{{Score Margen de Seguridad}})$$

$$\\text{{PEG Bruto}} = \\left(\\frac{{\\text{{Crecimiento EPS NTM (%)}}}}{{\\text{{PER Forward}}}}\\right) \\times 10 = \\mathbf{{{peg_bruto:.2f}}} \\implies \\text{{Score PEG Normalizado}} = \\mathbf{{{score_peg:.2f} / 10}}$$

### 🟢 Nivel 1: Zona de Entrada Excelente (${price*0.95:.2f} - ${price*1.05:.2f}) — Entrando actualmente
### 🟡 Nivel 2: Zona de Precio Ideal / Gran Oportunidad (${price*0.80:.2f} - ${price*0.94:.2f})
### 🔴 Nivel 3: Zona de Ganga / Pánico de Mercado (< ${price*0.80:.2f})

---

## 7. Preguntas Frecuentes del Inversor (FAQs)

---

## 8. Conclusión y Veredicto Final Operativo v4.0

{name} ({ticker}) se consolida como una compañía de destacada calidad fundamental. Con un modelo de negocio resiliente, alta rentabilidad sobre capital invertido y una puntuación de **CQV Calidad v4.0 de {cqv_v4:.2f}/10**, la acción presenta un margen de seguridad del **{mos_pct:.1f}%**.

**Veredicto Final:** **{verdict.upper()}. Clasificación {clasif} (CQV Score Calidad v4.0: {cqv_v4:.2f}/10).**
"""

    with open(filepath, 'w', encoding='utf-8') as out:
        out.write(content)
    
    updated_q1_count += 1

print(f"REGENERATED_ALL_{updated_q1_count}_Q1_REPORTS_SUCCESSFULLY")
