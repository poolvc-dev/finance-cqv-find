import json, os

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_data = json.load(f)

# Get all Q2 2026 items in cqv_data.json
q2_items = [x for x in cqv_data if x.get('quarter') == 'Q2 2026']

# Get all files in inform/
inform_files = os.listdir('inform')
q2_inform_files = [f for f in inform_files if '2026_Q2' in f.upper()]

# Tickers with Q2 report files
q2_report_map = {}
for f in q2_inform_files:
    ticker = f.split('_')[0].upper()
    q2_report_map[ticker] = f

print(f"Total empresas con quarter == 'Q2 2026' en cqv_data.json: {len(q2_items)}")
print(f"Total informes Q2 2026 en inform/: {len(q2_report_map)} distinct tickers ({len(q2_inform_files)} files)")

print("\n==========================================================================")
print("=== AUDITORÍA 1: EMPRESAS QUE TIENEN INFORME Q2 2026 EN INFORM/ ===")
print("==========================================================================")
for t, filename in sorted(q2_report_map.items()):
    match = [x for x in cqv_data if x.get('ticker') == t]
    if match:
        m = match[0]
        q_data = m.get('quarter')
        v_date = str(m.get('valuation_date'))
        status = m.get('status')
        print(f"  • {t:<6} | Data Quarter: {q_data:<8} | Val Date: {v_date:<12} | Status: {status} | File: {filename}")
    else:
        print(f"  • {t:<6} | (NO EXISTE EN CQV_DATA.JSON) | File: {filename}")

print("\n==========================================================================")
print("=== AUDITORÍA 2: EMPRESAS EN CQV_DATA.JSON CON QUARTER == 'Q2 2026' PERO SIN INFORME MARKDOWN ===")
print("==========================================================================")
q2_without_report = [x for x in q2_items if x.get('ticker') not in q2_report_map]
print(f"Total: {len(q2_without_report)} empresas")
for m in sorted(q2_without_report, key=lambda x: x.get('ticker')):
    t = m.get('ticker')
    v_date = str(m.get('valuation_date'))
    status = m.get('status')
    cqv = m.get('cqv_v4')
    print(f"  • {t:<6} | Name: {m.get('name'):<38} | Val Date: {v_date:<12} | Status: {status} | CQV: {cqv}")
