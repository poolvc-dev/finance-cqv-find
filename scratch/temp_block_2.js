
        // Check if data loaded correctly, fallback to fetch JSON if needed
        let companies = [];

        const companyDetailedData = {
            "MA": {
                desc: "Mastercard Incorporated es una empresa tecnológica líder global en la industria de medios de pago, conectando a consumidores, instituciones financieras, comercios y gobiernos en más de 210 países.",
                f1_desc: "Margen EBITDA extraordinario superior al 58% y ROIC colosal. Alta conversión de beneficio contable a flujo de caja libre neto.",
                f2_desc: "Balance y solvencia excepcionales. Liquidez inmediata superior a 1.2x la deuda a corto plazo y cobertura de intereses sumamente holgada.",
                f3_desc: "Crecimiento eficiente impulsado por la transición global del dinero físico a transacciones digitales y transfronterizas sin requerir alta inversión de capital.",
                f4_desc: "Foso competitivo (Moat) casi impenetrable derivado de efectos de red globales bilaterales masivos y un duopolio de red de peaje de facto con Visa.",
                f5_desc: "Preeminencia en seguridad digital mediante IA aplicada a detección de fraudes y soluciones transfronterizas complejas, asegurando resiliencia frente a disrupción Fintech.",
                f6_desc: "Asignación de capital ultra-eficiente centrado en recompras masivas de acciones constantes y dividendos crecientes sustentados en flujos predecibles.",
                f7_desc: "FCF Yield estable de ~3.0%-3.5% que refleja una valoración premium pero justificada por su foso de duopolio.",
                f8_desc: "Diversificación total con miles de millones de tarjetas y comercios integrados en su red global."
            },
            "V": {
                desc: "Visa Inc. es la red de procesamiento de pagos electrónicos más grande del mundo, operando como un peaje de transacción global para consumidores, comercios e instituciones financieras.",
                f1_desc: "Margen operativo superior al 64%. Negocio asset-light con requerimientos mínimos de capital e inmensa conversión de efectivo.",
                f2_desc: "Apalancamiento mínimo con Deuda Neta/EBITDA muy por debajo de 1.0x, complementado por flujos de caja de alta predecibilidad anticíclica.",
                f3_desc: "Crecimiento constante impulsado por la digitalización del efectivo y la expansión de pagos sin contacto y transferencias P2P.",
                f4_desc: "Efecto red bilateral insuperable (comercios-consumidores) y foso de escala global regulado, operando de facto como un peaje indestructible.",
                f5_desc: "Opcionalidad en flujos transfronterizos complejos y APIs de seguridad financiera, inmune a la desintermediación por su escala y confianza institucional.",
                f6_desc: "Asignación de capital óptima. Recompra neta masiva y constante reducción de acciones en circulación sin deuda significativa.",
                f7_desc: "FCF Yield de ~3.0%-3.5%, consistente con un negocio de altísima calidad y baja intensidad de capital.",
                f8_desc: "Excelente diversificación de ingresos entre múltiples emisores y adquirentes a nivel mundial."
            },
            "AAPL": {
                desc: "Apple Inc. es la compañía de hardware de consumo y servicios más grande del mundo, destacando por su ecosistema cerrado que integra iPhone, iPad, Mac y una suite de servicios de alta fidelidad.",
                f1_desc: "Márgenes brutos estables del 45% y generación de caja operativa colosal. ROIC extraordinario (>50%) debido a su modelo de manufactura optimizado.",
                f2_desc: "Estructura de deuda conservadora orientada a neutralidad de caja neta, con alta predecibilidad del flujo libre de caja.",
                f3_desc: "Crecimiento a un dígito alto apoyado por servicios recurrentes que compensan la maduración de las ventas de hardware físico.",
                f4_desc: "Foso insuperable basado en costos de cambio extremos del ecosistema iOS/macOS y el valor de marca más fuerte del planeta.",
                f5_desc: "Fuerte opcionalidad en servicios financieros, salud y computación espacial (Vision Pro), con un ecosistema extremadamente resistente a la desintermediación por terceros.",
                f6_desc: "Asignación de capital agresiva y exitosa enfocada en recompras masivas (más de 90B anuales) y dividendos constantes.",
                f7_desc: "FCF Yield de ~3.0%-3.5%. Su flujo de caja colosal ofrece protección ante presiones macroeconómicas.",
                f8_desc: "Dependencia significativa de la manufactura en Asia (Foxconn), aunque cuenta con millones de consumidores diversificados en todo el mundo."
            },
            "ASML": {
                desc: "ASML Holding N.V. es el único fabricante en el mundo de máquinas de litografía ultravioleta extrema (EUV), indispensables para fabricar los semiconductores más avanzados de la actualidad.",
                f1_desc: "Rentabilidad extraordinaria con retornos de capital muy elevados (ROIC >30%) apoyados en su monopolio tecnológico.",
                f2_desc: "Balance impecable con caja neta y nulo riesgo crediticio debido a pagos por hitos adelantados de sus clientes.",
                f3_desc: "Crecimiento sólido impulsado por la demanda estructural de microchips de última generación y centros de datos de IA.",
                f4_desc: "Monopolio tecnológico e intelectual absoluto en litografía avanzada, con barreras de entrada físicas y científicas multimillonarias.",
                f5_desc: "Proveedor crítico insustituible para el futuro de la Inteligencia Artificial y la computación de alto rendimiento.",
                f6_desc: "Retornos elevados sobre capital incremental (ROCIC) gracias a la reinversión constante en I+D crítica y recompras oportunistas.",
                f7_desc: "FCF Yield bajo (~2.0%) debido a múltiplos de valoración exigentes que reflejan su monopolio tecnológico.",
                f8_desc: "Riesgo de concentración de clientes medio-alto (TSMC, Intel y Samsung representan la gran mayoría de sus ingresos de EUV)."
            },
            "AVGO": {
                desc: "Broadcom Inc. es un líder tecnológico global que diseña, desarrolla y suministra una amplia gama de soluciones de software de infraestructura y semiconductores analógicos y digitales.",
                f1_desc: "Margen operativo superior al 45% sostenido. Excelente generación de flujo de caja libre, con conversión superior al 110%.",
                f2_desc: "Apalancamiento manejable gracias a la rápida reducción de deuda utilizando los flujos de caja operativos tras la compra de VMware.",
                f3_desc: "Crecimiento impulsado por adquisiciones estratégicas masivas (M&A) e integración de software y silicio personalizado para centros de datos de IA.",
                f4_desc: "Moat fuerte basado en contratos de software empresarial a largo plazo y patentes críticas de conectividad de silicio para centros de datos.",
                f5_desc: "Papel fundamental en el despliegue de redes para clústeres de GPU para IA y chips propietarios personalizados (ASICs).",
                f6_desc: "Estrategia M&A agresiva pero disciplinada dirigida por Hock Tan, logrando desapalancamiento rápido tras adquisiciones (ej. VMware).",
                f7_desc: "FCF Yield atractivo (~4.0%) sustentado en su capacidad de ordeñar flujos recurrentes de software de infraestructura.",
                f8_desc: "Dependencia parcial de grandes proveedores de infraestructura cloud e hiperscalers en el área de silicio."
            },
            "GOOGL": {
                desc: "Alphabet Inc. (Google) es el líder indiscutible en búsquedas web, publicidad digital y sistemas operativos móviles (Android). Su modelo de negocio se basa en la monetización de la atención de los usuarios y el procesamiento masivo de datos mediante IA.",
                f1_desc: "Margen operativo superior al 27% sostenido. Elevado ROIC (>25%), aunque presionado por la intensidad de capital necesaria para la infraestructura de Inteligencia Artificial.",
                f2_desc: "Balance extremadamente sólido con caja neta de más de 100,000 millones de dólares y un ratio Deuda Neta/EBITDA negativo.",
                f3_desc: "Crecimiento histórico constante superior al 10%, sin embargo, el factor se ve afectado por la dilución neta derivada de su alta compensación basada en acciones (SBC).",
                f4_desc: "Foso competitivo masivo derivado de costos de cambio operativos en Android/Google Workspace y un efecto red colosal en su motor de búsqueda y YouTube.",
                f5_desc: "Posicionamiento líder en la revolución de IA con Gemini, Google Cloud y Waymo, ofreciendo opcionalidad en conducción autónoma y computación en la nube.",
                f6_desc: "Asignación de capital buena pero diluida levemente por su compensación en acciones (SBC). Inversiones masivas en Capex de IA.",
                f7_desc: "FCF Yield sólido de ~3.5%-4.0%, representando una de las valoraciones más atractivas en Big Tech por flujo de caja.",
                f8_desc: "Excelente diversificación de anunciantes a nivel global, con nula dependencia de clientes individuales."
            },
            "MSFT": {
                desc: "Microsoft Corporation es el gigante del software empresarial y servicios en la nube (Azure), con una integración líder en productividad de oficina (Office) e Inteligencia Artificial corporativa.",
                f1_desc: "Márgenes operativos superiores al 40% y una de las tasas de conversión de beneficio neto a FCF más altas del mercado corporativo.",
                f2_desc: "Calificación crediticia AAA (de las pocas del mundo), con una cobertura de intereses de triple dígito y una pila de caja formidable.",
                f3_desc: "Crecimiento del 12%-18% anual impulsado por la migración masiva a la nube inteligente y la suscripción SaaS en todas sus líneas de negocio.",
                f4_desc: "Monopolio de facto corporativo con la suite Office, Windows, Active Directory y Azure, con costos de cambio casi prohibitivos para empresas.",
                f5_desc: "Máxima opcionalidad tecnológica derivada de su alianza preferente con OpenAI y la integración de Copilot en todo su ecosistema de software corporativo.",
                f6_desc: "Retornos sobre capital invertido incremental (ROCIC) estelares mediante adquisiciones estratégicas clave y Capex agresivo en infraestructura de nube.",
                f7_desc: "FCF Yield de ~2.5%-3.0% debido a múltiplos exigentes impulsados por el optimismo en IA.",
                f8_desc: "Ecosistema empresarial masivo e hiper-diversificado con millones de clientes corporativos y consumidores globales."
            },
            "NVDA": {
                desc: "NVIDIA Corporation es el diseñador dominante de unidades de procesamiento gráfico (GPU) y la plataforma de software CUDA, sirviendo como la espina dorsal tecnológica de la IA global.",
                f1_desc: "Margen operativo superior al 55% y ROIC récord de la industria (>80%) gracias a su poder de fijación de precios absoluto ante la demanda de cómputo.",
                f2_desc: "Posición financiera impecable con caja neta masiva generada en los últimos trimestres y nulo riesgo de liquidez.",
                f3_desc: "Crecimiento explosivo de ingresos superior al 200% interanual en el sector de centros de datos, limitado únicamente por la capacidad de producción de TSMC.",
                f4_desc: "Foso tecnológico e intelectual inmenso debido a CUDA, la plataforma de software propietaria que impide la migración fácil a chips competidores.",
                f5_desc: "Posicionamiento absoluto como el 'peaje de hardware' de la revolución de IA, con opcionalidad en robótica, automóviles autónomos y gemelos digitales.",
                f6_desc: "Reinversión masiva de capital en Capex y diseño de semiconductores de próxima generación para mantener el liderazgo tecnológico.",
                f7_desc: "FCF Yield muy bajo (~1.5%-2.0%) debido a una valoración implícita de crecimiento hiper-exigente.",
                f8_desc: "Alta concentración de ingresos en pocos proveedores en la nube y fabricantes contratados, penalizada por la regla del factor."
            },
            "FICO": {
                desc: "Fair Isaac Corporation es el proveedor estándar del algoritmo de puntuación crediticia utilizado por más del 90% de los prestamistas en los Estados Unidos para evaluar el riesgo de consumo.",
                f1_desc: "Márgenes EBITDA del 45% y ROIC infinito gracias a un modelo de negocio de licenciamiento puramente digital con mínima base de activos físicos.",
                f2_desc: "Operación antifrágil. Aunque tiene patrimonio neto negativo debido a recompras agresivas, la cobertura de intereses supera las 10 veces el EBITDA.",
                f3_desc: "Crecimiento del 10%-15% impulsado por incrementos continuos de precios y mayor adopción de analítica predictiva en banca.",
                f4_desc: "Monopolio de facto regulado por las agencias hipotecarias federales (Fannie Mae y Freddie Mac), que exigen el uso del Score FICO para finalizar créditos.",
                f5_desc: "Expansión en FICO Platform, una suite de decisión empresarial en la nube que integra analítica de IA y optimización de flujos de trabajo financieros.",
                f6_desc: "Asignación de capital ultra-agresiva mediante recompras destructoras de flotante, logrando un crecimiento masivo de BPA a pesar del apalancamiento.",
                f7_desc: "FCF Yield modesto (~2.5%) debido a la revalorización de múltiplos históricos por su pricing power absoluto.",
                f8_desc: "Dependencia directa de los tres burós de crédito principales norteamericanos (Equifax, Experian y TransUnion)."
            }
        };

        function getCompanyDetails(ticker, company) {
            if (companyDetailedData[ticker]) {
                return companyDetailedData[ticker];
            }
            return {
                desc: `${company.name} (${company.ticker}) es una empresa cotizada en bolsa calificada con un Score CQV global de ${company.cqv.toFixed(2)}, posicionándose en la categoría de ${getTier(company.cqv).name}.`,
                f1_desc: `Calificación F1 de ${company.f1.toFixed(2)} sobre rentabilidad, márgenes operativos y conversión de flujo de caja libre.`,
                f2_desc: `Calificación F2 de ${company.f2.toFixed(2)} sobre la solidez de su balance y cobertura de intereses frente a la deuda.`,
                f3_desc: `Calificación F3 de ${company.f3.toFixed(2)} sobre su tasa de crecimiento orgánico auditada y control de la dilución al accionista por SBC.`,
                f4_desc: `Calificación F4 de ${company.f4.toFixed(2)} que refleja sus barreras de entrada competitivas (Moat) y retención del cliente.`,
                f5_desc: `Calificación F5 de ${company.f5.toFixed(2)} de opcionalidad tecnológica ante la revolución digital y resiliencia disruptiva.`,
                f6_desc: `Calificación F6 de ${company.f6 ? company.f6.toFixed(2) : '8.00'} sobre la asignación de capital operativo y dividendos de la directiva.`,
                f7_desc: `Calificación F7 de ${company.f7 ? company.f7.toFixed(2) : '8.00'} sobre el FCF Yield y la valoración del flujo de caja de la empresa.`,
                f8_desc: `Calificación F8 de ${company.f8 ? company.f8.toFixed(2) : '8.00'} sobre la resiliencia operativa y la diversificación de ingresos frente al riesgo de concentración.`
            };
        }

        let currentVersion = 'v3'; // 'v1', 'v1_1', 'v2' or 'v3'

        function setCQVVersion(version) {
            currentVersion = version;
            
            const dropdown = document.getElementById('select-cqv-version');
            if (dropdown && dropdown.value !== version) {
                dropdown.value = version;
            }
            
            companies.forEach(c => {
                if (version === 'v1') {
                    c.cqv = c.cqv_v1;
                } else if (version === 'v1_1') {
                    c.cqv = c.cqv_v1_1;
                } else if (version === 'v2') {
                    c.cqv = c.cqv_v2;
                } else {
                    c.cqv = c.cqv_v3;
                }
            });
            
            updateVersionUI();
            
            // Re-render everything
            initKPIs();
            renderTopChart();
            sortData();
            renderTable();
            
            // Update History/Trends
            const historySelect = document.getElementById('history-company-select');
            if (historySelect && historySelect.value) {
                loadCompanyHistory();
            }
            
            // Update Simulator
            const simSelect = document.getElementById('sim-company-select');
            if (simSelect) {
                if (simSelect.value) {
                    changeSimYear();
                } else {
                    runSimulation();
                }
            }
            
            // Update Portfolio
            const portfolioYearSelect = document.getElementById('portfolio-year-select');
            if (portfolioYearSelect) {
                renderPortfolioTab();
            }
        }
        
        function updateVersionUI() {
            if (currentVersion === 'v1' || currentVersion === 'v1_1') {
                document.body.classList.add('cqv-v1-active');
            } else {
                document.body.classList.remove('cqv-v1-active');
            }
        }

        function initDashboard() {
            // Apply saved theme preference
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme === 'light') {
                document.body.classList.add('light-theme');
                const themeIcon = document.getElementById('theme-toggle-icon');
                if (themeIcon) {
                    themeIcon.className = 'fa-solid fa-moon';
                }
            }
            
            companies = window.companiesData || (typeof companiesData !== 'undefined' ? companiesData : []);
            if (companies.length === 0) {
                console.error("No companies data available!");
                return;
            }
            filteredData = [...companies];
            
            // Set initial version
            setCQVVersion('v3');
            
            populateSimCompanySelect();
            populateHistoryCompanySelect();
            initThesesTab();
        }

        function populateSimCompanySelect() {
            const selectEl = document.getElementById('sim-company-select');
            if (!selectEl) return;
            selectEl.innerHTML = '<option value="">-- Valores por defecto (Simulación libre) --</option>';
            const sortedCompanies = [...companies].sort((a, b) => a.ticker.localeCompare(b.ticker));
            sortedCompanies.forEach(c => {
                const opt = document.createElement('option');
                opt.value = c.ticker;
                opt.innerText = `${c.ticker} - ${c.name} (CQV: ${c.cqv.toFixed(2)})`;
                selectEl.appendChild(opt);
            });
        }

        function loadCompanyIntoSimulator() {
            const ticker = document.getElementById('sim-company-select').value;
            const yearWrapper = document.getElementById('sim-year-wrapper');
            const yearSelect = document.getElementById('sim-year-select');
            const simProfileCard = document.getElementById('sim-profile-card');
            const simProfileDesc = document.getElementById('sim-profile-desc');
            const simProfileFactors = document.getElementById('sim-profile-factors');
            
            if (!ticker) {
                if (yearWrapper) yearWrapper.style.display = 'none';
                if (simProfileCard) simProfileCard.style.display = 'none';
                
                document.getElementById('slide-f1').value = 7.5;
                document.getElementById('slide-f2').value = 8.0;
                document.getElementById('slide-f3').value = 7.0;
                document.getElementById('slide-f4').value = 8.5;
                document.getElementById('slide-f5').value = 8.0;
                document.getElementById('slide-f6').value = 8.0;
                document.getElementById('slide-f7').value = 7.0;
                document.getElementById('slide-f8').value = 8.0;
                window.originalSimData = null;
                runSimulation();
            } else {
                const company = companies.find(c => c.ticker === ticker);
                if (company) {
                    if (simProfileCard && simProfileDesc && simProfileFactors) {
                        const details = getCompanyDetails(ticker, company);
                        simProfileDesc.innerText = details.desc;
                        
                        simProfileFactors.innerHTML = `
                            <li><strong style="color: #3b82f6;"><i class="fa-solid fa-wallet"></i> F1 (Rentabilidad):</strong> ${details.f1_desc}</li>
                            <li><strong style="color: #a855f7;"><i class="fa-solid fa-lock"></i> F2 (Solidez):</strong> ${details.f2_desc}</li>
                            <li><strong style="color: #10b981;"><i class="fa-solid fa-arrow-trend-up"></i> F3 (Crecimiento):</strong> ${details.f3_desc}</li>
                            <li><strong style="color: #f59e0b;"><i class="fa-solid fa-shield-halved"></i> F4 (Moat):</strong> ${details.f4_desc}</li>
                            <li><strong style="color: #d946ef;"><i class="fa-solid fa-rocket"></i> F5 (Proyección):</strong> ${details.f5_desc}</li>
                            <li class="v2-only"><strong style="color: #6366f1;"><i class="fa-solid fa-hand-holding-dollar"></i> F6 (Asignación):</strong> ${details.f6_desc}</li>
                            <li class="v2-only"><strong style="color: #06b6d4;"><i class="fa-solid fa-money-bill-trend-up"></i> F7 (FCF Yield):</strong> ${details.f7_desc}</li>
                            <li class="v2-only"><strong style="color: #ec4899;"><i class="fa-solid fa-triangle-exclamation"></i> F8 (Antifragilidad):</strong> ${details.f8_desc}</li>
                        `;
                        simProfileCard.style.display = 'block';
                    }
                    
                    if (yearSelect && yearWrapper) {
                        yearSelect.innerHTML = '';
                        
                        const rawHistory = (typeof cqvHistoryData !== 'undefined' && cqvHistoryData[ticker]) ? cqvHistoryData[ticker] : {};
                        const years = Object.keys(rawHistory).sort();
                        
                        if (!years.includes("2026")) {
                            years.push("2026");
                        }
                        
                        years.sort((a, b) => b - a);
                        
                        years.forEach(yr => {
                            const opt = document.createElement('option');
                            opt.value = yr;
                            opt.innerText = yr === "2026" ? "2026 (Act.)" : yr;
                            yearSelect.appendChild(opt);
                        });
                        
                        yearWrapper.style.display = 'block';
                        yearSelect.value = "2026";
                    }
                    changeSimYear();
                }
            }
        }

        function changeSimYear() {
            const ticker = document.getElementById('sim-company-select').value;
            const yr = document.getElementById('sim-year-select').value;
            if (!ticker || !yr) return;
            
            const company = companies.find(c => c.ticker === ticker);
            if (!company) return;
            
            let f1 = company.f1;
            let f2 = company.f2;
            let f3 = company.f3;
            
            const rawHistory = (typeof cqvHistoryData !== 'undefined' && cqvHistoryData[ticker]) ? cqvHistoryData[ticker] : {};
            if (rawHistory[yr]) {
                f1 = rawHistory[yr].f1;
                f2 = rawHistory[yr].f2;
                f3 = rawHistory[yr].f3;
            }
            
            const f4 = company.f4;
            const f5 = company.f5;
            const f6 = company.f6;
            const f7 = company.f7;
            const f8 = company.f8;
            
            document.getElementById('slide-f1').value = f1;
            document.getElementById('slide-f2').value = f2;
            document.getElementById('slide-f3').value = f3;
            document.getElementById('slide-f4').value = f4;
            document.getElementById('slide-f5').value = f5;
            document.getElementById('slide-f6').value = f6;
            document.getElementById('slide-f7').value = f7;
            document.getElementById('slide-f8').value = f8;
            
            window.originalSimData = {
                name: company.name,
                ticker: `${company.ticker} (${yr === "2026" ? "2026 Act." : yr})`,
                data: [f1, f2, f3, f4, f5, f6, f7, f8]
            };
            
            runSimulation();
        }

        function populateHistoryCompanySelect() {
            const selectEl = document.getElementById('history-company-select');
            if (!selectEl) return;
            selectEl.innerHTML = '<option value="">-- Seleccionar una empresa --</option>';
            const sortedCompanies = [...companies].sort((a, b) => a.ticker.localeCompare(b.ticker));
            sortedCompanies.forEach(c => {
                if (typeof cqvHistoryData !== 'undefined' && cqvHistoryData[c.ticker]) {
                    const opt = document.createElement('option');
                    opt.value = c.ticker;
                    opt.innerText = `${c.ticker} - ${c.name} (CQV: ${c.cqv.toFixed(2)})`;
                    selectEl.appendChild(opt);
                }
            });
        }

        function getChartGridColor() {
            return document.body.classList.contains('light-theme') ? 'rgba(15, 23, 42, 0.08)' : 'rgba(255, 255, 255, 0.06)';
        }

        function getChartLabelColor() {
            return document.body.classList.contains('light-theme') ? '#475569' : '#94a3b8';
        }

        function toggleTheme() {
            document.body.classList.toggle('light-theme');
            const isLight = document.body.classList.contains('light-theme');
            localStorage.setItem('theme', isLight ? 'light' : 'dark');
            
            const themeIcon = document.getElementById('theme-toggle-icon');
            if (themeIcon) {
                themeIcon.className = isLight ? 'fa-solid fa-moon' : 'fa-solid fa-sun';
            }
            
            // Re-render charts
            renderTopChart();
            runSimulation();
            if (typeof loadCompanyHistory === 'function') {
                loadCompanyHistory();
            }
        }

        const presetCompanyNotes = {
            "GOOGL": "La reducción en el score CQV de Google se debe principalmente a una contracción en el Factor F1 (Rentabilidad y Retornos) por el aumento masivo en inversiones de capital (CapEx) en infraestructura de centros de datos para IA y mayores gastos operativos de desarrollo. Esto afectó el Factor F3 (Crecimiento de utilidades libres de caja), contrarrestando su excelente foso competitivo en búsquedas (Factor F4).",
            "AAPL": "El score de Apple muestra gran solidez debido a su insuperable Factor F4 (Foso de Ecosistema cautivo) y alta rentabilidad (F1). Los ligeros retrocesos temporales se atribuyen a una desaceleración en el volumen de crecimiento en hardware (Factor F3), balanceado por el aumento de ingresos en servicios.",
            "NVDA": "La subida vertical de la calificación CQV de Nvidia se debe al incremento exponencial en el Factor F1 (Rentabilidad operativa neta récord de márgenes) y el Factor F3 (Crecimiento de ingresos superiores al 200% interanual), consolidando un monopolio de hardware para Inteligencia Artificial (Factor F4).",
            "MSFT": "Microsoft mantiene un posicionamiento de élite constante. Su score se ve impulsado por la expansión del margen y ventas en la nube (Azure) y la integración rápida de IA en su catálogo de software (Factor F5 - Proyecciones y Factor F4 - Foso corporativo)."
        };

        function loadCompanyNotes(ticker) {
            const textarea = document.getElementById('company-analyst-notes');
            const descLabel = document.getElementById('notes-description-label');
            if (!textarea || !descLabel) return;
            
            const company = companies.find(c => c.ticker === ticker);
            if (!company) {
                textarea.value = '';
                descLabel.innerText = 'Selecciona una empresa para gestionar sus notas de auditoría financiera.';
                textarea.disabled = true;
                return;
            }
            
            textarea.disabled = false;
            descLabel.innerText = `Notas del Analista para ${company.ticker} (${company.name}):`;
            
            // Check localStorage first
            const saved = localStorage.getItem(`cqv_note_${ticker}`);
            if (saved !== null) {
                textarea.value = saved;
            } else if (presetCompanyNotes[ticker]) {
                textarea.value = presetCompanyNotes[ticker];
            } else {
                // Generate automated notes based on factors
                const factors = [
                    { name: 'Rentabilidad (F1)', val: company.f1 },
                    { name: 'Solidez (F2)', val: company.f2 },
                    { name: 'Crecimiento (F3)', val: company.f3 },
                    { name: 'Foso/Moat (F4)', val: company.f4 },
                    { name: 'Proyección (F5)', val: company.f5 }
                ];
                factors.sort((a, b) => b.val - a.val);
                const highest = factors[0];
                const lowest = factors[factors.length - 1];
                
                textarea.value = `Análisis de Score: Su principal fortaleza radica en ${highest.name} con una puntuación de ${highest.val.toFixed(2)}, mientras que presenta áreas de mejora en ${lowest.name} con ${lowest.val.toFixed(2)}.`;
            }
        }

        function saveCompanyNotes() {
            const selectEl = document.getElementById('history-company-select');
            const textarea = document.getElementById('company-analyst-notes');
            const statusSpan = document.getElementById('save-note-status');
            if (!selectEl || !textarea) return;
            
            const ticker = selectEl.value;
            if (!ticker) return;
            
            localStorage.setItem(`cqv_note_${ticker}`, textarea.value);
            
            // Show status label
            if (statusSpan) {
                statusSpan.style.opacity = '1';
                setTimeout(() => {
                    statusSpan.style.opacity = '0';
                }, 2000);
            }
        }

        let historyChart = null;
        function loadCompanyHistory() {
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
                tbody.innerHTML = '<tr><td colspan="10" style="text-align: center; color: var(--text-secondary); padding: 30px 10px;">Selecciona una empresa para ver su evolución.</td></tr>';
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
            
            const rawHistory = (typeof cqvHistoryData !== 'undefined' && cqvHistoryData[ticker]) ? cqvHistoryData[ticker] : {};
            const history = { ...rawHistory };
            
            // Append 2026 calculation if not already present in the history database
            if (!history["2026"]) {
                history["2026"] = { 
                    f1: company.f1, 
                    f2: company.f2, 
                    f3: company.f3, 
                    cqv_v1: company.cqv_v1,
                    cqv_v1_1: company.cqv_v1_1,
                    cqv_v2: company.cqv_v2,
                    cqv_v3: company.cqv_v3,
                    cqv: company.cqv 
                };
            }
            
            const years = Object.keys(history).sort();
            
            years.forEach(yr => {
                const data = history[yr];
                const isCurrent = yr === "2026" && !rawHistory["2026"];
                const label = isCurrent ? "2026 (Act.)" : yr;
                
                let yrCqv = data.cqv;
                if (currentVersion === 'v1') {
                    yrCqv = data.cqv_v1 || (data.f1 * 0.25 + data.f2 * 0.15 + data.f3 * 0.15 + company.f4 * 0.25 + company.f5 * 0.20);
                } else if (currentVersion === 'v1_1') {
                    yrCqv = data.cqv_v1_1 || (data.f1 * 0.25 + data.f2 * 0.15 + data.f3 * 0.15 + company.f4 * 0.25 + company.f5 * 0.20);
                    if (company.f4 < 6.0 || data.f2 < 5.0) {
                        yrCqv = Math.min(yrCqv, 7.00);
                    }
                } else if (currentVersion === 'v2') {
                    yrCqv = data.cqv_v2 || (data.f1 * 0.20 + data.f2 * 0.10 + data.f3 * 0.10 + company.f4 * 0.20 + company.f5 * 0.10 + company.f6 * 0.10 + company.f7 * 0.10 + company.f8 * 0.10);
                } else {
                    yrCqv = data.cqv_v3 || (data.f1 * 0.20 + data.f2 * 0.10 + data.f3 * 0.10 + company.f4 * 0.20 + company.f5 * 0.10 + company.f6 * 0.10 + company.f7 * 0.10 + company.f8 * 0.10);
                    if (company.f4 < 6.0 || data.f2 < 5.0) {
                        yrCqv = Math.min(yrCqv, 7.00);
                    }
                }
                
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><span style="font-weight: bold; color: ${isCurrent ? 'var(--accent)' : 'var(--text-primary)'};">${label}</span></td>
                    <td class="cqv-value-cell">${data.f1.toFixed(2)}</td>
                    <td class="cqv-value-cell">${data.f2.toFixed(2)}</td>
                    <td class="cqv-value-cell">${data.f3.toFixed(2)}</td>
                    <td class="cqv-value-cell">${company.f4.toFixed(2)}</td>
                    <td class="cqv-value-cell">${company.f5.toFixed(2)}</td>
                    <td class="cqv-value-cell">${company.f6.toFixed(2)}</td>
                    <td class="cqv-value-cell">${company.f7.toFixed(2)}</td>
                    <td class="cqv-value-cell">${company.f8.toFixed(2)}</td>
                    <td class="cqv-value-cell score-high" style="font-weight: bold;">${yrCqv.toFixed(2)}</td>
                `;
                tbody.appendChild(tr);
            });
            
            const chartLabels = years.map(yr => (yr === "2026" && !rawHistory["2026"]) ? "2026 (Act.)" : yr);
            const chartData = years.map(yr => {
                const data = history[yr];
                if (currentVersion === 'v1') {
                    return data.cqv_v1 || (data.f1 * 0.25 + data.f2 * 0.15 + data.f3 * 0.15 + company.f4 * 0.25 + company.f5 * 0.20);
                } else if (currentVersion === 'v1_1') {
                    let val = data.cqv_v1_1 || (data.f1 * 0.25 + data.f2 * 0.15 + data.f3 * 0.15 + company.f4 * 0.25 + company.f5 * 0.20);
                    if (company.f4 < 6.0 || data.f2 < 5.0) {
                        val = Math.min(val, 7.00);
                    }
                    return val;
                } else if (currentVersion === 'v2') {
                    return data.cqv_v2 || (data.f1 * 0.20 + data.f2 * 0.10 + data.f3 * 0.10 + company.f4 * 0.20 + company.f5 * 0.10 + company.f6 * 0.10 + company.f7 * 0.10 + company.f8 * 0.10);
                } else {
                    let val = data.cqv_v3 || (data.f1 * 0.20 + data.f2 * 0.10 + data.f3 * 0.10 + company.f4 * 0.20 + company.f5 * 0.10 + company.f6 * 0.10 + company.f7 * 0.10 + company.f8 * 0.10);
                    if (company.f4 < 6.0 || data.f2 < 5.0) {
                        val = Math.min(val, 7.00);
                    }
                    return val;
                }
            });
            renderHistoryChart(ticker, chartLabels, chartData);
            
            // Load analyst notes
            loadCompanyNotes(ticker);
        }

        function renderHistoryChart(ticker, labels, data) {
            if (typeof Chart === 'undefined') {
                console.warn("Chart.js is not loaded. Skipping line chart rendering.");
                return;
            }
            const canvasEl = document.getElementById('historyChart');
            if (!canvasEl) return;
            const ctx = canvasEl.getContext('2d');
            
            if (historyChart) {
                historyChart.destroy();
            }
            
            const gradient = ctx.createLinearGradient(0, 0, 0, 300);
            gradient.addColorStop(0, 'rgba(79, 70, 229, 0.4)');
            gradient.addColorStop(1, 'rgba(79, 70, 229, 0.0)');
            
            historyChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: `Evolución CQV - ${ticker}`,
                        data: data,
                        fill: true,
                        backgroundColor: gradient,
                        borderColor: '#4f46e5',
                        borderWidth: 3,
                        pointBackgroundColor: '#d946ef',
                        pointBorderColor: '#fff',
                        pointRadius: 6,
                        pointHoverRadius: 8,
                        tension: 0.3
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            backgroundColor: '#0f172a',
                            borderColor: '#334155',
                            borderWidth: 1,
                            padding: 12,
                            displayColors: false,
                            callbacks: {
                                title: function(context) {
                                    return `Año ${context[0].label}`;
                                },
                                label: function(context) {
                                    return `CQV Score: ${context.parsed.y.toFixed(2)}`;
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            grid: { color: getChartGridColor() },
                            ticks: { color: getChartLabelColor() }
                        },
                        y: {
                            min: 1,
                            max: 10,
                            grid: { color: getChartGridColor() },
                            ticks: { color: getChartLabelColor(), stepSize: 1 }
                        }
                    }
                }
            });
        }

        // Navigation state
        function switchTab(tabId) {
            // Deactivate all panels
            document.querySelectorAll('.tab-panel').forEach(panel => {
                panel.classList.remove('active');
            });
            // Deactivate all nav buttons
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            
            // Activate current
            document.getElementById('tab-' + tabId).classList.add('active');
            
            // Activate current button
            const clickedBtn = Array.from(document.querySelectorAll('.nav-btn')).find(btn => {
                const text = btn.innerText.toLowerCase();
                if (tabId === 'explorer') return text.includes('explorador');
                if (tabId === 'methodology') return text.includes('metodología');
                if (tabId === 'history') return text.includes('tendencias') || text.includes('historial');
                return text.includes(tabId);
            });
            if (clickedBtn) clickedBtn.classList.add('active');
            
            // Re-render chart if navigating back to dashboard or history
            if (tabId === 'dashboard') {
                setTimeout(renderTopChart, 50);
            } else if (tabId === 'history' && historyChart) {
                setTimeout(() => historyChart.resize(), 50);
            } else if (tabId === 'portfolio') {
                setTimeout(renderPortfolioTab, 50);
            } else if (tabId === 'tesis') {
                setTimeout(renderActiveThesis, 50);
            } else if (tabId === 'momentum') {
                setTimeout(renderMomentumMatrix, 50);
            }
        }

        // Portfolio proposed logic
        function getHistoricalCQV(ticker, year) {
            const company = companies.find(c => c.ticker === ticker);
            if (!company) return null;
            
            const history = typeof cqvHistoryData !== 'undefined' ? cqvHistoryData[ticker] : null;
            
            if (year === '2026') {
                if (history && history["2026"]) {
                    return getScoreForYearData(history["2026"], company);
                }
                return company.cqv;
            }
            
            if (history && history[year]) {
                return getScoreForYearData(history[year], company);
            }
            return null;
        }

        function getScoreForYearData(yrData, company) {
            if (currentVersion === 'v1') {
                return yrData.cqv_v1 || (yrData.f1 * 0.25 + yrData.f2 * 0.15 + yrData.f3 * 0.15 + company.f4 * 0.25 + company.f5 * 0.20);
            } else if (currentVersion === 'v1_1') {
                let val = yrData.cqv_v1_1 || (yrData.f1 * 0.25 + yrData.f2 * 0.15 + yrData.f3 * 0.15 + company.f4 * 0.25 + company.f5 * 0.20);
                if (company.f4 < 6.0 || yrData.f2 < 5.0) {
                    val = Math.min(val, 7.00);
                }
                return val;
            } else if (currentVersion === 'v2') {
                return yrData.cqv_v2 || (yrData.f1 * 0.20 + yrData.f2 * 0.10 + yrData.f3 * 0.10 + company.f4 * 0.20 + company.f5 * 0.10 + company.f6 * 0.10 + company.f7 * 0.10 + company.f8 * 0.10);
            } else {
                let val = yrData.cqv_v3 || (yrData.f1 * 0.20 + yrData.f2 * 0.10 + yrData.f3 * 0.10 + company.f4 * 0.20 + company.f5 * 0.10 + company.f6 * 0.10 + company.f7 * 0.10 + company.f8 * 0.10);
                if (company.f4 < 6.0 || yrData.f2 < 5.0) {
                    val = Math.min(val, 7.00);
                }
                return val;
            }
        }

        function getTop20ForYear(year) {
            const list = [];
            companies.forEach(company => {
                const score = getHistoricalCQV(company.ticker, year);
                if (score !== null) {
                    list.push({
                        ticker: company.ticker,
                        name: company.name,
                        sector: company.sector,
                        cqv: score,
                        peg_score: company.peg_score !== undefined ? company.peg_score : 5.00
                    });
                }
            });
            list.sort((a, b) => b.cqv - a.cqv);
            return list.slice(0, 20);
        }

        let activePortfolioView = 'annual';

        function setPortfolioView(view) {
            activePortfolioView = view;
            
            const btnAnnual = document.getElementById('btn-portfolio-view-annual');
            const btnMatrix = document.getElementById('btn-portfolio-view-matrix');
            const btnRank = document.getElementById('btn-portfolio-view-rank');
            
            const containerAnnual = document.getElementById('portfolio-annual-container');
            const containerMatrix = document.getElementById('portfolio-matrix-container');
            const containerRank = document.getElementById('portfolio-rank-container');
            
            if (!btnAnnual || !btnMatrix || !btnRank) return;
            
            const resetBtn = (btn) => {
                btn.style.background = 'var(--input-bg)';
                btn.style.borderColor = 'var(--input-border)';
                btn.style.color = 'var(--text-secondary)';
            };
            const setBtnActive = (btn) => {
                btn.style.background = 'var(--primary)';
                btn.style.borderColor = 'var(--primary)';
                btn.style.color = '#fff';
            };
            
            resetBtn(btnAnnual);
            resetBtn(btnMatrix);
            resetBtn(btnRank);
            
            containerAnnual.style.display = 'none';
            containerMatrix.style.display = 'none';
            containerRank.style.display = 'none';
            
            if (view === 'annual') {
                setBtnActive(btnAnnual);
                containerAnnual.style.display = 'block';
                renderPortfolioTab();
            } else if (view === 'matrix') {
                setBtnActive(btnMatrix);
                containerMatrix.style.display = 'block';
                renderPortfolioMatrix();
            } else {
                setBtnActive(btnRank);
                containerRank.style.display = 'block';
                renderPortfolioRank();
            }
        }

        function renderPortfolioMatrix() {
            const years = ['2022', '2023', '2024', '2025', '2026'];
            const yearlyTop20 = {};
            years.forEach(yr => {
                yearlyTop20[yr] = getTop20ForYear(yr);
            });
            
            const allTickersSet = new Set();
            years.forEach(yr => {
                yearlyTop20[yr].forEach(c => {
                    allTickersSet.add(c.ticker);
                });
            });
            const allTickers = Array.from(allTickersSet);
            
            const rows = [];
            allTickers.forEach(ticker => {
                const company = companies.find(c => c.ticker === ticker);
                if (!company) return;
                
                const row = {
                    ticker: ticker,
                    name: company.name,
                    sector: company.sector,
                    scores: {}
                };
                
                years.forEach(yr => {
                    const top20Yr = yearlyTop20[yr];
                    const inTop20 = top20Yr.find(c => c.ticker === ticker);
                    
                    if (inTop20) {
                        row.scores[yr] = {
                            score: inTop20.cqv,
                            inTop20: true
                        };
                    } else {
                        const score = getHistoricalCQV(ticker, yr);
                        row.scores[yr] = {
                            score: score,
                            inTop20: false
                        };
                    }
                });
                rows.push(row);
            });
            
            rows.sort((a, b) => {
                const scoreA = a.scores['2026'].score || 0;
                const scoreB = b.scores['2026'].score || 0;
                return scoreB - scoreA;
            });
            
            const tbody = document.getElementById('portfolio-matrix-body');
            if (!tbody) return;
            tbody.innerHTML = '';
            
            rows.forEach(r => {
                const tr = document.createElement('tr');
                let cellsHtml = '';
                years.forEach(yr => {
                    const yrData = r.scores[yr];
                    if (yrData && yrData.score !== null) {
                        if (yrData.inTop20) {
                            cellsHtml += `<td style="text-align: right; font-weight: bold; background: rgba(16, 185, 129, 0.08); color: var(--accent); border: 1px solid rgba(16, 185, 129, 0.1);">${yrData.score.toFixed(2)}</td>`;
                        } else {
                            cellsHtml += `<td style="text-align: right; color: var(--text-secondary); opacity: 0.45;">-</td>`;
                        }
                    } else {
                        cellsHtml += `<td style="text-align: right; color: var(--text-secondary); opacity: 0.45;">-</td>`;
                    }
                });
                
                tr.innerHTML = `
                    <td><span class="ticker-badge">${r.ticker}</span></td>
                    <td><span class="company-name" style="font-size: 12px; font-weight: 600;">${r.name}</span></td>
                    <td style="font-size: 11px; color: var(--text-secondary);">${r.sector}</td>
                    ${cellsHtml}
                `;
                tbody.appendChild(tr);
            });
        }

        function renderPortfolioRank() {
            const years = ['2022', '2023', '2024', '2025', '2026'];
            const yearlyTop20 = {};
            years.forEach(yr => {
                yearlyTop20[yr] = getTop20ForYear(yr);
            });
            
            const tbody = document.getElementById('portfolio-rank-body');
            if (!tbody) return;
            tbody.innerHTML = '';
            
            for (let i = 0; i < 20; i++) {
                const tr = document.createElement('tr');
                let cellsHtml = '';
                
                years.forEach(yr => {
                    const top20Yr = yearlyTop20[yr];
                    const company = top20Yr[i];
                    
                    if (company) {
                        const score = company.cqv;
                        let cellStyle = '';
                        if (score >= 9.0) {
                            cellStyle = 'background: rgba(16, 185, 129, 0.22); color: var(--text-primary); border: 1px solid rgba(16, 185, 129, 0.3); font-weight: bold;';
                        } else if (score >= 8.5) {
                            cellStyle = 'background: rgba(16, 185, 129, 0.12); color: var(--text-primary); border: 1px solid rgba(16, 185, 129, 0.2); font-weight: 600;';
                        } else if (score >= 8.0) {
                            cellStyle = 'background: rgba(234, 179, 8, 0.08); color: var(--text-secondary); border: 1px solid rgba(234, 179, 8, 0.15);';
                        } else {
                            cellStyle = 'background: rgba(148, 163, 184, 0.04); color: var(--text-secondary); border: 1px solid var(--card-border);';
                        }
                        
                        cellsHtml += `
                            <td style="text-align: center; padding: 10px; ${cellStyle}">
                                <div style="font-size: 11px; font-family: var(--font-title);">${company.ticker}</div>
                                <div style="font-size: 9px; opacity: 0.8; margin-top: 2px;">${score.toFixed(2)}</div>
                            </td>
                        `;
                    } else {
                        cellsHtml += `<td style="text-align: center; padding: 10px; color: var(--text-secondary); opacity: 0.45; border: 1px solid var(--card-border);">-</td>`;
                    }
                });
                
                tr.innerHTML = `
                    <td style="font-weight: bold; color: var(--text-secondary); text-align: left; padding: 10px; vertical-align: middle;">#${i + 1}</td>
                    ${cellsHtml}
                `;
                tbody.appendChild(tr);
            }
        }

        function renderPortfolioTab() {
            if (activePortfolioView === 'matrix') {
                renderPortfolioMatrix();
                return;
            }
            if (activePortfolioView === 'rank') {
                renderPortfolioRank();
                return;
            }
            const yearSelect = document.getElementById('portfolio-year-select');
            if (!yearSelect) return;
            const year = yearSelect.value;
            
            document.getElementById('portfolio-title-year').innerText = year;
            
            const top20 = getTop20ForYear(year);
            const tbody = document.getElementById('portfolio-table-body');
            tbody.innerHTML = '';
            
            top20.forEach((c, idx) => {
                const tr = document.createElement('tr');
                let pegStyle = 'color: var(--text-secondary);';
                if (c.peg_score >= 8.5) pegStyle = 'color: var(--elite); font-weight: 700;';
                else if (c.peg_score >= 7.0) pegStyle = 'color: var(--strong); font-weight: 600;';
                else if (c.peg_score >= 5.0) pegStyle = 'color: var(--medium);';
                else pegStyle = 'color: var(--weak);';

                tr.innerHTML = `
                    <td style="font-weight: bold; color: var(--text-secondary);">${idx + 1}</td>
                    <td><span class="ticker-badge">${c.ticker}</span></td>
                    <td><span class="company-name" style="font-size: 12px; font-weight: 600;">${c.name}</span></td>
                    <td style="font-size: 12px; color: var(--text-secondary);">${c.sector}</td>
                    <td style="text-align: right; ${pegStyle}">${c.peg_score.toFixed(2)}</td>
                    <td class="cqv-value-cell score-high" style="font-weight: bold; text-align: right; color: var(--accent);">${c.cqv.toFixed(2)}</td>
                `;
                tbody.appendChild(tr);
            });
            
            const prevYear = (parseInt(year) - 1).toString();
            const inflowsList = document.getElementById('portfolio-inflows-list');
            const outflowsList = document.getElementById('portfolio-outflows-list');
            
            inflowsList.innerHTML = '';
            outflowsList.innerHTML = '';
            
            const prevTop20 = getTop20ForYear(prevYear);
            
            if (prevTop20.length > 0) {
                const currentTickers = top20.map(c => c.ticker);
                const prevTickers = prevTop20.map(c => c.ticker);
                
                const inflows = top20.filter(c => !prevTickers.includes(c.ticker));
                const outflows = prevTop20.filter(c => !currentTickers.includes(c.ticker));
                
                if (inflows.length === 0) {
                    inflowsList.innerHTML = '<div style="color: var(--text-secondary); font-style: italic;">Sin rotación (0% cambios)</div>';
                } else {
                    inflows.forEach(c => {
                        inflowsList.innerHTML += `
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(16, 185, 129, 0.05); padding-bottom: 4px;">
                                <span><span class="ticker-badge" style="background: rgba(16, 185, 129, 0.15); color: var(--elite); border-color: rgba(16, 185, 129, 0.3); font-size:10px;">${c.ticker}</span> ${c.name}</span>
                                <span style="font-weight: 600; color: var(--elite); font-size:11px;">Score: ${c.cqv.toFixed(2)}</span>
                            </div>
                        `;
                    });
                }
                
                if (outflows.length === 0) {
                    outflowsList.innerHTML = '<div style="color: var(--text-secondary); font-style: italic;">Sin rotación (0% cambios)</div>';
                } else {
                    outflows.forEach(c => {
                        outflowsList.innerHTML += `
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(239, 68, 68, 0.05); padding-bottom: 4px; opacity: 0.85;">
                                <span><span class="ticker-badge" style="background: rgba(239, 68, 68, 0.1); color: var(--weak); border-color: rgba(239, 68, 68, 0.2); font-size:10px;">${c.ticker}</span> ${c.name}</span>
                                <span style="font-weight: 600; color: var(--weak); font-size:11px;">Pre-Score: ${c.cqv.toFixed(2)}</span>
                            </div>
                        `;
                    });
                }
            } else {
                inflowsList.innerHTML = '<div style="color: var(--text-secondary); font-style: italic;">No hay historial previo para comparar</div>';
                outflowsList.innerHTML = '<div style="color: var(--text-secondary); font-style: italic;">No hay historial previo para comparar</div>';
            }
            
            const sectorDist = {};
            top20.forEach(c => {
                sectorDist[c.sector] = (sectorDist[c.sector] || 0) + 1;
            });
            
            const sectorDistDiv = document.getElementById('portfolio-sector-dist');
            sectorDistDiv.innerHTML = '';
            
            const sortedSectors = Object.keys(sectorDist).sort((a, b) => sectorDist[b] - sectorDist[a]);
            sortedSectors.forEach(sec => {
                const count = sectorDist[sec];
                const pct = (count / 20) * 100;
                sectorDistDiv.innerHTML += `
                    <div style="margin-bottom: 4px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 2px; font-size: 11px;">
                            <span style="max-width: 170px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${sec}</span>
                            <span style="font-weight: 600; color: var(--text-primary);">${count} (${pct.toFixed(0)}%)</span>
                        </div>
                        <div class="dist-bar-bg" style="height: 6px; background: rgba(148,163,184,0.15); border-radius:3px; overflow:hidden;">
                            <div class="dist-bar-fill" style="background: var(--accent); width: ${pct}%; height: 100%;"></div>
                        </div>
                    </div>
                `;
            });
        }

        // Data Helpers
        function getTier(score) {
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
        function renderTopChart() {
            if (typeof Chart === 'undefined') {
                console.warn("Chart.js is not loaded. Skipping chart rendering.");
                return;
            }
            const canvasEl = document.getElementById('topChart');
            if (!canvasEl) return;
            const ctx = canvasEl.getContext('2d');
            const top15 = [...companies].sort((a, b) => b.cqv - a.cqv).slice(0, 15);
            
            const labels = top15.map(c => c.ticker);
            const data = top15.map(c => c.cqv);
            
            if (topChart) {
                topChart.destroy();
            }
            
            // Gradient fill
            const gradient = ctx.createLinearGradient(0, 0, 0, 300);
            gradient.addColorStop(0, '#4f46e5');
            gradient.addColorStop(1, '#d946ef');
            
            topChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'CQV Score',
                        data: data,
                        backgroundColor: gradient,
                        borderColor: 'rgba(255,255,255,0.1)',
                        borderWidth: 1,
                        borderRadius: 6,
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            backgroundColor: '#0f172a',
                            titleColor: '#f8fafc',
                            bodyColor: '#cbd5e1',
                            borderColor: '#334155',
                            borderWidth: 1,
                            padding: 12,
                            displayColors: false,
                            callbacks: {
                                title: function(context) {
                                    const index = context[0].dataIndex;
                                    return `${top15[index].ticker} - ${top15[index].name}`;
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            grid: {
                                display: false
                            },
                            ticks: {
                                color: getChartLabelColor(),
                                font: { family: 'Inter', size: 11 }
                            }
                        },
                        y: {
                            min: 6,
                            max: 10,
                            grid: {
                                color: getChartGridColor()
                            },
                            ticks: {
                                color: getChartLabelColor(),
                                font: { family: 'Outfit', size: 11 }
                            }
                        }
                    }
                }
            });
        }

        // Explorer Table Logic
        let filteredData = [];
        let currentSort = { column: 'cqv', direction: 'desc' };
        let currentPage = 1;
        let rowsPerPage = 'all';

        function renderTable() {
            const tbody = document.getElementById('companies-table-body');
            if (!tbody) return;
            tbody.innerHTML = '';
            
            const pageData = filteredData;
            
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
                        
                        bars += `<div class="sparkline-bar" style="height: ${heightPct}%; background-color: ${barColor};" title="Año ${yr}: ${yrCqv.toFixed(2)}"></div>`;
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
                            <div class="sparkline-bar" style="height: ${heightPct}%; background-color: ${barColor};" title="Año 2026 (Act.): ${c.cqv.toFixed(2)}"></div>
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

                const pegVal = c.peg_score !== undefined ? c.peg_score : 5.00;
                let pegStyle = 'color: var(--text-secondary);';
                if (pegVal >= 8.5) pegStyle = 'color: var(--elite); font-weight: 700;';
                else if (pegVal >= 7.0) pegStyle = 'color: var(--strong); font-weight: 600;';
                else if (pegVal >= 5.0) pegStyle = 'color: var(--medium); font-weight: 500;';
                else pegStyle = 'color: var(--weak); font-weight: 500;';

                const momVal = c.momentum_score !== undefined ? c.momentum_score : 5.00;
                let momStyle = 'color: var(--text-secondary);';
                if (momVal >= 8.5) momStyle = 'color: var(--elite); font-weight: 700;';
                else if (momVal >= 7.0) momStyle = 'color: var(--strong); font-weight: 600;';
                else if (momVal >= 5.0) momStyle = 'color: var(--medium); font-weight: 500;';
                else momStyle = 'color: var(--weak); font-weight: 500;';

                tr.innerHTML = `
                    <td><span class="ticker-badge">${c.ticker}</span></td>
                    <td><span class="company-name">${c.name}</span></td>
                    <td class="cqv-value-cell">${c.f1.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f2.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f3.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f4.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f5.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f6.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f7.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f8.toFixed(2)}</td>
                    <td class="cqv-value-cell" style="${pegStyle}">${pegVal.toFixed(2)}</td>
                    <td class="cqv-value-cell" style="${momStyle}">${momVal.toFixed(2)}</td>
                    <td class="cqv-value-cell score-high" style="font-weight: bold;">${c.cqv.toFixed(2)}</td>
                    <td>${sparklineCellHtml}</td>
                    <td><span class="tier-badge ${tier.class}">${tier.name}</span></td>
                `;
                tbody.appendChild(tr);
            });
            
            // Update labels
            const totalCount = filteredData.length;
            document.getElementById('showing-entries-label').innerText = `Mostrando las ${totalCount} empresas`;
            
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

        function toggleAdvancedFilters() {
            const panel = document.getElementById('advanced-filters-panel');
            const btn = document.getElementById('btn-toggle-advanced-filters');
            if (panel.style.display === 'none') {
                panel.style.display = 'block';
                btn.style.background = 'var(--primary)';
                btn.style.borderColor = 'var(--primary)';
                btn.style.color = '#fff';
                btn.innerHTML = '<i class="fa-solid fa-xmark"></i> Ocultar Rangos';
            } else {
                panel.style.display = 'none';
                btn.style.background = 'var(--input-bg)';
                btn.style.borderColor = 'var(--input-border)';
                btn.style.color = 'var(--text-secondary)';
                btn.innerHTML = '<i class="fa-solid fa-sliders"></i> Filtros Avanzados';
            }
        }

        function resetAdvancedFilters() {
            const ids = ['cqv', 'peg', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8'];
            ids.forEach(id => {
                const elMin = document.getElementById('range-min-' + id);
                if (elMin) elMin.value = 0.0;
                const elMax = document.getElementById('range-max-' + id);
                if (elMax) elMax.value = 10.0;
            });
            applyAdvancedFilters();
        }

        function applyAdvancedFilters() {
            const ids = ['cqv', 'peg', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8'];
            ids.forEach(id => {
                const elMin = document.getElementById('range-min-' + id);
                const elMax = document.getElementById('range-max-' + id);
                if (elMin && elMax) {
                    let minVal = parseFloat(elMin.value);
                    let maxVal = parseFloat(elMax.value);
                    
                    if (minVal > maxVal) {
                        minVal = maxVal;
                        elMin.value = minVal;
                    }
                    
                    const valMinSpan = document.getElementById('val-min-' + id);
                    const valMaxSpan = document.getElementById('val-max-' + id);
                    if (valMinSpan) valMinSpan.innerText = minVal.toFixed(1);
                    if (valMaxSpan) valMaxSpan.innerText = maxVal.toFixed(1);
                }
            });
            
            const tier = document.getElementById('tier-filter').value;
            const query = document.getElementById('search-bar').value.toLowerCase().trim();
            applyFilters(query, tier);
        }

        function applyFilters(query, tier) {
            const getRange = (id) => {
                const elMin = document.getElementById('range-min-' + id);
                const elMax = document.getElementById('range-max-' + id);
                return {
                    min: elMin ? parseFloat(elMin.value) : 0.0,
                    max: elMax ? parseFloat(elMax.value) : 10.0
                };
            };
            
            const rCqv = getRange('cqv');
            const rPeg = getRange('peg');
            const rF1 = getRange('f1');
            const rF2 = getRange('f2');
            const rF3 = getRange('f3');
            const rF4 = getRange('f4');
            const rF5 = getRange('f5');
            const rF6 = getRange('f6');
            const rF7 = getRange('f7');
            const rF8 = getRange('f8');

            filteredData = companies.filter(c => {
                let matchesQuery = false;
                if (query.includes(',')) {
                    const parts = query.split(',').map(p => p.trim()).filter(p => p.length > 0);
                    if (parts.length === 0) {
                        matchesQuery = true;
                    } else {
                        matchesQuery = parts.some(part => c.ticker.toLowerCase().includes(part) || c.name.toLowerCase().includes(part));
                    }
                } else {
                    matchesQuery = c.ticker.toLowerCase().includes(query) || c.name.toLowerCase().includes(query);
                }
                
                let matchesTier = true;
                if (tier === 'elite') matchesTier = c.cqv >= 9.0;
                else if (tier === 'strong') matchesTier = c.cqv >= 8.5 && c.cqv < 9.0;
                else if (tier === 'medium') matchesTier = c.cqv >= 8.0 && c.cqv < 8.5;
                else if (tier === 'speculative') matchesTier = c.cqv < 8.0;
                
                const matchesCqv = c.cqv >= rCqv.min && c.cqv <= rCqv.max;
                const pegVal = c.peg_score !== undefined ? c.peg_score : 5.0;
                const matchesPeg = pegVal >= rPeg.min && pegVal <= rPeg.max;
                
                const matchesF1 = c.f1 >= rF1.min && c.f1 <= rF1.max;
                const matchesF2 = c.f2 >= rF2.min && c.f2 <= rF2.max;
                const matchesF3 = c.f3 >= rF3.min && c.f3 <= rF3.max;
                const matchesF4 = c.f4 >= rF4.min && c.f4 <= rF4.max;
                const matchesF5 = c.f5 >= rF5.min && c.f5 <= rF5.max;
                
                let matchesV2Factors = true;
                if (currentVersion === 'v2' || currentVersion === 'v3') {
                    matchesV2Factors = (c.f6 >= rF6.min && c.f6 <= rF6.max) &&
                                       (c.f7 >= rF7.min && c.f7 <= rF7.max) &&
                                       (c.f8 >= rF8.min && c.f8 <= rF8.max);
                }
                
                return matchesQuery && matchesTier && matchesCqv && matchesPeg && matchesF1 && matchesF2 && matchesF3 && matchesF4 && matchesF5 && matchesV2Factors;
            });
            
            currentPage = 1;
            sortData();
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
            const colIndices = { 'ticker': 0, 'name': 1, 'f1': 2, 'f2': 3, 'f3': 4, 'f4': 5, 'f5': 6, 'f6': 7, 'f7': 8, 'f8': 9, 'peg_score': 10, 'momentum_score': 11, 'cqv': 12 };
            
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
                let valA = a[col] !== undefined ? a[col] : 0;
                let valB = b[col] !== undefined ? b[col] : 0;
                
                if (typeof valA === 'string') {
                    return valA.localeCompare(valB) * dir;
                }
                return (valA - valB) * dir;
            });
        }

        function renderMomentumMatrix() {
            const listLeaders = document.getElementById('list-leaders');
            const listValue = document.getElementById('list-value-opportunities');
            const listSpec = document.getElementById('list-speculative');
            const listAvoid = document.getElementById('list-avoid');

            if (!listLeaders || !listValue || !listSpec || !listAvoid) return;

            listLeaders.innerHTML = '';
            listValue.innerHTML = '';
            listSpec.innerHTML = '';
            listAvoid.innerHTML = '';

            // Sort companies by CQV descending to show high quality first
            const sortedCompanies = [...companies].sort((a, b) => b.cqv - a.cqv);

            sortedCompanies.forEach(c => {
                const cqv = c.cqv;
                const mom = c.momentum_score !== undefined ? c.momentum_score : 5.0;

                const itemHtml = `
                    <div style="display: flex; align-items: center; justify-content: space-between; padding: 6px 10px; background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 6px; transition: var(--transition);">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="ticker-badge" style="min-width: 55px; text-align: center;">${c.ticker}</span>
                            <span style="font-weight: 500; font-family: var(--font-title); font-size: 11.5px; color: var(--text-primary); text-overflow: ellipsis; overflow: hidden; white-space: nowrap; max-width: 220px;">${c.name}</span>
                        </div>
                        <div style="display: flex; align-items: center; gap: 15px; font-size: 11px;">
                            <span>CQV: <strong style="color: ${cqv >= 9.0 ? 'var(--elite)' : cqv >= 8.5 ? 'var(--strong)' : cqv >= 8.0 ? 'var(--medium)' : 'var(--weak)'};">${cqv.toFixed(2)}</strong></span>
                            <span>Mom: <strong style="color: ${mom >= 8.5 ? 'var(--elite)' : mom >= 7.0 ? 'var(--strong)' : mom >= 5.0 ? 'var(--medium)' : 'var(--weak)'};">${mom.toFixed(2)}</strong></span>
                        </div>
                    </div>
                `;

                if (cqv > 8.0 && mom > 6.5) {
                    listLeaders.insertAdjacentHTML('beforeend', itemHtml);
                } else if (cqv > 8.0 && mom <= 6.5) {
                    listValue.insertAdjacentHTML('beforeend', itemHtml);
                } else if (cqv <= 8.0 && mom > 6.5) {
                    listSpec.insertAdjacentHTML('beforeend', itemHtml);
                } else {
                    listAvoid.insertAdjacentHTML('beforeend', itemHtml);
                }
            });

            // Show empty placeholders if no items match
            if (listLeaders.children.length === 0) listLeaders.innerHTML = '<div style="color: var(--text-secondary); padding: 10px; font-size: 11px; text-align: center;">Ninguna empresa en esta categoría</div>';
            if (listValue.children.length === 0) listValue.innerHTML = '<div style="color: var(--text-secondary); padding: 10px; font-size: 11px; text-align: center;">Ninguna empresa en esta categoría</div>';
            if (listSpec.children.length === 0) listSpec.innerHTML = '<div style="color: var(--text-secondary); padding: 10px; font-size: 11px; text-align: center;">Ninguna empresa en esta categoría</div>';
            if (listAvoid.children.length === 0) listAvoid.innerHTML = '<div style="color: var(--text-secondary); padding: 10px; font-size: 11px; text-align: center;">Ninguna empresa en esta categoría</div>';
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
            } else if (currentVersion === 'v1_1') {
                cqv = (f1 * 0.25) + (f2 * 0.15) + (f3 * 0.15) + (f4 * 0.25) + (f5 * 0.20);
                if (f4 < 6.0 || f2 < 5.0) {
                    cqv = Math.min(cqv, 7.00);
                }
            } else {
                cqv = (f1 * 0.20) + (f2 * 0.10) + (f3 * 0.10) + (f4 * 0.20) + (f5 * 0.10) + (f6 * 0.10) + (f7 * 0.10) + (f8 * 0.10);
                if (currentVersion === 'v3') {
                    if (f4 < 6.0 || f2 < 5.0) {
                        cqv = Math.min(cqv, 7.00);
                    }
                }
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
            
            const is5F = (currentVersion === 'v1' || currentVersion === 'v1_1');
            const simDataFinal = is5F ? data.slice(0, 5) : data;
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
                const benchmarkDataFinal = is5F ? originalBenchmark.data.slice(0, 5) : originalBenchmark.data;
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
                    labels: is5F ?
                        ['F1 (Rent.)', 'F2 (Solidez)', 'F3 (Crec.)', 'F4 (Moat)', 'F5 (Proj.)'] :
                        ['F1 (Rent.)', 'F2 (Solidez)', 'F3 (Crec.)', 'F4 (Moat)', 'F5 (Proj.)', 'F6 (Asig.)', 'F7 (Yield)', 'F8 (Antif.)'],
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
        const hasData = (typeof window.companiesData !== 'undefined') || (typeof companiesData !== 'undefined');
        if (!hasData) {
            console.warn("cqv_data.js not found or blocked. Fetching cqv_data.json...");
            fetch('cqv_data.json')
                .then(r => r.json())
                .then(data => {
                    window.companiesData = data;
                    initDashboard();
                })
                .catch(err => {
                    console.error("CORS block or missing file. Manually injecting fallback...", err);
                    window.companiesData = [];
                });
        } else {
            initDashboard();
        }
        // Investment Theses Tab logic
        function initThesesTab() {
            const select = document.getElementById('thesis-ticker-select');
            if (!select) return;
            select.innerHTML = '';
            
            const tickers = Object.keys(window.investmentTheses || {}).sort();
            if (tickers.length === 0) {
                select.innerHTML = '<option value="">No hay informes disponibles</option>';
                document.getElementById('thesis-content-container').innerHTML = '<p style="color: var(--text-secondary);">No hay tesis de inversión disponibles en la base de datos.</p>';
                return;
            }
            
            tickers.forEach(t => {
                const company = companies.find(c => {
                    const norm = c.ticker.split('.')[0].split('-')[0];
                    return c.ticker === t || norm === t;
                });
                const name = company ? company.name : t;
                const option = document.createElement('option');
                option.value = t;
                option.innerText = `${t} - ${name}`;
                select.appendChild(option);
            });
            
            renderActiveThesis();
        }
        
        function renderActiveThesis() {
            const select = document.getElementById('thesis-ticker-select');
            const container = document.getElementById('thesis-content-container');
            if (!select || !container) return;
            
            const ticker = select.value;
            if (!ticker) {
                container.innerHTML = '<p style="color: var(--text-secondary);">Selecciona una empresa para ver su tesis de inversión.</p>';
                return;
            }
            
            const markdown = (window.investmentTheses || {})[ticker];
            container.innerHTML = renderMarkdownToHTML(markdown);
        }
        
        function renderMarkdownToHTML(markdown) {
            if (!markdown) return '<p style="color: var(--text-secondary);">Selecciona una empresa para cargar su informe.</p>';
            
            let lines = markdown.split('\n');
            let html = '';
            let inList = false;
            let inTable = false;
            let tableHeaders = [];
            let tableRows = [];
            
            for (let i = 0; i < lines.length; i++) {
                let line = lines[i].trim();
                
                if (line === '---') {
                    if (inList) { html += '</ul>'; inList = false; }
                    if (inTable) { html += renderHTMLTable(tableHeaders, tableRows); inTable = false; tableHeaders = []; tableRows = []; }
                    html += '<hr style="border: 0; border-top: 1px solid var(--card-border); margin: 20px 0;">';
                    continue;
                }
                
                if (line.startsWith('# ')) {
                    if (inList) { html += '</ul>'; inList = false; }
                    if (inTable) { html += renderHTMLTable(tableHeaders, tableRows); inTable = false; tableHeaders = []; tableRows = []; }
                    html += `<h2 style="font-family: var(--font-title); font-size: 20px; color: var(--primary); margin-top: 0; margin-bottom: 15px; padding-bottom: 8px; border-bottom: 2px solid var(--primary);">${line.substring(2)}</h2>`;
                    continue;
                }
                if (line.startsWith('## ')) {
                    if (inList) { html += '</ul>'; inList = false; }
                    if (inTable) { html += renderHTMLTable(tableHeaders, tableRows); inTable = false; tableHeaders = []; tableRows = []; }
                    html += `<h3 style="font-family: var(--font-title); font-size: 15px; color: var(--text-primary); margin-top: 25px; margin-bottom: 12px; border-bottom: 1px solid var(--card-border); padding-bottom: 5px;">${line.substring(3)}</h3>`;
                    continue;
                }
                if (line.startsWith('### ')) {
                    if (inList) { html += '</ul>'; inList = false; }
                    if (inTable) { html += renderHTMLTable(tableHeaders, tableRows); inTable = false; tableHeaders = []; tableRows = []; }
                    html += `<h4 style="font-family: var(--font-title); font-size: 13px; color: var(--accent); margin-top: 18px; margin-bottom: 8px;">${line.substring(4)}</h4>`;
                    continue;
                }
                
                if (line.startsWith('- ') || line.startsWith('* ')) {
                    if (inTable) { html += renderHTMLTable(tableHeaders, tableRows); inTable = false; tableHeaders = []; tableRows = []; }
                    if (!inList) {
                        html += '<ul style="margin: 10px 0; padding-left: 20px; list-style-type: disc;">';
                        inList = true;
                    }
                    html += `<li style="font-size: 12.5px; color: var(--text-secondary); margin-bottom: 6px; line-height: 1.5;">${parseInlineMarkdown(line.substring(2))}</li>`;
                    continue;
                }
                
                const numMatch = line.match(/^(\d+)\.\s(.*)/);
                if (numMatch) {
                    if (inTable) { html += renderHTMLTable(tableHeaders, tableRows); inTable = false; tableHeaders = []; tableRows = []; }
                    if (inList) { html += '</ul>'; inList = false; }
                    html += `<p style="font-size: 12.5px; color: var(--text-secondary); margin-bottom: 8px; line-height: 1.5; padding-left: 15px; text-indent: -15px;"><strong>${numMatch[1]}.</strong> ${parseInlineMarkdown(numMatch[2])}</p>`;
                    continue;
                }
                
                if (line.startsWith('|')) {
                    if (inList) { html += '</ul>'; inList = false; }
                    if (!inTable) {
                        inTable = true;
                        tableHeaders = line.split('|').map(s => s.trim()).filter((s, idx, arr) => idx > 0 && idx < arr.length - 1);
                    } else {
                        if (line.includes('---')) continue;
                        let cells = line.split('|').map(s => s.trim()).filter((s, idx, arr) => idx > 0 && idx < arr.length - 1);
                        tableRows.push(cells);
                    }
                    continue;
                }
                
                if (line === '') {
                    if (inList) { html += '</ul>'; inList = false; }
                    if (inTable) { html += renderHTMLTable(tableHeaders, tableRows); inTable = false; tableHeaders = []; tableRows = []; }
                    continue;
                }
                
                if (inList) { html += '</ul>'; inList = false; }
                if (inTable) { html += renderHTMLTable(tableHeaders, tableRows); inTable = false; tableHeaders = []; tableRows = []; }
                
                html += `<p style="font-size: 12.5px; color: var(--text-secondary); margin-bottom: 12px; line-height: 1.6;">${parseInlineMarkdown(line)}</p>`;
            }
            
            if (inList) html += '</ul>';
            if (inTable) html += renderHTMLTable(tableHeaders, tableRows);
            
            return html;
        }
        
        function parseInlineMarkdown(text) {
            text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
            text = text.replace(/\[(.*?)\]\(.*?\)/g, '$1');
            return text;
        }
        
        function renderHTMLTable(headers, rows) {
            let html = '<div class="table-container" style="margin: 15px 0;"><table class="companies-table" style="width: 100%; border-collapse: collapse; border: 1px solid var(--card-border);">';
            
            html += '<thead><tr>';
            headers.forEach(h => {
                html += `<th style="padding: 10px; font-size: 11px; text-align: left; background: var(--input-bg); border-bottom: 2px solid var(--card-border);">${parseInlineMarkdown(h)}</th>`;
            });
            html += '</tr></thead>';
            
            html += '<tbody>';
            rows.forEach(r => {
                html += '<tr style="border-bottom: 1px solid var(--card-border);">';
                r.forEach(cell => {
                    let cellStyle = 'padding: 10px; font-size: 11.5px;';
                    if (cell.includes('<strong>')) {
                        cellStyle += ' font-weight: bold;';
                    }
                    html += `<td style="${cellStyle}">${parseInlineMarkdown(cell)}</td>`;
                });
                html += '</tr>';
            });
            html += '</tbody></table></div>';
            
            return html;
        }

        window.onload = function() {
            if (companies.length === 0 && ((window.companiesData && window.companiesData.length > 0) || (typeof companiesData !== 'undefined' && companiesData.length > 0))) {
                initDashboard();
            }
        };
    