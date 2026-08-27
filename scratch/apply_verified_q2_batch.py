import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data_path = root / 'cqv_data.json'
data = json.loads(data_path.read_text(encoding='utf-8'))

base = {
    'f1': None, 'f2': None, 'f3': None, 'f4': None,
    'f5': None, 'f6': None, 'f7': None, 'f8': None,
    'cqv_v1': None, 'cqv_v1_1': None, 'cqv_v2': None,
    'cqv_v3': None, 'cqv_v4': None, 'cqv': None,
    'value_score': None, 'peg_bruto': None, 'score_peg': None,
    'intrinsic_value': None, 'mos_pct': None,
    'owner_earnings': None, 'fcf_yield_pct': None,
    'score_fcf_yield': None, 'score_mos': None,
    'verdict': 'N/D - factores CQV incompletos',
    'clasificacion': 'N/D',
    'data_confidence': 'Alta para resultados publicados; N/D para CQV completo',
    'quarter': 'Q2 2026',
    'status': 'Q2 2026 actualizado con datos oficiales; CQV N/D por factores no documentados',
}

records = {
    'HCA': {
        **base,
        'ticker': 'HCA', 'name': 'HCA Healthcare, Inc.', 'sector': 'Healthcare',
        'price': 382.19, 'price_currency': 'USD', 'price_market': 'NYSE',
        'publication_date': '2026-07-24', 'valuation_date': '2026-07-24', 'price_date': '2026-07-24',
        'revenue': 20230.0, 'net_income': 1699.0, 'operating_income': None,
        'eps': 7.62, 'ocf': 2335.0, 'maintenance_capex': None,
        'cash': 1013.0, 'shares_diluted_m': 222.828,
        'price_source': 'https://investor.hcahealthcare.com/stock-information/default.aspx',
        'sources': [
            'https://investor.hcahealthcare.com/news/news-details/2026/HCA-Healthcare-Reports-Second-Quarter-2026-Results/default.aspx',
            'https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm',
        ],
    },
    'TSLA': {
        **base,
        'ticker': 'TSLA', 'name': 'Tesla, Inc.', 'sector': 'Consumer Cyclical',
        'price': 374.01, 'price_currency': 'USD', 'price_market': 'NASDAQ',
        'publication_date': '2026-07-22', 'valuation_date': '2026-07-22', 'price_date': '2026-07-22',
        'revenue': 28236.0, 'net_income': 1114.0, 'operating_income': 398.0,
        'eps': 0.32, 'ocf': None, 'maintenance_capex': None,
        'cash': 16425.0, 'debt': 9342.0, 'shares_outstanding_m': 3949.547,
        'price_source': 'https://ir.tesla.com/press-release/tesla-releases-second-quarter-2026-financial-results',
        'sources': [
            'https://ir.tesla.com/press-release/tesla-releases-second-quarter-2026-financial-results',
            'https://www.sec.gov/Archives/edgar/data/1318605/000162828026049270/tsla-20260630.htm',
            'https://chartexchange.com/symbol/nasdaq-tsla/historical/',
        ],
    },
}

for ticker, record in records.items():
    matches = [i for i, item in enumerate(data) if item.get('ticker') == ticker]
    if len(matches) != 1:
        raise RuntimeError(f'{ticker}: se esperaba exactamente un registro, encontrados {len(matches)}')
    data[matches[0]] = record

data_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

