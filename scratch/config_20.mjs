export const CONFIG_20 = {
  NVDA: {
    name: 'NVIDIA Corporation',
    sector: 'Technology / Semiconductors & AI Accelerated Computing',
    industry: 'Semiconductors',
    exchange: 'NASDAQ',
    weights_scores: { f1: 9.95, f2: 9.90, f3: 9.85, f4: 9.90, f5: 9.60, f6: 9.75, f7: 9.90, f8: 9.40 },
    moat_desc: 'Ecosistema propietario CUDA (>5.5M desarrolladores), interconexión NVLink/InfiniBand y liderazgo en arquitecturas Blackwell y Vera Rubin para centros de datos de IA',
    wacc: 9.0, g: 4.0,
    eps_growth_ntm_pct: 42.5,
    seg1_name: 'Data Center (Compute & Networking IA)', seg1_share: 0.929,
    seg2_name: 'Gaming, Pro Visualization & Automotive', seg2_share: 0.071,
    guidance_summary: 'La dirección proyecta ingresos para Q4 FY27 de $130,000M (±3%), con márgenes brutos GAAP y Non-GAAP de 71.0%–72.0% durante la rampa inicial de Vera Rubin, además de ampliar la autorización de recompra de acciones en $150,000M tras devolver $28,100M en los primeros nueve meses.',
    competitors: [
      {
        name: 'Advanced Micro Devices, Inc. (AMD)',
        overlap: 'Aceleradores de centros de datos para entrenamiento e inferencia de IA (serie Instinct MI325X / MI350)',
        diff: 'NVIDIA mantiene un foso de software insalvable con CUDA, librerías cuDNN/TensorRT-LLM y redes integradas Spectrum-X/NVLink a escala de rack completo (NVL72), superando el rendimiento TCO de chips aislados.',
        moat: 'Excepcional'
      },
      {
        name: 'Broadcom Inc. (AVGO) / ASICs Personalizados (Google TPU, AWS Trainium)',
        overlap: 'Silicio personalizado (XPUs/ASICs) diseñado para cargas de trabajo internas de hyperscalers',
        diff: 'La cadencia anual de arquitectura de NVIDIA (Hopper -> Blackwell -> Vera Rubin) y su flexibilidad universal para cualquier modelo fundacional evitan la obsolescencia rápida que sufren los ASICs de propósito fijo.',
        moat: 'Excepcional'
      }
    ],
    bear_points: [
      'Transición de liderazgo ejecutivo tras la designación de Colette Kress como CEO interina, generando incertidumbre táctica en el mercado pese a batir ampliamente las estimaciones.',
      'Compresión temporal del margen bruto hacia el rango 71.0%–72.0% en Q4 FY27 debido a los costes iniciales de fabricación y empaquetado CoWoS de la nueva plataforma Vera Rubin.',
      'Riesgo de concentración de ingresos en los cuatro grandes hyperscalers (Microsoft, Meta, Alphabet, Amazon) que desarrollan en paralelo sus propios aceleradores ASIC y restricciones de exportación de EE. UU. hacia China.'
    ],
    bull_points: [
      'Foso de software e infraestructura a escala de centro de datos: CUDA + NIM microservices + interconexión NVLink/Spectrum-X crean costes de cambio prohibitivos donde el cliente compra sistemas integrados completos y no simples GPUs.',
      'Despliegue anticipado de la arquitectura Vera Rubin e hipercrecimiento del segmento Data Center ($107,600M en el trimestre, +110% YoY y +20% secuencial), consolidando el estándar de factorías de IA.',
      'Generación de flujo de caja libre sin precedentes y retorno masivo al accionista con una nueva ampliación de $150,000M en el programa de recompras de acciones.'
    ],
    green_lines: [
      '🟢 Ingresos trimestrales de Data Center superando los $115,000M con adopción acelerada de sistemas Vera Rubin y margen bruto estabilizado sobre el 72%.',
      '🟢 Crecimiento de ingresos de software empresarial (NVIDIA AI Enterprise / NIM) e IA soberana por encima del +50% anual.'
    ],
    red_lines: [
      '🔴 Caída del margen bruto consolidado por debajo del 68.0% durante dos trimestres consecutivos por pérdida de poder de fijación de precios.',
      '🔴 Recorte abrupto (>15% YoY) en el CapEx de infraestructura de IA anunciado por al menos dos de los cuatro principales hyperscalers.'
    ]
  },
  PANW: {
    name: 'Palo Alto Networks, Inc.',
    sector: 'Technology / Software & Next-Generation Cybersecurity',
    industry: 'Software - Infrastructure',
    exchange: 'NASDAQ',
    weights_scores: { f1: 9.40, f2: 9.60, f3: 9.50, f4: 9.65, f5: 9.20, f6: 9.45, f7: 9.50, f8: 9.50 },
    moat_desc: 'Plataformización integral en tres pilares (Strata Network Security, Prisma Cloud/SASE y Cortex XSIAM) con $9.73B en NGS ARR (+66% YoY) y altísimos costes de cambio',
    wacc: 8.5, g: 3.5,
    eps_growth_ntm_pct: 18.5,
    seg1_name: 'Subscription & Support (NGS ARR / Cloud & XSIAM)', seg1_share: 0.815,
    seg2_name: 'Product (Next-Gen Firewalls & Appliances)', seg2_share: 0.185,
    guidance_summary: 'Para el ejercicio FY27, la dirección proyecta mantener el crecimiento de NGS ARR por encima del 40%, un margen operativo Non-GAAP superior al 30% y un margen de Free Cash Flow ajustado del 37%–38%, integrando la adquisición estratégica de Applied Compute para seguridad de agentes de IA.',
    competitors: [
      {
        name: 'CrowdStrike Holdings, Inc. (CRWD)',
        overlap: 'Seguridad de endpoints (EDR/XDR), operaciones de seguridad (SOC) y protección cloud (Falcon)',
        diff: 'PANW domina simultáneamente la seguridad de red (firewalls/SASE) y el SOC automatizado con Cortex XSIAM, permitiendo a los CISOs consolidar de 15 a 3 proveedores bajo una sola arquitectura.',
        moat: 'Excepcional'
      },
      {
        name: 'Zscaler, Inc. (ZS) / Fortinet, Inc. (FTNT)',
        overlap: 'Arquitectura Zero Trust Network Access (ZTNA / SASE) y firewalls corporativos de alto rendimiento',
        diff: 'Prisma SASE de PANW integra protección de red, SD-WAN y seguridad de navegador con telemetría cruzada hacia Cortex XSIAM, logrando un RPO de $21,000M (+35% YoY).',
        moat: 'Alto'
      }
    ],
    bear_points: [
      'Caída del beneficio operativo GAAP en Q1 FY27 ($96M vs $309M YoY) por el incremento de gastos de compensación basada en acciones (SBC) y costes de adquisiciones como Applied Compute.',
      'Fricción comercial a corto plazo derivada de la estrategia de "plataformización", donde PANW ofrece periodos gratuitos iniciales para desplazar contratos existentes de competidores.',
      'Intensa competencia en precios y consolidación de suites frente a CrowdStrike, Microsoft Defender/Sentinel y Zscaler en grandes cuentas Fortune 500.'
    ],
    bull_points: [
      'Éxito rotundo de la estrategia de plataformización: el ARR de Seguridad de Nueva Generación (NGS ARR) se disparó un +66% YoY hasta $9,730M, mientras las obligaciones de desempeño restantes (RPO) alcanzaron $21,000M (+35% YoY).',
      'Cortex XSIAM está reemplazando a los SIEM heredados (Splunk/QRadar) mediante automatización con IA que reduce el tiempo medio de remediación de amenazas de días a minutos.',
      'Máquina de conversión de flujo de caja: FCF ajustado trimestral de $1,900M (margen FCF del 56.2%) y $4,640M TTM (+24% YoY).'
    ],
    green_lines: [
      '🟢 NGS ARR superando los $11,500M en los próximos trimestres con más de 2,000 clientes empresariales completamente plataformizados.',
      '🟢 Sostenimiento del margen operativo Non-GAAP por encima del 30.5% y margen FCF TTM > 37%.'
    ],
    red_lines: [
      '🔴 Desaceleración del crecimiento de RPO por debajo del +18% YoY o caída del crecimiento de NGS ARR por debajo del +25%.',
      '🔴 Dilución accionaria neta por SBC y adquisiciones que supere el 3.5% anual sin retorno proporcional en FCF por acción.'
    ]
  },
  INTU: {
    name: 'Intuit Inc.',
    sector: 'Technology / Financial, Accounting & Tax Enterprise SaaS',
    industry: 'Software - Application',
    exchange: 'NASDAQ',
    weights_scores: { f1: 9.50, f2: 9.30, f3: 9.25, f4: 9.75, f5: 9.10, f6: 9.35, f7: 9.20, f8: 9.50 },
    moat_desc: 'Sistema operativo financiero insustituible para PYMEs (QuickBooks Online / Intuit Enterprise Suite) y consumidores (TurboTax / Credit Karma) con altísima retención y datos propietarios',
    wacc: 8.5, g: 3.5,
    eps_growth_ntm_pct: 16.8,
    seg1_name: 'Global Business Solutions (QuickBooks & Enterprise Suite)', seg1_share: 0.713,
    seg2_name: 'Consumer & Credit Karma (TurboTax & Personal Finance)', seg2_share: 0.287,
    guidance_summary: 'La dirección actualizó la guía de ingresos FY27 a $23,081M–$23,365M (+8% a +9% YoY) y reiteró sus objetivos de beneficio operativo y BPA para el año completo, anunciando además la venta definitiva de Mailchimp a Bending Spoons por $3,680M para concentrar el capital en QuickBooks Mid-Market e Intuit Assist IA.',
    competitors: [
      {
        name: 'Xero Limited / Sage Group plc / NetSuite (ORCL)',
        overlap: 'Software de contabilidad en la nube, nóminas, pagos y ERP para pequeñas y medianas empresas',
        diff: 'QuickBooks posee más del 75% de cuota en PYMEs de EE. UU. e integra pagos, nóminas, capital circulante y contadores externos en una red bilateral imposible de replicar.',
        moat: 'Excepcional'
      },
      {
        name: 'H&R Block, Inc. (HRB) / IRS Direct File',
        overlap: 'Preparación de impuestos asistida y digital (DIY) en Estados Unidos',
        diff: 'TurboTax Live combina automatización con IA generativa (Intuit Assist) y una red de miles de expertos fiscales certificados, dominando los segmentos de mayor complejidad y margen.',
        moat: 'Excepcional'
      }
    ],
    bear_points: [
      'Desinversión de Mailchimp por $3,680M a Bending Spoons, cristalizando una minusvalía contable frente a los ~$12,000M pagados en 2021 y reconociendo las dificultades de integración del marketing para PYMEs.',
      'Revisión a la baja en la guía de ingresos de FY27 (+8% a +9%) debido a una recuperación más lenta de lo previsto en préstamos personales y tarjetas dentro de Credit Karma.',
      'Castigo bursátil a corto plazo (-12% post-resultados hasta $270.44) ante una guía de Q2 FY27 más conservadora que el consenso de Wall Street.'
    ],
    bull_points: [
      'Disciplina estratégica al vender Mailchimp por $3,680M en efectivo: elimina el principal lastre del crecimiento de Global Business Solutions, libera capital para recompras de acciones a múltiplos deprimidos y eleva el margen operativo estructural.',
      'Fuerte aceleración del ecosistema core: los ingresos de Global Business Solutions crecieron un +15% YoY hasta $3,100M (con el Online Ecosystem creciendo +20% YoY) y el EBIT GAAP se disparó un +63% YoY hasta $868M.',
      'Expansión hacia el segmento Mid-Market con Intuit Enterprise Suite (ERP nativo para empresas de $5M a $100M de facturación), multiplicando el ARPC (ingreso medio por cliente) a una fracción del coste de NetSuite.'
    ],
    green_lines: [
      '🟢 Crecimiento sostenido del Online Ecosystem de QuickBooks (excluyendo Mailchimp) por encima del +20% YoY con expansión de margen operativo > 200 bps.',
      '🟢 Destino íntegro de los $3,680M de la venta de Mailchimp a recompras aceleradas de acciones por debajo de 22x PER Forward.'
    ],
    red_lines: [
      '🔴 Desaceleración del crecimiento de QuickBooks Online por debajo del +12% YoY o pérdida de cuota en el segmento Mid-Market.',
      '🔴 Expansión agresiva de programas públicos gratuitos de declaración fiscal que erosionen el volumen de clientes de pago de TurboTax en más de un 5% anual.'
    ]
  },
  KEYS: {
    name: 'Keysight Technologies Inc.',
    sector: 'Technology / Electronic Design, Test & AI Network Emulation',
    industry: 'Scientific & Technical Instruments',
    exchange: 'NYSE',
    weights_scores: { f1: 8.85, f2: 9.10, f3: 8.70, f4: 9.25, f5: 8.75, f6: 8.80, f7: 8.90, f8: 8.60 },
    moat_desc: 'Estándar mundial en instrumentación de prueba electrónica, emulación de redes de IA (800G/1.6T) y software EDA PathWave con altísimos costes de cambio en I+D',
    wacc: 8.5, g: 3.5,
    eps_growth_ntm_pct: 22.0,
    seg1_name: 'Communications Solutions Group (AI Data Center, 5G/6G & Aerospace/Defense)', seg1_share: 0.715,
    seg2_name: 'Electronic Industrial Solutions Group (Semiconductor, Auto & General Electronics)', seg2_share: 0.285,
    guidance_summary: 'Tras un Q4 FY26 récord ($1,990M de ingresos, +40.5% YoY y BPA ajustado de $3.61), la dirección emitió una guía muy sólida para Q1 FY27 proyectando ingresos de hasta $2,060M y un BPA ajustado de hasta $3.69, impulsado por pedidos récord en interconexión óptica de IA 800G/1.6T.',
    competitors: [
      {
        name: 'Rohde & Schwarz / Anritsu Corporation',
        overlap: 'Analizadores de espectro, generadores de señal y pruebas de radiofrecuencia / telecomunicaciones',
        diff: 'Keysight posee la mayor escala global en I+D, dominando los estándares emergentes de redes de centros de datos de IA de 1.6 Terabits y validación de silicio PCIe Gen 6/7.',
        moat: 'Excepcional'
      },
      {
        name: 'Teradyne, Inc. (TER) / Advantest Corp.',
        overlap: 'Pruebas automatizadas de semiconductores y validación en fase de producción/laboratorio',
        diff: 'Keysight domina la fase crítica de diseño y validación en laboratorio (R&D Lab) con su suite de software PathWave, asegurando ingresos recurrentes y márgenes operativos del 35.8%.',
        moat: 'Alto'
      }
    ],
    bear_points: [
      'Debilidad cíclica remanente en el segmento de automoción (vehículos eléctricos y baterías) y manufactura industrial general en Europa y Asia.',
      'Exposición a controles de exportación de tecnología estadounidense hacia clientes de semiconductores y telecomunicaciones en China.',
      'Apalancamiento moderado tras adquisiciones estratégicas de software de simulación e ingeniería (ESI Group / Spirent assets).'
    ],
    bull_points: [
      'Inflexión explosiva por infraestructura de IA: los ingresos de Q4 FY26 saltaron un +40.5% YoY hasta $1,990M y el margen operativo se expandió 950 bps hasta el 35.8% gracias a la demanda de pruebas para clusters de IA de 800G y 1.6T.',
      'Crecimiento estructural del peso de software y servicios recurrentes (>35% de la facturación total), elevando el margen bruto por encima del 65%.',
      'Foso de misión crítica en defensa, aeroespacial y redes cuánticas/6G, donde los ingenieros se forman desde la universidad con hardware y software de Keysight.'
    ],
    green_lines: [
      '🟢 Crecimiento de pedidos (orders) en comunicaciones de centros de datos de IA > 25% YoY con margen operativo ajustado > 32%.',
      '🟢 Integración exitosa de activos de simulación y prueba de red que eleve la proporción de ingresos recurrentes de software al 40%.'
    ],
    red_lines: [
      '🔴 Pausa en el ciclo de actualización de redes ópticas de hyperscalers que provoque una caída del ratio Book-to-Bill por debajo de 0.90x.',
      '🔴 Contracción del margen bruto consolidado por debajo del 61.0%.'
    ]
  },
  NTES: {
    name: 'NetEase, Inc.',
    sector: 'Communication Services / Interactive Gaming & Digital Entertainment',
    industry: 'Electronic Gaming & Multimedia',
    exchange: 'NASDAQ',
    weights_scores: { f1: 8.90, f2: 9.60, f3: 8.10, f4: 8.70, f5: 8.60, f6: 8.40, f7: 8.20, f8: 8.30 },
    moat_desc: 'Franquicias de videojuegos multijugador longevas (Fantasy Westward Journey, Justice, Naraka), alianza estratégica con Blizzard en China y balance con enorme posición de caja neta',
    wacc: 9.5, g: 3.0,
    eps_growth_ntm_pct: 11.5,
    seg1_name: 'Games and Related Value-Added Services (PC & Mobile Games)', seg1_share: 0.821,
    seg2_name: 'Youdao, NetEase Cloud Music & Innovative Businesses', seg2_share: 0.179,
    guidance_summary: 'La dirección prioriza la expansión del margen bruto (que alcanzó un récord de 68.4%, +430 bps YoY) mediante juegos de desarrollo propio, el relanzamiento completo del catálogo de Blizzard en China y el ejecución de su programa de recompra de acciones de $5,000M junto a dividendos trimestrales.',
    competitors: [
      {
        name: 'Tencent Holdings Ltd. (TCEHY)',
        overlap: 'Desarrollo y publicación de videojuegos móviles y de PC en China y mercados globales',
        diff: 'NetEase posee una mayor proporción de estudios internos de I+D propio en géneros MMORPG y Party Games, logrando un margen bruto del 68.4% al depender menos de licencias de terceros.',
        moat: 'Alto'
      },
      {
        name: 'miHoYo (HoYoverse) / Sony Interactive (SONY)',
        overlap: 'Juegos RPG de alto presupuesto multiplataforma (Genshin Impact, Honkai) y expansión en consolas/PC',
        diff: 'NetEase cuenta con franquicias de más de 20 años de antigüedad con economías virtuales ultra-estables y el retorno oficial de World of Warcraft y Hearthstone en China.',
        moat: 'Alto'
      }
    ],
    bear_points: [
      'Ligera contracción de ingresos en Q3 2026 (-1.8% YoY hasta RMB 27.9B / ~$4,200M USD) por la normalización de títulos móviles lanzados el año anterior como Eggy Party.',
      'Riesgo regulatorio persistente en China sobre límites de gasto y tiempo de juego en menores y monetización mediante mecánicas gacha.',
      'Retornos aún modestos en algunos estudios internacionales abiertos en Japón, Norteamérica y Europa.'
    ],
    bull_points: [
      'Expansión sobresaliente del margen bruto consolidado hasta el 68.4% (+430 bps YoY desde 64.1%), impulsada por la migración hacia canales de pago propios y títulos auto-desarrollados.',
      'Recuperación de millones de jugadores activos en PC gracias al regreso triunfal de los títulos de Blizzard (World of Warcraft, Overwatch, Hearthstone) en China continental.',
      'Balance blindado con más de $16,000M USD en caja neta e inversiones a corto plazo, respaldando recompras continuas y dividendos.'
    ],
    green_lines: [
      '🟢 Retorno al crecimiento positivo de ingresos de videojuegos (>+8% YoY) impulsado por Marvel Rivals, Where Winds Meet y el catálogo de Blizzard.',
      '🟢 Sostenimiento del margen bruto consolidado por encima del 66.0% con ejecución activa de recompras.'
    ],
    red_lines: [
      '🔴 Nuevas restricciones de la NPPA en China que limiten severamente la monetización de juegos MMORPG.',
      '🔴 Caída de ingresos del segmento de videojuegos durante tres trimestres consecutivos.'
    ]
  },
  ROST: {
    name: 'Ross Stores, Inc.',
    sector: 'Consumer Cyclical / Off-Price Apparel & Home Fashion Retail',
    industry: 'Apparel Retail',
    exchange: 'NASDAQ',
    weights_scores: { f1: 8.65, f2: 9.20, f3: 8.35, f4: 8.75, f5: 8.60, f6: 8.55, f7: 7.40, f8: 8.60 },
    moat_desc: 'Escala masiva de compras oportunistas off-price (más de 2,150 tiendas Ross Dress for Less y dd’s DISCOUNTS) con rotación acelerada de inventario y alta resiliencia anticíclica',
    wacc: 8.2, g: 3.0,
    eps_growth_ntm_pct: 12.8,
    seg1_name: 'Ross Dress for Less (Off-Price Apparel, Footwear & Home)', seg1_share: 0.875,
    seg2_name: 'dd’s DISCOUNTS (Value-Focused Off-Price Stores)', seg2_share: 0.125,
    guidance_summary: 'Tras batir estimaciones en Q3 FY26 ($6,260M de ingresos, +11.8% YoY y BPA de $1.91), la dirección elevó la guía de BPA para el ejercicio FY26 completo al rango de $8.75–$8.84 USD, apoyada en una expansión de 70 bps en el margen operativo (12.3%) y aperturas netas de ~90 tiendas anuales.',
    competitors: [
      {
        name: 'The TJX Companies, Inc. (TJX)',
        overlap: 'Retail off-price de moda, calzado y artículos del hogar en Estados Unidos (T.J. Maxx, Marshalls)',
        diff: 'Ross opera exclusivamente en EE. UU. con un formato de tienda más estandarizado y menor estructura de costes en tienda, enfocándose en el consumidor de ingresos medios y moderados con descuentos del 20%–60%.',
        moat: 'Alto'
      },
      {
        name: 'Burlington Stores, Inc. (BURL)',
        overlap: 'Tiendas departamentales de descuento off-price en centros comerciales suburbanos',
        diff: 'Ross duplica la escala de compras de Burlington, mantiene un margen operativo muy superior (12.3% vs ~7%) y cuenta con un balance con amplia posición de caja neta.',
        moat: 'Alto'
      }
    ],
    bear_points: [
      'Presión inflacionaria acumulada sobre el consumidor de bajos ingresos (núcleo de dd’s DISCOUNTS), lo que llevó a la directiva a mantener una guía prudente para el trimestre navideño Q4.',
      'Ausencia deliberada de canal de comercio electrónico transaccional, dependiendo al 100% del tráfico físico a las tiendas.',
      'Presiones salariales en tiendas y centros de distribución junto a la volatilidad en tarifas de flete marítimo y terrestre.'
    ],
    bull_points: [
      'Fuerte aceleración operativa en Q3 FY26: las ventas crecieron un +11.8% YoY hasta $6,260M, el margen operativo subió 70 bps hasta el 12.3% ($767M EBIT) y el BPA creció un +20.9% YoY hasta $1.91.',
      'Efecto "trade-down" favorable: en entornos de precios altos, los consumidores de clase media migran desde grandes almacenes tradicionales (Macy’s, Kohl’s) hacia la experiencia de "caza del tesoro" de Ross.',
      'Red de más de 900 compradores especializados que adquieren excedentes de inventario de miles de marcas de primer nivel con descuentos imposibles de igualar por minoristas regionales.'
    ],
    green_lines: [
      '🟢 Crecimiento de ventas comparables (comp store sales) > +4.0% con margen operativo consolidado superando el 12.5%.',
      '🟢 Apertura rentable de 90–100 nuevas tiendas anuales hacia el objetivo de 3,600 ubicaciones a largo plazo.'
    ],
    red_lines: [
      '🔴 Contracción de ventas comparables en tiendas existentes durante dos trimestres seguidos.',
      '🔴 Escasez estructural de inventario excedente de marcas de moda que comprima el margen bruto de mercancías en más de 150 bps.'
    ]
  },
  PDD: {
    name: 'PDD Holdings Inc.',
    sector: 'Consumer Cyclical / Social E-Commerce & Global Cross-Border Marketplace',
    industry: 'Internet Retail',
    exchange: 'NASDAQ',
    weights_scores: { f1: 9.20, f2: 9.50, f3: 8.50, f4: 8.50, f5: 8.30, f6: 7.90, f7: 8.40, f8: 8.00 },
    moat_desc: 'Red C2M (Consumer-to-Manufacturer) hiper-eficiente en China (Pinduoduo) y escala global transfronteriza (Temu) con márgenes operativos del 30% y más de $40B en caja neta',
    wacc: 10.5, g: 3.5,
    eps_growth_ntm_pct: 14.5,
    seg1_name: 'Online Marketing Services and Others (Pinduoduo Core Advertising)', seg1_share: 0.552,
    seg2_name: 'Transaction Services (Temu Global & Duo Duo Grocery Commissions)', seg2_share: 0.448,
    guidance_summary: 'En Q3 2026, PDD priorizó la rentabilidad y la transición de Temu hacia el modelo semi-gestionado con inventario local, logrando un beneficio operativo Non-GAAP de RMB 32.6B (~$4,860M USD, margen del 30.1%) y batiendo el consenso de BPA ($3.14 vs $2.77 estimado) pese a la estabilización de ingresos por aranceles internacionales.',
    competitors: [
      {
        name: 'Alibaba Group Holding Ltd. (BABA) / JD.com, Inc. (JD)',
        overlap: 'Comercio electrónico minorista, publicidad de comerciantes y productos agrícolas en China',
        diff: 'PDD opera con una estructura organizativa ultra-ligera y algoritmos de compra social que conectan directamente fábricas y agricultores con el consumidor sin intermediarios, logrando márgenes operativos del 30%.',
        moat: 'Alto'
      },
      {
        name: 'Amazon.com, Inc. (AMZN) / Shein',
        overlap: 'Comercio electrónico transfronterizo de bajo precio en Norteamérica, Europa y mercados emergentes',
        diff: 'Temu aprovecha la cadena de suministro industrial directa de China y está migrando rápidamente al modelo "semi-managed" con almacenes locales para sortear barreras aduaneras.',
        moat: 'Medio'
      }
    ],
    bear_points: [
      'Desaceleración abrupta del crecimiento de ingresos en Q3 2026 (+0.1% YoY hasta RMB 108.3B / ~$16,200M USD), con una caída del 12% en servicios de transacción debido a las restricciones arancelarias y la eliminación de exenciones de minimis en EE. UU. y Europa.',
      'Falta de política formal de dividendos o recompras significativas pese a acumular una montaña de efectivo en balance, penalizando el múltiplo PER.',
      'Guerra de subsidios y precios en el mercado doméstico chino frente a Taobao/Tmall (Alibaba) y Douyin (ByteDance).'
    ],
    bull_points: [
      'Disciplina de costes y rentabilidad extraordinaria: el BPA diluido Non-GAAP alcanzó $3.14 por ADS (RMB 21.04), superando en un +13.4% el consenso de Wall Street gracias a la optimización del gasto en marketing.',
      'El negocio principal de publicidad online (Online Marketing Services) creció un sólido +12% YoY hasta RMB 59.8B, demostrando que la monetización de comerciantes en Pinduoduo sigue intacta.',
      'Valoración extremadamente deprimida (<8x PER Forward) con una posición de caja neta que representa más del 35% de su capitalización bursátil.'
    ],
    green_lines: [
      '🟢 Éxito del modelo semi-gestionado de Temu (con cumplimiento desde almacenes locales en EE. UU. y UE) reactivando el crecimiento de Transaction Services > +10% YoY.',
      '🟢 Anuncio de un primer programa estructural de recompra de acciones o dividendo que libere el valor de su caja neta.'
    ],
    red_lines: [
      '🔴 Prohibición regulatoria o aranceles punitivos (>60%) que hagan inviable el modelo económico de Temu en Occidente.',
      '🔴 Caída del margen operativo Non-GAAP por debajo del 22.0% por reactivación de subsidios agresivos.'
    ]
  },
  WSM: {
    name: 'Williams-Sonoma, Inc.',
    sector: 'Consumer Cyclical / Omnichannel Specialty Home Furnishings Retail',
    industry: 'Specialty Retail',
    exchange: 'NYSE',
    weights_scores: { f1: 8.85, f2: 9.30, f3: 7.90, f4: 8.40, f5: 8.95, f6: 8.60, f7: 7.50, f8: 8.10 },
    moat_desc: 'Cartera de marcas propias de mobiliario y hogar de gama media-alta (Pottery Barn, West Elm, Williams Sonoma) con 66% de ventas digitales, diseño propio (>90%) y ROIC > 35%',
    wacc: 8.8, g: 2.8,
    eps_growth_ntm_pct: 10.5,
    seg1_name: 'Pottery Barn & Pottery Barn Kids/Teen (Home Furnishings)', seg1_share: 0.565,
    seg2_name: 'West Elm, Williams Sonoma & B2B Contract', seg2_share: 0.435,
    guidance_summary: 'Tras reportar un crecimiento de ingresos del +5.8% YoY ($1,990M), ventas comparables de marca del +5.1% y un margen operativo GAAP del 18.9% (BPA GAAP de $2.38, +21.4% YoY), la dirección reafirmó su guía anual de margen operativo (17.8%–18.2%) y continúa recomprando acciones con un balance sin deuda a largo plazo.',
    competitors: [
      {
        name: 'RH (Restoration Hardware - RH) / Arhaus, Inc. (ARHS)',
        overlap: 'Mobiliario de diseño y decoración del hogar para segmentos de renta media-alta y alta',
        diff: 'WSM opera sin deuda financiera, con un modelo omnicanal donde dos tercios de los ingresos son e-commerce de alta conversión, logrando una estabilidad de márgenes muy superior a RH.',
        moat: 'Alto'
      },
      {
        name: 'Wayfair Inc. (W) / IKEA',
        overlap: 'Venta online y física de muebles, menaje de cocina y textiles para el hogar',
        diff: 'Más del 90% de los productos de WSM son diseñados internamente y vendidos en exclusiva bajo sus marcas propias, evitando la comparación directa de precios con marketplaces como Wayfair.',
        moat: 'Alto'
      }
    ],
    bear_points: [
      'Sensibilidad al mercado inmobiliario residencial de EE. UU., donde las ventas de viviendas existentes siguen frenadas por tipos hipotecarios elevados.',
      'Exposición a aranceles de importación sobre mobiliario y componentes fabricados en Asia.',
      'Toma de beneficios en la acción (-15% el día de resultados hasta $220.66) tras una fuerte apreciación previa en el año ante expectativas muy exigentes del mercado.'
    ],
    bull_points: [
      'Vuelta al crecimiento positivo en todas las marcas: ingresos de $1,990M (+5.8% YoY) y +5.1% en ventas comparables en Q3 FY26, demostrando ganancia de cuota de mercado en un sector de muebles plano.',
      'Disciplina férrea de precios ("full-price selling") y optimización de la cadena de suministro que mantienen un margen operativo GAAP del 18.9% (muy por encima del ~8%–10% pre-pandemia).',
      'Expansión acelerada del canal B2B (equipamiento para hoteles, oficinas y restaurantes) y balance inmaculado sin deuda a largo plazo con ROIC superior al 35%.'
    ],
    green_lines: [
      '🟢 Crecimiento de ventas comparables consolidado > +4.5% con recuperación sostenida de la marca West Elm.',
      '🟢 Expansión de la división B2B por encima de los $1,200M anuales manteniendo márgenes operativos > 17.5%.'
    ],
    red_lines: [
      '🔴 Regreso a promociones y descuentos agresivos que compriman el margen bruto por debajo del 42.0%.',
      '🔴 Caída de ventas comparables (brand comps) a terreno negativo durante dos trimestres consecutivos.'
    ]
  },
  WWD: {
    name: 'Woodward, Inc.',
    sector: 'Industrials / Aerospace & Industrial Energy Control Systems',
    industry: 'Aerospace & Defense',
    exchange: 'NASDAQ',
    weights_scores: { f1: 8.35, f2: 8.80, f3: 8.55, f4: 8.85, f5: 8.40, f6: 8.50, f7: 8.00, f8: 8.45 },
    moat_desc: 'Sistemas críticos de control de combustible, actuadores y combustión certificados por la FAA en motores comerciales/defensa (LEAP, GTF) y generación de energía para centros de datos',
    wacc: 8.3, g: 3.2,
    eps_growth_ntm_pct: 16.5,
    seg1_name: 'Aerospace (Commercial & Defense Fuel/Motion Control & Aftermarket)', seg1_share: 0.635,
    seg2_name: 'Industrial (Power Generation for Data Centers, Marine & Gas Turbines)', seg2_share: 0.365,
    guidance_summary: 'Woodward cerró un ejercicio FY26 récord ($4,360M de ingresos anuales, +22.1% YoY y BPA de $9.49, +32% YoY) con un Q4 FY26 de $1,160M (+16.6% YoY) y BPA ajustado de $2.83, apoyado en una cartera de pedidos (backlog) récord de $4,570M e impulsado por el aftermarket aeroespacial y turbinas de respaldo para centros de datos de IA.',
    competitors: [
      {
        name: 'Moog Inc. (MOG.A) / Parker-Hannifin Corp. (PH)',
        overlap: 'Actuadores de control de vuelo, válvulas y sistemas hidromecánicos aeroespaciales',
        diff: 'Woodward posee posiciones sole-source en los sistemas de dosificación de combustible de los motores de pasillo único más vendidos del mundo (CFM LEAP y Pratt & Whitney GTF), garantizando décadas de aftermarket cautivo.',
        moat: 'Excepcional'
      },
      {
        name: 'Curtiss-Wright Corp. (CW) / Eaton Corp. (ETN)',
        overlap: 'Controles industriales para turbinas de gas, motores diésel marinos y componentes de defensa',
        diff: 'Woodward domina los sistemas de inyección y control para motores de gas natural y diésel de gran calibre utilizados en generación eléctrica primaria y de emergencia para centros de datos.',
        moat: 'Alto'
      }
    ],
    bear_points: [
      'Cuellos de botella en la cadena de suministro aeroespacial y ritmos de producción de Boeing que pueden limitar las entregas OEM a corto plazo.',
      'Normalización eventual de la demanda de camiones pesados a gas natural (LNG) en el mercado chino dentro del segmento Industrial.',
      'Cotización cerca de máximos históricos ($319.07 en la fecha de publicación), exigiendo una ejecución impecable en la expansión de márgenes.'
    ],
    bull_points: [
      'Cosecha secular del aftermarket aeroespacial: la flota global de motores LEAP y GTF está entrando en su primera ventana intensa de revisiones de taller (shop visits), donde Woodward obtiene márgenes tres veces superiores a la venta OEM.',
      'Viento de cola en el segmento Industrial por la construcción masiva de centros de datos de IA, que requieren turbinas de gas y generadores de respaldo equipados con controles Woodward.',
      'Cartera de pedidos récord de $4,570M que otorga una visibilidad plurianual excepcional de ingresos y flujo de caja libre.'
    ],
    green_lines: [
      '🟢 Crecimiento de ingresos de aftermarket aeroespacial > +18% YoY con expansión del margen del segmento Aerospace por encima del 21%.',
      '🟢 Sostenimiento del backlog total por encima de los $4,500M con conversión de FCF > 90% del beneficio neto.'
    ],
    red_lines: [
      '🔴 Problemas de calidad o retiradas técnicas en componentes de motores LEAP/GTF que generen cargos de garantía significativos.',
      '🔴 Contracción del margen operativo del segmento Industrial por debajo del 14.0%.'
    ]
  },
  HD: {
    name: 'The Home Depot, Inc.',
    sector: 'Consumer Cyclical / Home Improvement & Pro Building Materials Retail',
    industry: 'Home Improvement Retail',
    exchange: 'NYSE',
    weights_scores: { f1: 8.80, f2: 8.10, f3: 7.90, f4: 9.30, f5: 8.70, f6: 8.80, f7: 7.80, f8: 8.60 },
    moat_desc: 'Líder indiscutible en mejora del hogar en Norteamérica (>2,340 almacenes) y ecosistema logístico para contratistas profesionales (Pro + SRS Distribution) con ROIC > 30%',
    wacc: 8.0, g: 3.0,
    eps_growth_ntm_pct: 9.5,
    seg1_name: 'Pro Contractor & SRS Distribution Ecosystem', seg1_share: 0.530,
    seg2_name: 'Do-It-Yourself (DIY) Consumer Home Improvement', seg2_share: 0.470,
    guidance_summary: 'Tras superar expectativas en Q3 FY26 con ventas de $43,400M (+4.9% YoY), beneficio operativo GAAP de $5,480M (ajustado de $5,660M) y BPA ajustado de $3.86, la dirección elevó su guía de ventas anuales (+4.0% YoY incluyendo SRS Distribution) y proyecta un margen operativo anual de ~13.5%–13.8%.',
    competitors: [
      {
        name: 'Lowe’s Companies, Inc. (LOW)',
        overlap: 'Grandes almacenes de bricolaje, materiales de construcción, electrodomésticos y jardinería en EE. UU.',
        diff: 'Home Depot genera más del 50% de sus ventas del cliente profesional (Pro), frente al ~25%–30% de Lowe’s, obteniendo mayores ventas por pie cuadrado y un ROIC superior.',
        moat: 'Excepcional'
      },
      {
        name: 'Builders FirstSource (BLDR) / Ferguson Enterprises (FERG)',
        overlap: 'Distribución mayorista especializada para contratistas de techado, piscinas, paisajismo y fontanería',
        diff: 'Con la integración de SRS Distribution ($18.25B), Home Depot combina su red de 2,340 tiendas con una flota de entrega directa en obra y crédito comercial para grandes contratistas.',
        moat: 'Alto'
      }
    ],
    bear_points: [
      'Aplazamiento persistente de grandes proyectos de remodelación discrecional (cocinas, baños completos) debido a los altos tipos de interés en préstamos HELOC e hipotecas.',
      'Aumento del endeudamiento neto para financiar la adquisición de SRS Distribution, lo que ha pausado temporalmente las recompras de acciones hasta reducir el ratio de apalancamiento.',
      'Dilución de ~40 bps en el margen bruto consolidado por el mix mayorista de SRS Distribution.'
    ],
    bull_points: [
      'Inflexión positiva en Q3 FY26: ingresos de $43,400M (+4.9% YoY) batiendo el consenso en más de $600M, impulsados por la demanda de reparación tras huracanes y la solidez del segmento Pro.',
      'La adquisición de SRS Distribution amplía el mercado total direccionable (TAM) de Home Depot en $50,000M adicionales hasta $1,000B, capturando al contratista especializado de techos, paisajismo y piscinas.',
      'Fundamentos estructurales intactos: el parque de viviendas de EE. UU. tiene una antigüedad media récord de más de 42 años y acumula billones de dólares en home equity.'
    ],
    green_lines: [
      '🟢 Retorno a ventas comparables (comp sales) positivas > +3.0% en EE. UU. a medida que se normalicen los tipos de interés.',
      '🟢 Desapalancamiento rápido del balance que permita reactivar el programa de recompra de acciones en FY27.'
    ],
    red_lines: [
      '🔴 Contracción del margen operativo consolidado por debajo del 12.0% por presiones competitivas o fallos de integración en SRS.',
      '🔴 Caída del ticket promedio y de las transacciones Pro durante tres trimestres consecutivos.'
    ]
  },
  LOW: {
    name: "Lowe's Companies, Inc.",
    sector: 'Consumer Cyclical / Home Improvement & Omnichannel Retail',
    industry: 'Home Improvement Retail',
    exchange: 'NYSE',
    weights_scores: { f1: 8.65, f2: 7.70, f3: 7.85, f4: 8.90, f5: 8.55, f6: 8.60, f7: 7.70, f8: 8.40 },
    moat_desc: 'Duopolio nacional en mejora del hogar (>1,740 tiendas en EE. UU.) con fuerte aceleración digital (+17.4% online YoY) y penetración creciente en el segmento Pro',
    wacc: 8.2, g: 3.0,
    eps_growth_ntm_pct: 10.2,
    seg1_name: 'DIY Consumer & Online Omnichannel Home Improvement', seg1_share: 0.700,
    seg2_name: 'Pro Customer & Building Products Installation', seg2_share: 0.300,
    guidance_summary: 'Lowe’s reportó en Q3 FY26 un crecimiento de ingresos del +9.3% YoY hasta $22,756M (con +1.8% en ventas comparables, sexto trimestre consecutivo en positivo, y +17.4% en ventas online) y un BPA ajustado de $3.10 (incluyendo $0.34 por reembolsos arancelarios IEEPA), elevando sus previsiones anuales de ingresos.',
    competitors: [
      {
        name: 'The Home Depot, Inc. (HD)',
        overlap: 'Almacenes de bricolaje, reformas, electrodomésticos y suministros para contratistas en EE. UU.',
        diff: 'Lowe’s posee una mayor exposición al consumidor residencial DIY y a mercados suburbanos/rurales con menor solapamiento competitivo, además de registrar un crecimiento online del +17.4% YoY.',
        moat: 'Excepcional'
      },
      {
        name: 'Amazon.com (AMZN) / Best Buy (BBY) / Ace Hardware',
        overlap: 'Venta de electrodomésticos, herramientas eléctricas, domótica y ferretería ligera',
        diff: 'La red logística de Lowe’s para entrega e instalación de artículos voluminosos (electrodomésticos, suelos, madera) constituye una barrera física infranqueable para el e-commerce puro.',
        moat: 'Alto'
      }
    ],
    bear_points: [
      'Patrimonio neto contablemente negativo y apalancamiento financiero derivado de años de agresivas recompras de acciones financiadas con deuda.',
      'Parte del batimiento de BPA en Q3 FY26 ($3.10 ajustado) provino de un beneficio extraordinario de $250M pre-impuestos ($0.34/acción) por reembolsos de aranceles IEEPA.',
      'Ligera compresión del margen bruto subyacente debido a la reinversión de los reembolsos arancelarios en precios competitivos y mayor mix de ventas online.'
    ],
    bull_points: [
      'Sexto trimestre consecutivo de ventas comparables positivas (+1.8% en Q3 FY26) con ingresos totales creciendo un +9.3% YoY hasta $22,756M.',
      'Desempeño omnicanal sobresaliente: las ventas en Lowes.com se dispararon un +17.4% YoY gracias a la renovación de la experiencia móvil y el programa de fidelización MyLowe’s Rewards.',
      'Iniciativa "Total Home Strategy" ganando tracción continua en el pequeño y mediano contratista Pro con entregas en el mismo día.'
    ],
    green_lines: [
      '🟢 Crecimiento del segmento Pro y ventas online a doble dígito (+10% YoY) sosteniendo ventas comparables totales > +2.5%.',
      '🟢 Expansión del margen operativo hacia el 12.5%–13.0% excluyendo partidas extraordinarias arancelarias.'
    ],
    red_lines: [
      '🔴 Deterioro del ratio de cobertura de intereses por debajo de 5.0x o degradación de calificación crediticia.',
      '🔴 Pérdida de cuota de mercado en electrodomésticos y bricolaje con comps negativos superiores al -2%.'
    ]
  },
  TGT: {
    name: 'Target Corporation',
    sector: 'Consumer Defensive / Omnichannel General Merchandise & Grocery Retail',
    industry: 'Discount Stores',
    exchange: 'NYSE',
    weights_scores: { f1: 8.15, f2: 8.40, f3: 7.90, f4: 8.35, f5: 8.30, f6: 8.20, f7: 7.80, f8: 8.30 },
    moat_desc: 'Red de casi 2,000 tiendas como hubs logísticos omnicanal (Drive Up / Same-Day Delivery), marcas propias multimillonarias y plataforma publicitaria Roundel',
    wacc: 8.2, g: 2.8,
    eps_growth_ntm_pct: 14.2,
    seg1_name: 'Everyday Essentials, Beauty, Food & Beverage', seg1_share: 0.540,
    seg2_name: 'Discretionary Apparel, Home, Electronics & Roundel Media', seg2_share: 0.460,
    guidance_summary: 'Target sorprendió positivamente en Q3 2026 con ingresos de $27,070M (+7.1% YoY), un crecimiento de ventas comparables del +5.6% (impulsado por un +5.0% en tráfico de clientes) y un BPA de $2.65 (superando ampliamente el consenso de $2.08 e incluyendo $0.50 por reembolsos de aranceles IEEPA), lo que llevó a la dirección a elevar su guía anual.',
    competitors: [
      {
        name: 'Walmart Inc. (WMT)',
        overlap: 'Supercentros omnicanal de alimentación, productos básicos del hogar, moda y electrónica en EE. UU.',
        diff: 'Target se diferencia mediante un posicionamiento "cheap chic" con más de $30,000M en marcas de diseño exclusivo (Good & Gather, Cat & Jack, Threshold) y alianzas con Ulta Beauty.',
        moat: 'Alto'
      },
      {
        name: 'Amazon.com, Inc. (AMZN) / Costco Wholesale (COST)',
        overlap: 'Comercio electrónico con entrega rápida, membresías (Target Circle 360) y mercancía general',
        diff: 'Target cumple más del 95% de sus pedidos digitales directamente desde sus tiendas locales mediante Drive Up y Shipt, logrando un coste de envío de última milla hasta un 40% inferior.',
        moat: 'Alto'
      }
    ],
    bear_points: [
      'Mayor exposición a categorías discrecionales (moda, decoración del hogar, juguetes) en comparación con Walmart, lo que introduce mayor volatilidad cíclica.',
      'El resultado de Q3 2026 incluyó un beneficio extraordinario pre-impuestos de $301M ($0.50 por acción) derivado de reembolsos de aranceles IEEPA.',
      'Competencia feroz en precios de alimentación y membresías de entrega rápida frente a Walmart+ y Amazon Prime.'
    ],
    bull_points: [
      'Fuerte recuperación del tráfico y cuota de mercado en Q3 2026: ingresos de $27,070M (+7.1% YoY) y ventas comparables del +5.6% con un aumento del +5.0% en el número de transacciones.',
      'Incluso excluyendo el beneficio de $0.50/acción por reembolsos arancelarios IEEPA, el BPA ajustado creció un +21% YoY hasta $2.15, demostrando una mejora real en merma (shrink) y eficiencia logística.',
      'Crecimiento a doble dígito de Roundel (su negocio de Retail Media de muy alto margen) y del programa de fidelización Target Circle 360.'
    ],
    green_lines: [
      '🟢 Sostenimiento del crecimiento de tráfico en tiendas y canales digitales > +3.0% YoY con margen operativo estabilizado sobre el 6.0%.',
      '🟢 Crecimiento de ingresos publicitarios de Roundel > +20% anual aportando expansión estructural al margen bruto.'
    ],
    red_lines: [
      '🔴 Recaída de las ventas comparables en terreno negativo o aumento de pérdidas por hurto/merma de inventario.',
      '🔴 Compresión del margen operativo por debajo del 4.8% debido a guerras de precios promocionales.'
    ]
  },
  WMT: {
    name: 'Walmart Inc.',
    sector: 'Consumer Defensive / Global Omnichannel Retail, Grocery & Retail Media',
    industry: 'Discount Stores',
    exchange: 'NYSE',
    weights_scores: { f1: 8.30, f2: 8.85, f3: 8.35, f4: 9.45, f5: 8.60, f6: 8.90, f7: 8.30, f8: 9.40 },
    moat_desc: 'Mayor escala minorista y logística del mundo (>10,500 tiendas, liderazgo absoluto en alimentación en EE. UU., Sam’s Club) combinada con un flywheel digital de alto margen (Walmart Connect & Marketplace)',
    wacc: 7.5, g: 3.0,
    eps_growth_ntm_pct: 12.5,
    seg1_name: 'Walmart U.S. (Omnichannel Grocery, General Merchandise & Walmart Connect)', seg1_share: 0.685,
    seg2_name: 'Walmart International & Sam’s Club Warehouse', seg2_share: 0.315,
    guidance_summary: 'En Q3 FY27, Walmart reportó ingresos consolidados de $188,800M (+5.2% YoY) y un crecimiento del beneficio operativo del +16.0% YoY hasta $7,770M (BPA ajustado de $0.65), confirmando que el beneficio operativo crece más de tres veces más rápido que las ventas gracias a Walmart Connect, membresías Walmart+ y automatización de almacenes.',
    competitors: [
      {
        name: 'Amazon.com, Inc. (AMZN)',
        overlap: 'Comercio electrónico, entrega en el mismo día, marketplace de terceros y publicidad retail media',
        diff: 'Walmart tiene a menos de 10 millas de una tienda al 90% de la población de EE. UU., dominando el supermercado fresco (grocery) y utilizándolo como ancla de frecuencia semanal imposible de igualar.',
        moat: 'Excepcional'
      },
      {
        name: 'Costco Wholesale Corp. (COST) / Target Corp. (TGT)',
        overlap: 'Clubes de compras por membresía (Sam’s Club vs Costco) y grandes superficies de descuento',
        diff: 'Sam’s Club lidera en tecnología de tienda sin fricción (Scan & Go y arcos de salida con visión artificial), mientras Walmart U.S. capta hogares de más de $100,000 de renta anual.',
        moat: 'Excepcional'
      }
    ],
    bear_points: [
      'Múltiplo de valoración exigente (>35x PER Forward a $126.04), cotizando con una prima histórica significativa frente a su media de la última década.',
      'Márgenes operativos minoristas estructuralmente estrechos (4.1% en Q3 FY27) que requieren volúmenes colosales y ejecución logística perfecta.',
      'Volatilidad cambiaria e incertidumbre regulatoria en mercados internacionales clave como México (Walmex) e India (Flipkart/PhonePe).'
    ],
    bull_points: [
      'Inflexión estructural del modelo de negocio ("Flywheel de Alto Margen"): en Q3 FY27 los ingresos subieron un +5.2% hasta $188,800M, pero el beneficio operativo se disparó un +16.0% YoY hasta $7,770M.',
      'Aceleración de motores de alto margen: la publicidad global (Walmart Connect), las comisiones del Marketplace 3P y los ingresos por membresías (Walmart+ y Sam’s Club) ya representan una parte mayoritaria del crecimiento incremental del EBIT.',
      'Automatización con robótica e IA en centros de distribución (Symbotic), reduciendo el coste unitario de manipulación en más de un 20%.'
    ],
    green_lines: [
      '🟢 Crecimiento del beneficio operativo consolidado (EBIT) superando de forma consistente al crecimiento de ingresos (>8%–10% YoY).',
      '🟢 Crecimiento de Walmart Connect (Retail Media) > +25% YoY y e-commerce global rentable.'
    ],
    red_lines: [
      '🔴 Desaceleración de las ventas comparables de Walmart U.S. por debajo del +2.0% con pérdida de clientes de renta alta.',
      '🔴 Contracción del margen operativo consolidado por debajo del 3.6%.'
    ]
  },
  BRBR: {
    name: 'BellRing Brands, Inc.',
    sector: 'Consumer Defensive / Convenient Nutrition & Ready-to-Drink Protein',
    industry: 'Packaged Foods',
    exchange: 'NYSE',
    weights_scores: { f1: 8.40, f2: 7.80, f3: 8.10, f4: 8.35, f5: 8.20, f6: 8.15, f7: 7.70, f8: 8.25 },
    moat_desc: 'Marca líder #1 en batidos de proteína listos para beber (Premier Protein) y polvos nutricionales (Dymatize) con distribución dominante en clubes de compras y supermercados',
    wacc: 8.2, g: 3.0,
    eps_growth_ntm_pct: 18.0,
    seg1_name: 'Premier Protein (Ready-to-Drink Protein Shakes & Powders)', seg1_share: 0.855,
    seg2_name: 'Dymatize & PowerBar (Sports Nutrition & International)', seg2_share: 0.145,
    guidance_summary: 'En Q4 FY26, BellRing reportó ventas netas de $692.0M (+6.8% YoY; $2,398.4M en el año completo, +3.5% YoY), beneficio operativo de $67.8M (impactado por $16M de ajuste puntual de inventario) y BPA ajustado de $0.22, proyectando una aceleración en FY27 gracias a la nueva capacidad de co-manufactura y el viento de cola estructural de usuarios de GLP-1.',
    competitors: [
      {
        name: 'Fairlife (The Coca-Cola Company - KO) / Muscle Milk (PepsiCo - PEP)',
        overlap: 'Batidos de proteína listos para beber (RTD) en canales de gran consumo, clubes y conveniencia',
        diff: 'Premier Protein posee la mayor cuota de mercado en la categoría RTD de nutrición conveniente en Norteamérica, con una lealtad de marca y tasa de repetición de compra líder en Costco, Sam’s Club y Walmart.',
        moat: 'Alto'
      },
      {
        name: 'Glanbia plc (Optimum Nutrition) / Simply Good Foods (SMPL - Atkins/Quest)',
        overlap: 'Polvos de proteína de suero (Whey), barritas nutricionales y suplementos deportivos',
        diff: 'El modelo asset-light de BellRing (producción 100% subcontratada a una red diversificada de co-packers) le permite convertir una alta proporción de su EBITDA en flujo de caja libre.',
        moat: 'Alto'
      }
    ],
    bear_points: [
      'Impacto de $16M pre-impuestos por ajustes de inventario en Q4 FY26 y volatilidad en los costes de las proteínas lácteas (suero de leche y caseinato).',
      'Alta concentración de clientes minoristas, donde los clubes de compras (Costco y Sam’s Club) y Walmart representan una porción mayoritaria de la facturación.',
      'Intensificación de la competencia en los lineales por parte de Fairlife (Coca-Cola) y marcas blancas de distribuidores.'
    ],
    bull_points: [
      'Viento de cola secular por la adopción masiva de fármacos GLP-1 para pérdida de peso, cuyos pacientes requieren suplementación diaria de proteína de fácil digestión para evitar la pérdida de masa muscular.',
      'Resolución de las restricciones históricas de capacidad productiva mediante la incorporación de nuevos co-manufacturers en Norteamérica, permitiendo retomar promociones y lanzar nuevos formatos en FY27.',
      'Reacción muy positiva del mercado (+24% el día de resultados hasta $13.66) ante una valoración de múltiplo sumamente atractiva y fuerte generación de caja para recompras.'
    ],
    green_lines: [
      '🟢 Aceleración del crecimiento de ventas de Premier Protein > +10% YoY en FY27 gracias a mayor disponibilidad de inventario y promociones en clubes.',
      '🟢 Recuperación del margen EBITDA ajustado por encima del 19.5%.'
    ],
    red_lines: [
      '🔴 Pérdida de espacio de lineal o rotación en Costco / Sam’s Club frente a Fairlife o marcas propias.',
      '🔴 Inflación descontrolada en proteínas lácteas que comprima el margen bruto en más de 250 bps sin capacidad de traslado a precios.'
    ]
  },
  BJ: {
    name: "BJ's Wholesale Club Holdings, Inc.",
    sector: 'Consumer Defensive / Warehouse Club Membership Retail',
    industry: 'Discount Stores',
    exchange: 'NYSE',
    weights_scores: { f1: 7.80, f2: 8.10, f3: 7.95, f4: 8.20, f5: 8.10, f6: 8.15, f7: 7.40, f8: 8.50 },
    moat_desc: 'Densidad regional dominante de clubes de membresía en la Costa Este de EE. UU. (>245 clubes) con tasa de renovación del 90% y surtido híbrido de alimentación fresca',
    wacc: 7.8, g: 2.8,
    eps_growth_ntm_pct: 11.5,
    seg1_name: 'Merchandise Sales (Grocery, Perishables & General Merchandise)', seg1_share: 0.977,
    seg2_name: 'Membership Fee Revenue (~7.5M Members, 90% Renewal Rate)', seg2_share: 0.023,
    guidance_summary: 'BJ’s reportó en Q3 FY26 ingresos récord de $6,280M (+17.5% YoY), ventas comparables ex-gasolina del +4.1%, beneficio operativo de $313.8M (+43.7% YoY, impulsado por un acuerdo neto de litigio de tasas de intercambio de tarjetas) y un BPA de $1.73 (vs $1.26 estimado), elevando su guía para el ejercicio completo.',
    competitors: [
      {
        name: 'Costco Wholesale Corporation (COST)',
        overlap: 'Clubes de compras mayoristas por membresía anual en Estados Unidos',
        diff: 'BJ’s ofrece el doble de SKUs de supermercado (~7,000 vs ~4,000 de Costco) en envases más manejables para familias pequeñas, acepta cupones de fabricantes y tiene una densidad de tiendas 3x superior en Nueva Inglaterra y Nueva York.',
        moat: 'Alto'
      },
      {
        name: 'Sam’s Club (Walmart Inc. - WMT)',
        overlap: 'Clubes de descuento por membresía enfocados en ahorro familiar y gasolina',
        diff: 'BJ’s domina ubicaciones inmobiliarias estratégicas de difícil replicación en el corredor noreste de EE. UU. y ha integrado su cadena de frío propia (adquisición de Burris Logistics).',
        moat: 'Medio'
      }
    ],
    bear_points: [
      'Contracción de ~170 bps en el margen bruto subyacente de mercancías en Q3 FY26 debido a inversiones promocionales agresivas para captar tráfico y cuota de mercado.',
      'El fuerte batimiento de BPA ($1.73 vs $1.26) estuvo beneficiado por una ganancia neta extraordinaria del acuerdo de litigio por comisiones de intercambio de tarjetas de crédito (~$240M brutos menos ~$95M de reinversiones).',
      'Menor productividad de ventas por pie cuadrado y menor escala internacional que Costco.'
    ],
    bull_points: [
      'Crecimiento acelerado de ingresos (+17.5% YoY hasta $6,280M) y sólido aumento del +4.1% en ventas comparables de clubes (ex-gasolina) impulsado por ganancia de tráfico y unidades.',
      'Flujo de ingresos por cuotas de membresía de altísima visibilidad con una tasa de renovación récord del 90% y penetración creciente de niveles de membresía premium.',
      'Aceleración del ritmo de apertura de nuevos clubes en mercados de alto crecimiento del sureste y medio oeste de EE. UU.'
    ],
    green_lines: [
      '🟢 Estabilización del margen bruto de mercancías junto a un crecimiento de ingresos por cuotas de membresía > +8% YoY.',
      '🟢 Ventas comparables (ex-gas) sostenidas por encima del +3.0% con tasa de renovación >= 90%.'
    ],
    red_lines: [
      '🔴 Caída de la tasa de renovación de membresías por debajo del 87%.',
      '🔴 Deterioro continuado del margen bruto de mercancías (>100 bps anuales) sin retorno en tráfico recurrente.'
    ]
  },
  GLOB: {
    name: 'Globant S.A.',
    sector: 'Technology / AI-Native Digital Engineering & IT Services',
    industry: 'Information Technology Services',
    exchange: 'NYSE',
    weights_scores: { f1: 7.90, f2: 8.60, f3: 7.75, f4: 8.10, f5: 8.00, f6: 8.20, f7: 8.40, f8: 7.80 },
    moat_desc: 'Arquitectura ágil de "Studios" especializados en ingeniería de software digital, plataformas propietarias de agentes de IA (Globant Enterprise AI / GeneXus) y relaciones profundas con clientes Fortune 500',
    wacc: 9.8, g: 3.2,
    eps_growth_ntm_pct: 13.5,
    seg1_name: 'Digital & AI Studio Engineering (North America & Europe)', seg1_share: 0.785,
    seg2_name: 'Latin America & New Markets (Middle East / Sports & Media)', seg2_share: 0.215,
    guidance_summary: 'En Q3 2026, Globant reportó ingresos de $611.1M (-1.0% YoY, superando ligeramente el consenso de $610.9M), expandió su margen operativo ajustado secuencialmente al 14.1% y alcanzó un BPA ajustado de $1.48, acelerando su transición hacia contratos basados en consumo de tokens y agentes de IA (AI Pods).',
    competitors: [
      {
        name: 'EPAM Systems, Inc. (EPAM)',
        overlap: 'Ingeniería de productos de software, transformación digital y consultoría tecnológica global',
        diff: 'Globant cuenta con una base de talento predominantemente en América Latina (husos horarios alineados con EE. UU.), plataformas de software low-code/IA propias (GeneXus) y fuerte presencia en medios, entretenimiento y deportes (Disney, FIFA, F1).',
        moat: 'Alto'
      },
      {
        name: 'Accenture plc (ACN) / Endava plc (DAVA)',
        overlap: 'Implementación de inteligencia artificial empresarial, modernización cloud y experiencia digital',
        diff: 'Su cultura nativa de ingeniería por Studios y el nuevo modelo de suscripción por "AI Pods" permiten una entrega mucho más rápida que las consultoras tradicionales.',
        moat: 'Medio'
      }
    ],
    bear_points: [
      'Estancamiento temporal del crecimiento orgánico de ingresos (-1.0% YoY en Q3 2026 con $611.1M) debido a la cautela en presupuestos discrecionales de TI corporativos.',
      'Temor estructural del mercado a que las herramientas de codificación con IA generativa deflacionen las horas facturables del modelo tradicional Time & Materials (T&M), lo que ha comprimido la acción a ~$39.98 (<9x PER Forward).',
      'Presión cambiaria e inflación salarial en centros de desarrollo clave de América Latina (Argentina, Colombia, Brasil).'
    ],
    bull_points: [
      'Reinvención proactiva del modelo de negocio: Globant está canibalizando el modelo por horas mediante "AI Pods" y licencias de Globant Enterprise AI, donde cobra por resultados y velocidad de desarrollo.',
      'Resiliencia de márgenes y rentabilidad: pese al entorno macro adverso, el margen operativo ajustado se expandió al 14.1% y el BPA ajustado ($1.48) cumplió el consenso con conversión positiva de flujo de caja.',
      'Valoración de suelo histórico ($39.98 USD), ofreciendo un margen de seguridad muy amplio si los proyectos de arquitectura de datos para IA corporativa pasan de fase piloto a producción masiva en 2027.'
    ],
    green_lines: [
      '🟢 Retorno al crecimiento positivo de ingresos (>+6% YoY) impulsado por contratos de AI Studios y expansión en Europa/Oriente Medio.',
      '🟢 Sostenimiento del margen operativo ajustado en el rango del 14.5%–16.0%.'
    ],
    red_lines: [
      '🔴 Contracción de ingresos superior al -5% YoY por automatización de desarrollo interno en sus 10 mayores clientes.',
      '🔴 Caída del margen operativo ajustado por debajo del 12.0%.'
    ]
  },
  BABA: {
    name: 'Alibaba Group Holding Limited',
    sector: 'Consumer Cyclical / E-Commerce Ecosystem & AI Cloud Infrastructure',
    industry: 'Internet Retail',
    exchange: 'NYSE',
    weights_scores: { f1: 7.80, f2: 8.90, f3: 7.40, f4: 8.10, f5: 7.90, f6: 7.40, f7: 8.30, f8: 7.60 },
    moat_desc: 'Mayor ecosistema de comercio digital (Taobao/Tmall) e infraestructura de nube e IA (Alibaba Cloud / modelos Qwen) en China, respaldado por una masiva generación de caja y recompras',
    wacc: 10.5, g: 3.0,
    eps_growth_ntm_pct: 12.0,
    seg1_name: 'Taobao and Tmall Group & AIDC International Commerce', seg1_share: 0.610,
    seg2_name: 'Cloud Intelligence Group (AI & Cloud), Cainiao & Local Services', seg2_share: 0.390,
    guidance_summary: 'En el trimestre cerrado en septiembre (reportado el 19/11/2026), Alibaba alcanzó ingresos de RMB 271.52B (~$40,700M USD, +10% YoY), disparó su beneficio operativo GAAP un +443% YoY hasta RMB 29.1B (~$4,360M USD) impulsado por un crecimiento del +53% en productos de nube relacionados con IA, y continúa ejecutando recompras masivas de acciones.',
    competitors: [
      {
        name: 'PDD Holdings Inc. (PDD) / ByteDance (Douyin)',
        overlap: 'Comercio electrónico minorista, livestreaming shopping y publicidad de comerciantes en China',
        diff: 'Taobao y Tmall conservan la mayor cartera de marcas oficiales globales y el mayor poder adquisitivo por usuario, mejorando su tasa de monetización (take rate) mediante la herramienta publicitaria con IA Quanzhantui.',
        moat: 'Alto'
      },
      {
        name: 'Tencent Cloud (TCEHY) / Huawei Cloud / Baidu (BIDU)',
        overlap: 'Infraestructura de nube pública (IaaS/PaaS) y modelos fundacionales de IA en Asia',
        diff: 'Alibaba Cloud es el líder número uno en cuota de nube en China y su familia de modelos open-source Qwen lidera los benchmarks globales, acelerando los ingresos de IA al +53% YoY.',
        moat: 'Alto'
      }
    ],
    bear_points: [
      'El BPA Non-GAAP trimestral (RMB 8.10) quedó por debajo del consenso de analistas debido al aumento del CapEx en infraestructura de servidores de IA y subsidios selectivos en comercio internacional (AIDC).',
      'Riesgos geopolíticos, restricciones estadounidenses al acceso a chips de vanguardia y estructura societaria VIE.',
      'Entorno macroeconómico deflacionario y competencia intensa en el consumo minorista dentro de China continental.'
    ],
    bull_points: [
      'Fuerte aceleración operativa: los ingresos totales crecieron un +10% YoY hasta RMB 271.52B (~$40,700M USD) y el beneficio operativo GAAP se multiplicó por más de cinco (+443% YoY hasta RMB 29.1B / ~$4,360M USD).',
      'Alibaba Cloud se consolida como el motor de inteligencia artificial de China, con los ingresos de productos de IA creciendo un +53% YoY y expandiendo márgenes.',
      'Retorno agresivo de capital al accionista: recompras continuas que están reduciendo el número total de acciones en circulación a un ritmo superior al 4%–5% anual a múltiplos inferiores a 10x PER.'
    ],
    green_lines: [
      '🟢 Crecimiento sostenido de Alibaba Cloud > +15% YoY con ingresos de IA creciendo a más del +40% anual.',
      '🟢 Estabilización de la cuota de GMV de Taobao/Tmall con aumento del take-rate gracias a Quanzhantui.'
    ],
    red_lines: [
      '🔴 Pérdida acelerada de cuota de mercado en e-commerce doméstico frente a PDD o Douyin.',
      '🔴 Deterioro del flujo de caja libre anual por debajo de los $12,000M USD.'
    ]
  },
  JD: {
    name: 'JD.com, Inc.',
    sector: 'Consumer Cyclical / Direct Supply-Chain E-Commerce & Logistics',
    industry: 'Internet Retail',
    exchange: 'NASDAQ',
    weights_scores: { f1: 7.30, f2: 8.80, f3: 7.20, f4: 7.90, f5: 7.80, f6: 7.50, f7: 7.40, f8: 7.60 },
    moat_desc: 'Red logística y de almacenes propia inigualable en China (JD Logistics) con entrega en el mismo día/día siguiente y liderazgo en electrónica y electrodomésticos auténticos',
    wacc: 10.5, g: 2.5,
    eps_growth_ntm_pct: 11.0,
    seg1_name: 'JD Retail (1P Electronics, Home Appliances & General Supermarket)', seg1_share: 0.855,
    seg2_name: 'JD Logistics & New Businesses', seg2_share: 0.145,
    guidance_summary: 'En Q3 2026 (publicado el 17/11/2026), JD.com retornó al crecimiento positivo de ingresos (+3.5% YoY hasta RMB 309.6B / ~$46,200M USD), revirtió pérdidas operativas previas logrando un EBIT GAAP de RMB 5.2B (Non-GAAP de RMB 7.3B) y elevó su BPA diluido un +35.4% YoY hasta $0.68 ($0.88 Non-GAAP), apoyado en el programa gubernamental de renovación de electrodomésticos.',
    competitors: [
      {
        name: 'Alibaba Group Holding Ltd. (BABA)',
        overlap: 'Venta minorista online de electrónica, electrodomésticos y supermercado en China',
        diff: 'A diferencia del modelo marketplace de Alibaba, JD controla directamente el inventario (1P) y su propia flota de reparto con empleados en plantilla, garantizando autenticidad 100% y entregas en menos de 24 horas.',
        moat: 'Alto'
      },
      {
        name: 'PDD Holdings Inc. (PDD) / Meituan',
        overlap: 'Productos de gran consumo a bajo precio y entregas locales rápidas (instant retail)',
        diff: 'JD domina las categorías de ticket alto (electrodomésticos, ordenadores, smartphones) donde el consumidor prioriza la garantía oficial, la instalación en el hogar y el servicio postventa.',
        moat: 'Medio'
      }
    ],
    bear_points: [
      'Márgenes operativos estructuralmente bajos (1.7% GAAP y ~2.4% Non-GAAP en Q3 2026) propios de un modelo 1P intensivo en inventario y logística.',
      'Crecimiento de ingresos modesto (+3.5% YoY) condicionado por la debilidad del mercado inmobiliario chino, que frena la demanda orgánica de grandes electrodomésticos.',
      'Inversiones en entregas instantáneas y subsidios para defender cuota frente a PDD y Meituan.'
    ],
    bull_points: [
      'Fuerte recuperación de la rentabilidad en Q3 2026: paso de pérdidas operativas en Q3 2025 a un beneficio operativo GAAP de RMB 5.2B (Non-GAAP RMB 7.3B) y un salto del +35.4% YoY en el BPA GAAP ($0.68/ADS).',
      'Beneficiario directo de los estímulos estatales de China para el recambio ("trade-in") de electrodomésticos y equipos electrónicos eficientes.',
      'Cotización a múltiplos de liquidación (~$25.43 USD, <7x PER Forward) con balance muy líquido, dividendos crecientes y recompras activas.'
    ],
    green_lines: [
      '🟢 Expansión del margen operativo Non-GAAP de JD Retail por encima del 4.0% con aceleración de la categoría de supermercado.',
      '🟢 Crecimiento de ingresos consolidados superando el +6% YoY junto a recompras netas > 4% del capital anual.'
    ],
    red_lines: [
      '🔴 Regreso a pérdidas operativas trimestrales por guerras de subsidios en entregas locales o comercio minorista.',
      '🔴 Contracción de ingresos en la categoría core de electrónica y electrodomésticos.'
    ]
  },
  SMWB: {
    name: 'Similarweb Ltd.',
    sector: 'Technology / Digital Market Intelligence & Web Traffic Analytics SaaS',
    industry: 'Software - Application',
    exchange: 'NYSE',
    weights_scores: { f1: 7.40, f2: 8.20, f3: 8.10, f4: 7.80, f5: 7.50, f6: 7.80, f7: 8.00, f8: 7.80 },
    moat_desc: 'Base de datos propietaria de inteligencia digital, tráfico web y analítica de motores de búsqueda/IA generativa utilizada por más de 5,000 empresas globales bajo suscripción SaaS',
    wacc: 10.0, g: 3.5,
    eps_growth_ntm_pct: 28.0,
    seg1_name: 'Enterprise & Strategic Customer ARR (> $100k Subscriptions)', seg1_share: 0.610,
    seg2_name: 'SMB Digital Research, Sales, Shopper & Investor Intelligence', seg2_share: 0.390,
    guidance_summary: 'Similarweb logró un hito histórico en Q3 2026 (publicado el 17/11/2026): los ingresos aceleraron un +15.6% YoY hasta $83.0M, el beneficio operativo Non-GAAP se más que duplicó hasta $10.1M (margen del 12.2%, BPA Non-GAAP de $0.10 vs $0.08 estimado) y registró por primera vez en su historia como empresa cotizada beneficio operativo y beneficio neto positivos bajo normativa GAAP.',
    competitors: [
      {
        name: 'Semrush Holdings, Inc. (SEMR)',
        overlap: 'Herramientas SaaS de visibilidad online, SEO/SEM y análisis competitivo de marketing digital',
        diff: 'Similarweb domina el segmento Enterprise y fondos de inversión (Investor Intelligence) gracias a la precisión de su panel global multi-fuente para estimar tráfico real, conversión en marketplaces (Amazon) y tráfico derivado de LLMs.',
        moat: 'Alto'
      },
      {
        name: 'Sensor Tower (data.ai) / Comscore (SCOR)',
        overlap: 'Medición de audiencias digitales, tráfico móvil y benchmarking competitivo',
        diff: 'Similarweb ofrece una plataforma unificada que abarca web, apps móviles, búsqueda tradicional, retail media y visibilidad en motores de IA generativa (ChatGPT/Perplexity).',
        moat: 'Medio'
      }
    ],
    bear_points: [
      'Escala todavía mediana ($83.0M trimestrales / ~$330M anualizados) con gastos de compensación en acciones (SBC) que, aunque en descenso, requieren vigilancia.',
      'Ciclos de venta empresariales exigentes en clientes pequeños y medianos (SMB) que muestran mayor rotación (churn) que las cuentas Fortune 500.',
      'Cambios en políticas de privacidad de navegadores y sistemas operativos móviles que obligan a inversión constante en fuentes de datos.'
    ],
    bull_points: [
      'Inflexión hacia la rentabilidad GAAP en Q3 2026: primer trimestre con EBIT y beneficio neto GAAP positivos, mientras el EBIT Non-GAAP se duplicó con creces hasta $10.1M y los ingresos aceleraron al +15.6% YoY ($83.0M).',
      'Nuevo motor de crecimiento en IA: licenciamiento de sus datos de tráfico web en tiempo real para entrenar LLMs y nuevas herramientas (AI Traffic Analytics) para que las marcas midan su visibilidad en respuestas de IA generativa.',
      'Más del 60% del ARR proviene de grandes clientes Enterprise (>$100,000 anuales) bajo contratos plurianuales con NRR superior al 108%.'
    ],
    green_lines: [
      '🟢 Sostenimiento del crecimiento de ingresos > +15% YoY con expansión del margen operativo Non-GAAP por encima del 15%.',
      '🟢 Tasa de retención neta (NRR) en clientes de >$100k superando el 112%.'
    ],
    red_lines: [
      '🔴 Recaída en pérdidas operativas GAAP o caída de la tasa de retención neta global por debajo del 98%.',
      '🔴 Desaceleración del crecimiento de RPO y facturación por debajo del +8% YoY.'
    ]
  },
  API: {
    name: 'Agora, Inc.',
    sector: 'Technology / Real-Time Engagement (RTE) & Conversational AI Voice PaaS',
    industry: 'Software - Application',
    exchange: 'NASDAQ',
    weights_scores: { f1: 6.80, f2: 8.60, f3: 7.40, f4: 7.20, f5: 7.40, f6: 7.30, f7: 8.20, f8: 7.00 },
    moat_desc: 'Red global definida por software (SD-RTN) de ultra-baja latencia para transmisión de voz/video en tiempo real e integración con agentes de voz de IA conversacional, respaldada por amplia caja neta',
    wacc: 10.5, g: 3.0,
    eps_growth_ntm_pct: 25.0,
    seg1_name: 'Agora (International Real-Time Engagement & Conversational AI SDKs)', seg1_share: 0.535,
    seg2_name: 'Shengwang (China Real-Time Video, Audio & IoT PaaS)', seg2_share: 0.465,
    guidance_summary: 'En Q3 2026 (publicado el 16/11/2026), Agora logró su tercer trimestre consecutivo de aceleración de ingresos (+19.0% YoY hasta $42.1M) y su octavo trimestre consecutivo de beneficio neto GAAP positivo ($3.0M, BPA de $0.03 vs pérdida esperada de -$0.18), impulsado por la adopción de su Conversational AI Engine para agentes de voz en tiempo real.',
    competitors: [
      {
        name: 'Twilio Inc. (TWLO) / Vonage (Ericsson)',
        overlap: 'APIs de comunicaciones en la nube (CPaaS), voz programable y video en tiempo real',
        diff: 'Agora se especializa exclusivamente en transporte de audio y video bidireccional con latencia ultra-baja (<300ms) a través de su red SD-RTN, siendo ideal para agentes de voz de IA interactivos.',
        moat: 'Medio'
      },
      {
        name: 'Tencent RTC (TCEHY) / LiveKit / Daily.co',
        overlap: 'SDKs de transmisión de audio/video en vivo y conectividad WebRTC para aplicaciones de IA',
        diff: 'Agora ofrece SDKs optimizados con cancelación de ruido por IA y manejo de interrupciones en dispositivos IoT, juguetes inteligentes y call centers automatizados, además de una posición de caja neta superior a su capitalización.',
        moat: 'Medio'
      }
    ],
    bear_points: [
      'A pesar de alcanzar $3.0M de beneficio neto GAAP gracias a los ingresos por intereses de su tesorería, el resultado operativo GAAP siguió ligeramente en negativo (-$1.5M en Q3 2026).',
      'Escala reducida ($42.1M de ingresos trimestrales) y exposición regulatoria a la demanda de aplicaciones sociales y educativas en China (división Shengwang).',
      'Competencia de protocolos abiertos WebRTC y APIs directas lanzadas por proveedores de modelos de IA (OpenAI Realtime API).'
    ],
    bull_points: [
      'Clara inflexión fundamental en Q3 2026: los ingresos aceleraron al +19.0% YoY ($42.1M) por tercer trimestre consecutivo y logró su octavo trimestre seguido de beneficio neto GAAP positivo ($3.0M, BPA $0.03).',
      'Catalizador de IA Conversacional: el uso de minutos de transporte de voz de baja latencia para conectar usuarios humanos con agentes de IA generativa (atención al cliente, tutores virtuales, dispositivos IoT) está impulsando la expansión de clientes.',
      'Balance blindado con más de $350M en efectivo e inversiones a corto plazo frente a una capitalización bursátil deprimida (~$300M a $4.01/ADS), cotizando prácticamente a valor de su caja neta.'
    ],
    green_lines: [
      '🟢 Alcanzar beneficio operativo GAAP positivo de forma sostenida con crecimiento de ingresos > +20% YoY impulsado por minutos de IA conversacional.',
      '🟢 Tasa de expansión neta en dólares (Dollar-Based Net Retention Rate) > 105% en la división internacional Agora.'
    ],
    red_lines: [
      '🔴 Desaceleración del crecimiento de ingresos por debajo del +5% YoY o retorno a pérdidas netas GAAP.',
      '🔴 Consumo de caja operativa que erosione su posición de tesorería neta.'
    ]
  }
};
