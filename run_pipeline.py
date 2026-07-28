import os
import json
import time
from datetime import datetime
import pandas as pd
import numpy as np
import yfinance as yf
import concurrent.futures

# 1. Config paths
CONFIG_PATH = "cqv_qualitative_config.json"
CACHE_DIR = "cache"

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# Load configuration
try:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config_data = json.load(f)
    qualitative_f4_f5 = config_data.get("qualitative_f4_f5", {})
    custom_f6_f7_f8 = config_data.get("custom_metrics_f6_f7_f8", {})
    print("Loaded qualitative configuration and custom metrics.")
except Exception as e:
    print(f"Error loading {CONFIG_PATH}: {e}")
    qualitative_f4_f5 = {}
    custom_f6_f7_f8 = {}

# 2. Tickers & Mappings
raw_tickers = """
ABB,AAPL, ACN,ADBE,ADI,AJG,AMAT,AMD,AMZN,ANET,APH,APO,APP,ASML,AVGO,AXON,AXP,AZO,
BABA,BAH,BJ,BKNG,BLDR,BMI,BRK=BRK-B,BRO,BXSX
CAT,CDNS,CEG,CHDN,COR,COST,CPRT,CRM,CRVL,CRWD,CSL,CSU=CSU.TO,CTAS,
DECK,DRS,DSGX,
EL,EME,EPAM,ETN,EXLS,
FAST,FICO,FIX,FLEX,FN,FDRL,FND,FSS,FTNT,
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
WCN,WM,WMT,WTS,WWD,
8001=8001.T,8002=8002.T,8031=8031.T,8058=8058.T,ACGL,APG,BF.B=BF-B,BR,CB,CME,
EVO=EVO.ST,FDS,FSLR,GWRE,ICE,KKR,KRI=KRI.AT,LOTB=LOTB.BR,MORN,ROL,
SJ=SJ.TO,SNPS,SPCX,SSD,STE,SYK,VEEV,VRSN,ZTS,
ASM=ASM.AS,CBOE,LOR=OR.PA,AFRM,ALFEN=ALFEN.AS,ADP,CELH,CDW,CRSP,CASY,
API,ALAB,COIN,CMCSA,ASTS,ALGM,CNXC,WOSG=WOSG.L,CHTR,BCPC,ACLS,CSGP,
APPS,DASH,AMGN,CLFD,CIGI,ARM,ADSK,DIOD,EXPO,DDOG,EBAY,ENTG,DOCU,
ENPH,FROG,HON,DUOL,IBKR,GTLB,DXCM,FRPT,FIVN,ICLR,INTA,FORM,FRSH,
FTDR,HOOD,FIVE,INMD,JD,IPAR,INTC,IREN,JKHY,KINS,LITE,MKTX,MNST,
LOGI,MDB,LULU,NTES,MAMA,LSCC,NOVT,NNE,OKTA,NSSC,MRNA,PAYX,ON,OPEN,
PODD,MMSI,MAR,MRVL,MSTR,PCTY,QCOM,NXPI,NICE,PEP,PDD,QLYS,RGTI,
ROST,ROP,SMCI,SBUX,SPSC,SBAC,SEZL,SSNC,TECH,TEAM,TRMB,TLN,TDUP,
TEM,SOUN,RPD,TTWO,TXRH,TROW,SAIA,SOFI,STLD,SEDG,TXN,SNDK,ULTA,
TER,STX,VRTX,UPST,XPEL,ZG,WDC,WDAY,ZBRA,WING,ABBV,ATR,USLM,AME,
AI,AGM,ABT,ACA,ZS,ANF,AON,BE,ATKR,BAM,CACI,BLK,BN,CAVA,BRBR,
BILL,BX,CHPT,CI,CP,CMG,CLH,CPNG,CNI,DG,COHR,CVNA,DAVA,DHR,CNS,
DE,DIS,CMC,CTVA,CRCL,DHI,DT,DELL,DOV,ELF,DBD,DOLE,EGP,ELV,EFX,
EVR,DOCN,EW,GDDY,GIB,EXR,GLOB,GNRC,GPN,KEYS,IHG,HTB,HRB,JCI,
HCI,JNJ,HUBS,HSY,ITW,KR,GGG,KO,LW,LEN,KMX,IIPR,HIMS,LPX,IONQ,
IEX,INSP,LYB,MAA,MLM,MAS,MTH,MKC,MCD,MP,MTN,MATX,MTD,NRG,MKL,
NIO,NUE,NEE,NSP,NET,NYT,NU,OKLO,NKE,OSCR,PFGC,PATH,NOC,OTIS,
MRK,PAC,OWL,PAYC,PHM,PJT,PKG,RELX,RMD,SCHW,RDDT,SCI,TMO,SMWB,
ROK,SONY,TRU,TDY,TOST,RH,TTC,TDOC,STZ,TWLO,TFII,TGT,TREX,TYL,
U,UI,UDR,UNP,VAL,YETI,VICI,WSO,WSM,W,VMC,YUM,NESN=NESN.SW,WAT,
TEQ=TEQ.ST,WGO,GSY=GSY.TO,VLO,NA9=NA9.DE,CNR=CNR.TO,CNQ=CNQ.TO,
WST,HFG=HFG.DE,TCEHY=0700.HK
"""

