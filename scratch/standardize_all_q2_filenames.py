import json
import os

data = json.load(open('cqv_data.json', encoding='utf-8'))
q2_companies = {d['ticker']: d for d in data if d.get('quarter') == 'Q2 2026'}

print(f"Total Q2 2026 tickers in SSOT: {len(q2_companies)}")

inform_files = os.listdir('inform')

# Alias map for tickers with different names
ALIAS_MAP = {
    'APPLE': 'AAPL',
    'FORTINET': 'FTNT',
    'PAYPAL': 'PYPL',
    'VISA': 'V'
}

renamed = 0
created = 0

for comp_ticker, comp_data in q2_companies.items():
    upper_ticker = comp_ticker.upper()
    target_name = f"{upper_ticker}_2026_Q2.md"
    target_path = os.path.join('inform', target_name)

    # Find existing candidates
    candidates = []
    for f in inform_files:
        if '2026' in f and ('q2' in f.lower() or 'Q2' in f):
            prefix = f.split('_')[0].upper()
            if prefix == upper_ticker or ALIAS_MAP.get(prefix) == upper_ticker:
                candidates.append(f)

    if not os.path.exists(target_path):
        if candidates:
            src = candidates[0]
            src_path = os.path.join('inform', src)
            print(f"Renaming {src} -> {target_name}")
            os.rename(src_path, target_path)
            renamed += 1
            # Remove remaining duplicates
            for dup in candidates[1:]:
                dup_path = os.path.join('inform', dup)
                if os.path.exists(dup_path):
                    os.remove(dup_path)
        else:
            print(f"Creating new report for {target_name}")
            created += 1

# Re-audit and format all 117 uppercase reports to match cqv_data.json
exec(open('scratch/audit_and_generate_q2_reports.py', encoding='utf-8').read())
