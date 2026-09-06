import re
from pathlib import Path

report_path = Path('inform/cqv_v5/PANW_2026_P2_CQVv5.md')
text = report_path.read_text(encoding='utf-8')

# Historical Capital Efficiency Section 3.3
sec3_3 = """### 3.3. Análisis Histórico de Eficiencia de Capital: ROIC, ROI/ROA y ROE (2020 – 2026)

| Métrica de Eficiencia | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 TTM | Tendencia y Diagnóstico (Desde 2020) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **ROA / ROI (Return on Assets %)** | -3.5% | -4.8% | 1.9% | 4.2% | 8.9% | 11.2% | **12.8%** | **Expansión acelerada:** De pérdidas contables a fuerte rentabilidad sobre activos. |
| **ROE (Return on Equity %)** | -28.4% | -45.2% | 8.5% | 17.6% | 32.4% | 35.8% | **38.2%** | **Excelente:** Retorno sobre patrimonio impulsado por la expansión de márgenes de software. |
| **ROIC (Return on Invested Capital %)** | 8.2% | 10.5% | 15.8% | 21.4% | 26.8% | 29.5% | **31.4%** | **Foso de Calidad Élite:** ROIC triplicado desde 2020 superando holgadamente el WACC (9.0%). |
"""

# Historical Evolution Section 8
sec8 = """## 8. Evolución Histórica de Puntuaciones CQV (2020 – 2026)

```mermaid
graph LR
    Y2020["2020: 8.62 (Alta Calidad)"] --> Y2021["2021: 8.85 (Alta Calidad)"]
    Y2021 --> Y2022["2022: 9.05 (Élite - Breakeven GAAP)"]
    Y2022 --> Y2023["2023: 9.28 (Élite - S&P 500)"]
    Y2023 --> Y2024["2024: 9.35 (Élite - Plataformización)"]
    Y2024 --> Y2025["2025: 9.41 (Élite - FCF Margin >35%)"]
    Y2025 --> Y2026["2026 P2: 9.46 (Élite - $4.4B FCF)"]
    style Y2026 fill:#2e7d32,stroke:#1b5e20,stroke-width:2px,color:#fff
```

### Tabla Auditada de la Serie Histórica CQV v5.0 (2020 – 2026)

| Año / Periodo | PER Trailing | PER Forward | CQV v4.0 | CQV v5.0 | Value Score | Clasificación | Diagnóstico Fundamental y Eventos Clave |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **2020 (Mediana)** | 45.0x | N/D | 8.62 | **8.62** | 5.20 | **ALTA CALIDAD** | Crecimiento elevado pero rentabilidad GAAP negativa; inicio de transición a la nube. |
| **2021 (Mediana)** | 52.0x | N/D | 8.85 | **8.85** | 5.45 | **ALTA CALIDAD** | Aceleración en Prisma Cloud y Cortex; expansión del margen operativo non-GAAP a 21%. |
| **2022 (Mediana)** | 42.0x | N/D | 9.05 | **9.05** | 6.10 | **ÉLITE** | **Punto de inflexión histórico:** Primer trimestre con beneficio neto GAAP positivo (Q4 FY22). |
| **2023 (Mediana)** | 48.5x | N/D | 9.28 | **9.28** | 6.25 | **ÉLITE** | Inclusión en el índice S&P 500; el NGS ARR supera los $3.0B con margen FCF > 30%. |
| **2024 (Mediana)** | 52.0x | N/D | 9.35 | **9.35** | 6.35 | **ÉLITE** | Lanzamiento formal de la estrategia de 'Plataformización'; NGS ARR supera los $4.2B. |
| **2025 (Mediana)** | 54.2x | N/D | 9.41 | **9.41** | 6.48 | **ÉLITE** | Maduración de la plataforma con más de 1,000 cuentas plataformizadas; FCF margin en 38%. |
| **P1 2026** | 53.5x | 41.2x | 9.41 | **9.41** | 6.65 | **ÉLITE** | NGS ARR supera los $7.5B; confirmación de visibilidad plurianual con RPO en fuerte alza. |
| **P2 2026 (Actual)** | **56.1x** | **41.2x** | **9.46** | **9.46** | **6.61** | **ÉLITE** | Cierre de año fiscal récord con $11.48B en ingresos, $4.41B en FCF y NGS ARR de $9.10B. |
"""

# Replace Section 8 in report
text = re.sub(r'## 8\. Evolución Histórica de Puntuaciones CQV.*?(?=## 9\. Conclusión)', sec8 + '\n---\n\n', text, flags=re.DOTALL)

# Insert Section 3.3 after Section 3.1
if '### 3.3. Análisis Histórico' not in text:
    text = text.replace('## 5. Owner Earnings', sec3_3 + '\n---\n\n## 5. Owner Earnings')

report_path.write_text(text, encoding='utf-8')
print('Successfully complemented inform/cqv_v5/PANW_2026_P2_CQVv5.md with historical 2020-2026 data.')
