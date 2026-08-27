import subprocess
import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract script contents (ignoring script tags with src=...)
pattern = r'<script(?![^>]*src=)[^>]*>([\s\S]*?)</script>'
matches = re.finditer(pattern, html)

for i, m in enumerate(matches):
    script_text = m.group(1).strip()
    if not script_text:
        continue
    filename = f'temp_check_{i}.js'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(script_text)
    
    res = subprocess.run(['node', '--check', filename], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FAILED Script Block {i}:")
        print(res.stderr)
        lines = script_text.split('\n')
        err_match = re.search(rf'{filename}:(\d+)', res.stderr)
        if err_match:
            l_num = int(err_match.group(1))
            for idx in range(max(0, l_num-4), min(len(lines), l_num+4)):
                print(f"  Line {idx+1}: {lines[idx]}")
    else:
        print(f"[OK] Script Block {i} syntax valid ({len(script_text)} chars)")
