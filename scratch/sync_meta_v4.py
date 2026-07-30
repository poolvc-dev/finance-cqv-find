import json
import re

# 1. Update cqv_data.json & cqv_data.js for META
with open('cqv_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    if item['ticker'] == 'META':
        item['pe'] = 21.60
        item['cqv_v4'] = 9.46
        item['cqv_v3'] = 9.16
        item['cqv'] = 9.46

data.sort(key=lambda x: x.get('cqv', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(data, indent=2) + ';')

# 2. Update cqv_history.json for META with 2020 history
with open('cqv_history.json', 'r', encoding='utf-8') as f:
    hist = json.load(f)

hist['META'] = {
    '2020': {'f1': 9.10, 'f2': 9.50, 'f3': 9.20, 'cqv_v1': 8.75, 'cqv_v1_1': 8.75, 'cqv_v2': 8.70, 'cqv_v3': 8.85, 'cqv_v4': 8.95, 'cqv': 8.95, 'pe': 31.20},
    '2021': {'f1': 9.25, 'f2': 9.50, 'f3': 9.40, 'cqv_v1': 8.90, 'cqv_v1_1': 8.90, 'cqv_v2': 8.80, 'cqv_v3': 8.95, 'cqv_v4': 9.02, 'cqv': 9.02, 'pe': 23.80},
    '2022': {'f1': 9.00, 'f2': 9.50, 'f3': 8.80, 'cqv_v1': 8.80, 'cqv_v1_1': 8.80, 'cqv_v2': 8.65, 'cqv_v3': 8.80, 'cqv_v4': 8.95, 'cqv': 8.95, 'pe': 14.50},
    '2023': {'f1': 9.20, 'f2': 9.50, 'f3': 9.50, 'cqv_v1': 9.05, 'cqv_v1_1': 9.05, 'cqv_v2': 8.90, 'cqv_v3': 9.05, 'cqv_v4': 9.08, 'cqv': 9.08, 'pe': 28.40},
    '2024': {'f1': 9.25, 'f2': 9.50, 'f3': 9.70, 'cqv_v1': 9.15, 'cqv_v1_1': 9.15, 'cqv_v2': 9.00, 'cqv_v3': 9.12, 'cqv_v4': 9.12, 'cqv': 9.12, 'pe': 29.50},
    '2025': {'f1': 9.28, 'f2': 9.50, 'f3': 9.75, 'cqv_v1': 9.20, 'cqv_v1_1': 9.20, 'cqv_v2': 9.05, 'cqv_v3': 9.15, 'cqv_v4': 9.14, 'cqv': 9.14, 'pe': 26.80}
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

print("SYNCHRONIZED_META_V4_SUCCESSFULLY")
