# Prompt maestro de actualización CQV v4.0

Utiliza este prompt para actualizar una o varias acciones bajo el flujo SSOT definido en `flujo_actualizacion_datos.md`.

## Prompt

```text
Actualiza completamente bajo la metodología CQV v4.0 las siguientes acciones:

[TICKER1], [TICKER2], [TICKER3]

Periodo de análisis: [Q? YEAR]
Fecha de valoración: [DD/MM/AAAA]

La fecha de valoración debe ser la fecha en la que se publicó el informe financiero o earnings release analizado (`publication_date`). El precio utilizado debe ser obligatoriamente el cierre de mercado de esa misma fecha (`price_date`) y del mismo mercado de cotización. Está estrictamente prohibido usar el precio o la capitalización actual para un informe histórico.

Aplica estrictamente:
- flujo_actualizacion_datos.md
- metodo_v4.0.md
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
   - SEC 10-Q/10-K o RNS.
   - Earnings release.
   - Presentaciones oficiales.
   - Guidance oficial.
   - Informe anual.
   - Datos de mercado fechados.
7. No reutilices datos de otro trimestre sin indicarlo expresamente.

8. Fecha histórica y precio de mercado (Anclaje Temporal Obligatorio):
   - Todo informe debe elaborarse congelado en la fecha exacta en la que se publicó el informe financiero o earnings release analizado (`publication_date`).
   - `valuation_date` debe coincidir exactamente con `publication_date`, salvo que se documente una razón operativa verificable.
   - `price_date` debe coincidir con `valuation_date` y el precio utilizado debe corresponder obligatoriamente al cierre del mercado de cotización de esa misma fecha.
   - Si la publicación ocurre fuera del horario de mercado, utiliza el cierre de esa misma sesión; si no hubo sesión, utiliza la sesión anterior y documenta el motivo.
   - Registra `price_source`, `price_market`, `price_currency` y la hora de publicación cuando esté disponible.
   - Para informes históricos está prohibido utilizar un precio actual o una capitalización actual.
   - Si no puede verificarse el precio de la fecha correcta, `price`, capitalización, PER, PEG, Value Score, MoS y veredicto dependientes deben quedar como `N/D`.

9. Historial trimestral obligatorio:
   - `cqv_history.json` debe organizarse como `TICKER → AÑO → Q1/Q2/Q3/Q4`.
   - La actualización solo puede añadir o corregir el trimestre solicitado.
   - Debe conservar los trimestres anteriores y no sobrescribirlos.
   - No conviertas una puntuación anual en una puntuación trimestral.
   - Si un trimestre no tiene evidencia verificable, registra `null`/`N/D`.
   - Los registros anuales antiguos, si existen, deben conservarse bajo `annual_legacy` y no utilizarse como sustituto de Q1-Q4.
   - Cada snapshot trimestral debe incluir, cuando existan, periodo, fecha de cierre, fecha de publicación, fecha de valoración, fecha del precio, F1-F8, CQV, valoración, fuentes y confianza.

DATOS A RECOPILAR PARA CADA ACCIÓN

A. Identificación:
- Ticker, nombre, sector, periodo, fecha de cierre fiscal, fecha de publicación, fecha de valoración y fecha del precio.

B. Resultados financieros:
- Ingresos.
- Beneficio operativo.
- Margen operativo.
- EBITDA, si procede.
- Beneficio neto GAAP.
- EPS GAAP y EPS normalizado.
- OCF.
- CapEx total y Maintenance CapEx.
- Free Cash Flow.
- Deuda, caja y deuda neta.
- Acciones diluidas.
- SBC y dilución neta.
- Recompras y dividendos.

C. Evolución histórica:
- Ingresos, EPS, márgenes, FCF, ROIC, ROA/ROI y ROE.
- CAGR de ingresos y EPS.
- Serie histórica 2020–2026 o el periodo disponible.
- Evolución histórica de las puntuaciones CQV.

D. Factores CQV v4.0:

Calcula y justifica F1-F8:

- F1: Economía del negocio y rentabilidad.
- F2: Solidez financiera.
- F3: Crecimiento durable.
- F4: Moat competitivo.
- F5: Asignación de capital.
- F6: Dirección, gobierno y ejecución.
- F7: Opcionalidad futura y disrupción.
- F8: Antifragilidad y recurrencia.

Cada factor debe incluir:
- Puntuación de 0 a 10.
- Subcomponentes evaluados.
- Evidencia cuantitativa o cualitativa.
- Fuente.
- Limitaciones.
- Nivel de confianza.

Calcula:

CQV =
F1×0.20 + F2×0.15 + F3×0.15 + F4×0.15
+ F5×0.10 + F6×0.10 + F7×0.05 + F8×0.10

Aplica los filtros rígidos de F2 y F4.

Clasificación CQV:
- ÉLITE: CQV ≥ 9.00 y F2, F4, F8 ≥ 7.0.
- ALTA CALIDAD: CQV 8.00–8.99.
- EN OBSERVACIÓN: CQV 7.00–7.99.
- VULNERABLE: CQV < 7.00 o activación de filtro severo.

Reglas de veredicto (CQV × Margen de Seguridad):
- CQV ≥ 9.00 y MoS ≥ 25%: Comprar / Candidato Prioritario.
- CQV ≥ 9.00 y MoS ≥ 18%: Comprar / Acumular.
- CQV ≥ 8.00 y MoS ≥ 10%: Acumular / Compra Escalonada.
- CQV ≥ 8.00 y MoS < 10%: Mantener.
- CQV < 8.00 o filtro rígido activo: Evitar / En Observación.
- Si CQV, MoS o un dato crítico es N/D, no se emite recomendación afirmativa.

E. Valoración:

Recopila:
- Precio de cierre de la fecha de valoración, no precio actual salvo que el informe sea del periodo actual.
- Fuente, mercado, moneda y fecha exacta del precio.
- PER Trailing.
- PER Forward.
- Crecimiento EPS NTM en puntos porcentuales.
- Capitalización bursátil.
- OCF.
- Maintenance CapEx.
- Valor intrínseco.
- WACC.
- Tasa terminal.
- Horizonte de proyección.
- Escenarios Bear, Base y Bull.

Calcula:

Owner Earnings = OCF - Maintenance CapEx

FCF Yield = (Owner Earnings / Capitalización bursátil) × 100

PEG Bruto =
(Crecimiento EPS NTM en puntos porcentuales / PER Forward) × 10

Score PEG =
min(10, max(0, PEG Bruto))

Margen de Seguridad =
(Valor Intrínseco - Precio Actual) / Valor Intrínseco × 100

Value Score =
0.40 × Score FCF Yield
+ 0.30 × Score PEG
+ 0.30 × Score Margen de Seguridad

El PEG Bruto puede superar 10, pero el Score PEG normalizado no puede superar 10.

No calcules el FCF Yield a partir del PER.

F. DCF y valoración por escenarios:

Incluye:
- Escenario pesimista.
- Escenario base.
- Escenario optimista.
- Sensibilidad con al menos tres WACC y tres tasas terminales.
- Expectativas implícitas del precio actual.
- Supuestos utilizados.
- Riesgos que puedan invalidar la valoración.

G. Registro de riesgos:

Para cada riesgo indica:
- Descripción.
- Probabilidad.
- Impacto.
- Mitigación.
- Riesgo residual.
- Fuente.

ACTUALIZACIÓN DE ARCHIVOS

Actualiza solo después de validar todos los datos:

1. cqv_data.json
2. cqv_history.json
3. Ejecuta:
    Para una acción: python sync_cqv.py --ticker [TICKER]`r`n    Para varias acciones: python sync_cqv.py
4. Verifica la actualización de:
   - cqv_data.js
   - cqv_history.js
   - dashboard.html

5. Genera o actualiza el informe trimestral a partir de `inform/template.md`, cumpliendo al 100% su formato en 10 secciones y siguiendo la convención estricta:
   - inform/[ACCION]_[AÑO]_[Q?].md  (Donde [ACCION] es el ticker en MAYÚSCULAS ej. MSFT, LIN, FICO, CPRT; [AÑO] es el año ej. 2026; y [Q?] es Q1, Q2, Q3 o Q4). Nunca usar el nombre de la empresa ni minúsculas.

El dashboard debe actualizarse exclusivamente desde el SSOT, incluyendo:
- window.companiesData
- window.cqvHistoryData
- let companies

No edites manualmente el dashboard.

La **Sección 8 del informe Markdown** y la sección **Tendencias del Dashboard** deben consumir exclusivamente `cqv_history.json` / `window.cqvHistoryData` y presentar el desglose trimestral de cuatro observaciones por año (`Q1`, `Q2`, `Q3`, `Q4`) cuando existan. Tanto la tabla de la Sección 8 como el gráfico Mermaid del informe deben desglosar cada trimestre disponible por año (ejemplo: `2025 Q1`, `2025 Q2`, `2025 Q3`, `2025 Q4`, `2026 Q1`, `2026 Q2`). Los trimestres sin snapshot deben aparecer como `N/D` o valor nulo, sin interpolación ni reutilización de datos anuales.

El informe final de cada acción debe estructurarse obligatoriamente en 10 secciones a partir de `inform/template.md`:
- Sección 1: Resumen Ejecutivo y Bloque de Salida 9.6.
- Sección 2: Métricas y Puntuaciones CQV Calidad v4.0 (con tabla 2.1 de F1-F8).
- Sección 3: Análisis del Estado de Resultados, Competidores y ROIC.
  - Subsección 3.4: Evolución Multianual y Diagnóstico de Tendencia (¿Mejorando o Empeorando?) — Comparativa cuantitativa/cualitativa de los últimos 3 ejercicios fiscales (FY-2, FY-1, FY) auditando Ingresos, Márgenes, EPS, FCF y ROIC con diagnósticos explícitos (🟢 Mejorando / 🟡 Estabilidad / 🔴 Empeorando).
  - Subsección 3.5: Guidance y Perspectivas Futuras para Próximos Periodos — Proyecciones oficiales de la compañía para el próximo ejercicio fiscal (FY+1), desglosadas por segmentos operativos y especificando cambios contables o estratégicos previstos.
- Sección 4: Tesis de Inversión (Escenarios Toro vs. Oso y Líneas Rojas).
- Sección 5: Owner Earnings, FCF Yield y Desglose del Value Score.
- Sección 6: Valuación por Descuento de Flujos de Caja (DCF) y Sensibilidad.
- Sección 7: Registro Auditado de Riesgos y Preguntas Frecuentes (FAQs).
- Sección 8: Evolución Histórica de Puntuaciones CQV y Valuación por Trimestres (Serie 2020 - Presente con gráfico Mermaid).
- Sección 9: Conclusión y Veredicto Final Operativo v4.0.
- Sección 10: Auditoría, Observaciones y Recomendaciones del Analista / Auditor (Matriz 10.1 de coherencia SSOT vs Informe, Registro 10.2 de correcciones/campos N/D, y Recomendaciones Operativas 10.3 para gestión de cartera).

PASO ADICIONAL DE AUDITORÍA Y AUTO-CORRECCIÓN

1. **Regla Rígida de Redondeo:** El CQV Calidad v4.0 debe redondearse estrictamente a dos decimales a partir del cálculo de la suma ponderada de F1-F8 (`round(sum(F_i * w_i), 2)`). `sync_cqv.py` es la autoridad matemática SSOT. Está prohibido incluir en el informe Markdown un valor distinto al generado por el script.
2. Ejecuta una auditoría matemática y de integridad entre SSOT JSON e Informe Markdown.
3. Si detectas cualquier discrepancia numérica o de redondeo, corrige de inmediato el informe Markdown y re-ejecuta `python sync_cqv.py --ticker [TICKER]` para garantizar coherencia del 100%.
4. Documenta en la Sección 10 las observaciones, correcciones realizadas, campos `N/D` y recomendaciones para la toma de decisiones.

VALIDACIÓN FINAL

Comprueba que coincidan exactamente entre JSON, JS, dashboard e informe:

- Fecha de publicación, fecha de valoración y fecha del precio.
- Mercado, moneda y fuente del precio histórico.
- Estructura trimestral `TICKER → AÑO → Q1/Q2/Q3/Q4`.
- Conservación de los trimestres históricos no actualizados.

- F1-F8.
- CQV.
- Precio.
- PER y PER Forward.
- PEG Bruto.
- Score PEG normalizado.
- Owner Earnings.
- FCF Yield.
- Value Score.
- Valor intrínseco.
- Margen de seguridad.
- Veredicto.
- Sección 10 de Auditoría y Recomendaciones completada.

Si una acción presenta errores, datos faltantes o discrepancias:

- No ocultes el problema.
- No inventes una cifra.
- Marca el campo como N/D.
- Auto-corrige cualquier discrepancia antes de finalizar.
- No emitas una recomendación afirmativa si faltan datos críticos.
- No realices una actualización parcial sin informarlo.

Entrega al final una tabla resumen:

Ticker | Estado | CQV | Value Score | PEG Bruto | Score PEG | FCF Yield | MoS | Veredicto | Confianza | Campos N/D | Fuentes principales
```

