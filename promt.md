# Prompt maestro de actualización CQV v5.0

Utiliza este prompt para actualizar una o varias acciones bajo el flujo SSOT definido en `flujo_actualizacion_datos.md` y el estándar metodológico oficial `metodo_v5.0.md`.

---

## 📌 Estándar de Nominación por Ciclo de Presentación (P1 - P4)

La nominación de periodos de análisis en la metodología CQV se rige **estrictamente por la ventana del año calendario en que la empresa emite la presentación de resultados al mercado**, independientemente de las variaciones del año fiscal de cada compañía:

- **P1**: Presentación de resultados emitida entre **Abril y Junio** (Mayo - Junio; 1er informe trimestral presentado en el año).
- **P2**: Presentación de resultados emitida entre **Julio y Septiembre** (Julio - Agosto; 2º informe trimestral / mitad del año).
- **P3**: Presentación de resultados emitida entre **Octubre y Diciembre** (Octubre - Noviembre; 3er informe trimestral del año).
- **P4**: Presentación de resultados emitida entre **Enero y Marzo del siguiente año** (4º informe trimestral / cierre del ejercicio previo).

> [!IMPORTANT]
> **Queda terminantemente prohibido usar Q1, Q2, Q3, Q4 como nombre del periodo analizado en el ciclo CQV.**  
> El periodo debe denominarse obligatoriamente como **P1, P2, P3 o P4**.  
> El trimestre fiscal de la compañía solo se cita como complemento entre paréntesis para trazabilidad contable:  
> `P[1-4] [AÑO_CALENDARIO] (Q[1-4] Fiscal [AÑO_FISCAL])`.

---

## ⚙️ Metodología Oficial Obligatoria: CQV v5.0

Todos los cálculos, recopilaciones de datos, valoraciones y emisiones de informes operan exclusivamente bajo **CQV v5.0**:
- **Manual metodológico único:** `metodo_v5.0.md`.
- **Campo obligatorio en `cqv_data.json`:** `"metodologia_version": "v5.0"`.
- **Ruta y organización de informes Markdown:** `inform/cqv_v5/[AÑO] P[1-4]/[TICKER]_[AÑO]_P[1-4]_CQVv5.md` (organizado estrictamente en subcarpetas por periodo como `2026 P3`, `2026 P2`, etc., donde `[TICKER]` va en MAYÚSCULAS).

---

## 🏛️ Estándar de Rigor Analítico y Calidad Exhaustiva (Norma FICO 2026 P3)

Inspirado en el estándar de excelencia demostrado en el informe de **FICO 2026 P3**, cada bloque de análisis debe cumplir con un nivel de profundidad y personalización riguroso. **Queda estrictamente prohibido el uso de textos genéricos, plantillas repetitivas o marcadores de posición (*boilerplate*).**

### 1. Cero Textos Genéricos (*No Boilerplate*):
* **Prohibido:** Nombres ficticios de competidores como *"Par Sectorial 1"*, *"Par Sectorial 2"* o *"Competidor en segmento primario"*. Deben identificarse los **dos competidores directos o iniciativas rivales reales más relevantes**, con su nombre corporativo y símbolo bursátil / ticker (ej. *Equifax Inc. (EFX)*, *VantageScore 4.0*, *Microsoft Corporation (MSFT)*, *Snowflake Inc. (SNOW)*).
* **Prohibido:** Marcadores comodín como *"Ver 10-K"* o *"N/D"* en tablas multianuales cuando los datos históricos están disponibles en los estados financieros auditados.
* **Prohibido:** Viñetas de guidance repetitivas o universales (ej. *"La dirección reafirma sus objetivos con foco en márgenes"*). Cada guidance debe contener proyecciones numéricas específicas para los próximos doce meses (NTM).

