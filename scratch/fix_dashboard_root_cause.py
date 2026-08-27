import json
import re

# 1. Update sync_cqv.py
with open("sync_cqv.py", "r", encoding="utf-8") as f:
    sync_code = f.read()

sync_code = re.sub(
    r'def write_data\(path, data, variable=None\):[\s\S]*?if variable:\s*handle\.write\(";"\)',
    '''def write_data(path, data, variable=None):
    with open(path, "w", encoding="utf-8") as handle:
        if variable == "cqvData":
            handle.write("window.cqvData = ")
        elif variable == "cqvHistory":
            handle.write("window.cqvHistoryData = ")
        elif variable:
            handle.write(f"window.{variable} = ")
        json.dump(data, handle, indent=2, ensure_ascii=False)
        if variable == "cqvHistory":
            handle.write(";\\nwindow.cqvHistory = window.cqvHistoryData;")
        elif variable:
            handle.write(";")''',
    sync_code
)

with open("sync_cqv.py", "w", encoding="utf-8") as f:
    f.write(sync_code)
print("[OK] Updated sync_cqv.py write_data function")

# 2. Update generate_dashboard.py to move helper functions formatDashboardScore and getTier to top of script
with open("generate_dashboard.py", "r", encoding="utf-8") as f:
    gd_code = f.read()

helpers_code = """
        function formatDashboardScore(value) {
            return (value !== undefined && value !== null && Number.isFinite(Number(value))) ? Number(value).toFixed(2) : 'N/D';
        }

        function getTier(score) {
            if (!Number.isFinite(Number(score))) return { name: 'N/D', class: 'tier-unknown' };
            if (score >= 9.0) return { name: 'ÉLITE', class: 'tier-elite' };
            if (score >= 8.5) return { name: 'SÓLIDA', class: 'tier-strong' };
            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };
            return { name: 'ESPECULATIVA', class: 'tier-speculative' };
        }
"""

if "function formatDashboardScore" not in gd_code[:gd_code.find("let companies = [];") + 100]:
    gd_code = gd_code.replace("let companies = [];", "let companies = [];\n" + helpers_code)

with open("generate_dashboard.py", "w", encoding="utf-8") as f:
    f.write(gd_code)
print("[OK] Updated generate_dashboard.py with top-level helper functions")

# 3. Update dashboard.html directly
with open("dashboard.html", "r", encoding="utf-8") as f:
    dh_code = f.read()

if "function formatDashboardScore" not in dh_code[:dh_code.find("let companies = [];") + 100]:
    dh_code = dh_code.replace("let companies = [];", "let companies = [];\n" + helpers_code)

with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(dh_code)
print("[OK] Updated dashboard.html with top-level helper functions")
