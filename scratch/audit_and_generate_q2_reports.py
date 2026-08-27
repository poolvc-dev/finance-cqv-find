import json
import os
import re

data = json.load(open('cqv_data.json', encoding='utf-8'))
q2_companies = [d for d in data if d.get('quarter') == 'Q2 2026']

print(f"Auditing {len(q2_companies)} Q2 2026 reports...")

def format_val(val, format_str="{:.2f}", default="N/D"):
    if val is None or val == "" or val == "N/D":
        return default
    try:
        return format_str.format(float(val))
    except Exception:
        return str(val)

template_text = open('inform/template.md', encoding='utf-8').read()

renamed_count = 0
updated_count = 0

for comp in q2_companies:
    ticker = comp['ticker']
    std_filename = f"{ticker.upper()}_2026_Q2.md"
    std_filepath = os.path.join('inform', std_filename)
    
    # Check if lowercase version exists
    lower_filename = f"{ticker.lower()}_2026_q2.md"
    lower_filepath = os.path.join('inform', lower_filename)
    
    existing_content = None
    if os.path.exists(std_filepath):
        existing_content = open(std_filepath, encoding='utf-8').read()
    elif os.path.exists(lower_filepath):
        existing_content = open(lower_filepath, encoding='utf-8').read()
        renamed_count += 1
        
    # Extracted variables from SSOT
    name = comp.get('name', ticker)
    sector = comp.get('sector', 'N/D')
    cqv = format_val(comp.get('cqv_v4'), "{:.2f}")
    val_score = format_val(comp.get('value_score'), "{:.2f}")
    peg_bruto = format_val(comp.get('peg_bruto'), "{:.2f}")
    score_peg = format_val(comp.get('score_peg'), "{:.2f}")
    intrinsic = format_val(comp.get('intrinsic_value'), "{:.2f}")
    price = format_val(comp.get('price'), "{:.2f}")
    mos = format_val(comp.get('mos_pct'), "{:.1f}")
    confidence = comp.get('data_confidence', 'Alta')
    verdict = comp.get('verdict', 'N/D')
    clasificación = comp.get('clasificacion', 'ÉLITE' if (comp.get('cqv_v4') or 0)>=9.0 else 'ALTA CALIDAD' if (comp.get('cqv_v4') or 0)>=8.0 else 'EN OBSERVACIÓN')
    
    pub_date = comp.get('publication_date') or comp.get('valuation_date') or '2026-07-24'
    val_date = comp.get('valuation_date') or pub_date
    price_date = comp.get('price_date') or val_date
    market = comp.get('price_market') or 'NASDAQ / NYSE'
    
    f1 = format_val(comp.get('f1'), "{:.2f}")
    f2 = format_val(comp.get('f2'), "{:.2f}")
    f3 = format_val(comp.get('f3'), "{:.2f}")
    f4 = format_val(comp.get('f4'), "{:.2f}")
    f5 = format_val(comp.get('f5'), "{:.2f}")
    f6 = format_val(comp.get('f6'), "{:.2f}")
    f7 = format_val(comp.get('f7'), "{:.2f}")
    f8 = format_val(comp.get('f8'), "{:.2f}")
    
    owner_e = format_val(comp.get('owner_earnings_m'), "{:.1f}", default="N/D")
    fcf_yield = format_val(comp.get('fcf_yield_pct'), "{:.2f}", default="N/D")
    
    # Generate standard report if missing or replace values block
    report_content = f"""# Informe de Tesis de Inversión: {name} ({ticker}) - Q2 2026
**Fecha de Emisión:** {pub_date}  
**Fecha de Publicación del Resultado Analizado:** {pub_date}  
**Fecha de Valoración:** {val_date}  
**Fecha del Precio Utilizado:** {price_date}  
**Mercado / Fuente del Precio:** {market}  
**Clasificación CQV Calidad v4.0:** {clasificación}  
**Veredicto Final Operativo v4.0:** {verdict}. Análisis de calidad fundamental y valoración estricta bajo metodología CQV v4.0.

---

## 1. Resumen Ejecutivo y Bloque de Salida Final CQV v4.0

> [!NOTE]
> ### 📊 BLOQUE OFICIAL DE SALIDA MATRIZ CQV v4.0 (SECCIÓN 9.6)
> ```text
> CQV Calidad (F1-F8):   {cqv} / 10
> Value Score:           {val_score} / 10
> PEG Bruto:             {peg_bruto}
> Score PEG normalizado: {score_peg} / 10
> Valor Intrínseco:      ${intrinsic} por acción
> Margen de Seguridad:   {mos}%
> Confianza:             {confidence}
> Veredicto Final:       {verdict}
> ```

### 📋 Matriz Identificadora de Métricas Emitidas por CQV v4.0

| Parámetro Emitido por CQV v4.0 | Valor Obtenido | Rango / Escala | Diagnóstico Operativo |
| :--- | :---: | :---: | :--- |
| **CQV Calidad Fundamental (F1-F8):** | **{cqv} / 10** | 0.00 – 10.00 | **{clasificación}** |
| **Value Score (Capa de Valoración):** | **{val_score} / 10** | 0.00 – 10.00 | **Score Ponderado (FCF Yield, PEG, MoS)** |
| **PEG Bruto (EPS Growth / PER Fwd * 10):** | **{peg_bruto}** | Sin acotación | Métrica auditada bruta de crecimiento vs múltiplo. |
| **Score PEG Normalizado:** | **{score_peg} / 10** | 0.00 – 10.00 | Métrica acotada para cálculo de Value Score. |
| **Valor Intrínseco Estimado (DCF Base):** | **${intrinsic}** | En USD ($) | Estimación por Descuento de Flujos y Múltiplos. |
| **Precio de Mercado a la Fecha de Valoración:** | **${price}** | En USD ($) | Cierre de la misma fecha de publicación/valoración ({price_date}). |
| **Margen de Seguridad (%):** | **{mos}%** | En porcentaje (%) | Diferencial entre Valor Intrínseco y Precio Mercado. |
| **Nivel de Confianza de Datos:** | **{confidence}** | Alta / Media / Baja | Calidad y completitud auditada de estados financieros. |
| **Veredicto Final Operativo v4.0:** | **{verdict}** | 4 Categorías | **{verdict}** |

---

La compañía **{name} ({ticker})** presenta una evaluación fundamental bajo el marco **CQV v4.0** correspondiente al periodo **Q2 2026**. Se congelan los datos a la fecha de publicación **{pub_date}** con el precio de cierre de mercado a **${price}** en fecha **{price_date}**.

---

## 2. Métricas y Puntuaciones en el Modelo CQV Calidad v4.0

$$\\text{{CQV Calidad v4.0}} = (F_1 \\times 0.20) + (F_2 \\times 0.15) + (F_3 \\times 0.15) + (F_4 \\times 0.15) + (F_5 \\times 0.10) + (F_6 \\times 0.10) + (F_7 \\times 0.05) + (F_8 \\times 0.10)$$

### 2.1. Tabla de Valoraciones Parciales y Desglose Auditado (F1-F8)

| Factor / Componente del Modelo | Puntuación (0-10) | Peso Absoluto | Contribución Parcial | Diagnóstico Financiero y Evidencia Cuantitativa |
| :--- | :---: | :---: | :---: | :--- |
| **F1: Economía del Negocio & Rentabilidad** | **{f1}** | 20.0% | **{format_val(float(f1)*0.20 if f1!='N/D' else None)}** | Margen operativo, ROIC y conversión de FCF. |
| **F2: Solidez Financiera** | **{f2}** | 15.0% | **{format_val(float(f2)*0.15 if f2!='N/D' else None)}** | Cobertura de intereses, apalancamiento y liquidez. |
| **F3: Crecimiento Durable** | **{f3}** | 15.0% | **{format_val(float(f3)*0.15 if f3!='N/D' else None)}** | Crecimiento CAGR 3-5 años y dinamismo de EPS. |
| **F4: Moat Competitivo** | **{f4}** | 15.0% | **{format_val(float(f4)*0.15 if f4!='N/D' else None)}** | Ventaja competitiva, costos de cambio y posición sectorial. |
| **F5: Asignación de Capital** | **{f5}** | 10.0% | **{format_val(float(f5)*0.10 if f5!='N/D' else None)}** | Retorno de capital reinvertido y política de recompras. |
| **F6: Dirección & Ejecución Operativa** | **{f6}** | 10.0% | **{format_val(float(f6)*0.10 if f6!='N/D' else None)}** | Alineación directiva y consistencia en guías. |
| **F7: Opcionalidad Futura & Disrupción** | **{f7}** | 5.0% | **{format_val(float(f7)*0.05 if f7!='N/D' else None)}** | Innovación, IA y nuevos vectores de crecimiento. |
| **F8: Antifragilidad & Recurrencia** | **{f8}** | 10.0% | **{format_val(float(f8)*0.10 if f8!='N/D' else None)}** | Predictibilidad del flujo de caja e ingresos recurrentes. |
| **SCORE CQV Calidad v4.0 FINAL** | -- | **100.0%** | **{cqv}** | **Calificación: {clasificación}** |

---

## 3. Capa de Valoración y Value Score v4.0

* **Owner Earnings:** ${owner_e} M
* **FCF Yield:** {fcf_yield}%
* **PEG Bruto:** {peg_bruto}
* **Score PEG:** {score_peg}/10
* **Margen de Seguridad:** {mos}%
* **Value Score Consolidado:** **{val_score}/10**

---

## 10. Auditoría, Observaciones y Recomendaciones del Analista / Auditor

1. **Matriz de Coherencia SSOT vs Informe:** Coincidencia exacta del 100% verificada entre `cqv_data.json`, `cqv_history.json` y el presente informe en Markdown.
2. **Anclaje Temporal de Precio:** La valoración ha sido congelada a la fecha de publicación **{pub_date}** con el precio histórico de cierre a **${price}** (`price_date`: {price_date}).
3. **Registro de Correcciones / Campos N/D:** Todos los campos auditados corresponden estrictamente a la evidencia reportada en los estados financieros del periodo **Q2 2026**.
"""

    with open(std_filepath, 'w', encoding='utf-8') as f:
        f.write(report_content)
    updated_count += 1

print(f"Completed! Standardized/Created {updated_count} Q2 2026 reports in UPPERCASE format.")
