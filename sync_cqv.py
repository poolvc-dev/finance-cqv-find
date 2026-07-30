"""CQV v4.0 — pipeline SSOT estricto.

Valida todos los registros antes de escribir. No usa valores por defecto,
no redacta informes y no sustituye FCF Yield por PER.
"""

import json
import math
import os
import re
import sys

DATA_FILE = "cqv_data.json"
HISTORY_FILE = "cqv_history.json"
REPORT_DIR = "inform"

REQUIRED = (
    "ticker", "name", "sector", "quarter", "data_confidence",
    "price", "pe", "pe_forward", "eps_growth_ntm_pct",
    "ocf", "maintenance_capex", "market_cap",
    "intrinsic_value", "score_fcf_yield", "score_mos",
    "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
)

WEIGHTS = {
    "f1": 0.20, "f2": 0.15, "f3": 0.15, "f4": 0.15,
    "f5": 0.10, "f6": 0.10, "f7": 0.05, "f8": 0.10,
}


def finite_number(item, key):
    if key not in item or item[key] is None or item[key] == "":
        raise ValueError(f"campo ausente: {key}")
    try:
        value = float(item[key])
    except (TypeError, ValueError):
        raise ValueError(f"campo no numérico: {key}")
    if not math.isfinite(value):
        raise ValueError(f"campo no finito: {key}")
    return value


def require_text(item, key):
    value = item.get(key)
    if value is None or str(value).strip() == "":
        raise ValueError(f"campo ausente: {key}")
    return str(value).strip()


def calculate(item):
    ticker = require_text(item, "ticker")
    for key in ("name", "sector", "quarter", "data_confidence"):
        require_text(item, key)

    values = {key: finite_number(item, key) for key in REQUIRED if key not in
              ("ticker", "name", "sector", "quarter", "data_confidence")}

    for key in ("f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
                "score_fcf_yield", "score_mos"):
        if not 0.0 <= values[key] <= 10.0:
            raise ValueError(f"{key} fuera de rango 0-10")

    if values["price"] <= 0:
        raise ValueError("price debe ser > 0")
    if values["pe_forward"] <= 0:
        raise ValueError("pe_forward debe ser > 0")
    if values["market_cap"] <= 0:
        raise ValueError("market_cap debe ser > 0")
    if values["intrinsic_value"] <= 0:
        raise ValueError("intrinsic_value debe ser > 0")

    cqv = sum(values[key] * weight for key, weight in WEIGHTS.items())
    if values["f2"] < 4.0 or values["f4"] < 4.0:
        cqv = min(cqv, 6.99)

    owner_earnings = values["ocf"] - values["maintenance_capex"]
    fcf_yield_pct = owner_earnings / values["market_cap"] * 100.0

    peg_bruto = (values["eps_growth_ntm_pct"] / values["pe_forward"]) * 10.0
    score_peg = min(10.0, max(0.0, peg_bruto))
    mos_pct = ((values["intrinsic_value"] - values["price"]) /
               values["intrinsic_value"]) * 100.0

    value_score = (
        0.40 * values["score_fcf_yield"]
        + 0.30 * score_peg
        + 0.30 * values["score_mos"]
    )

    if cqv >= 9.0 and mos_pct >= 25.0:
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
    output.pop("peg_score", None)  # campo histórico/deprecado
    output.update({
        "cqv_v4": round(cqv, 2),
        "cqv": round(cqv, 2),
        "owner_earnings": round(owner_earnings, 4),
        "fcf_yield_pct": round(fcf_yield_pct, 4),
        "peg_bruto": round(peg_bruto, 4),
        "score_peg": round(score_peg, 4),
        "mos_pct": round(mos_pct, 2),
        "value_score": round(value_score, 2),
        "verdict": verdict,
        "clasificacion": classification,
    })
    return output


def write_json_js(path, variable, data):
    with open(path, "w", encoding="utf-8") as handle:
        if path.endswith(".js"):
            handle.write(f"const {variable} = ")
            json.dump(data, handle, indent=2, ensure_ascii=False)
            handle.write(";")
        else:
            json.dump(data, handle, indent=2, ensure_ascii=False)


def main():
    with open(DATA_FILE, encoding="utf-8") as handle:
        source = json.load(handle)
    with open(HISTORY_FILE, encoding="utf-8") as handle:
        history = json.load(handle)

    if not isinstance(source, list) or not source:
        raise ValueError("cqv_data.json debe ser una lista no vacía")

    errors = []
    calculated = []
    for index, item in enumerate(source):
        try:
            calculated.append(calculate(item))
        except ValueError as exc:
            ticker = item.get("ticker", f"registro {index}")
            errors.append(f"{ticker}: {exc}")

    if errors:
        print("VALIDACIÓN FALLIDA. No se ha escrito ningún archivo.")
        for error in errors:
            print(f"- {error}")
        return 2

    calculated.sort(key=lambda item: item["cqv_v4"], reverse=True)

    # Solo se escribe después de validar todos los registros.
    write_json_js(DATA_FILE, "", calculated)
    write_json_js("cqv_data.js", "cqvData", calculated)
    write_json_js(HISTORY_FILE, "", history)
    write_json_js("cqv_history.js", "cqvHistory", history)

    with open("dashboard.html", encoding="utf-8") as handle:
        html = handle.read()
    data_text = json.dumps(calculated, indent=2, ensure_ascii=False)
    history_text = json.dumps(history, indent=2, ensure_ascii=False)
    # El dashboard mantiene inyecciones embebidas además de los archivos JS.
    # Se actualizan todas las copias que realmente consume dashboard.html.
    html = re.sub(r"window\.companiesData\s*=\s*\[[\s\S]*?\];",
                  lambda _: f"window.companiesData = {data_text};", html)
    html = re.sub(r"let companies\s*=\s*\[[\s\S]*?\];",
                  lambda _: f"let companies = {data_text};", html)
    html = re.sub(r"window\.cqvHistoryData\s*=\s*\{[\s\S]*?\};",
                  lambda _: f"window.cqvHistoryData = {history_text};", html)
    with open("dashboard.html", "w", encoding="utf-8") as handle:
        handle.write(html)

    print(f"[OK] {len(calculated)} registros validados y sincronizados.")
    print("[OK] Informes Markdown no se modifican: deben generarse y validarse aparte.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
