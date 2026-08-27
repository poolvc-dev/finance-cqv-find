import subprocess
import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract every inline <script> block and save to disk
pattern = r'<script(?![^>]*src=)[^>]*>([\s\S]*?)</script>'
for idx, match in enumerate(re.finditer(pattern, html)):
    content = match.group(1)
    filename = f'temp_script_block_{idx}.js'
    with open(filename, 'w', encoding='utf-8') as sf:
        sf.write(content)
    print(f"Checking {filename} ({len(content)} chars)...")
    res = subprocess.run(['node', '--check', filename], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FAILED {filename}:")
        print(res.stderr)
    else:
        print(f"SUCCESS {filename}")