reports = {
    'hca_2026_q2.md': '''# Informe de Tesis de Inversión: HCA Healthcare, Inc. (HCA) - Q2 2026
**Fecha de emisión:** 21/08/2026  
**Fecha de publicación del resultado:** 24/07/2026  
**Fecha de valoración y precio utilizado:** 24/07/2026 — cierre NYSE $382.19  
**Fuentes:** [IR Q2 2026](https://investor.hcahealthcare.com/news/news-details/2026/HCA-Healthcare-Reports-Second-Quarter-2026-Results/default.aspx), [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm), [precio histórico IR](https://investor.hcahealthcare.com/stock-information/default.aspx)

## Salida CQV v4.0

| Métrica | Resultado |
|---|---:|
| CQV calidad F1-F8 | N/D |
| PEG bruto / PEG normalizado | N/D / N/D |
| Value Score | N/D |
| Valor intrínseco / margen de seguridad | N/D / N/D |
| Veredicto | **N/D — no recomendación afirmativa** |

El informe incorpora únicamente datos publicados y verificables. No se asignan puntuaciones F1-F8 porque este lote no contiene todavía la evidencia completa y homogénea exigida por CQV v4.0 para rentabilidad histórica, deuda, crecimiento durable, moat, asignación de capital, dirección, opcionalidad y recurrencia.

## Resultados Q2 2026

| Métrica | Q2 2026 |
|---|---:|
| Ingresos | $20,230 M |
| Beneficio neto atribuible | $1,699 M |
| BPA diluido | $7.62 |
| Flujo de caja operativo | $2,335 M |
| CapEx de mantenimiento / FCF CQV | N/D |
| Caja | $1,013 M |

La compañía publicó los resultados el 24/07/2026. La valoración usa el cierre de esa misma fecha, conforme a la regla de fecha de publicación; no se sustituye por el precio actual.

## Limitaciones y decisión

No se calcula DCF, Owner Earnings, FCF Yield, PEG ni margen de seguridad porque faltan datos homogéneos de mantenimiento CapEx, crecimiento EPS NTM y demás insumos de valoración. Por tanto, el resultado operativo es **N/D** y no debe interpretarse como Comprar, Acumular, Mantener o Evitar.
''',
    'tsla_2026_q2.md': '''# Informe de Tesis de Inversión: Tesla, Inc. (TSLA) - Q2 2026
**Fecha de emisión:** 21/08/2026  
**Fecha de publicación del resultado:** 22/07/2026  
**Fecha de valoración y precio utilizado:** 22/07/2026 — cierre NASDAQ $374.01  
**Fuentes:** [IR Q2 2026](https://ir.tesla.com/press-release/tesla-releases-second-quarter-2026-financial-results), [SEC 10-Q](https://www.sec.gov/Archives/edgar/data/1318605/000162828026049270/tsla-20260630.htm), [precio histórico](https://chartexchange.com/symbol/nasdaq-tsla/historical/)

## Salida CQV v4.0

| Métrica | Resultado |
|---|---:|
| CQV calidad F1-F8 | N/D |
| PEG bruto / PEG normalizado | N/D / N/D |
| Value Score | N/D |
| Valor intrínseco / margen de seguridad | N/D / N/D |
| Veredicto | **N/D — no recomendación afirmativa** |

El informe usa datos oficiales del periodo terminado el 30/06/2026. No se asignan puntuaciones F1-F8 sin completar la evidencia histórica y cualitativa requerida por CQV v4.0. Los importes de caja y deuda se conservan como datos publicados; no se convierten en una puntuación.

## Resultados Q2 2026

| Métrica | Q2 2026 |
|---|---:|
| Ingresos | $28,236 M |
| Beneficio operativo | $398 M |
| Beneficio neto atribuible | $1,114 M |
| BPA diluido | $0.32 |
| Flujo de caja operativo trimestral | N/D — el 10-Q presentado no desglosa aquí el dato trimestral aislado |
| CapEx de mantenimiento / FCF CQV | N/D |
| Caja, equivalentes y restringida | $16,425 M |
| Deuda y arrendamientos financieros | $9,342 M |

Tesla publicó el resultado después del cierre del 22/07/2026. Se conserva el cierre de esa fecha como precio de valoración, sin usar el movimiento posterior del 23/07/2026.

## Limitaciones y decisión

No se calcula DCF, Owner Earnings, FCF Yield, PEG ni margen de seguridad. El dato de flujo de caja disponible en el 10-Q es acumulado de seis meses, no un Q2 aislado; no se resta ni se presenta como flujo trimestral. La salida es **N/D** y queda detenida cualquier recomendación afirmativa.
'''
}
for filename, content in reports.items():
    (root / 'inform' / filename).write_text(content, encoding='utf-8')
print('Datos y dos informes verificados preparados.')
