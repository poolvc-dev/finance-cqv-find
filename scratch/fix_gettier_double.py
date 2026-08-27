import re

def fix_double_gettier(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    # Remove all duplicated getTier definitions and standardize to one clean definition
    code = re.sub(r'function getTier\(score\) \{[\s\S]*?\}function getTier\(score\) \{', 'function getTier(score) {', code)
    code = re.sub(r'return \{ name: \'tier-unknown\' \};?function getTier\(score\) \{', 'return { name: \'tier-unknown\' };\n', code)
    code = re.sub(r'return \{ name: \'N/D\', class: \'tier-unknown\' \};?function getTier\(score\) \{', 'return { name: \'N/D\', class: \'tier-unknown\' };\n', code)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"[OK] Cleaned double getTier in {filepath}")

fix_double_gettier("generate_dashboard.py")
fix_double_gettier("dashboard.html")
