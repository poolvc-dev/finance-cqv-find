import re
import os

red_lines_by_ticker = {
    "MSFT": [
        "Desaceleración estructural del crecimiento de ingresos de Azure por debajo del +18.0% YoY en moneda constante durante dos trimestres consecutivos, evidenciando pérdida de cuota de mercado en cargas de trabajo de IA empresarial frente a AWS o Google Cloud.",
        "Ruptura o conflicto estratégico en la alianza con OpenAI sin un reemplazo equivalente en modelos de frontera propietarios, o comoditización del software Copilot con tasas de adopción corporativa inferiores al 10% de la base instalada de Office 365.",
        "Compresión severa del margen operativo por debajo del 38.0% derivada de un sobre-dimensionamiento improductivo del CapEx en centros de datos de IA con retornos sobre capital decrecientes."
    ],
    "GOOGL": [
        "Resolución judicial definitiva antimonopolio del Departamento de Justicia de EE.UU. (DoJ) que ordene la escisión forzosa de activos nucleares (Chrome o Android) o la prohibición de acuerdos de distribución de búsqueda con Apple sin una alternativa viable de tráfico.",
        "Contracción estructural de los ingresos publicitarios de Google Search (crecimiento negativo o plano) provocada por la migración masiva de usuarios hacia interfaces conversacionales de respuesta directa que eliminen la monetización por enlaces patrocinados.",
        "Desaceleración abrupta de Google Cloud por debajo del +15.0% YoY junto con una contracción del ROIC corporativo por debajo del 20.0% durante más de dos ejercicios fiscales consecutivos."
    ],
    "V": [
        "Aprobación y entrada en vigor de la Credit Card Competition Act en EE.UU. o normativas globales que impongan un enrutamiento obligatorio por redes alternativas de bajo coste o un tope regulatorio a las tasas de intercambio crediticio.",
        "Desintermediación sustancial del volumen de pagos mediante la adopción corporativa y minorista masiva de pagos directos cuenta a cuenta (A2A), sistemas estatales instantáneos (FedNow/Pix) o liquidaciones nativas en blockchain que eludan VisaNet.",
        "Caída sostenida del crecimiento del volumen total de pagos procesados por debajo del +4.0% nominal interanual, reflejando pérdida de relevancia frente a billeteras cerradas o competidores locales."
    ],
    "NOW": [
        "Desaceleración del crecimiento de los ingresos por suscripción por debajo del +16.0% YoY en moneda constante o contracción de la tasa de renovación anual por debajo del 95.0% (actualmente en 98.5%).",
        "Captura de la capa frontal de interacción (front-end user experience) por parte de agentes autónomos de Microsoft Copilot o Salesforce Agentforce, relegando a ServiceNow a una base de datos secundaria (backend) y destruyendo su poder de fijación de precios.",
        "Destrucción de ingresos por licencias de usuario (seat-based pricing) provocada por la automatización con IA que no logre ser compensada por el modelo de consumo de Now Assist (contracción del margen de flujo de caja libre por debajo del 25.0%)."
    ],
    "KLAC": [
        "Bloqueo regulatorio y geopolítico absoluto a la exportación de herramientas de inspección óptica y metrología hacia fundiciones chinas, sin compensación de volumen por la construcción de fabs en EE.UU., Taiwán o Europa.",
        "Pérdida perceptible de cuota de mercado en inspección de obleas por debajo del 50.0% (actualmente >55%) frente a Applied Materials o ASML en la adopción de arquitecturas de transistores GAA (Gate-All-Around) y nodos sub-2nm.",
        "Recorte abrupto superior al 35.0% en el presupuesto anual de capex de sus dos mayores clientes combinados (TSMC y Samsung), provocando una caída del margen bruto por debajo del 56.0%."
    ],
    "ODFL": [
        "Deterioro estructural del Operating Ratio (OR) por encima del 78.0% durante tres trimestres consecutivos en un entorno macroeconómico ordinario, señalando pérdida de eficiencia operativa en la red LTL.",
        "Inicio de una guerra de precios destructiva en el sector de transporte fraccionado que obligue a Old Dominion a conceder descuentos que reduzcan el ingreso por quintal (revenue per hundredweight) por debajo de la inflación de costes laborales.",
        "Aumento del ratio de reclamaciones por carga dañada o pérdida por encima del 0.4% del volumen transportado (destruyendo su foso de servicio prémium de fiabilidad)."
    ],
    "BSX": [
        "Retirada obligatoria del mercado (FDA Class I recall) o hallazgos clínicos de complicaciones adversas graves no anticipadas en sus dispositivos estrella Farapulse (PFA) o Watchman FLX.",
        "Pérdida de cuota de mercado en electrofisiología frente a tecnologías de ablación por campo pulsado de competidores (Medtronic, Johnson & Johnson) que demuestren superioridad clínica demostrada.",
        "Caída del crecimiento orgánico de ventas por debajo del +6.0% interanual o aumento del apalancamiento financiero por encima de 3.5x Deuda Neta/EBITDA debido a adquisiciones inorgánicas fallidas."
    ],
    "ORLY": [
        "Ruptura de su racha histórica con ventas comparables en tiendas existentes (comp store sales) negativas durante dos trimestres consecutivos, indicando pérdida de cuota frente a AutoZone o canales digitales.",
        "Contracción del margen bruto por debajo del 49.0% provocada por incapacidad de trasladar la inflación de proveedores o guerras de precios en el segmento comercial de talleres (DIFM).",
        "Deterioro de la cadena de suministro y logística hub-and-spoke que eleve los tiempos medios de entrega a talleres mecánicos por encima de 2.5 horas, eliminando su principal foso competitivo."
    ],
    "KO": [
        "Caída estructural del volumen de cajas unitarias (crecimiento negativo de volumen durante más de 4 trimestres consecutivos) acelerada por cambios de hábitos de consumo y la adopción masiva de fármacos GLP-1.",
        "Implementación coordinada a nivel global de impuestos punitivos sobre bebidas carbonatadas y azucaradas que el portafolio Zero Sugar y de reformulación no logre neutralizar.",
        "Incapacidad de trasladar la inflación de costes de edulcorantes, aluminio y empaque a precios finales, provocando una compresión del margen operativo comparable por debajo del 25.0%."
    ],
    "SPGI": [
        "Pérdida, suspensión o revocación de la designación como agencia de calificación reconocida a nivel nacional (NRSRO) por parte de la SEC o de reguladores financieros internacionales en ESMA.",
        "Congelamiento prolongado de la emisión de deuda corporativa y bonos de grado de inversión a nivel mundial durante más de 6 trimestres debido a una crisis sistémica de liquidez o tipos restrictivos.",
        "Migración masiva de fondos cotizados (ETFs) y fondos institucionales fuera de la familia de índices S&P hacia autoindexación de gestoras de activos (BlackRock, Vanguard) o índices de coste cero."
    ],
    "VRT": [
        "Cancelación o congelamiento masivo del capex de centros de datos de IA por parte de los hiperescaladores (Microsoft, Google, AWS, Meta), provocando una caída superior al 30% en la cartera de pedidos (backlog).",
        "Pérdida de los diseños de referencia (design wins) de refrigeración líquida directa al chip para los aceleradores de IA de próxima generación (NVIDIA Rubin y ASICs de hiperescala) en favor de Schneider Electric o Eaton.",
        "Problemas de calidad o cuellos de botella en la entrega de módulos de potencia y distribución térmica que compriman el margen operativo ajustado por debajo del 14.0%."
    ],
    "CDNS": [
        "Disrupción del duopolio de automatización de diseño electrónico (EDA) por herramientas de código abierto impulsadas por IA o software propietario desarrollado internamente por los grandes fabricantes de chips (Apple, Google, NVIDIA).",
        "Bloqueo geopolítico integral que prohíba la venta de licencias EDA y bloques de propiedad intelectual (IP) a todos los clientes asiáticos sin una compensación proporcional de gasto en fundiciones de EE.UU. y Europa.",
        "Desaceleración del crecimiento del backlog contratado por debajo del +8.0% interanual o compresión del margen operativo por debajo del 34.0%."
    ],
    "TSM": [
        "Conflicto bélico o bloqueo naval militar en el estrecho de Taiwán que interrumpa físicamente las operaciones de fabricación de las Gigafabs de Hsinchu, Taichung o Tainan.",
        "Retraso tecnológico material en el nodo N2 (2nm GAA) o rendimientos de fabricación defectuosos (yields < 40%) que permitan a Samsung o Intel Foundry capturar contratos de vanguardia de Apple o NVIDIA.",
        "Sobrecostes incontrolados e insostenibles en la construcción y operación de las fábricas internacionales (Arizona Fab 21 y Dresden ESMC) que compriman el margen bruto consolidado por debajo del 50.0%."
    ],
    "JPM": [
        "Pérdida del 'balance tipo fortaleza': deterioro abrupto del ratio de capital CET1 por debajo del 13.0% debido a pérdidas crediticias imprevistas en carteras de crédito comercial o inmobiliario.",
        "Regulación bancaria punitiva (ej. implementación estricta de Basilea III Endgame sin mitigaciones) que exija una retención excesiva de capital y reduzca estructuralmente el ROTCE por debajo del 14.0%.",
        "Fuga masiva de depósitos no remunerados de clientes minoristas hacia fondos del mercado monetario o fintechs alternativas que obligue a encarecer drásticamente el coste de financiación bancaria."
    ],
    "UNH": [
        "Aumento sostenido e incontrolado del ratio de costes médicos (Medical Loss Ratio - MLR) por encima del 86.5% durante más de tres trimestres consecutivos sin capacidad de trasladarlo a primas.",
        "Recortes severos por parte del gobierno federal de EE.UU. a las tarifas de reembolso de Medicare Advantage o prohibición regulatoria de modelos de integración vertical entre aseguradoras y farmacias de especialidad (PBMs / Optum Rx).",
        "Fallos catastróficos de ciberseguridad o interrupción operativa prolongada en la red de procesamiento de pagos clínicos de Optum Insight que destruyan la confianza institucional."
    ],
    "PGR": [
        "Deterioro continuado del Ratio Combinado (Combined Ratio) por encima del 96.0% durante un ejercicio anual completo, señalando pérdida del rigor actuarial o deficiencias en la tarificación telemática (Snapshot).",
        "Frecuencia y severidad extrema de desastres climáticos (huracanes consecutivos en Florida y costa este) que agoten las coberturas de reaseguro y erosionen el superávit de capital regulatorio.",
        "Pérdida del ritmo de crecimiento de pólizas personales en vigor (PIF) con fuga masiva de asegurados hacia GEICO o State Farm debido a sobreprecios en la renovación."
    ],
    "BLK": [
        "Salidas netas estructurales continuadas de activos bajo gestión (AUM) durante más de dos trimestres consecutivos en la división de fondos cotizados iShares.",
        "Pérdida de mandatos institucionales clave o fallos regulatorios en la plataforma Aladdin que provoquen la cancelación de licencias por parte de grandes bancos centrales y entidades financieras.",
        "Fracaso en la integración de activos privados e infraestructuras (Global Infrastructure Partners) con compresión del margen operativo por debajo del 38.0%."
    ],
    "FAST": [
        "Caída continuada de las ventas diarias promedio por encima del 3.0% durante más de tres trimestres provocada por una contracción manufacturera profunda en EE.UU.",
        "Ralentización severa en la firma e instalación de nuevos contratos Onsite (menos de 60 aperturas por trimestre) y caída en la tasa de utilización de dispositivos automatizados FASTVend.",
        "Compresión del margen operativo por debajo del 18.0% provocada por inflación logística o guerras de precios con distribuidores industriales competidores (Grainger, MSC Industrial)."
    ],
    "IBKR": [
        "Pérdidas operativas o de contrapartida masivas provocadas por movimientos extremos de mercado que superen la capacidad de liquidación automática de márgenes en tiempo real de su motor de riesgos.",
        "Recortes agresivos de tipos de interés a nivel global por debajo del 1.5% que reduzcan los ingresos netos por intereses en más de un 40% sin que el crecimiento del volumen de trading logre compensarlo.",
        "Fallos técnicos o regulatorios severos en su infraestructura de SmartRouting que comprometan la ejecución de órdenes institucionales en mercados clave."
    ],
    "BAC": [
        "Compresión prolongada del margen neto de intermediación (NIM) por debajo del 1.80% combinada con pérdidas no realizadas en carteras HTM que restrinjan la capacidad de retorno de capital a los accionistas.",
        "Aumento brusco de las provisiones por insolvencias en tarjetas de crédito y préstamos comerciales que sitúe el ratio de morosidad por encima del 2.5% de la cartera total.",
        "Pérdida de cuota de mercado en depósitos minoristas esenciales de bajo coste frente a bancos regionales o plataformas digitales, forzando un encarecimiento estructural del fondeo."
    ],
    "FTNT": [
        "Pérdida perceptible de cuota de mercado en la convergencia hacia Unified SASE y SecOps, reflejada en un crecimiento de los ingresos por servicios inferior al +8.0% interanual que evidencie fracaso en la transición fuera de la red local.",
        "Desaceleración estructural del crecimiento de la facturación contratada (Total Billings) por debajo del +10.0% interanual o compresión del margen operativo por debajo del 30.0% durante dos trimestres consecutivos ante guerras de precios destructivas en hardware.",
        "Vulnerabilidad crítica recurrente de día cero (Zero-Day) en el núcleo de FortiOS que provoque deserciones masivas de clientes Fortune 500 y dañe irreparablemente la reputación de confianza corporativa."
    ]
}

