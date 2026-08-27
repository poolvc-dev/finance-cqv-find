with open('generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

if "import os" not in code[:100]:
    code = "import os\n" + code

with open('generate_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("[OK] Added import os to top of generate_dashboard.py")
