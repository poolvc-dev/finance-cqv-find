import json
import re

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    if item['ticker'] == 'FICO':
        item['pe'] = 42.38

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(data, indent=2) + ';')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

json_str = json.dumps(data, indent=2)
html = re.sub(r'const cqvData = \[[\s\S]*?\];', f'const cqvData = {json_str};', html)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("UPDATED_FICO_PE_IN_DATASETS_AND_DASHBOARD")
