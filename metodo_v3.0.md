# Manual Metodológico CQV v3.0 (8 Factores Pro)
## Estándar Oficial Actual de Evaluación de Calidad y Valor Estructural

El modelo **CQV v3.0 (Quality and Structural Value)** es el estándar analítico oficial y definitivo del sistema. Combina la granularidad de las 8 macro-dimensiones con el cálculo cuantitativo del **ROIC Real**, la normalización de **Owner Earnings (FCF Ajustado)**, la valuación en **Free Cash Flow Yield Real** y el **Filtro de Degradación Fundamental**.

---

## 📐 La Ecuación Matriz del CQV v3.0

El Score CQV v3.0 se calcula mediante la suma ponderada de 8 factores en escala del **1.0 al 10.0**:

$$\text{CQV v3.0} = (F_1 \times 0.20) + (F_2 \times 0.10) + (F_3 \times 0.10) + (F_4 \times 0.20) + (F_5 \times 0.10) + (F_6 \times 0.10) + (F_7 \times 0.10) + (F_8 \times 0.10)$$

---

## 🗂️ Algoritmos Quirúrgicos de Puntuación (Factor por Factor)

Cada macro-factor $F_n$ resulta del promediado o ponderación de métricas específicas convertidas rigurosamente a una escala continua de **1.0 a 10.0**.

---

### $F_1$: Rentabilidad Operativa y ROIC Real (Peso: 20%)

$$F_1 = \frac{\text{Score Margen} + \text{Score ROIC} + \text{Score Conversión FCF}}{3}$$

#### 1. Score Margen Operativo / EBITDA ($\text{Margen} = \max(\frac{\text{EBITDA}}{\text{Ventas}}, \frac{\text{EBIT}}{\text{Ventas}})$):
- $\text{Margen} \ge 35.0\% \implies \text{Score Margen} = 10.0$
- $15.0\% \le \text{Margen} < 35.0\% \implies \text{Score Margen} = 7.0 + 3.0 \times \left( \frac{\text{Margen} - 0.15}{0.20} \right)$
- $5.0\% \le \text{Margen} < 15.0\% \implies \text{Score Margen} = 5.0 + 2.0 \times \left( \frac{\text{Margen} - 0.05}{0.10} \right)$
- $\text{Margen} < 5.0\% \implies \text{Score Margen} = \max\left(1.0, 5.0 \times \frac{\text{Margen}}{0.05}\right)$

#### 2. Score ROIC Real ($\text{ROIC} = \frac{\text{EBIT}(1 - t)}{\text{Deuda} + \text{Patrimonio} - \text{Caja}}$):
- $\text{ROIC} \ge 20.0\% \implies \text{Score ROIC} = 10.0$
- $10.0\% \le \text{ROIC} < 20.0\% \implies \text{Score ROIC} = 7.5 + 2.5 \times \left( \frac{\text{ROIC} - 0.10}{0.10} \right)$
- $5.0\% \le \text{ROIC} < 10.0\% \implies \text{Score ROIC} = 5.0 + 2.5 \times \left( \frac{\text{ROIC} - 0.05}{0.05} \right)$
- $\text{ROIC} < 5.0\% \implies \text{Score ROIC} = \max\left(1.0, 5.0 \times \frac{\text{ROIC}}{0.05}\right)$

#### 3. Score Conversión FCF ($\text{Conversión} = \frac{\text{FCF}}{\text{Beneficio Neto GAAP}}$):
- $\text{Conversión} \ge 100.0\% \implies \text{Score Conversión} = 10.0$
- $50.0\% \le \text{Conversión} < 100.0\% \implies \text{Score Conversión} = 7.0 + 3.0 \times \left( \frac{\text{Conversión} - 0.50}{0.50} \right)$
- $\text{Conversión} < 50.0\% \implies \text{Score Conversión} = \max\left(1.0, 7.0 \times \frac{\text{Conversión}}{0.50}\right)$

---

### $F_2$: Solidez Financiera y Estructura de Balance (Peso: 10%)

$$F_2 = \frac{\text{Score Deuda} + \text{Score Predecibilidad}}{2}$$

#### 1. Score Deuda / EBITDA ($\text{Ratio} = \frac{\text{Deuda Neta}}{\text{EBITDA}}$):
- $\text{Deuda Neta} \le 0 \text{ (Caja Neta)} \implies \text{Score Deuda} = 10.0$
- $\text{Ratio} \le 1.5\text{x} \implies \text{Score Deuda} = 9.5$
- $1.5\text{x} < \text{Ratio} \le 4.0\text{x} \implies \text{Score Deuda} = 9.5 - 4.5 \times \left( \frac{\text{Ratio} - 1.5}{2.5} \right)$
- $\text{Ratio} > 4.0\text{x} \implies \text{Score Deuda} = \max\left(1.0, 5.0 - 4.0 \times \left( \frac{\text{Ratio} - 4.0}{6.0} \right)\right)$

#### 💡 Regla de Anulación por Patrimonio Neto Negativo Intencional:
Si el Patrimonio Neto Contable es $\le 0$ pero se debe a recompras masivas de acciones (ej. FICO, ORLY, MSCI) y el Margen Neto es $> 15.0\%$ con Cobertura de Intereses por EBITDA $> 8.0\text{x}$, el **Score Deuda se eleva automáticamente a un piso mínimo de 8.5**.

#### 2. Score Predecibilidad Sectorial:
- Software / SaaS B2B / Datos Regulados: **9.0 - 9.5**
- Salud / Tecnología Médica / Infraestructura: **8.5 - 9.0**
- Financieras / Industriales / Consumo: **8.0 - 8.5**

---

### $F_3$: Crecimiento del Negocio y Filtro Anti-Dilución SBC (Peso: 10%)

