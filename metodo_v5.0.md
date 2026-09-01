# Manual Metodológico CQV v5.0
## Estándar operativo de Calidad, Resiliencia y Valor

CQV v5.0 evalúa separadamente la **calidad económica de una empresa** y el **atractivo de su precio**. Su propósito es priorizar investigación fundamental reproducible; no emitir órdenes automáticas de compra. Sustituye v4.0 para informes nuevos. Las puntuaciones de versiones anteriores se conservan, pero no son comparables directamente con v5.0.

---

## 1. Principios obligatorios

1. Todo dato debe poder reconstruirse con valor bruto, unidad, periodo fiscal, fecha de publicación, fuente y fórmula.
2. Cada informe queda congelado en `publication_date`: se usa exclusivamente el cierre de mercado de esa fecha como `price_date` y `valuation_date`. Nunca se mezcla un resultado histórico con precio, capitalización o consenso actuales.
3. Se usan tendencias de 3–5 años y LTM; un trimestre no determina por sí solo una puntuación extrema.
4. No se imputa una puntuación positiva ante datos críticos ausentes. Un dato no disponible se registra como `N/D`, con motivo y efecto.
5. Los umbrales se aplican contra comparables del mismo sector y modelo económico. No se fuerza deuda/EBITDA, ROIC industrial ni FCFF a bancos, aseguradoras o REIT.
6. Calidad, valoración, confianza y riesgo se muestran por separado. Una valoración barata no compensa mala calidad, y una gran empresa no justifica cualquier precio.
7. Se puntúan atributos económicos una sola vez: cada submétrica tiene un factor propietario para evitar doble conteo.

La escala de todos los scores es 1.0–10.0 salvo que se indique `N/D`. Los pesos suman 100%.

---

## 2. Ecuación de calidad CQV

$$CQV = 0.20F_1 + 0.15F_2 + 0.15F_3 + 0.15F_4 + 0.10F_5 + 0.10F_6 + 0.05F_7 + 0.10F_8$$

| Factor | Concepto | Peso | Propietario del atributo |
| :--- | :--- | ---: | :--- |
| F1 | Economía y rentabilidad | 20% | margen, retornos y conversión de caja |
| F2 | Solidez financiera | 15% | deuda, liquidez y refinanciación |
| F3 | Crecimiento durable | 15% | crecimiento, precio/retención y dilución |
| F4 | Moat competitivo | 15% | evidencia de ventaja y durabilidad |
| F5 | Asignación de capital | 10% | reinversión y distribución de capital |
| F6 | Dirección y gobierno | 10% | ejecución, incentivos y transparencia |
| F7 | Opcionalidad y disrupción | 5% | oportunidades incrementales y adaptación |
| F8 | Resiliencia operativa | 10% | concentración, ciclicidad y flexibilidad |

---

## 3. Datos, comparables y puntuación

### 3.1 Ventanas de medición

- Ingresos, EPS y acciones: CAGR de 3 y 5 años cuando existan, contrastado con LTM.
- Márgenes, retornos, conversión de caja y apalancamiento: mediana de los últimos tres ejercicios completos; LTM se informa aparte.
- Métricas con volatilidad extraordinaria: se muestra rango y explicación, sin eliminar años desfavorables salvo ajuste contable claramente documentado.
- Todos los importes conservan moneda, unidades, periodo fiscal, fecha de corte y enlace o referencia de la fuente primaria. Las fuentes secundarias se etiquetan como tales.

### 3.1.1 Norma de Periodización P1 - P4 por Ventana de Publicación

La nominación de periodos (P1 - P4) en la metodología CQV se rige estrictamente por la **ventana del año calendario en que la empresa emite la presentación de resultados**, independientemente de las variaciones del año fiscal de cada compañía:

- **P1**: Presentación emitida entre **Abril y Junio** (Mayo - Junio; 1er trimestre presentado en el año).
- **P2**: Presentación emitida entre **Julio y Septiembre** (Julio - Agosto; 2º trimestre / mitad del año).
- **P3**: Presentación emitida entre **Octubre y Diciembre** (Octubre - Noviembre; 3er trimestre del año).
- **P4**: Presentación emitida entre **Enero y Marzo del año siguiente** (4º trimestre / cierre del ejercicio previo).

