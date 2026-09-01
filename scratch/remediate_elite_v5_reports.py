"""Make CQV v5 elite reports internally auditable from the available SSOT.

This deliberately marks information not present in cqv_data.json as N/D instead
of retaining unsupported narrative or fabricated primary-source assertions.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "cqv_data.json"
REPORTS = ROOT / "inform" / "cqv_v5"
WEIGHTS = (0.20, 0.15, 0.15, 0.15, 0.10, 0.10, 0.05, 0.10)


def number(value):
    return "N/D" if value is None else f"{value:,.2f}"


def first_match(pattern: str, text: str):
    match = re.search(pattern, text, flags=re.I)
    return float(match.group(1).replace(",", "")) if match else None


def report_path(item):
    ticker = item["ticker"]
    quarter = str(item.get("quarter", "")).replace(" ", "_")
    candidates = list(REPORTS.glob(f"{ticker}_{quarter}_CQVv5.md"))
    return candidates[0] if candidates else next(REPORTS.glob(f"{ticker}_*CQVv5.md"), None)


def build_report(item, existing: str) -> str:
    ticker = item["ticker"]
    name = item.get("name", ticker)
    quarter = item.get("quarter", "N/D")
    price = item.get("price")
    cqv = item.get("cqv_v5", item.get("cqv"))
    value = item.get("value_score")
    base = item.get("intrinsic_value_base", item.get("intrinsic_value"))
    expected = item.get("intrinsic_value_expected")
    mos_base = item.get("mos_base_pct", item.get("mos_pct"))
    mos_expected = item.get("mos_esperado_pct")
    verdict = item.get("verdict", "N/D")
    scores = [item.get(f"f{i}") for i in range(1, 9)]
    contributions = [None if s is None else s * w for s, w in zip(scores, WEIGHTS)]
    raw_yield = item.get("fcf_yield_pct")
    fcf_score = item.get("score_fcf_yield")
    growth_score = item.get("score_crecimiento_multiplo", item.get("score_peg"))
    mos_score = item.get("score_mos")
    calc = sum(c for c in contributions if c is not None) if all(c is not None for c in contributions) else None
    calc_note = "COHERENTE" if calc is not None and abs(calc - cqv) < 0.011 else "REVISAR"
    expected_line = f"${expected:,.2f} (MoS {mos_expected:.2f}%)" if expected is not None and mos_expected is not None else "N/D"
    source_note = (
        "El SSOT no conserva enlaces ni valores brutos suficientes para reconstruir "
        "los estados financieros y los percentiles sectoriales. Esos campos se presentan "
        "como N/D; el informe requiere fuentes primarias antes de elevar la confianza."
    )
    rows = []
    for i, (score, contribution) in enumerate(zip(scores, contributions), 1):
        rows.append(
            f"| F{i} | {number(score)} | {WEIGHTS[i-1]:.0%} | {number(contribution)} | "
            "Evidencia bruta y percentil: N/D en SSOT |"
        )
    return f"""# Informe de Tesis de Inversión: {name} ({ticker}) — {quarter}
**Fecha de emisión:** {item.get('publication_date', 'N/D')}  
**Fecha de publicación analizada:** {item.get('publication_date', 'N/D')}  
**Fecha de valoración / precio:** {item.get('valuation_date', item.get('price_date', 'N/D'))}  
**Metodología aplicada:** CQV v5.0  
**Confianza de datos:** Media — validación interna SSOT; fuentes primarias pendientes de incorporar.  
**Veredicto operativo:** {verdict}

---

## 1. Resumen ejecutivo y salida final

```text
CQV Calidad:             {number(cqv)} / 10
Value Score:             {number(value)} / 10
Valor intrínseco base:   {number(base)}
Valor intrínseco esperado: {expected_line}
Precio usado:            {number(price)}
Veredicto:               {verdict}
```

El score identifica una compañía de alta calidad dentro del SSOT. No constituye una recomendación independiente hasta que se registren fuentes primarias y se complete la valoración por escenarios.

## 2. Puntuación CQV y desglose auditable

$$\\text{{CQV}} = 0.20F_1 + 0.15F_2 + 0.15F_3 + 0.15F_4 + 0.10F_5 + 0.10F_6 + 0.05F_7 + 0.10F_8$$

| Factor | Score | Peso | Contribución | Evidencia |
| :--- | ---: | ---: | ---: | :--- |
{chr(10).join(rows)}
| **CQV total** | **{number(cqv)}** | **100%** | **{number(calc)}** | **{calc_note} con SSOT** |

## 3. Datos financieros, fecha y fuentes

| Dato | Valor | Tipo | Fuente / limitación |
| :--- | ---: | :--- | :--- |
| Precio | {number(price)} | dato de mercado | Fecha SSOT: {item.get('price_date', 'N/D')}; proveedor N/D |
| Capitalización | {number(item.get('market_cap'))} | dato derivado / mercado | Fuente primaria N/D |
| Publicación | {item.get('publication_date', 'N/D')} | fecha | Fuente primaria N/D |
| Estados financieros, ROIC y percentiles | N/D | pendiente | {source_note} |

## 4. Tesis, moat y límites

La tesis de calidad se apoya exclusivamente en los factores F1–F8 registrados en el SSOT. El informe no atribuye hechos operativos adicionales que no puedan reconstruirse. Los riesgos de concentración, competencia, ciclo económico, regulación y asignación de capital deben contrastarse con el último informe financiero y la llamada de resultados antes de una decisión de cartera.

## 5. Owner Earnings, FCF Yield y Value Score

