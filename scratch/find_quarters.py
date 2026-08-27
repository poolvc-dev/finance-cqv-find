import json

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_data = json.load(f)
with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

print("=== CHECK DE COMPAÑÍAS CON REGISTROS EN CQV_HISTORY.JSON EN 2026 (Q3 O Q4) ===")
q3_history = []
q4_history = []

for ticker, years in cqv_hist.items():
    if '2026' in years:
        if 'Q3' in years['2026'] and years['2026']['Q3'] is not None:
            q3_history.append(ticker)
        if 'Q4' in years['2026'] and years['2026']['Q4'] is not None:
            q4_history.append(ticker)

print(f"\nEmpresas con registro Q3 2026 en cqv_history.json ({len(q3_history)}):")
for t in sorted(q3_history):
    print("  •", t)

print(f"\nEmpresas con registro Q4 2026 en cqv_history.json ({len(q4_history)}):")
for t in sorted(q4_history):
    print("  •", t)
