import json
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor

matches = [
    ('QLYS', '2026-11-09', 1.96, 2.12, 8.4),
    ('HRB', '2026-11-09', -1.44, -1.4, 3.11),
    ('TTWO', '2026-11-09', -0.86, -0.29, 66.38),
    ('NOVT', '2026-11-09', 0.97, 1.05, 8.62),
    ('CEG', '2026-11-09', 3.89, 5.06, 30.08),
    ('NRG', '2026-11-09', 3.03, 4.68, 54.53),
    ('ASTS', '2026-11-09', -0.45, -0.44, 1.77),
    ('HIMS', '2026-11-09', 0.06, -0.14, -348.58),
    ('APPS', '2026-11-09', 0.17, 0.18, 5.88),
    ('DOLE', '2026-11-09', 0.34, 0.16, -53.12),
    ('KKR', '2026-11-09', 1.58, 1.78, 12.48),
    ('TDG', '2026-11-10', 12.21, 12.44, 1.89),
    ('CLFD', '2026-11-10', 0.1, None, -100.0),
    ('RGTI', '2026-11-10', -0.05, -0.06, -17.07),
    ('INMD', '2026-11-11', 0.32, 0.37, 14.91),
    ('CTVA', '2026-11-11', 0.1, 0.06, -37.31),
    ('GIB', '2026-11-11', 2.3, 2.31, 0.35),
    ('OR', '2026-11-11', 0.27, 0.29, 5.96),
    ('AMAT', '2026-11-12', 4.05, 4.16, 2.6),
    ('YETI', '2026-11-12', 0.84, 0.91, 8.1),
    ('NU', '2026-11-12', 0.22, 0.22, 0.32),
    ('TTEK', '2026-11-12', 0.47, 0.49, 4.63)
]

