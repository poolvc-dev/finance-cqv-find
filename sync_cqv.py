"""CQV v4.0 — pipeline SSOT estricto y selectivo.

Uso:
    python sync_cqv.py
    python sync_cqv.py --ticker MSFT

No usa valores por defecto para cálculos. Los datos ausentes permanecen como N/D.
"""

import argparse
import json
import math
import re
import sys

DATA_FILE = "cqv_data.json"
HISTORY_FILE = "cqv_history.json"

WEIGHTS = {
    "f1": 0.20, "f2": 0.15, "f3": 0.15, "f4": 0.15,
    "f5": 0.10, "f6": 0.10, "f7": 0.05, "f8": 0.10,
}


def number(item, key, required=False):
    raw = item.get(key)
    if raw is None or raw == "":
        if required:
            raise ValueError(f"campo ausente: {key}")
        return None
    try:
        value = float(raw)
    except (TypeError, ValueError):
        raise ValueError(f"campo no numérico: {key}")
    if not math.isfinite(value):
        raise ValueError(f"campo no finito: {key}")
    return value


def text(item, key, required=True):
    value = item.get(key)
    if value is None or str(value).strip() == "":
        if required:
            raise ValueError(f"campo ausente: {key}")
        return None
    return str(value).strip()


def calculate(item):
    ticker = text(item, "ticker")
    for key in ("name", "sector", "quarter"):
        text(item, key)

    scores = {}
    for key in WEIGHTS:
        scores[key] = number(item, key, required=True)
        if not 0.0 <= scores[key] <= 10.0:
            raise ValueError(f"{key} fuera de rango 0-10")

    price = number(item, "price", required=True)
    pe = number(item, "pe")
    pe_forward = number(item, "pe_forward")
    eps_growth = number(item, "eps_growth_ntm_pct")
    ocf = number(item, "ocf")
    maintenance_capex = number(item, "maintenance_capex")
    market_cap = number(item, "market_cap")
    intrinsic_value = number(item, "intrinsic_value")
    score_fcf_yield = number(item, "score_fcf_yield")
    score_mos = number(item, "score_mos")

    if price <= 0:
        raise ValueError("price debe ser > 0")
    for key, value in (("score_fcf_yield", score_fcf_yield), ("score_mos", score_mos)):
        if value is not None and not 0.0 <= value <= 10.0:
            raise ValueError(f"{key} fuera de rango 0-10")

    cqv = sum(scores[key] * weight for key, weight in WEIGHTS.items())
    if scores["f2"] < 4.0 or scores["f4"] < 4.0:
        cqv = min(cqv, 6.99)

    owner_earnings = None
    fcf_yield_pct = None
    if ocf is not None and maintenance_capex is not None and market_cap and market_cap > 0:
        owner_earnings = ocf - maintenance_capex
        fcf_yield_pct = owner_earnings / market_cap * 100.0

    peg_bruto = None
    score_peg = None
    if eps_growth is not None and pe_forward is not None and pe_forward > 0:
        peg_bruto = (eps_growth / pe_forward) * 10.0
        score_peg = min(10.0, max(0.0, peg_bruto))

    mos_pct = None
    if intrinsic_value is not None and intrinsic_value > 0:
        mos_pct = ((intrinsic_value - price) / intrinsic_value) * 100.0

    value_score = None
    if score_fcf_yield is not None and score_mos is not None and score_peg is not None:
        value_score = (
            0.40 * score_fcf_yield
            + 0.30 * score_peg
            + 0.30 * score_mos
        )

    if mos_pct is None:
        verdict = "N/D - valoración incompleta"
    elif cqv >= 9.0 and mos_pct >= 25.0:
        verdict = "Comprar / Candidato Prioritario"
    elif cqv >= 9.0 and mos_pct >= 18.0:
        verdict = "Comprar / Acumular"
    elif cqv >= 8.0 and mos_pct >= 10.0:
        verdict = "Acumular / Compra Escalonada"
    elif cqv >= 8.0:
        verdict = "Mantener"
    else:
        verdict = "Evitar / En Observación"

    classification = (
        "ÉLITE" if cqv >= 9.0 else
        "ALTA CALIDAD" if cqv >= 8.0 else
        "VULNERABLE" if cqv < 7.0 else
        "EN OBSERVACIÓN"
    )

    output = dict(item)
    output.pop("peg_score", None)
    output["data_confidence"] = item.get("data_confidence", "N/D")
    output.update({
        "cqv_v4": round(cqv, 2),
        "cqv": round(cqv, 2),
        "owner_earnings": round(owner_earnings, 4) if owner_earnings is not None else None,
        "fcf_yield_pct": round(fcf_yield_pct, 4) if fcf_yield_pct is not None else None,
        "peg_bruto": round(peg_bruto, 4) if peg_bruto is not None else None,
        "score_peg": round(score_peg, 4) if score_peg is not None else None,
        "mos_pct": round(mos_pct, 2) if mos_pct is not None else None,
        "value_score": round(value_score, 2) if value_score is not None else None,
        "verdict": verdict,
        "clasificacion": classification,
    })
    return output


