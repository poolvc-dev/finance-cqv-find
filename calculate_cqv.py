import yfinance as yf
import pandas as pd
import numpy as np
import concurrent.futures
import time
import sys

# Define the tickers
raw_tickers = """
ABB,AAPL, ACN,ADBE,ADI,AJG,AMAT,AMD,AMZN,ANET,APH,APO,APP,ASML,AVGO,AXON,AXP,AZO,
BABA,BAH,BJ,BKNG,BLDR,BMI,BRK=BRK-B,BRO,BXSX
CAT,CDNS,CEG,CHDN,COR,COST,CPRT,CRM,CRVL,CRWD,CSL,CSU=CSU.TO,CTAS,
DECK,DRS,DSGX,
EL,EME,EPAM,ETN,EXLS,
FAST,FICO,FIX,FLEX,FN,FDRL,FSS,FTNT,
GE,GEV,GOOGL,GWW,
HCA,HD,HEI,HLI,HLT,HWM,
IDXX,INFY,INTU,ISRG,IT,
JBL,JPM,
KBR,KLAC,KNSL,
LIN,LLY,LOW,LPLA,LRCX,LVMH=MC.PA,
MA,MANH,MCK,MCO,MEDP,MELI,META,MLI,MOH,MPC,MPWR,MRSH=MMC,MSCI,MSFT,MSI,MU,MUSA,
NFLX,NOW,NTRA,NVDA,NVO,NVR,
ODFL,OR=ORA,ORCL,ORLY,
PANW,PGR,PH,PLTR,POOL,PRI,PWR,PYPL,
RACE,RJF,RLI,RMS=RMS.PA,RS,
SAP,SHOP,SHW,SKY,SMH,SPGI,SPOT,
TDG,TEL,TKO,TMUS,TPL,TSLA,TSM,TT,TDD=TTD,TTEK,TW,
UBER,UNH,URI,
V,VRSK,VRT,
WCN,WM,WMT,WTS,WWD
"""

# Helper dictionaries for mappings
TICKER_MAP = {
    'BXSX': 'BSX',     # Boston Scientific
    'FDRL': 'FND',     # Floor & Decor (probable typo for FND)
    'BRK': 'BRK-B',    # Berkshire Hathaway
    'CSU': 'CSU.TO',   # Constellation Software
    'LVMH': 'MC.PA',   # LVMH Moet Hennessy
    'MRSH': 'MMC',     # Marsh & McLennan
    'OR': 'ORA',       # Ormat Technologies (OR trades as ORA)
    'RMS': 'RMS.PA',   # Hermes International
    'TDD': 'TTD',      # The Trade Desk
}

# Clean tickers
tickers_list = []
original_names = {}
for line in raw_tickers.replace('\n', ',').split(','):
    item = item_clean = line.strip()
    if not item_clean:
        continue
    # Handle direct mappings in string
    if '=' in item_clean:
        orig, mapped = item_clean.split('=')
        orig = orig.strip()
        mapped = mapped.strip()
        tickers_list.append(mapped)
        original_names[mapped] = orig
    else:
        if item_clean in TICKER_MAP:
            mapped = TICKER_MAP[item_clean]
            tickers_list.append(mapped)
            original_names[mapped] = item_clean
        else:
            tickers_list.append(item_clean)
            original_names[item_clean] = item_clean

# Remove duplicates while preserving order
seen = set()
clean_tickers = [x for x in tickers_list if not (x in seen or seen.add(x))]

print(f"Total tickers to process: {len(clean_tickers)}")

