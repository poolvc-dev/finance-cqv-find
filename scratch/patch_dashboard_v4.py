import re
import json

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update HTML dropdown option for version-select to include CQV v4.0 and make it selected by default
old_select_pattern = r'<select id="version-select"[\s\S]*?</select>'
new_select_html = '''<select id="version-select" class="select-filter" onchange="setCQVVersion(this.value)" style="padding: 4px 10px; border-radius: 20px; background: var(--input-bg); color: var(--font-title); border: 1px solid var(--primary); font-weight: 700; cursor: pointer; font-size: 0.82rem; height: 32px;">
                        <option value="v4" selected>CQV v4.0 (Estándar Operativo - 8F Pro)</option>
                        <option value="v3">CQV v3.0 (8F Pro)</option>
                        <option value="v2">CQV v2.0 (8F Legacy)</option>
                        <option value="v1_1">CQV v1.1 (5F Pro)</option>
                        <option value="v1">CQV v1.0 (5F Legacy)</option>
                    </select>'''

html = re.sub(old_select_pattern, new_select_html, html)

# 2. Update default currentVersion variable
html = html.replace("let currentVersion = 'v3';", "let currentVersion = 'v4';")
html = html.replace("setCQVVersion('v3');", "setCQVVersion('v4');")

# 3. Update setCQVVersion function logic to support v4
old_cqv_assign = '''if (version === 'v1') {
                    c.cqv = (c.cqv_v1 !== undefined && c.cqv_v1 !== null) ? c.cqv_v1 : c.cqv;
                } else if (version === 'v1_1') {
                    c.cqv = (c.cqv_v1_1 !== undefined && c.cqv_v1_1 !== null) ? c.cqv_v1_1 : (c.cqv_v1 || c.cqv);
                } else if (version === 'v2') {
                    c.cqv = (c.cqv_v2 !== undefined && c.cqv_v2 !== null) ? c.cqv_v2 : c.cqv;
                } else {
                    c.cqv = (c.cqv_v3 !== undefined && c.cqv_v3 !== null) ? c.cqv_v3 : (c.cqv_v2 || c.cqv);
                }'''

new_cqv_assign = '''if (version === 'v1') {
                    c.cqv = (c.cqv_v1 !== undefined && c.cqv_v1 !== null) ? c.cqv_v1 : c.cqv;
                } else if (version === 'v1_1') {
                    c.cqv = (c.cqv_v1_1 !== undefined && c.cqv_v1_1 !== null) ? c.cqv_v1_1 : (c.cqv_v1 || c.cqv);
                } else if (version === 'v2') {
                    c.cqv = (c.cqv_v2 !== undefined && c.cqv_v2 !== null) ? c.cqv_v2 : c.cqv;
                } else if (version === 'v3') {
                    c.cqv = (c.cqv_v3 !== undefined && c.cqv_v3 !== null) ? c.cqv_v3 : (c.cqv_v2 || c.cqv);
                } else {
                    c.cqv = (c.cqv_v4 !== undefined && c.cqv_v4 !== null) ? c.cqv_v4 : (c.cqv_v3 || c.cqv);
                }'''

html = html.replace(old_cqv_assign, new_cqv_assign)

# 4. Update updateVersionUI is8F check
html = html.replace("const is8F = (currentVersion === 'v2' || currentVersion === 'v3');", "const is8F = (currentVersion === 'v2' || currentVersion === 'v3' || currentVersion === 'v4');")

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("PATCHED_DASHBOARD_SELECT_V4_DEFAULT_SUCCESSFULLY")
