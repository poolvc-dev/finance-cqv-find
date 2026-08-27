import re

# 1. Clean generate_dashboard.py
with open("generate_dashboard.py", "r", encoding="utf-8") as f:
    gd_code = f.read()

# Remove any second DATA_INJECTION_START block in template body
gd_code = re.sub(
    r'<!-- DATA_INJECTION_START -->\s*<script src="cqv_data\.js"></script>\s*<script src="cqv_history\.js"></script>\s*<!-- DATA_INJECTION_END -->',
    '',
    gd_code
)

with open("generate_dashboard.py", "w", encoding="utf-8") as f:
    f.write(gd_code)
print("[OK] Removed duplicate DATA_INJECTION_START block in generate_dashboard.py")

# 2. Clean dashboard.html
with open("dashboard.html", "r", encoding="utf-8") as f:
    dh_code = f.read()

# Remove second DATA_INJECTION_START block at bottom of body
dh_code = re.sub(
    r'<!-- DATA_INJECTION_START -->\s*<script src="cqv_data\.js"></script>\s*<script src="cqv_history\.js"></script>\s*<!-- DATA_INJECTION_END -->',
    '',
    dh_code
)

with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(dh_code)
print("[OK] Removed duplicate DATA_INJECTION_START block in dashboard.html")
