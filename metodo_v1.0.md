# Manual Metodológico CQV v1.0 (5 Factores Legacy)
## Protocolo Fundacional del Score CQV

El modelo **CQV v1.0 (Quality and Structural Value)** es el marco metodológico fundacional de 5 macro-factores diseñado para evaluar la fortaleza cualitativa y cuantitativa de una empresa de forma consolidada.

---

## 📐 Ecuación Matriz del CQV v1.0

El Score CQV v1.0 se calcula mediante una suma ponderada de 5 factores clave en escala del **1.0 al 10.0**:

$$\text{CQV v1.0} = (F_1 \times 0.25) + (F_2 \times 0.15) + (F_3 \times 0.15) + (F_4 \times 0.25) + (F_5 \times 0.20)$$

---

## 🗂️ Desglose de Factores del CQV v1.0

| Factor | Denominación | Peso | Indicadores Evaluados |
| :--- | :--- | :---: | :--- |
| **$F_1$** | Rentabilidad Operativa | **25%** | Margen operativo GAAP, margen EBITDA y conversión de beneficio en Free Cash Flow. |
| **$F_2$** | Solidez Financiera | **15%** | Ratio Deuda Neta / EBITDA y estabilidad del flujo de caja operativo en ciclos. |
| **$F_3$** | Crecimiento Eficiente | **15%** | Crecimiento orgánico de ingresos ($>6-8\%$) y control de la dilución al accionista. |
| **$F_4$** | Foso Económico (Moat) | **25%** | Barreras de entrada, costes de cambio (*switching costs*), patentes y marcas. |
| **$F_5$** | Proyección Futura | **20%** | Exposición a megatendencias globales, adopción tecnológica y resiliencia a 10 años. |

---

## 🛠️ Criterios de Calificación de Factores

- **$F_1$ (Rentabilidad):** Nota 10.0 si Margen Operativo $> 30\%$ o Margen EBITDA $> 35\%$.
- **$F_2$ (Solidez):** Nota 10.0 si Deuda Neta / EBITDA $< 1.5\text{x}$ o caja neta positiva.
- **$F_3$ (Crecimiento):** Se utiliza el crecimiento interanual de ingresos como métrica principal. La SBC se evalúa mediante la variación neta de acciones diluidas: si existe dilución neta material, se resta entre 0.5 y 2.0 puntos; si las recompras la compensan, no se aplica penalización.
- **$F_4$ (Moat):** Evaluado según la dificultad de réplica del negocio con $10,000M en efectivo.
- **$F_5$ (Futuro):** Evaluación cualitativa de opcionalidad tecnológica e inmunidad a la disrupción.

---

## 📊 Definición Formal del Score PEG Propietario

En la literatura financiera tradicional, el ratio **PEG Convencional** se define como:

$$\text{PEG Convencional} = \frac{\text{PER Forward}}{\text{Tasa Crecimiento EPS (en puntos porcentuales)}}$$

*Donde valores menores a 1.0x indican infravaloración.*

Sin embargo, para mantener una escala consistente donde **notas más altas significan mejores oportunidades de inversión**, la metodología CQV utiliza la métrica inversa **Score PEG Normalizado (escala 1.0 - 10.0)**:

$$\text{Score PEG} = \min\left(10.0, \max\left(1.0, \left( \frac{\text{Tasa Crecimiento EPS (en puntos porcentuales)}}{\text{PER Forward}} \right) \times 10 \right)\right)$$

*La tasa de crecimiento se introduce como puntos porcentuales: 42.1% se introduce como 42.1, no como 0.421. El PER Forward y la tasa de crecimiento deben corresponder a la misma fecha y horizonte.*

### Interpretación del Score PEG:
- **Score PEG $\ge 8.0$:** *Anomalía de Descuento* (se paga muy poco por un alto crecimiento). Activa una señal de revisión de compra si el CQV es Élite ($≥9.00$); no constituye una orden automática.
- **Score PEG $5.0 - 7.9$:** Valoración justa / razonable.
- **Score PEG $< 5.0$:** Múltiplo elevado respecto al crecimiento esperado.
