import json

data = json.load(open('cqv_data.json', encoding='utf-8'))
tickers = {'MEDP', 'TMO', 'ABT', 'CME', 'PM'}
for x in data:
    if x.get('ticker') in tickers:
        print(f"{x['ticker']}: cqv_v5={x.get('cqv_v5')}, VS={x.get('value_score')}, PEG={x.get('peg_bruto')}, FCF_Y={x.get('fcf_yield_pct')}, MoS={x.get('mos_pct')}, Verdict={x.get('verdict')}, Class={x.get('clasificacion')}")