### 2. Rigor Estructural en la Sección 3.1 (*Tabla Comparativa de Resultados Periódicos*):
* **Estructura estricta de exactamente 6 columnas:** La tabla Markdown debe tener idéntico número de delimitadores (6 columnas) en el encabezado, en la fila separadora (`| :--- | :---: | :---: | :---: | :---: | :---: |`) y en cada una de las filas de datos.
* **Cifras trimestrales reales (no anualizadas ni extrapoladas de capitalización):** Ingresos, EBIT, Margen %, Beneficio Neto, EPS GAAP y Non-GAAP, OCF, CapEx, FCF y Acciones Diluidas deben ser cifras reales del periodo expresadas en millones de USD (\$M) o EPS en USD (\$).
* **Variaciones porcentuales calculadas matemáticamente:** Obligatorio incluir Variación PoP (%) respecto al trimestre previo y Variación YoY (%) respecto al mismo trimestre del año anterior.

### 3. Profundidad Estratégica en la Sección 3.2 y Sección 4 (*Factores que Afectan al Negocio y Estrategias Defensivas*):
* **¿Qué está afectando al negocio en el periodo analizado?:** Análisis explícito de los vientos en contra actuales (cambios regulatorios, iniciativas gubernamentales, ciclos de tipos de interés, presiones de costes o intentos de disrupción por parte de clientes/burós/plataformas).
* **Estrategias para no ser desplazado:** Identificación de las palancas defensivas que la compañía despliega activamente para proteger y ensanchar su foso (*moat*), tales como:
  * Dependencia institucional y estandarización en mercados secundarios o mercados de capitales (ej. exigencias de inversores de bonos/titulizaciones).
  * Superioridad tecnológica y precisión predictiva de nuevos productos (ej. modelos de datos con series temporales / *trended data*).
  * Pivote estratégico hacia modelos de software en la nube / plataformas SaaS con altas tasas de retención neta (NRR > 115%) e ingresos recurrentes (ARR).
  * Reestructuración de acuerdos mayoristas y fijación directa de precios (*direct-to-lender / direct-to-consumer*).
  * Integración nativa de nuevas fuentes de datos (ej. datos alternativos, IA, pagos aplazados/BNPL).

### 4. Rigor en Guidance y Perspectivas Futuras (Sección 3.5):
Cada informe debe detallar obligatoriamente:
* **Rango de Ingresos Consolidados Estimados (NTM):** Estimación en millones de USD (\$M) con porcentaje de crecimiento esperado YoY.
* **Beneficio por Acción Diluido Forward (BPA NTM):** Cifra de consenso y aceleración porcentual esperada frente al trailing.
* **Rango Objetivo de Margen Operativo:** Rango porcentual proyectado por la dirección.
* **Estrategia de Asignación de Capital:** Prioridades de I+D, CapEx orgánico, adquisiciones y programas de recompras de acciones.
* **Consenso de Analistas de Wall Street:** Número de analistas cubriendo la acción, recomendación media (BUY / HOLD / SELL) y precio objetivo promedio (con rango mínimo y máximo).

### 5. Tesis de Inversión Rigurosa (Sección 4):
* **Tesis del Oso (Sección 4.1):** Mínimo 3 argumentos sustantivos detallando riesgos sectoriales, regulatorios, competitivos o de compresión de múltiplos.
* **Tesis del Toro (Sección 4.2):** Mínimo 3 catalizadores fundamentales basados en ventajas competitivas verificadas, apalancamiento operativo y generación de Owner Earnings.
* **Líneas Verdes (Sección 4.3):** Hitos operacionales cuantitativos que confirman la aceleración del moat.
* **Líneas Rojas (Sección 4.4):** Condiciones numéricas y estructurales de ruptura (ej. contracción de márgenes >250 bps por 2 trimestres, pérdida de cuota >X% frente a rivales específicos, o desaceleración de ARR).