## Addendum obligatorio: uso de fuentes secundarias confiables

Cuando un dato no aparezca en los estados financieros, earnings release, presentacion oficial, guidance o filing regulatorio, se permite utilizar fuentes secundarias de buena reputacion para completar la recopilacion, siempre que se cumplan estas reglas:

1. Prioridad de fuentes

   - **Nivel 1 - Primarias:** SEC 10-Q/10-K, earnings release, presentaciones y guidance oficial.
   - **Nivel 2 - Datos de mercado y consenso reputados:** S&P Global Market Intelligence, FactSet, Refinitiv/LSEG, Bloomberg, Capital IQ, Nasdaq, NYSE y proveedores institucionales equivalentes.
   - **Nivel 3 - Fuentes financieras reputadas:** Morningstar, MarketBeat, StockAnalysis, Zacks, Yahoo Finance, Reuters y similares.
   - **Nivel 4 - Fuentes de apoyo:** prensa financiera reconocida, informes de universidades, brokers o casas de analisis con metodologia identificable.

   No utilizar blogs anonimos, foros, redes sociales, contenido generado automaticamente sin metodologia, paginas sin fecha o agregadores que no indiquen el origen del dato.

2. Reglas de trazabilidad

   Para cada dato secundario registrar obligatoriamente:

   - valor y unidad;
   - moneda;
   - periodo fiscal o fecha de mercado;
   - fecha de consulta y fecha de publicacion/actualizacion de la fuente;
   - nombre exacto del proveedor;
   - URL o referencia verificable;
   - si es dato reportado, estimacion de consenso, dato derivado o calculo propio;
   - limitaciones y posible desfase temporal.

