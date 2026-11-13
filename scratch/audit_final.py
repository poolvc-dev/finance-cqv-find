import os
import json

DATA_FILE = "cqv_data.json"
data = json.load(open(DATA_FILE, encoding='utf-8'))
data_map = {x['ticker']: x for x in data}

tickers = ['TSLA', 'META', 'LRCX', 'MEDP', 'TMO', 'PM', 'CME', 'ABT', 'TXN']

print(f"{'Ticker':<6} | {'Period':<7} | {'CQV v5':<6} | {'VS':<5} | {'PEG':<6} | {'FCF_Y':<6} | {'MoS':<7} | {'Verdict':<10} | {'Report Exists':<13} | {'Size (KB)'}")
print("-" * 90)

for t in tickers:
    rec = data_map.get(t, {})
    rep_path = f"inform/cqv_v5/{t}_2026_P3_CQVv5.md"
    exists = os.path.exists(rep_path)
    size_kb = round(os.path.getsize(rep_path) / 1024, 1) if exists else 0
    cqv = rec.get('cqv_v5', 'N/D')
    vs = rec.get('value_score', 'N/D')
    peg = round(rec.get('peg_bruto', 0), 2) if rec.get('peg_bruto') else 'N/D'
    fcf_y = f"{round(rec.get('fcf_yield_pct', 0), 2)}%" if rec.get('fcf_yield_pct') else 'N/D'
    mos = f"{round(rec.get('mos_pct', 0), 1)}%" if rec.get('mos_pct') else 'N/D'
    verd = rec.get('verdict', 'N/D')
    q = rec.get('quarter', 'N/D')
    print(f"{t:<6} | {q:<7} | {cqv:<6} | {vs:<5} | {str(peg):<6} | {str(fcf_y):<6} | {str(mos):<7} | {verd:<10} | {str(exists):<13} | {size_kb} KB")
