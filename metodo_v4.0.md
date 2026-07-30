# Manual Metodológico CQV v4.0
## Estándar Operativo de Calidad, Resiliencia y Valor

CQV v4.0 es la versión operativa actual del sistema Quality and Structural Value. Mantiene la continuidad histórica con v1.0–v3.0, pero separa explícitamente calidad empresarial, valoración y confianza de los datos. Su objetivo es producir una puntuación reproducible, comparable dentro del sector y auditable por terceros.

---

## 1. Principios de la v4.0

1. Cada puntuación debe poder reconstruirse desde datos, fórmula, fecha y fuente.
2. Los datos trimestrales no sustituyen a las tendencias de 3–5 años.
3. No se utilizan valores predeterminados positivos cuando falta información crítica.
4. Los umbrales deben interpretarse según el sector y el modelo de negocio.
5. El CQV no genera una orden automática de compra: genera una señal que debe combinarse con valoración, riesgo y margen de seguridad.
6. La valoración no debe ocultar una calidad empresarial deficiente.

La escala de todos los factores es de 1.0 a 10.0. Los pesos suman 100%.

---

## 2. Ecuación matriz

$$\text{CQV v4.0} = (F_1 \times 0.20) + (F_2 \times 0.15) + (F_3 \times 0.15) + (F_4 \times 0.15) + (F_5 \times 0.10) + (F_6 \times 0.10) + (F_7 \times 0.05) + (F_8 \times 0.10)$$

| Factor | Concepto | Peso |
| :--- | :--- | ---: |
| **F1** | Economía del negocio y rentabilidad | **20%** |
| **F2** | Solidez financiera | **15%** |
| **F3** | Crecimiento durable | **15%** |
| **F4** | Moat competitivo | **15%** |
| **F5** | Asignación y reinversión de capital | **10%** |
| **F6** | Dirección, gobierno y ejecución | **10%** |
| **F7** | Opcionalidad futura y riesgo de disrupción | **5%** |
| **F8** | Antifragilidad y recurrencia | **10%** |

---

## 3. Reglas generales de medición

### 3.1 Periodos y normalización

- Crecimiento: CAGR de 3–5 años, confirmado por los últimos 12 meses.
- Márgenes, ROIC, FCF y deuda: mediana de los últimos 3 años cuando sea posible.
- Datos de mercado: precio y capitalización de la misma fecha de valoración.
- Las métricas de bancos, aseguradoras y REIT se adaptan a sus métricas sectoriales equivalentes; no se fuerza deuda/EBITDA cuando no sea económicamente aplicable.
- Los datos extraordinarios, adquisiciones, desinversiones y cambios contables deben identificarse por separado.

### 3.2 Calidad de datos

Cada métrica debe registrar:

- valor bruto;
- unidad y moneda;
- periodo fiscal;
- fecha de corte;
- fuente primaria o secundaria;
- fórmula aplicada;
- puntuación resultante;
- nivel de confianza: Alta, Media o Baja.

Si falta una métrica crítica de F2 o F8, el resultado final es **N/D** y no se emite veredicto de inversión.

---

## 4. Puntuación de factores

### F1: Economía del negocio y rentabilidad — 20%

$$F_1 = \frac{\text{Score Margen} + \text{Score ROIC} + \text{Score Conversión FCF}}{3}$$

- Score Margen: se calcula con el margen operativo o EBITDA normalizado, eligiendo la métrica económicamente representativa del sector.
- Score ROIC: utiliza NOPAT / Capital Invertido Neto. Si el denominador es menor o igual que cero, el ROIC es no interpretable y requiere una métrica alternativa documentada.
- Score Conversión FCF: FCF reportado / Beneficio Neto GAAP.
- Owner Earnings no se utiliza dentro de F1; se reserva para F8.

Como referencia general para negocios no financieros: margen ≥35% y ROIC ≥20% reciben 10.0, pero los sectores deben normalizarse por percentiles y estructura económica.

### F2: Solidez financiera — 15%

$$F_2 = 0.40(\text{Score Deuda}) + 0.30(\text{Score Intereses}) + 0.20(\text{Score Liquidez}) + 0.10(\text{Score Estabilidad FCF})$$

- Score Deuda: deuda neta/EBITDA o métrica sectorial equivalente.
- Score Intereses: EBITDA / intereses, o cobertura equivalente para entidades financieras.
- Score Liquidez: caja, líneas disponibles y vencimientos próximos.
- Score Estabilidad FCF: variabilidad del FCF y frecuencia de años negativos.