3. Reconciliacion entre fuentes

   - Contrastar cada dato material con al menos dos fuentes cuando sea posible.
   - Si las fuentes difieren, no promediar automaticamente: explicar la diferencia metodologica y escoger la fuente mas cercana a la fecha de valoracion.
   - Para precios y capitalizacion, utilizar la misma fecha y mercado.
   - Para PER forward y crecimiento EPS, exigir el mismo horizonte NTM o indicar expresamente si se utiliza FY2026/FY2027.
   - No mezclar EPS GAAP con estimaciones ajustadas sin identificarlo.
   - Los datos secundarios nunca pueden sobrescribir silenciosamente un dato primario posterior.

4. Datos derivados permitidos

   Se pueden calcular datos derivados si las entradas estan documentadas. Ejemplos:

   - capitalizacion = precio x acciones en circulacion;
   - PER = precio / EPS;
   - PEG = crecimiento EPS en puntos porcentuales / PER forward x 10;
   - deuda neta = deuda total - caja y equivalentes;
   - margen operativo = beneficio operativo / ingresos.

   Marcar siempre el resultado como **calculado**, conservar las entradas y no presentarlo como cifra reportada por la empresa.

5. Maintenance CapEx y Owner Earnings

   Si la empresa no desglosa maintenance capex, buscar en este orden:

   - disclosure oficial de CapEx de mantenimiento;
   - presentaciones de inversores o notas de analistas con metodologia explicita;
   - estimacion de consenso de proveedores institucionales;
   - informe sectorial reputado con una metodologia reproducible.

   Si solo existe una estimacion secundaria, registrarla como **estimacion**, indicar su rango y ejecutar sensibilidad. No usar automaticamente CapEx total como maintenance capex. Si no existe una estimacion defendible, dejar Owner Earnings, FCF Yield y Value Score como N/D.

