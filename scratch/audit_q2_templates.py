import os, re

inform_dir = 'inform'
files = [f for f in os.listdir(inform_dir) if f.endswith('_2026_Q2.md') and f[0].isupper()]

complete = []
incomplete = []

for filename in sorted(files):
    filepath = os.path.join(inform_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check key sections required by template.md
    has_sec1 = '## 1.' in content or '# 1.' in content
    has_sec2 = '## 2.' in content or '# 2.' in content
    has_sec3 = '## 3.' in content or '# 3.' in content
    has_sec34 = '3.4' in content
    has_sec35 = '3.5' in content
    has_sec4 = '## 4.' in content or '# 4.' in content
    has_sec5 = '## 5.' in content or '# 5.' in content
    has_sec6 = '## 6.' in content or '# 6.' in content
    has_sec7 = '## 7.' in content or '# 7.' in content
    has_sec8 = '## 8.' in content or '# 8.' in content
    has_sec9 = '## 9.' in content or '# 9.' in content
    has_sec10 = '## 10.' in content or '# 10.' in content
    has_mermaid = 'mermaid' in content
    line_count = len(content.splitlines())
    
    is_full = (has_sec1 and has_sec2 and has_sec3 and has_sec34 and has_sec35 and 
               has_sec4 and has_sec5 and has_sec6 and has_sec7 and has_sec8 and 
               has_sec9 and has_sec10 and has_mermaid and line_count > 150)
    
    info = {
        'file': filename,
        'line_count': line_count,
        'has_34': has_sec34,
        'has_35': has_sec35,
        'has_10': has_sec10,
        'is_full': is_full
    }
    
    if is_full:
        complete.append(info)
    else:
        incomplete.append(info)

print(f"Total archivos *_2026_Q2.md auditados: {len(files)}")
print(f"Informes 100% COMPLETOS según template.md (10 secciones + 3.4 + 3.5 + Mermaid): {len(complete)}")
print(f"Informes INCOMPLETOS o con formato antiguo: {len(incomplete)}")

print("\n--- INFORMES COMPLETOS ---")
for x in complete:
    print(f"  [OK] {x['file']:<20} | Líneas: {x['line_count']}")

print("\n--- INFORMES INCOMPLETOS / A ACTUALIZAR ---")
for x in incomplete:
    reasons = []
    if not x['has_34']: reasons.append('Falta 3.4 (Tendencia)')
    if not x['has_35']: reasons.append('Falta 3.5 (Guidance)')
    if not x['has_10']: reasons.append('Falta Sec 10 (Auditoría)')
    if x['line_count'] < 100: reasons.append(f"Muy corto ({x['line_count']} líneas)")
    print(f"  [PENDIENTE] {x['file']:<20} | Líneas: {x['line_count']:<4} | Motivos: {', '.join(reasons)}")