### 3.2 Grupos comparables y percentiles

Antes de puntuar se asigna una taxonomía: software/servicios recurrentes, consumo defensivo, industrial/cíclico, energía/materiales, salud, financiero, inmobiliario u otra justificada. Se documentan entre 8 y 25 pares cotizados comparables, país o región, fecha, fuente y exclusiones.

Para métricas cuantitativas, salvo una rúbrica específica, se usa percentil sectorial de cinco años:

| Percentil favorable | Score |
| :--- | ---: |
| ≥90 | 10.0 |
| 75–89 | 8.5 |
| 60–74 | 7.0 |
| 40–59 | 5.5 |
| 25–39 | 4.0 |
| <25 | 2.0 |

El analista puede ajustar como máximo ±1.0 punto si existe una diferencia estructural demostrable. Debe indicar métrica, evidencia, ajuste y aprobador. No se promedian empresas de sectores distintos para fabricar un percentil.

### 3.3 Confianza de datos

Cada submétrica recibe una confianza: **Alta** (fuente primaria, cálculo reproducible y serie ≥3 años), **Media** (una estimación razonable o serie incompleta) o **Baja** (estimación material, fuente secundaria no verificable o comparables débiles). La confianza de cada factor es la menor de sus submétricas críticas. La confianza global es la menor de F1, F2, F3 y F8; en ausencia de una métrica crítica, es la media ponderada de los ocho factores.

Si F2 o F8 es `N/D`, el CQV y cualquier veredicto de compra son `N/D`. Si la confianza global es Baja, toda conclusión se etiqueta como provisional.

---

## 4. Puntuación de calidad

### F1. Economía y rentabilidad — 20%

$$F_1 = 0.35S_{margen} + 0.40S_{ROIC} + 0.25S_{caja}$$

- **Margen:** margen operativo normalizado; EBITDA solo si representa mejor la economía sectorial. Se compara nivel y estabilidad, no expansión puntual.
- **ROIC:** $NOPAT / capital\ invertido\ neto$, usando mediana trianual y ROIC incremental cuando sea posible. Si el capital invertido neto es ≤0, el ROIC es `N/D`; se documenta un retorno alternativo sectorial, sin asignar 10.0 por denominador negativo.
- **Conversión de caja:** mediana de $FCF/NOPAT$ y $FCF/EBIT(1-t)$, con explicación de capital circulante, CapEx de crecimiento y pagos extraordinarios. No se usa $FCF/beneficio\ neto$ como único indicador.

### F2. Solidez financiera — 15%

$$F_2 = 0.30S_{apalancamiento} + 0.20S_{cobertura} + 0.20S_{liquidez} + 0.20S_{refinanciacion} + 0.10S_{estres}$$

- **Apalancamiento:** deuda neta/EBITDA, deuda/FCF o métrica sectorial equivalente.
- **Cobertura:** EBITDA/intereses, EBIT/intereses o cobertura financiera equivalente.
- **Liquidez:** caja, líneas comprometidas, capital circulante y obligaciones próximas.
- **Refinanciación:** calendario anual de vencimientos, tipo fijo/variable, covenants y acceso demostrado a mercados. Puntúa por capacidad, no por ausencia nominal de deuda.
- **Estrés:** cobertura y liquidez bajo una caída documentada de EBIT/FCF coherente con el peor ciclo histórico o el percentil 25 sectorial.

Para bancos se usan CET1, liquidez, calidad crediticia, reservas, financiación y sensibilidad a depósitos; para aseguradoras, solvencia, reservas, combinado y duración; para REIT, deuda/EBITDAre, vencimientos, cobertura y AFFO. El patrimonio negativo exige evidencia acumulada de FCF positivo, cobertura y vencimientos manejables; no activa una excepción automática.

### F3. Crecimiento durable — 15%

