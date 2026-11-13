CONFIG_22 = {
    'AMAT': {
        'name': 'Applied Materials, Inc.',
        'sector': 'Technology / Semiconductors & Semiconductor Equipment',
        'industry': 'Semiconductor Equipment & Materials',
        'weights_scores': {'f1': 8.90, 'f2': 9.50, 'f3': 8.60, 'f4': 9.20, 'f5': 8.80, 'f6': 8.70, 'f7': 8.50, 'f8': 8.50},
        'moat_desc': 'Portafolio líder en deposición, grabado y planarización CMP con alta base instalada de servicios',
        'wacc': 8.5, 'g': 3.5,
        'competitors': [
            {'name': 'Lam Research (LRCX)', 'overlap': 'Grabado conductor y deposición dieléctrica en memoria y fundición', 'diff': 'AMAT ofrece mayor amplitud integral en deposición epitaxial, CMP e implantación iónica.', 'moat': 'Excepcional'},
            {'name': 'Tokyo Electron (TEL)', 'overlap': 'Pistas de recubrimiento (coaters/developers) y grabado de obleas', 'diff': 'AMAT domina en empaquetado avanzado heterogéneo y metrología integrada.', 'moat': 'Alto'}
        ],
        'bull_points': [
            'Liderazgo absoluto en la transición a transistores Gate-All-Around (GAA) y redes de distribución de energía trasera (Backside Power Delivery).',
            'Crecimiento secular de la división de servicios AGS (Applied Global Services), con más del 65% de ingresos bajo contratos plurianuales recurrentes.',
            'Posición privilegiada en empaquetado avanzado (Hybrid Bonding y Through-Silicon Vias) para aceleradores de inteligencia artificial.'
        ],
        'bear_points': [
            'Restricciones y controles de exportación del Departamento de Comercio de EE. UU. hacia clientes en China continental.',
            'Ciclicidad y retrasos en el gasto de capital (WFE) por parte de fabricantes de memoria DRAM/NAND y fundiciones.',
            'Competencia creciente en nodos maduros y commoditización de tecnologías convencionales de grabado.'
        ],
        'green_lines': [
            '🟢 Crecimiento de ingresos de empaquetado avanzado y GAA > 25% YoY.',
            '🟢 Sostenimiento del margen operativo por encima del 29.5%.'
        ],
        'red_lines': [
            '🔴 Endurecimiento adicional de sanciones a China que afecte a más del 15% de la facturación.',
            '🔴 Pérdida de cuota en litografía de empaquetado o grabado avanzado frente a Lam o TEL.'
        ]
    },
    'TDG': {
        'name': 'TransDigm Group Incorporated',
        'sector': 'Industrials / Aerospace & Defense Components',
        'industry': 'Aerospace & Defense',
        'weights_scores': {'f1': 9.60, 'f2': 7.80, 'f3': 8.80, 'f4': 9.80, 'f5': 9.20, 'f6': 9.00, 'f7': 7.50, 'f8': 9.50},
        'moat_desc': 'Monopolio en piezas aeroespaciales patentadas (sole-source) con márgenes EBITDA del 50%+',
        'wacc': 8.2, 'g': 3.0,
        'competitors': [
            {'name': 'HEICO Corporation (HEI)', 'overlap': 'Piezas de repuesto PMA para aviación comercial y defensa', 'diff': 'HEICO compite en ingeniería inversa PMA; TDG posee la propiedad intelectual original exclusiva (OEM).', 'moat': 'Excepcional'},
            {'name': 'RTX Corporation (RTX)', 'overlap': 'Sistemas de propulsión y aviónica comercial (Pratt & Whitney / Collins)', 'diff': 'RTX tiene márgenes diluidos por motores originales; TDG opera como un peaje de alto margen en componentes nicho.', 'moat': 'Alto'}
        ],
        'bull_points': [
            'Más del 90% de las ventas provienen de productos propietarios, y aproximadamente el 80% son piezas donde TDG es la única fuente aprobada por la FAA.',
            'El negocio de aftermarket aeroespacial genera márgenes EBITDA superiores al 52%, respaldado por el aumento de horas de vuelo globales.',
            'Historial insuperable de retorno de capital a accionistas mediante dividendos extraordinarios apalancados y recompras tácticas.'
        ],
        'bear_points': [
            'Estructura de balance con elevado apalancamiento financiero heredado de su estrategia de compras nicho.',
            'Escrutinio recurrente del Departamento de Defensa (DoD) sobre los márgenes en contratos militares de repuestos.',
            'Riesgo de paralización o caída abrupta en los viajes aéreos comerciales por factores geopolíticos o sanitarios.'
        ],
        'green_lines': [
            '🟢 Margen EBITDA consolidado sostenido por encima del 51.5%.',
            '🟢 Crecimiento orgánico de ingresos de aftermarket comercial > 12% YoY.'
        ],
        'red_lines': [
            '🔴 Reformas regulatorias federales que limiten el pricing en piezas militares no estándar.',
            '🔴 Coste del servicio de la deuda superando el 35% del EBITDA operativo.'
        ]
    },
    'NU': {
        'name': 'Nu Holdings Ltd.',
        'sector': 'Financials / Digital Banking & Fintech',
        'industry': 'Banks - Regional / Digital Banking',
        'weights_scores': {'f1': 9.00, 'f2': 9.20, 'f3': 9.40, 'f4': 8.90, 'f5': 8.80, 'f6': 9.30, 'f7': 8.80, 'f8': 8.40},
        'moat_desc': 'Plataforma bancaria digital líder en América Latina con coste de servicio ultra-bajo ($0.90/mes)',
        'wacc': 10.5, 'g': 4.0,
        'competitors': [
            {'name': 'Itaú Unibanco (ITUB)', 'overlap': 'Banca minorista, tarjetas de crédito y préstamos en Brasil', 'diff': 'Itaú soporta una costosa red de sucursales físicas; Nu opera 100% en la nube con un coste operativo 85% inferior.', 'moat': 'Alto'},
            {'name': 'MercadoLibre / Mercado Pago (MELI)', 'overlap': 'Cuentas digitales, billetera electrónica y créditos de consumo en LatAm', 'diff': 'Nu posee licencia bancaria completa, captando depósitos minoristas a coste significativamente más bajo.', 'moat': 'Alto'}
        ],
        'bull_points': [
            'Superación del umbral de 105 millones de clientes activos en Brasil, México y Colombia con ARPAC (ingreso promedio por cliente activo) en continua expansión.',
            'Eficiencia de escala sobresaliente con ratio de eficiencia por debajo del 32% y ROE consolidado superando el 28%.',
            'Aceleración del crecimiento de captación de depósitos en México tras la oferta de rendimiento atractivo, reduciendo drásticamente el coste de fondeo.'
        ],
        'bear_points': [
            'Riesgo macroeconómico de morosidad y deterioro crediticio en el ciclo de consumo minorista brasileño y mexicano.',
            'Volatilidad de los tipos de cambio en América Latina frente al dólar estadounidense.',
            'Competencia agresiva de bancos tradicionales invirtiendo masivamente en sus propias aplicaciones móviles.'
        ],
        'green_lines': [
            '🟢 ROE sostenido por encima del 25% y ratio de morosidad (NPL 90+) estabilizado en niveles saludables.',
            '🟢 Adición neta de clientes en México superior a 1.2M por trimestre con depósitos en aceleración.'
        ],
        'red_lines': [
            '🔴 NPL 90+ disparándose por encima del 7.5% sin la debida cobertura de provisiones.',
            '🔴 Estancamiento del ARPAC por debajo de $10 USD mensuales en clientes maduros.'
        ]
    },
    'QLYS': {
        'name': 'Qualys, Inc.',
        'sector': 'Technology / Software, Cybersecurity & Vulnerability Management',
        'industry': 'Software - Infrastructure',
        'weights_scores': {'f1': 9.20, 'f2': 9.60, 'f3': 8.20, 'f4': 8.70, 'f5': 8.50, 'f6': 8.50, 'f7': 8.00, 'f8': 9.00},
        'moat_desc': 'Agente universal de nube instalado en millones de endpoints con altos costes de cambio',
        'wacc': 8.5, 'g': 3.0,
        'competitors': [
            {'name': 'Tenable Holdings (TENB)', 'overlap': 'Gestión de vulnerabilidades y exposición de superficies de ataque', 'diff': 'Qualys ofrece una arquitectura de nube pura con agente multifuncional y márgenes operativos superiores al 40%.', 'moat': 'Alto'},
            {'name': 'Rapid7 (RPD)', 'overlap': 'Detección de vulnerabilidades y servicios de seguridad gestionada', 'diff': 'Qualys cuenta con balance libre de deuda y mayor rentabilidad FCF estructural.', 'moat': 'Medio'}
        ],
        'bull_points': [
            'Margen EBITDA superior al 45% y conversión de flujo de caja libre de más del 35% de los ingresos.',
            'Qualys Cloud Agent instalado en millones de dispositivos, facilitando la venta cruzada de parches automáticos y seguridad cloud.',
            'Balance inmaculado con caja neta y sin endeudamiento financiero.'
        ],
        'bear_points': [
            'Desaceleración del crecimiento de ingresos hacia dígitos simples altos debido a mayor escrutinio presupuestario en TI.',
            'Competencia de plataformas de ciberseguridad integradas como CrowdStrike y Palo Alto Networks consolidando herramientas.',
            'Menor exposición a la seguridad de identidad y detección activa de amenazas en tiempo real.'
        ],
        'green_lines': [
            '🟢 Tasa de retención neta (NRR) estabilizada por encima del 106%.',
            '🟢 FCF Yield sostenido superior al 4.5% con recompra de acciones.'
        ],
        'red_lines': [
            '🔴 Pérdida de clientes empresariales estratégicos frente a suites consolidadas de ciberseguridad.',
            '🔴 Caída del crecimiento de ingresos por debajo del +6% YoY.'
        ]
    },
    'CEG': {
        'name': 'Constellation Energy Corp.',
        'sector': 'Utilities / Independent Clean Power Generation',
        'industry': 'Utilities - Independent Power Producers',
        'weights_scores': {'f1': 8.50, 'f2': 8.50, 'f3': 9.00, 'f4': 9.30, 'f5': 8.60, 'f6': 8.60, 'f7': 8.20, 'f8': 8.80},
        'moat_desc': 'Mayor flota nuclear de EE. UU., proveedor indispensable de energía limpia 24/7 para centros de datos de IA',
        'wacc': 7.8, 'g': 2.8,
        'competitors': [
            {'name': 'Vistra Corp (VST)', 'overlap': 'Generación de energía nuclear, gas y comercialización mayorista en EE. UU.', 'diff': 'CEG posee la mayor flota nuclear no emisora de carbono de la nación con menor exposición al carbón/gas fósil.', 'moat': 'Excepcional'},
            {'name': 'NRG Energy (NRG)', 'overlap': 'Suministro y generación minorista y mayorista de electricidad', 'diff': 'NRG está más orientada al retail y gas natural; CEG domina la capacidad nuclear de carga base para hyperscalers.', 'moat': 'Medio'}
        ],
        'bull_points': [
            'Contrato histórico de 20 años con Microsoft para reiniciar la central de Three Mile Island (Crane Clean Energy Center), validando primas masivas por energía nuclear limpia 24/7.',
            'Demanda exponencial de energía continua e ininterrumpida por parte de centros de datos de entrenamiento e inferencia de IA.',
            'Créditos fiscales del Acta de Reducción de la Inflación (IRA) que fijan un suelo de rentabilidad garantizado para la generación nuclear.'
        ],
        'bear_points': [
            'Riesgo regulatorio y de rechazo de la FERC a acuerdos de coinserción física (co-location) directa tras la resolución de Talen Energy.',
            'Sensibilidad a los precios mayoristas de la energía eléctrica en los mercados PJM y ERCOT.',
            'Costes y plazos complejos asociados a la reactivación y extensión de licencias nucleares.'
        ],
        'green_lines': [
            '🟢 Cierre de nuevos contratos bilaterales PPA a largo plazo con hyperscalers a tarifas fijas superiores a $100/MWh.',
            '🟢 Aprobación regulatoria de interconexión para centros de datos adyacentes a plantas nucleares.'
        ],
        'red_lines': [
            '🔴 Intervención de la FERC prohibiendo de forma generalizada la conexión directa de centros de datos a generadores nucleares.',
            '🔴 Incidentes operativos o paradas imprevistas prolongadas en reactores nucleares principales.'
        ]
    },
    'TTWO': {
        'name': 'Take-Two Interactive Software',
        'sector': 'Communication Services / Interactive Home Entertainment',
        'industry': 'Electronic Gaming & Multimedia',
        'weights_scores': {'f1': 8.20, 'f2': 8.20, 'f3': 9.20, 'f4': 9.40, 'f5': 8.20, 'f6': 8.50, 'f7': 8.60, 'f8': 8.00},
        'moat_desc': 'Propiedad intelectual insustituible (Grand Theft Auto, Red Dead, NBA 2K) con poder cultural global',
        'wacc': 8.8, 'g': 3.2,
        'competitors': [
            {'name': 'Electronic Arts (EA)', 'overlap': 'Franquicias deportivas (EA Sports FC, Madden) y juegos de acción/simulación', 'diff': 'EA depende de licencias anuales de ligas; Take-Two es dueña del fenómeno cultural más lucrativo de la historia (GTA).', 'moat': 'Excepcional'},
            {'name': 'Sony Interactive Entertainment (SONY)', 'overlap': 'Distribución de videojuegos de gran presupuesto (AAA) y plataformas', 'diff': 'Take-Two es desarrollador multiplataforma capaz de maximizar ingresos en consolas, PC y servicios de suscripción.', 'moat': 'Alto'}
        ],
        'bull_points': [
            'El inminente lanzamiento global de Grand Theft Auto VI (GTA VI) representa el catalizador de ingresos más grande en la historia de la industria del entretenimiento.',
            'Capacidad demostrada para monetizar ecosistemas de servicio en vivo durante más de una década (GTA Online ha generado miles de millones).',
            'Sinergias de distribución móvil a través de Zynga para expandir marcas clave en plataformas portátiles.'
        ],
        'bear_points': [
            'Riesgo de retrasos adicionales en la fecha definitiva de estreno de GTA VI.',
            'Elevados costes de desarrollo y marketing que comprimen el flujo de caja a corto plazo antes de la ventana de lanzamiento.',
            'Comportamiento de consumo discrecional más prudente en títulos móviles de Zynga.'
        ],
        'green_lines': [
            '🟢 Confirmación oficial de lanzamiento de GTA VI sin retrasos y reservas récord en preventa.',
            '🟢 Crecimiento recurrente del gasto de los jugadores (RCS) en NBA 2K y GTA Online superior al 10% YoY.'
        ],
        'red_lines': [
            '🔴 Postergación imprevista del lanzamiento de GTA VI más allá del año fiscal 2026.',
            '🔴 Fuerte contracción del gasto de usuarios en monetización móvil de Zynga.'
        ]
    },
    'KKR': {
        'name': 'KKR & Co. Inc.',
        'sector': 'Financials / Asset Management & Private Equity',
        'industry': 'Asset Management',
        'weights_scores': {'f1': 8.60, 'f2': 8.80, 'f3': 8.80, 'f4': 9.10, 'f5': 9.00, 'f6': 9.00, 'f7': 8.30, 'f8': 8.80},
        'moat_desc': 'Gestora de activos alternativos de prestigio mundial con capital bloqueado a largo plazo',
        'wacc': 9.0, 'g': 3.5,
        'competitors': [
            {'name': 'Blackstone Inc. (BX)', 'overlap': 'Inversión alternativa en capital privado, inmobiliario, crédito e infraestructura', 'diff': 'KKR tiene una ventaja estratégica en crédito privado y el control de Global Atlantic en seguros de vida.', 'moat': 'Excepcional'},
            {'name': 'Apollo Global Management (APO)', 'overlap': 'Crédito privado, gestión de capital de jubilación y deuda corporativa', 'diff': 'KKR mantiene una distribución más diversificada entre capital privado tradicional, infraestructura y seguros.', 'moat': 'Excepcional'}
        ],
        'bull_points': [
            'Integración de Global Atlantic aportando flujos masivos de capital de anualidades y seguros de carácter perpetuo.',
            'Crecimiento exponencial de las comisiones de gestión vinculadas a tarifas (Fee-Related Earnings - FRE) superior al 20% anual.',
            'Penetración agresiva en el canal patrimonial minorista y cuentas de jubilación privadas (401k).'
        ],
        'bear_points': [
            'Periodos de congelación o menores desinversiones (exits) en el mercado de capital privado afectando a los carried interest.',
            'Riesgo crediticio en la cartera de préstamos directos corporativos ante tipos de interés elevados.',
            'Volatilidad de los beneficios contables GAAP respecto a los beneficios distribuibles operativos.'
        ],
        'green_lines': [
            '🟢 Crecimiento del FRE superior al 20% YoY con captaciones de capital neto de más de $25B por trimestre.',
            '🟢 Expansión de activos bajo gestión (AUM) perpetuos o a largo plazo superando el 50% del total.'
        ],
        'red_lines': [
            '🔴 Aumento severo de impagos en la cartera de crédito directo no garantizado.',
            '🔴 Caída abrupta en el ritmo de recaudación de fondos institucionales.'
        ]
    },
    'NOVT': {
        'name': 'Novanta Inc.',
        'sector': 'Technology / Precision Photonics & Motion Control',
        'industry': 'Electronic Components',
        'weights_scores': {'f1': 8.40, 'f2': 8.80, 'f3': 8.20, 'f4': 8.50, 'f5': 8.30, 'f6': 8.40, 'f7': 8.10, 'f8': 8.30},
        'moat_desc': 'Componentes fotónicos y mecatrónicos de precisión embebidos en equipos médicos y robóticos con aprobación FDA',
        'wacc': 8.5, 'g': 3.0,
        'competitors': [
            {'name': 'Cognex Corporation (CGNX)', 'overlap': 'Sistemas de visión artificial y sensores industriales', 'diff': 'Novanta está fuertemente orientada a aplicaciones quirúrgicas y dispositivos médicos críticos de alta regulación.', 'moat': 'Alto'},
            {'name': 'MKS Instruments (MKSI)', 'overlap': 'Subsistemas de precisión para semiconductores y láseres industriales', 'diff': 'Novanta mantiene un balance mucho menos endeudado y mayor exposición al sector médico secular.', 'moat': 'Alto'}
        ],
        'bull_points': [
            'Componentes críticos integrados en sistemas de cirugía robótica y equipos de diagnóstico médico con ciclos de vida de 7 a 10 años.',
            'Elevados costes de sustitución debidos a la necesidad de recertificación ante la FDA si el fabricante OEM altera el proveedor.',
            'Exposición al crecimiento secular de la automatización industrial de alta precisión y microprocesamiento láser.'
        ],
        'bear_points': [
            'Riesgo de aplazamiento en pedidos de fabricantes OEM ante acumulación temporal de inventarios.',
            'Dependencia del ritmo de adopción comercial de nuevas plataformas quirúrgicas robóticas.',
            'Sensibilidad al gasto de capital industrial en los mercados europeo y asiático.'
        ],
        'green_lines': [
            '🟢 Ganancias de diseño de nuevos productos (Design Wins) superando los $100M anuales.',
            '🟢 Margen operativo ajustado en expansión hacia el 22%.'
        ],
        'red_lines': [
            '🔴 Desaceleración de ingresos orgánicos en la división médica por debajo del 0%.',
            '🔴 Pérdida de un contrato OEM estratégico en robótica médica.'
        ]
    },
    'NRG': {
        'name': 'NRG Energy, Inc.',
        'sector': 'Utilities / Retail Electricity & Smart Home Services',
        'industry': 'Utilities - Independent Power Producers',
        'weights_scores': {'f1': 8.20, 'f2': 7.80, 'f3': 8.00, 'f4': 7.90, 'f5': 8.10, 'f6': 8.00, 'f7': 7.60, 'f8': 7.80},
        'moat_desc': 'Escala masiva en suministro minorista de energía en Texas y servicios para el hogar inteligente (Vivint)',
        'wacc': 7.5, 'g': 2.0,
        'competitors': [
            {'name': 'Constellation Energy (CEG)', 'overlap': 'Venta mayorista y minorista de energía en mercados desregulados', 'diff': 'NRG centra su estrategia en el cliente residencial y servicios integrados del hogar (Vivint Smart Home).', 'moat': 'Medio'},
            {'name': 'Vistra Corp (VST)', 'overlap': 'Generación eléctrica y comercialización minorista en ERCOT y PJM', 'diff': 'Vistra cuenta con mayor cuota en nuclear y baterías; NRG posee mayor densidad minorista residencial.', 'moat': 'Medio'}
        ],
        'bull_points': [
            'Fuerte generación de flujo de caja libre respaldada por la demanda creciente de electricidad en Texas (ERCOT).',
            'Capacidad de venta cruzada de servicios de seguridad y automatización residencial a través de la plataforma Vivint.',
            'Retorno masivo de capital a accionistas vía recompras aceleradas de acciones y dividendos crecientes.'
        ],
        'bear_points': [
            'Volatilidad extrema ante eventos climáticos adversos en la red eléctrica de Texas.',
            'Endeudamiento financiero contraído para la adquisición de Vivint que requiere disciplina de desapalancamiento.',
            'Competencia feroz en tarifas minoristas de electricidad con bajas barreras de cambio para el consumidor.'
        ],
        'green_lines': [
            '🟢 Generación de FCF superior a $1.8B anuales con ratio Deuda/EBITDA descendiendo de 2.8x.',
            '🟢 Crecimiento neto de clientes de Vivint Smart Home superando el 5% anual.'
        ],
        'red_lines': [
            '🔴 Pérdidas operativas por picos de precios de energía mayorista en ERCOT durante tormentas invernales/veraniegas.',
            '🔴 Incumplimiento del plan de reducción de deuda corporativa.'
        ]
    },
    'HRB': {
        'name': 'H&R Block, Inc.',
        'sector': 'Consumer Cyclical / Personal Tax Preparation & Financial Services',
        'industry': 'Personal Services',
        'weights_scores': {'f1': 8.60, 'f2': 8.00, 'f3': 7.60, 'f4': 8.50, 'f5': 8.60, 'f6': 8.20, 'f7': 7.20, 'f8': 8.20},
        'moat_desc': 'Red nacional inigualable de oficinas y confianza de marca en preparación de impuestos asistida',
        'wacc': 8.0, 'g': 2.0,
        'competitors': [
            {'name': 'Intuit Inc. (INTU)', 'overlap': 'Preparación de declaraciones de impuestos DIY (TurboTax) y asistencia profesional', 'diff': 'HRB mantiene una ventaja de confianza y proximidad física con más de 9,000 sucursales para perfiles fiscales complejos.', 'moat': 'Alto'},
            {'name': 'Jackson Hewitt Tax Service', 'overlap': 'Servicios asistidos de preparación fiscal minorista en centros comerciales', 'diff': 'HRB posee una escala tres veces superior y una plataforma digital propietaria sólida.', 'moat': 'Medio'}
        ],
        'bull_points': [
            'Generación predecible de flujo de caja libre gracias al mandato legal federal ineludible de presentar impuestos anualmente.',
            'Poder de fijación de precios moderado pero consistente con subidas tarifarias del 4-6% anual.',
            'Política de asignación de capital formidable: ha recomprado y retirado más del 35% de sus acciones en circulación en la última década.'
        ],
        'bear_points': [
            'Iniciativa del IRS de lanzar su propia plataforma de declaración directa y gratuita (Direct File).',
            'Migración estructural paulatina de clientes desde el canal asistido presencial hacia herramientas digitales autónomas.',
            'Negocio fuertemente estacional concentrado en el primer trimestre del año natural (Q4 fiscal).'
        ],
        'green_lines': [
            '🟢 Crecimiento continuado del ingreso medio por declaración (Net Average Charge) > 4%.',
            '🟢 Recompra anual de al menos el 5-7% de las acciones en circulación a múltiplos atractivos.'
        ],
        'red_lines': [
            '🔴 Adopción masiva de la herramienta Direct File del IRS que erosione cuota de mercado asistida.',
            '🔴 Caída continuada en el volumen total de declaraciones procesadas en oficinas presenciales.'
        ]
    },
    'YETI': {
        'name': 'YETI Holdings, Inc.',
        'sector': 'Consumer Cyclical / Premium Outdoor & Drinkware Equipment',
        'industry': 'Leisure',
        'weights_scores': {'f1': 8.50, 'f2': 9.20, 'f3': 7.80, 'f4': 8.50, 'f5': 8.30, 'f6': 8.30, 'f7': 7.50, 'f8': 7.80},
        'moat_desc': 'Marca de culto con poder de fijación de precios en neveras portátiles y recipientes térmicos premium',
        'wacc': 8.8, 'g': 2.8,
        'competitors': [
            {'name': 'Stanley (PMI Worldwide)', 'overlap': 'Recipientes térmicos de hidratación, vasos y termos de viaje', 'diff': 'YETI goza de una reputación inquebrantable de durabilidad extrema y ecosistema completo de aventuras outdoor.', 'moat': 'Alto'},
            {'name': 'Hydro Flask (Helen of Troy - HELE)', 'overlap': 'Botellas aisladas y equipamiento para actividades al aire libre', 'diff': 'YETI ostenta un margen bruto superior (>57%) y mayor penetración en el canal Direct-to-Consumer (DTC).', 'moat': 'Medio'}
        ],
        'bull_points': [
            'Margen bruto sobresaliente del 57-58%, respaldado por el poder de marca y la venta directa al consumidor (DTC).',
            'Expansión internacional en Europa, Australia y Japón creciendo a tasas superiores al 25% YoY.',
            'Balance sólido con posición neta de caja, permitiendo recompras de acciones y adquisiciones selectivas de marcas de aventuras.'
        ],
        'bear_points': [
            'Sensibilidad al gasto discrecional del consumidor en artículos no esenciales de alto precio.',
            'Modas virales efímeras en recipientes de hidratación (como el fenómeno Stanley Cup) que restan atención al producto base.',
            'Dependencia del mercado estadounidense para más del 80% de los ingresos totales.'
        ],
        'green_lines': [
            '🟢 Crecimiento de ingresos internacionales superior al 20% anual.',
            '🟢 Margen bruto consolidado por encima del 57%.'
        ],
        'red_lines': [
            '🔴 Descuentos comerciales generalizados para mover inventario en cadenas mayoristas.',
            '🔴 Caída de ventas de la división Coolers & Equipment por encima del 10% YoY.'
        ]
    },
    'GIB': {
        'name': 'CGI Inc.',
        'sector': 'Technology / IT Consulting & Outsourcing Services',
        'industry': 'Information Technology Services',
        'weights_scores': {'f1': 8.40, 'f2': 9.00, 'f3': 7.90, 'f4': 8.30, 'f5': 8.50, 'f6': 8.60, 'f7': 7.70, 'f8': 8.80},
        'moat_desc': 'Relaciones contractuales plurianuales con gobiernos y grandes bancos con costes de cambio críticos',
        'wacc': 8.2, 'g': 2.5,
        'competitors': [
            {'name': 'Accenture plc (ACN)', 'overlap': 'Consultoría estratégica, transformación digital e integración de sistemas', 'diff': 'CGI enfoca su modelo en externalización de procesos de TI a largo plazo con menor rotación de personal y contratos defensivos.', 'moat': 'Alto'},
            {'name': 'Infosys Limited (INFY)', 'overlap': 'Servicios globales de desarrollo de software y mantenimiento de aplicaciones', 'diff': 'CGI cuenta con una presencia de proximidad local ("metro market model") con habilitación de seguridad militar y gubernamental.', 'moat': 'Alto'}
        ],
        'bull_points': [
            'Cartera de pedidos firmada (Backlog) superior a los $28.000M CAD, otorgando una visibilidad de ingresos de más de 2 años.',
            'Margen EBITA estable en el entorno del 15.5-16.5% con una conversión de flujo de caja libre casi idéntica al beneficio neto.',
            'Estrategia probada "Build & Buy" adquiriendo pequeñas consultoras rentables con múltiplos disciplinados.'
        ],
        'bear_points': [
            'Ralentización de proyectos discrecionales de consultoría digital ante la cautela presupuestaria empresarial.',
            'Presión salarial en perfiles especializados en inteligencia artificial y ciberseguridad.',
            'Bajo crecimiento orgánico histórico en periodos de incertidumbre económica.'
        ],
        'green_lines': [
            '🟢 Ratio Book-to-Bill sostenido por encima de 1.05x de forma continuada.',
            '🟢 Margen EBITA ajustado superior al 16.0%.'
        ],
        'red_lines': [
            '🔴 Book-to-Bill cayendo por debajo de 0.92x durante dos trimestres consecutivos.',
            '🔴 Cancelación anticipada de grandes contratos gubernamentales en Norteamérica o Europa.'
        ]
    },
    'TTEK': {
        'name': 'Tetra Tech, Inc.',
        'sector': 'Industrials / Environmental Engineering & Consulting Services',
        'industry': 'Engineering & Construction',
        'weights_scores': {'f1': 8.30, 'f2': 8.80, 'f3': 8.50, 'f4': 8.40, 'f5': 8.30, 'f6': 8.50, 'f7': 8.00, 'f8': 8.50},
        'moat_desc': 'Liderazgo mundial número 1 en consultoría e ingeniería del agua, remediación de PFAS y resiliencia climática',
        'wacc': 8.2, 'g': 2.8,
        'competitors': [
            {'name': 'Jacobs Solutions (J)', 'overlap': 'Servicios de ingeniería, infraestructura y soluciones ambientales avanzadas', 'diff': 'Tetra Tech opera como consultora pura de ingeniería ambiental de alto margen, sin riesgos de construcción a precio fijo.', 'moat': 'Alto'},
            {'name': 'AECOM (ACM)', 'overlap': 'Diseño y gestión de infraestructura de transporte, agua y edificios sostenibles', 'diff': 'Tetra Tech mantiene el puesto #1 del ranking ENR en tratamiento y gestión de recursos hídricos.', 'moat': 'Alto'}
        ],
        'bull_points': [
            'Beneficiario directo de los fondos federales de la Ley de Infraestructura de EE. UU. (IIJA) y las nuevas normativas estrictas de la EPA sobre PFAS ("químicos eternos").',
            'Modelo de negocio de bajo riesgo: consultoría técnica "Cost-Plus" y servicios profesionales que evitan contratos EPC con sobrecostes.',
            'Historial intachable de crecimiento compuesto de ingresos y dividendos durante más de una década.'
        ],
        'bear_points': [
            'Dependencia de la asignación y desembolso efectivo de presupuestos de agencias gubernamentales estadounidenses (DoD, EPA, USAID).',
            'Posibles retrasos en licitaciones públicas ante ciclos electorales o disputas de techo de deuda en Washington.',
            'Riesgo de integración en adquisiciones internacionales de gran tamaño (como RPS Group).'
        ],
        'green_lines': [
            '🟢 Cartera de pedidos (Backlog) marcando nuevos máximos históricos con crecimiento orgánico > 8%.',
            '🟢 Margen operativo ajustado expandiéndose hacia el 13.5%.'
        ],
        'red_lines': [
            '🔴 Recorte presupuestario federal que paralice los programas de remediación de PFAS.',
            '🔴 Pérdida de certificaciones preferentes con el Cuerpo de Ingenieros del Ejército de EE. UU.'
        ]
    },
    'CTVA': {
        'name': 'Corteva, Inc.',
        'sector': 'Basic Materials / Agricultural Seeds & Crop Protection',
        'industry': 'Agricultural Inputs',
        'weights_scores': {'f1': 8.30, 'f2': 8.70, 'f3': 8.00, 'f4': 8.80, 'f5': 8.30, 'f6': 8.30, 'f7': 8.00, 'f8': 8.00},
        'moat_desc': 'Duopolio global en genética de semillas de maíz/soja (marca Pioneer) y patentes de protección de cultivos',
        'wacc': 8.0, 'g': 2.5,
        'competitors': [
            {'name': 'Bayer Crop Science (BAYN)', 'overlap': 'Semillas transgénicas y agroquímicos de protección vegetal', 'diff': 'Corteva opera libre de pasivos por litigios masivos de glifosato heredados, con mayor impulso en semillas Enlist E3.', 'moat': 'Excepcional'},
            {'name': 'FMC Corporation (FMC)', 'overlap': 'Insecticidas, herbicidas y soluciones sintéticas de protección de cultivos', 'diff': 'Corteva combina protección química con una de las carteras de germoplasma y semillas más ricas del planeta.', 'moat': 'Alto'}
        ],
        'bull_points': [
            'Liderazgo incontestable en semillas con la tecnología Enlist E3, captando cuota de mercado en soja en Norteamérica frente a Xtend de Bayer.',
            'Transformación del mix de ingresos hacia productos propietarios de mayor margen y aumento de cobro de regalías tecnológicas.',
            'Aceleración de soluciones biológicas para agricultura sostenible con márgenes brutos superiores.'
        ],
        'bear_points': [
            'Ciclicidad de las materias primas agrícolas (precios de maíz y soja) reduciendo el poder adquisitivo de los agricultores.',
            'Desestocaje de inventarios de productos genéricos de protección de cultivos en canales de distribución.',
            'Condiciones climáticas desfavorables o sequías prolongadas en zonas agrícolas clave de América.'
        ],
        'green_lines': [
            '🟢 Penetración de la tecnología Enlist E3 superando el 65% de la superficie de soja en EE. UU.',
            '🟢 Margen EBITDA operativo en expansión hacia el 21%.'
        ],
        'red_lines': [
            '🔴 Caída acusada en los precios de los futuros agrícolas que reduzca drásticamente las intenciones de siembra.',
            '🔴 Pérdida de eficacia biológica por resistencia de malezas sin alternativas patentadas listas.'
        ]
    },
    'HIMS': {
        'name': 'Hims & Hers Health, Inc.',
        'sector': 'Healthcare / Direct-to-Consumer Telehealth & Personalized Wellness',
        'industry': 'Health Information Services',
        'weights_scores': {'f1': 7.60, 'f2': 8.80, 'f3': 8.80, 'f4': 7.20, 'f5': 7.80, 'f6': 7.90, 'f7': 8.20, 'f8': 6.80},
        'moat_desc': 'Plataforma directa al consumidor de suscripción en salud y bienestar con formulaciones personalizadas',
        'wacc': 9.5, 'g': 3.5,
        'competitors': [
            {'name': 'Teladoc Health (TDOC)', 'overlap': 'Servicios de telemedicina general y consultas virtuales corporativas', 'diff': 'Hims vende suscripciones directas al consumidor de tratamientos de marca propia con márgenes brutos del 80%.', 'moat': 'Bajo'},
            {'name': 'Ro (Roman Health)', 'overlap': 'Salud masculina, pérdida de peso, dermatología y farmacia digital', 'diff': 'Hims cotiza en bolsa con escala superior, mayor notoriedad de marca y rentabilidad positiva probada.', 'moat': 'Medio'}
        ],
        'bull_points': [
            'Crecimiento exponencial de suscriptores superando los 2.0 millones con una tasa de retención elevada.',
            'Márgenes brutos extraordinarios del 79-81% respaldados por la dispensación de formulaciones compuestas personalizadas.',
            'Expansión hacia tratamientos para el control de peso (GLP-1), salud cardiovascular y dermatología especializada.'
        ],
        'bear_points': [
            'Riesgo regulatorio inminente de la FDA sobre la preparación magistral (compounding) de GLP-1 (semaglutida) una vez resuelta la escasez oficial.',
            'Elevadísimo gasto de adquisición de clientes (CAC) en publicidad en redes sociales que comprime el margen neto.',
            'Bajas barreras de entrada para rivales en tratamientos genéricos de pérdida de cabello y salud sexual.'
        ],
        'green_lines': [
            '🟢 Diversificación de ingresos donde las categorías no-GLP-1 crezcan a más del 30% YoY.',
            '🟢 Tasa de conversión a suscripciones personalizadas ("Hers" y tratamientos a medida) superando el 50%.'
        ],
        'red_lines': [
            '🔴 Acción regulatoria formal de la FDA prohibiendo de inmediato la distribución de semaglutida compuesta.',
            '🔴 Disparo del ratio CAC/LTV que torne negativo el flujo de caja libre.'
        ]
    },
    'INMD': {
        'name': 'InMode Ltd.',
        'sector': 'Healthcare / Medical Aesthetic Devices & Technology',
        'industry': 'Medical Devices',
        'weights_scores': {'f1': 8.50, 'f2': 9.60, 'f3': 7.00, 'f4': 7.80, 'f5': 7.80, 'f6': 7.80, 'f7': 7.20, 'f8': 7.00},
        'moat_desc': 'Tecnología patentada de radiofrecuencia mínimamente invasiva (RFAL) para remodelación estética y facial',
        'wacc': 9.2, 'g': 2.5,
        'competitors': [
            {'name': 'Cutera, Inc. (CUTR)', 'overlap': 'Sistemas láser y energía para estética médica dermatológica', 'diff': 'InMode genera márgenes brutos del 80%+ y sostiene una tesorería neta gigantesca, mientras Cutera acumula pérdidas.', 'moat': 'Medio'},
            {'name': 'Sisram Medical / Alma Lasers', 'overlap': 'Dispositivos de estética corporal, reducción de grasa y rejuvenecimiento', 'diff': 'InMode posee la propiedad intelectual original sobre radiofrecuencia bipolar subdérmica mínimamente invasiva.', 'moat': 'Medio'}
        ],
        'bull_points': [
            'Posición financiera hiperdefensiva: más de $700M en efectivo y equivalentes sin deuda bancaria, cubriendo más del 60% de su valor bursátil.',
            'Márgenes brutos estables por encima del 80% gracias a la venta recurrente de consumibles y piezas de mano.',
            'Liderazgo clínico reconocido por cirujanos plásticos en procedimientos de lipólisis por radiofrecuencia (FaceTite, BodyTite).'
        ],
        'bear_points': [
            'Debilidad en la venta de plataformas de capital médico debido a los altos tipos de interés que encarecen el leasing a los médicos.',
            'Presión geopolítica y logística derivada de la localización de su sede e instalaciones en Israel.',
            'Ralentización del consumo discrecional en procedimientos cosméticos no cubiertos por seguros de salud.'
        ],
        'green_lines': [
            '🟢 Recuperación de las ventas de plataformas en EE. UU. ante bajadas de tipos de interés de la Fed.',
            '🟢 Aceleración del peso de consumibles y servicios recurrentes superando el 22% de la facturación.'
        ],
        'red_lines': [
            '🔴 Disrupción física o logística severa en centros de producción en Oriente Medio.',
            '🔴 Destrucción de valor por adquisiciones corporativas mal estructuradas con el exceso de caja.'
        ]
    },
    'APPS': {
        'name': 'Digital Turbine, Inc.',
        'sector': 'Technology / Mobile Advertising & On-Device App Delivery',
        'industry': 'Software - Application',
        'weights_scores': {'f1': 7.20, 'f2': 7.50, 'f3': 7.40, 'f4': 7.50, 'f5': 7.20, 'f6': 7.40, 'f7': 7.80, 'f8': 6.90},
        'moat_desc': 'Software SingleTap integrado a nivel de firmware en operadores de telefonía móvil (Verizon, AT&T)',
        'wacc': 9.8, 'g': 2.5,
        'competitors': [
            {'name': 'AppLovin Corporation (APP)', 'overlap': 'Monetización y distribución de aplicaciones móviles y publicidad programática', 'diff': 'AppLovin lidera en motores de subasta y juegos con IA (AXON); Digital Turbine opera a nivel de dispositivo y operador.', 'moat': 'Alto'},
            {'name': 'Unity Software (U)', 'overlap': 'Monetización publicitaria dentro de juegos móviles y motores de desarrollo', 'diff': 'Digital Turbine instala aplicaciones directamente en el momento de activación del smartphone (Out-of-the-Box).', 'moat': 'Medio'}
        ],
        'bull_points': [
            'Opcionalidad estratégica masiva derivada de la Ley de Mercados Digitales de la UE (DMA), que obliga a abrir tiendas de apps alternativas.',
            'Tecnología propietaria SingleTap que permite descargar e instalar apps con un solo clic fuera de Google Play.',
            'Priorización absoluta del desapalancamiento financiero para reducir el coste de la deuda.'
        ],
        'bear_points': [
            'Alargamiento del ciclo de sustitución de smartphones a nivel global, reduciendo el volumen de nuevos dispositivos activados.',
            'Dependencia extrema de acuerdos de reparto de ingresos con operadores de telecomunicaciones estadounidenses.',
            'Presión competitiva y de márgenes en el segmento de publicidad programática abierta.'
        ],
        'green_lines': [
            '🟢 Cierre de acuerdos con grandes desarrolladores (ej. Epic Games) para desplegar tiendas de apps mediante SingleTap.',
            '🟢 Generación de FCF positivo trimestral sostenido para amortizar deuda sénior.'
        ],
        'red_lines': [
            '🔴 Pérdida o renegociación a la baja de un contrato de operador Tier-1 en EE. UU.',
            '🔴 Incumplimiento de covenants de deuda por deterioro del EBITDA operativo.'
        ]
    },
    'OR': {
        'name': 'Ormat Technologies, Inc.',
        'sector': 'Utilities / Geothermal & Renewable Energy Storage',
        'industry': 'Utilities - Renewable',
        'weights_scores': {'f1': 7.80, 'f2': 7.70, 'f3': 7.80, 'f4': 8.20, 'f5': 7.60, 'f6': 7.90, 'f7': 7.60, 'f8': 8.20},
        'moat_desc': 'Líder vertical en exploración geotérmica, fabricación de turbinas de ciclo binario (OEC) y contratos PPA regulados',
        'wacc': 7.5, 'g': 2.5,
        'competitors': [
            {'name': 'NextEra Energy Partners (NEP)', 'overlap': 'Generación y venta de energía renovable a largo plazo', 'diff': 'Ormat produce energía geotérmica de carga base (24/7 continua), mientras NextEra depende de solar y eólica intermitentes.', 'moat': 'Alto'},
            {'name': 'Brookfield Renewable Partners (BEP)', 'overlap': 'Activos hidroeléctricos y renovables de carga base continua', 'diff': 'Ormat es el fabricante líder exclusivo de sus propios equipos y turbinas de ciclo binario.', 'moat': 'Alto'}
        ],
        'bull_points': [
            'La energía geotérmica es la única renovable pura que ofrece energía de carga base continua las 24 horas del día, altamente cotizada por centros de datos.',
            'Contratos de compra de energía (PPA) a muy largo plazo (15 a 25 años) con empresas de servicios públicos de alta solvencia.',
            'Avances en sistemas geotérmicos mejorados (EGS) y expansión en almacenamiento en baterías a escala de red.'
        ],
        'bear_points': [
            'Elevada intensidad de capital y riesgo geológico exploratorio en la perforación de nuevos pozos geotérmicos.',
            'Apalancamiento financiero elevado característico del sector de infraestructuras energéticas en fases de expansión.',
            'Eventos de recursos naturales (sismicidad o agotamiento de temperatura en reservorios subterráneos).'
        ],
        'green_lines': [
            '🟢 Adición de nueva capacidad geotérmica en MW a tiempo y dentro del presupuesto de inversión.',
            '🟢 Firma de contratos PPA premium para centros de datos con tarifas superiores a la media del mercado.'
        ],
        'red_lines': [
            '🔴 Agotamiento térmico severo no previsto en alguno de sus campos geotérmicos principales (ej. Puna o McGinness Hills).',
            '🔴 Costes descontrolados en perforaciones exploratorias fallidas.'
        ]
    },
    'DOLE': {
        'name': 'Dole plc',
        'sector': 'Consumer Defensive / Agricultural Produce & Fresh Fruit Distribution',
        'industry': 'Farm Products',
        'weights_scores': {'f1': 7.00, 'f2': 7.50, 'f3': 6.80, 'f4': 7.40, 'f5': 7.20, 'f6': 7.50, 'f7': 6.50, 'f8': 7.00},
        'moat_desc': 'Infraestructura global de cadena de frío y marca icónica número 1 en plátanos y piñas frescas',
        'wacc': 7.8, 'g': 1.8,
        'competitors': [
            {'name': 'Fresh Del Monte Produce (FDP)', 'overlap': 'Cultivo, logística y comercialización de piñas, plátanos y fruta fresca', 'diff': 'Dole ostenta mayor diversificación geográfica y superior volumen en canales de distribución minorista en Europa.', 'moat': 'Medio'},
            {'name': 'Mission Produce (AVO)', 'overlap': 'Abastecimiento y distribución global de aguacates y fruta madurada', 'diff': 'Dole cuenta con una marca de consumo global mucho más reconocida entre los consumidores finales.', 'moat': 'Medio'}
        ],
        'bull_points': [
            'Marca líder mundialmente reconocida y red logística de barcos refrigerados e instalaciones portuarias insustituible.',
            'Venta estratégica de la división de verduras frescas (Fresh Vegetables) para centrarse en productos de mayor margen y menor volatilidad.',
            'Demanda alimentaria inelástica de frutas y verduras frescas de consumo cotidiano.'
        ],
        'bear_points': [
            'Márgenes netos estructuralmente delgados (2-3%) vulnerables a fluctuaciones en fletes marítimos, combustible y fertilizantes.',
            'Riesgos fitosanitarios y de plagas agrícolas (ej. hongo Fusarium raza 4 en plantaciones bananeras).',
            'Poder de negociación de las grandes cadenas de supermercados que presionan los precios al por mayor.'
        ],
        'green_lines': [
            '🟢 Margen EBITDA ajustado consolidado superando el 4.5%.',
            '🟢 Reducción continuada de la deuda neta hacia un ratio de apalancamiento inferior a 2.0x.'
        ],
        'red_lines': [
            '🔴 Aparición de enfermedades en cultivos que diezmen la producción de plátanos en Latinoamérica.',
            '🔴 Huelgas logísticas prolongadas o interrupciones en la cadena de transporte refrigerado.'
        ]
    },
    'CLFD': {
        'name': 'Clearfield, Inc.',
        'sector': 'Technology / Fiber Optic Management & Broadband Connectivity',
        'industry': 'Communication Equipment',
        'weights_scores': {'f1': 7.00, 'f2': 8.80, 'f3': 7.50, 'f4': 7.60, 'f5': 7.60, 'f6': 7.80, 'f7': 7.40, 'f8': 6.80},
        'moat_desc': 'Arquitectura patentada de casetes modulares FieldSmart para despliegues rápidos de fibra óptica hasta el hogar (FTTH)',
        'wacc': 8.8, 'g': 2.8,
        'competitors': [
            {'name': 'Corning Incorporated (GLW)', 'overlap': 'Cables y conectividad óptica para redes de telecomunicaciones', 'diff': 'Clearfield se especializa en ingeniería de gestión de fibra para operadores rurales y de comunidades medianas.', 'moat': 'Alto'},
            {'name': 'CommScope Holding (COMM)', 'overlap': 'Equipamiento de conectividad para redes fijas e inalámbricas', 'diff': 'Clearfield opera con balance libre de deuda y mayor flexibilidad de personalización técnica.', 'moat': 'Medio'}
        ],
        'bull_points': [
            'Gran catalizador pendiente: despliegue de los $42.500M del programa federal BEAD (Broadband Equity, Access, and Deployment) para fibra rural.',
            'Balance inmaculado con posición neta de tesorería y sin deuda bancaria a largo plazo.',
            'Plataforma FieldSmart reduce el tiempo de instalación y la necesidad de mano de obra especializada en el empalme de fibra.'
        ],
        'bear_points': [
            'Retrasos burocráticos continuados en la adjudicación y liberación de fondos del programa BEAD por parte de los estados.',
            'Proceso prolongado de absorción de inventarios en los almacenes de los operadores de telecomunicaciones.',
            'Concentración de clientes en operadores de banda ancha de tamaño comunitario.'
        ],
        'green_lines': [
            '🟢 Entrada masiva de pedidos vinculados a proyectos financiados por BEAD en la segunda mitad de 2026.',
            '🟢 Recuperación del margen bruto hacia niveles históricos del 38-40%.'
        ],
        'red_lines': [
            '🔴 Postergación indefinida del gasto de infraestructura de fibra por recortes regulatorios.',
            '🔴 Consumo de la caja neta por caída sostenida de ingresos trimestrales.'
        ]
    },
    'RGTI': {
        'name': 'Rigetti Computing, Inc.',
        'sector': 'Technology / Quantum Computing Hardware & Systems',
        'industry': 'Computer Hardware',
        'weights_scores': {'f1': 5.50, 'f2': 7.20, 'f3': 7.80, 'f4': 7.40, 'f5': 7.00, 'f6': 7.20, 'f7': 8.80, 'f8': 5.20},
        'moat_desc': 'Diseño y fabricación propia de procesadores cuánticos superconductores en su sala limpia Fab-1',
        'wacc': 11.5, 'g': 4.0,
        'competitors': [
            {'name': 'IonQ, Inc. (IONQ)', 'overlap': 'Computación cuántica de iones atrapados accesible vía nube', 'diff': 'Rigetti utiliza cúbits superconductores con velocidades de puerta más rápidas y compatibilidad de fabricación con silicio.', 'moat': 'Alto'},
            {'name': 'D-Wave Quantum (QBTS)', 'overlap': 'Sistemas cuánticos de recocido (annealing) y prototipos de puertas lógicas', 'diff': 'Rigetti enfoca sus esfuerzos en computación cuántica universal tolerante a fallos basada en puertas.', 'moat': 'Medio'}
        ],
        'bull_points': [
            'Propiedad de Fab-1, una de las pocas instalaciones dedicadas exclusivamente a la fabricación de chips cuánticos en el mundo.',
            'Avances en la arquitectura modular de mosaico para escalar el recuento de cúbits manteniendo alta fidelidad de puertas de dos cúbits.',
            'Contratos de colaboración con laboratorios nacionales y agencias de defensa de EE. UU. e internacionales.'
        ],
        'bear_points': [
            'Modelo de negocio pre-comercial con pérdidas operativas y quema continuada de caja (Cash Burn).',
            'Riesgo constante de dilución mediante emisiones secundarias de acciones para financiar la investigación científica.',
            'Competencia contra gigantes tecnológicos con presupuestos ilimitados (IBM, Google, Microsoft).'
        ],
        'green_lines': [
            '🟢 Demostración de fidelidad de puertas de dos cúbits superior al 99.5% en sistemas de más de 84 cúbits.',
            '🟢 Venta y entrega de sistemas cuánticos on-premise a clientes gubernamentales o académicos.'
        ],
        'red_lines': [
            '🔴 Reducción de la pista de tesorería (Cash Runway) por debajo de 12 meses sin capacidad de financiación no dilutiva.',
            '🔴 Fracaso técnico en superar los cuellos de botella de decoherencia y control criogénico.'
        ]
    },
    'ASTS': {
        'name': 'AST SpaceMobile, Inc.',
        'sector': 'Telecommunications / Satellite Cellular Broadband Direct-to-Cell',
        'industry': 'Telecom Services',
        'weights_scores': {'f1': 6.00, 'f2': 7.50, 'f3': 9.00, 'f4': 8.50, 'f5': 7.50, 'f6': 8.20, 'f7': 9.20, 'f8': 5.80},
        'moat_desc': 'Mayor constelación de antenas de matriz en fase en órbita para banda ancha celular directa a móviles estándar',
        'wacc': 11.0, 'g': 4.0,
        'competitors': [
            {'name': 'Starlink Direct to Cell (SpaceX)', 'overlap': 'Conectividad satelital directa a dispositivos móviles no modificados', 'diff': 'ASTS cuenta con satélites BlueBird de enormes dimensiones con capacidad de banda ancha real (5G/4G), voz y video.', 'moat': 'Excepcional'},
            {'name': 'Lynk Global', 'overlap': 'Tecnología satelital celular para mensajería y servicios de emergencia', 'diff': 'ASTS posee más de 3.400 patentes y el respaldo comercial directo de operadores líderes mundiales.', 'moat': 'Alto'}
        ],
        'bull_points': [
            'Alianzas estratégicas e inversiones comerciales firmadas con gigantes como AT&T, Verizon, Vodafone y Google.',
            'Despliegue exitoso de los primeros satélites comerciales BlueBird, validando la tecnología de banda ancha espacial directa.',
            'Mercado direccionable colosal: miles de millones de teléfonos inteligentes existentes sin necesidad de cambiar de terminal ni instalar software.'
        ],
        'bear_points': [
            'Intensidad extrema de capital para fabricar y lanzar la constelación completa de más de 100 satélites.',
            'Riesgo de retrasos o fallos en los lanzamientos orbitales operados por terceros.',
            'Necesidad de aprobaciones regulatorias definitivas de espectro por parte de la FCC en EE. UU. y organismos internacionales.'
        ],
        'green_lines': [
            '🟢 Despliegue comercial continuo de satélites BlueBird en órbita operativa y arranque del servicio comercial en EE. UU.',
            '🟢 Obtención de prepagos comerciales adicionales y financiación no dilutiva del gobierno de EE. UU.'
        ],
        'red_lines': [
            '🔴 Fallo catastrófico en un lanzamiento múltiple de satélites que retrase el cronograma en más de un año.',
            '🔴 Bloqueo regulatorio de la FCC que limite el uso de espectro celular terrestre para comunicaciones satelitales.'
        ]
    }
}