def write_data(path, data, variable=None):
    with open(path, "w", encoding="utf-8") as handle:
        if variable:
            handle.write(f"const {variable} = ")
        json.dump(data, handle, indent=2, ensure_ascii=False)
        if variable:
            handle.write(";")


def sync_dashboard(data, history):
    with open("dashboard.html", encoding="utf-8") as handle:
        html = handle.read()

    data_text = json.dumps(data, indent=2, ensure_ascii=False)
    history_text = json.dumps(history, indent=2, ensure_ascii=False)

    patterns = [
        (r"window\.companiesData\s*=\s*\[[\s\S]*?\];",
         f"window.companiesData = {data_text};"),
        (r"let companies\s*=\s*\[[\s\S]*?\];",
         f"let companies = {data_text};"),
        (r"window\.cqvHistoryData\s*=\s*\{[\s\S]*?\};",
         f"window.cqvHistoryData = {history_text};"),
    ]
    for pattern, replacement in patterns:
        html, count = re.subn(pattern, replacement, html, count=1)
        if count != 1:
            raise ValueError(f"bloque no encontrado en dashboard.html: {pattern}")

    with open("dashboard.html", "w", encoding="utf-8") as handle:
        handle.write(html)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", help="Actualizar solo este ticker")
    args = parser.parse_args()

    with open(DATA_FILE, encoding="utf-8") as handle:
        source = json.load(handle)
    with open(HISTORY_FILE, encoding="utf-8") as handle:
        history = json.load(handle)

    if not isinstance(source, list) or not source:
        raise ValueError("cqv_data.json debe ser una lista no vacía")

    target = args.ticker.upper() if args.ticker else None
    selected = [item for item in source if not target or item.get("ticker") == target]
    if target and not selected:
        raise ValueError(f"ticker no encontrado: {target}")

    calculated = []
    errors = []
    for item in source:
        if target and item.get("ticker") != target:
            calculated.append(item)
            continue
        try:
            calculated.append(calculate(item))
        except ValueError as exc:
            errors.append(f"{item.get('ticker', 'registro')}: {exc}")

    if errors:
        print("VALIDACIÓN FALLIDA. No se ha escrito ningún archivo.")
        for error in errors:
            print(f"- {error}")
        return 2

    calculated.sort(key=lambda item: item.get("cqv_v4", 0) or 0, reverse=True)

    write_data(DATA_FILE, calculated)
    write_data("cqv_data.js", calculated, "cqvData")
    write_data(HISTORY_FILE, history)
    write_data("cqv_history.js", history, "cqvHistory")
    sync_dashboard(calculated, history)

    print(f"[OK] {len(selected)} registro(s) recalculado(s).")
    print("[OK] SSOT, JS y dashboard sincronizados.")
    print("[OK] Los informes Markdown se generan y validan por separado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
