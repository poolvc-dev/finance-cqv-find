import re

with open("generate_dashboard.py", "r", encoding="utf-8") as f:
    code = f.read()

# Fix 1: populateHistoryCompanySelect
old_phcs = "opt.innerText = `${c.ticker} - ${c.name} (CQV: ${c.cqv.toFixed(2)})`;"
new_phcs = """const scoreVal = (currentVersion === 'v4' && c.cqv_v4 !== undefined && c.cqv_v4 !== null) ? c.cqv_v4 : ((currentVersion === 'v3' && c.cqv_v3 !== undefined && c.cqv_v3 !== null) ? c.cqv_v3 : c.cqv);
                    opt.innerText = `${c.ticker} - ${c.name} (CQV: ${formatDashboardScore(scoreVal)})`;"""

if old_phcs in code:
    code = code.replace(old_phcs, new_phcs)
    print("[OK] Fixed populateHistoryCompanySelect")

# Fix 2: getCompanyDetails fallback block
old_gcd = """            return {
                desc: `${company.name} (${company.ticker}) es una empresa cotizada en bolsa calificada con un Score CQV global de ${company.cqv.toFixed(2)}, posicionándose en la categoría de ${getTier(company.cqv).name}.`,
                f1_desc: `Calificación F1 de ${company.f1.toFixed(2)} sobre rentabilidad, márgenes operativos y conversión de flujo de caja libre.`,
                f2_desc: `Calificación F2 de ${company.f2.toFixed(2)} sobre la solidez de su balance y cobertura de intereses frente a la deuda.`,
                f3_desc: `Calificación F3 de ${company.f3.toFixed(2)} sobre su tasa de crecimiento orgánico auditada y control de la dilución al accionista por SBC.`,
                f4_desc: `Calificación F4 de ${company.f4.toFixed(2)} que refleja sus barreras de entrada competitivas (Moat) y retención del cliente.`,
                f5_desc: `Calificación F5 de ${company.f5.toFixed(2)} de opcionalidad tecnológica ante la revolución digital y resiliencia disruptiva.`,
                f6_desc: `Calificación F6 de ${company.f6 ? company.f6.toFixed(2) : '8.00'} sobre la asignación de capital operativo y dividendos de la directiva.`,
                f7_desc: `Calificación F7 de ${company.f7 ? company.f7.toFixed(2) : '8.00'} sobre el FCF Yield y la valoración del flujo de caja de la empresa.`,
                f8_desc: `Calificación F8 de ${company.f8 ? company.f8.toFixed(2) : '8.00'} sobre la resiliencia operativa y la diversificación de ingresos frente al riesgo de concentración.`
            };"""

new_gcd = """            const cqvVal = company ? company.cqv : null;
            return {
                desc: `${company ? company.name : ticker} (${company ? company.ticker : ticker}) es una empresa cotizada en bolsa calificada con un Score CQV global de ${formatDashboardScore(cqvVal)}, posicionándose en la categoría de ${getTier(cqvVal).name}.`,
                f1_desc: `Calificación F1 de ${formatDashboardScore(company?.f1)} sobre rentabilidad, márgenes operativos y conversión de flujo de caja libre.`,
                f2_desc: `Calificación F2 de ${formatDashboardScore(company?.f2)} sobre la solidez de su balance y cobertura de intereses frente a la deuda.`,
                f3_desc: `Calificación F3 de ${formatDashboardScore(company?.f3)} sobre su tasa de crecimiento orgánico auditada y control de la dilución al accionista por SBC.`,
                f4_desc: `Calificación F4 de ${formatDashboardScore(company?.f4)} que refleja sus barreras de entrada competitivas (Moat) y retención del cliente.`,
                f5_desc: `Calificación F5 de ${formatDashboardScore(company?.f5)} de opcionalidad tecnológica ante la revolución digital y resiliencia disruptiva.`,
                f6_desc: `Calificación F6 de ${formatDashboardScore(company?.f6)} sobre la asignación de capital operativo y dividendos de la directiva.`,
                f7_desc: `Calificación F7 de ${formatDashboardScore(company?.f7)} sobre el FCF Yield y la valoración del flujo de caja de la empresa.`,
                f8_desc: `Calificación F8 de ${formatDashboardScore(company?.f8)} sobre la resiliencia operativa y la diversificación de ingresos frente al riesgo de concentración.`
            };"""

