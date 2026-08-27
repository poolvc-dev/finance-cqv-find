with open('generate_dashboard.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace("import os\n    history_db =", "history_db =")
code = code.replace("import os", "")

code = "import os\n" + code

with open('generate_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("[OK] Fixed import os scope in generate_dashboard.py")
