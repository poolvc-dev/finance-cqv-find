import re

def clean_duplicate_history_select(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    
    dup_block = """            const historySelect = document.getElementById('history-company-select');
            if (historySelect && (!historySelect.value || historySelect.value === '')) {
                const sortedComp = [...companies].filter(c => Number.isFinite(Number(c.cqv))).sort((a, b) => b.cqv - a.cqv);
                if (sortedComp.length > 0) {
                    historySelect.value = sortedComp[0].ticker;
                    loadCompanyHistory();
                } else if (companies.length > 0) {
                    historySelect.value = companies[0].ticker;
                    loadCompanyHistory();
                }
            }

            const historySelect = document.getElementById('history-company-select');
            if (historySelect && (!historySelect.value || historySelect.value === '')) {
                const sortedComp = [...companies].filter(c => Number.isFinite(Number(c.cqv))).sort((a, b) => b.cqv - a.cqv);
                if (sortedComp.length > 0) {
                    historySelect.value = sortedComp[0].ticker;
                    loadCompanyHistory();
                } else if (companies.length > 0) {
                    historySelect.value = companies[0].ticker;
                    loadCompanyHistory();
                }
            }"""

    single_block = """            const historySelect = document.getElementById('history-company-select');
            if (historySelect && (!historySelect.value || historySelect.value === '')) {
                const sortedComp = [...companies].filter(c => Number.isFinite(Number(c.cqv))).sort((a, b) => b.cqv - a.cqv);
                if (sortedComp.length > 0) {
                    historySelect.value = sortedComp[0].ticker;
                    loadCompanyHistory();
                } else if (companies.length > 0) {
                    historySelect.value = companies[0].ticker;
                    loadCompanyHistory();
                }
            }"""

    if dup_block in code:
        code = code.replace(dup_block, single_block)
        print(f"[OK] Cleaned duplicate block in {file_path}")
    else:
        # Fallback regex if formatting differs slightly
        code = re.sub(
            r"(const historySelect = document\.getElementById\('history-company-select'\);[\s\S]*?loadCompanyHistory\(\);\s*\}\s*\}\s*)\s*const historySelect = document\.getElementById\('history-company-select'\);[\s\S]*?loadCompanyHistory\(\);\s*\}\s*\}",
            r"\1",
            code
        )
        print(f"[OK] Applied regex cleanup in {file_path}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)

clean_duplicate_history_select("generate_dashboard.py")
clean_duplicate_history_select("dashboard.html")