### 6. Integridad de la Sección 8 (*Historial Periódico y Gráfico Mermaid*):
* **Tabla 8.1:** Debe contener **exactamente 13 columnas** obligatorias:
  `| Periodo Auditado | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | CQV v5.0 | Value Score | Clasificación | Veredicto Operativo |`
* **Gráfico Mermaid 8.2:** Sintaxis formal `xychart-beta` con eje X conteniendo los periodos históricos (`["2024 P1", ..., "2026 P3"]`) y línea de evolución continua del score CQV v5.0.

---

## Prompt

```text
Actualiza completamente bajo la metodología CQV v5.0 las siguientes acciones:

[TICKER1], [TICKER2], [TICKER3]

Periodo de análisis: P[1-4] [AÑO_CALENDARIO] (Correspondiente a Q[1-4] Fiscal [AÑO_FISCAL])
Fecha de valoración: [DD/MM/AAAA]

La fecha de valoración debe ser la fecha en la que se publicó el informe financiero o earnings release analizado (publication_date). El precio utilizado debe ser obligatoriamente el cierre de mercado de esa misma fecha (price_date) y del mismo mercado de cotización. Está estrictamente prohibido usar el precio o la capitalización actual para un informe histórico.

Aplica estrictamente:
- flujo_actualizacion_datos.md
- metodo_v5.0.md
- inform/template.md
- Norma de rigor analítico FICO 2026 P3 (cero boilerplate, datos trimestrales reales, competidores concretos, estrategias anti-desplazamiento).

OBJETIVO

Recopila toda la información financiera, operativa, competitiva y de valoración necesaria. Actualiza el SSOT, sincroniza los archivos derivados, el dashboard y los informes Markdown en sus respectivas subcarpetas de periodo.

REGLAS OBLIGATORIAS

1. No inventes ningún dato.
2. No utilices valores por defecto ni textos plantilla prefabricados.
3. No completes campos faltantes mediante estimaciones no identificadas.
4. Si un dato no está disponible o no puede verificarse, utiliza N/D, indica el motivo y explica su impacto.
5. Registra para cada cifra la fuente, fecha, periodo y unidad.
6. Utiliza preferentemente fuentes primarias:
   - SEC 10-Q/10-K, 6-K o RNS.
   - Earnings release oficial y transcripción de la conferencia de resultados (*Earnings Call*).
   - Presentaciones oficiales para inversores.
   - Guidance oficial corporativo y consenso de analistas.
   - Datos de mercado oficiales de cierre fechados al día de publicación.
7. No reutilices datos de otro periodo sin indicarlo expresamente.

8. Fecha histórica y precio de mercado (Anclaje Temporal Obligatorio):
   - Todo informe debe elaborarse congelado en la fecha exacta en la que se publicó el informe financiero o earnings release analizado (publication_date).
   - valuation_date debe coincidir exactamente con publication_date, salvo que se documente una razón operativa verificable.
   - price_date debe coincidir con valuation_date y el precio utilizado debe corresponder obligatoriamente al cierre del mercado de cotización de esa misma fecha.
   - Si la publicación ocurre fuera del horario de mercado, utiliza el cierre de esa misma sesión; si no hubo sesión, utiliza la sesión anterior y documenta el motivo.
   - Registra price_source, price_market, price_currency y la hora de publicación cuando esté disponible.
   - Para informes históricos está prohibido utilizar un precio actual o una capitalización actual.
   - Si no puede verificarse el precio de la fecha correcta, price, capitalización, PER, Value Score, MoS y veredicto dependientes deben quedar como N/D.

9. Historial periódico obligatorio (P1 - P4):
   - cqv_history.json debe organizarse estrictamente como TICKER → AÑO → P1/P2/P3/P4.
   - La actualización solo puede añadir o corregir el periodo solicitado (P1, P2, P3 o P4).
   - Debe conservar los periodos anteriores y no sobrescribirlos.
   - No conviertas una puntuación anual en una puntuación periódica.
   - Si un periodo no tiene evidencia verificable, registra null/N/D.
   - Los registros anuales antiguos, si existen, deben conservarse bajo annual_legacy y no utilizarse como sustituto de P1-P4.
   - Cada snapshot debe incluir periodo, fecha de cierre, fecha de publicación, fecha de valoración, fecha del precio, F1-F8, CQV v5.0, Value Score v5.0, valoración, fuentes y confianza.

10. Rigor analítico en los bloques de texto del informe:
   - La Sección 3.1 debe estructurarse con exactamente 6 columnas y con cifras trimestrales reales en millones de USD (\$M).
   - La Sección 3.2 debe identificar competidores y amenazas reales con ticker y detallar la ventaja competitiva estructural.
   - La Sección 4 debe analizar tanto los factores adversos actuales que impactan al negocio como las estrategias concretas que la directiva adopta para no ser desplazada del mercado.
   - La Sección 3.5 debe contener proyecciones numéricas de ingresos, BPA forward, márgenes y consenso de analistas.
   - La Sección 8.1 debe cumplir con el formato de 13 columnas auditado por verify_section8.py.

DATOS A RECOPILAR PARA CADA ACCIÓN

A. Identificación:
- Ticker, nombre, sector, industria, periodo (P1-P4), fecha de cierre fiscal, fecha de publicación, fecha de valoración y fecha del precio.

B. Resultados financieros trimestrales:
- Ingresos consolidados del trimestre actual, previo y mismo trimestre del año anterior.
- Beneficio operativo (EBIT) y margen operativo actual, previo y YoY.
- Beneficio neto GAAP y Non-GAAP.
- EPS GAAP diluido y EPS ajustado/normalizado.
- Flujo de caja operativo (OCF) y CapEx de mantenimiento.
- Free Cash Flow (FCF) del periodo y Owner Earnings TTM.
- Deuda bruta, caja/equivalentes y deuda neta.
- Acciones diluidas en circulación.
- Recompras de acciones y dividendos.

C. Evolución histórica y eficiencia de capital:
- ROIC, ROA/ROI y ROE (nivel actual y comparativa con el WACC).
- Serie histórica de ingresos, márgenes, EPS y FCF (FY-2, FY-1, TTM).
- Evolución histórica de las puntuaciones CQV v5.0 por periodos P1–P4 desde 2020.

D. Factores CQV v5.0:

Calcula y justifica F1-F8 con evidencia específica del negocio conforme a metodo_v5.0.md:
- F1: Economía del negocio y rentabilidad (Margen, ROIC, Conversión de caja). Peso: 20%.
- F2: Solidez financiera (Apalancamiento, Cobertura, Liquidez, Refinanciación, Estrés). Peso: 15%.
- F3: Crecimiento durable (Ingresos, EPS, Retención/Precio, Dilución neta). Peso: 15%.
- F4: Moat competitivo (Switching costs, Efecto red/Datos/IP, Retornos vs pares, Durabilidad). Peso: 15%.
- F5: Asignación de capital (ROIC incremental vs WACC, Recompras, M&A, Balance). Peso: 10%.
- F6: Dirección, gobierno y ejecución (Cumplimiento de guías, Transparencia, Incentivos, Ejecución). Peso: 10%.
- F7: Opcionalidad futura y disrupción (Oportunidades comprobables, Adaptación a IA). Peso: 5%.
- F8: Resiliencia operativa (Recurrencia contractual, Ciclicidad, Diversificación, Flexibilidad). Peso: 10%.

Ecuación de Calidad CQV v5.0:
CQV v5.0 = F1×0.20 + F2×0.15 + F3×0.15 + F4×0.15 + F5×0.10 + F6×0.10 + F7×0.05 + F8×0.10

Filtros rígidos de CQV v5.0:
- Si F2 < 4.0 o F4 < 4.0, el CQV máximo permitido es 6.99.
- Si el estrés de F2 revela riesgo de quiebra/covenants, severe_stress_flag = true (CQV capped en 6.99, Vulnerable).
- Si F2 o F8 es N/D, CQV = N/D.

Clasificación de Calidad CQV v5.0:
- ÉLITE SUPREMA: CQV ≥ 9.50 y F2, F4, F8 ≥ 7.0.
- ÉLITE: CQV 9.00–9.49 y F2, F4, F8 ≥ 7.0.
- ALTA CALIDAD: CQV 8.00–8.99.
- EN OBSERVACIÓN: CQV 7.00–7.99.
- VULNERABLE: CQV < 7.00 o activación de filtro de estrés severo F2.

E. Capa de Valoración (Value Score v5.0):
- Precio de cierre de la fecha de valoración (price_date = publication_date).
- PER Trailing y PER Forward NTM.
- Crecimiento EPS NTM en porcentaje (%).
- Capitalización bursátil (precio × acciones diluidas).
- OCF TTM y Maintenance CapEx TTM (Owner Earnings).
- Valor intrínseco DCF base y esperado (ponderación multiescenario).
- WACC y tasa terminal (g).

Fórmulas de Valoración CQV v5.0:
- Owner Earnings = OCF - Maintenance CapEx
- FCF Yield Real (%) = (Owner Earnings / Capitalización bursátil) × 100
- Score FCF Yield: escala 1.0–10.0 según percentil sectorial.
- Ratio Crecimiento / Múltiplo Bruto = (Crecimiento EPS NTM (%) / PER Forward) × 10
- Score Crecimiento / Múltiplo Normalizado = min(10.0, max(1.0, Ratio Bruto))
- Margen de Seguridad (%) = (Valor Intrínseco Base - Precio) / Valor Intrínseco Base × 100
- Score Margen de Seguridad: escala 1.0–10.0.

Ecuación Consolidada del Value Score v5.0:
Value Score v5.0 = 0.40 × Score FCF Yield + 0.30 × Score Crecimiento/Múltiplo + 0.30 × Score MoS

Reglas de Veredicto v5.0 (Sección 7 de metodo_v5.0.md):
- Comprar / Revisar Compra: CQV ≥ 8.0, confianza Alta/Media, F2 y F8 disponibles, MoS esperado ≥ 20%, MoS base ≥ 10%, Value Score ≥ 6.0.
- Acumular: CQV ≥ 8.0, confianza Alta/Media, MoS esperado ≥ 10%, Value Score ≥ 5.0.
- Mantener: CQV ≥ 8.0, pero MoS esperado < 10% o supuestos implícitos exigentes.
- Evitar / Vulnerable: CQV < 7.0, filtro severo activo, confianza Baja o datos críticos N/D.

ACTUALIZACIÓN DE ARCHIVOS SSOT

Actualiza solo después de validar todos los datos:
1. cqv_data.json (con "metodologia_version": "v5.0" y periodo "P[1-4] [AÑO]").
2. cqv_history.json (bloque organizado estrictamente en TICKER → AÑO → P1/P2/P3/P4).
3. Ejecuta la autoridad matemática:
   Para una acción: python sync_cqv.py --ticker [TICKER]
   Para varias acciones: python sync_cqv.py
4. Verifica la actualización automática de:
   - cqv_data.js
   - cqv_history.js
   - dashboard.html (inyección SSOT de métricas y tesis)
5. Genera o actualiza el informe trimestral en su subcarpeta por periodo:
   inform/cqv_v5/[AÑO] P[1-4]/[TICKER]_[AÑO]_P[1-4]_CQVv5.md
   Cumpliendo al 100% la estructura de 10 secciones de inform/template.md y el estándar de rigor FICO 2026 P3.

Estructura obligatoria de 10 secciones a partir de inform/template.md:
- Sección 1: Resumen Ejecutivo y Bloque de Salida Final CQV v5.0.
- Sección 2: Métricas y Puntuaciones en el Modelo CQV Calidad v5.0 (Tabla 2.1 de F1-F8).
- Sección 3: Análisis Detallado del Estado de Resultados (Periodo P[1-4] [AÑO] / Q[1-4] Fiscal [AÑO_FISCAL]):
  - Subsección 3.1: Tabla Comparativa de Resultados Periódicos (6 columnas estrictas con cifras trimestrales reales en \$M).
  - Subsección 3.2: Posicionamiento Competitivo y Matriz de Moat (rivales concretos con ticker y diagrama Mermaid).
  - Subsección 3.3: Eficiencia de Capital: ROIC, ROA/ROI y ROE (evaluación frente al WACC).
  - Subsección 3.4: Evolución Multianual y Diagnóstico de Tendencia (cifras numéricas FY-2, FY-1 y TTM).
  - Subsección 3.5: Guidance y Perspectivas Futuras para Próximos Periodos (proyecciones NTM, BPA forward y consenso Wall Street).
- Sección 4: Tesis de Inversión (Toro vs. Oso, Factores Adversos Actuales, Estrategias Defensivas y Líneas Rojas).
- Sección 5: Owner Earnings, FCF Yield y Desglose del Value Score v5.0.
- Sección 6: Valuación por Descuento de Flujos de Caja (DCF) y Sensibilidad Multiescenario.
- Sección 7: Registro Auditado de Riesgos y Preguntas Frecuentes (FAQs).
- Sección 8: Evolución Histórica de Puntuaciones CQV y Valuación por Periodos (P1–P4 desde 2020 con tabla de 13 columnas y gráfico Mermaid xychart-beta).
- Sección 9: Conclusión, Síntesis Estratégica y Veredicto Final Operativo v5.0.
- Sección 10: Auditoría, Observaciones y Recomendaciones del Analista / Auditor.

PASO ADICIONAL DE AUDITORÍA Y AUTO-CORRECCIÓN

1. Ejecución de verificación estructural: python scratch/verify_section8.py
2. Verificación de coherencia tridireccional: Los datos numéricos de precios, puntuaciones, BPA y márgenes deben coincidir al 100% entre cqv_data.json, cqv_history.json, cqv_data.js, dashboard.html y el informe Markdown.
3. Si detectas cualquier discrepancia numérica o desajuste de columnas en tablas Markdown, corrige y re-ejecuta python sync_cqv.py.

Entrega al final una tabla resumen:
Ticker | Periodo | Estado | CQV v5.0 | Value Score | Ratio Bruto | FCF Yield | MoS Base | Veredicto | Confianza | Fuentes
```