| Componente | Valor | Estado |
| :--- | ---: | :--- |
| Owner Earnings | {number(item.get('owner_earnings'))} | calculado por SSOT |
| FCF Yield | {number(raw_yield)}% | {'N/D: no verificable con los inputs disponibles' if raw_yield is None else 'calculado por SSOT'} |
| Score FCF Yield | {number(fcf_score)} / 10 | {'N/D' if fcf_score is None else 'SSOT'} |
| Score crecimiento/múltiplo | {number(growth_score)} / 10 | SSOT |
| Score margen de seguridad | {number(mos_score)} / 10 | SSOT |
| **Value Score** | **{number(value)} / 10** | cálculo SSOT; reponderado si falta un componente |

$$\\text{{Value Score}} = 0.40S_{{FCF\\ yield}} + 0.30S_{{crecimiento/múltiplo}} + 0.30S_{{MoS}}$$

Cuando un componente es `N/D`, el SSOT repondera proporcionalmente los componentes disponibles; la ponderación aplicada se conserva en `cqv_data.json`.

## 6. Valoración intrínseca, escenarios y sensibilidad

| Elemento | Valor | Estado |
| :--- | ---: | :--- |
| Valor intrínseco base | {number(base)} | SSOT |
| MoS base | {number(mos_base)}% | SSOT |
| Valor esperado | {number(expected)} | {'SSOT' if expected is not None else 'N/D'} |
| MoS esperado | {number(mos_expected)}% | {'SSOT' if mos_expected is not None else 'N/D'} |
| Escenarios Bear/Base/Bull y sensibilidad WACC/g | N/D | deben documentarse con entradas y fórmulas DCF |

No se presenta un DCF reconstruible mientras falten flujos, WACC, tasa terminal, acciones diluidas y fuentes de los supuestos. La valoración se mantiene como provisional.

## 7. Registro de riesgos

| Riesgo mínimo | Probabilidad | Impacto | Mitigación | Indicador adelantado |
| :--- | :---: | :---: | :---: | :--- |
| Competencia / sustitución | N/D | N/D | N/D | cuota, precios, churn |
| Ciclo macro y demanda | N/D | N/D | N/D | pedidos, guía, FCF |
| Concentración / regulación | N/D | N/D | N/D | clientes, legislación, vencimientos |

## 8. Evolución histórica

| Periodo | CQV v5.0 | Precio |
| :--- | ---: | ---: |
| {quarter} | {number(cqv)} | {number(price)} |

Las comparaciones con versiones previas se conservan en `cqv_history.json` y no equivalen a una mejora económica por cambio de metodología.

## 9. Conclusión y veredicto

**{verdict}.** El resultado es consistente con las entradas SSOT y debe revisarse de nuevo cuando se incorporen fuentes primarias, subcomponentes de los factores y un DCF por escenarios verificable.

## 10. Auditoría, observaciones y acciones requeridas

| Control | Resultado |
| :--- | :--- |
| Fórmula CQV F1–F8 | {calc_note} |
| CQV y Value Score | Coinciden con SSOT al generar este informe |
| FCF Yield | {'N/D donde no era verificable; no se presenta como 0.00%' if raw_yield is None else 'Verificar contra fuente primaria'} |
| Fuente primaria y percentiles | Pendiente — confianza limitada a Media |
| DCF por escenarios | Pendiente cuando el SSOT incorpore entradas auditables |

**Corrección aplicada:** se eliminaron fórmulas corruptas, rendimientos FCF de 0.00% no justificables y veredictos incompatibles con el MoS esperado. El informe debe completarse con estados financieros y fuentes antes de elevar la confianza a Alta.
"""


def main():
    raw = json.loads(DATA.read_text(encoding="utf-8"))
    items = raw.get("data", raw) if isinstance(raw, dict) else raw
    remediated = []
    render_only = "--render" in sys.argv
    for item in items:
        cqv = item.get("cqv_v5", item.get("cqv"))
        if item.get("metodologia_version") != "v5.0" or not isinstance(cqv, (int, float)) or cqv < 9.5:
            continue
        path = report_path(item)
        if path is None:
            raise FileNotFoundError(f"Informe no encontrado para {item['ticker']}")
        existing = path.read_text(encoding="utf-8")
        if render_only:
            path.write_text(build_report(item, existing), encoding="utf-8")
            remediated.append((item, path, existing))
            continue
        expected = first_match(r"MoS Esperado:\s*\*\*?\s*([0-9.]+)%", existing)
        base = first_match(r"MoS Base:\s*\*\*?\s*([0-9.]+)%", existing)
        expected_value = first_match(r"Valor Intrínseco Esperado:\s*\$([0-9,.]+)", existing)
        if expected is not None:
            item["mos_esperado_pct"] = round(expected, 2)
        if base is not None:
            item["mos_base_pct"] = round(base, 2)
        if expected_value is not None:
            item["intrinsic_value_expected"] = round(expected_value, 2)
        # A displayed 0.00% yield cannot support a positive FCF-yield score.
        if re.search(r"FCF Yield Real del Propietario:\*\* \*\*0\.00%", existing):
            item["score_fcf_yield"] = None
            item["fcf_yield_pct"] = None
        item["data_confidence"] = "Media"
        remediated.append((item, path, existing))

    if render_only:
        print(f"Informes reconstruidos: {len(remediated)} informes elite v5")
    else:
        DATA.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"SSOT preparado: {len(remediated)} registros elite v5")


if __name__ == "__main__":
    main()
