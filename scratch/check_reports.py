import json
import os

data = json.load(open('cqv_data.json', encoding='utf-8'))
q2_tickers = [d for d in data if d.get('quarter') == 'Q2 2026']

print(f"Total Q2 2026 companies in cqv_data.json: {len(q2_tickers)}")

existing_files = os.listdir('inform')
file_map = {f.lower(): f for f in existing_files}

missing = []
existing = []

for comp in q2_tickers:
    t = comp['ticker']
    expected_upper = f"{t.upper()}_2026_Q2.md"
    expected_lower = f"{t.lower()}_2026_q2.md"
    
    if expected_upper in existing_files:
        existing.append((t, expected_upper, 'exact'))
    elif expected_lower.lower() in file_map:
        existing.append((t, file_map[expected_lower.lower()], 'case_mismatch'))
    else:
        missing.append(t)

print(f"Existing reports: {len(existing)}")
print(f"Missing reports: {len(missing)}")
print("\nMissing tickers:", missing)
