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
- **Ruta y sufijo del informe Markdown:** `inform/cqv_v5/[TICKER]_[AÑO]_P[1-4]_CQVv5.md` (donde `[TICKER]` va en MAYÚSCULAS, `[AÑO]` es el año calendario y `P[1-4]` es el ciclo de presentación).

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

OBJETIVO

Recopila toda la información financiera, operativa, competitiva y de valoración necesaria. Actualiza el SSOT, sincroniza los archivos derivados, el dashboard y los informes Markdown.

REGLAS OBLIGATORIAS

1. No inventes ningún dato.
2. No utilices valores por defecto.
3. No completes campos faltantes mediante estimaciones no identificadas.
4. Si un dato no está disponible o no puede verificarse, utiliza N/D, indica el motivo y explica su impacto.
5. Registra para cada cifra la fuente, fecha, periodo y unidad.
6. Utiliza preferentemente fuentes primarias:
   - SEC 10-Q/10-K, 6-K o RNS.
   - Earnings release oficial.
   - Presentaciones oficiales para inversores.
   - Guidance oficial.
   - Informe anual.
   - Datos de mercado fechados al día de publicación.
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

DATOS A RECOPILAR PARA CADA ACCIÓN

A. Identificación:
- Ticker, nombre, sector, periodo (P1-P4), fecha de cierre fiscal, fecha de publicación, fecha de valoración y fecha del precio.

B. Resultados financieros:
- Ingresos consolidados.
- Beneficio operativo (EBIT).
- Margen operativo.
- EBITDA, si procede.
- Beneficio neto GAAP y Non-GAAP.
- EPS GAAP diluido y EPS normalizado.
- Flujo de caja operativo (OCF).
- CapEx total y Maintenance CapEx.
- Free Cash Flow (FCF).
- Deuda bruta, caja/equivalentes y deuda neta.
- Acciones diluidas en circulación.
- Stock-Based Compensation (SBC) y dilución neta.
- Recompras de acciones y dividendos.

C. Evolución histórica:
- Ingresos, EPS, márgenes, FCF, ROIC, ROA/ROI y ROE.
- CAGR de ingresos y EPS (3 y 5 años).
- Serie histórica 2020–2026 por periodos P1–P4.
- Evolución histórica de las puntuaciones CQV v5.0.

D. Factores CQV v5.0:

Calcula y justifica F1-F8 conforme a metodo_v5.0.md:

- F1: Economía del negocio y rentabilidad (Margen, ROIC, Conversión de caja). Peso: 20%.
- F2: Solidez financiera (Apalancamiento, Cobertura, Liquidez, Refinanciación, Estrés). Peso: 15%.
- F3: Crecimiento durable (Ingresos, EPS, Retención/Precio, Dilución neta). Peso: 15%.
- F4: Moat competitivo (Switching costs, Efecto red/Datos/IP, Retornos vs pares, Durabilidad). Peso: 15%.
- F5: Asignación de capital (ROIC incremental vs WACC, Recompras, M&A, Balance). Peso: 10%.
- F6: Dirección, gobierno y ejecución (Cumplimiento de guías, Transparencia, Incentivos, Ejecución). Peso: 10%.
- F7: Opcionalidad futura y disrupción (Oportunidades comprobables, Adaptación a IA). Peso: 5%.
- F8: Resiliencia operativa (Recurrencia contractual, Ciclicidad, Diversificación, Flexibilidad). Peso: 10%.

Cada factor debe incluir:
- Puntuación de 1.0 a 10.0 (o N/D).
- Subcomponentes evaluados.
- Evidencia cuantitativa y cualitativa.
- Fuente primaria.
- Limitaciones y nivel de confianza.

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

Recopila:
- Precio de cierre de la fecha de valoración (price_date = publication_date).
- Fuente, mercado, moneda y fecha exacta del precio.
- PER Trailing.
- PER Forward NTM.
- Crecimiento EPS NTM en porcentaje (%).
- Capitalización bursátil (precio × acciones diluidas).
- OCF TTM y Maintenance CapEx TTM.
- Valor intrínseco DCF base y esperado.
- WACC y tasa terminal (g).
- Escenarios Bear, Base y Bull.

Fórmulas de Valoración CQV v5.0:
- Owner Earnings = OCF - Maintenance CapEx
- FCF Yield Real (%) = (Owner Earnings / Capitalización bursátil) × 100
- Score FCF Yield: escala 1.0–10.0 según percentil sectorial (≥8.0% en software = 10.0).
- Ratio Crecimiento / Múltiplo Bruto = (Crecimiento EPS NTM (%) / PER Forward) × 10
- Score Crecimiento / Múltiplo Normalizado = min(10.0, max(1.0, Ratio Bruto))
  (Si Crecimiento EPS NTM ≤ 0 o PER Forward ≤ 0, el score es N/D, no cero).
- Margen de Seguridad (%) = (Valor Intrínseco Base - Precio) / Valor Intrínseco Base × 100
- Score Margen de Seguridad: escala 1.0–10.0 (MoS ≥ 30% = 9.0–10.0).

Ecuación Consolidada del Value Score v5.0:
Value Score v5.0 = 0.40 × Score FCF Yield + 0.30 × Score Crecimiento/Múltiplo + 0.30 × Score MoS
(En v5.0, si falta un componente, los pesos se reponderan proporcionalmente entre los componentes disponibles).