$$F_3 = \frac{\text{Score Crecimiento} + \text{Score M\&A} + \text{Score Dilución SBC}}{3}$$

#### 1. Score Crecimiento de Ventas y EPS ($\text{CAGR / YoY}$):
- Crecimiento $\ge 15.0\% \implies \text{Score Crecimiento} = 10.0$
- $6.0\% \le \text{Crecimiento} < 15.0\% \implies \text{Score Crecimiento} = 7.0 + 3.0 \times \left( \frac{\text{Crecimiento} - 0.06}{0.09} \right)$
- Crecimiento $< 6.0\% \implies \text{Score Crecimiento} = \max\left(1.0, 5.0 + 2.0 \times \frac{\text{Crecimiento}}{0.06}\right)$

#### 2. Score Maestría M&A:
- Adquirentes en serie excepcionales (*Roll-ups* probados como Constellation Software, Heico, Accenture): **9.8**
- Base estándar general: **8.5**

#### 3. Score Dilución por Compensación en Acciones (SBC):
- Recompras netas agresivas que reducen activamente el flotante accionario (AAPL, FICO, AZO, ORLY): **10.0**
- Empresas industriales / tradicionales sin emisión relevante de SBC: **9.5**
- Empresas tecnológicas con alta emisión de SBC no neutralizada por recompras: **8.0**

---

### $F_4$: Foso Económico (Moat) (Peso: 20%)

Puntuación cualitativa rigurosa (1.0 a 10.0) basada en la presencia de barreras de entrada:
- **10.0 (Monopolio / Foso Inexpugnable):** Estándar regulatorio o de facto utilizado por el 90%+ de la industria con costes de cambio extremos (ej. FICO, MSCI, ASML).
- **9.0 - 9.5 (Foso Fuerte):** Marca global dominante, economías de escala imbatibles o red logística propia (ej. ORLY, FTNT, MSFT, KLAC).
- **7.5 - 8.9 (Foso Moderado):** Ventaja competitiva sólida pero expuesta a rivales de gran tamaño.
- **< 7.0 (Foso Débil):** Negocio commoditizado sin poder de fijación de precios.

---

### $F_5$: Proyecciones e IA (Peso: 10%)

- **9.5 - 10.0:** Infraestructura indispensable para megatendencias globales (Superclústeres de IA, semiconductores de precisión, ciberseguridad integrada).
- **8.5 - 9.4:** Adopción rápida de IA generativa/agéntica monetizable con expansión sostenida del TAM.
- **7.5 - 8.4:** Negocios tradicionales protegidos frente a la disrupción tecnológica.

---

### $F_6$: Asignación de Capital (Peso: 10%)

- **9.5 - 10.0:** Programa de recompra de acciones masivo a precios de descuento ($>3\%$ del flotante retirado por año), política de dividendos creciente y ROIC $>25\%$.
- **8.5 - 9.4:** Reversion eficiente del flujo de caja en proyectos de expansión interna (*Growth CapEx*) con ROIC superior al costo de capital ($WACC$).
- **< 8.0:** Acumulación ineficiente de caja o M&A destructores de valor sobrepagando por *Goodwill*.

---

### $F_7$: FCF Yield Real & Valuación (Peso: 10%)

Rendimiento real del Flujo de Caja Libre sobre la Capitalización Bursátil ($\text{FCF Yield} = \frac{\text{Owner Earnings FCF}}{\text{Market Cap}}$):

- $\text{FCF Yield} \ge 6.0\% \implies F_7 = 10.0$
- $2.0\% \le \text{FCF Yield} < 6.0\% \implies F_7 = 5.0 + 5.0 \times \left( \frac{\text{FCF Yield} - 0.02}{0.04} \right)$
- $0.0\% \le \text{FCF Yield} < 2.0\% \implies F_7 = 1.0 + 4.0 \times \left( \frac{\text{FCF Yield}}{0.02} \right)$
- $\text{FCF Yield} < 0.0\% \implies F_7 = 1.0$

*Nota de Normalización: Cuando un pico puntual de Growth CapEx reduce el FCF GAAP, se utiliza el **Owner Earnings (OCF - Maintenance CapEx)**.*

---

### $F_8$: Antifragilidad y Recurrencia (Peso: 10%)

- **9.5 - 10.0:** Ingresos recurrentes por suscripciones o mantenimiento contractual $> 70\%$, base de clientes diversificada globalmente y demanda insensible a ciclos recesivos.
- **8.5 - 9.4:** Ingresos recurrentes entre $50\%$ y $70\%$ con contratos plurianuales.
- **< 8.0:** Ventas por proyectos únicos con alta volatilidad macroeconómica.

---

## 🛡️ Filtro Automático de Degradación Fundamental (*Degradation Filter*)

Para evitar trampas de valor o empresas vulnerables a la disrupción, el pipeline ejecuta la siguiente regla de seguridad:

$$\text{Si } F_4 < 6.0 \text{ o } F_2 < 5.0 \implies \text{CQV v3.0} = \min(\text{CQV v3.0}, 7.00)$$

---

## 📊 Regla de Decisión y Score PEG Normalizado

Para compañías en categoría **ÉLITE (CQV v3.0 $\ge 9.00$)**, la decisión de compra se valida con el **Score PEG Normalizado**:

$$\text{Score PEG} = \min\left(10.0, \max\left(1.0, \left( \frac{\text{Tasa Crecimiento EPS (\%) chaos}}{\text{PER Forward}} \right) \times 10 \right)\right)$$

- **Score PEG $\ge 8.0$:** *Anomalía de Descuento* (se activa gatillo de compra inmediata).
- **Score PEG $5.0 - 7.9$:** Zona de compra razonable / acumulativa.
