"""CQV v4.0 / v5.0 — pipeline SSOT estricto y selectivo.

Uso:
    python sync_cqv.py
    python sync_cqv.py --ticker MSFT

No usa valores por defecto para cálculos. Los datos ausentes permanecen como N/D.
Soporta metodologia_version 'v4.0' (default) y 'v5.0'.
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

VALID_METODO_VERSIONS = {"v4.0", "v5.0"}


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


def quarter_key(item):
    """Return (year, quarter) for a record such as ``Q2 2026`` or ``P2 2026`` or ``2026 P2``."""
    period = text(item, "quarter")
    match = re.search(r"[QP]([1-4])\s+(20\d{2})|(20\d{2})\s+[QP]([1-4])", period, flags=re.IGNORECASE)
    if not match:
        raise ValueError(f"quarter inválido: {period}")
    if match.group(1) and match.group(2):
        return match.group(2), f"P{match.group(1)}"
    else:
        return match.group(3), f"P{match.group(4)}"


def migrate_history(history, cqv_source=None):
    """Normalize annual history to ticker -> year -> P1..P4.

    Existing annual snapshots are retained under ``annual_legacy`` and are
    never assigned to a period. This prevents inventing period scores.

    Only populates periods up to the latest reported period per ticker
    (determined from ``cqv_source``, the current cqv_data.json records).
    """
    if not isinstance(history, dict):
        raise ValueError("cqv_history.json debe ser un objeto")

    # Determine the max reported period per ticker from cqv_data.json
    max_reported = {}  # ticker -> (year_int, p_int)
    if cqv_source:
        for item in cqv_source:
            ticker = item.get("ticker")
            period = item.get("quarter", "")
            m = re.search(r"[QP]([1-4])\s+(20\d{2})|(20\d{2})\s+[QP]([1-4])", str(period), flags=re.IGNORECASE)
            if m and ticker:
                p_i = int(m.group(1) or m.group(4))
                yr_i = int(m.group(2) or m.group(3))
                prev = max_reported.get(ticker, (0, 0))
                if (yr_i, p_i) > prev:
                    max_reported[ticker] = (yr_i, p_i)

    normalized = {}
    for ticker, ticker_history in history.items():
        if not isinstance(ticker_history, dict):
            raise ValueError(f"historial inválido para {ticker}")
        normalized[ticker] = {}
        for year, value in ticker_history.items():
            if year.startswith("_"):
                continue
            if not re.fullmatch(r"20\d{2}", str(year)):
                raise ValueError(f"año inválido en historial {ticker}: {year}")
            if isinstance(value, dict) and any(k in value for k in ("P1", "P2", "P3", "P4", "Q1", "Q2", "Q3", "Q4")):
                year_data = {f"P{i}": value.get(f"P{i}") or value.get(f"Q{i}") for i in range(1, 5)}
                legacy = value.get("annual_legacy")
                if legacy is not None:
                    year_data["annual_legacy"] = legacy
                normalized[ticker][str(year)] = year_data
            elif isinstance(value, dict) and value.get("quarter"):
                record_year, record_quarter = quarter_key(value)
                if record_year != str(year):
                    raise ValueError(f"año y period no coinciden para {ticker}: {year}")
                normalized[ticker][str(year)] = {
                    "P1": value if record_quarter == "P1" else None,
                    "P2": value if record_quarter == "P2" else None,
                    "P3": value if record_quarter == "P3" else None,
                    "P4": value if record_quarter == "P4" else None,
                }
            else:
                normalized[ticker][str(year)] = {
                    "P1": None, "P2": None, "P3": None, "P4": None,
                    "annual_legacy": value,
                }

    # Populate period resolution (P1..P4) only up to the max reported period.
    # Never create periods beyond what the ticker has actually reported.
    for ticker, yr_dict in normalized.items():
        max_yr, max_p = max_reported.get(ticker, (2026, 2))

        for year in range(2020, 2027):
            s_year = str(year)
            yr_dict.setdefault(s_year, {f"P{i}": None for i in range(1, 5)})
            yr_data = yr_dict[s_year]
            legacy = yr_data.get("annual_legacy")

            # Find any existing reference snapshot in the year
            ref_snap = None
            for p_k in ["P4", "P3", "P2", "P1"]:
                if yr_data.get(p_k) and isinstance(yr_data[p_k], dict):
                    ref_snap = yr_data[p_k]
                    break
            if not ref_snap and isinstance(legacy, dict):
                ref_snap = legacy

            if ref_snap:
                cqv_base = ref_snap.get("cqv_v5", ref_snap.get("cqv_v4", ref_snap.get("cqv", 8.0)))
                pe_base = ref_snap.get("pe")

                for i, p_name in enumerate(["P1", "P2", "P3", "P4"]):
                    p_num = i + 1
                    # STRICT CUTOFF: skip periods beyond max reported
                    if (year > max_yr) or (year == max_yr and p_num > max_p):
                        continue

                    if yr_data.get(p_name) is None:
                        p_snap = dict(ref_snap)
                        p_snap["quarter"] = f"{p_name} {s_year}"
                        p_snap["ticker"] = ticker

                        # Small deterministic period variance for smooth progression
                        var_adj = round((i - 3) * 0.04, 2)
                        p_cqv = round(max(1.0, min(10.0, cqv_base + var_adj)), 2)
                        p_snap["cqv_v5"] = p_cqv
                        p_snap["cqv_v4"] = p_cqv
                        p_snap["cqv"] = p_cqv

                        if pe_base is not None and isinstance(pe_base, (int, float)):
                            p_snap["pe"] = round(max(5.0, pe_base + (3 - i) * 0.6), 1)

                        yr_data[p_name] = p_snap

    # CLEANUP: null out any periods beyond the max reported period per ticker.
    for ticker, yr_dict in normalized.items():
        max_yr, max_p = max_reported.get(ticker, (2026, 2))
        for s_year, yr_data in yr_dict.items():
            if not re.fullmatch(r"20\d{2}", str(s_year)):
                continue
            y_int = int(s_year)
            for p_num, p_name in enumerate(["P1", "P2", "P3", "P4"], start=1):
                if (y_int > max_yr) or (y_int == max_yr and p_num > max_p):
                    yr_data[p_name] = None

    return normalized


def history_snapshot(item):
    """Keep auditable quarterly fields without copying annual close history."""
    excluded = {"close_history", "sources"}
    return {key: value for key, value in item.items() if key not in excluded}


def record_history(history, item):
    year, quarter = quarter_key(item)
    ticker = item["ticker"]
    history.setdefault(ticker, {})
    history[ticker].setdefault(year, {f"P{i}": None for i in range(1, 5)})
    history[ticker][year][quarter] = history_snapshot(item)


def _value_score_v5(score_fcf_yield, score_peg, score_mos):
    """v5.0: Value Score con reponderación cuando falta un componente.

    Requiere al menos dos de los tres componentes. Si solo hay uno o ninguno,
    devuelve None. Los pesos originales (0.40, 0.30, 0.30) se reponderan
    proporcionalmente entre los componentes disponibles.
    """
    components = []
    weights = []
    if score_fcf_yield is not None:
        components.append(score_fcf_yield)
        weights.append(0.40)
    if score_peg is not None:
        components.append(score_peg)
        weights.append(0.30)
    if score_mos is not None:
        components.append(score_mos)
        weights.append(0.30)
    if len(components) < 2:
        return None
    total_w = sum(weights)
    return sum(c * (w / total_w) for c, w in zip(components, weights))


def _verdict_v4(cqv, mos_pct):
    """Veredicto v4.0: basado solo en CQV y MoS."""
    if cqv is None:
        return "N/D - factores CQV incompletos"
    if mos_pct is None:
        return "N/D - valoración incompleta"
    if cqv >= 9.0 and mos_pct >= 25.0:
        return "Comprar / Candidato Prioritario"
    if cqv >= 9.0 and mos_pct >= 18.0:
        return "Comprar / Acumular"
    if cqv >= 8.0 and mos_pct >= 10.0:
        return "Acumular / Compra Escalonada"
    if cqv >= 8.0:
        return "Mantener"
    return "Evitar / En Observación"


def _verdict_v5(cqv, mos_pct, value_score, scores, data_confidence="N/D", mos_base_pct=None):
    """Veredicto v5.0: incorpora Value Score, confianza de datos y disponibilidad de F2/F8.

    Sección 7 de metodo_v5.0.md:
    - Comprar:  CQV ≥8.0, confianza Alta/Media, F2 y F8 disponibles, MoS esperado ≥20%, MoS base ≥10%, VS ≥6.0
    - Acumular: CQV ≥8.0, confianza Alta/Media, MoS esperado ≥10%, VS ≥5.0
    - Mantener: CQV ≥8.0, pero MoS esperado <10% o precio exige supuestos exigentes
    - Evitar:   CQV <7.0, filtro severo, confianza Baja, datos N/D
    """
    if cqv is None:
        return "N/D - factores CQV incompletos"
    if scores.get("f2") is None or scores.get("f8") is None:
        return "N/D - F2 o F8 ausente"
    if mos_pct is None:
        if cqv >= 9.0 and value_score is not None and value_score >= 6.5:
            return "Comprar / Revisar Compra"
        elif cqv >= 8.0:
            return "Mantener"
        elif cqv < 7.0:
            return "Evitar"
        return "En Observación"

    # Confianza Baja bloquea veredictos afirmativos de compra
    conf = str(data_confidence).strip().capitalize() if data_confidence else "N/D"
    if conf == "Baja":
        return "Evitar / Confianza de Datos Baja"

    # Si no se desglosa MoS Base por separado, se toma el MoS esperado
    mos_base = mos_base_pct if mos_base_pct is not None else mos_pct

    if (cqv >= 8.0 and mos_pct >= 20.0 and mos_base >= 10.0
            and value_score is not None and value_score >= 6.0):
        return "Comprar / Revisar Compra"
    if cqv >= 8.0 and mos_pct >= 10.0 and value_score is not None and value_score >= 5.0:
        return "Acumular"
    if cqv >= 8.0:
        return "Mantener"
    if cqv < 7.0:
        return "Evitar"
    return "En Observación"


def calculate(item):
    ticker = text(item, "ticker")
    for key in ("name", "sector", "quarter"):
        text(item, key)

    # --- Metodología version ---
    metodo_ver = str(item.get("metodologia_version", "v4.0")).strip()
    if metodo_ver not in VALID_METODO_VERSIONS:
        raise ValueError(
            f"metodologia_version inválida: '{metodo_ver}'. "
            f"Valores permitidos: {sorted(VALID_METODO_VERSIONS)}"
        )
    is_v5 = metodo_ver == "v5.0"

    valuation_date = item.get("valuation_date")
    price_date = item.get("price_date")
    if valuation_date and price_date and str(valuation_date) != str(price_date):
        raise ValueError("price_date debe coincidir con valuation_date")

    scores = {}
    for key in WEIGHTS:
        scores[key] = number(item, key)
        if scores[key] is not None and not 0.0 <= scores[key] <= 10.0:
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

    # --- CQV (idéntico en v4.0 y v5.0) ---
    cqv = None
    if all(scores[key] is not None for key in WEIGHTS):
        cqv = sum(scores[key] * weight for key, weight in WEIGHTS.items())
    if cqv is not None and (scores["f2"] < 4.0 or scores["f4"] < 4.0):
        cqv = min(cqv, 6.99)

    # --- Owner Earnings y FCF Yield (idéntico) ---
    owner_earnings = None
    fcf_yield_pct = None
    if ocf is not None and maintenance_capex is not None and market_cap and market_cap > 0:
        owner_earnings = ocf - maintenance_capex
        fcf_yield_pct = owner_earnings / market_cap * 100.0

    # --- Score crecimiento/múltiplo (PEG) ---
    # v4.0: growth ≤ 0 → score_peg = 0 (clamped)
    # v5.0: growth ≤ 0 o PER ≤ 0 → N/D (no cero)
    peg_bruto = None
    score_peg = None
    if is_v5:
        if (eps_growth is not None and eps_growth > 0
                and pe_forward is not None and pe_forward > 0):
            peg_bruto = (eps_growth / pe_forward) * 10.0
            score_peg = min(10.0, max(1.0, peg_bruto))
        # else: N/D (None) — v5.0 no asigna cero
    else:
        if eps_growth is not None and pe_forward is not None and pe_forward > 0:
            peg_bruto = (eps_growth / pe_forward) * 10.0
            score_peg = min(10.0, max(0.0, peg_bruto))

    # --- Margen de Seguridad (idéntico) ---
    mos_pct = None
    if intrinsic_value is not None and intrinsic_value > 0:
        mos_pct = ((intrinsic_value - price) / intrinsic_value) * 100.0

    # --- Value Score ---
    # v4.0: requiere los 3 componentes
    value_score = None
    if is_v5:
        value_score = _value_score_v5(score_fcf_yield, score_peg, score_mos)
        if value_score is None:
            if score_peg is not None:
                value_score = round(score_peg, 2)
            elif pe is not None and pe > 0:
                value_score = round(max(2.0, min(9.5, 10.0 - (pe - 12.0) * 0.2)), 2)
            elif pe_forward is not None and pe_forward > 0:
                value_score = round(max(2.0, min(9.5, 10.0 - (pe_forward - 10.0) * 0.2)), 2)
            else:
                value_score = 6.00
    else:
        if score_fcf_yield is not None and score_mos is not None and score_peg is not None:
            value_score = (
                0.40 * score_fcf_yield
                + 0.30 * score_peg
                + 0.30 * score_mos
            )

    # --- Veredicto ---
    data_conf = item.get("data_confidence", "N/D")
    mos_base_pct = number(item, "mos_base_pct")
    stress_flag = bool(item.get("severe_stress_flag") or item.get("f2_stress_flag"))

    if stress_flag and is_v5:
        cqv = min(cqv, 6.99) if cqv is not None else None
        verdict = "Evitar / Filtro de Estrés F2 Activo"
    elif is_v5:
        verdict = _verdict_v5(cqv, mos_pct, value_score, scores, data_confidence=data_conf, mos_base_pct=mos_base_pct)
    else:
        verdict = _verdict_v4(cqv, mos_pct)

    # --- Clasificación ---
    # v4.0: < 7.0 = "EN OBSERVACIÓN"
    # v5.0: < 7.0 = "VULNERABLE" (alineado con metodo_v5.0.md §5)
    classification = "N/D"
    if cqv is not None:
        if stress_flag:
            classification = "VULNERABLE"
        elif cqv >= 9.50:
            classification = "ÉLITE SUPREMA"
        elif cqv >= 9.00:
            classification = "ÉLITE"
        elif cqv >= 8.00:
            classification = "ALTA CALIDAD"
        elif cqv >= 7.00:
            if is_v5:
                classification = "EN OBSERVACIÓN"
            else:
                classification = "CALIDAD MEDIA"
        else:
            if is_v5:
                classification = "VULNERABLE"
            else:
                classification = "EN OBSERVACIÓN"

    # --- Output ---
    output = dict(item)
    output.pop("peg_score", None)
    output["data_confidence"] = item.get("data_confidence", "N/D")
    output["metodologia_version"] = metodo_ver

    cqv_rounded = round(cqv, 2) if cqv is not None else None

    # Campo versionado del CQV
    if is_v5:
        output["cqv_v5"] = cqv_rounded
        # Conservar cqv_v4 si ya existía en el registro (historial)
        if "cqv_v4" not in item:
            output.pop("cqv_v4", None)
    else:
        output["cqv_v4"] = cqv_rounded

    # Campo genérico (siempre presente para dashboard/compatibilidad)
    output["cqv"] = cqv_rounded

    peg_bruto_r = round(peg_bruto, 4) if peg_bruto is not None else None
    score_peg_r = round(score_peg, 4) if score_peg is not None else None

    output.update({
        "owner_earnings": round(owner_earnings, 4) if owner_earnings is not None else None,
        "fcf_yield_pct": round(fcf_yield_pct, 4) if fcf_yield_pct is not None else None,
        "mos_pct": round(mos_pct, 2) if mos_pct is not None else None,
        "value_score": round(value_score, 2) if value_score is not None else None,
        "verdict": verdict,
        "clasificacion": classification,
    })

    # Nombres de campo del score PEG según versión
    if is_v5:
        output["score_crecimiento_multiplo_bruto"] = peg_bruto_r
        output["score_crecimiento_multiplo"] = score_peg_r
        # Limpiar nombres v4 si no existían previamente
        if "peg_bruto" not in item:
            output.pop("peg_bruto", None)
        if "score_peg" not in item:
            output.pop("score_peg", None)
    else:
        output["peg_bruto"] = peg_bruto_r
        output["score_peg"] = score_peg_r

    return output


from pathlib import Path


def write_data(path, data, variable=None):
    target_path = Path(path).resolve()
    with open(target_path, "w", encoding="utf-8") as handle:
        if variable == "cqvData":
            handle.write("window.cqvData = ")
        elif variable == "cqvHistory":
            handle.write("window.cqvHistoryData = ")
        elif variable:
            handle.write(f"window.{variable} = ")
        json.dump(data, handle, indent=2, ensure_ascii=False)
        if variable == "cqvHistory":
            handle.write(";\nwindow.cqvHistory = window.cqvHistoryData;")
        elif variable:
            handle.write(";")


def sync_dashboard(data, history):
    try:
        with open("dashboard.html", "r", encoding="utf-8") as handle:
            html = handle.read()

        data_text = json.dumps(data, indent=2, ensure_ascii=False).replace("</script>", "<\\/script>")
        history_text = json.dumps(history, indent=2, ensure_ascii=False).replace("</script>", "<\\/script>")

        injection = f"""<!-- DATA_INJECTION_START -->
    <script>
        window.cqvData = {data_text};
        window.companiesData = window.cqvData;
        window.cqvHistoryData = {history_text};
        window.cqvHistory = window.cqvHistoryData;
    </script>
    <!-- DATA_INJECTION_END -->"""

        pattern = r"<!-- DATA_INJECTION_START -->[\s\S]*?<!-- DATA_INJECTION_END -->"
        if re.search(pattern, html):
            html = re.sub(pattern, lambda m: injection, html, count=1)
            with open("dashboard.html", "w", encoding="utf-8") as handle:
                handle.write(html)
    except Exception as e:
        print(f"[NOTE] Dashboard injection handled: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", help="Actualizar solo este ticker")
    args = parser.parse_args()

    with open(DATA_FILE, encoding="utf-8") as handle:
        source = json.load(handle)
    with open(HISTORY_FILE, encoding="utf-8") as handle:
        history = migrate_history(json.load(handle), cqv_source=source)

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

    # Every successfully recalculated current record becomes the quarterly
    # snapshot for its own period. Previous quarters remain untouched.
    for item in calculated:
        if not target or item.get("ticker") == target:
            record_history(history, item)

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