TICKER_MAP = {
    'BXSX': 'BSX',     # Boston Scientific
    'FDRL': 'FND',     # Floor & Decor (probable typo)
    'BRK': 'BRK-B',    # Berkshire Hathaway
    'CSU': 'CSU.TO',   # Constellation Software
    'LVMH': 'MC.PA',   # LVMH Moet Hennessy
    'MRSH': 'MMC',     # Marsh & McLennan
    'OR': 'ORA',       # Ormat Technologies
    'RMS': 'RMS.PA',   # Hermes International
    'TDD': 'TTD',      # The Trade Desk
    '8001': '8001.T',
    '8002': '8002.T',
    '8031': '8031.T',
    '8058': '8058.T',
    'BF.B': 'BF-B',
    'EVO': 'EVO.ST',
    'KRI': 'KRI.AT',
    'LOTB': 'LOTB.BR',
    'SJ': 'SJ.TO',
    'ASM': 'ASM.AS',
    'LOR': 'OR.PA',
    'ALFEN': 'ALFEN.AS',
    'WOSG': 'WOSG.L',
    'NESN': 'NESN.SW',
    'TEQ': 'TEQ.ST',
    'GSY': 'GSY.TO',
    'NA9': 'NA9.DE',
    'CNR': 'CNR.TO',
    'CNQ': 'CNQ.TO',
    'HFG': 'HFG.DE',
    'TCEHY': '0700.HK',
}

# Clean tickers
tickers_list = []
original_names = {}
for line in raw_tickers.replace('\n', ',').split(','):
    item = line.strip()
    if not item:
        continue
    if '=' in item:
        orig, mapped = item.split('=')
        orig = orig.strip()
        mapped = mapped.strip()
        tickers_list.append(mapped)
        original_names[mapped] = orig
    else:
        if item in TICKER_MAP:
            mapped = TICKER_MAP[item]
            tickers_list.append(mapped)
            original_names[mapped] = item
        else:
            tickers_list.append(item)
            original_names[item] = item

seen = set()
clean_tickers = [x for x in tickers_list if not (x in seen or seen.add(x))]
print(f"Total tickers to process: {len(clean_tickers)}")

