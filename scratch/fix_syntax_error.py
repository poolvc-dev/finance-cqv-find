import re

def fix_extra_braces(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    bad_block = """        function populateHistoryCompanySelect() {
            const selectEl = document.getElementById('history-company-select');
            if (!selectEl) return;
            selectEl.innerHTML = '<option value="">-- Seleccionar una empresa --</option>';
            const sortedCompanies = [...companies].sort((a, b) => a.ticker.localeCompare(b.ticker));
            const historyObj = (typeof cqvHistory !== 'undefined' ? cqvHistory : (window.cqvHistory || window.cqvHistoryData || {}));
            sortedCompanies.forEach(c => {
                if (!historyObj || historyObj[c.ticker]) {
                    const opt = document.createElement('option');
                    opt.value = c.ticker;
                    const scoreVal = (currentVersion === 'v4' && c.cqv_v4 !== undefined && c.cqv_v4 !== null) ? c.cqv_v4 : ((currentVersion === 'v3' && c.cqv_v3 !== undefined && c.cqv_v3 !== null) ? c.cqv_v3 : c.cqv);
                    const scoreText = formatDashboardScore(scoreVal);
                    opt.innerText = `${c.ticker} - ${c.name} (CQV: ${scoreText})`;
                    selectEl.appendChild(opt);
                }
            });
        }
            });
        }"""

    good_block = """        function populateHistoryCompanySelect() {
            const selectEl = document.getElementById('history-company-select');
            if (!selectEl) return;
            selectEl.innerHTML = '<option value="">-- Seleccionar una empresa --</option>';
            const sortedCompanies = [...companies].sort((a, b) => a.ticker.localeCompare(b.ticker));
            const historyObj = (typeof cqvHistory !== 'undefined' ? cqvHistory : (window.cqvHistory || window.cqvHistoryData || {}));
            sortedCompanies.forEach(c => {
                if (!historyObj || historyObj[c.ticker]) {
                    const opt = document.createElement('option');
                    opt.value = c.ticker;
                    const scoreVal = (currentVersion === 'v4' && c.cqv_v4 !== undefined && c.cqv_v4 !== null) ? c.cqv_v4 : ((currentVersion === 'v3' && c.cqv_v3 !== undefined && c.cqv_v3 !== null) ? c.cqv_v3 : c.cqv);
                    const scoreText = formatDashboardScore(scoreVal);
                    opt.innerText = `${c.ticker} - ${c.name} (CQV: ${scoreText})`;
                    selectEl.appendChild(opt);
                }
            });
        }"""

    if bad_block in code:
        code = code.replace(bad_block, good_block)
        print(f"[OK] Replaced extra braces block in {filepath}")
    else:
        code = re.sub(
            r'function populateHistoryCompanySelect\(\) \{[\s\S]*?\}\s*\}\);\s*\}',
            good_block,
            code
        )
        print(f"[OK] Applied regex fix in {filepath}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

fix_extra_braces("generate_dashboard.py")
fix_extra_braces("dashboard.html")
