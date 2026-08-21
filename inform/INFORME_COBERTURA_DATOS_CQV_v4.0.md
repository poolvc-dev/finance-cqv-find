# Informe de cobertura de datos y ajustes metodologicos CQV v4.0

Fecha: 09/08/2026  
Alcance: metodologia, prompt maestro, flujo SSOT, pipeline y cuatro informes recientes: AMZN, AAPL, UBER y CDNS.

## 1. Objetivo

Este informe identifica:

1. Que datos podemos obtener de forma recurrente y auditable.
2. Que datos solo podemos obtener con fuentes secundarias o calculos propios.
3. Que datos normalmente no podremos obtener con precision suficiente.
4. Como ajustar la metodologia para producir informes completos sin inventar cifras.

La regla central debe mantenerse: **N/D es preferible a una cifra no verificable**. Un informe completo no significa que todos los campos tengan un numero; significa que cada campo tiene un estado, una fuente, una limitacion y un impacto explicito.

## 2. Flujo real utilizado

El proceso actual es:

1. Identificar ticker, periodo fiscal y fecha de valoracion.
2. Leer earnings release, presentacion, 10-Q/10-K y datos de mercado fechados.
3. Contrastar con fuentes secundarias reputadas cuando la fuente primaria no desglosa el dato.
4. Registrar entradas y puntuaciones en `cqv_data.json` y la serie en `cqv_history.json`.
5. Ejecutar `python sync_cqv.py --ticker TICKER`.
6. Sincronizar `cqv_data.js`, `cqv_history.js` y `dashboard.html` desde el SSOT.
7. Redactar `inform/TICKER_AAAA_QX.md` a partir de `inform/template.md`.
8. Auditar matematicamente SSOT contra informe.

El pipeline recalcula campos; no redacta narrativas ni demuestra por si mismo la calidad de las fuentes. La trazabilidad fuente-fecha-periodo-unidad debe seguir documentandose en el informe y, como mejora, tambien en el SSOT.

## 3. Que es el CQV

El CQV mide calidad empresarial, no precio atractivo:

```text
CQV = F1 x 0.20 + F2 x 0.15 + F3 x 0.15 + F4 x 0.15
    + F5 x 0.10 + F6 x 0.10 + F7 x 0.05 + F8 x 0.10
```

| Factor | Peso | Datos que lo soportan |
|---|---:|---|
| F1 Economia y rentabilidad | 20% | Revenue, EBIT, margenes, EBITDA, EPS, OCF, FCF, ROIC/ROA/ROE cuando existen |
| F2 Solidez financiera | 15% | Caja, deuda, deuda neta, liquidez, cobertura, vencimientos, OCF |
| F3 Crecimiento durable | 15% | CAGR, crecimiento trimestral, guidance, backlog, cRPO, usuarios, volumen y retencion |
| F4 Moat competitivo | 15% | Cuota, switching costs, red, IP, recurrencia, concentracion, competencia |
| F5 Asignacion de capital | 10% | Recompras, dividendos, adquisiciones, deuda, reinversion y SBC |
| F6 Direccion y ejecucion | 10% | Cumplimiento de guidance, margenes, estrategia, gobierno y consistencia |
| F7 Opcionalidad y disrupcion | 5% | Nuevos productos, AI, AV, TAM, plataformas, riesgos de sustitucion |
| F8 Antifragilidad y recurrencia | 10% | Recurrencia, diversificacion, resiliencia de margenes y conversion de caja |

F4, F6, F7 y parte de F8 no son cifras contables puras. Son puntuaciones analiticas que requieren evidencia cualitativa. No deben presentarse como datos reportados por la empresa.

## 4. Datos que normalmente si podremos obtener

### 4.1 Resultados y balance

Estos datos suelen estar disponibles en earnings release y 10-Q/10-K:

| Dato | Disponibilidad esperada | Fuente principal | Estado recomendado |
|---|---|---|---|
| Revenue | Alta | Estado de resultados / release | Reportado primario |
| EBIT o income from operations | Alta | 10-Q/10-K / release | Reportado primario |
| Margen operativo | Alta o calculable | EBIT / revenue | Calculado |
| Net income GAAP | Alta | Estado de resultados | Reportado primario |
| EPS GAAP | Alta | Estado de resultados | Reportado primario |
| EPS ajustado | Media-Alta | Release y conciliacion no-GAAP | Reportado primario, no mezclar con GAAP |
| OCF | Alta en 10-Q/10-K | Estado de flujos | Reportado primario; Q2 puede requerir restar Q1 al acumulado |
| CapEx total | Media-Alta | Flujos de inversion / notas | Reportado o calculado |
| Caja y equivalentes | Alta | Balance | Reportado primario |
| Deuda total | Alta | Balance / notas | Reportado primario |
| Deuda neta | Alta si hay caja y deuda | Deuda - caja | Calculado |
| Acciones diluidas | Alta | EPS y notas | Reportado primario |
| SBC | Media-Alta | Flujos, notas y conciliacion | Reportado primario |
| Recompras | Media-Alta | 10-Q/10-K y notas | Reportado primario; trimestre exacto si se desglosa |

### 4.2 Datos de mercado y consenso

| Dato | Disponibilidad esperada | Fuente | Advertencia |
|---|---|---|---|
| Precio | Alta | Nasdaq, NYSE, Yahoo, StockAnalysis, proveedores institucionales | Debe tener fecha y mercado |
| Capitalizacion | Alta | S&P Global, FactSet, StockAnalysis, Yahoo | Debe corresponder a la misma fecha o calcularse con acciones |
| PER trailing | Alta | Proveedor de mercado | Revisar si usa GAAP, ajustado o TTM restatado |
| PER forward | Media-Alta | FactSet, LSEG, Bloomberg, Barchart, StockAnalysis | Exigir mismo horizonte que EPS growth |
| EPS estimado | Media-Alta | Consenso reputado | Registrar numero de analistas, fecha y si es GAAP/no-GAAP |
| Precio objetivo | Alta | Consenso secundario | No equivale a valor intrinseco CQV |
| Beta, tasa libre y prima de riesgo | Media | Proveedores de mercado y fuentes macro | Fecha y metodologia pueden variar |

### 4.3 Datos operativos y competitivos

Se pueden obtener cuando la empresa los publica: usuarios, clientes, bookings, volumen, backlog, cRPO, segmentos, mix geografico, cuota, capacidad, retencion y guidance. Si la empresa no los publica, una fuente secundaria puede complementar, pero la confianza debe bajar y el dato debe etiquetarse como reportado por tercero, estimado o calculado.

## 5. Datos que podremos obtener solo de forma condicional

| Dato | Por que es condicional | Tratamiento |
|---|---|---|
| OCF trimestral | Algunos emisores publican solo seis meses o nueve meses | Calcular diferencia entre acumulados y documentar el periodo base |
| FCF trimestral | Puede estar en release, pero no siempre en 10-Q | Usar definicion de la empresa; no confundir con Owner Earnings |
| ROIC, ROA y ROE | Requieren capital invertido, activos y patrimonio normalizados | Calcular solo si las entradas son comparables; si no, N/D |
| CAGR 2020-2026 | Cambios de fiscal year, adquisiciones y restatements | Usar periodo homogeneo y explicar exclusiones |
| Dilucion neta SBC | SBC, acciones emitidas y recompras pueden estar en periodos distintos | Calcular solo con acciones comparables; si no, reportar SBC bruto y N/D neto |
| EPS growth NTM | Depende de consenso y horizonte | Usar solo con PER forward del mismo horizonte; si no, N/D |
| Market Cap | Puede cambiar intradia | Fijar fecha/hora o usar cierre y acciones de la misma fecha |
| CapEx de crecimiento | No siempre se separa de CapEx recurrente | No inferirlo a partir del total sin metodologia |
| DCF FCFF | Requiere EBIT, impuestos, D&A, CapEx y variacion de NWC | Puede calcularse con estados completos y supuestos documentados |

## 6. Datos que normalmente no obtendremos de forma primaria

### 6.1 Maintenance CapEx

La mayoria de las companias no separa formalmente CapEx de mantenimiento y CapEx de crecimiento. Esta es la principal causa de N/D en los informes actuales.

No debe hacerse lo siguiente:

- usar automaticamente CapEx total como Maintenance CapEx;
- usar FCF como Owner Earnings sin declararlo;
- inferir mantenimiento como porcentaje fijo de revenue sin fuente;
- copiar la cifra de otro trimestre.

Orden permitido:

1. Disclosure oficial de maintenance CapEx.
2. Presentacion o CFO commentary con metodologia.
3. Estimacion institucional con rango y metodologia reproducible.
4. Informe sectorial reputado con una base defendible.
5. Si nada existe: `maintenance_capex = N/D`.

Impacto: Owner Earnings, FCF Yield y Value Score deben ser N/D. El CQV de calidad puede seguir calculandose si F1-F8 tienen evidencia suficiente, pero no se debe emitir recomendacion afirmativa.

### 6.2 Valor intrinseco exacto

El valor intrinseco no es un dato reportado. Es un modelo dependiente de supuestos. No obtendremos una cifra objetiva unica. Solo podemos obtener:

- un rango DCF propio con entradas trazables;
- un consenso o precio objetivo secundario, etiquetado como externo;
- escenarios Bear/Base/Bull con probabilidad justificada.

Si faltan FCFF, deuda neta, acciones o supuestos defendibles, el valor intrinseco CQV debe ser N/D. Un precio objetivo de un analista no debe sobrescribir `intrinsic_value`.

### 6.3 Moat, direccion y opcionalidad

No existen medidas contables universales para moat, calidad de la direccion u opcionalidad. Estas dimensiones siempre requeriran juicio analitico. La solucion no es eliminarlas, sino registrar:

- evidencia observable;
- hipotesis;
- contraevidencia;
- nivel de confianza;
- limite de la puntuacion.

### 6.4 Expectativas implicitas

El crecimiento, margen, WACC o valor terminal que descuenta el precio no se observa directamente. Solo puede inferirse mediante un modelo inverso y depende de supuestos. Debe marcarse como `calculado/estimado`, no como dato reportado.

## 7. Diagnostico de los informes actuales

| Empresa | Datos con los que contamos | Campos que faltan | Impacto actual |
|---|---|---|---|
| AMZN | Precio, PER, PER forward, EPS growth y resultados operativos | OCF/market cap/maintenance CapEx/DCF auditable | CQV separado de valor; Value Score N/D |
| AAPL | Precio, resultados, OCF TTM y calidad | PER comparable, EPS growth NTM, market cap y Maintenance CapEx | PEG y Value Score N/D |
| UBER | Precio, PER, forward PE, EPS growth, OCF y market cap | Maintenance CapEx, Owner Earnings, intrinsic value | PEG disponible; Value Score y veredicto N/D |
| CDNS | Revenue, margenes, backlog, cRPO, OCF, FCF, deuda, precio y consenso | Maintenance CapEx, DCF propio y MoS | CQV y PEG disponibles; Value Score N/D |

Patron identificado: **los informes de calidad pueden estar completos aun cuando la capa de valoracion no lo este**. La metodologia debe mostrar esos dos estados por separado.

## 8. Ajustes metodologicos recomendados

### 8.1 Introducir estado por dato

Cada campo debe tener uno de estos estados:

| Estado | Significado | Puede alimentar formula |
|---|---|---|
| `reported_primary` | Publicado por empresa/SEC | Si |
| `reported_secondary` | Publicado por proveedor reputado | Si, con confianza reducida |
| `calculated` | Derivado de entradas documentadas | Si |
| `estimated` | Supuesto o consenso identificado | Solo en escenarios; no como historico |
| `N/D` | No verificable o no defendible | No |

### 8.2 Separar tres puntuaciones de salida

El informe debe mostrar:

1. **CQV Calidad:** F1-F8 y sus evidencias.
2. **Completitud de datos:** porcentaje de campos criticos disponibles, sin convertirlo en una nota de calidad.
3. **Value Score:** solo si Owner Earnings, PEG y MoS tienen entradas validas.

Ejemplo de estado:

```text
CQV Calidad: 8.95/10
Completitud calidad: Alta
Completitud valoracion: Baja
Value Score: N/D
Veredicto: N/D - valoracion incompleta
```

### 8.3 Definir puertas de publicacion