$$F_3 = 0.35S_{ingresos} + 0.20S_{EPS} + 0.25S_{retencion\ y\ precio} + 0.20S_{dilucion}$$

- **Ingresos:** CAGR 3/5 años, calidad orgánica frente a adquisiciones y contraste LTM.
- **EPS:** crecimiento normalizado por partidas no recurrentes, recompras y cambios contables.
- **Retención y precio:** NRR, churn, renovación, volumen/precio o evolución de margen, según sector. La falta de una métrica directa requiere evidencia alternativa concreta.
- **Dilución:** variación neta de acciones diluidas a tres años, incluyendo SBC y recompras. Se puntúa la reducción o contención neta, no el tamaño de recompras brutas.

### F4. Moat competitivo — 15%

$$F_4 = 0.30S_{switching} + 0.25S_{red\ datos\ IP} + 0.25S_{retornos\ frente\ a\ pares} + 0.20S_{durabilidad}$$

La puntuación necesita al menos dos piezas de evidencia cuantitativa y una cualitativa. Cuota de mercado aislada no es moat.

| Score | Evidencia mínima |
| :--- | :--- |
| 9.0–10.0 | estándar regulatorio o de facto, sustitución muy costosa y retornos persistentemente superiores a pares durante ≥5 años |
| 7.0–8.9 | ventaja defendible con retención, poder de precio o retornos superiores durante ≥3 años |
| 4.0–6.9 | ventaja local, temporal o con rivales relevantes erosionándola |
| 1.0–3.9 | producto sustituible, retornos no superiores o competencia basada en precio |

### F5. Asignación y reinversión de capital — 10%

$$F_5 = 0.45S_{ROIC\ incremental} + 0.25S_{recompras} + 0.20S_{M\&A} + 0.10S_{balance\ y\ distribucion}$$

La reinversión se compara contra WACC por proyectos, periodos o cohortes. Las recompras requieren reducción neta de acciones y una valoración razonable frente al valor intrínseco estimado en su fecha. M&A se evalúa con precio, integración, retorno posterior y goodwill/deterioro; sin evidencia suficiente recibe 5.0 como neutral, no una nota positiva. Dividendos o reducción de deuda no compensan destrucción de valor operativo.

### F6. Dirección, gobierno y ejecución — 10%

$$F_6 = 0.30S_{cumplimiento} + 0.25S_{transparencia} + 0.20S_{incentivos} + 0.25S_{ejecucion}$$

| Score | Rúbrica |
| :--- | :--- |
| 9.0–10.0 | guía históricamente fiable, comunicación completa, incentivos ligados a valor por acción y capital bien asignado |
| 7.0–8.9 | ejecución buena con desviaciones menores y gobierno adecuado |
| 4.0–6.9 | objetivos incumplidos repetidamente, divulgación incompleta o incentivos solo parcialmente alineados |
| 1.0–3.9 | opacidad, conflictos, remuneración desalineada, sanciones o destrucción de valor recurrente |

Se citan guías históricas, operaciones de insiders, remuneración, independencia del consejo y decisiones de capital. No existe puntuación base por defecto.

### F7. Opcionalidad y disrupción — 5%

$$F_7 = 0.50S_{oportunidad} + 0.50S_{adaptacion}$$

Una oportunidad requiere monetización o adopción observable, inversión financiable y ventaja verificable. La adaptación requiere evidencia de sustitutos, costes de cambio y respuesta de producto. Narrativas de IA o TAM sin evidencia no puntúan por encima de 5.0.

### F8. Resiliencia operativa — 10%

$$F_8 = 0.30S_{recurrencia} + 0.25S_{ciclicidad} + 0.25S_{diversificacion} + 0.20S_{flexibilidad}$$

- **Recurrencia:** proporción verificable de ingresos contractuales, repetitivos o de reposición; no se vuelve a puntuar estabilidad de FCF.
- **Ciclicidad:** caída histórica de ingresos, margen y FCF en la peor desaceleración relevante.
- **Diversificación:** concentración de clientes, productos, geografías, proveedores y reguladores.
- **Flexibilidad:** costes fijos/variables, capacidad de reducir CapEx/opex sin deterioro permanente y liquidez operativa.

