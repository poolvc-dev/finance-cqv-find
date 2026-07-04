import yfinance as yf
import pandas as pd
import numpy as np
import json
import concurrent.futures
import time

def clean_value(val):
    if val is None or np.isnan(val) or np.isinf(val):
        return None
    return float(val)

# Load current CQV results to get tickers and qualitative scores
try:
    current_df = pd.read_csv('cqv_results.csv')
    print(f"Loaded {len(current_df)} tickers from cqv_results.csv")
except Exception as e:
    print("Error loading cqv_results.csv:", e)
    import sys
    sys.exit(1)

# Clean tickers mapping (from calculate_cqv.py)
TICKER_MAP = {
    'BXSX': 'BSX',     # Boston Scientific
    'FDRL': 'FND',     # Floor & Decor (probable typo for FND)
    'BRK': 'BRK-B',    # Berkshire Hathaway
    'CSU': 'CSU.TO',   # Constellation Software
    'LVMH': 'MC.PA',   # LVMH Moet Hennessy
    'MRSH': 'MMC',     # Marsh & McLennan
    'OR': 'ORA',       # Ormat Technologies
    'RMS': 'RMS.PA',   # Hermes International
    'TDD': 'TTD',      # The Trade Desk
}

# Reverse mapping for output compatibility
REV_MAP = {v: k for k, v in TICKER_MAP.items()}

# We want to extract history for all successfully processed tickers
companies_list = current_df.to_dict(orient='records')

def get_sector_and_qual(ticker):
    # Retrieve F4, F5 and sector from current results
    row = current_df[current_df['ticker'] == ticker]
    if not row.empty:
        # We need to map the ticker to the Yahoo Finance ticker
        yf_ticker = ticker
        if ticker in TICKER_MAP:
            yf_ticker = TICKER_MAP[ticker]
        return row.iloc[0]['f4'], row.iloc[0]['f5'], row.iloc[0]['f1'], row.iloc[0]['f2'], row.iloc[0]['f3']
    return 8.0, 8.0, 8.0, 8.0, 8.0