| Capa | Minimo para publicar numero | Si falta |
|---|---|---|
| CQV | F1-F8 justificables; F2 y F8 no N/D | CQV N/D |
| PEG | PER forward y EPS growth mismo horizonte | PEG N/D |
| Owner Earnings | OCF y Maintenance CapEx defendible | Owner Earnings N/D |
| FCF Yield | Owner Earnings y market cap misma fecha | FCF Yield N/D |
| MoS | Intrinsic value con DCF documentado | MoS N/D |
| Value Score | Score FCF Yield, Score PEG y Score MoS | Value Score N/D |
| Veredicto | CQV, MoS y confianza suficientes | No recomendacion afirmativa |

### 8.4 Ajustar el DCF sin contaminar Owner Earnings

Debe permitirse un DCF con FCFF cuando existan EBIT, impuestos, D&A, CapEx y NWC, aunque Maintenance CapEx no este disponible. Sin embargo:

- ese DCF debe llamarse **DCF FCFF**, no Owner Earnings;
- sus supuestos deben estar en el informe;
- debe tener Bear/Base/Bull y sensibilidad 3x3;
- su confianza maxima debe ser Media si depende de fuentes secundarias;
- no debe desbloquear automaticamente FCF Yield ni Value Score.

Esto permite completar la capa de valoracion sin mezclar dos conceptos distintos.

### 8.5 Incorporar metadatos en el SSOT

El JSON actual almacena valores agregados, pero no una fuente individual por campo. Se recomienda añadir una estructura como:

```json
"data_meta": {
  "ocf": {
    "value": 635.0,
    "unit": "USD millions",
    "period": "Q2 2026",
    "as_of": "2026-07-27",
    "source": "Cadence Q2 release / 10-Q",
    "status": "reported_primary",
    "confidence": "Alta"
  }
}
```

Como minimo deben incorporarse `valuation_date`, `source`, `source_date`, `period`, `unit`, `status`, `method` y `confidence` para cada entrada material.

## 9. Datos que no deberiamos intentar forzar

- Maintenance CapEx sin desglose o metodologia.
- Owner Earnings usando FCF total sin declaracion.
- Valor intrinseco puntual basado en un unico precio objetivo externo.
- PER forward y EPS growth de horizontes diferentes.
- ROIC/ROE comparados entre empresas con definiciones distintas.
- Moat expresado como cifra supuestamente objetiva.
- Probabilidades DCF sin justificacion.
- Datos de otro trimestre para rellenar el actual.
- Precio sin fecha de cierre o mercado.

## 10. Plan de implementacion recomendado

### Fase 1: ajuste documental

- Modificar `promt.md` para exigir estado y metadatos por dato.
- Añadir al template una tabla de cobertura de datos.
- Separar explicitamente CQV Calidad, Completitud y Value Score.

### Fase 2: ajuste del SSOT y pipeline

- Añadir `data_status`, `source_date`, `valuation_date`, `unit` y `confidence`.
- Validar que `maintenance_capex` no pueda rellenarse con `capex` automaticamente.
- Añadir `data_completeness_quality` y `data_completeness_valuation` calculados.
- Permitir DCF FCFF separado de Owner Earnings.

### Fase 3: auditoria

- Comprobar que todo numero del bloque 9.6 existe en SSOT.
- Comprobar que cada N/D tiene motivo e impacto.
- Comparar periodos y horizontes de PER forward/EPS growth.
- Verificar que la fuente del precio coincide con la fecha de valoracion.

## 11. Conclusion operativa

Con el flujo actual obtendremos de forma fiable la mayor parte de resultados, balance, deuda, caja, EPS, OCF, CapEx total, datos operativos y datos de mercado. No obtendremos de forma consistente Maintenance CapEx, Owner Earnings normalizado, valor intrinseco unico ni medidas objetivas de moat y direccion.

Por tanto, el ajuste correcto no es rellenar todos los N/D. Es producir dos salidas independientes:

- **Informe CQV de calidad completo**, basado en F1-F8 y evidencia.
- **Capa de valoracion completa o parcialmente disponible**, con PEG, DCF FCFF, Owner Earnings y Value Score solo cuando sus entradas sean defendibles.

Esta separacion mantiene la auditabilidad, evita recomendaciones falsas y permite identificar exactamente que dato falta para desbloquear cada calculo.