Una empresa no obtiene más de 8.0 por recurrencia si un cliente representa >20% de los ingresos o si su flujo depende de un único producto sin sustituto financiero demostrado.

---

## 5. Filtros y clasificación de calidad

- Si F2 <4.0 o F4 <4.0, el CQV máximo publicado es 6.99.
- Si el escenario de estrés de F2 revela incumplimiento probable de covenants, vencimiento no financiable o liquidez insuficiente, se activa la bandera de estrés severo (`severe_stress_flag` / `f2_stress_flag`: true en el SSOT). Esto captea el CQV en máximo 6.99 y clasifica el negocio como **Vulnerable** con veredicto **Evitar / Filtro de Estrés F2 Activo**, independientemente del promedio.
- Si F2 o F8 es `N/D`, CQV = `N/D`.

| Clasificación | Condición |
| :--- | :--- |
| **Élite Suprema** | CQV ≥9.50 y F2, F4 y F8 ≥7.0 |
| **Élite** | CQV 9.00–9.49 y F2, F4 y F8 ≥7.0 |
| **Alta calidad** | 8.00–8.99 |
| **En observación** | 7.00–7.99 |
| **Vulnerable** | <7.00 o filtro de estrés severo activo |

### 5.1 Matriz de decisión de dos ejes

La señal de inversión se interpreta cruzando calidad y valoración. Ningún cuadrante genera una orden automática:

| Calidad CQV | Value Score | Señal |
|---|---|---|
| Alta (≥8.0) | Alta (≥6.0) | Candidato prioritario para revisión |
| Alta (≥8.0) | Baja (<6.0) | Empresa excelente, precio exigente |
| Baja (<8.0) | Alta (≥6.0) | Posible trampa de valor |
| Baja (<8.0) | Baja (<6.0) | Evitar o mantener fuera de cartera |

La señal final debe incluir CQV de calidad, Value Score, confianza de ambos, fecha de datos, riesgos principales y margen de seguridad.

---

## 6. Valoración intrínseca y Value Score

La valoración es independiente del CQV. Todo veredicto de inversión usa el precio de `valuation_date`, no el precio actual si es una revisión histórica.

### 6.1 Modelos por sector

Para empresas no financieras:

$$FCFF = EBIT(1-t) + D\&A - CapEx - \Delta NWC$$
$$EV = \sum_{t=1}^{n}\frac{FCFF_t}{(1+WACC)^t} + \frac{TV}{(1+WACC)^n}$$
$$TV = \frac{FCFF_{n+1}}{WACC-g}, \quad g < WACC$$

$$Valor\ Equity = EV - Deuda\ Neta + Activos\ No\ Operativos$$
$$Valor\ por\ Acción = Valor\ Equity / Acciones\ Diluídas$$

Para bancos, aseguradoras y REIT se emplean dividend discount, excess returns, P/B ajustado, FFO/AFFO u otro modelo sectorial documentado. Nunca se fuerza un FCFF industrial.

Cada DCF muestra explícitamente: periodo de proyección, ingresos, margen, impuestos, reinversión, WACC, crecimiento terminal, valor terminal/EV, deuda neta, acciones diluidas y conciliación con múltiplos históricos y pares. Si el valor terminal supera 75% de EV, la confianza de valoración no puede ser Alta sin una justificación específica.

### 6.2 Escenarios, sensibilidad y expectativas implícitas

Se presentan escenarios pesimista, base y optimista. Sus probabilidades suman 100%; las bandas orientativas son 20–30%, 40–60% y 20–30%, respectivamente. Si el riesgo es claramente asimétrico se permite salir de las bandas, con evidencia y aprobación explícitas.

Se incluye una matriz de, como mínimo, 3×3 entre WACC y crecimiento terminal, y sensibilidades de margen y crecimiento cuando sean materiales. También se calcula qué crecimiento, margen y duración de crecimiento descuenta el precio; si esos supuestos superan el escenario optimista, se registra como advertencia de valoración.

### 6.3 Value Score

