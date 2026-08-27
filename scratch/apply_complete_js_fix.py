import re

def fix_code(code_str):
    # 1. Define top-level helpers at the start of script
    helpers = """
        function formatDashboardScore(value) {
            return (value !== undefined && value !== null && Number.isFinite(Number(value))) ? Number(value).toFixed(2) : 'N/D';
        }

        function getTier(score) {
            if (!Number.isFinite(Number(score))) return { name: 'N/D', class: 'tier-unknown' };
            if (score >= 9.0) return { name: 'ÉLITE', class: 'tier-elite' };
            if (score >= 8.5) return { name: 'SÓLIDA', class: 'tier-strong' };
            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };
            return { name: 'ESPECULATIVA', class: 'tier-speculative' };
        }
"""
    # Remove existing definitions if misplaced
    code_str = re.sub(r'function formatDashboardScore\(value\) \{[\s\S]*?\}', '', code_str)
    code_str = re.sub(r'function getTier\(score\) \{[\s\S]*?\}', '', code_str)

    # Insert helpers right after 'let companies = [];'
    code_str = code_str.replace("let companies = [];", "let companies = [];\n" + helpers)

    # 2. Fix getCompanyDetails
    old_gcd = r'function getCompanyDetails\(ticker, company\) \{[\s\S]*?return \{[\s\S]*?f8_desc:[\s\S]*?\};[\s\S]*?\}'
    new_gcd = """function getCompanyDetails(ticker, company) {
            if (companyDetailedData[ticker]) {
                return companyDetailedData[ticker];
            }
            const fmt = val => (val !== undefined && val !== null && Number.isFinite(Number(val))) ? Number(val).toFixed(2) : 'N/D';
            const cqvScoreStr = fmt(company ? company.cqv : null);
            const tierInfo = getTier(company ? company.cqv : null);
            return {
                desc: `${company ? company.name : ticker} (${company ? company.ticker : ticker}) es una empresa cotizada en bolsa calificada con un Score CQV global de ${cqvScoreStr}, posicionándose en la categoría de ${tierInfo.name}.`,
                f1_desc: `Calificación F1 de ${fmt(company ? company.f1 : null)} sobre rentabilidad, márgenes operativos y conversión de flujo de caja libre.`,
                f2_desc: `Calificación F2 de ${fmt(company ? company.f2 : null)} sobre la solidez de su balance y cobertura de intereses frente a la deuda.`,
                f3_desc: `Calificación F3 de ${fmt(company ? company.f3 : null)} sobre su tasa de crecimiento orgánico auditada y control de la dilución al accionista por SBC.`,
                f4_desc: `Calificación F4 de ${fmt(company ? company.f4 : null)} que refleja sus barreras de entrada competitivas (Moat) y retención del cliente.`,
                f5_desc: `Calificación F5 de ${fmt(company ? company.f5 : null)} de opcionalidad tecnológica ante la revolución digital y resiliencia disruptiva.`,
                f6_desc: `Calificación F6 de ${fmt(company ? company.f6 : null)} sobre la asignación de capital operativo y dividendos de la directiva.`,
                f7_desc: `Calificación F7 de ${fmt(company ? company.f7 : null)} sobre el FCF Yield y la valoración del flujo de caja de la empresa.`,
                f8_desc: `Calificación F8 de ${fmt(company ? company.f8 : null)} sobre la resiliencia operativa y la diversificación de ingresos frente al riesgo de concentración.`
            };
        }"""
    
    code_str = re.sub(old_gcd, new_gcd, code_str)

    # 3. Fix setCQVVersion to include v4
    old_version_loop = r'companies\.forEach\(c => \{[\s\S]*?\}\);'
    new_version_loop = """companies.forEach(c => {
                if (version === 'v1') {
                    c.cqv = (c.cqv_v1 !== undefined && c.cqv_v1 !== null) ? c.cqv_v1 : c.cqv;
                } else if (version === 'v1_1') {
                    c.cqv = (c.cqv_v1_1 !== undefined && c.cqv_v1_1 !== null) ? c.cqv_v1_1 : (c.cqv_v1 || c.cqv);
                } else if (version === 'v2') {
                    c.cqv = (c.cqv_v2 !== undefined && c.cqv_v2 !== null) ? c.cqv_v2 : c.cqv;
                } else if (version === 'v3') {
                    c.cqv = (c.cqv_v3 !== undefined && c.cqv_v3 !== null) ? c.cqv_v3 : (c.cqv_v2 || c.cqv);
                } else {
                    c.cqv = (c.cqv_v4 !== undefined && c.cqv_v4 !== null) ? c.cqv_v4 : (c.cqv_v3 || c.cqv_v2 || c.cqv);
                }
            });"""
    code_str = re.sub(old_version_loop, new_version_loop, code_str)

    # 4. Fix populateHistoryCompanySelect
    old_phcs = r'function populateHistoryCompanySelect\(\) \{[\s\S]*?\}\n'
    new_phcs = """function populateHistoryCompanySelect() {
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
        }\n"""
    code_str = re.sub(old_phcs, new_phcs, code_str)

    # 5. Fix loadCompanyHistory to avoid direct toFixed on factor properties
    old_lch_table = r'<td class="cqv-value-cell">\$\{data\.f1\.toFixed\(2\)\}</td>[\s\S]*?<td class="cqv-value-cell score-high" style="font-weight: bold;">\$\{cqv_v2\.toFixed\(2\)\}</td>'
    new_lch_table = """<td class="cqv-value-cell">${formatDashboardScore(data?.f1)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(data?.f2)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(data?.f3)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(company?.f4)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(company?.f5)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(company?.f6)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(company?.f7)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(company?.f8)}</td>
                    <td class="cqv-value-cell">${data?.pe ? Number(data.pe).toFixed(1) + 'x' : 'N/D'}</td>
                    <td class="cqv-value-cell score-high" style="font-weight: bold;">${formatDashboardScore(cqv_v2)}</td>"""
    code_str = re.sub(old_lch_table, new_lch_table, code_str)

    # 6. Ensure default selection when initDashboard finishes
    old_init = r'setCQVVersion\([^\)]+\);\s*populateSimCompanySelect\(\);\s*populateHistoryCompanySelect\(\);'
    new_init = """setCQVVersion('v4');
            populateSimCompanySelect();
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
    code_str = re.sub(old_init, new_init, code_str)

    return code_str

with open("generate_dashboard.py", "r", encoding="utf-8") as f:
    gd_code = f.read()

gd_fixed = fix_code(gd_code)

with open("generate_dashboard.py", "w", encoding="utf-8") as f:
    f.write(gd_fixed)
print("[OK] Applied complete JS fix to generate_dashboard.py")

with open("dashboard.html", "r", encoding="utf-8") as f:
    dh_code = f.read()

dh_fixed = fix_code(dh_code)

with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(dh_fixed)
print("[OK] Applied complete JS fix to dashboard.html")
