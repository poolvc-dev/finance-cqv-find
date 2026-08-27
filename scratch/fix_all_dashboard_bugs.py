import re

# 1. Fix sync_cqv.py write_data
with open('sync_cqv.py', 'r', encoding='utf-8') as f:
    sync_code = f.read()

sync_code = sync_code.replace(
    'handle.write(f"const {variable} = ")',
    'handle.write(f"window.{variable} = ")'
)

with open('sync_cqv.py', 'w', encoding='utf-8') as f:
    f.write(sync_code)
print("[OK] Updated sync_cqv.py write_data to use window.variable")

# 2. Fix generate_dashboard.py
with open('generate_dashboard.py', 'r', encoding='utf-8') as f:
    gd_code = f.read()

# Replace unsafe toFixed calls in renderTable inside generate_dashboard.py
gd_code = gd_code.replace("${c.f1.toFixed(2)}", "${formatDashboardScore(c.f1)}")
gd_code = gd_code.replace("${c.f2.toFixed(2)}", "${formatDashboardScore(c.f2)}")
gd_code = gd_code.replace("${c.f3.toFixed(2)}", "${formatDashboardScore(c.f3)}")
gd_code = gd_code.replace("${c.f4.toFixed(2)}", "${formatDashboardScore(c.f4)}")
gd_code = gd_code.replace("${c.f5.toFixed(2)}", "${formatDashboardScore(c.f5)}")
gd_code = gd_code.replace("${c.f6.toFixed(2)}", "${formatDashboardScore(c.f6)}")
gd_code = gd_code.replace("${c.f7.toFixed(2)}", "${formatDashboardScore(c.f7)}")
gd_code = gd_code.replace("${c.f8.toFixed(2)}", "${formatDashboardScore(c.f8)}")
gd_code = gd_code.replace("${c.cqv.toFixed(2)}", "${formatDashboardScore(c.cqv)}")
gd_code = gd_code.replace("${yrCqv.toFixed(2)}", "${formatDashboardScore(yrCqv)}")
gd_code = gd_code.replace("${diff.toFixed(2)}", "${formatDashboardScore(diff)}")

with open('generate_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(gd_code)
print("[OK] Updated generate_dashboard.py with safe score formatters")

# 3. Fix dashboard.html directly as well
with open('dashboard.html', 'r', encoding='utf-8') as f:
    dh_code = f.read()

dh_code = dh_code.replace("${c.f1.toFixed(2)}", "${formatDashboardScore(c.f1)}")
dh_code = dh_code.replace("${c.f2.toFixed(2)}", "${formatDashboardScore(c.f2)}")
dh_code = dh_code.replace("${c.f3.toFixed(2)}", "${formatDashboardScore(c.f3)}")
dh_code = dh_code.replace("${c.f4.toFixed(2)}", "${formatDashboardScore(c.f4)}")
dh_code = dh_code.replace("${c.f5.toFixed(2)}", "${formatDashboardScore(c.f5)}")
dh_code = dh_code.replace("${c.f6.toFixed(2)}", "${formatDashboardScore(c.f6)}")
dh_code = dh_code.replace("${c.f7.toFixed(2)}", "${formatDashboardScore(c.f7)}")
dh_code = dh_code.replace("${c.f8.toFixed(2)}", "${formatDashboardScore(c.f8)}")
dh_code = dh_code.replace("${c.cqv.toFixed(2)}", "${formatDashboardScore(c.cqv)}")
dh_code = dh_code.replace("${yrCqv.toFixed(2)}", "${formatDashboardScore(yrCqv)}")
dh_code = dh_code.replace("${diff.toFixed(2)}", "${formatDashboardScore(diff)}")

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dh_code)
print("[OK] Updated dashboard.html with safe score formatters")
