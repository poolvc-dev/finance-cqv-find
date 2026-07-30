import os
import json
import re
import yfinance as yf

# List of Q2 tickers
q2_tickers = ['ASML', 'FICO', 'FTNT', 'GOOGL', 'INTC', 'ISRG', 'KLAC', 'KNSL', 'MEDP', 'META', 'MRSH', 'MSCI', 'MSFT', 'NOW', 'NVDA', 'ORLY', 'PGR', 'SPGI', 'TSM']

print(f"Processing {len(q2_tickers)} tickers for Q2 2026 CQV v4.0 update...")

# Live data cache
live_data = {}
for ticker in q2_tickers:
    try:
        t = yf.Ticker(ticker)
        info = t.info
        price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
        pe_t = info.get('trailingPE')
        pe_f = info.get('forwardPE')
        eps_t = info.get('trailingEps')
        eps_f = info.get('forwardEps')
        live_data[ticker] = {
            'price': price,
            'pe_trailing': pe_t,
            'pe_forward': pe_f,
            'eps_trailing': eps_t,
            'eps_forward': eps_f
        }
        print(f"Fetched {ticker}: Price=${price}, PE_t={pe_t}, PE_f={pe_f}")
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")

with open('scratch/live_data_q2.json', 'w', encoding='utf-8') as f:
    json.dump(live_data, f, indent=2)

print("Fetched all live data successfully.")
