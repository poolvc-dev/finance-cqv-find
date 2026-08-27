import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add safe fmt helper function definition in loadCompanyHistory if not present
    old_load = "function loadCompanyHistory() {"
    new_load = """function loadCompanyHistory() {
            const fmt = val => (val !== undefined && val !== null && Number.isFinite(Number(val))) ? Number(val).toFixed(2) : 'N/D';"""
    
    if old_load in content and "const fmt =" not in content:
        content = content.replace(old_load, new_load)

    # 2. Replace factor toFixed calls inside loadCompanyHistory
    content = content.replace("<td class=\"cqv-value-cell\">${data.f1.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${fmt(data?.f1)}</td>")
    content = content.replace("<td class=\"cqv-value-cell\">${data.f2.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${fmt(data?.f2)}</td>")
    content = content.replace("<td class=\"cqv-value-cell\">${data.f3.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${fmt(data?.f3)}</td>")
    content = content.replace("<td class=\"cqv-value-cell\">${company.f4.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${fmt(company?.f4)}</td>")
    content = content.replace("<td class=\"cqv-value-cell\">${company.f5.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${fmt(company?.f5)}</td>")
    content = content.replace("<td class=\"cqv-value-cell\">${company.f6.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${fmt(company?.f6)}</td>")
    content = content.replace("<td class=\"cqv-value-cell\">${company.f7.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${fmt(company?.f7)}</td>")
    content = content.replace("<td class=\"cqv-value-cell\">${company.f8.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${fmt(company?.f8)}</td>")
    content = content.replace("<td class=\"cqv-value-cell score-high\" style=\"font-weight: bold;\">${cqv_v2.toFixed(2)}</td>", "<td class=\"cqv-value-cell score-high\" style=\"font-weight: bold;\">${fmt(cqv_v2)}</td>")

    # 3. Replace populateHistoryCompanySelect toFixed call
    content = content.replace("opt.innerText = `${c.ticker} - ${c.name} (CQV: ${c.cqv.toFixed(2)})`;",
                              "const scoreVal = (currentVersion === 'v4' && c.cqv_v4 !== undefined && c.cqv_v4 !== null) ? c.cqv_v4 : ((currentVersion === 'v3' && c.cqv_v3 !== undefined && c.cqv_v3 !== null) ? c.cqv_v3 : c.cqv);\n                    const scoreText = Number.isFinite(Number(scoreVal)) ? Number(scoreVal).toFixed(2) : 'N/D';\n                    opt.innerText = `${c.ticker} - ${c.name} (CQV: ${scoreText})`;")

    # 4. Safe default selection in initDashboard
    old_init = "populateSimCompanySelect();\n            populateHistoryCompanySelect();"
    new_init = """populateSimCompanySelect();
            populateHistoryCompanySelect();

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

    if old_init in content:
        content = content.replace(old_init, new_init)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[OK] Fixed JS safety in {filepath}")

fix_file('generate_dashboard.py')
fix_file('dashboard.html')
