# Manual Metodológico CQV v1.1 (5 Factores Pro)
## Evolución de 5 Factores con ROIC Real y Filtro de Degradación

El modelo **CQV v1.1** mantiene la arquitectura compacta de 5 macro-factores del modelo fundacional, pero introduce dos innovaciones analíticas fundamentales: el cálculo del **ROIC Real (Return on Invested Capital)** y un **Filtro Automático de Degradación Fundamental**.

---

## 📐 Ecuación Matriz del CQV v1.1

$$\text{CQV v1.1} = (F_{1,\text{v1.1}} \times 0.25) + (F_{2,\text{v1.1}} \times 0.15) + (F_{3,\text{v1.1}} \times 0.15) + (F_4 \times 0.25) + (F_5 \times 0.20)$$

*Nota: Los sub-componentes cuantitativos $F_{1,\text{v1.1}}$, $F_{2,\text{v1.1}}$ y $F_{3,\text{v1.1}}$ incorporan por primera vez datos contables ajustados de ROIC y Solidez.*

---

## 🚀 Innovaciones Clave en CQV v1.1

### 1. Integración del ROIC Real en $F_{1,\text{v1.1}}$
A diferencia del modelo v1.0 que dependía únicamente de márgenes brutos y operativos, el factor $F_{1,\text{v1.1}}$ computa el retorno sobre el capital investido neto ($ROIC$):

$$\text{ROIC} = \frac{\text{NOPAT}}{\text{Capital Investido Neto}} = \frac{\text{Beneficio Operativo (EBIT)} \times (1 - t)}{\text{Deuda Total} + \text{Patrimonio Neto} - \text{Caja Excedente}}$$

* **Puntuación de ROIC:**
  * $ROIC \ge 20.0\% \rightarrow 10.0$ puntos.
  * $ROIC \in [10.0\%, 20.0\%] \rightarrow 7.5 - 10.0$ puntos.
  * $ROIC \in [5.0\%, 10.0\%] \rightarrow 5.0 - 7.5$ puntos.
  * $ROIC < 5.0\% \rightarrow < 5.0$ puntos.

El factor se calcula como $F_{1,\text{v1.1}}=(\text{Score Margen}+\text{Score ROIC}+\text{Score Conversión FCF})/3$. La conversión FCF es $FCF/Beneficio Neto GAAP$. Si el capital invertido neto es menor o igual que cero, el ROIC no se puntúa como infinito: se marca como no interpretable y se exige una justificación económica específica.

---

### 2. Filtro Automático de Degradación Fundamental (*Degradation Filter*)
Para evitar la sobrevaloración de empresas con ventajas competitivas deterioradas o balances frágiles, el modelo v1.1 impone una restricción de seguridad:

$$\text{Si } F_4 < 6.0 \text{ o } F_{2,\text{v1.1}} < 5.0 \implies \text{CQV v1.1} = \min(\text{CQV v1.1}, 7.00)$$

Esto garantiza que ninguna compañía con foso económico débil ($F_4 < 6.0$) o solvencia comprometida ($F_{2,\text{v1.1}} < 5.0$) pueda figurar en la categoría **ÉLITE** o **ALTA CALIDAD**.

Para completar la puntuación, $F_{2,\text{v1.1}}$ es el promedio de Score Deuda y Score Predecibilidad; $F_{3,\text{v1.1}}$ es el promedio de Score Crecimiento y Score Dilución SBC. La dilución neta material reduce la nota del subcomponente entre 0.5 y 2.0 puntos.

---

## 🗂️ Resumen de Factores de CQV v1.1

| Factor | Denominación | Peso | Avance Metodológico |
| :--- | :--- | :---: | :--- |
| **$F_{1,\text{v1.1}}$** | Rentabilidad con ROIC | **25%** | Incorpora $ROIC$ real y conversión FCF. |
| **$F_{2,\text{v1.1}}$** | Solidez Ajustada | **15%** | Tratamiento especial de patrimonio neto negativo por recompras de acciones (FICO, ORLY). |
| **$F_{3,\text{v1.1}}$** | Crecimiento & SBC | **15%** | Auditoría estricta de dilución por Stock-Based Compensation. |
| **$F_4$** | Moat Actual | **25%** | Ventaja defensiva cualitativa y costes de cambio. |
| **$F_5$** | Proyección e IA | **20%** | Resiliencia tecnológica y megatendencias. |
