import re

# 1. Update sync_cqv.py
with open("sync_cqv.py", "r", encoding="utf-8") as f:
    code = f.read()

pos1 = code.find("def sync_dashboard(data, history):")
pos2 = code.find("def main():")

new_sync_func = """def sync_dashboard(data, history):
    with open("dashboard.html", encoding="utf-8") as handle:
        html = handle.read()

    data_text = json.dumps(data, indent=2, ensure_ascii=False).replace("</script>", "<\\\\/script>")
    history_text = json.dumps(history, indent=2, ensure_ascii=False).replace("</script>", "<\\\\/script>")

    injection = f\"\"\"<!-- DATA_INJECTION_START -->
    <script>
        window.cqvData = {data_text};
        window.companiesData = window.cqvData;
        window.cqvHistoryData = {history_text};
        window.cqvHistory = window.cqvHistoryData;
    </script>
    <!-- DATA_INJECTION_END -->\"\"\"

    pattern = r"<!-- DATA_INJECTION_START -->[\\s\\S]*?<!-- DATA_INJECTION_END -->"
    if re.search(pattern, html):
        html = re.sub(pattern, lambda m: injection, html, count=1)

    with open("dashboard.html", "w", encoding="utf-8") as handle:
        handle.write(html)

"""

if pos1 != -1 and pos2 != -1:
    code = code[:pos1] + new_sync_func + code[pos2:]

with open("sync_cqv.py", "w", encoding="utf-8") as f:
    f.write(code)
print("[OK] Escaped script tags in sync_cqv.py")

# 2. Update generate_dashboard.py
with open("generate_dashboard.py", "r", encoding="utf-8") as f:
    gd_code = f.read()

gd_code = gd_code.replace(
    "window.cqvHistoryData = {json.dumps(history_db, indent=2)};",
    "window.cqvHistoryData = {json.dumps(history_db, indent=2).replace('</script>', '<\\\\/script>')};"
)

with open("generate_dashboard.py", "w", encoding="utf-8") as f:
    f.write(gd_code)
print("[OK] Escaped script tags in generate_dashboard.py")
