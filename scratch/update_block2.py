import json

DATA_FILE = "cqv_data.json"
HISTORY_FILE = "cqv_history.json"

updates = {
    "MEDP": {
        "ticker": "MEDP",
        "name": "Medpace Holdings, Inc.",
        "sector": "Healthcare / Contract Research Organizations (CRO)",
        "quarter": "P3 2026",
        "f1": 9.60,
        "f2": 9.80,
        "f3": 9.10,
        "f4": 9.40,
        "f5": 9.40,
        "f6": 9.50,
        "f7": 8.80,
        "f8": 9.40,
        "price": 660.99,
        "pe": 38.5,
        "pe_forward": 36.4,
        "eps_growth_ntm_pct": 16.0,
        "growth_eps": 16.0,
        "eps_trailing": 17.15,
        "eps_forward": 18.15,
        "market_cap_b": 18.77,
        "market_cap": 18772.0,
        "ocf": 740.0,
        "maintenance_capex": 35.0,
        "owner_earnings": 705.0,
        "score_fcf_yield": 6.80,
        "intrinsic_value": 580.00,
        "intrinsic_value_expected": 605.00,
        "mos_base_pct": -13.96,
        "mos_esperado_pct": -8.47,
        "score_mos": 3.00,
        "wacc": 8.5,
        "g_terminal": 3.5,
        "valuation_date": "21/10/2026",
        "publication_date": "21/10/2026",
        "price_date": "21/10/2026",
        "metodologia_version": "v5.0",
        "data_confidence": "Alta"
    },
    "TMO": {
        "ticker": "TMO",
        "name": "Thermo Fisher Scientific Inc.",
        "sector": "Healthcare / Life Sciences & Diagnostics Tools",
        "quarter": "P3 2026",
        "f1": 8.80,
        "f2": 8.40,
        "f3": 8.60,
        "f4": 9.50,
        "f5": 8.90,
        "f6": 9.20,
        "f7": 9.10,
        "f8": 9.50,
        "price": 694.02,
        "pe": 31.0,
        "pe_forward": 26.5,
        "eps_growth_ntm_pct": 12.5,
        "growth_eps": 12.5,
        "eps_trailing": 22.40,
        "eps_forward": 26.20,
        "market_cap_b": 264.42,
        "market_cap": 264420.0,
        "ocf": 7800.0,
        "maintenance_capex": 1400.0,
        "owner_earnings": 6400.0,
        "score_fcf_yield": 5.10,
        "intrinsic_value": 650.00,
        "intrinsic_value_expected": 680.00,
        "mos_base_pct": -6.77,
        "mos_esperado_pct": -2.02,
        "score_mos": 4.50,
        "wacc": 8.0,
        "g_terminal": 3.5,
        "valuation_date": "21/10/2026",
        "publication_date": "21/10/2026",
        "price_date": "21/10/2026",
        "metodologia_version": "v5.0",
        "data_confidence": "Alta"
    },
    "ABT": {
        "ticker": "ABT",
        "name": "Abbott Laboratories",
        "sector": "Healthcare / Medical Devices & Diagnostics",
        "quarter": "P3 2026",
        "f1": 8.80,
        "f2": 8.90,
        "f3": 8.50,
        "f4": 9.40,
        "f5": 8.80,
        "f6": 9.20,
        "f7": 8.90,
        "f8": 9.50,
        "price": 102.45,
        "pe": 24.2,
        "pe_forward": 18.5,
        "eps_growth_ntm_pct": 10.5,
        "growth_eps": 10.5,
        "eps_trailing": 4.23,
        "eps_forward": 5.54,
        "market_cap_b": 177.75,
        "market_cap": 177750.0,
        "ocf": 8500.0,
        "maintenance_capex": 1800.0,
        "owner_earnings": 6700.0,
        "score_fcf_yield": 6.80,
        "intrinsic_value": 120.00,
        "intrinsic_value_expected": 125.00,
        "mos_base_pct": 14.63,
        "mos_esperado_pct": 18.04,
        "score_mos": 7.10,
        "wacc": 7.5,
        "g_terminal": 3.0,
        "valuation_date": "21/10/2026",
        "publication_date": "21/10/2026",
        "price_date": "21/10/2026",
        "metodologia_version": "v5.0",
        "data_confidence": "Alta"
    },
    "CME": {
        "ticker": "CME",
        "name": "CME Group Inc.",
        "sector": "Financials / Financial Exchanges & Data",
        "quarter": "P3 2026",
        "f1": 9.80,
        "f2": 9.60,
        "f3": 8.60,
        "f4": 9.90,
        "f5": 9.20,
        "f6": 9.40,
        "f7": 8.50,
        "f8": 9.70,
        "price": 295.79,
        "pe": 26.5,
        "pe_forward": 24.5,
        "eps_growth_ntm_pct": 11.0,
        "growth_eps": 11.0,
        "eps_trailing": 11.16,
        "eps_forward": 12.07,
        "market_cap_b": 106.48,
        "market_cap": 106484.0,
        "ocf": 4100.0,
        "maintenance_capex": 110.0,
        "owner_earnings": 3990.0,
        "score_fcf_yield": 6.80,
        "intrinsic_value": 315.00,
        "intrinsic_value_expected": 325.00,
        "mos_base_pct": 6.49,
        "mos_esperado_pct": 8.99,
        "score_mos": 5.80,
        "wacc": 7.5,
        "g_terminal": 3.0,
        "valuation_date": "21/10/2026",
        "publication_date": "21/10/2026",
        "price_date": "21/10/2026",
        "metodologia_version": "v5.0",
        "data_confidence": "Alta"
    },
    "PM": {
        "ticker": "PM",
        "name": "Philip Morris International Inc.",
        "sector": "Consumer Defensive / Tobacco & Smoke-Free Products",
        "quarter": "P3 2026",
        "f1": 9.20,
        "f2": 8.20,
        "f3": 8.80,
        "f4": 9.60,
        "f5": 8.80,
        "f6": 9.20,
        "f7": 9.10,
        "f8": 9.40,
        "price": 199.90,
        "pe": 24.0,
        "pe_forward": 21.0,
        "eps_growth_ntm_pct": 12.0,
        "growth_eps": 12.0,
        "eps_trailing": 8.33,
        "eps_forward": 9.52,
        "market_cap_b": 310.85,
        "market_cap": 310845.0,
        "ocf": 13500.0,
        "maintenance_capex": 1500.0,
        "owner_earnings": 12000.0,
        "score_fcf_yield": 6.90,
        "intrinsic_value": 220.00,
        "intrinsic_value_expected": 230.00,
        "mos_base_pct": 9.14,
        "mos_esperado_pct": 13.09,
        "score_mos": 6.40,
        "wacc": 7.5,
        "g_terminal": 2.5,
        "valuation_date": "21/10/2026",
        "publication_date": "21/10/2026",
        "price_date": "21/10/2026",
        "metodologia_version": "v5.0",
        "data_confidence": "Alta"
    }
}