6. DCF con datos secundarios

   Se permite obtener de fuentes secundarias el WACC, beta, prima de riesgo, tasa libre de riesgo, crecimiento terminal y consenso de FCFF, pero cada entrada debe indicar proveedor, fecha y metodologia. Presentar al menos tres escenarios y una sensibilidad. Si el DCF depende principalmente de estimaciones secundarias o de una sola fuente, la confianza maxima de la valoracion sera **Media**.

7. Regla de confianza

   - Datos primarios corroborados: confianza Alta.
   - Datos primarios combinados con consenso secundario reputado: confianza Media-Alta.
   - Valoracion basada principalmente en fuentes secundarias: confianza Media o Baja.
   - Si un dato critico solo esta disponible en una fuente secundaria no verificable, marcar N/D.

8. Seccion obligatoria del informe

   Añadir una tabla **Fuentes secundarias y datos complementarios** con estas columnas:

   `Dato | Valor | Fuente | Fecha/periodo | Tipo (reportado/estimado/calculado) | Concordancia | Limitacion | Confianza`

   La Seccion 10 debe indicar que campos fueron completados mediante fuentes secundarias, cuales permanecen N/D y como cambia esto la confianza y el veredicto.

## Ejemplo para una acción

```text
Actualiza completamente MSFT para Q2 2026 bajo CQV v4.0 siguiendo exactamente el protocolo anterior.
```

## Ejemplo para varias acciones

```text
Actualiza completamente FICO, MSCI y MSFT para Q2 2026 bajo CQV v4.0 siguiendo exactamente el protocolo anterior. Procesa las acciones de forma transaccional y no publiques cambios parciales si alguna falla la validación.
```
