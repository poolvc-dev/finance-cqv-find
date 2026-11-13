import json

DATA_FILE = "cqv_data.json"
HISTORY_FILE = "cqv_history.json"

updates = {
    "TSLA": {
        "ticker": "TSLA",
        "name": "Tesla, Inc.",
        "sector": "Consumer Cyclical / Electric Vehicles & Clean Energy",
        "quarter": "P3 2026",
        "f1": 6.80,
        "f2": 9.60,
        "f3": 7.80,
        "f4": 8.80,
        "f5": 7.70,
        "f6": 7.50,
        "f7": 9.70,
        "f8": 7.20,
        "price": 386.47,
        "pe": 340.0,
        "pe_forward": 170.0,
        "eps_growth_ntm_pct": 28.0,
        "growth_eps": 28.0,
        "eps_trailing": 1.14,
        "eps_forward": 2.27,
        "market_cap_b": 1383.56,
        "market_cap": 1383560.0,
        "ocf": 15500.0,
        "maintenance_capex": 5000.0,
        "owner_earnings": 10500.0,
        "score_fcf_yield": 2.10,
        "intrinsic_value": 185.00,
        "intrinsic_value_expected": 210.00,
        "mos_base_pct": -52.13,
        "mos_esperado_pct": -45.66,
        "score_mos": 1.00,
        "wacc": 9.0,
        "g_terminal": 4.0,
        "valuation_date": "21/10/2026",
        "publication_date": "21/10/2026",
        "price_date": "21/10/2026",
        "metodologia_version": "v5.0",
        "data_confidence": "Media"
    },
    "META": {
        "ticker": "META",
        "name": "Meta Platforms, Inc.",
        "sector": "Communication Services / Digital Advertising & Artificial Intelligence",
        "quarter": "P3 2026",
        "f1": 9.60,
        "f2": 9.30,
        "f3": 9.70,
        "f4": 9.90,
        "f5": 9.10,
        "f6": 9.50,
        "f7": 9.70,
        "f8": 9.30,
        "price": 697.43,
        "pe": 26.5,
        "pe_forward": 21.0,
        "eps_growth_ntm_pct": 18.5,
        "growth_eps": 18.5,
        "eps_trailing": 26.30,
        "eps_forward": 33.20,
        "market_cap_b": 1792.40,
        "market_cap": 1792400.0,
        "ocf": 118000.0,
        "maintenance_capex": 32000.0,
        "owner_earnings": 86000.0,
        "score_fcf_yield": 7.80,
        "intrinsic_value": 825.00,
        "intrinsic_value_expected": 850.00,
        "mos_base_pct": 15.46,
        "mos_esperado_pct": 17.95,
        "score_mos": 7.20,
        "wacc": 8.5,
        "g_terminal": 3.5,
        "valuation_date": "21/10/2026",
        "publication_date": "21/10/2026",
        "price_date": "21/10/2026",
        "metodologia_version": "v5.0",
        "data_confidence": "Alta"
    },
    "TXN": {
        "ticker": "TXN",
        "name": "Texas Instruments Incorporated",
        "sector": "Technology / Analog & Embedded Processing Semiconductors",
        "quarter": "P3 2026",
        "f1": 9.40,
        "f2": 9.30,
        "f3": 8.80,
        "f4": 9.60,
        "f5": 9.50,
        "f6": 9.40,
        "f7": 8.70,
        "f8": 9.60,
        "price": 284.65,
        "pe": 33.5,
        "pe_forward": 28.0,
        "eps_growth_ntm_pct": 22.0,
        "growth_eps": 22.0,
        "eps_trailing": 8.50,
        "eps_forward": 10.16,
        "market_cap_b": 262.16,
        "market_cap": 262160.0,
        "ocf": 9896.0,
        "maintenance_capex": 1200.0,
        "owner_earnings": 8696.0,
        "score_fcf_yield": 6.20,
        "intrinsic_value": 310.00,
        "intrinsic_value_expected": 320.00,
        "mos_base_pct": 8.18,
        "mos_esperado_pct": 11.05,
        "score_mos": 6.20,
        "wacc": 8.0,
        "g_terminal": 3.5,
        "valuation_date": "21/10/2026",
        "publication_date": "21/10/2026",
        "price_date": "21/10/2026",
        "metodologia_version": "v5.0",
        "data_confidence": "Alta"
    },
    "LRCX": {
        "ticker": "LRCX",
        "name": "Lam Research Corporation",
        "sector": "Technology / Semiconductor Wafer Fabrication Equipment",
        "quarter": "P3 2026",
        "f1": 9.50,
        "f2": 9.60,
        "f3": 9.30,
        "f4": 9.60,
        "f5": 9.30,
        "f6": 9.30,
        "f7": 9.50,
        "f8": 8.90,
        "price": 260.81,
        "pe": 35.8,
        "pe_forward": 28.5,
        "eps_growth_ntm_pct": 25.0,
        "growth_eps": 25.0,
        "eps_trailing": 7.28,
        "eps_forward": 9.15,
        "market_cap_b": 326.01,
        "market_cap": 326010.0,
        "ocf": 8800.0,
        "maintenance_capex": 720.0,
        "owner_earnings": 8080.0,
        "score_fcf_yield": 5.20,
        "intrinsic_value": 295.00,
        "intrinsic_value_expected": 305.00,
        "mos_base_pct": 11.59,
        "mos_esperado_pct": 14.49,
        "score_mos": 6.80,
        "wacc": 8.5,
        "g_terminal": 3.5,
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

for item in cqv_data:
    t = item.get("ticker")
    if t in updates:
        for k, v in updates[t].items():
            item[k] = v

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(cqv_data, f, indent=2, ensure_ascii=False)

print("Updated cqv_data.json successfully.")

# Update cqv_history.json
with open(HISTORY_FILE, "r", encoding="utf-8") as f:
    cqv_history = json.load(f)

for t, u in updates.items():
    if t not in cqv_history:
        cqv_history[t] = {}
    if "2026" not in cqv_history[t]:
        cqv_history[t]["2026"] = {"P1": None, "P2": None, "P3": None, "P4": None}
    
    # Preserve existing P3 if exists or set new dict
    snap = dict(u)
    cqv_history[t]["2026"]["P3"] = snap

with open(HISTORY_FILE, "w", encoding="utf-8") as f:
    json.dump(cqv_history, f, indent=2, ensure_ascii=False)

print("Updated cqv_history.json successfully.")