# 3. Data Fetching & Caching
def fetch_ticker_data(ticker):
    cache_path = os.path.join(CACHE_DIR, f"{ticker}.json")
    if os.path.exists(cache_path):
        mtime = os.path.getmtime(cache_path)
        mdate = datetime.fromtimestamp(mtime)
        now = datetime.now()
        # Same month & year -> reuse cache
        if mdate.year == now.year and mdate.month == now.month:
            try:
                with open(cache_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error reading cache for {ticker}, refetching: {e}")

    print(f"Downloading {ticker} from yfinance...")
    try:
        t = yf.Ticker(ticker)
        info = t.info or {}
        
        def clean_df(df):
            if df is None or df.empty:
                return {}
            raw_dict = df.to_dict()
            json_dict = {}
            for col_ts, row in raw_dict.items():
                col_str = str(col_ts)[:10]  # 'YYYY-MM-DD'
                clean_row = {}
                for k, v in row.items():
                    if pd.isna(v) or np.isinf(v):
                        clean_row[str(k)] = None
                    else:
                        clean_row[str(k)] = float(v) if isinstance(v, (int, float, np.integer, np.floating)) else str(v)
                json_dict[col_str] = clean_row
            return json_dict

        financials = clean_df(t.financials)
        balance_sheet = clean_df(t.balance_sheet)
        cashflow = clean_df(t.cashflow)

        close_history = {}
        try:
            hist_df = t.history(period="5y")
            if not hist_df.empty:
                ye_hist = hist_df['Close'].resample('YE').last()
                for dt, val in ye_hist.items():
                    close_history[str(dt)[:4]] = round(float(val), 2)
        except Exception as he:
            print(f"Error fetching history for {ticker}: {he}")

        data = {
            "ticker": ticker,
            "info": info,
            "financials": financials,
            "balance_sheet": balance_sheet,
            "cashflow": cashflow,
            "close_history": close_history,
            "last_updated": datetime.now().isoformat()
        }

        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        return data
    except Exception as e:
        print(f"Error downloading {ticker}: {e}")
        return None

# Helpers for querying statements
def get_statement_val(statement_dict, keys, date_str=None):
    if not statement_dict:
        return None
    sorted_dates = sorted(list(statement_dict.keys()), reverse=True)
    if not sorted_dates:
        return None
    dates_to_check = [date_str] if date_str in statement_dict else sorted_dates
    for d in dates_to_check:
        row_data = statement_dict[d]
        for k in keys:
            if k in row_data:
                val = row_data[k]
                if val is not None:
                    return val
    return None

def extract_metrics(data, date_str=None):
    fin = data.get("financials", {})
    bs = data.get("balance_sheet", {})
    cf = data.get("cashflow", {})
    info = data.get("info", {})
    
    metrics = {}
    metrics["rev"] = get_statement_val(fin, ['Total Revenue', 'Revenue'], date_str) or info.get("totalRevenue")
    metrics["ebitda"] = get_statement_val(fin, ['EBITDA'], date_str) or info.get("ebitda")
    metrics["ebit"] = get_statement_val(fin, ['Operating Income', 'EBIT'], date_str) or info.get("operatingIncome")
    metrics["net_income"] = get_statement_val(fin, ['Net Income', 'Net Income Common Stockholders', 'Net Income To Common'], date_str) or info.get("netIncomeToCommon")
    metrics["tax_provision"] = get_statement_val(fin, ['Tax Provision'], date_str)
    metrics["pretax_income"] = get_statement_val(fin, ['Pretax Income', 'Income Before Tax'], date_str)
    metrics["cash"] = get_statement_val(bs, ['Cash And Cash Equivalents', 'Cash Cash Equivalents And Short Term Investments', 'Cash'], date_str) or info.get("totalCash")
    
    debt = get_statement_val(bs, ['Total Debt'], date_str)
    if debt is None:
        st_debt = get_statement_val(bs, ['Current Debt', 'Short Long Term Debt'], date_str) or 0.0
        lt_debt = get_statement_val(bs, ['Long Term Debt'], date_str) or 0.0
        debt = st_debt + lt_debt
    metrics["debt"] = debt or info.get("totalDebt") or 0.0
    
    metrics["equity"] = get_statement_val(bs, ['Stockholders Equity', 'Total Equity Gross Minor Interest'], date_str)
    metrics["ocf"] = get_statement_val(cf, ['Operating Cash Flow', 'Cash Flow From Operating Activities'], date_str) or info.get("operatingCashflow")
    metrics["capex"] = get_statement_val(cf, ['Capital Expenditure'], date_str) or info.get("capitalExpenditure")
    
    metrics["fcf"] = info.get("freeCashflow")
    if metrics["fcf"] is None and metrics["ocf"] is not None:
        metrics["fcf"] = metrics["ocf"] + (metrics["capex"] or 0.0)
        
    metrics["eps"] = get_statement_val(fin, ['Diluted EPS', 'Basic EPS'], date_str)
    if metrics["eps"] is None and date_str is None:
        metrics["eps"] = info.get("trailingEps")
        
    return metrics

def compute_real_roic(metrics, info):
    ebit = metrics["ebit"]
    if ebit is None or ebit <= 0:
        ebit = (metrics["ebitda"] or 0.0) * 0.8
    if ebit <= 0:
        ebit = max(0.0, metrics["net_income"] or 0.0)
        
    tax_provision = metrics["tax_provision"] or 0.0
    pretax_income = metrics["pretax_income"] or 0.0
    
    tax_rate = 0.21
    if pretax_income > 0 and tax_provision > 0:
        rate = tax_provision / pretax_income
        if 0 <= rate <= 0.45:
            tax_rate = rate
            
    nopat = ebit * (1 - tax_rate)
    
    debt = metrics["debt"] or 0.0
    equity = metrics["equity"] or 0.0
    cash = metrics["cash"] or 0.0
    
    if equity <= 0:
        equity = 0.0
        
    invested_capital = debt + equity - cash
    if invested_capital <= 0:
        invested_capital = max(1.0, debt + equity)
        
    roic = nopat / invested_capital if invested_capital > 0 else 0.0
    
    roa = info.get('returnOnAssets', 0.0) or 0.0
    roe = info.get('returnOnEquity', 0.0) or 0.0
    if roic <= 0 or roic > 2.0:
        if roe > 0 and roe < 1.0:
            roic = roe
        elif roa > 0:
            roic = roa * 1.5
            
    return roic

# 4. Calculation functions
def get_qualitative_f4_f5(ticker, sector):
    if ticker in qualitative_f4_f5:
        return qualitative_f4_f5[ticker]["moat"], qualitative_f4_f5[ticker]["proj"]
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

# Legacy Calculations (to keep v1.0 and v2.0 exact)
def score_f1_rentabilidad_legacy(info):
    ebitda_margin = info.get('ebitdaMargins', 0.0)
    operating_margin = info.get('operatingMargins', 0.0)
    margin = max(ebitda_margin or 0, operating_margin or 0)
    if margin >= 0.35:
        margin_score = 10.0
    elif margin >= 0.15:
        margin_score = 7.0 + 3.0 * (margin - 0.15) / 0.20
    elif margin >= 0.05:
        margin_score = 5.0 + 2.0 * (margin - 0.05) / 0.10
    else:
        margin_score = max(1.0, 5.0 * margin / 0.05)
    roa = info.get('returnOnAssets', 0.0) or 0.0
    roe = info.get('returnOnEquity', 0.0) or 0.0
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
    fcf = info.get('freeCashflow', 0.0) or 0.0
    net_income = info.get('netIncomeToCommon', 0.0) or 0.0
    if net_income > 0:
        conversion = fcf / net_income
    else:
        ebitda = info.get('ebitda', 0.0) or 0.0
        conversion = fcf / (ebitda * 0.7) if ebitda > 0 else 0.8
    if conversion >= 1.0:
        conversion_score = 10.0
    elif conversion >= 0.5:
        conversion_score = 7.0 + 3.0 * (conversion - 0.5) / 0.5
    else:
        conversion_score = max(1.0, 7.0 * conversion / 0.5)
    return round((margin_score + roic_score + conversion_score) / 3.0, 2)

def score_f2_solidez_legacy(info, sector):
    total_debt = info.get('totalDebt', 0.0) or 0.0
    total_cash = info.get('totalCash', 0.0) or 0.0
    ebitda = info.get('ebitda', 0.0) or 1.0
    net_debt = total_debt - total_cash
    debt_ebitda = net_debt / ebitda if ebitda > 0 else 0.0
    if net_debt <= 0:
        debt_score = 10.0
    elif debt_ebitda <= 1.5:
        debt_score = 9.5
    elif debt_ebitda <= 4.0:
        debt_score = 9.5 - 4.5 * (debt_ebitda - 1.5) / 2.5
    else:
        debt_score = max(1.0, 5.0 - 4.0 * (debt_ebitda - 4.0) / 6.0)
    roe = info.get('returnOnEquity', 0.0) or 0.0
    if roe < 0 and debt_score < 8.0:
        pm = info.get('profitMargins', 0.0) or 0.0
        if pm > 0.15:
            debt_score = max(debt_score, 8.5)
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

def score_f3_crecimiento_legacy(info, sector):
    rev_growth = info.get('revenueGrowth', 0.0) or info.get('earningsGrowth', 0.0) or 0.05
    if rev_growth >= 0.15:
        growth_score = 10.0
    elif rev_growth >= 0.06:
        growth_score = 7.0 + 3.0 * (rev_growth - 0.06) / 0.09
    else:
        growth_score = max(1.0, 5.0 + 2.0 * (rev_growth / 0.06))
    ma_score = 8.5
    if info.get('symbol') in ['CSU.TO', 'HEI', 'ACN']:
        ma_score = 9.8
    sec = (sector or '').lower()
    if 'tech' in sec or 'software' in sec:
        dilution_score = 8.0
    else:
        dilution_score = 9.5
    if info.get('symbol') in ['AAPL', 'FICO', 'AZO', 'ORLY', 'MUSA']:
        dilution_score = 10.0
    return round((growth_score + ma_score + dilution_score) / 3.0, 2)

# V3 Calculations (Real ROIC and Real FCF Yield)
def score_f1_rentabilidad_v3(metrics, info):
    rev = metrics["rev"] or 1.0
    ebitda = metrics["ebitda"] or 0.0
    ebit = metrics["ebit"] or 0.0
    margin = max(ebitda / rev, ebit / rev)
    
    if margin >= 0.35:
        margin_score = 10.0
    elif margin >= 0.15:
        margin_score = 7.0 + 3.0 * (margin - 0.15) / 0.20
    elif margin >= 0.05:
        margin_score = 5.0 + 2.0 * (margin - 0.05) / 0.10
    else:
        margin_score = max(1.0, 5.0 * margin / 0.05)
        
    roic = compute_real_roic(metrics, info)
    if roic >= 0.20:
        roic_score = 10.0
    elif roic >= 0.10:
        roic_score = 7.5 + 2.5 * (roic - 0.10) / 0.10
    elif roic >= 0.05:
        roic_score = 5.0 + 2.5 * (roic - 0.05) / 0.05
    else:
        roic_score = max(1.0, 5.0 * roic / 0.05)
        
    fcf = metrics["fcf"] or 0.0
    net_income = metrics["net_income"] or 0.0
    if net_income > 0:
        conversion = fcf / net_income
    else:
        conversion = fcf / ((ebitda or 1.0) * 0.7)
        
    if conversion >= 1.0:
        conversion_score = 10.0
    elif conversion >= 0.5:
        conversion_score = 7.0 + 3.0 * (conversion - 0.5) / 0.5
    else:
        conversion_score = max(1.0, 7.0 * conversion / 0.5)
        
    return round((margin_score + roic_score + conversion_score) / 3.0, 2)

def score_f2_solidez_v3(metrics, info, sector):
    total_debt = metrics["debt"] or 0.0
    total_cash = metrics["cash"] or 0.0
    ebitda = metrics["ebitda"] or 1.0
    net_debt = total_debt - total_cash
    debt_ebitda = net_debt / ebitda if ebitda > 0 else 0.0
    
    if net_debt <= 0:
        debt_score = 10.0
    elif debt_ebitda <= 1.5:
        debt_score = 9.5
    elif debt_ebitda <= 4.0:
        debt_score = 9.5 - 4.5 * (debt_ebitda - 1.5) / 2.5
    else:
        debt_score = max(1.0, 5.0 - 4.0 * (debt_ebitda - 4.0) / 6.0)
        
    equity = metrics["equity"] or 0.0
    if equity <= 0 and debt_score < 8.5:
        margin_net = (metrics["net_income"] or 0.0) / (metrics["rev"] or 1.0)
        if margin_net > 0.15:
            debt_score = max(debt_score, 8.5)
            
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

def score_f3_crecimiento_v3(metrics, info, sector, ticker):
    rev_growth = info.get('revenueGrowth', 0.0) or info.get('earningsGrowth', 0.0) or 0.05
    if rev_growth >= 0.15:
        growth_score = 10.0
    elif rev_growth >= 0.06:
        growth_score = 7.0 + 3.0 * (rev_growth - 0.06) / 0.09
    else:
        growth_score = max(1.0, 5.0 + 2.0 * (rev_growth / 0.06))
        
    ma_score = 8.5
    if ticker in ['CSU.TO', 'HEI', 'ACN']:
        ma_score = 9.8
        
    sec = (sector or '').lower()
    if 'tech' in sec or 'software' in sec:
        dilution_score = 8.0
    else:
        dilution_score = 9.5
    if ticker in ['AAPL', 'FICO', 'AZO', 'ORLY', 'MUSA']:
        dilution_score = 10.0
        
    return round((growth_score + ma_score + dilution_score) / 3.0, 2)

def score_f7_fcf_yield_v3(metrics, info, f1_score, ticker):
    if ticker in custom_f6_f7_f8 and 'f7' in custom_f6_f7_f8[ticker]:
        return custom_f6_f7_f8[ticker]['f7']
        
    fcf = metrics["fcf"]
    mcap = info.get("marketCap")
    if fcf is not None and mcap is not None and mcap > 0:
        yield_val = fcf / mcap
        if yield_val >= 0.06:
            score = 10.0
        elif yield_val >= 0.02:
            score = 5.0 + 5.0 * (yield_val - 0.02) / 0.04
        elif yield_val >= 0.0:
            score = 1.0 + 4.0 * (yield_val) / 0.02
        else:
            score = 1.0
        return round(score, 2)
        
    val = (10.0 - (f1_score - 5.0)) * 0.8
    return round(max(1.0, min(10.0, val)), 2)

def calculate_peg_score(info, ticker):
    # Try retrieving standard PEG ratios
    peg = info.get('pegRatio') or info.get('trailingPEGRatio')
    
    # Fallback to computing it from P/E and growth (revenue or earnings)
    if peg is None:
        pe = info.get('trailingPE') or info.get('forwardPE')
        growth = info.get('revenueGrowth') or info.get('earningsGrowth')
        if pe is not None and growth is not None and growth > 0.001:
            peg = pe / (growth * 100.0)
            
    # Default to neutral 5.00 if data is not available
    if peg is None or peg <= 0:
        return 5.00
        
    # Scale PEG to a 0-10 score (10 is best: undervalued or high growth)
    if peg <= 1.0:
        score = 10.0 - 1.0 * peg
    elif peg <= 2.0:
        score = 9.0 - 2.0 * (peg - 1.0)
    elif peg <= 3.0:
        score = 7.0 - 3.0 * (peg - 2.0)
    else:
        score = max(1.0, 4.0 - (peg - 3.0) / 2.0)
        
    return round(score, 2)

def compute_momentum_score(info):
    if not info:
        return 5.0
    current = info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose")
    high52 = info.get("fiftyTwoWeekHigh")
    low52 = info.get("fiftyTwoWeekLow")
    sma50 = info.get("fiftyDayAverage")
    sma200 = info.get("twoHundredDayAverage")
    
    if not current or not high52 or not low52 or not sma50 or not sma200:
        return 5.0 # default/neutral
        
    # 1. 52-week position (0 to 1) -> weight: 30%
    diff = high52 - low52
    pos_52w = (current - low52) / diff if diff > 0 else 0.5
    pos_52w = max(0.0, min(1.0, pos_52w))
    
    # 2. 50-day SMA position -> weight: 25%
    # If price is 15% above 50-day SMA, score is 10. If 15% below, score is 0.
    ratio_50 = (current - sma50) / sma50 if sma50 > 0 else 0.0
    score_50 = 5.0 + (ratio_50 * 33.3)
    score_50 = max(0.0, min(10.0, score_50))
    
    # 3. 200-day SMA position -> weight: 25%
    # If price is 30% above 200-day SMA, score is 10. If 30% below, score is 0.
    ratio_200 = (current - sma200) / sma200 if sma200 > 0 else 0.0
    score_200 = 5.0 + (ratio_200 * 16.6)
    score_200 = max(0.0, min(10.0, score_200))
    
    # 4. SMA Cross alignment -> weight: 20%
    # If 50-day SMA is above 200-day SMA, score is 10, else 2.0. (with scaling if close)
    ratio_sma = (sma50 - sma200) / sma200 if sma200 > 0 else 0.0
    score_sma = 5.0 + (ratio_sma * 50.0)
    score_sma = max(0.0, min(10.0, score_sma))
    
    final_score = (pos_52w * 10 * 0.30) + (score_50 * 0.25) + (score_200 * 0.25) + (score_sma * 0.20)
    return round(final_score, 2)

def get_quarter_for_company(ticker, data):
    inform_dir = 'inform'
    if os.path.exists(inform_dir):
        matching_q = []
        for fn in os.listdir(inform_dir):
            if fn.lower().startswith(ticker.lower() + '_') and fn.endswith('.md'):
                parts = fn.replace('.md', '').split('_')
                if len(parts) >= 3:
                    yr = parts[1]
                    q_str = parts[2].upper()
                    matching_q.append((yr, q_str))
        if matching_q:
            matching_q.sort(key=lambda x: (x[0], x[1]), reverse=True)
            latest = matching_q[0]
            return f"{latest[1]} {latest[0]}"
    
    if data and 'info' in data and data['info']:
        mrq = data['info'].get('mostRecentQuarter')
        if mrq:
            dt = datetime.fromtimestamp(mrq)
            m = dt.month
            yr = dt.year
            if m in [1, 2, 3]: return f"Q1 {yr}"
            elif m in [4, 5, 6]: return f"Q2 {yr}"
            elif m in [7, 8, 9]: return f"Q3 {yr}"
            else: return f"Q4 {yr}"
            
        fin = data.get('financials', {})
        if fin:
            latest_date = sorted(list(fin.keys()))[-1]
            dt = datetime.strptime(latest_date[:10], '%Y-%m-%d')
            m = dt.month
            yr = dt.year
            if m in [1, 2, 3]: return f"Q1 {yr}"
            elif m in [4, 5, 6]: return f"Q2 {yr}"
            elif m in [7, 8, 9]: return f"Q3 {yr}"
            else: return f"Q4 {yr}"

    return "Q1 2026"

# 5. Pipeline execution
def process_ticker(ticker):
    data = fetch_ticker_data(ticker)
    if not data or 'info' not in data or not data['info']:
        return {'ticker': ticker, 'name': 'N/A', 'status': 'Error', 'error': 'Failed to fetch'}
        
    info = data['info']
    name = info.get('shortName', info.get('longName', ticker))
    sector = info.get('sector', '')
    quarter_str = get_quarter_for_company(ticker, data)
    
    # Extract metrics for current period
    metrics = extract_metrics(data)
    
    # Legacy calculations
    f1_legacy = score_f1_rentabilidad_legacy(info)
    f2_legacy = score_f2_solidez_legacy(info, sector)
    f3_legacy = score_f3_crecimiento_legacy(info, sector)
    
    # Qualitative F4 & F5
    f4_moat, f5_proj = get_qualitative_f4_f5(ticker, sector)
    
    # Custom or Default F6, F7, F8
    if ticker in custom_f6_f7_f8:
        f6 = custom_f6_f7_f8[ticker].get('f6', round((f1_legacy + f3_legacy)/2.0, 2))
        f7_legacy = custom_f6_f7_f8[ticker].get('f7', round(max(1.0, min(10.0, (10.0 - (f1_legacy - 5.0))*0.8)), 2))
        f8 = custom_f6_f7_f8[ticker].get('f8', 8.0)
    else:
        f6 = round((f1_legacy + f3_legacy)/2.0, 2)
        f7_legacy = round(max(1.0, min(10.0, (10.0 - (f1_legacy - 5.0))*0.8)), 2)
        f8 = 8.0
        
    # V3 calculations
    f1_v3 = score_f1_rentabilidad_v3(metrics, info)
    f2_v3 = score_f2_solidez_v3(metrics, info, sector)
    f3_v3 = score_f3_crecimiento_v3(metrics, info, sector, ticker)
    f7_v3 = score_f7_fcf_yield_v3(metrics, info, f1_v3, ticker)
    
    # Valuation PEG Score
    peg_score = calculate_peg_score(info, ticker)
    
    # Momentum Score
    momentum_score = compute_momentum_score(info)
    
    # CQV v1.0
    cqv_v1 = (f1_legacy * 0.25) + (f2_legacy * 0.15) + (f3_legacy * 0.15) + (f4_moat * 0.25) + (f5_proj * 0.20)
    cqv_v1 = round(cqv_v1, 2)
    
    # CQV v1.1 (5F with real ROIC & DEGRADATION filter)
    cqv_v1_1 = (f1_v3 * 0.25) + (f2_v3 * 0.15) + (f3_v3 * 0.15) + (f4_moat * 0.25) + (f5_proj * 0.20)
    if f4_moat < 6.0 or f2_v3 < 5.0:
        cqv_v1_1 = min(cqv_v1_1, 7.00)
    cqv_v1_1 = round(cqv_v1_1, 2)
    
    # CQV v2.0
    cqv_v2 = (f1_legacy * 0.20) + (f2_legacy * 0.10) + (f3_legacy * 0.10) + (f4_moat * 0.20) + (f5_proj * 0.10) + (f6 * 0.10) + (f7_legacy * 0.10) + (f8 * 0.10)
    cqv_v2 = round(cqv_v2, 2)
    
    # CQV v3.0 (with real ROIC, FCF Yield and DEGRADATION filter)
        # Apply custom report factor overrides if present
    ticker_cfg = config_data.get(ticker, {})
    if not ticker_cfg and ticker in custom_f6_f7_f8:
        ticker_cfg = custom_f6_f7_f8[ticker]
    if ticker_cfg:
        if 'f1' in ticker_cfg: f1_v3 = ticker_cfg['f1']
        if 'f2' in ticker_cfg: f2_v3 = ticker_cfg['f2']
        if 'f3' in ticker_cfg: f3_v3 = ticker_cfg['f3']
        if 'f4' in ticker_cfg: f4_moat = ticker_cfg['f4']
        if 'f5' in ticker_cfg: f5_proj = ticker_cfg['f5']
        if 'f6' in ticker_cfg: f6 = ticker_cfg['f6']
        if 'f7' in ticker_cfg: f7_v3 = ticker_cfg['f7']
        if 'f8' in ticker_cfg: f8 = ticker_cfg['f8']

    cqv_v3 = (f1_v3 * 0.20) + (f2_v3 * 0.10) + (f3_v3 * 0.10) + (f4_moat * 0.20) + (f5_proj * 0.10) + (f6 * 0.10) + (f7_v3 * 0.10) + (f8 * 0.10)
    
    # DEGRADATION FILTER: Cap at 7.00 if F4 < 6.0 or F2_v3 < 5.0
    if f4_moat < 6.0 or f2_v3 < 5.0:
        cqv_v3 = min(cqv_v3, 7.00)
    cqv_v3 = round(cqv_v3, 2)
    
    pe = info.get('trailingPE') or info.get('forwardPE')
    pe = round(pe, 2) if pe else None
    
    orig_t = original_names.get(ticker, ticker)
    
    return {
        'ticker': orig_t,
        'name': name,
        'sector': sector,
        'quarter': quarter_str,
        'f1': f1_v3,
        'f2': f2_v3,
        'f3': f3_v3,
        'f4': f4_moat,
        'f5': f5_proj,
        'f6': f6,
        'f7': f7_v3,
        'f8': f8,
        'peg_score': peg_score,
        'momentum_score': momentum_score,
        'cqv_v1': cqv_v1,
        'cqv_v1_1': cqv_v1_1,
        'cqv_v2': cqv_v2,
        'cqv_v3': cqv_v3,
        'cqv': cqv_v3,  # default in table
        'pe': pe,
        'close_history': data.get('close_history', {}),
        'status': 'Success'
    }

def process_historical_company(cqv_result):
    ticker = cqv_result['ticker']
    yf_ticker = TICKER_MAP.get(ticker, ticker)
    
    # Read cache
    cache_path = os.path.join(CACHE_DIR, f"{yf_ticker}.json")
    if not os.path.exists(cache_path):
        return {'ticker': ticker, 'status': 'Error', 'error': 'Cache missing'}
        
    try:
        with open(cache_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        fin = data.get("financials", {})
        if not fin:
            return {'ticker': ticker, 'status': 'Success', 'history': {}}
            
        sorted_dates = sorted(list(fin.keys()))
        years = sorted_dates[-5:] # last 5 years
        
        info = data.get("info", {})
        sector = info.get("sector", "")
        
        # Qual/fixed factors from current V3 result
        f4 = cqv_result['f4']
        f5 = cqv_result['f5']
        f6 = cqv_result['f6']
        f8 = cqv_result['f8']
        
        history_scores = {}
        
        for idx, y_str in enumerate(years):
            yr_label = y_str[:4] # '2024'
            
            # Extract metrics for specific year
            metrics = extract_metrics(data, y_str)
            if not metrics.get("rev") or metrics["rev"] <= 0:
                continue
                
            # Compute historical factors
            # V3 factors
            f1_v3 = score_f1_rentabilidad_v3(metrics, info)
            f2_v3 = score_f2_solidez_v3(metrics, info, sector)
            
            # Growth calculation Yo-Y
            growth = 0.07
            if idx > 0:
                prev_y_str = years[idx-1]
                prev_metrics = extract_metrics(data, prev_y_str)
                prev_rev = prev_metrics.get("rev")
                if prev_rev and prev_rev > 0 and metrics.get("rev"):
                    growth = (metrics["rev"] - prev_rev) / prev_rev
            
            # Calculate F3 growth score
            if growth >= 0.15:
                growth_score = 10.0
            elif growth >= 0.06:
                growth_score = 7.0 + 3.0 * (growth - 0.06) / 0.09
            else:
                growth_score = max(1.0, 5.0 + 2.0 * (growth / 0.06))
                
            # M&A and Dilution defaults
            ma_score = 9.8 if ticker in ['CSU.TO', 'HEI', 'ACN'] else 8.5
            sec = (sector or '').lower()
            dilution_score = 8.0 if 'tech' in sec or 'software' in sec else 9.5
            if ticker in ['AAPL', 'FICO', 'AZO', 'ORLY', 'MUSA']:
                dilution_score = 10.0
                
            f3_v3 = round((growth_score + ma_score + dilution_score) / 3.0, 2)
            
            # F7 valuation historical
            f7_v3 = score_f7_fcf_yield_v3(metrics, info, f1_v3, ticker)
            
            # Compute historical P/E
            close_price = data.get("close_history", {}).get(yr_label)
            eps = metrics.get("eps")
            hist_pe = None
            if close_price and eps and eps > 0:
                hist_pe = round(close_price / eps, 2)
            elif yr_label == "2026":
                hist_pe = info.get('trailingPE') or info.get('forwardPE')
                if hist_pe:
                    hist_pe = round(hist_pe, 2)
            
            # Compute consolidated scores
            # CQV v1.0 (5F)
            cqv_v1 = (f1_v3 * 0.25) + (f2_v3 * 0.15) + (f3_v3 * 0.15) + (f4 * 0.25) + (f5 * 0.20)
            cqv_v1 = round(cqv_v1, 2)
            
            # CQV v1.1 (5F Pro with real ROIC & DEGRADATION)
            cqv_v1_1 = (f1_v3 * 0.25) + (f2_v3 * 0.15) + (f3_v3 * 0.15) + (f4 * 0.25) + (f5 * 0.20)
            if f4 < 6.0 or f2_v3 < 5.0:
                cqv_v1_1 = min(cqv_v1_1, 7.00)
            cqv_v1_1 = round(cqv_v1_1, 2)
            
            # CQV v2.0 (8F)
            cqv_v2 = (f1_v3 * 0.20) + (f2_v3 * 0.10) + (f3_v3 * 0.10) + (f4 * 0.20) + (f5 * 0.10) + (f6 * 0.10) + (f7_v3 * 0.10) + (f8 * 0.10)
            cqv_v2 = round(cqv_v2, 2)
            
            # CQV v3.0 (8F with real ROIC & DEGRADATION)
            cqv_v3 = (f1_v3 * 0.20) + (f2_v3 * 0.10) + (f3_v3 * 0.10) + (f4 * 0.20) + (f5 * 0.10) + (f6 * 0.10) + (f7_v3 * 0.10) + (f8 * 0.10)
            if f4 < 6.0 or f2_v3 < 5.0:
                cqv_v3 = min(cqv_v3, 7.00)
            cqv_v3 = round(cqv_v3, 2)
            
            history_scores[yr_label] = {
                'f1': f1_v3,
                'f2': f2_v3,
                'f3': f3_v3,
                'cqv_v1': cqv_v1,
                'cqv_v1_1': cqv_v1_1,
                'cqv_v2': cqv_v2,
                'cqv_v3': cqv_v3,
                'cqv': cqv_v3,
                'pe': hist_pe
            }
            
        return {
            'ticker': ticker,
            'history': history_scores,
            'status': 'Success'
        }
    except Exception as e:
        print(f"Error processing history for {ticker}: {e}")
        return {'ticker': ticker, 'status': 'Error', 'error': str(e)}

def main():
    print("==================================================")
    print("STARTING CQV PIPELINE (VERSION 3.0 PRO)")
    print("==================================================")
    
    results = []
    
    # Process current CQV in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        futures = {executor.submit(process_ticker, ticker): ticker for ticker in clean_tickers}
        for future in concurrent.futures.as_completed(futures):
            t = futures[future]
            try:
                res = future.result()
                results.append(res)
                print(f"Processed {t}: {res.get('status')}")
            except Exception as exc:
                print(f"{t} generated an exception: {exc}")
                results.append({'ticker': t, 'name': 'N/A', 'status': 'Error', 'error': str(exc)})

    # Filter successful processes
    success_results = [r for r in results if r['status'] == 'Success']
    error_results = [r for r in results if r['status'] != 'Success']
    
    # Sort by cqv_v3 desc
    success_results = sorted(success_results, key=lambda x: x['cqv_v3'], reverse=True)
    
    # 6. Save current CSV
    df = pd.DataFrame(success_results)
    df.to_csv('cqv_results.csv', index=False)
    print(f"\nSaved {len(success_results)} tickers to cqv_results.csv")
    
    # 7. Process history in parallel
    history_db = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        history_futures = {executor.submit(process_historical_company, r): r['ticker'] for r in success_results}
        for future in concurrent.futures.as_completed(history_futures):
            t = history_futures[future]
            try:
                h_res = future.result()
                if h_res.get('status') == 'Success':
                    history_db[t] = h_res['history']
            except Exception as exc:
                print(f"History exception for {t}: {exc}")

    # 8. Save history files
    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(history_db, f, indent=2)
    print("Saved cqv_history.json")
    
    js_history_content = f"const cqvHistoryData = {json.dumps(history_db, indent=2)};"
    with open('cqv_history.js', 'w', encoding='utf-8') as f:
        f.write(js_history_content)
    print("Saved cqv_history.js")

    # 9. Save current JSON data
    # We must ensure f6, f7, f8, cqv_v1, cqv_v2, cqv_v3 are correctly structured
    json_data = json.dumps(success_results, indent=2)
    with open('cqv_data.json', 'w', encoding='utf-8') as f:
        f.write(json_data)
    print("Saved cqv_data.json")
    
    js_data_content = f"window.companiesData = {json_data};"
    with open('cqv_data.js', 'w', encoding='utf-8') as f:
        f.write(js_data_content)
    print("Saved cqv_data.js")

    # 10. Inject data directly into dashboard.html to allow offline file:/// usage
    try:
        try:
            import generate_dashboard
            generate_dashboard.main()
        except Exception as ge:
            print(f"Warning running generate_dashboard: {ge}")
            
        html_path = 'dashboard.html'
        if os.path.exists(html_path):
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            start_marker = "<!-- DATA_INJECTION_START -->"
            end_marker = "<!-- DATA_INJECTION_END -->"
            
            # Load investment theses from inform/ directory
            theses_dict = {}
            inform_dir = 'inform'
            if os.path.exists(inform_dir):
                for fn in os.listdir(inform_dir):
                    if fn.endswith('.md'):
                        ticker = fn.split('_')[0].upper()
                        with open(os.path.join(inform_dir, fn), 'r', encoding='utf-8') as tf:
                            theses_dict[ticker] = tf.read()

            import re
            injection_block = f"""<!-- DATA_INJECTION_START -->
    <script>
        window.companiesData = {json_data};
        window.cqvHistoryData = {json.dumps(history_db, indent=2)};
        window.investmentTheses = {json.dumps(theses_dict, indent=2)};
    </script>
    <!-- DATA_INJECTION_END -->"""

            pattern = r'<!-- DATA_INJECTION_START -->[\s\S]*?<!-- DATA_INJECTION_END -->'
            if re.search(pattern, html_content):
                new_html = re.sub(pattern, lambda m: injection_block, html_content, count=1)
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(new_html)
                print("Successfully injected calculations and investment theses directly into dashboard.html")
            else:
                print("Warning: Data injection markers not found in dashboard.html")
    except Exception as e:
        print(f"Error injecting data into dashboard.html: {e}")

    # 11. Summary table in stdout
    print("\n==================================================")
    print("TOP 10 QUALITY COMPANIES (CQV V3.0)")
    print("==================================================")
    print("| Ticker | Nombre | F1 (Rent) | F2 (Solidez) | F4 (Moat) | CQV v1.0 | CQV v2.0 | CQV v3.0 |")
    print("| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |")
    for r in success_results[:10]:
        print(f"| **{r['ticker']}** | {r['name']} | {r['f1']:.2f} | {r['f2']:.2f} | {r['f4']:.2f} | {r['cqv_v1']:.2f} | {r['cqv_v2']:.2f} | **{r['cqv_v3']:.2f}** |")

    if error_results:
        print("\nERRORS DETECTED:")
        for r in error_results:
            print(f"- {r['ticker']}: {r.get('error')}")
    print("\nPipeline execution completed successfully.")

if __name__ == "__main__":
    main()