def fetch_data(item):
    ticker, pub_date, eps_est, eps_rep, surp = item
    print(f"Fetching data for {ticker}...")
    try:
        t = yf.Ticker(ticker)
        # 1. Price on publication date
        hist = t.history(start='2026-11-05', end='2026-11-13')
        price = None
        if not hist.empty:
            for idx in hist.index:
                if str(idx)[:10] <= pub_date:
                    price = float(hist.loc[idx, 'Close'])
            if price is None:
                price = float(hist['Close'].iloc[-1])
        else:
            price = t.info.get('regularMarketPrice') or t.info.get('currentPrice')
            
        # 2. Quarterly financials
        q_inc = t.quarterly_income_stmt
        q_cf = t.quarterly_cash_flow
        q_bs = t.quarterly_balance_sheet
        info = t.info or {}
        
        # Parse quarterly dates
        q_dates = [str(c)[:10] for c in q_inc.columns] if q_inc is not None and not q_inc.empty else []
        
        # Helper to get line item
        def get_val(df, row_name, col_idx=0):
            if df is not None and not df.empty and row_name in df.index and len(df.columns) > col_idx:
                v = df.loc[row_name].iloc[col_idx]
                if v is not None and str(v) != 'nan':
                    return float(v)
            return None

        # Current Q (col 0), Previous Q (col 1), Prior Year Q (col 4 or closest)
        rev_curr = get_val(q_inc, 'Total Revenue', 0)
        rev_prev = get_val(q_inc, 'Total Revenue', 1)
        rev_yoy = get_val(q_inc, 'Total Revenue', 4) if len(q_dates) > 4 else get_val(q_inc, 'Total Revenue', 2)
        
        opinc_curr = get_val(q_inc, 'Operating Income', 0) or get_val(q_inc, 'EBIT', 0)
        opinc_prev = get_val(q_inc, 'Operating Income', 1) or get_val(q_inc, 'EBIT', 1)
        opinc_yoy = get_val(q_inc, 'Operating Income', 4) if len(q_dates) > 4 else get_val(q_inc, 'Operating Income', 2)
        
        ni_curr = get_val(q_inc, 'Net Income', 0)
        ni_prev = get_val(q_inc, 'Net Income', 1)
        ni_yoy = get_val(q_inc, 'Net Income', 4) if len(q_dates) > 4 else get_val(q_inc, 'Net Income', 2)
        
        eps_curr = get_val(q_inc, 'Diluted EPS', 0)
        eps_prev = get_val(q_inc, 'Diluted EPS', 1)
        eps_yoy = get_val(q_inc, 'Diluted EPS', 4) if len(q_dates) > 4 else get_val(q_inc, 'Diluted EPS', 2)
        
        gp_curr = get_val(q_inc, 'Gross Profit', 0)
        cor_curr = get_val(q_inc, 'Cost Of Revenue', 0)
        shares_curr = get_val(q_inc, 'Diluted Average Shares', 0)
        
        ocf_curr = get_val(q_cf, 'Operating Cash Flow', 0)
        ocf_prev = get_val(q_cf, 'Operating Cash Flow', 1)
        ocf_yoy = get_val(q_cf, 'Operating Cash Flow', 4) if len(q_dates) > 4 else get_val(q_cf, 'Operating Cash Flow', 2)
        
        capex_curr = get_val(q_cf, 'Capital Expenditure', 0)
        capex_prev = get_val(q_cf, 'Capital Expenditure', 1)
        capex_yoy = get_val(q_cf, 'Capital Expenditure', 4) if len(q_dates) > 4 else get_val(q_cf, 'Capital Expenditure', 2)
        
        fcf_curr = get_val(q_cf, 'Free Cash Flow', 0)
        if fcf_curr is None and ocf_curr is not None and capex_curr is not None:
            fcf_curr = ocf_curr + capex_curr if capex_curr < 0 else ocf_curr - capex_curr
            
        fcf_prev = get_val(q_cf, 'Free Cash Flow', 1)
        fcf_yoy = get_val(q_cf, 'Free Cash Flow', 4) if len(q_dates) > 4 else get_val(q_cf, 'Free Cash Flow', 2)

        # Balance sheet
        cash_curr = get_val(q_bs, 'Cash And Cash Equivalents', 0)
        debt_curr = get_val(q_bs, 'Total Debt', 0) or 0
        equity_curr = get_val(q_bs, 'Stockholders Equity', 0)
        assets_curr = get_val(q_bs, 'Total Assets', 0)

        # Annual income stmt for ROA/ROE/ROIC
        a_inc = t.income_stmt
        a_bs = t.balance_sheet
        
        annual_metrics = {}
        if a_inc is not None and not a_inc.empty:
            for yr_col in a_inc.columns:
                yr_str = str(yr_col)[:4]
                try:
                    a_rev = get_val(a_inc, 'Total Revenue', list(a_inc.columns).index(yr_col))
                    a_ebit = get_val(a_inc, 'Operating Income', list(a_inc.columns).index(yr_col)) or get_val(a_inc, 'EBIT', list(a_inc.columns).index(yr_col))
                    a_ni = get_val(a_inc, 'Net Income', list(a_inc.columns).index(yr_col))
                    a_assets = get_val(a_bs, 'Total Assets', list(a_bs.columns).index(yr_col)) if a_bs is not None and yr_col in a_bs.columns else None
                    a_equity = get_val(a_bs, 'Stockholders Equity', list(a_bs.columns).index(yr_col)) if a_bs is not None and yr_col in a_bs.columns else None
                    a_debt = get_val(a_bs, 'Total Debt', list(a_bs.columns).index(yr_col)) if a_bs is not None and yr_col in a_bs.columns else 0
                    
                    a_roa = (a_ni / a_assets * 100) if a_assets and a_ni else None
                    a_roe = (a_ni / a_equity * 100) if a_equity and a_ni else None
                    inv_cap = (a_equity + a_debt) if a_equity else None
                    a_roic = (a_ebit * 0.80 / inv_cap * 100) if inv_cap and a_ebit else None
                    
                    annual_metrics[yr_str] = {
                        'revenue_m': round(a_rev / 1e6, 1) if a_rev else None,
                        'operating_income_m': round(a_ebit / 1e6, 1) if a_ebit else None,
                        'net_income_m': round(a_ni / 1e6, 1) if a_ni else None,
                        'roa_pct': round(a_roa, 1) if a_roa else None,
                        'roe_pct': round(a_roe, 1) if a_roe else None,
                        'roic_pct': round(a_roic, 1) if a_roic else None,
                    }
                except:
                    pass

        # TTM metrics
        ttm_rev = sum([get_val(q_inc, 'Total Revenue', i) or 0 for i in range(min(4, len(q_dates)))])
        ttm_opinc = sum([get_val(q_inc, 'Operating Income', i) or get_val(q_inc, 'EBIT', i) or 0 for i in range(min(4, len(q_dates)))])
        ttm_ni = sum([get_val(q_inc, 'Net Income', i) or 0 for i in range(min(4, len(q_dates)))])
        ttm_ocf = sum([get_val(q_cf, 'Operating Cash Flow', i) or 0 for i in range(min(4, len(q_dates)))])
        ttm_capex = abs(sum([get_val(q_cf, 'Capital Expenditure', i) or 0 for i in range(min(4, len(q_dates)))]))

        return {
            'ticker': ticker,
            'publication_date': pub_date,
            'price': round(price, 2) if price else None,
            'eps_estimate': eps_est,
            'eps_reported': eps_rep,
            'surprise_pct': surp,
            'quarterly_dates': q_dates[:5],
            'revenue_curr_m': round(rev_curr / 1e6, 1) if rev_curr else None,
            'revenue_prev_m': round(rev_prev / 1e6, 1) if rev_prev else None,
            'revenue_yoy_m': round(rev_yoy / 1e6, 1) if rev_yoy else None,
            'operating_income_curr_m': round(opinc_curr / 1e6, 1) if opinc_curr else None,
            'operating_income_prev_m': round(opinc_prev / 1e6, 1) if opinc_prev else None,
            'operating_income_yoy_m': round(opinc_yoy / 1e6, 1) if opinc_yoy else None,
            'net_income_curr_m': round(ni_curr / 1e6, 1) if ni_curr else None,
            'net_income_prev_m': round(ni_prev / 1e6, 1) if ni_prev else None,
            'net_income_yoy_m': round(ni_yoy / 1e6, 1) if ni_yoy else None,
            'diluted_eps_curr': round(eps_curr, 2) if eps_curr else None,
            'diluted_eps_prev': round(eps_prev, 2) if eps_prev else None,
            'diluted_eps_yoy': round(eps_yoy, 2) if eps_yoy else None,
            'gross_profit_curr_m': round(gp_curr / 1e6, 1) if gp_curr else None,
            'cost_of_revenue_curr_m': round(cor_curr / 1e6, 1) if cor_curr else None,
            'diluted_shares_m': round(shares_curr / 1e6, 1) if shares_curr else None,
            'ocf_curr_m': round(ocf_curr / 1e6, 1) if ocf_curr else None,
            'ocf_prev_m': round(ocf_prev / 1e6, 1) if ocf_prev else None,
            'ocf_yoy_m': round(ocf_yoy / 1e6, 1) if ocf_yoy else None,
            'capex_curr_m': round(abs(capex_curr) / 1e6, 1) if capex_curr else None,
            'capex_prev_m': round(abs(capex_prev) / 1e6, 1) if capex_prev else None,
            'capex_yoy_m': round(abs(capex_yoy) / 1e6, 1) if capex_yoy else None,
            'fcf_curr_m': round(fcf_curr / 1e6, 1) if fcf_curr else None,
            'fcf_prev_m': round(fcf_prev / 1e6, 1) if fcf_prev else None,
            'fcf_yoy_m': round(fcf_yoy / 1e6, 1) if fcf_yoy else None,
            'cash_curr_m': round(cash_curr / 1e6, 1) if cash_curr else None,
            'debt_curr_m': round(debt_curr / 1e6, 1) if debt_curr else None,
            'equity_curr_m': round(equity_curr / 1e6, 1) if equity_curr else None,
            'assets_curr_m': round(assets_curr / 1e6, 1) if assets_curr else None,
            'ttm_revenue_m': round(ttm_rev / 1e6, 1) if ttm_rev else None,
            'ttm_operating_income_m': round(ttm_opinc / 1e6, 1) if ttm_opinc else None,
            'ttm_net_income_m': round(ttm_ni / 1e6, 1) if ttm_ni else None,
            'ttm_ocf_m': round(ttm_ocf / 1e6, 1) if ttm_ocf else None,
            'ttm_capex_m': round(ttm_capex / 1e6, 1) if ttm_capex else None,
            'forward_pe': info.get('forwardPE'),
            'trailing_pe': info.get('trailingPE'),
            'target_mean_price': info.get('targetMeanPrice'),
            'target_high_price': info.get('targetHighPrice'),
            'target_low_price': info.get('targetLowPrice'),
            'num_analysts': info.get('numberOfAnalystOpinions'),
            'consensus_recommendation': info.get('recommendationKey'),
            'annual_metrics': annual_metrics
        }
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        return {'ticker': ticker, 'error': str(e)}

print(f"Starting fetch for {len(matches)} companies...")
financials = {}
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_data, matches))
    for r in results:
        financials[r['ticker']] = r

with open('scratch/financials_22.json', 'w', encoding='utf-8') as f:
    json.dump(financials, f, indent=2, ensure_ascii=False)

print("Saved scratch/financials_22.json successfully!")