# Qualitative Moat and Proyección mappings
QUAL_DATA = {
    'MSFT': {'moat': 9.8, 'proj': 9.8, 'sector': 'Technology'},
    'AAPL': {'moat': 9.7, 'proj': 9.5, 'sector': 'Technology'},
    'NVDA': {'moat': 9.8, 'proj': 9.9, 'sector': 'Technology'},
    'AVGO': {'moat': 9.5, 'proj': 9.7, 'sector': 'Technology'},
    'ASML': {'moat': 9.8, 'proj': 9.8, 'sector': 'Technology'},
    'TSM':  {'moat': 9.8, 'proj': 9.8, 'sector': 'Technology'},
    'GOOGL':{'moat': 9.6, 'proj': 9.6, 'sector': 'Technology'},
    'META': {'moat': 9.5, 'proj': 9.6, 'sector': 'Technology'},
    'AMZN': {'moat': 9.6, 'proj': 9.6, 'sector': 'Consumer Cyclical'},
    'V':    {'moat': 9.8, 'proj': 9.5, 'sector': 'Financial Services'},
    'MA':   {'moat': 9.8, 'proj': 9.5, 'sector': 'Financial Services'},
    'FICO': {'moat': 9.9, 'proj': 9.6, 'sector': 'Technology'},
    'MSCI': {'moat': 9.7, 'proj': 9.6, 'sector': 'Financial Services'},
    'SPGI': {'moat': 9.7, 'proj': 9.5, 'sector': 'Financial Services'},
    'MCO':  {'moat': 9.7, 'proj': 9.5, 'sector': 'Financial Services'},
    'COST': {'moat': 9.5, 'proj': 9.0, 'sector': 'Consumer Defensive'},
    'BKNG': {'moat': 9.4, 'proj': 9.0, 'sector': 'Consumer Cyclical'},
    'ISRG': {'moat': 9.6, 'proj': 9.6, 'sector': 'Healthcare'},
    'LLY':  {'moat': 9.5, 'proj': 9.7, 'sector': 'Healthcare'},
    'NVO':  {'moat': 9.5, 'proj': 9.7, 'sector': 'Healthcare'},
    'ADBE': {'moat': 9.4, 'proj': 9.3, 'sector': 'Technology'},
    'ACN':  {'moat': 9.1, 'proj': 9.2, 'sector': 'Technology'},
    'INTU': {'moat': 9.5, 'proj': 9.3, 'sector': 'Technology'},
    'NOW':  {'moat': 9.4, 'proj': 9.5, 'sector': 'Technology'},
    'CRM':  {'moat': 9.1, 'proj': 9.1, 'sector': 'Technology'},
    'ORCL': {'moat': 9.0, 'proj': 9.2, 'sector': 'Technology'},
    'ODFL': {'moat': 9.2, 'proj': 9.0, 'sector': 'Industrials'},
    'CTAS': {'moat': 9.1, 'proj': 8.8, 'sector': 'Industrials'},
    'CPRT': {'moat': 9.3, 'proj': 9.0, 'sector': 'Industrials'},
    'GWW':  {'moat': 8.8, 'proj': 8.5, 'sector': 'Industrials'},
    'WM':   {'moat': 9.0, 'proj': 8.8, 'sector': 'Industrials'},
    'WCN':  {'moat': 9.0, 'proj': 8.8, 'sector': 'Industrials'},
    'TPL':  {'moat': 9.5, 'proj': 9.5, 'sector': 'Energy'},
    'PLTR': {'moat': 9.2, 'proj': 9.7, 'sector': 'Technology'},
    'ANET': {'moat': 9.1, 'proj': 9.6, 'sector': 'Technology'},
    'VRT':  {'moat': 8.8, 'proj': 9.5, 'sector': 'Industrials'},
    'RACE': {'moat': 9.7, 'proj': 9.2, 'sector': 'Consumer Cyclical'},
    'RMS.PA':{'moat': 9.8, 'proj': 9.2, 'sector': 'Consumer Cyclical'},
    'MC.PA':{'moat': 9.6, 'proj': 9.1, 'sector': 'Consumer Cyclical'},
    'CSU.TO':{'moat': 9.6, 'proj': 9.3, 'sector': 'Technology'},
}

def get_qualitative(ticker, sector):
    # Lookup in custom mappings
    if ticker in QUAL_DATA:
        return QUAL_DATA[ticker]['moat'], QUAL_DATA[ticker]['proj']
    
    # Generic defaults by sector
    sec = (sector or '').lower()
    if 'tech' in sec or 'software' in sec:
        return 8.2, 8.5
    elif 'health' in sec or 'biotech' in sec:
        return 8.3, 8.6
    elif 'financial' in sec or 'bank' in sec or 'insurance' in sec:
        return 8.0, 8.0
    elif 'industrial' in sec or 'aerospace' in sec:
        return 8.0, 8.0
    elif 'consumer' in sec:
        return 7.8, 7.8
    else:
        return 8.0, 8.0