def process_history(company):
    ticker = company['ticker']
    # Map to yfinance ticker
    yf_ticker = ticker
    if ticker in TICKER_MAP:
        yf_ticker = TICKER_MAP[ticker]
        
    print(f"Processing history for {ticker} (using {yf_ticker})...")
    
    try:
        t = yf.Ticker(yf_ticker)
        fin = t.financials
        bs = t.balance_sheet
        cf = t.cashflow
        
        if fin.empty or bs.empty or cf.empty:
            return {'ticker': ticker, 'error': 'Missing financial statements'}
            
        # Get sorted list of years
        years = sorted(list(fin.columns))
        # Keep only the last 5 years
        years = years[-5:]
        
        # Qualitative scores from the current audit (assumed constant)
        f4_moat, f5_proj, curr_f1, curr_f2, curr_f3 = get_sector_and_qual(ticker)
        
        # Sector predictability default (from calculate_cqv.py logic)
        # We'll approximate this by checking current F2 and current Debt score
        # predictability = current_F2 * 2 - debt_score
        # For simplicity, we just use a default predictability score of 8.5
        pred_score = 8.5
        
        history_scores = {}
        
        # Helper to get value from DataFrame safely
        def get_val(df, keys, year):
            for k in keys:
                if k in df.index:
                    val = df.loc[k, year]
                    if isinstance(val, pd.Series):
                        val = val.iloc[0]
                    if val is not None and not np.isnan(val) and not np.isinf(val):
                        return float(val)
            return None

        # Build year-by-year metrics dictionary
        yearly_metrics = {}
        for y in years:
            y_str = str(y)[:4] # e.g. "2024"
            
            rev = get_val(fin, ['Total Revenue', 'Revenue'], y)
            ebitda = get_val(fin, ['EBITDA'], y)
            op_inc = get_val(fin, ['Operating Income', 'EBIT'], y)
            net_inc = get_val(fin, ['Net Income', 'Net Income Common Stockholders'], y)
            
            cash = get_val(bs, ['Cash And Cash Equivalents', 'Cash Cash Equivalents And Short Term Investments', 'Cash'], y)
            debt = get_val(bs, ['Total Debt'], y)
            if debt is None:
                st_debt = get_val(bs, ['Current Debt', 'Short Long Term Debt'], y) or 0.0
                lt_debt = get_val(bs, ['Long Term Debt'], y) or 0.0
                debt = st_debt + lt_debt
                
            ocf = get_val(cf, ['Operating Cash Flow', 'Cash Flow From Operating Activities'], y)
            capex = get_val(cf, ['Capital Expenditure'], y)
            
            yearly_metrics[y_str] = {
                'rev': rev,
                'ebitda': ebitda,
                'op_inc': op_inc,
                'net_inc': net_inc,
                'cash': cash,
                'debt': debt,
                'ocf': ocf,
                'capex': capex
            }
            
        # Calculate CQV for each year
        year_keys = sorted(list(yearly_metrics.keys()))
        for i, y_str in enumerate(year_keys):
            metrics = yearly_metrics[y_str]
            rev = metrics['rev']
            ebitda = metrics['ebitda']
            op_inc = metrics['op_inc']
            net_inc = metrics['net_inc']
            cash = metrics['cash']
            debt = metrics['debt']
            ocf = metrics['ocf']
            capex = metrics['capex']
            
            if rev is None or rev <= 0:
                continue
                
            # 1. Rentabilidad (F1)
            margin = max((ebitda or 0) / rev, (op_inc or 0) / rev)
            if margin >= 0.35:
                margin_score = 10.0
            elif margin >= 0.15:
                margin_score = 7.0 + 3.0 * (margin - 0.15) / 0.20
            elif margin >= 0.05:
                margin_score = 5.0 + 2.0 * (margin - 0.05) / 0.10
            else:
                margin_score = max(1.0, 5.0 * margin / 0.05)
                
            # ROIC approximation (scale current F1 by margin trend, or use ROA proxy)
            # Since we don't have total assets for all years easily, let's use margin_score as a proxy for ROIC score
            # or keep it close to current_F1
            roic_score = min(10.0, max(1.0, curr_f1 * (margin_score / 10.0 + 0.3)))
            
            # FCF conversion
            fcf = 0.0
            if ocf is not None:
                fcf = ocf + (capex or 0.0) # capex is usually negative in statement
            else:
                fcf = (ebitda or 0.0) * 0.6
                
            if net_inc is not None and net_inc > 0:
                conversion = fcf / net_inc
            else:
                conversion = fcf / ((ebitda or 1.0) * 0.7)
                
            if conversion >= 1.0:
                conversion_score = 10.0
            elif conversion >= 0.5:
                conversion_score = 7.0 + 3.0 * (conversion - 0.5) / 0.5
            else:
                conversion_score = max(1.0, 7.0 * conversion / 0.5)
                
            f1 = (margin_score + roic_score + conversion_score) / 3.0
            
            # 2. Solidez (F2)
            ebitda_val = ebitda if ebitda and ebitda > 0 else (op_inc if op_inc and op_inc > 0 else rev * 0.1)
            net_debt = (debt or 0.0) - (cash or 0.0)
            debt_ebitda = net_debt / ebitda_val
            
            if net_debt <= 0:
                debt_score = 10.0
            elif debt_ebitda <= 1.5:
                debt_score = 9.5
            elif debt_ebitda <= 4.0:
                debt_score = 9.5 - 4.5 * (debt_ebitda - 1.5) / 2.5
            else:
                debt_score = max(1.0, 5.0 - 4.0 * (debt_ebitda - 4.0) / 6.0)
                
            f2 = (debt_score + pred_score) / 2.0
            
            # 3. Crecimiento (F3)
            # Calculate year-over-year revenue growth
            growth = 0.07 # default if no previous year
            if i > 0:
                prev_y_str = year_keys[i-1]
                prev_rev = yearly_metrics[prev_y_str]['rev']
                if prev_rev and prev_rev > 0:
                    growth = (rev - prev_rev) / prev_rev
                    
            if growth >= 0.15:
                growth_score = 10.0
            elif growth >= 0.06:
                growth_score = 7.0 + 3.0 * (growth - 0.06) / 0.09
            else:
                growth_score = max(1.0, 5.0 + 2.0 * (growth / 0.06))
                
            # M&A and Dilution default (using current values as proxy)
            # F3 = (growth_score + ma_score + dilution_score) / 3.0
            # Since current_F3 = (curr_growth_score + curr_ma + curr_dilution) / 3.0
            # We will approximate historical F3 by adjusting current F3 by the growth score change:
            f3 = min(10.0, max(1.0, curr_f3 + (growth_score - 8.0) * 0.15))
            
            # 4. Moat (F4) and 5. Proyeccion (F5) are constant
            cqv = (f1 * 0.25) + (f2 * 0.15) + (f3 * 0.15) + (f4_moat * 0.25) + (f5_proj * 0.20)
            cqv = round(cqv, 2)
            
            history_scores[y_str] = {
                'f1': round(f1, 2),
                'f2': round(f2, 2),
                'f3': round(f3, 2),
                'cqv': cqv
            }
            
        print(f"Computed history for {ticker}: {list(history_scores.keys())}")
        return {
            'ticker': ticker,
            'history': history_scores,
            'status': 'Success'
        }
        
    except Exception as e:
        print(f"Error computing history for {ticker}: {e}")
        return {'ticker': ticker, 'status': 'Error', 'error': str(e)}

def main():
    print("Starting processing of 5-year CQV history...")
    history_db = {}
    
    # Process in parallel with ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_company = {executor.submit(process_history, c): c for c in companies_list}
        for future in concurrent.futures.as_completed(future_to_company):
            c = future_to_company[future]
            ticker = c['ticker']
            try:
                res = future.result()
                if res.get('status') == 'Success':
                    history_db[ticker] = res['history']
            except Exception as exc:
                print(f"{ticker} generated an exception: {exc}")
                
    # Save raw JSON data to cqv_history.json
    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(history_db, f, indent=2)
    print("Successfully created cqv_history.json")
    
    # Save JS wrapper to cqv_history.js
    js_content = f"const cqvHistoryData = {json.dumps(history_db, indent=2)};"
    with open('cqv_history.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("Successfully created cqv_history.js")

if __name__ == "__main__":
    main()
