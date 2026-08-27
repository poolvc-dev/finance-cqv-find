
        // Check if data loaded correctly, fallback to fetch JSON if needed
        let companies = [];
        function formatDashboardScore(value) {
            return (value !== undefined && value !== null && Number.isFinite(Number(value))) ? Number(value).toFixed(2) : 'N/D';
        }

        // Data Helpers
        function getTier(score) {
            if (!Number.isFinite(Number(score))) return { name: 'N/D', class: 'tier-unknown' };
            if (score >= 9.0) return { name: 'ÉLITE', class: 'tier-elite' };
            if (score >= 8.5) return { name: 'SÓLIDA', class: 'tier-strong' };
            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };
            return { name: 'ESPECULATIVA', class: 'tier-speculative' };
        }

        // KPI Calculations
        function initKPIs() {
            document.getElementById('kpi-total-companies').innerText = companies.length;
            
            const totalCqv = companies.reduce((acc, c) => acc + c.cqv, 0);
            const avgCqv = totalCqv / companies.length;
            document.getElementById('kpi-avg-cqv').innerText = avgCqv.toFixed(2);
            
            const eliteCount = companies.filter(c => c.cqv >= 9.0).length;
            document.getElementById('kpi-elite-count').innerText = eliteCount;
            
            if (companies.length > 0) {
                const sorted = [...companies].sort((a, b) => b.cqv - a.cqv);
                document.getElementById('kpi-top-performer').innerText = `${sorted[0].ticker} (${sorted[0].cqv.toFixed(2)})`;
            }
            
            // Calculate distributions
            const total = companies.length;
            const elite = companies.filter(c => c.cqv >= 9.0).length;
            const strong = companies.filter(c => c.cqv >= 8.5 && c.cqv < 9.0).length;
            const medium = companies.filter(c => c.cqv >= 8.0 && c.cqv < 8.5).length;
            const weak = companies.filter(c => c.cqv < 8.0).length;
            
            document.getElementById('dist-count-elite').innerText = `${elite} emp. (${(elite/total*100).toFixed(0)}%)`;
            document.getElementById('dist-count-strong').innerText = `${strong} emp. (${(strong/total*100).toFixed(0)}%)`;
            document.getElementById('dist-count-medium').innerText = `${medium} emp. (${(medium/total*100).toFixed(0)}%)`;
            document.getElementById('dist-count-weak').innerText = `${weak} emp. (${(weak/total*100).toFixed(0)}%)`;
            
            document.getElementById('dist-bar-elite').style.width = `${(elite/total*100).toFixed(0)}%`;
            document.getElementById('dist-bar-strong').style.width = `${(strong/total*100).toFixed(0)}%`;
            document.getElementById('dist-bar-medium').style.width = `${(medium/total*100).toFixed(0)}%`;
            document.getElementById('dist-bar-weak').style.width = `${(weak/total*100).toFixed(0)}%`;
        }

        // Render Top 15 Bar Chart
        let topChart = null;
        let top20SectorChart = null;
        let top20PillarsChart = null;
        let top20ValuationChart = null;

        function renderTopChart() {
            if (typeof Chart === 'undefined') {
                console.warn("Chart.js is not loaded. Skipping chart rendering.");
                return;
            }
            
            if (!companies || companies.length === 0) return;
            
            // Sort companies descending by CQV score
            const top20 = [...companies].sort((a, b) => b.cqv - a.cqv).slice(0, 20);
            
            const labelColor = getChartLabelColor();
            const gridColor = getChartGridColor();
            
            // 1. Render Top 20 Bar Chart (Score CQV)
            const canvasTop = document.getElementById('topChart');
            if (canvasTop) {
                const ctx = canvasTop.getContext('2d');
                const labels = top20.map(c => c.ticker);
                const data = top20.map(c => c.cqv);
                
                if (topChart && typeof topChart.destroy === 'function') topChart.destroy();
                
                const gradient = ctx.createLinearGradient(0, 0, 0, 300);
                gradient.addColorStop(0, '#6366f1');
                gradient.addColorStop(1, '#a855f7');
                
                topChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Score CQV',
                            data: data,
                            backgroundColor: gradient,
                            borderColor: 'rgba(255,255,255,0.15)',
                            borderWidth: 1,
                            borderRadius: 6
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { display: false },
                            tooltip: {
                                backgroundColor: '#0f172a',
                                titleColor: '#f8fafc',
                                bodyColor: '#cbd5e1',
                                borderColor: '#334155',
                                borderWidth: 1,
                                padding: 12,
                                callbacks: {
                                    title: (items) => `${top20[items[0].dataIndex].ticker} - ${top20[items[0].dataIndex].name}`,
                                    label: (item) => `Score CQV: ${item.raw.toFixed(2)} / 10`
                                }
                            }
                        },
                        scales: {
                            x: {
                                grid: { display: false },
                                ticks: { color: labelColor, font: { family: 'Inter', size: 10, weight: '700' } }
                            },
                            y: {
                                min: 7, max: 10,
                                grid: { color: gridColor },
                                ticks: { color: labelColor, font: { family: 'Outfit', size: 11 } }
                            }
                        }
                    }
                });
            }

            // 2. Render Top 20 Sector Distribution Doughnut Chart
            const canvasSector = document.getElementById('top20SectorChart');
            if (canvasSector) {
                const ctx = canvasSector.getContext('2d');
                const sectorCounts = {};
                top20.forEach(c => {
                    const sec = c.sector || 'Otros';
                    sectorCounts[sec] = (sectorCounts[sec] || 0) + 1;
                });
                
                const sectorLabels = Object.keys(sectorCounts);
                const sectorData = Object.values(sectorCounts);
                const sectorColors = ['#6366f1', '#10b981', '#3b82f6', '#f59e0b', '#ec4899', '#8b5cf6', '#14b8a6'];
                
                if (top20SectorChart && typeof top20SectorChart.destroy === 'function') top20SectorChart.destroy();
                
                top20SectorChart = new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: sectorLabels,
                        datasets: [{
                            data: sectorData,
                            backgroundColor: sectorColors.slice(0, sectorLabels.length),
                            borderWidth: 2,
                            borderColor: gridColor
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                display: true,
                                position: 'right',
                                labels: { color: labelColor, font: { family: 'Inter', size: 10 } }
                            },
                            tooltip: {
                                callbacks: {
                                    label: (item) => `${item.label}: ${item.raw} empresas (${(item.raw/20*100).toFixed(0)}%)`
                                }
                            }
                        },
                        cutout: '60%'
                    }
                });
            }

            // 3. Render Top 20 Pillars Comparison Chart (F1 Rentabilidad, F2 Solidez, F4 Moat)
            const canvasPillars = document.getElementById('top20PillarsChart');
            if (canvasPillars) {
                const ctx = canvasPillars.getContext('2d');
                const labels = top20.map(c => c.ticker);
                const dataF1 = top20.map(c => c.f1 || 0);
                const dataF2 = top20.map(c => c.f2 || 0);
                const dataF4 = top20.map(c => c.f4 || 0);
                
                if (top20PillarsChart && typeof top20PillarsChart.destroy === 'function') top20PillarsChart.destroy();
                
                top20PillarsChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [
                            { label: 'F1 Rentabilidad', data: dataF1, backgroundColor: '#3b82f6', borderRadius: 4 },
                            { label: 'F2 Solidez', data: dataF2, backgroundColor: '#10b981', borderRadius: 4 },
                            { label: 'F4 Moat', data: dataF4, backgroundColor: '#8b5cf6', borderRadius: 4 }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                display: true,
                                position: 'top',
                                labels: { color: labelColor, font: { family: 'Inter', size: 11 } }
                            }
                        },
                        scales: {
                            x: {
                                grid: { display: false },
                                ticks: { color: labelColor, font: { family: 'Inter', size: 10 } }
                            },
                            y: {
                                min: 5, max: 10,
                                grid: { color: gridColor },
                                ticks: { color: labelColor, font: { family: 'Outfit', size: 11 } }
                            }
                        }
                    }
                });
            }

            // 4. Render Top 20 Valuation PER vs Quality Score Chart
            const canvasValuation = document.getElementById('top20ValuationChart');
            if (canvasValuation) {
                const ctx = canvasValuation.getContext('2d');
                const labels = top20.map(c => c.ticker);
                const dataCQV = top20.map(c => c.cqv || 0);
                const dataPER = top20.map(c => c.pe || 0);
                
                if (top20ValuationChart && typeof top20ValuationChart.destroy === 'function') top20ValuationChart.destroy();
                
                top20ValuationChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                type: 'line',
                                label: 'Score CQV (Eje Izq)',
                                data: dataCQV,
                                borderColor: '#10b981',
                            spanGaps: true,
                                backgroundColor: '#10b981',
                                borderWidth: 3,
                                pointRadius: 4,
                                yAxisID: 'y'
                            },
                            {
                                type: 'bar',
                                label: 'PER Trailing (Eje Der)',
                                data: dataPER,
                                backgroundColor: 'rgba(59, 130, 246, 0.65)',
                                borderRadius: 4,
                                yAxisID: 'y1'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                display: true,
                                position: 'top',
                                labels: { color: labelColor, font: { family: 'Inter', size: 11 } }
                            }
                        },
                        scales: {
                            x: {
                                grid: { display: false },
                                ticks: { color: labelColor, font: { family: 'Inter', size: 10 } }
                            },
                            y: {
                                type: 'linear',
                                display: true,
                                position: 'left',
                                min: 6, max: 10,
                                title: { display: true, text: 'Score CQV', color: labelColor, font: { size: 10 } },
                                grid: { color: gridColor },
                                ticks: { color: labelColor }
                            },
                            y1: {
                                type: 'linear',
                                display: true,
                                position: 'right',
                                min: 0,
                                title: { display: true, text: 'Múltiplo PER', color: labelColor, font: { size: 10 } },
                                grid: { drawOnChartArea: false },
                                ticks: { color: labelColor }
                            }
                        }
                    }
                });
            }

            // 5. Render Top 20 Cards Showcase Grid
            renderTop20Grid(top20);
        }

        function renderTop20Grid(top20) {
            const gridEl = document.getElementById('top20-grid');
            if (!gridEl) return;
            gridEl.innerHTML = '';
            
            top20.forEach((c, idx) => {
                const rank = idx + 1;
                const card = document.createElement('div');
                card.className = 'top20-card';
                card.onclick = () => {
                    switchTab('history');
                    var historySelect = document.getElementById('history-company-select');
                    if (historySelect) {
                        historySelect.value = c.ticker;
                        loadCompanyHistory();
                    }
                };
                
                const tierInfo = getTier(c.cqv);
                card.innerHTML = `
                    <div class="top20-rank-badge">#${rank}</div>
                    <div class="top20-header">
                        <div>
                            <div class="top20-ticker">${c.ticker}</div>
                            <div class="top20-name">${c.name}</div>
                        </div>
                    </div>
                    <div class="top20-score-row">
                        <div>
                            <div class="top20-score-label">Score CQV</div>
                            <span class="badge ${tierInfo.class}" style="font-size: 11px;">${tierInfo.name}</span>
                        </div>
                        <div class="top20-score-val">${formatDashboardScore(c.cqv)}</div>
                    </div>
                    <div class="top20-metrics-pills">
                        <div class="top20-pill">
                            <div class="top20-pill-lbl">F1 Rentab.</div>
                            <div class="top20-pill-val">${c.f1.toFixed(1)}</div>
                        </div>
                        <div class="top20-pill">
                            <div class="top20-pill-lbl">F2 Solidez</div>
                            <div class="top20-pill-val">${c.f2.toFixed(1)}</div>
                        </div>
                        <div class="top20-pill">
                            <div class="top20-pill-lbl">F4 Moat</div>
                            <div class="top20-pill-val">${c.f4.toFixed(1)}</div>
                        </div>
                        <div class="top20-pill">
                            <div class="top20-pill-lbl">PER Trailing</div>
                            <div class="top20-pill-val">${c.pe ? c.pe.toFixed(1) + 'x' : '-'}</div>
                        </div>
                    </div>
                `;
                gridEl.appendChild(card);
            });
        }

        // Explorer Table Logic
        let filteredData = [];
        let currentSort = { column: 'cqv', direction: 'desc' };
        let currentPage = 1;
        let rowsPerPage = 50;

        function renderTable() {
            const tbody = document.getElementById('companies-table-body');
            if (!tbody) return;
            tbody.innerHTML = '';
            
            const start = (currentPage - 1) * rowsPerPage;
            const end = rowsPerPage === 'all' ? filteredData.length : start + parseInt(rowsPerPage);
            const pageData = rowsPerPage === 'all' ? filteredData : filteredData.slice(start, end);
            
            pageData.forEach(c => {
                const tier = getTier(c.cqv);
                const tr = document.createElement('tr');
                tr.style.cursor = 'pointer';
                tr.onclick = function() {
                    switchTab('history');
                    const selectEl = document.getElementById('history-company-select');
                    if (selectEl) {
                        selectEl.value = c.ticker;
                        loadCompanyHistory();
                    }
                };
                
                // Build sparkline HTML for 5-year CQV history (including current 2026)
                let sparklineHtml = '';
                const history = typeof cqvHistoryData !== 'undefined' ? cqvHistoryData[c.ticker] : null;
                if (history) {
                    const yrData = { ...history };
                    if (!yrData["2026"]) {
                        yrData["2026"] = { f1: c.f1, f2: c.f2, f3: c.f3, cqv: c.cqv };
                    }
                    const years = Object.keys(yrData).sort();
                    let bars = '';
                    years.forEach(yr => {
                        let yrCqv = yrData[yr].cqv;
                        if (currentVersion === 'v2') {
                            yrCqv = (yrData[yr].f1 * 0.20) + (yrData[yr].f2 * 0.10) + (yrData[yr].f3 * 0.10) + (c.f4 * 0.20) + (c.f5 * 0.10) + (c.f6 * 0.10) + (c.f7 * 0.10) + (c.f8 * 0.10);
                        }
                        const heightPct = (yrCqv / 10.0) * 100;
                        let barColor = 'var(--text-secondary)';
                        if (yrCqv >= 9.0) barColor = 'var(--elite)';
                        else if (yrCqv >= 8.5) barColor = 'var(--strong)';
                        else if (yrCqv >= 8.0) barColor = 'var(--medium)';
                        else barColor = 'var(--weak)';
                        
                        bars += `<div class="sparkline-bar" style="height: ${heightPct}%; background-color: ${barColor};" title="Año ${yr}: ${formatDashboardScore(yrCqv)}"></div>`;
                    });
                    sparklineHtml = `<div class="sparkline-container">${bars}</div>`;
                } else {
                    // Fallback to show at least the current 2026 bar if no history database is available
                    const heightPct = (c.cqv / 10.0) * 100;
                    let barColor = 'var(--text-secondary)';
                    if (c.cqv >= 9.0) barColor = 'var(--elite)';
                    else if (c.cqv >= 8.5) barColor = 'var(--strong)';
                    else if (c.cqv >= 8.0) barColor = 'var(--medium)';
                    else barColor = 'var(--weak)';
                    
                    sparklineHtml = `
                        <div class="sparkline-container" style="justify-content: center;">
                            <div class="sparkline-bar" style="height: ${heightPct}%; background-color: ${barColor};" title="Año 2026 (Act.): ${formatDashboardScore(c.cqv)}"></div>
                        </div>
                    `;
                }

                // Calculate trend from 2025 to 2026
                let trendHtml = '';
                if (history && history["2025"]) {
                    let score2025 = history["2025"].cqv;
                    if (currentVersion === 'v2') {
                        score2025 = (history["2025"].f1 * 0.20) + (history["2025"].f2 * 0.10) + (history["2025"].f3 * 0.10) + (c.f4 * 0.20) + (c.f5 * 0.10) + (c.f6 * 0.10) + (c.f7 * 0.10) + (c.f8 * 0.10);
                    }
                    const score2026 = c.cqv;
                    const diff = score2026 - score2025;
                    
                    if (diff > 0.005) {
                        trendHtml = `<span style="color: var(--elite); font-weight: bold; font-size: 11px; display: inline-flex; align-items: center;" title="Mejorando vs 2025: +${diff.toFixed(2)}"><i class="fa-solid fa-arrow-trend-up"></i></span>`;
                    } else if (diff < -0.005) {
                        trendHtml = `<span style="color: var(--weak); font-weight: bold; font-size: 11px; display: inline-flex; align-items: center;" title="Empeorando vs 2025: ${diff.toFixed(2)}"><i class="fa-solid fa-arrow-trend-down"></i></span>`;
                    } else {
                        trendHtml = `<span style="color: var(--medium); font-weight: bold; font-size: 11px; display: inline-flex; align-items: center;" title="Sin cambios vs 2025"><i class="fa-solid fa-arrow-right"></i></span>`;
                    }
                } else {
                    trendHtml = `<span style="color: var(--text-secondary); opacity: 0.3; font-size: 11px;" title="Sin datos de 2025">-</span>`;
                }

                const sparklineCellHtml = `
                    <div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; width: 68px;">
                        ${sparklineHtml}
                        ${trendHtml}
                    </div>
                `;

                tr.innerHTML = `
                    <td><span class="ticker-badge">${c.ticker}</span></td>
                    <td><span class="company-name">${c.name}</span></td>
                    <td><span class="q-badge">${c.quarter || 'Q1 2026'}</span></td>
                    <td class="cqv-value-cell">${formatDashboardScore(c.f1)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(c.f2)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(c.f3)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(c.f4)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(c.f5)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(c.f6)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(c.f7)}</td>
                    <td class="cqv-value-cell">${formatDashboardScore(c.f8)}</td>
                    <td class="cqv-value-cell">${c.pe ? c.pe.toFixed(1) + 'x' : '-'}</td>
                    <td class="cqv-value-cell score-high">${formatDashboardScore(c.cqv)}</td>
                    <td>${sparklineCellHtml}</td>
                    <td><span class="tier-badge ${tier.class}">${tier.name}</span></td>
                `;
                tbody.appendChild(tr);
            });
            
            // Update labels
            const totalCount = filteredData.length;
            const showingStart = totalCount === 0 ? 0 : start + 1;
            const showingEnd = rowsPerPage === 'all' ? totalCount : Math.min(end, totalCount);
            document.getElementById('showing-entries-label').innerText = `Mostrando ${showingStart} - ${showingEnd} de ${totalCount} empresas`;
            
            renderPagination(totalCount);
        }

        function renderPagination(totalCount) {
            const wrapper = document.getElementById('pagination-wrapper');
            if (!wrapper) return;
            wrapper.innerHTML = '';
            
            if (rowsPerPage === 'all' || totalCount <= rowsPerPage) return;
            
            const totalPages = Math.ceil(totalCount / rowsPerPage);
            
            // Prev btn
            const prevBtn = document.createElement('button');
            prevBtn.className = 'page-btn';
            prevBtn.innerHTML = '<i class="fa-solid fa-chevron-left"></i>';
            prevBtn.disabled = currentPage === 1;
            prevBtn.onclick = () => { currentPage--; renderTable(); };
            wrapper.appendChild(prevBtn);
            
            // Page numbers
            const maxVisible = 5;
            let startPage = Math.max(1, currentPage - 2);
            let endPage = Math.min(totalPages, startPage + maxVisible - 1);
            if (endPage - startPage < maxVisible - 1) {
                startPage = Math.max(1, endPage - maxVisible + 1);
            }
            
            for (let i = startPage; i <= endPage; i++) {
                const pageBtn = document.createElement('button');
                pageBtn.className = `page-btn ${i === currentPage ? 'active' : ''}`;
                pageBtn.innerText = i;
                pageBtn.onclick = () => { currentPage = i; renderTable(); };
                wrapper.appendChild(pageBtn);
            }
            
            // Next btn
            const nextBtn = document.createElement('button');
            nextBtn.className = 'page-btn';
            nextBtn.innerHTML = '<i class="fa-solid fa-chevron-right"></i>';
            nextBtn.disabled = currentPage === totalPages;
            nextBtn.onclick = () => { currentPage++; renderTable(); };
            wrapper.appendChild(nextBtn);
        }

        function handleSearch() {
            const query = document.getElementById('search-bar').value.toLowerCase().trim();
            applyFilters(query, document.getElementById('tier-filter').value);
        }

        function handleFilter() {
            const tier = document.getElementById('tier-filter').value;
            const query = document.getElementById('search-bar').value.toLowerCase().trim();
            applyFilters(query, tier);
        }

        function applyFilters(query, tier) {
            filteredData = companies.filter(c => {
                const matchesQuery = c.ticker.toLowerCase().includes(query) || c.name.toLowerCase().includes(query);
                
                let matchesTier = true;
                if (tier === 'elite') matchesTier = c.cqv >= 9.0;
                else if (tier === 'strong') matchesTier = c.cqv >= 8.5 && c.cqv < 9.0;
                else if (tier === 'medium') matchesTier = c.cqv >= 8.0 && c.cqv < 8.5;
                else if (tier === 'speculative') matchesTier = c.cqv < 8.0;
                
                return matchesQuery && matchesTier;
            });
            
            currentPage = 1;
            sortData();
            renderTable();
        }

        function handleRowsChange() {
            rowsPerPage = document.getElementById('rows-filter').value;
            currentPage = 1;
            renderTable();
        }

        function handleSort(column) {
            if (currentSort.column === column) {
                currentSort.direction = currentSort.direction === 'asc' ? 'desc' : 'asc';
            } else {
                currentSort.column = column;
                currentSort.direction = 'desc'; // default high to low
            }
            
            // Update UI headers indicators
            const colIndices = { 'ticker': 0, 'name': 1, 'quarter': 2, 'f1': 3, 'f2': 4, 'f3': 5, 'f4': 6, 'f5': 7, 'f6': 8, 'f7': 9, 'f8': 10, 'pe': 11, 'cqv': 12 };
            
            for (let key in colIndices) {
                const icon = document.getElementById('sort-icon-' + key);
                if (icon) {
                    if (key === column) {
                        icon.innerHTML = currentSort.direction === 'asc' ? '<i class="fa-solid fa-sort-up"></i>' : '<i class="fa-solid fa-sort-down"></i>';
                    } else {
                        icon.innerHTML = '<i class="fa-solid fa-sort"></i>';
                    }
                }
            }
            
            sortData();
            renderTable();
        }

        function sortData() {
            const col = currentSort.column;
            const dir = currentSort.direction === 'asc' ? 1 : -1;
            
            filteredData.sort((a, b) => {
                let valA = a[col];
                let valB = b[col];
                
                if (typeof valA === 'string') {
                    return valA.localeCompare(valB) * dir;
                }
                return (valA - valB) * dir;
            });
        }

        // Simulator Logic
        let simChart = null;
        function runSimulation() {
            const f1 = parseFloat(document.getElementById('slide-f1').value);
            const f2 = parseFloat(document.getElementById('slide-f2').value);
            const f3 = parseFloat(document.getElementById('slide-f3').value);
            const f4 = parseFloat(document.getElementById('slide-f4').value);
            const f5 = parseFloat(document.getElementById('slide-f5').value);
            const f6 = parseFloat(document.getElementById('slide-f6').value);
            const f7 = parseFloat(document.getElementById('slide-f7').value);
            const f8 = parseFloat(document.getElementById('slide-f8').value);
            
            // Update labels
            document.getElementById('val-f1').innerText = f1.toFixed(1);
            document.getElementById('val-f2').innerText = f2.toFixed(1);
            document.getElementById('val-f3').innerText = f3.toFixed(1);
            document.getElementById('val-f4').innerText = f4.toFixed(1);
            document.getElementById('val-f5').innerText = f5.toFixed(1);
            document.getElementById('val-f6').innerText = f6.toFixed(1);
            document.getElementById('val-f7').innerText = f7.toFixed(1);
            document.getElementById('val-f8').innerText = f8.toFixed(1);
            
            // Equation weights based on version
            let cqv = 0;
            if (currentVersion === 'v1') {
                cqv = (f1 * 0.25) + (f2 * 0.15) + (f3 * 0.15) + (f4 * 0.25) + (f5 * 0.20);
            } else {
                cqv = (f1 * 0.20) + (f2 * 0.10) + (f3 * 0.10) + (f4 * 0.20) + (f5 * 0.10) + (f6 * 0.10) + (f7 * 0.10) + (f8 * 0.10);
            }
            
            // Update display
            const display = document.getElementById('sim-cqv-score');
            display.innerText = cqv.toFixed(2);
            
            const tier = getTier(cqv);
            const tierBadge = document.getElementById('sim-tier-badge');
            tierBadge.innerText = tier.name;
            tierBadge.className = `tier-badge ${tier.class}`;
            
            const simData = [f1, f2, f3, f4, f5, f6, f7, f8];
            updateSimChart(simData, window.originalSimData);
        }

        function updateSimChart(data, originalBenchmark) {
            if (typeof Chart === 'undefined') {
                console.warn("Chart.js is not loaded. Skipping radar chart update.");
                return;
            }
            const canvasEl = document.getElementById('simChart');
            if (!canvasEl) return;
            const ctx = canvasEl.getContext('2d');
            
            if (simChart) {
                simChart.destroy();
            }
            
            const simDataFinal = (currentVersion === 'v2') ? data : data.slice(0, 5);
            const datasets = [{
                label: 'Valores Simulados',
                data: simDataFinal,
                backgroundColor: 'rgba(6, 182, 212, 0.2)',
                borderColor: '#06b6d4',
                borderWidth: 2,
                pointBackgroundColor: '#06b6d4',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: '#06b6d4'
            }];
            
            if (originalBenchmark) {
                const benchmarkDataFinal = (currentVersion === 'v2') ? originalBenchmark.data : originalBenchmark.data.slice(0, 5);
                datasets.push({
                    label: `Original: ${originalBenchmark.ticker}`,
                    data: benchmarkDataFinal,
                    backgroundColor: 'rgba(217, 70, 239, 0.05)',
                    borderColor: 'rgba(217, 70, 239, 0.6)',
                    borderWidth: 1.5,
                    borderDash: [5, 5],
                    pointBackgroundColor: '#d946ef',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: '#d946ef'
                });
            }
            
            simChart = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: (currentVersion === 'v2') ?
                        ['F1 (Rent.)', 'F2 (Solidez)', 'F3 (Crec.)', 'F4 (Moat)', 'F5 (Proj.)', 'F6 (Asig.)', 'F7 (Yield)', 'F8 (Antif.)'] :
                        ['F1 (Rent.)', 'F2 (Solidez)', 'F3 (Crec.)', 'F4 (Moat)', 'F5 (Proj.)'],
                    datasets: datasets
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: originalBenchmark ? true : false,
                            labels: {
                                color: '#94a3b8',
                                font: { family: 'Inter', size: 10 }
                            }
                        }
                    },
                    scales: {
                        r: {
                            min: 0,
                            max: 10,
                            ticks: {
                                stepSize: 2,
                                display: false
                            },
                            grid: {
                                color: getChartGridColor()
                            },
                            angleLines: {
                                color: getChartGridColor()
                            },
                            pointLabels: {
                                color: getChartLabelColor(),
                                font: {
                                    family: 'Outfit',
                                    size: 11
                                }
                            }
                        }
                    }
                }
            });
        }

        // Initialize script logic
        function bootDashboard() {
            const hasGlobalData = (typeof window.cqvData !== 'undefined' && window.cqvData.length > 0) || (typeof window.companiesData !== 'undefined' && window.companiesData.length > 0) || (typeof companiesData !== 'undefined' && companiesData.length > 0);
            if (hasGlobalData) {
                initDashboard();
            } else {
                fetch('cqv_data.json')
                    .then(r => r.json())
                    .then(data => {
                        window.companiesData = data;
                        initDashboard();
                    })
                    .catch(err => {
                        console.warn("CORS block or missing file during fetch, falling back to window.companiesData if available", err);
                        if (window.companiesData) {
                            initDashboard();
                        }
                    });
            }
        }

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', bootDashboard);
        } else {
            bootDashboard();
        }
        window.addEventListener('load', bootDashboard);
    