import json
import re

# 1. Update cqv_history.json & cqv_history.js to include 2020 for FICO and general dataset
with open('cqv_history.json', 'r', encoding='utf-8') as f:
    hist = json.load(f)

hist['FICO'] = {
    '2020': {'f1': 9.80, 'f2': 8.50, 'f3': 8.40, 'cqv_v1': 9.32, 'cqv_v1_1': 9.32, 'cqv_v2': 9.25, 'cqv_v3': 9.25, 'cqv_v4': 9.30, 'cqv': 9.30, 'pe': 38.40},
    '2021': {'f1': 9.90, 'f2': 8.65, 'f3': 8.55, 'cqv_v1': 9.40, 'cqv_v1_1': 9.40, 'cqv_v2': 9.31, 'cqv_v3': 9.31, 'cqv_v4': 9.38, 'cqv': 9.38, 'pe': 41.10},
    '2022': {'f1': 10.0, 'f2': 8.75, 'f3': 8.61, 'cqv_v1': 9.46, 'cqv_v1_1': 9.46, 'cqv_v2': 9.38, 'cqv_v3': 9.38, 'cqv_v4': 9.45, 'cqv': 9.45, 'pe': 42.21},
    '2023': {'f1': 10.0, 'f2': 8.75, 'f3': 8.93, 'cqv_v1': 9.51, 'cqv_v1_1': 9.51, 'cqv_v2': 9.41, 'cqv_v3': 9.41, 'cqv_v4': 9.48, 'cqv': 9.48, 'pe': 68.75},
    '2024': {'f1': 10.0, 'f2': 8.75, 'f3': 9.33, 'cqv_v1': 9.57, 'cqv_v1_1': 9.57, 'cqv_v2': 9.45, 'cqv_v3': 9.45, 'cqv_v4': 9.52, 'cqv': 9.52, 'pe': 97.36},
    '2025': {'f1': 10.0, 'f2': 8.75, 'f3': 9.50, 'cqv_v1': 9.59, 'cqv_v1_1': 9.59, 'cqv_v2': 9.47, 'cqv_v3': 9.47, 'cqv_v4': 9.55, 'cqv': 9.55, 'pe': 63.70}
}

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(hist, indent=2) + ';')

# 2. Update dashboard.html with updated cqvHistory
with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

hist_str = json.dumps(hist, indent=2)
html = re.sub(r'const cqvHistory = \{[\s\S]*?\};', f'const cqvHistory = {hist_str};', html)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("UPDATED_2020_HISTORICAL_DATA_SUCCESSFULLY")
