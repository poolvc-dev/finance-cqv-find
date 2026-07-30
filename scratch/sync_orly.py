import json
import re
import os

# 1. Update cqv_data.json
with open('cqv_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

found = False
for item in data:
    if item.get('ticker') == 'ORLY':
        found = True
        item['quarter'] = 'Q2 2026'
        item['f1'] = 9.40
        item['f2'] = 8.50
        item['f3'] = 9.00
        item['f4'] = 9.50
        item['f5'] = 9.00
        item['f6'] = 9.80
        item['f7'] = 8.40
        item['f8'] = 9.50
        item['cqv_v1'] = 9.20
        item['cqv_v1_1'] = 9.20
        item['cqv_v2'] = 9.20
        item['cqv_v3'] = 9.20
        item['cqv'] = 9.20
        item['pe'] = 26.50

if not found:
    new_item = {
        'ticker': 'ORLY',
        'name': "O'Reilly Automotive, Inc.",
        'sector': 'Consumer Cyclical',
        'quarter': 'Q2 2026',
        'f1': 9.40,
        'f2': 8.50,
        'f3': 9.00,
        'f4': 9.50,
        'f5': 9.00,
        'f6': 9.80,
        'f7': 8.40,
        'f8': 9.50,
        'peg_score': 7.50,
        'momentum_score': 8.20,
        'cqv_v1': 9.20,
        'cqv_v1_1': 9.20,
        'cqv_v2': 9.20,
        'cqv_v3': 9.20,
        'cqv': 9.20,
        'pe': 26.50,
        'close_history': "{'2021': 47.08, '2022': 56.27, '2023': 63.34, '2024': 79.05, '2025': 91.21, '2026': 86.25}",
        'status': 'Success'
    }
    data.append(new_item)

# Sort data by cqv descending
data.sort(key=lambda x: x.get('cqv', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(data, indent=2) + ';')

# 2. Update cqv_history.json
with open('cqv_history.json', 'r', encoding='utf-8') as f:
    hist = json.load(f)

hist['ORLY'] = {
    '2021': {'f1': 8.63, 'f2': 8.35, 'f3': 8.61, 'cqv_v1': 8.69, 'cqv_v1_1': 8.69, 'cqv_v2': 8.79, 'cqv_v3': 8.79, 'cqv': 8.79, 'pe': None},
    '2022': {'f1': 8.63, 'f2': 8.35, 'f3': 8.61, 'cqv_v1': 8.69, 'cqv_v1_1': 8.69, 'cqv_v2': 8.79, 'cqv_v3': 8.79, 'cqv': 8.79, 'pe': 25.24},
    '2023': {'f1': 8.53, 'f2': 8.22, 'f3': 8.91, 'cqv_v1': 8.69, 'cqv_v1_1': 8.69, 'cqv_v2': 8.78, 'cqv_v3': 8.78, 'cqv': 8.78, 'pe': 24.70},
    '2024': {'f1': 8.48, 'f2': 8.22, 'f3': 8.46, 'cqv_v1': 8.61, 'cqv_v1_1': 8.61, 'cqv_v2': 8.73, 'cqv_v3': 8.73, 'cqv': 8.73, 'pe': 29.16},
    '2025': {'f1': 8.42, 'f2': 8.23, 'f3': 8.55, 'cqv_v1': 8.61, 'cqv_v1_1': 8.61, 'cqv_v2': 8.73, 'cqv_v3': 8.73, 'cqv': 8.73, 'pe': 30.71}
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

print("SYNCHRONIZED_ORLY_IN_DATASETS_AND_DASHBOARD_SUCCESSFULLY")
