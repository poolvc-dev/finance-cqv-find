import json
import re
import os

# 1. Update cqv_qualitative_config.json for FICO under v4.0
with open('cqv_qualitative_config.json', 'r', encoding='utf-8') as f:
    cfg = json.load(f)

cfg['FICO'] = {
    'f1': 10.00,
    'f2': 9.36,
    'f3': 9.82,
    'f4': 9.91,
    'f5': 9.69,
    'f6': 9.51,
    'f7': 9.45,
    'f8': 8.66
}

with open('cqv_qualitative_config.json', 'w', encoding='utf-8') as f:
    json.dump(cfg, f, indent=2)

# 2. Update cqv_data.json & cqv_data.js
with open('cqv_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    if item.get('ticker') == 'FICO':
        item['quarter'] = 'Q3 FY26 (Q2 26)'
        item['f1'] = 10.00
        item['f2'] = 9.36
        item['f3'] = 9.82
        item['f4'] = 9.91
        item['f5'] = 9.69
        item['f6'] = 9.51
        item['f7'] = 9.45
        item['f8'] = 8.66
        item['cqv_v1'] = 9.60
        item['cqv_v1_1'] = 9.60
        item['cqv_v2'] = 9.49
        item['cqv_v3'] = 9.49
        item['cqv_v4'] = 9.62
        item['cqv'] = 9.62  # v4 is now official standard

data.sort(key=lambda x: x.get('cqv', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(data, indent=2) + ';')

# 3. Update cqv_history.json & cqv_history.js
with open('cqv_history.json', 'r', encoding='utf-8') as f:
    hist = json.load(f)

hist['FICO'] = {
    '2022': {'f1': 10.0, 'f2': 8.75, 'f3': 8.61, 'cqv_v1': 9.46, 'cqv_v1_1': 9.46, 'cqv_v2': 9.38, 'cqv_v3': 9.38, 'cqv_v4': 9.45, 'cqv': 9.45, 'pe': 42.21},
    '2023': {'f1': 10.0, 'f2': 8.75, 'f3': 8.93, 'cqv_v1': 9.51, 'cqv_v1_1': 9.51, 'cqv_v2': 9.41, 'cqv_v3': 9.41, 'cqv_v4': 9.48, 'cqv': 9.48, 'pe': 68.75},
    '2024': {'f1': 10.0, 'f2': 8.75, 'f3': 9.33, 'cqv_v1': 9.57, 'cqv_v1_1': 9.57, 'cqv_v2': 9.45, 'cqv_v3': 9.45, 'cqv_v4': 9.52, 'cqv': 9.52, 'pe': 97.36},
    '2025': {'f1': 10.0, 'f2': 8.75, 'f3': 9.50, 'cqv_v1': 9.59, 'cqv_v1_1': 9.59, 'cqv_v2': 9.47, 'cqv_v3': 9.47, 'cqv_v4': 9.55, 'cqv': 9.55, 'pe': 63.70}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(hist, indent=2) + ';')

# 4. Update dashboard.html
with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

json_str = json.dumps(data, indent=2)
hist_str = json.dumps(hist, indent=2)

html = re.sub(r'const cqvData = \[[\s\S]*?\];', f'const cqvData = {json_str};', html)
html = re.sub(r'const cqvHistory = \{[\s\S]*?\};', f'const cqvHistory = {hist_str};', html)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("UPDATED_FICO_V4_SUCCESSFULLY")