$$Value\ Score = 0.40S_{FCF\ yield} + 0.30S_{crecimiento/multiplo} + 0.30S_{MoS}$$

$$Owner\ Earnings = OCF - Maintenance\ CapEx$$
$$FCF\ Yield = Owner\ Earnings / Capitalizacion\ Bursatil$$
$$MoS = (Valor\ Intrinseco - Precio) / Valor\ Intrinseco$$

El antiguo nombre “PEG invertido” se sustituye por **Score crecimiento/múltiplo**. Usa crecimiento de EPS NTM consensuado y PER Forward NTM del mismo proveedor y fecha. Se registra el valor bruto $Ratio\ Bruto = (Crecimiento\ EPS\ NTM\ (\%)/PER\ Forward) \times 10$. 
Si crecimiento ≤0, PER ≤0 o falta uno de los dos datos, el score es `N/D` (no cero). 
El cálculo matemático base normalizado del pipeline SSOT se obtiene mediante:

$$Score\ Crecimiento/Múltiplo = \min\left(10.0, \max\left(1.0, \left(\frac{\text{Crecimiento EPS NTM (\%)}}{\text{PER Forward}}\right) \times 10\right)\right)$$

Cuando se disponga de un dataset suficiente de pares sectoriales (8 a 25 empresas cotizadas), el score se normaliza mediante la rúbrica de percentiles sectoriales de la Sección 3.2. En todos los casos el score queda acotado a 1.0–10.0 y no sustituye al modelo de valoración DCF.

Maintenance CapEx debe derivarse de divulgación de la empresa, activos/vida útil, o una estimación claramente marcada. Si no es fiable, FCF Yield es `N/D` y la confianza del Value Score no puede ser Alta. El Value Score se calcula con los componentes disponibles reponderados, pero el informe debe señalar el componente ausente; un veredicto Comprar exige al menos dos componentes y DCF por escenarios.

---

## 7. Riesgo y decisión

Cada riesgo se registra con probabilidad (0–1), impacto (1–5), mitigación (0–1), indicador adelantado y responsable de seguimiento:

$$Riesgo\ Ajustado = Probabilidad \times Impacto \times (1-\text{Mitigación})$$

Se revisan como mínimo regulación, sustitución tecnológica, concentración, macroeconomía, refinanciación, ejecución y dependencia de estimaciones o guías.

| Señal | Requisito mínimo |
| :--- | :--- |
| Comprar / Revisar compra | CQV ≥8.0, confianza Alta/Media, F2 y F8 disponibles, valor esperado con MoS ≥20%, escenario base con MoS ≥10%, y Value Score ≥6.0 |
| Acumular | CQV ≥8.0, confianza Alta/Media, MoS esperado ≥10% y Value Score ≥5.0 |
| Mantener | CQV ≥8.0, pero MoS esperado <10% o precio exige supuestos exigentes |
| Evitar | CQV <7.0, filtro severo, confianza Baja, datos críticos `N/D` o valoración dependiente del escenario optimista |

Los umbrales son puntos de partida y pueden modificarse solo mediante una excepción escrita que indique causa, riesgo y aprobación. Ninguna señal sustituye límites de cartera, liquidez del valor o idoneidad del inversor.

### 7.1 Salida final obligatoria

El resultado final de cada informe debe mostrar separadamente, con este formato exacto:

```text
CQV Calidad:          X.XX / 10
Value Score:          X.XX / 10
Valor Intrínseco:     $X.XX por acción
Precio Actual:        $X.XX
Margen de Seguridad:  X.X%
Confianza:            Alta / Media / Baja
Metodología:          v5.0
Veredicto:            Comprar / Acumular / Mantener / Evitar
```

El CQV Calidad se redondea estrictamente a dos decimales a partir de `round(sum(F_i × w_i), 2)`. `sync_cqv.py` es la autoridad matemática SSOT; está prohibido incluir en el informe un valor distinto al generado por el script.

---

## 8. Publicación, auditoría y compatibilidad

### 8.1 Requisitos mínimos de publicación