El patrimonio negativo no activa una excepción automática. Solo puede justificarse cuando existe evidencia de recompras, flujo de caja positivo, cobertura suficiente y vencimientos manejables.

### F3: Crecimiento durable — 15%

$$F_3 = 0.40(\text{Score Ingresos}) + 0.20(\text{Score EPS}) + 0.20(\text{Score Retención/Precio}) + 0.20(\text{Score Dilución})$$

- El crecimiento de ingresos se mide mediante CAGR de 3–5 años.
- El EPS debe normalizarse por partidas extraordinarias y recompras.
- La retención y el poder de precio deben estar respaldados por métricas operativas o evolución de márgenes.
- La dilución se mide por variación neta de acciones diluidas, incluyendo SBC y recompras.

Un trimestre excepcional no puede recibir por sí solo una puntuación de 10.0.

### F4: Moat competitivo — 15%

$$F_4 = 0.30(\text{Switching Costs}) + 0.25(\text{Red/Datos/Regulación/IP}) + 0.25(\text{Cuota y Retornos}) + 0.20(\text{Durabilidad})$$

- 9.5–10.0: estándar regulatorio o de facto, costes de cambio extremos y sustitución difícil.
- 8.5–9.4: ventaja global dominante con evidencia de retornos superiores.
- 7.5–8.4: ventaja defendible, pero expuesta a rivales relevantes.
- 6.0–7.4: ventaja limitada o local.
- 1.0–5.9: negocio fácilmente sustituible o commoditizado.

La cuota de mercado no equivale por sí sola a un moat.

### F5: Asignación y reinversión de capital — 10%

$$F_5 = 0.40(\text{Reinversión}) + 0.30(\text{Recompras netas}) + 0.20(\text{M\&A}) + 0.10(\text{Dividendos/Deuda})$$

- La reinversión puntúa según ROIC incremental frente al WACC.
- Las recompras solo puntúan si reducen las acciones por acción y no se realizan a precios manifiestamente excesivos.
- Las adquisiciones deben evaluarse por retorno, integración y evolución del goodwill.
- El retorno de capital no compensa una destrucción de valor operativa.

### F6: Dirección, gobierno y ejecución — 10%

$F_6 = 0.30(\text{Cumplimiento}) + 0.25(\text{Transparencia}) + 0.20(\text{Incentivos}) + 0.25(\text{Ejecución})$

- 9.5–10.0: dirección con historial consistente, comunicación transparente, incentivos alineados y ejecución superior.
- 8.5–9.4: buen historial con desviaciones menores y gobierno adecuado.
- 7.0–8.4: ejecución mixta, incentivos parcialmente alineados o información limitada.
- 1.0–6.9: incumplimiento recurrente, remuneración cuestionable, opacidad o destrucción de valor.

La puntuación debe apoyarse en guías históricas, remuneración, operaciones con insiders, calidad de adquisiciones y decisiones de capital. No se asigna una puntuación base por defecto.
### F7: Opcionalidad futura y disrupción — 5%

$$F_7 = 0.50(\text{Oportunidad Futura}) + 0.50(\text{Inmunidad o Adaptación})$$

La puntuación debe apoyarse en monetización, adopción, inversión y ventaja verificable. La mera exposición narrativa a IA, megatendencias o un mercado potencial no es suficiente.

- 9.5–10.0: oportunidad estructural demostrada y baja amenaza de sustitución.
- 8.0–9.4: oportunidad real con ejecución todavía parcialmente pendiente.
- 6.0–7.9: futuro incierto o equilibrado entre oportunidades y riesgos.
- 1.0–5.9: disrupción probable o deterioro estructural.

### F8: Antifragilidad y recurrencia — 10%

$F_8 = 0.30(\text{Recurrencia}) + 0.25(\text{Resistencia Recesiva}) + 0.20(\text{Diversificación}) + 0.25(\text{Flexibilidad})$

- 9.5–10.0: ingresos recurrentes superiores al 70%, clientes diversificados y demanda muy resistente.
- 8.5–9.4: recurrencia entre 50% y 70% y contratos plurianuales.
- 8.0–8.4: recurrencia parcial o sensibilidad cíclica moderada.
- 7.0–7.9: volatilidad relevante, pero con capacidad financiera de adaptación.
- 1.0–6.9: alta exposición cíclica, concentración o escasa flexibilidad.

La valoración no forma parte de F8 ni del CQV de calidad. No se asigna una puntuación base por defecto.
---

## 5. Filtros de seguridad

Después del cálculo ponderado:

