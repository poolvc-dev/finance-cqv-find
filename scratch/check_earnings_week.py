import json
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

p2_tickers = [x['ticker'] for x in data if 'P2' in x.get('quarter', '') or 'P1' in x.get('quarter', '')]
print(f'Checking {len(p2_tickers)} tickers for earnings between 2026-11-09 and 2026-11-12...')

target_dates = ['2026-11-09', '2026-11-10', '2026-11-11', '2026-11-12']

def check_ticker(ticker):
    try:
        t = yf.Ticker(ticker)
        # Check earnings dates
        ed = t.earnings_dates
        if ed is not None and not ed.empty:
            for idx in ed.index:
                dt_str = str(idx)[:10]
                if dt_str in target_dates:
                    eps_est = ed.loc[idx].get('EPS Estimate')
                    rep_eps = ed.loc[idx].get('Reported EPS')
                    surp = ed.loc[idx].get('Surprise(%)')
                    return (ticker, dt_str, eps_est, rep_eps, surp)
    except Exception as e:
        pass
    return None

matches = []
with ThreadPoolExecutor(max_workers=20) as executor:
    futures = {executor.submit(check_ticker, t): t for t in p2_tickers}
    for f in as_completed(futures):
        res = f.result()
        if res:
            matches.append(res)
            print(f'MATCH: {res[0]} reported on {res[1]} (EPS: {res[3]} vs Est: {res[2]}, Surp: {res[4]})')

print(f'\nTotal matches found: {len(matches)}')
matches.sort(key=lambda x: x[1])
for m in matches:
    print(m)

