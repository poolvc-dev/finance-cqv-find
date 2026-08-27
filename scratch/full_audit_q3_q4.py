import json, os

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_data = json.load(f)
with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

print(f"Total registros en cqv_data.json: {len(cqv_data)}")
print(f"Total empresas en cqv_history.json: {len(cqv_hist)}")

# 1. Audit cqv_data.json
q3_data = []
q4_data = []
other_2026_2027 = []

for item in cqv_data:
    q = str(item.get('quarter', '')).strip()
    ticker = item.get('ticker')
    name = item.get('name')
    val_date = item.get('valuation_date')
    
    if 'Q3' in q and '2026' in q:
        q3_data.append((ticker, name, q, val_date))
    elif 'Q4' in q and '2026' in q:
        q4_data.append((ticker, name, q, val_date))
    elif '2026' in q or '2027' in q:
        other_2026_2027.append((ticker, name, q, val_date))

print("\n--- 1. AUDITORÍA EXHAUSTIVA DE CQV_DATA.JSON ---")
print(f"Empresas en Q3 2026 en cqv_data.json: {len(q3_data)}")
for t, n, q, d in q3_data:
    print(f"  • {t:<6} | {n:<35} | Quarter: {q:<10} | Valuation Date: {d}")

print(f"\nEmpresas en Q4 2026 en cqv_data.json: {len(q4_data)}")
for t, n, q, d in q4_data:
    print(f"  • {t:<6} | {n:<35} | Quarter: {q:<10} | Valuation Date: {d}")

# 2. Audit cqv_history.json
print("\n--- 2. AUDITORÍA EXHAUSTIVA DE CQV_HISTORY.JSON (AÑO 2026 EN ADELANTE) ---")
q3_hist = []
q4_hist = []

for ticker, years in cqv_hist.items():
    if '2026' in years and isinstance(years['2026'], dict):
        for q_key, val in years['2026'].items():
            if val is not None and isinstance(val, dict):
                if q_key == 'Q3':
                    q3_hist.append((ticker, val.get('quarter'), val.get('valuation_date')))
                elif q_key == 'Q4':
                    q4_hist.append((ticker, val.get('quarter'), val.get('valuation_date')))

print(f"Empresas con registro Q3 2026 no nulo en cqv_history.json: {len(q3_hist)}")
for t, q, d in q3_hist:
    print(f"  • {t:<6} | Quarter: {q:<10} | Valuation Date: {d}")

print(f"\nEmpresas con registro Q4 2026 no nulo en cqv_history.json: {len(q4_hist)}")
for t, q, d in q4_hist:
    print(f"  • {t:<6} | Quarter: {q:<10} | Valuation Date: {d}")

# 3. Audit inform/ directory
inform_files = os.listdir('inform')
q3_inform = [f for f in inform_files if '2026_Q3' in f.upper()]
q4_inform = [f for f in inform_files if '2026_Q4' in f.upper()]

print("\n--- 3. AUDITORÍA DE ARCHIVOS EN INFORM/ ---")
print(f"Informes Q3 2026 en inform/: {q3_inform}")
print(f"Informes Q4 2026 en inform/: {q4_inform}")
