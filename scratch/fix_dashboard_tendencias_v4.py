import json
import re

# 1. Update cqv_history.json & cqv_history.js for FICO and all tickers
with open('cqv_history.json', 'r', encoding='utf-8') as f:
    hist = json.load(f)

# FICO exact history calibration (matching inform/fico_2026_q2.md)
hist['FICO'] = {
    '2020': {'f1': 9.30, 'f2': 8.50, 'f3': 8.40, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.32, 'cqv_v1_1': 9.32, 'cqv_v2': 9.25, 'cqv_v3': 9.25, 'cqv_v4': 9.30, 'cqv': 9.30, 'pe': 38.40},
    '2021': {'f1': 9.40, 'f2': 8.60, 'f3': 8.50, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.40, 'cqv_v1_1': 9.40, 'cqv_v2': 9.31, 'cqv_v3': 9.31, 'cqv_v4': 9.38, 'cqv': 9.38, 'pe': 41.10},
    '2022': {'f1': 9.50, 'f2': 8.75, 'f3': 8.61, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.46, 'cqv_v1_1': 9.46, 'cqv_v2': 9.38, 'cqv_v3': 9.38, 'cqv_v4': 9.45, 'cqv': 9.45, 'pe': 42.21},
    '2023': {'f1': 9.60, 'f2': 8.75, 'f3': 8.93, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.51, 'cqv_v1_1': 9.51, 'cqv_v2': 9.41, 'cqv_v3': 9.41, 'cqv_v4': 9.48, 'cqv': 9.48, 'pe': 68.75},
    '2024': {'f1': 9.70, 'f2': 8.75, 'f3': 9.33, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.57, 'cqv_v1_1': 9.57, 'cqv_v2': 9.45, 'cqv_v3': 9.45, 'cqv_v4': 9.52, 'cqv': 9.52, 'pe': 97.36},
    '2025': {'f1': 9.85, 'f2': 8.75, 'f3': 9.50, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.59, 'cqv_v1_1': 9.59, 'cqv_v2': 9.47, 'cqv_v3': 9.47, 'cqv_v4': 9.55, 'cqv': 9.55, 'pe': 63.70},
    '2026': {'f1': 10.0, 'f2': 9.36, 'f3': 9.82, 'f4': 9.91, 'f5': 9.69, 'f6': 9.51, 'f7': 9.45, 'f8': 8.66, 'cqv_v1': 9.60, 'cqv_v1_1': 9.60, 'cqv_v2': 9.49, 'cqv_v3': 9.49, 'cqv_v4': 9.62, 'cqv': 9.62, 'pe': 42.38}
}

# Update cqv_data.json close_history for FICO
with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

for item in cqv_list:
    if item['ticker'] == 'FICO':
        item['close_history'] = {
            '2020': 350.00,
            '2021': 433.67,
            '2022': 598.58,
            '2023': 1164.01,
            '2024': 1990.93,
            '2025': 1690.62,
            '2026': 1373.08
        }

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

with open('cqv_history.json', 'w', encoding='utf-8') as f:
    json.dump(hist, f, indent=2)

with open('cqv_history.js', 'w', encoding='utf-8') as f:
    f.write('const cqvHistory = ' + json.dumps(hist, indent=2) + ';')

# 2. Update dashboard.html loadCompanyHistory function logic
with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace JS logic in loadCompanyHistory for historical score calculation
old_calc_code = """                // Recalculate historical CQV using 8 factors (F1-F3 historical, F4-F8 fixed/current)
                const cqv_v2 = (
                    data.f1 * 0.20 +
                    data.f2 * 0.10 +
                    data.f3 * 0.10 +
                    company.f4 * 0.20 +
                    company.f5 * 0.10 +
                    company.f6 * 0.10 +
                    company.f7 * 0.10 +
                    company.f8 * 0.10
                );
                chartData.push(cqv_v2);"""

new_calc_code = """                // Compute historical CQV according to currentVersion (v4, v3, v2, v1)
                let cqvScoreHist = data.cqv_v4 || data.cqv;
                if (currentVersion === 'v4') {
                    cqvScoreHist = data.cqv_v4 || (
                        data.f1 * 0.20 +
                        data.f2 * 0.15 +
                        data.f3 * 0.15 +
                        (company.f4 || 9.0) * 0.15 +
                        (company.f5 || 9.0) * 0.10 +
                        (company.f6 || 9.0) * 0.10 +
                        (company.f7 || 8.5) * 0.05 +
                        (company.f8 || 9.0) * 0.10
                    );
                } else if (currentVersion === 'v3') {
                    cqvScoreHist = data.cqv_v3 || (
                        data.f1 * 0.20 +
                        data.f2 * 0.10 +
                        data.f3 * 0.10 +
                        (company.f4 || 9.0) * 0.20 +
                        (company.f5 || 9.0) * 0.10 +
                        (company.f6 || 9.0) * 0.10 +
                        (company.f7 || 8.5) * 0.10 +
                        (company.f8 || 9.0) * 0.10
                    );
                } else if (currentVersion === 'v2') {
                    cqvScoreHist = data.cqv_v2 || data.cqv;
                } else {
                    cqvScoreHist = data.cqv_v1 || data.cqv;
                }
                cqvScoreHist = Number(cqvScoreHist.toFixed(2));
                chartData.push(cqvScoreHist);"""

old_cell_code = """<td class="cqv-value-cell score-high" style="font-weight: bold;">${cqv_v2.toFixed(2)}</td>"""
new_cell_code = """<td class="cqv-value-cell score-high" style="font-weight: bold;">${cqvScoreHist.toFixed(2)}</td>"""

html = html.replace(old_calc_code, new_calc_code)
html = html.replace(old_cell_code, new_cell_code)

# Ensure cqvData and cqvHistory are injected into HTML
json_str = json.dumps(cqv_list, indent=2)
hist_str = json.dumps(hist, indent=2)

html = re.sub(r'const cqvData = \[[\s\S]*?\];', lambda m: f'const cqvData = {json_str};', html)
html = re.sub(r'const cqvHistory = \{[\s\S]*?\};', lambda m: f'const cqvHistory = {hist_str};', html)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("UPDATED_DASHBOARD_TENDENCIAS_AND_FICO_HISTORY_TO_2020_SUCCESSFULLY")
