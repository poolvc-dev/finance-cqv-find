import os
import json

TEMPLATE_PATH = os.path.join('inform', 'template.md')
DATA_PATH = os.path.join('tmp', 'klac_q2_data.json')
OUTPUT_PATH = os.path.join('inform', 'klac_2026_q2.md')

def load_template():
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def load_data():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def substitute(template, data):
    # Simple placeholder replacement: [X] or $[X]
    result = template
    # Quarter and ticker placeholders
    result = result.replace('[Trimestre/Año ej. Q2 2026]', data.get('quarter', 'Q2 2026'))
    result = result.replace('[TICKER]', 'KLAC')
    result = result.replace('[Nombre de la Empresa]', data.get('name', 'KLA Corporation'))
    # Financial numbers – if missing, use N/A
    def fmt(val):
        return f M if isinstance(val, (int, float)) else 'N/A'
    result = result.replace('$[X]', fmt(data.get('revenue')))
    result = result.replace('[X]', fmt(data.get('net_income')))
    result = result.replace('[X]', fmt(data.get('diluted_eps')))
    # Additional placeholders can be added as needed
    return result

def main():
    tmpl = load_template()
    data = load_data()
    report = substitute(tmpl, data)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(report)
    print('Report written to', OUTPUT_PATH)

if __name__ == '__main__':
    main()
