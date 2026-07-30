import json
import re

# 1. Update cqv_data.json & cqv_data.js for GOOGL
with open('cqv_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    if item['ticker'] == 'GOOGL':
        item['pe'] = 16.75
        item['cqv_v4'] = 9.41
        item['cqv_v3'] = 9.41
        item['cqv'] = 9.41

data.sort(key=lambda x: x.get('cqv', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(data, indent=2) + ';')

# 2. Update cqv_history.json for GOOGL with 2020 history
with open('cqv_history.json', 'r', encoding='utf-8') as f:
    hist = json.load(f)

hist['GOOGL'] = {
    '2020': {'f1': 9.20, 'f2': 9.80, 'f3': 8.80, 'cqv_v1': 8.95, 'cqv_v1_1': 8.95, 'cqv_v2': 8.85, 'cqv_v3': 9.15, 'cqv_v4': 9.25, 'cqv': 9.25, 'pe': 28.50},
    '2021': {'f1': 9.40, 'f2': 9.80, 'f3': 9.10, 'cqv_v1': 9.10, 'cqv_v1_1': 9.10, 'cqv_v2': 8.95, 'cqv_v3': 9.25, 'cqv_v4': 9.32, 'cqv': 9.32, 'pe': 26.80},
    '2022': {'f1': 9.45, 'f2': 9.80, 'f3': 9.20, 'cqv_v1': 9.15, 'cqv_v1_1': 9.15, 'cqv_v2': 9.00, 'cqv_v3': 9.30, 'cqv_v4': 9.35, 'cqv': 9.35, 'pe': 19.20},
    '2023': {'f1': 9.50, 'f2': 9.80, 'f3': 9.30, 'cqv_v1': 9.20, 'cqv_v1_1': 9.20, 'cqv_v2': 9.05, 'cqv_v3': 9.35, 'cqv_v4': 9.38, 'cqv': 9.38, 'pe': 25.40},
    '2024': {'f1': 9.60, 'f2': 9.80, 'f3': 9.35, 'cqv_v1': 9.28, 'cqv_v1_1': 9.28, 'cqv_v2': 9.10, 'cqv_v3': 9.38, 'cqv_v4': 9.40, 'cqv': 9.40, 'pe': 27.10},
    '2025': {'f1': 9.65, 'f2': 9.80, 'f3': 9.40, 'cqv_v1': 9.30, 'cqv_v1_1': 9.30, 'cqv_v2': 9.12, 'cqv_v3': 9.40, 'cqv_v4': 9.40, 'cqv': 9.40, 'pe': 25.60}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(hist, indent=2) + ';')

# 3. Update dashboard.html
with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

json_str = json.dumps(data, indent=2)
hist_str = json.dumps(hist, indent=2)

html = re.sub(r'const cqvData = \[[\s\S]*?\];', f'const cqvData = {json_str};', html)
html = re.sub(r'const cqvHistory = \{[\s\S]*?\};', f'const cqvHistory = {hist_str};', html)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SYNCHRONIZED_GOOGL_V4_SUCCESSFULLY")
