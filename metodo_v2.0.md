# Manual Metodológico CQV v2.0 (8 Factores Legacy)
## Expansión del Modelo a 8 Macro-Dimensiones Fundamentalmente Desglosadas

El modelo **CQV v2.0** expandió la arquitectura fundacional de 5 factores a un sistema multifactorial de 8 dimensiones para permitir un análisis más granular de la asignación de capital, la valuación en flujo de caja libre y la antifragilidad del negocio.

---

## 📐 Ecuación Matriz del CQV v2.0

$$\text{CQV v2.0} = (F_1 \times 0.20) + (F_2 \times 0.10) + (F_3 \times 0.10) + (F_4 \times 0.20) + (F_5 \times 0.10) + (F_6 \times 0.10) + (F_7 \times 0.10) + (F_8 \times 0.10)$$

---

## 🗂️ Desglose de los 8 Factores del CQV v2.0

| Factor | Denominación | Peso | Métrica / Heurística Aplicada |
| :--- | :--- | :---: | :--- |
| **$F_1$** | Rentabilidad Operativa | **20%** | Margen bruto, margen operativo GAAP y conversión de caja libre. |
| **$F_2$** | Solidez Financiera | **10%** | Ratio Deuda Neta / EBITDA y liquidez. |
| **$F_3$** | Crecimiento del Negocio | **10%** | Crecimiento YoY de ventas, beneficio operativo y EPS. |
| **$F_4$** | Foso Económico (Moat) | **20%** | Ventaja competitiva, marca, escala y costes de cambio. |
| **$F_5$** | Proyecciones e IA | **10%** | Adaptación tecnológica e impacto de la IA. |
| **$F_6$** | Asignación de Capital | **10%** | Promedio heurístico de Rentabilidad y Crecimiento ($F_6 = \frac{F_1 + F_3}{2}$). |
| **$F_7$** | Valuación Heurística | **10%** | Ajuste inverso de rentabilidad ($F_7 = \max(1.0, \min(10.0, 10.0 - (F_1 - 5.0) \times 0.8))$). |
| **$F_8$** | Antifragilidad Base | **10%** | Puntuación base predeterminada ($F_8 = 8.0$). |

---

## ⚠️ Análisis de Limitaciones Históricas del Modelo Legacy v2.0

La revisión crítica del modelo v2.0 identificó dos heurísticas de cálculo que requerían una superación metodológica:

1. **Deficiencia de Valuación en $F_7$ (Heurística Inversa):**
   En la versión 2.0 legacy, $F_7$ se calculaba como $F_7 = 10.0 - (F_1 - 5.0) \times 0.8$. Esta fórmula estimaba una compresión de múltiplo al asumir que una rentabilidad $F_1$ muy elevada producía una peor nota de valuación sin consultar el precio de mercado, la capitalización ni el PER. Por esta razón, el modelo v3.0 reemplazó totalmente este cálculo por el **Free Cash Flow Yield Real ($FCF / Market Cap$)**.

2. **Valor Predeterminado Fijo en $F_8$ ($F_8 = 8.0$):**
   En v2.0, $F_8$ asumía un valor fijo predeterminado de 8.0 para representar la resiliencia base de empresas cotizadas maduras. El modelo v3.0 eliminó esta constante fija y pasó a calificar $F_8$ cuantitativa y cualitativamente en función del porcentaje de ingresos recurrentes ($>60\%$) y la inelasticidad recesiva.

---

## 💡 Importancia del CQV v2.0

A pesar de sus limitaciones heurísticas iniciales, el modelo v2.0 sentó la estructura de ponderaciones **20-10-10-20-10-10-10-10** que otorgó mayor peso del 20% a los pilares clave ($F_1$ Rentabilidad y $F_4$ Moat), sirviendo de puente hacia el estándar cuantitativo oficial **CQV v3.0**.
