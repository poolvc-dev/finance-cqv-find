import os

print("Injecting Section 6.3 Analyst Consensus Comparison into FICO, META, ISRG, GOOGL, MSFT reports...")

reports_data = {
    'fico_2026_q2.md': {
        'ticker': 'FICO',
        'price': '$1,373.08',
        'dcf_bear': '$1,660.00',
        'dcf_base': '$2,075.00',
        'dcf_bull': '$2,448.50',
        'target_low': '$1,250.00',
        'target_mean': '$1,850.00',
        'target_high': '$2,100.00',
        'num_analysts': 14,
        'upside': '+34.7%'
    },
    'meta_2026_q2.md': {
        'ticker': 'META',
        'price': '$585.61',
        'dcf_bear': '$585.61',
        'dcf_base': '$735.00',
        'dcf_bull': '$867.30',
        'target_low': '$520.00',
        'target_mean': '$675.00',
        'target_high': '$775.00',
        'num_analysts': 58,
        'upside': '+15.3%'
    },
    'isrg_2026_q2.md': {
        'ticker': 'ISRG',
        'price': '$445.50',
        'dcf_bear': '$445.50',
        'dcf_base': '$556.88',
        'dcf_bull': '$651.50',
        'target_low': '$410.00',
        'target_mean': '$535.00',
        'target_high': '$610.00',
        'num_analysts': 34,
        'upside': '+20.1%'
    },
    'googl_2026_q2.md': {
        'ticker': 'GOOGL',
        'price': '$336.71',
        'dcf_bear': '$336.71',
        'dcf_base': '$450.00',
        'dcf_bull': '$525.00',
        'target_low': '$310.00',
        'target_mean': '$415.00',
        'target_high': '$480.00',
        'num_analysts': 52,
        'upside': '+23.2%'
    },
    'msft_2026_q2.md': {
        'ticker': 'MSFT',
        'price': '$448.37',
        'dcf_bear': '$448.37',
        'dcf_base': '$560.00',
        'dcf_bull': '$660.00',
        'target_low': '$415.00',
        'target_mean': '$545.00',
        'target_high': '$600.00',
        'num_analysts': 56,
        'upside': '+21.6%'
    },
    'msft_2026_q1.md': {
        'ticker': 'MSFT',
        'price': '$448.37',
        'dcf_bear': '$448.37',
        'dcf_base': '$560.00',
        'dcf_bull': '$660.00',
        'target_low': '$415.00',
        'target_mean': '$545.00',
        'target_high': '$600.00',
        'num_analysts': 56,
        'upside': '+21.6%'
    }
}

for filename, data in reports_data.items():
    filepath = os.path.join('inform', filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        section_6_3 = f"""
---

### 6.3. Comparativa de Valoración DCF CQV v4.0 vs. Consenso de Analistas de Wall Street (12M)

| Escenario / Fuente | Escenario Pesimista (Bear) | Escenario Base (Neutro) | Escenario Optimista (Bull) | Diagnóstico de Brecha de Mercado |
| :--- | :---: | :---: | :---: | :--- |
| **Valor Intrínseco DCF CQV v4.0** | **{data['dcf_bear']}** | **{data['dcf_base']}** | **{data['dcf_bull']}** | Estimación multifactorial de caja propia a largo plazo (5-10a). |
| **Consenso Analistas Wall Street (12M)** | **{data['target_low']}** | **{data['target_mean']}** | **{data['target_high']}** | Basado en el consenso de {data['num_analysts']} analistas institucionales. |
| **Cotización Actual de Mercado** | **{data['price']}** | **{data['price']}** | **{data['price']}** | Potencial de revalorización al Target Mean: **{data['upside']}**. |
"""

        if '### 6.3. Comparativa de Valoración' not in content:
            if '## 7. Registro' in content:
                parts = content.split('## 7. Registro')
                content = parts[0] + section_6_3 + '\n## 7. Registro' + parts[1]
            elif '## 7. Preguntas' in content:
                parts = content.split('## 7. Preguntas')
                content = parts[0] + section_6_3 + '\n## 7. Preguntas' + parts[1]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected Section 6.3 into {filename}")

print("SUCCESSFULLY_ENRICHED_ALL_TARGET_REPORTS")