Reglas de Veredicto v5.0 (Sección 7 de metodo_v5.0.md):
- Comprar / Revisar Compra: CQV ≥ 8.0, confianza Alta/Media, F2 y F8 disponibles, MoS esperado ≥ 20%, MoS base ≥ 10%, Value Score ≥ 6.0.
- Acumular: CQV ≥ 8.0, confianza Alta/Media, MoS esperado ≥ 10%, Value Score ≥ 5.0.
- Mantener: CQV ≥ 8.0, pero MoS esperado < 10% o supuestos implícitos exigentes.
- Evitar / Vulnerable: CQV < 7.0, filtro severo activo, confianza Baja o datos críticos N/D.

F. DCF y Valoración por Escenarios:
- Escenario pesimista (Bear: 20-25% probabilidad).
- Escenario base (Base: 50-60% probabilidad).
- Escenario optimista (Bull: 20-25% probabilidad).
- Matriz de sensibilidad bidimensional (WACC vs g de al menos 3x3).
- Expectativas implícitas del precio de mercado (Reverse DCF).

G. Registro de Riesgos:
- ID, descripción, probabilidad (0-1), impacto (1-5), mitigación (0-1), riesgo residual y fuente.

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
   - dashboard.html (inyección SSOT)
5. Genera o actualiza el informe trimestral en:
   inform/cqv_v5/[TICKER]_[AÑO]_P[1-4]_CQVv5.md
   Cumpliendo al 100% la estructura de 10 secciones de inform/template.md.

La Sección 8 del informe Markdown y la sección Tendencias del Dashboard deben consumir exclusivamente cqv_history.json / window.cqvHistoryData y presentar el desglose por periodos de presentación (P1, P2, P3, P4) para cada año registrado. Los periodos sin snapshot deben aparecer como null / N/D, sin interpolación ni reutilización de datos anuales.

Estructura obligatoria de 10 secciones a partir de inform/template.md:
- Sección 1: Resumen Ejecutivo y Bloque de Salida Final CQV v5.0 (Sección 7.1 / 9.6).
- Sección 2: Métricas y Puntuaciones en el Modelo CQV Calidad v5.0 (Tabla 2.1 de F1-F8).
- Sección 3: Análisis Detallado del Estado de Resultados (Periodo P[1-4] [AÑO_CALENDARIO] / Q[1-4] Fiscal [AÑO_FISCAL]).
  - Subsección 3.4: Evolución Multianual y Diagnóstico de Tendencia (¿Mejorando o Empeorando?).
  - Subsección 3.5: Guidance y Perspectivas Futuras para Próximos Periodos.
- Sección 4: Tesis de Inversión (Toro vs. Oso y Líneas Rojas).
- Sección 5: Owner Earnings, FCF Yield y Desglose del Value Score v5.0.
- Sección 6: Valuación por Descuento de Flujos de Caja (DCF) y Sensibilidad.
- Sección 7: Registro Auditado de Riesgos y Preguntas Frecuentes (FAQs).
- Sección 8: Evolución Histórica de Puntuaciones CQV y Valuación por Periodos (P1–P4 desde 2020 con gráfico Mermaid).
- Sección 9: Conclusión y Veredicto Final Operativo v5.0.
- Sección 10: Auditoría, Observaciones y Recomendaciones del Analista / Auditor.

PASO ADICIONAL DE AUDITORÍA Y AUTO-CORRECCIÓN

1. Regla Rígida de Redondeo: El CQV Calidad v5.0 debe redondearse estrictamente a dos decimales a partir de la suma ponderada de F1-F8 (round(sum(F_i * w_i), 2)). sync_cqv.py es la autoridad matemática SSOT.
2. Ejecuta auditoría de coherencia entre SSOT JSON e Informe Markdown.
3. Si detectas cualquier discrepancia numérica, corrige el informe Markdown y re-ejecuta python sync_cqv.py --ticker [TICKER].
4. Documenta en la Sección 10 las observaciones, correcciones realizadas, campos N/D y recomendaciones para gestión de cartera.

Entrega al final una tabla resumen:
Ticker | Periodo | Estado | CQV v5.0 | Value Score | Ratio Bruto | FCF Yield | MoS Base | Veredicto | Confianza | Fuentes
```

---

## Ejemplos de Invocación Correcta

### Ejemplo para una acción:
```text
Actualiza completamente MSFT para P2 2026 (Q4 Fiscal 2026) bajo CQV v5.0 siguiendo exactamente el protocolo anterior.
```

### Ejemplo para varias acciones:
```text
Actualiza completamente FICO, CPRT y ORCL para P2 2026 bajo CQV v5.0 siguiendo exactamente el protocolo anterior. Procesa las acciones de forma transaccional y no publiques cambios parciales si alguna falla la validación.
```

---

### Estándar de Título de Informe Markdown:
Todo informe debe titularse obligatoriamente en su encabezado H1 con el periodo de presentación P1-P4 y el trimestre fiscal contable:
`# Informe de Tesis de Inversión: [Nombre de la Empresa] ([TICKER]) — P[1-4] [AÑO_CALENDARIO] (Q[1-4] Fiscal [AÑO_FISCAL])`

*Ruta y nombre de archivo oficial:*  
`inform/cqv_v5/[TICKER]_[AÑO_CALENDARIO]_P[1-4]_CQVv5.md`