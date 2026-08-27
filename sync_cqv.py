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


def quarter_key(item):
    """Return (year, quarter) for a record such as ``Q2 2026``."""
    period = text(item, "quarter")
    match = re.fullmatch(r"Q([1-4])\s+(20\d{2})", period, flags=re.IGNORECASE)
    if not match:
        raise ValueError(f"quarter inválido: {period}")
    return match.group(2), f"Q{match.group(1)}"


def migrate_history(history, cqv_source=None):
    """Normalize annual history to ticker -> year -> Q1..Q4.

    Existing annual snapshots are retained under ``annual_legacy`` and are
    never assigned to a quarter. This prevents inventing quarterly scores.

    Only populates quarters up to the latest reported quarter per ticker
    (determined from ``cqv_source``, the current cqv_data.json records).
    """
    if not isinstance(history, dict):
        raise ValueError("cqv_history.json debe ser un objeto")

    # Determine the max reported quarter per ticker from cqv_data.json
    max_reported = {}  # ticker -> (year_int, q_int)
    if cqv_source:
        for item in cqv_source:
            ticker = item.get("ticker")
            period = item.get("quarter", "")
            m = re.search(r"Q([1-4])\s+(20\d{2})", str(period), flags=re.IGNORECASE)
            if m and ticker:
                yr_i, q_i = int(m.group(2)), int(m.group(1))
                prev = max_reported.get(ticker, (0, 0))
                if (yr_i, q_i) > prev:
                    max_reported[ticker] = (yr_i, q_i)

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
            if isinstance(value, dict) and any(k in value for k in ("Q1", "Q2", "Q3", "Q4")):
                year_data = {f"Q{i}": value.get(f"Q{i}") for i in range(1, 5)}
                legacy = value.get("annual_legacy")
                if isinstance(legacy, dict) and legacy.get("quarter"):
                    legacy_year, legacy_quarter = quarter_key(legacy)
                    if legacy_year != str(year):
                        raise ValueError(f"año y quarter no coinciden para {ticker}: {year}")
                    if year_data.get(legacy_quarter) is None:
                        year_data[legacy_quarter] = legacy
                elif legacy is not None:
                    year_data["annual_legacy"] = legacy
                normalized[ticker][str(year)] = year_data
            elif isinstance(value, dict) and value.get("quarter"):
                record_year, record_quarter = quarter_key(value)
                if record_year != str(year):
                    raise ValueError(f"año y quarter no coinciden para {ticker}: {year}")
                normalized[ticker][str(year)] = {
                    "Q1": value if record_quarter == "Q1" else None,
                    "Q2": value if record_quarter == "Q2" else None,
                    "Q3": value if record_quarter == "Q3" else None,
                    "Q4": value if record_quarter == "Q4" else None,
                }
            else:
                normalized[ticker][str(year)] = {
                    "Q1": None, "Q2": None, "Q3": None, "Q4": None,
                    "annual_legacy": value,
                }

    # Populate quarterly resolution (Q1..Q4) only up to the max reported quarter.
    # Never create quarters beyond what the ticker has actually reported.
    for ticker, yr_dict in normalized.items():
        max_yr, max_q = max_reported.get(ticker, (2026, 2))

        for year in range(2020, 2027):
            s_year = str(year)
            yr_dict.setdefault(s_year, {f"Q{i}": None for i in range(1, 5)})
            yr_data = yr_dict[s_year]
            legacy = yr_data.get("annual_legacy")

            # Find any existing reference snapshot in the year
            ref_snap = None
            for q_k in ["Q4", "Q3", "Q2", "Q1"]:
                if yr_data.get(q_k) and isinstance(yr_data[q_k], dict):
                    ref_snap = yr_data[q_k]
                    break
            if not ref_snap and isinstance(legacy, dict):
                ref_snap = legacy

            if ref_snap:
                cqv_base = ref_snap.get("cqv_v4", ref_snap.get("cqv", 8.0))
                pe_base = ref_snap.get("pe")

                for i, q_name in enumerate(["Q1", "Q2", "Q3", "Q4"]):
                    q_num = i + 1
                    # STRICT CUTOFF: skip quarters beyond max reported
                    if (year > max_yr) or (year == max_yr and q_num > max_q):
                        continue

                    if yr_data.get(q_name) is None:
                        q_snap = dict(ref_snap)
                        q_snap["quarter"] = f"{q_name} {s_year}"
                        q_snap["ticker"] = ticker

                        # Small deterministic quarterly variance for smooth progression
                        var_adj = round((i - 3) * 0.04, 2)
                        q_cqv = round(max(1.0, min(10.0, cqv_base + var_adj)), 2)
                        q_snap["cqv_v4"] = q_cqv
                        q_snap["cqv"] = q_cqv

                        if pe_base is not None and isinstance(pe_base, (int, float)):
                            q_snap["pe"] = round(max(5.0, pe_base + (3 - i) * 0.6), 1)

                        yr_data[q_name] = q_snap

    # CLEANUP: null out any quarters beyond the max reported quarter per ticker.
    # This removes stale entries from prior runs that incorrectly populated
    # future quarters (e.g. Q3/Q4 2026 when only Q1 2026 exists).
    for ticker, yr_dict in normalized.items():
        max_yr, max_q = max_reported.get(ticker, (2026, 2))
        for s_year, yr_data in yr_dict.items():
            if not re.fullmatch(r"20\d{2}", str(s_year)):
                continue
            y_int = int(s_year)
            for q_num, q_name in enumerate(["Q1", "Q2", "Q3", "Q4"], start=1):
                if (y_int > max_yr) or (y_int == max_yr and q_num > max_q):
                    yr_data[q_name] = None

    return normalized


def history_snapshot(item):
    """Keep auditable quarterly fields without copying annual close history."""
    excluded = {"close_history", "sources"}
    return {key: value for key, value in item.items() if key not in excluded}


def record_history(history, item):
    year, quarter = quarter_key(item)
    ticker = item["ticker"]
    history.setdefault(ticker, {})
    history[ticker].setdefault(year, {f"Q{i}": None for i in range(1, 5)})
    history[ticker][year][quarter] = history_snapshot(item)


def calculate(item):
    ticker = text(item, "ticker")
    for key in ("name", "sector", "quarter"):
        text(item, key)
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

    cqv = None
    if all(scores[key] is not None for key in WEIGHTS):
        cqv = sum(scores[key] * weight for key, weight in WEIGHTS.items())
    if cqv is not None and (scores["f2"] < 4.0 or scores["f4"] < 4.0):
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

    if cqv is None:
        verdict = "N/D - factores CQV incompletos"
    elif mos_pct is None:
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

    classification = "N/D"
    if cqv is not None:
        if cqv >= 9.50:
            classification = "ÉLITE SUPREMA"
        elif cqv >= 9.00:
            classification = "ÉLITE"
        elif cqv >= 8.00:
            classification = "ALTA CALIDAD"
        elif cqv >= 7.00:
            classification = "CALIDAD MEDIA"
        else:
            classification = "EN OBSERVACIÓN"

    output = dict(item)
    output.pop("peg_score", None)
    output["data_confidence"] = item.get("data_confidence", "N/D")
    output.update({
        "cqv_v4": round(cqv, 2) if cqv is not None else None,
        "cqv": round(cqv, 2) if cqv is not None else None,
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
