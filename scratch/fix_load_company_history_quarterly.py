import re

def update_history_logic(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    # 1. Ensure getTier is defined properly
    old_get_tier = r'// Data Helpers\s*;?\s*if \(score >= 8\.5\)'
    new_get_tier = """// Data Helpers
        function getTier(score) {
            if (!Number.isFinite(Number(score))) return { name: 'N/D', class: 'tier-unknown' };
            if (score >= 9.0) return { name: 'ÉLITE', class: 'tier-elite' };
            if (score >= 8.5) return { name: 'SÓLIDA', class: 'tier-strong' };
            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };
            return { name: 'ESPECULATIVA', class: 'tier-speculative' };
        }"""
    code = re.sub(r'function getTier\(score\) \{[\s\S]*?\}', '', code)
    code = re.sub(old_get_tier, new_get_tier, code)

    # 2. Update loadCompanyHistory
    old_lch = r'function loadCompanyHistory\(\) \{[\s\S]*?function renderHistoryChart'
    new_lch = """function loadCompanyHistory() {
            const ticker = document.getElementById('history-company-select').value;
            const tbody = document.getElementById('history-details-body');
            const profileCard = document.getElementById('history-profile-card');
            const profileDesc = document.getElementById('history-profile-desc');
            const profileFactors = document.getElementById('history-profile-factors');
            
            if (!tbody) return;
            tbody.innerHTML = '';
            
            if (!ticker) {
                if (historyChart) {
                    historyChart.destroy();
                    historyChart = null;
                }
                tbody.innerHTML = '<tr><td colspan="11" style="text-align: center; color: var(--text-secondary); padding: 30px 10px;">Selecciona una empresa para ver su evolución.</td></tr>';
                loadCompanyNotes('');
                if (profileCard) profileCard.style.display = 'none';
                return;
            }
            
            const company = companies.find(c => c.ticker === ticker);
            if (!company) return;
            
            if (profileCard && profileDesc && profileFactors) {
                const details = getCompanyDetails(ticker, company);
                profileDesc.innerText = details.desc;
                
                profileFactors.innerHTML = `
                    <li><strong style="color: #3b82f6;"><i class="fa-solid fa-wallet"></i> F1 (Rentabilidad):</strong> ${details.f1_desc}</li>
                    <li><strong style="color: #a855f7;"><i class="fa-solid fa-lock"></i> F2 (Solidez):</strong> ${details.f2_desc}</li>
                    <li><strong style="color: #10b981;"><i class="fa-solid fa-arrow-trend-up"></i> F3 (Crecimiento):</strong> ${details.f3_desc}</li>
                    <li><strong style="color: #f59e0b;"><i class="fa-solid fa-shield-halved"></i> F4 (Moat):</strong> ${details.f4_desc}</li>
                    <li><strong style="color: #d946ef;"><i class="fa-solid fa-rocket"></i> F5 (Proyección):</strong> ${details.f5_desc}</li>
                    <li class="v2-only"><strong style="color: #6366f1;"><i class="fa-solid fa-hand-holding-dollar"></i> F6 (Asignación):</strong> ${details.f6_desc}</li>
                    <li class="v2-only"><strong style="color: #06b6d4;"><i class="fa-solid fa-money-bill-trend-up"></i> F7 (FCF Yield):</strong> ${details.f7_desc}</li>
                    <li class="v2-only"><strong style="color: #ec4899;"><i class="fa-solid fa-triangle-exclamation"></i> F8 (Antifragilidad):</strong> ${details.f8_desc}</li>
                `;
                profileCard.style.display = 'block';
            }
            
            const historyObj = window.cqvHistoryData || (typeof cqvHistoryData !== 'undefined' ? cqvHistoryData : (window.cqvHistory || {}));
            const rawHistory = historyObj[ticker] || {};
            const keys = Object.keys(rawHistory).sort((a, b) => a.localeCompare(b));
            
            const chartLabels = [];
            const chartData = [];
            const priceData = [];
            const peData = [];
            let peSum = 0;
            let peCount = 0;
            
            keys.forEach(k => {
                const data = rawHistory[k];
                if (!data) return;
                
                const label = k.replace('_', ' ');
                chartLabels.push(label);
                
                let score = data.cqv_v4 || data.cqv_v3 || data.cqv_v2 || data.cqv_v1 || data.cqv;
                if (!Number.isFinite(Number(score)) && data.f1 !== undefined && data.f1 !== null) {
                    score = (
                        Number(data.f1) * 0.20 +
                        Number(data.f2) * 0.10 +
                        Number(data.f3) * 0.10 +
                        Number(company.f4 || 8.0) * 0.20 +
                        Number(company.f5 || 8.0) * 0.10 +
                        Number(company.f6 || 8.0) * 0.10 +
                        Number(company.f7 || 8.0) * 0.10 +
                        Number(company.f8 || 8.0) * 0.10
                    );
                }
                chartData.push(Number.isFinite(Number(score)) ? Number(score) : null);
                
                const priceVal = (data.price !== undefined && data.price !== null) ? Number(data.price) : ((company.close_history && company.close_history[k]) ? Number(company.close_history[k]) : null);
                priceData.push(priceVal);
                
                const peVal = (data.pe !== undefined && data.pe !== null) ? Number(data.pe) : null;
                peData.push(peVal);
                if (peVal !== null && Number.isFinite(peVal)) {
                    peSum += peVal;
                    peCount++;
                }
                
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><span style="font-weight: bold; color: var(--text-primary);">${label}</span></td>
                    <td class="cqv-value-cell">${formatDashboardScore(data.f1)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(data.f2)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(data.f3)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(company.f4)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(company.f5)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(company.f6)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(company.f7)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(company.f8)}</td>
                    <td class="cqv-value-cell">${peVal ? peVal.toFixed(1) + 'x' : '-'}</td>
                    <td class="cqv-value-cell score-high" style="font-weight: bold;">${formatDashboardScore(score)}</td>
                `;
                tbody.appendChild(tr);
            });
            
            const avgPe = peCount > 0 ? (peSum / peCount) : null;
            
            renderHistoryChart(chartLabels, chartData, company.name);
            renderPEValuationChart(chartLabels, priceData, peData, avgPe, company.name);
            loadCompanyNotes(ticker);
        }

        function renderHistoryChart"""

    code = re.sub(old_lch, new_lch, code)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"[OK] Updated {filepath} for quarterly history support")

update_history_logic("generate_dashboard.py")
update_history_logic("dashboard.html")