---

## Ejemplos de Invocación Correcta

### Ejemplo para una acción:
```text
Actualiza completamente FICO para P3 2026 (Q4 Fiscal 2026) bajo CQV v5.0 siguiendo estrictamente la norma de rigor analítico FICO 2026 P3 sin textos genéricos.
```

### Ejemplo para varias acciones:
```text
Actualiza completamente AAPL, PLTR y UBER para P3 2026 bajo CQV v5.0 siguiendo exactamente el protocolo anterior. Procesa las acciones de forma transaccional, con cifras trimestrales reales en millones de USD, análisis de competidores reales y estrategias de protección de moat.
```

---

### Estándar de Título de Informe Markdown:
Todo informe debe titularse obligatoriamente en su encabezado H1 con el periodo de presentación P1-P4 y el trimestre fiscal contable:
`# Informe de Tesis de Inversión: [Nombre de la Empresa] ([TICKER]) — P[1-4] [AÑO_CALENDARIO] (Q[1-4] Fiscal [AÑO_FISCAL])`

*Ruta y nombre de archivo oficial (organizado por subcarpeta de periodo):*  
`inform/cqv_v5/[AÑO_CALENDARIO] P[1-4]/[TICKER]_[AÑO_CALENDARIO]_P[1-4]_CQVv5.md`
