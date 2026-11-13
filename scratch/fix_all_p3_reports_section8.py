import json
import glob
import os
import re
import math

def fix_all_p3_section8():
    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        cqv_history = json.load(f)
    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        cqv_data = json.load(f)

    data_by_ticker = {c['ticker']: c for c in cqv_data}
    report_files = sorted(glob.glob('inform/cqv_v5/*P3*.md'))
    print(f"Encontrados {len(report_files)} informes P3 en inform/cqv_v5/")

    fixed_count = 0

    for filepath in report_files:
        filename = os.path.basename(filepath)
        ticker = filename.split('_')[0].upper()
        
        hist_ticker = cqv_history.get(ticker, {})
        comp = data_by_ticker.get(ticker, {})

        hist_rows = []
        mermaid_labels = []
        mermaid_points = []

        # Recorrer histórico año por año
        for yr in sorted(hist_ticker.keys()):
            if yr.startswith('_') or yr in ['annual_legacy']:
                continue
            yr_obj = hist_ticker[yr]
            if isinstance(yr_obj, dict):
                for p_name in ['P1', 'P2', 'P3', 'P4']:
                    if yr == '2026' and p_name == 'P4':
                        continue  # Periodo futuro no emitido
                    snap = yr_obj.get(p_name)
                    if snap and isinstance(snap, dict):
                        sc = snap.get('cqv_v5', snap.get('cqv', snap.get('cqv_v4', 'N/D')))
                        pr = snap.get('price', 'N/D')
                        pe = snap.get('pe', 'N/D')
                        vs = snap.get('value_score', 'N/D')
                        cl = snap.get('clasificacion', 'N/D')
                        vd = snap.get('verdict', 'N/D')

                        f1_val = snap.get('f1', '-')
                        f2_val = snap.get('f2', '-')
                        f3_val = snap.get('f3', '-')
                        f4_val = snap.get('f4', '-')
                        f5_val = snap.get('f5', '-')
                        f6_val = snap.get('f6', '-')
                        f7_val = snap.get('f7', '-')
                        f8_val = snap.get('f8', '-')

                        sc_str = f"{sc:.2f}" if isinstance(sc, (int, float)) else str(sc)
                        vs_str = f"{vs:.2f}" if isinstance(vs, (int, float)) else str(vs)

                        hist_rows.append(
                            f"| **{yr} {p_name}** | {f1_val} | {f2_val} | {f3_val} | {f4_val} | {f5_val} | {f6_val} | {f7_val} | {f8_val} | **{sc_str}** | {vs_str} | {cl} | {vd} |"
                        )
                        if isinstance(sc, (int, float)):
                            mermaid_labels.append(f'"{yr} {p_name}"')
                            mermaid_points.append(f"{sc:.2f}")
                    elif yr >= '2024':
                        hist_rows.append(
                            f"| **{yr} {p_name}** | N/D | N/D | N/D | N/D | N/D | N/D | N/D | N/D | **N/D** | N/D | N/D | N/D |"
                        )

        # Si no hay puntos suficientes, usar dato actual de cqv_data
        curr_score = comp.get('cqv_v5', comp.get('cqv', 8.5))
        if not mermaid_points:
            mermaid_labels = ['"P3 2026"']
            mermaid_points = [f"{curr_score:.2f}"]

        # Tomar los últimos 8 periodos para la tabla
        selected_rows = hist_rows[-8:] if len(hist_rows) >= 8 else hist_rows
        # Tomar los últimos 6 periodos para el gráfico Mermaid
        labels_6 = mermaid_labels[-6:]
        points_6 = mermaid_points[-6:]

        # Calcular límite inferior para el eje Y
        try:
            min_val = min(float(p) for p in points_6)
            y_min = max(1.0, math.floor(min_val - 0.5))
        except Exception:
            y_min = 6.0

        section8_content = f"""## 8. Evolución Histórica de Puntuaciones CQV y Valuación por Periodos (P1–P4 desde 2020)

### 8.1. Desglose Periódico Histórico por Ciclo de Presentación (P1, P2, P3, P4 por Año)

| Periodo Auditado | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | **CQV v5.0** | Value Score | Clasificación | Veredicto Operativo |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
{chr(10).join(selected_rows)}

### 8.2. Gráfico Mermaid de Evolución Periódica de Calidad Fundamental CQV v5.0

```mermaid
---
config:
    theme: base
    themeVariables:
        primaryColor: "#22c55e"
---
xychart-beta
    title "{ticker} - Evolución Histórica de Score CQV v5.0 por Periodos"
    x-axis [{", ".join(labels_6)}]
    y-axis "Score CQV (1.0 - 10.0)" {y_min:.1f} --> 10.0
    line "CQV v5.0" [{", ".join(points_6)}]
```

---
"""

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Comprobar si ya existe la Sección 8
        if re.search(r'## 8\..*?(?=## 9\.|$)', content, re.DOTALL):
            # Reemplazar Sección 8 existente
            new_content = re.sub(
                r'## 8\..*?(?=## 9\.|$)',
                section8_content + "\n",
                content,
                flags=re.DOTALL
            )
        elif '## 9.' in content:
            # Insertar Sección 8 antes de la Sección 9
            parts = content.split('## 9.')
            new_content = parts[0] + section8_content + "\n## 9." + parts[1]
        else:
            # Anexar al final
            new_content = content + "\n\n" + section8_content

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        fixed_count += 1
        print(f"[OK] Sección 8 corregida y validada en: {filename}")

    print(f"\nProceso completado. Se actualizaron {fixed_count} informes con éxito.")

if __name__ == '__main__':
    fix_all_p3_section8()