def score_f1_rentabilidad(info):
    # ebitdaMargins or operatingMargins
    ebitda_margin = info.get('ebitdaMargins', 0.0)
    operating_margin = info.get('operatingMargins', 0.0)
    
    margin = max(ebitda_margin or 0, operating_margin or 0)
    
    # Margin score
    if margin >= 0.35:
        margin_score = 10.0
    elif margin >= 0.15:
        margin_score = 7.0 + 3.0 * (margin - 0.15) / 0.20
    elif margin >= 0.05:
        margin_score = 5.0 + 2.0 * (margin - 0.05) / 0.10
    else:
        margin_score = max(1.0, 5.0 * margin / 0.05)
        
    # ROIC approximation
    roa = info.get('returnOnAssets', 0.0) or 0.0
    roe = info.get('returnOnEquity', 0.0) or 0.0
    
    # ROIC is generally ~1.5x to 2x ROA, or we can use ROE if ROE is not distorted (>1.0)
    if roe > 0 and roe < 1.0:
        roic_est = roe
    else:
        roic_est = roa * 1.8
        
    if roic_est >= 0.20:
        roic_score = 10.0
    elif roic_est >= 0.10:
        roic_score = 7.5 + 2.5 * (roic_est - 0.10) / 0.10
    elif roic_est >= 0.05:
        roic_score = 5.0 + 2.5 * (roic_est - 0.05) / 0.05
    else:
        roic_score = max(1.0, 5.0 * roic_est / 0.05)
        
    # FCF conversion: freeCashflow / netIncomeToCommon
    fcf = info.get('freeCashflow', 0.0) or 0.0
    net_income = info.get('netIncomeToCommon', 0.0) or 0.0
    
    if net_income > 0:
        conversion = fcf / net_income
    else:
        # If no net income, estimate based on ebitda or default
        ebitda = info.get('ebitda', 0.0) or 0.0
        conversion = fcf / (ebitda * 0.7) if ebitda > 0 else 0.8
        
    if conversion >= 1.0:
        conversion_score = 10.0
    elif conversion >= 0.5:
        conversion_score = 7.0 + 3.0 * (conversion - 0.5) / 0.5
    else:
        conversion_score = max(1.0, 7.0 * conversion / 0.5)
        
    return round((margin_score + roic_score + conversion_score) / 3.0, 2)

def score_f2_solidez(info, sector):
    total_debt = info.get('totalDebt', 0.0) or 0.0
    total_cash = info.get('totalCash', 0.0) or 0.0
    ebitda = info.get('ebitda', 0.0) or 1.0
    
    net_debt = total_debt - total_cash
    debt_ebitda = net_debt / ebitda if ebitda > 0 else 0.0
    
    # Debt Score
    if net_debt <= 0:
        debt_score = 10.0
    elif debt_ebitda <= 1.5:
        debt_score = 9.5
    elif debt_ebitda <= 4.0:
        debt_score = 9.5 - 4.5 * (debt_ebitda - 1.5) / 2.5
    else:
        debt_score = max(1.0, 5.0 - 4.0 * (debt_ebitda - 4.0) / 6.0)
        
    # Exception for negative equity with good coverage
    # (Since we might not have EBIT/Interest easily, we check if ROE is negative or very high)
    roe = info.get('returnOnEquity', 0.0) or 0.0
    if roe < 0 and debt_score < 8.0:
        # Often means massive buybacks. If company is highly profitable, we upgrade debt score
        pm = info.get('profitMargins', 0.0) or 0.0
        if pm > 0.15:
            debt_score = max(debt_score, 8.5)
            
    # Predictability Score by sector
    sec = (sector or '').lower()
    if 'tech' in sec or 'software' in sec:
        pred_score = 9.0
    elif 'health' in sec or 'biotech' in sec:
        pred_score = 8.5
    elif 'utility' in sec or 'infra' in sec:
        pred_score = 9.5
    elif 'financial' in sec:
        pred_score = 8.5
    elif 'industrial' in sec:
        pred_score = 8.0
    else:
        pred_score = 8.0
        
    return round((debt_score + pred_score) / 2.0, 2)