- Si F2 < 4.0, el CQV máximo es 6.99.
- Si F4 < 4.0, el CQV máximo es 6.99.
- Si F2 o F8 son N/D, el CQV de calidad es N/D y no se emite recomendación de compra.
- Si la confianza global es Baja, el resultado se presenta como provisional.
- Ningún filtro convierte una empresa débil en una empresa de calidad.

La confianza global es la menor de las confianzas de F1, F2, F3 y F8 cuando cualquiera de ellas sea crítica; en otro caso es la media ponderada de los ocho factores. La confianza de la valoración se informa por separado.

---

## 6. Clasificación y decisión

- **ÉLITE:** CQV de calidad ≥9.00 y F2, F4 y F8 ≥7.0.
- **ALTA CALIDAD:** 8.00–8.99.
- **EN OBSERVACIÓN:** 7.00–7.99.
- **VULNERABLE:** <7.00 o activación de un filtro severo.

La decisión se expresa en dos ejes:

| Calidad CQV | Value Score | Señal |
|---|---|---|
| Alta | Alta | Candidato prioritario para revisión |
| Alta | Baja | Empresa excelente, precio exigente |
| Baja | Alta | Posible trampa de valor |
| Baja | Baja | Evitar o mantener fuera de cartera |

La v4.0 no activa compras automáticas. La señal final debe incluir CQV de calidad, Value Score, confianza de ambos, fecha de datos, riesgos principales y margen de seguridad.

---

## 7. Requisitos mínimos de publicación

Un informe v4.0 debe mostrar para cada factor:

1. Métricas brutas y unidades.
2. Periodo fiscal y fecha de mercado.
3. Fuente de cada dato.
4. Fórmula aplicada.
5. Puntuación del subcomponente.
6. Puntuación final del factor.
7. Confianza y limitaciones.

Un score sin estos elementos se considera una estimación cualitativa y no un CQV v4.0 auditable.

---

---

## 9. Capa complementaria de valoración intrínseca

El CQV v4.0 separa dos preguntas que no deben confundirse:

1. **Calidad:** qué tan sólida y durable es la empresa.
2. **Valor:** cuánto vale el negocio frente al precio actual.

El score CQV mide calidad y no sustituye al valor intrínseco. Para publicar un veredicto de inversión debe añadirse una valoración por escenarios. Esta capa produce un Value Score separado.

### 9.1 Flujo de caja descontado

Para empresas no financieras, el flujo de caja libre para la empresa se calcula como:

$$FCFF = EBIT(1-t) + D\&A - CapEx - \Delta NWC$$

El valor empresa se estima como:

$$EV = \sum_{t=1}^{n}\frac{FCFF_t}{(1+WACC)^t} + \frac{TV}{(1+WACC)^n}$$

$$TV = \frac{FCFF_{n+1}}{WACC-g}$$

El valor del equity se obtiene mediante:

$$\text{Valor Equity} = EV - \text{Deuda Neta} + \text{Activos No Operativos}$$

$$\text{Valor por Acción} = \frac{\text{Valor Equity}}{\text{Acciones Diluidas}}$$

Debe cumplirse siempre $g < WACC$. La tasa terminal no puede superar razonablemente el crecimiento nominal de la economía durante un periodo perpetuo.

Para bancos, aseguradoras y REIT se utilizarán modelos sectoriales equivalentes, como dividend discount, excess returns, P/B ajustado o FFO/AFFO, en lugar de forzar un FCFF industrial.

### 9.2 Escenarios obligatorios

La valoración debe presentar al menos tres escenarios:

| Escenario | Supuestos mínimos | Probabilidad |
| :--- | :--- | :---: |
| Pesimista | Menor crecimiento, presión de margen y mayor riesgo | 20%–30% |
| Base | Supuestos normalizados y consistentes con la historia | 40%–60% |
| Optimista | Mayor crecimiento, expansión de margen y ejecución favorable | 20%–30% |

El valor esperado se calcula como:

$$\text{Valor Esperado} = \sum(\text{Valor Escenario}_i \times \text{Probabilidad}_i)$$

Las probabilidades deben sumar 100% y deben justificarse. No se permite utilizar únicamente el escenario optimista para activar una recomendación.

### 9.3 Value Score, PEG invertido y expectativas implícitas

El Value Score no se incorpora a la fórmula CQV. Se calcula de forma independiente:

$$\text{Value Score} = 0.40(\text{Score FCF Yield}) + 0.30(\text{Score PEG}) + 0.30(\text{Score Margen de Seguridad})$$

