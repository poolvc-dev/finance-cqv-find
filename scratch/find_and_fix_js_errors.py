import subprocess
import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the main <script> tag at the bottom of body
pos = html.rfind('<script>')
end_pos = html.rfind('</script>')

js_code = html[pos+8:end_pos]
with open('temp_main_script.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

res = subprocess.run(['node', '--check', 'temp_main_script.js'], capture_output=True, text=True)
print("NODE JS CHECK RESULT:")
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)

if res.returncode != 0:
    lines = js_code.split('\n')
    # Try to parse line number from stderr
    match = re.search(r'temp_main_script\.js:(\d+)', res.stderr)
    if match:
        err_line = int(match.group(1))
        print(f"\nError around line {err_line}:")
        start_l = max(0, err_line - 5)
        end_l = min(len(lines), err_line + 5)
        for i in range(start_l, end_l):
            marker = ">>> " if i + 1 == err_line else "    "
            print(f"{marker}{i+1}: {lines[i]}")
