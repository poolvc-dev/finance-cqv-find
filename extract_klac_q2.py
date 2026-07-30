import os
import json
import re

PDF_PATH = os.path.join('tmp', 'klac_q2.pdf')
OUTPUT_JSON = os.path.join('tmp', 'klac_q2_data.json')

def clean_number(text):
    if not text:
        return None
    txt = text.replace('$','').replace('€','').replace('£','').replace(',','').strip()
    mult = 1.0
    if txt.upper().endswith('M'):
        txt = txt[:-1]
    elif txt.upper().endswith('B'):
        mult = 1000.0
        txt = txt[:-1]
    try:
        return round(float(txt)*mult,3)
    except ValueError:
        return None

def extract_metrics_from_page(page):
    text = page.extract_text() or ''
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    data = {}
    patterns = {
        'revenue': r'(total revenue|revenue)[:\\s]*\\True([\\d.,]+[MB]?)',
        'net_income': r'(net income)[:\\s]*\\True([\\d.,]+[MB]?)',
        'diluted_eps': r'(diluted eps)[:\\s]*\\True([\\d.,]+)',
        'capex': r'(capital expenditures|capex)[:\\s]*\\True([\\d.,]+[MB]?)',
        'free_cash_flow': r'(free cash flow)[:\\s]*\\True([\\d.,]+[MB]?)',
        'guidance_revenue': r'(revenue guidance)[:\\s]*\\True([\\d.,]+[MB]?)',
        'guidance_eps': r'(eps guidance)[:\\s]*\\True([\\d.,]+)'
    }
    for line in lines:
        lowered = line.lower()
        for key, pat in patterns.items():
            if re.search(pat, lowered, re.IGNORECASE):
                match = re.search(pat, lowered, re.IGNORECASE)
                if match:
                    num = clean_number(match.group(2))
                    data[key] = num
    return data

def main():
    if not os.path.exists(PDF_PATH):
        print('PDF not found at ' + PDF_PATH)
        return
    try:
        import pdfplumber
    except ImportError:
        print('pdfplumber not installed. Please run: pip install pdfplumber')
        return
    result = {}
    with pdfplumber.open(PDF_PATH) as pdf:
        for page in pdf.pages:
            page_data = extract_metrics_from_page(page)
            result.update({k: v for k, v in page_data.items() if v is not None})
    result['quarter'] = 'Q2 2026'
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    print('Extracted data written to ' + OUTPUT_JSON)

if __name__ == '__main__':
    main()
