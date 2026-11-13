import json
import glob
import os

hist = json.load(open('cqv_history.json', encoding='utf-8'))
now = hist.get('NOW', {})
print("=== HISTORIAL DE NOW ===")
for y in sorted(now.keys()):
    if y.startswith('_') or y == 'annual_legacy':
        continue
    for p in ['P1', 'P2', 'P3', 'P4']:
        s = now[y].get(p)
        if s:
            print(f"{y} {p} -> F4 (Moat): {s.get('f4')} | CQV: {s.get('cqv_v5') or s.get('cqv')} | F1: {s.get('f1')} | F3: {s.get('f3')} | F5: {s.get('f5')} | F8: {s.get('f8')}")

print("\n=== BUSCANDO TESIS O INFORMES PREVIOS DE NOW ===")
for path in glob.glob('inform/**/*.md', recursive=True) + glob.glob('tesis/**/*.md', recursive=True):
    if 'NOW' in os.path.basename(path).upper():
        print("Encontrado:", path)
