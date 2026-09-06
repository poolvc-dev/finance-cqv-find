import json

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    history = json.load(f).get('PANW', {})

for year in sorted(history.keys()):
    print('=== YEAR:', year)
    data = history[year]
    if isinstance(data, dict):
        for q, val in data.items():
            if isinstance(val, dict):
                cqv = val.get('cqv')
                cqv_v4 = val.get('cqv_v4')
                cqv_v5 = val.get('cqv_v5')
                pe = val.get('pe')
                f1 = val.get('f1')
                f2 = val.get('f2')
                f3 = val.get('f3')
                f4 = val.get('f4')
                print(f'  [{q}] cqv={cqv}, v4={cqv_v4}, v5={cqv_v5}, pe={pe}, f1={f1}, f2={f2}, f3={f3}, f4={f4}')
            else:
                print(f'  [{q}] {val}')