RED_LINES_MAP = {
    ticker: "\n".join([f"{i+1}. {line}" for i, line in enumerate(lines)])
    for ticker, lines in red_lines_by_ticker.items()
}

def update_redlines():
    print("=== ENRIQUECIMIENTO Y PERSONALIZACIÓN DE LÍNEAS ROJAS (SECCIÓN 4.3) ===")
    updated = 0
    for ticker, lines in red_lines_by_ticker.items():
        filepath = f"inform/cqv_v5/{ticker}_2026_P3_CQVv5.md"
        if not os.path.exists(filepath):
            print(f"No existe: {filepath}")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        formatted_lines = "\n".join([f"{i+1}. {line}" for i, line in enumerate(lines)])
        new_section_4_3 = f"### 4.3. Líneas Rojas y Condiciones de Ruptura de Tesis\n{formatted_lines}\n"

        # Regex para localizar 4.3 hasta el siguiente ## 5.
        if "### 4.3. Líneas Rojas" in content or "### 4.3. L" in content:
            new_content = re.sub(
                r'### 4\.3\..*?(?=---\s*\n\s*## 5\.|\n## 5\.)',
                new_section_4_3 + "\n",
                content,
                flags=re.DOTALL
            )
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated += 1
            print(f"[OK] {ticker}: Líneas rojas personalizadas actualizadas.")
        else:
            print(f"[Alerta] No se encontró Sección 4.3 en {ticker}")

    print(f"\nFinalizado: {updated} informes actualizados con líneas rojas personalizadas.")

if __name__ == '__main__':
    update_redlines()