def score_f3_crecimiento(info, sector):
    # Growth
    rev_growth = info.get('revenueGrowth', 0.0) or info.get('earningsGrowth', 0.0) or 0.05
    
    if rev_growth >= 0.15:
        growth_score = 10.0
    elif rev_growth >= 0.06:
        growth_score = 7.0 + 3.0 * (rev_growth - 0.06) / 0.09
    else:
        growth_score = max(1.0, 5.0 + 2.0 * (rev_growth / 0.06))
        
    # M&A mastery (qualitative default)
    ma_score = 8.5
    # Special rollups
    if info.get('symbol') in ['CSU.TO', 'HEI', 'ACN']:
        ma_score = 9.8
        
    # Dilution / SBC score
    sec = (sector or '').lower()
    if 'tech' in sec or 'software' in sec:
        dilution_score = 8.0 # typical SBC dilution
    else:
        dilution_score = 9.5 # share buybacks or low dilution
        
    # If massive buyback company
    if info.get('symbol') in ['AAPL', 'FICO', 'AZO', 'ORLY', 'MUSA']:
        dilution_score = 10.0
        
    return round((growth_score + ma_score + dilution_score) / 3.0, 2)

def process_ticker(ticker):
    try:
        t = yf.Ticker(ticker)
        info = t.info
        
        if not info or 'symbol' not in info:
            return {'ticker': ticker, 'name': 'N/A', 'error': 'No info found'}
            
        name = info.get('shortName', info.get('longName', ticker))
        sector = info.get('sector', '')
        
        # 1. Rentabilidad
        f1 = score_f1_rentabilidad(info)
        
        # 2. Solidez
        f2 = score_f2_solidez(info, sector)
        
        # 3. Crecimiento
        f3 = score_f3_crecimiento(info, sector)
        
        # 4. Moat (Qualitative lookup or default)
        # 5. Proyeccion (Qualitative lookup or default)
        f4_moat, f5_proj = get_qualitative(ticker, sector)
        
        # CQV calculation
        # CQV = F1 * 0.25 + F2 * 0.15 + F3 * 0.15 + F4 * 0.25 + F5 * 0.20
        cqv = (f1 * 0.25) + (f2 * 0.15) + (f3 * 0.15) + (f4_moat * 0.25) + (f5_proj * 0.20)
        cqv = round(cqv, 2)
        
        orig_t = original_names.get(ticker, ticker)
        
        return {
            'ticker': orig_t,
            'name': name,
            'f1': f1,
            'f2': f2,
            'f3': f3,
            'f4': f4_moat,
            'f5': f5_proj,
            'cqv': cqv,
            'status': 'Success'
        }
    except Exception as e:
        return {'ticker': ticker, 'name': 'N/A', 'error': str(e), 'status': 'Error'}

def main():
    print("Starting processing...")
    results = []
    
    # Process in parallel to save time
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_ticker = {executor.submit(process_ticker, ticker): ticker for ticker in clean_tickers}
        for future in concurrent.futures.as_completed(future_to_ticker):
            ticker = future_to_ticker[future]
            try:
                res = future.result()
                results.append(res)
                print(f"Processed {ticker}: {res.get('status', 'Error')}")
            except Exception as exc:
                print(f"{ticker} generated an exception: {exc}")
                results.append({'ticker': ticker, 'name': 'N/A', 'status': 'Error', 'error': str(exc)})
                
    # Create DataFrame
    df = pd.DataFrame(results)
    
    # Split successful and errored
    df_success = df[df['status'] == 'Success'].copy()
    df_error = df[df['status'] != 'Success'].copy()
    
    if not df_success.empty:
        df_success = df_success.sort_values(by='cqv', ascending=False)
        
        # Save to CSV
        df_success.to_csv('cqv_results.csv', index=False)
        print("\nSuccessfully saved results to cqv_results.csv")
        
        # Print markdown table
        print("\n### TABLA DE RESULTADOS CQV\n")
        print("| Acción | Nombre | F1 (Rent.) | F2 (Solidez) | F3 (Crec.) | F4 (Moat) | F5 (Proj.) | CQV Score |")
        print("| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |")
        for idx, row in df_success.iterrows():
            print(f"| **{row['ticker']}** | {row['name']} | {row['f1']:.2f} | {row['f2']:.2f} | {row['f3']:.2f} | {row['f4']:.2f} | {row['f5']:.2f} | **{row['cqv']:.2f}** |")
            
    if not df_error.empty:
        print("\n### Tickers con Error o no encontrados\n")
        print("| Ticker | Error |")
        print("| :--- | :--- |")
        for idx, row in df_error.iterrows():
            print(f"| {row['ticker']} | {row.get('error', 'Desconocido')} |")

if __name__ == "__main__":
    main()
