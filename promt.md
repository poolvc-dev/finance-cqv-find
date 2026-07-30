# Prompt maestro de actualización CQV v4.0

Utiliza este prompt para actualizar una o varias acciones bajo el flujo SSOT definido en `flujo_actualizacion_datos.md`.

## Prompt

```text
Actualiza completamente bajo la metodología CQV v4.0 las siguientes acciones:

[TICKER1], [TICKER2], [TICKER3]

Periodo de análisis: [Q2 2026]
Fecha de valoración: [DD/MM/AAAA]

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

DATOS A RECOPILAR PARA CADA ACCIÓN

A. Identificación:
- Ticker, nombre, sector, periodo y fecha de valoración.

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

E. Valoración:

Recopila:
- Precio actual.
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

FCF Yield = Owner Earnings / Capitalización bursátil

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

   python sync_cqv.py

4. Verifica la actualización de:
   - cqv_data.js
   - cqv_history.js
   - dashboard.html

5. Genera o actualiza:
   - inform/[ticker]_[periodo].md

El dashboard debe actualizarse exclusivamente desde el SSOT, incluyendo:
- window.companiesData
- window.cqvHistoryData
- let companies

No edites manualmente el dashboard.

INFORME FINAL

Cada informe debe incluir:
- Resumen ejecutivo.
- Bloque de salida 9.6.
- CQV Calidad.
- Value Score.
- PEG Bruto.
- Score PEG normalizado.
- Owner Earnings.
- FCF Yield.
- Desglose completo del Value Score.
- Justificación de F1-F8.
- Resultados financieros.
- DCF por escenarios.
- Sensibilidad.
- Registro de riesgos.
- Fuentes.
- Nivel de confianza.
- Veredicto final.

VALIDACIÓN FINAL

Comprueba que coincidan exactamente entre JSON, JS, dashboard e informe:

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

Si una acción presenta errores, datos faltantes o discrepancias:

- No ocultes el problema.
- No inventes una cifra.
- Marca el campo como N/D.
- No emitas una recomendación afirmativa.
- No realices una actualización parcial sin informarlo.

Entrega al final una tabla resumen:

Ticker | Estado | CQV | Value Score | PEG Bruto | Score PEG | FCF Yield | MoS | Veredicto | Confianza | Campos N/D | Fuentes principales
```

## Ejemplo para una acción

```text
Actualiza completamente MSFT para Q2 2026 bajo CQV v4.0 siguiendo exactamente el protocolo anterior.
```

## Ejemplo para varias acciones

```text
Actualiza completamente FICO, MSCI y MSFT para Q2 2026 bajo CQV v4.0 siguiendo exactamente el protocolo anterior. Procesa las acciones de forma transaccional y no publiques cambios parciales si alguna falla la validación.
```
