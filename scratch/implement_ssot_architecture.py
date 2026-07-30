import json
import re
import os

print("Implementing Single Source of Truth (SSOT) Architecture...")

# Read dashboard.html
with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update JS to prioritize window.cqvData and window.cqvHistory
html = html.replace(
    "companies = window.companiesData || (typeof companiesData !== 'undefined' ? companiesData : []);",
    "companies = (typeof cqvData !== 'undefined' ? cqvData : (window.cqvData || window.companiesData || []));"
)

html = html.replace(
    "const historyObj = window.cqvHistoryData || (typeof cqvHistoryData !== 'undefined' ? cqvHistoryData : null);",
    "const historyObj = (typeof cqvHistory !== 'undefined' ? cqvHistory : (window.cqvHistory || window.cqvHistoryData || {}));"
)

html = html.replace(
    "const historyObj = window.cqvHistoryData || (typeof cqvHistoryData !== 'undefined' ? cqvHistoryData : {});",
    "const historyObj = (typeof cqvHistory !== 'undefined' ? cqvHistory : (window.cqvHistory || window.cqvHistoryData || {}));"
)

html = html.replace(
    "const rawHistory = (typeof cqvHistoryData !== 'undefined' && cqvHistoryData[ticker]) ? cqvHistoryData[ticker] : {};",
    "const rawHistory = (typeof cqvHistory !== 'undefined' && cqvHistory[ticker]) ? cqvHistory[ticker] : ((typeof cqvHistoryData !== 'undefined' && cqvHistoryData[ticker]) ? cqvHistoryData[ticker] : {});"
)

# 2. Inject updated cqv_data.js and cqv_history.js content into html markers
with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

json_str = json.dumps(cqv_list, indent=2)
hist_str = json.dumps(cqv_hist, indent=2)

# Update embedded script blocks to sync SSOT
html = re.sub(r'window\.companiesData\s*=\s*\[[\s\S]*?\];', lambda m: f'window.companiesData = {json_str};', html)
html = re.sub(r'let companies\s*=\s*\[[\s\S]*?\];', lambda m: f'let companies = {json_str};', html)
html = re.sub(r'window\.cqvHistoryData\s*=\s*\{[\s\S]*?\};', lambda m: f'window.cqvHistoryData = {hist_str};', html)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SSOT_ARCHITECTURE_IMPLEMENTED_IN_DASHBOARD")
