# Marco Metodológico Unificado: CQV (Quality and Structural Value)
## Índice Maestro de Metodologías y Evolución de Versiones

Este documento constituye el manual metodológico central del sistema **CQV (Quality and Structural Value)**. Su propósito es definir la evolución del modelo de evaluación fundamental a lo largo de sus distintas iteraciones, estableciendo la referencia directa a cada manual metodológico específico por su sufijo correspondiente.

---

## 🗂️ Índice de Versiones del Modelo CQV

| Versión Metodológica | Archivo de Especificación | Arquitectura | Innovaciones Clave | Estándar Operativo |
| :--- | :--- | :---: | :--- | :--- |
| **CQV v1.0** | [metodo_v1.0.md](file:///e:/DeveloperGitHub/repo/finance-cqv-find/metodo_v1.0.md) | 5 Factores | Marco fundacional (Rentabilidad 25%, Solidez 15%, Crecimiento 15%, Moat 25%, Futuro 20%). Introduce el Score PEG Normalizado. | Histórico / Legacy |
| **CQV v1.1** | [metodo_v1.1.md](file:///e:/DeveloperGitHub/repo/finance-cqv-find/metodo_v1.1.md) | 5 Factores Pro | Incorporación del **ROIC Real** ($\frac{\text{NOPAT}}{\text{Capital Investido}}$) en $F_{1,\text{v1.1}}$ y el **Filtro de Degradación** (tope 7.00/10 si $F_4 < 6.0$). | Histórico / Pro |
| **CQV v2.0** | [metodo_v2.0.md](file:///e:/DeveloperGitHub/repo/finance-cqv-find/metodo_v2.0.md) | 8 Factores | Expansión a 8 dimensiones (20-10-10-20-10-10-10-10) añadiendo Asignación de Capital, Valuación heurística e Antifragilidad base. | Histórico / Legacy |
| **CQV v3.0** | [metodo_v3.0.md](file:///e:/DeveloperGitHub/repo/finance-cqv-find/metodo_v3.0.md) | 8 Factores Pro | Algoritmos cuantitativos de puntuación 1-10, ROIC Real, Owner Earnings, FCF Yield Real, Score PEG y Filtro de Degradación. | Histórico / Pro |
| **CQV v4.0** | [metodo_v4.0.md](file:///e:/DeveloperGitHub/repo/finance-cqv-find/metodo_v4.0.md) | 8 Factores Pro + Valoración Intrínseca Separada | **Estándar Operativo Actual**. Normalización sectorial, confianza de datos, DCF por escenarios, expectativas implícitas, margen de seguridad y filtros de seguridad. | **ESTÁNDAR OFICIAL ACTUAL** |

---

## 📐 Comparativa de Fórmulas por Versión

### 1. CQV v1.0 (5 Factores Legacy):
$$\text{CQV v1.0} = (F_1 \times 0.25) + (F_2 \times 0.15) + (F_3 \times 0.15) + (F_4 \times 0.25) + (F_5 \times 0.20)$$

### 2. CQV v1.1 (5 Factores Pro):
$$\text{CQV v1.1} = (F_{1,\text{v1.1}} \times 0.25) + (F_{2,\text{v1.1}} \times 0.15) + (F_{3,\text{v1.1}} \times 0.15) + (F_4 \times 0.25) + (F_5 \times 0.20)$$
$$\text{Si } F_4 < 6.0 \text{ o } F_{2,\text{v1.1}} < 5.0 \implies \text{CQV v1.1} = \min(\text{CQV v1.1}, 7.00)$$

### 3. CQV v2.0 (8 Factores Legacy):
$$\text{CQV v2.0} = (F_1 \times 0.20) + (F_2 \times 0.10) + (F_3 \times 0.10) + (F_4 \times 0.20) + (F_5 \times 0.10) + (F_6 \times 0.10) + (F_7 \times 0.10) + (F_8 \times 0.10)$$

### 4. CQV v3.0 (8 Factores Pro - Estándar Oficial Actual):
$$\text{CQV v3.0} = (F_1 \times 0.20) + (F_2 \times 0.10) + (F_3 \times 0.10) + (F_4 \times 0.20) + (F_5 \times 0.10) + (F_6 \times 0.10) + (F_7 \times 0.10) + (F_8 \times 0.10)$$
$$\text{Si } F_4 < 6.0 \text{ o } F_2 < 5.0 \implies \text{CQV v3.0} = \min(\text{CQV v3.0}, 7.00)$$

---

### 5. CQV v4.0 (8 Factores Pro - Estándar Operativo Actual):
$$\text{CQV v4.0} = (F_1 \times 0.20) + (F_2 \times 0.15) + (F_3 \times 0.15) + (F_4 \times 0.15) + (F_5 \times 0.10) + (F_6 \times 0.10) + (F_7 \times 0.05) + (F_8 \times 0.10)$$

## 🏆 Escala Unificada de Calidad CQV

- **ÉLITE (Score $\ge 9.00$):** Retornos sobre el capital ($ROIC \ge 20.0\%$), foso económico indestructible ($F_4 \ge 9.0$), asignación de capital estelar y flujo de caja libre masivo.
- **ALTA CALIDAD (Score $8.00 - 8.99$):** Empresas con gran fortaleza financiera y foso competitivo robusto, pero con tasas de crecimiento moderadas o industrias más maduras.
- **EN OBSERVACIÓN (Score $7.00 - 7.99$):** Compañías en transición o con compresión puntual en márgenes.
- **VULNERABLE (Score $< 7.00$):** Trampas de valor o modelos amenazados estructuralmente.
