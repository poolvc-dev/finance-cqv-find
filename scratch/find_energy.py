import json

with open('cqv_data.json', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total companies in cqv_data.json: {len(data)}")

sectors = set()
for d in data:
    sec = d.get('sector')
    if sec:
        sectors.add(sec)

print("\n--- All Sectors in Dataset ---")
for s in sorted(list(sectors)):
    print(" -", s)

print("\n--- Searching energy / oil / gas / utility / power / solar / nuclear ---")
matches = []
for d in data:
    sec = str(d.get('sector', '')).lower()
    name = str(d.get('name', '')).lower()
    t = d.get('ticker')
    if any(k in sec or k in name for k in ['energy', 'oil', 'gas', 'utility', 'utilities', 'power', 'solar', 'nuclear', 'refining', 'pipeline']):
        matches.append(d)

print(f"\nFound {len(matches)} matching companies:")
for m in sorted(matches, key=lambda x: x.get('cqv_v4') or x.get('cqv') or 0, reverse=True):
    cqv = m.get('cqv_v4') or m.get('cqv')
    print(f"Ticker: {m.get('ticker'):<6} | CQV: {cqv:<5} | Class: {m.get('clasificacion'):<16} | Name: {m.get('name')}")
