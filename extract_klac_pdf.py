import pdfplumber, re, os
from datetime import datetime
PDF_PATH = os.path.join('tmp', 'klac_report.pdf')
OUTPUT_MD = os.path.join('inform', 'klac_2026_q2.md')
TEMPLATE_PATH = os.path.join('inform', 'template.md')

def parse_pdf():
    if not os.path.exists(PDF_PATH):
        print(f'PDF not found at {PDF_PATH}')
        return ''
    with pdfplumber.open(PDF_PATH) as pdf:
        return '\n'.join(page.extract_text() or '' for page in pdf.pages)

def generate_report(text):
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()
    report = template.replace('[TICKER]', 'KLAC')\
                     .replace('[Nombre de la Empresa]', 'KLA Corporation')\
                     .replace('[Trimestre/Año ej. Q2 2026]', 'Q2 2026')\
                     .replace('[Fecha del Informe]', datetime.now().strftime('%Y-%m-%d'))
    with open(OUTPUT_MD, 'w', encoding='utf-8') as out:
        out.write(report)
    print(f'Report written to {OUTPUT_MD}')

if __name__ == '__main__':
    txt = parse_pdf()
    if txt:
        generate_report(txt)
