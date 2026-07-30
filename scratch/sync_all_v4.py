import json
import re
import os

tickers_list = ['FICO', 'MSFT', 'GOOGL', 'ISRG', 'KNSL', 'META', 'MSCI', 'NVDA', 'ORLY', 'SPGI', 'NOW', 'ASML', 'FTNT']

# 1. Load cqv_data.json
with open('cqv_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Factor weights for v3 and v4
# v3: F1: 20%, F2: 10%, F3: 10%, F4: 20%, F5: 10%, F6: 10%, F7: 10%, F8: 10%
# v4: F1: 20%, F2: 15%, F3: 15%, F4: 15%, F5: 10%, F6: 10%, F7: 5%, F8: 10%

def calc_v3(f):
    return round((f[0]*0.20)+(f[1]*0.10)+(f[2]*0.10)+(f[3]*0.20)+(f[4]*0.10)+(f[5]*0.10)+(f[6]*0.10)+(f[7]*0.10), 2)

def calc_v4(f):
    return round((f[0]*0.20)+(f[1]*0.15)+(f[2]*0.15)+(f[3]*0.15)+(f[4]*0.10)+(f[5]*0.10)+(f[6]*0.05)+(f[7]*0.10), 2)

for item in data:
    f = [item.get(f'f{i}', 8.0) for i in range(1, 9)]
    v3_val = calc_v3(f)
    v4_val = calc_v4(f)
    
    # Check degradation filter for v3 and v4
    f2_val = f[1]
    f4_val = f[3]
    
    if f4_val < 6.0 or f2_val < 5.0:
        v3_val = min(v3_val, 7.00)
    if f4_val < 4.0 or f2_val < 4.0:
        v4_val = min(v4_val, 6.99)
        
    item['cqv_v3'] = v3_val
    item['cqv_v4'] = v4_val
    item['cqv'] = v4_val  # v4 is official standard

# Sort dataset by cqv (v4.0) descending
data.sort(key=lambda x: x.get('cqv', 0), reverse=True)

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(data, indent=2) + ';')

# 2. Update cqv_history.json & cqv_history.js
with open('cqv_history.json', 'r', encoding='utf-8') as f:
    hist = json.load(f)

for t in hist:
    for yr in hist[t]:
        yr_data = hist[t][yr]
        f1 = yr_data.get('f1', 8.0)
        f2 = yr_data.get('f2', 8.0)
        f3 = yr_data.get('f3', 8.0)
        cqv_v3 = yr_data.get('cqv_v3', 8.0)
        # Calculate approximate v4 history for historical visualization
        cqv_v4 = round((f1*0.20) + (f2*0.15) + (f3*0.15) + (cqv_v3*0.15) + (8.5*0.10) + (8.5*0.10) + (7.0*0.05) + (8.0*0.10), 2)
        yr_data['cqv_v4'] = cqv_v4
        yr_data['cqv'] = cqv_v4

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

print("SYNCHRONIZED_ALL_DATASETS_AND_DASHBOARD_FOR_CQV_V4")
