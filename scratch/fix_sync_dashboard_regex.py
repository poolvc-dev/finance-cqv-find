with open("sync_cqv.py", "r", encoding="utf-8") as f:
    code = f.read()

pos1 = code.find("def sync_dashboard(data, history):")
pos2 = code.find("def main():")

new_sync_func = """def sync_dashboard(data, history):
    with open("dashboard.html", encoding="utf-8") as handle:
        html = handle.read()

    data_text = json.dumps(data, indent=2, ensure_ascii=False)
    history_text = json.dumps(history, indent=2, ensure_ascii=False)

    injection = f\"\"\"<!-- DATA_INJECTION_START -->
    <script>
        window.companiesData = {data_text};
        window.cqvHistoryData = {history_text};
        window.cqvHistory = window.cqvHistoryData;
    </script>
    <!-- DATA_INJECTION_END -->\"\"\"

    pattern = r"<!-- DATA_INJECTION_START -->[\\s\\S]*?<!-- DATA_INJECTION_END -->"
    if not re.search(pattern, html):
        raise ValueError("<!-- DATA_INJECTION_START --> block not found in dashboard.html")

    html = re.sub(pattern, lambda m: injection, html, count=1)

    with open("dashboard.html", "w", encoding="utf-8") as handle:
        handle.write(html)

"""

if pos1 != -1 and pos2 != -1:
    code = code[:pos1] + new_sync_func + code[pos2:]

with open("sync_cqv.py", "w", encoding="utf-8") as f:
    f.write(code)

print("[OK] Updated sync_cqv.py sync_dashboard function successfully.")
