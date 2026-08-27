import re

# 1. Update generate_dashboard.py
with open('generate_dashboard.py', 'r', encoding='utf-8') as f:
    gd_content = f.read()

# Fix populateHistoryCompanySelect in generate_dashboard.py
old_populate_history = """        function populateHistoryCompanySelect() {
            const selectEl = document.getElementById('history-company-select');
            if (!selectEl) return;
            selectEl.innerHTML = '<option value="">-- Seleccionar una empresa --</option>';
            const sortedCompanies = [...companies].sort((a, b) => a.ticker.localeCompare(b.ticker));
            const historyObj = window.cqvHistoryData || (typeof cqvHistoryData !== 'undefined' ? cqvHistoryData : null);
            sortedCompanies.forEach(c => {
                if (!historyObj || historyObj[c.ticker]) {
                    const opt = document.createElement('option');
                    opt.value = c.ticker;
                    opt.innerText = `${c.ticker} - ${c.name} (CQV: ${c.cqv.toFixed(2)})`;
                    selectEl.appendChild(opt);
                }
            });
        }"""

new_populate_history = """        function populateHistoryCompanySelect() {
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
                    const scoreText = Number.isFinite(Number(scoreVal)) ? Number(scoreVal).toFixed(2) : 'N/D';
                    opt.innerText = `${c.ticker} - ${c.name} (CQV: ${scoreText})`;
                    selectEl.appendChild(opt);
                }
            });
        }"""

if old_populate_history in gd_content:
    gd_content = gd_content.replace(old_populate_history, new_populate_history)
    print("[OK] Replaced populateHistoryCompanySelect in generate_dashboard.py")
else:
    print("[WARN] Could not find exact old_populate_history block in generate_dashboard.py, applying regex replacement")
    gd_content = re.sub(
        r'opt\.innerText = `\${c\.ticker} - \${c\.name} \(CQV: \${c\.cqv\.toFixed\(2\)}\)`;',
        r'''const scoreVal = (currentVersion === 'v4' && c.cqv_v4 !== undefined && c.cqv_v4 !== null) ? c.cqv_v4 : ((currentVersion === 'v3' && c.cqv_v3 !== undefined && c.cqv_v3 !== null) ? c.cqv_v3 : c.cqv);
                    const scoreText = Number.isFinite(Number(scoreVal)) ? Number(scoreVal).toFixed(2) : 'N/D';
                    opt.innerText = `${c.ticker} - ${c.name} (CQV: ${scoreText})`;''',
        gd_content
    )

# Fix initDashboard in generate_dashboard.py to set default history selection
old_init_dash = """      populateSimCompanySelect();
      populateHistoryCompanySelect();
    }"""

new_init_dash = """      populateSimCompanySelect();
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
      }
    }"""

if old_init_dash in gd_content:
    gd_content = gd_content.replace(old_init_dash, new_init_dash)

# Add spanGaps: true to history charts in generate_dashboard.py
gd_content = gd_content.replace("borderColor: '#4f46e5',", "borderColor: '#4f46e5',\n            spanGaps: true,")
gd_content = gd_content.replace("borderColor: '#10b981',", "borderColor: '#10b981',\n              spanGaps: true,")

with open('generate_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(gd_content)

print("[OK] Updated generate_dashboard.py")