$$\text{Owner Earnings} = \text{OCF} - \text{Maintenance CapEx}$$

$$\text{FCF Yield} = \frac{\text{Owner Earnings}}{\text{Capitalización Bursátil}}$$

El Score PEG invertido se limita a una escala de 0 a 10, aunque se conserva el valor bruto para auditoría:

$$\text{PEG Bruto} = (\frac{\text{Crecimiento EPS en puntos porcentuales}}{\text{PER Forward}})\times10$$

$$\text{Score PEG} = \min(10.0,\max(0.0,\text{PEG Bruto}))$$

- Si el crecimiento EPS es menor o igual que cero, Score PEG = 0.
- Si el PER Forward es menor o igual que cero o no está disponible, Score PEG = N/D.
- El crecimiento se introduce como 42.1, no como 0.421, y debe corresponder al mismo horizonte NTM que el PER Forward.
- Un PEG bruto superior a 10 se reporta como tal, pero el Score PEG queda en 10.0.

Interpretación: cuanto más cerca de 10, más atractiva es la relación entre crecimiento esperado y múltiplo pagado. Esto no sustituye al DCF ni demuestra por sí solo que la empresa sea una buena inversión.
El informe debe calcular qué está descontando el precio actual:

- crecimiento implícito de ingresos y EPS;
- margen operativo implícito;
- duración implícita del crecimiento;
- WACC implícito, si procede;
- valor terminal implícito.

Si el precio exige supuestos superiores al escenario optimista, la empresa puede ser excelente pero estar sobrevalorada.

### 9.4 Sensibilidad y margen de seguridad

Debe mostrarse una matriz de sensibilidad con al menos tres valores de WACC y tres tasas terminales. El margen de seguridad se calcula como:

$$\text{Margen de Seguridad} = \frac{\text{Valor Intrínseco por Acción} - \text{Precio Actual}}{\text{Valor Intrínseco por Acción}}$$

La decisión no debe basarse en un único valor puntual. Se recomienda utilizar el valor esperado y comprobar que el escenario base conserva un margen de seguridad positivo.

### 9.5 Registro de riesgos

Cada informe debe documentar los principales riesgos con:

$$\text{Riesgo Ajustado} = \text{Probabilidad} \times \text{Impacto} \times (1-\text{Mitigación})$$

Como mínimo deben revisarse:

- riesgo regulatorio;
- riesgo de sustitución tecnológica;
- concentración de clientes o productos;
- sensibilidad macroeconómica;
- riesgo de deuda y refinanciación;
- riesgo de ejecución de la dirección;
- dependencia de una estimación contable o de una guía corporativa.

### 9.6 Salida final obligatoria

El resultado final debe mostrar separadamente:

```text
CQV Calidad:          X.XX / 10
Value Score:          X.XX / 10
Valor Intrínseco:     $X.XX por acción
Precio Actual:        $X.XX
Margen de Seguridad:  X.X%
Confianza:            Alta / Media / Baja
Veredicto:            Comprar / Acumular / Mantener / Evitar
```

Reglas de decisión recomendadas:

- **Comprar/Revisar compra:** CQV de calidad ≥8.0, Value Score suficiente, valoración base o esperada con margen de seguridad positivo y confianza Alta/Media.
- **Acumular:** calidad alta, valoración razonable y margen de seguridad moderado.
- **Mantener:** empresa de alta calidad, pero precio sin margen suficiente.
- **Evitar:** CQV bajo, filtros severos, datos insuficientes o valoración dependiente del escenario optimista.

La v4.0 no convierte un CQV alto en una compra automática. Una empresa puede ser excelente y no ser una buena inversión al precio actual.
## 10. Compatibilidad histórica

Las puntuaciones v4.0 no son directamente comparables con v1.0, v1.1, v2.0 o v3.0. Las series históricas deben conservar la versión metodológica utilizada en cada fecha y no deben presentar una variación de versión como mejora fundamental de la empresa.

---

## 11. Protocolo Operativo y Flujo de Actualización de Datos SSOT

Para evitar incoherencias entre los informes de tesis, datasets y el Dashboard Web, el sistema exige seguir el flujo estandarizado en la guía oficial:
- [flujo_actualizacion_datos.md](file:///e:/DeveloperGitHub/repo/finance-cqv-find/flujo_actualizacion_datos.md)

Cualquier actualización de datos debe ingresar a través de `cqv_data.json` / `cqv_history.json` y sincronizarse mediante el pipeline automatizado `python sync_cqv.py`.