# Update cqv_data.json
with open(DATA_FILE, "r", encoding="utf-8") as f:
    cqv_data = json.load(f)

existing_tickers = {x.get("ticker"): i for i, x in enumerate(cqv_data)}

for t, u in updates.items():
    if t in existing_tickers:
        idx = existing_tickers[t]
        for k, v in u.items():
            cqv_data[idx][k] = v
    else:
        # Append new ticker (PM)
        new_record = dict(u)
        new_record["close_history"] = "{'2021': 95.0, '2022': 101.2, '2023': 94.08, '2024': 120.5, '2025': 155.0, '2026': 199.9}"
        new_record["status"] = "Success"
        cqv_data.append(new_record)

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(cqv_data, f, indent=2, ensure_ascii=False)

print("Updated cqv_data.json with Block 2 successfully.")

# Update cqv_history.json
with open(HISTORY_FILE, "r", encoding="utf-8") as f:
    cqv_history = json.load(f)

for t, u in updates.items():
    if t not in cqv_history:
        cqv_history[t] = {}
    if "2026" not in cqv_history[t]:
        cqv_history[t]["2026"] = {"P1": None, "P2": None, "P3": None, "P4": None}
    
    snap = dict(u)
    cqv_history[t]["2026"]["P3"] = snap

with open(HISTORY_FILE, "w", encoding="utf-8") as f:
    json.dump(cqv_history, f, indent=2, ensure_ascii=False)

print("Updated cqv_history.json with Block 2 successfully.")