if old_gcd in code:
    code = code.replace(old_gcd, new_gcd)
    print("[OK] Fixed getCompanyDetails")

# Fix 3: setCQVVersion default in initDashboard
old_init = """            // Set initial version
            setCQVVersion('v3');
            
            populateSimCompanySelect();
            populateHistoryCompanySelect();"""

new_init = """            // Set initial version
            setCQVVersion('v4');
            
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

if old_init in code:
    code = code.replace(old_init, new_init)
    print("[OK] Fixed initDashboard")

# Fix 4: setCQVVersion loop to include v4
old_version_loop = """                } else {
                    c.cqv = (c.cqv_v3 !== undefined && c.cqv_v3 !== null) ? c.cqv_v3 : (c.cqv_v2 || c.cqv);
                }"""

new_version_loop = """                } else {
                    c.cqv = (c.cqv_v4 !== undefined && c.cqv_v4 !== null) ? c.cqv_v4 : (c.cqv_v3 || c.cqv_v2 || c.cqv);
                }"""

if old_version_loop in code:
    code = code.replace(old_version_loop, new_version_loop)
    print("[OK] Fixed setCQVVersion loop")

# Fix 5: renderTable score cells
code = code.replace("<td class=\"cqv-value-cell\">${c.f1.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(c.f1)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${c.f2.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(c.f2)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${c.f3.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(c.f3)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${c.f4.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(c.f4)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${c.f5.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(c.f5)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${c.f6.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(c.f6)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${c.f7.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(c.f7)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${c.f8.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(c.f8)}</td>")
code = code.replace("<td class=\"cqv-value-cell score-high\">${c.cqv.toFixed(2)}</td>", "<td class=\"cqv-value-cell score-high\">${formatDashboardScore(c.cqv)}</td>")
code = code.replace("<div class=\"top20-score-val\">${c.cqv.toFixed(2)}</div>", "<div class=\"top20-score-val\">${formatDashboardScore(c.cqv)}</div>")
code = code.replace("title=\"Año ${yr}: ${yrCqv.toFixed(2)}\"", "title=\"Año ${yr}: ${formatDashboardScore(yrCqv)}\"")
code = code.replace("title=\"Año 2026 (Act.): ${c.cqv.toFixed(2)}\"", "title=\"Año 2026 (Act.): ${formatDashboardScore(c.cqv)}\"")

# Fix 6: loadCompanyHistory factor table cells
code = code.replace("<td class=\"cqv-value-cell\">${data.f1.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(data?.f1)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${data.f2.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(data?.f2)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${data.f3.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(data?.f3)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${company.f4.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(company?.f4)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${company.f5.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(company?.f5)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${company.f6.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(company?.f6)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${company.f7.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(company?.f7)}</td>")
code = code.replace("<td class=\"cqv-value-cell\">${company.f8.toFixed(2)}</td>", "<td class=\"cqv-value-cell\">${formatDashboardScore(company?.f8)}</td>")
code = code.replace("<td class=\"cqv-value-cell score-high\" style=\"font-weight: bold;\">${cqv_v2.toFixed(2)}</td>", "<td class=\"cqv-value-cell score-high\" style=\"font-weight: bold;\">${formatDashboardScore(cqv_v2)}</td>")

# Add spanGaps: true to history charts
code = code.replace("borderColor: '#4f46e5',", "borderColor: '#4f46e5',\n                        spanGaps: true,")
code = code.replace("borderColor: '#10b981',", "borderColor: '#10b981',\n                            spanGaps: true,")

with open("generate_dashboard.py", "w", encoding="utf-8") as f:
    f.write(code)
print("[OK] Finished applying clean fixes to generate_dashboard.py")
