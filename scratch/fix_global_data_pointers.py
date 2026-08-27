with open("sync_cqv.py", "r", encoding="utf-8") as f:
    sync_code = f.read()

pos1 = sync_code.find("def sync_dashboard(data, history):")
pos2 = sync_code.find("def main():")

new_sync_func = """def sync_dashboard(data, history):
    with open("dashboard.html", encoding="utf-8") as handle:
        html = handle.read()

    data_text = json.dumps(data, indent=2, ensure_ascii=False)
    history_text = json.dumps(history, indent=2, ensure_ascii=False)

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
    sync_code = sync_code[:pos1] + new_sync_func + sync_code[pos2:]

with open("sync_cqv.py", "w", encoding="utf-8") as f:
    f.write(sync_code)
print("[OK] Updated sync_cqv.py sync_dashboard function")

def fix_data_lookup(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    code = code.replace(
        "companies = window.companiesData || (typeof companiesData !== 'undefined' ? companiesData : []);",
        "companies = (typeof window.cqvData !== 'undefined' && window.cqvData.length > 0) ? window.cqvData : (window.companiesData || (typeof companiesData !== 'undefined' ? companiesData : []));"
    )

    code = code.replace(
        "const hasGlobalData = (typeof window.companiesData !== 'undefined' && window.companiesData.length > 0) || (typeof companiesData !== 'undefined' && companiesData.length > 0);",
        "const hasGlobalData = (typeof window.cqvData !== 'undefined' && window.cqvData.length > 0) || (typeof window.companiesData !== 'undefined' && window.companiesData.length > 0) || (typeof companiesData !== 'undefined' && companiesData.length > 0);"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"[OK] Updated data lookup in {filepath}")

fix_data_lookup("generate_dashboard.py")
fix_data_lookup("dashboard.html")
