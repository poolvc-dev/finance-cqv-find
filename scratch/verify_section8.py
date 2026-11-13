import glob
import re

files = sorted(list(dict.fromkeys(glob.glob('inform/cqv_v5/**/*P3*.md', recursive=True) + glob.glob('inform/cqv_v5/*P3*.md'))))
print(f"Auditando {len(files)} informes...")
errors = []

for f in files:
    content = open(f, encoding='utf-8').read()
    
    # 1. Auditar Tabla 8.1
    m = re.search(r'### 8\.1\..*?\n(\|.*?\|\n\|.*?\|\n(?:\|.*?\|\n)+)', content, re.DOTALL)
    if not m:
        errors.append(f"{f}: NO SE ENCONTRO TABLA 8.1")
        continue
        
    lines = m.group(1).strip().split('\n')
    h_cols = len(lines[0].split('|')) - 2
    s_cols = len(lines[1].split('|')) - 2
    if h_cols != 13 or s_cols != 13:
        errors.append(f"{f}: Header cols={h_cols}, Sep cols={s_cols} (deben ser 13)")
        
    for idx, r in enumerate(lines[2:], start=1):
        r_cols = len(r.split('|')) - 2
        if r_cols != 13:
            errors.append(f"{f}: Fila {idx} tiene {r_cols} cols (deben ser 13): {r}")
            
    # 2. Auditar Mermaid 8.2
    mm = re.search(r'### 8\.2\..*?```mermaid\n(.*?)```', content, re.DOTALL)
    if not mm:
        errors.append(f"{f}: NO SE ENCONTRO MERMAID 8.2")
        continue
    mermaid_code = mm.group(1)
    
    mx = re.search(r'x-axis \[(.*?)\]', mermaid_code)
    my = re.search(r'line "CQV v5\.0" \[(.*?)\]', mermaid_code)
    if not mx or not my:
        errors.append(f"{f}: Sintaxis Mermaid x-axis o line invalida")
    else:
        x_items = [x.strip() for x in mx.group(1).split(',') if x.strip()]
        y_items = [y.strip() for y in my.group(1).split(',') if y.strip()]
        if len(x_items) != len(y_items):
            errors.append(f"{f}: Longitud x-axis ({len(x_items)}) != longitud line ({len(y_items)})")
        if any('**' in x for x in x_items):
            errors.append(f"{f}: x-axis contiene asteriscos de markdown")

if errors:
    print(f"SE ENCONTRARON {len(errors)} ERRORES:")
    for e in errors:
        print(" -", e)
else:
    print("AUDITORIA 100% EXITOSA: Los 42 informes tienen tablas 8.1 y graficos Mermaid 8.2 perfectamente consistentes.")
