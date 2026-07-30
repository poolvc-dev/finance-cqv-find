import json
import re

# Load updated cqv_data.json & cqv_history.json
with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Read dashboard.html
with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update window.cqvHistoryData
hist_json_str = json.dumps(cqv_hist, indent=2)
html = re.sub(r'window\.cqvHistoryData\s*=\s*\{[\s\S]*?\};', lambda m: f'window.cqvHistoryData = {hist_json_str};', html)

# 2. Update let companies = [...]
comp_json_str = json.dumps(cqv_list, indent=2)
html = re.sub(r'let companies\s*=\s*\[[\s\S]*?\];', lambda m: f'let companies = {comp_json_str};', html)

# 3. Fix loadCompanyHistory() in dashboard.html to include 2020 and 2021 and compute v4 correctly
# Let's check how loadCompanyHistory is structured
old_load_hist_code = """            const years = Object.keys(history).sort();
            const chartLabels = years.map(yr => (yr === "2026" && !rawHistory["2026"]) ? "2026 (Act.)" : yr);"""

new_load_hist_code = """            // Ensure 2020 to 2026 are present in years
            let yearList = ["2020", "2021", "2022", "2023", "2024", "2025", "2026"];
            const availableKeys = Object.keys(history);
            const years = yearList.filter(yr => availableKeys.includes(yr) || yr === "2026");
            const chartLabels = years.map(yr => yr === "2026" ? "2026 (Act.)" : yr);"""

html = html.replace(old_load_hist_code, new_load_hist_code)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("EMBEDDED_DATA_AND_HISTORY_LOCATIONS_UPDATED_SUCCESSFULLY")