Cada informe trimestral sigue íntegramente [`inform/template.md`](file:///e:/DeveloperGitHub/repo/finance-cqv-find/inform/template.md) y la convención `inform/cqv_v5/[ACCION]_[AÑO]_P[1-4]_CQVv5.md`. Debe incluir diez secciones, puntuaciones brutas y finales, fuentes, fórmulas, nivel de confianza, `N/D`, riesgos, escenarios y registro de correcciones.

Un informe v5.0 debe mostrar para cada factor y sección:

1. Estructura estándar completa en 10 secciones (desde Resumen Ejecutivo hasta la Sección 10 de Auditoría).
2. Métricas brutas y unidades.
3. Periodo fiscal, fecha de publicación, fecha de valoración y fecha del precio.
4. Fuente de cada dato.
5. Fórmula aplicada.
6. Puntuación del subcomponente y puntuación final del factor.
7. Confianza, limitaciones y justificación de campos `N/D`.

Cualquier informe que no respete el formato de [`inform/template.md`](file:///e:/DeveloperGitHub/repo/finance-cqv-find/inform/template.md) o que omita los elementos auditables requeridos se considerará incompleto y no auditable dentro del marco CQV v5.0.

### 8.2 Protocolo de auditoría, auto-corrección y recomendaciones

El estándar CQV v5.0 exige una **fase obligatoria de auditoría y validación experta** antes de la publicación final de cualquier informe de tesis trimestral:

1. **Cumplimiento del Formato Estándar:** Verificar que el informe siga estrictamente el formato de [`inform/template.md`](file:///e:/DeveloperGitHub/repo/finance-cqv-find/inform/template.md) y la convención de nombres `inform/cqv_v5/[ACCION]_[AÑO]_P[1-4]_CQVv5.md`.
2. **Auditoría de Integridad Matemático-Financiera:** Validar la coherencia absoluta de las fórmulas ($F_1 \dots F_8$, Value Score, Score crecimiento/múltiplo, FCF Yield, MoS, DCF) entre el dataset SSOT (`cqv_data.json`) y el documento Markdown.
3. **Auto-Corrección Transparente:** En caso de discrepancias numéricas o de tipografía, el analista/sistema está facultado para corregir inmediatamente el informe y re-ejecutar el pipeline `sync_cqv.py` para asegurar que el 100% de los artefactos (JSON, JS, Dashboard, Markdown) sean idénticos.
4. **Observaciones y Advertencias de Datos (`N/D`):** Documentar formalmente las limitaciones de datos, vacíos de información (`N/D`) o particularidades contables del período.
5. **Incorporación en la Sección 10 del Informe:** Todo informe debe incluir la **Sección 10**, que detalla la Matriz de Auditoría, el Registro de Correcciones/Observaciones y las Recomendaciones Operativas para la gestión de cartera (incluida en [`inform/template.md`](file:///e:/DeveloperGitHub/repo/finance-cqv-find/inform/template.md)).

### 8.3 Protocolo operativo y flujo SSOT

Para evitar incoherencias entre los informes de tesis, datasets y el Dashboard Web, el sistema exige seguir el flujo estandarizado en la guía oficial:
- [flujo_actualizacion_datos.md](file:///e:/DeveloperGitHub/repo/finance-cqv-find/flujo_actualizacion_datos.md)

Cualquier informe trimestral generado debe redactarse a partir de [`inform/template.md`](file:///e:/DeveloperGitHub/repo/finance-cqv-find/inform/template.md). Cualquier actualización de datos debe ingresar a través de `cqv_data.json` / `cqv_history.json` y sincronizarse mediante el pipeline automatizado `python sync_cqv.py`.

### 8.4 Compatibilidad histórica

Las puntuaciones v5.0 no son directamente comparables con v1.0, v1.1, v2.0, v3.0 o v4.0. Las series históricas deben conservar la versión metodológica utilizada en cada fecha y no deben presentar una variación de versión como mejora fundamental de la empresa.

Los informes v5.0 deben etiquetar explícitamente `metodologia_version: v5.0`. No se presentan variaciones entre versiones como cambios fundamentales de la empresa.
