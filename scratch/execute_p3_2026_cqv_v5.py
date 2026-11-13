import json
import os

def update_p3_ssot():
    print("=== ACTUALIZACIÓN SSOT CQV v5.0 - PERIODO P3 2026 ===")
    
    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        cqv_data = json.load(f)
        
    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        cqv_history = json.load(f)

    # 1. TSM (Taiwan Semiconductor)
    tsm_entry = next((c for c in cqv_data if c.get('ticker') == 'TSM'), None)
    if tsm_entry:
        tsm_entry.update({
            "quarter": "P3 2026",
            "f1": 9.50, "f2": 9.60, "f3": 9.40, "f4": 9.85,
            "f5": 9.30, "f6": 9.50, "f7": 9.50, "f8": 9.30,
            "cqv_v5": 9.51, "cqv": 9.51, "clasificacion": "ÉLITE SUPREMA",
            "price": 201.63, "pe": 26.50, "pe_forward": 20.50,
            "eps_trailing": 7.61, "eps_forward": 9.84, "eps_growth_ntm_pct": 32.0, "growth_eps": 32.0,
            "market_cap_b": 1045.0, "market_cap": 1045000.0,
            "ocf_ttm_m": 48500.0, "maint_capex_m": 16500.0, "owner_earnings_m": 32000.0, "owner_earnings": 32000.0,
            "fcf_yield_pct": 3.06, "score_fcf_yield": 6.50, "score_mos": 6.67,
            "intrinsic_value": 252.0, "intrinsic_value_base": 252.0, "intrinsic_value_expected": 258.0,
            "mos_pct": 19.99, "mos_base_pct": 19.99, "mos_esperado_pct": 21.85,
            "score_crecimiento_multiplo_bruto": 15.61, "score_crecimiento_multiplo": 10.0,
            "value_score": 7.60, "verdict": "Comprar / Revisar Compra",
            "publication_date": "17/10/2026", "valuation_date": "17/10/2026", "price_date": "17/10/2026",
            "price_source": "NYSE Closing Price post-earnings SEC 6-K release", "price_currency": "USD",
            "data_confidence": "Alta", "metodologia_version": "v5.0", "status": "Success"
        })
        cqv_history.setdefault('TSM', {}).setdefault('2026', {})['P3'] = dict(tsm_entry)

    # 2. ASML (ASML Holding N.V.)
    asml_entry = next((c for c in cqv_data if c.get('ticker') == 'ASML'), None)
    if asml_entry:
        asml_entry.update({
            "quarter": "P3 2026",
            "f1": 9.40, "f2": 9.70, "f3": 8.90, "f4": 9.95,
            "f5": 9.30, "f6": 9.30, "f7": 9.50, "f8": 9.50,
            "cqv_v5": 9.45, "cqv": 9.45, "clasificacion": "ÉLITE",
            "price": 730.43, "pe": 34.10, "pe_forward": 25.20,
            "eps_trailing": 21.42, "eps_forward": 29.00, "eps_growth_ntm_pct": 22.0, "growth_eps": 22.0,
            "market_cap_b": 288.0, "market_cap": 288000.0,
            "ocf_ttm_m": 10200.0, "maint_capex_m": 1300.0, "owner_earnings_m": 8900.0, "owner_earnings": 8900.0,
            "fcf_yield_pct": 3.09, "score_fcf_yield": 6.50, "score_mos": 8.20,
            "intrinsic_value": 980.0, "intrinsic_value_base": 980.0, "intrinsic_value_expected": 995.0,
            "mos_pct": 25.47, "mos_base_pct": 25.47, "mos_esperado_pct": 26.59,
            "score_crecimiento_multiplo_bruto": 8.73, "score_crecimiento_multiplo": 8.73,
            "value_score": 7.68, "verdict": "Comprar / Revisar Compra",
            "publication_date": "15/10/2026", "valuation_date": "15/10/2026", "price_date": "15/10/2026",
            "price_source": "NASDAQ Closing Price post-earnings leak/release", "price_currency": "USD",
            "data_confidence": "Alta", "metodologia_version": "v5.0", "status": "Success"
        })
        cqv_history.setdefault('ASML', {}).setdefault('2026', {})['P3'] = dict(asml_entry)

    # 3. JPM (JPMorgan Chase & Co.)
    jpm_entry = next((c for c in cqv_data if c.get('ticker') == 'JPM'), None)
    if jpm_entry:
        jpm_entry.update({
            "quarter": "P3 2026",
            "f1": 9.25, "f2": 9.50, "f3": 8.85, "f4": 9.60,
            "f5": 9.25, "f6": 9.80, "f7": 8.90, "f8": 9.40,
            "cqv_v5": 9.32, "cqv": 9.32, "clasificacion": "ÉLITE",
            "price": 214.64, "pe": 11.50, "pe_forward": 11.80,
            "eps_trailing": 18.66, "eps_forward": 18.19, "eps_growth_ntm_pct": 10.5, "growth_eps": 10.5,
            "market_cap_b": 610.0, "market_cap": 610000.0,
            "ocf_ttm_m": 46000.0, "maint_capex_m": 2500.0, "owner_earnings_m": 43500.0, "owner_earnings": 43500.0,
            "fcf_yield_pct": 7.13, "score_fcf_yield": 9.13, "score_mos": 6.64,
            "intrinsic_value": 268.0, "intrinsic_value_base": 268.0, "intrinsic_value_expected": 262.0,
            "mos_pct": 19.91, "mos_base_pct": 19.91, "mos_esperado_pct": 18.08,
            "score_crecimiento_multiplo_bruto": 8.90, "score_crecimiento_multiplo": 8.90,
            "value_score": 8.31, "verdict": "Comprar / Revisar Compra",
            "publication_date": "11/10/2026", "valuation_date": "11/10/2026", "price_date": "11/10/2026",
            "price_source": "NYSE Closing Price post-earnings release", "price_currency": "USD",
            "data_confidence": "Alta", "metodologia_version": "v5.0", "status": "Success"
        })
        cqv_history.setdefault('JPM', {}).setdefault('2026', {})['P3'] = dict(jpm_entry)

    # 4. UNH (UnitedHealth Group)
    unh_entry = next((c for c in cqv_data if c.get('ticker') == 'UNH'), None)
    if unh_entry:
        unh_entry.update({
            "quarter": "P3 2026",
            "f1": 9.30, "f2": 9.40, "f3": 9.10, "f4": 9.60,
            "f5": 9.30, "f6": 9.35, "f7": 8.80, "f8": 9.50,
            "cqv_v5": 9.33, "cqv": 9.33, "clasificacion": "ÉLITE",
            "price": 530.36, "pe": 21.00, "pe_forward": 17.50,
            "eps_trailing": 25.25, "eps_forward": 30.30, "eps_growth_ntm_pct": 12.5, "growth_eps": 12.5,
            "market_cap_b": 488.0, "market_cap": 488000.0,
            "ocf_ttm_m": 32500.0, "maint_capex_m": 3700.0, "owner_earnings_m": 28800.0, "owner_earnings": 28800.0,
            "fcf_yield_pct": 5.90, "score_fcf_yield": 8.00, "score_mos": 6.14,
            "intrinsic_value": 650.0, "intrinsic_value_base": 650.0, "intrinsic_value_expected": 645.0,
            "mos_pct": 18.41, "mos_base_pct": 18.41, "mos_esperado_pct": 17.77,
            "score_crecimiento_multiplo_bruto": 7.14, "score_crecimiento_multiplo": 7.14,
            "value_score": 7.18, "verdict": "Acumular",
            "publication_date": "15/10/2026", "valuation_date": "15/10/2026", "price_date": "15/10/2026",
            "price_source": "NYSE Closing Price post-earnings release", "price_currency": "USD",
            "data_confidence": "Alta", "metodologia_version": "v5.0", "status": "Success"
        })
        cqv_history.setdefault('UNH', {}).setdefault('2026', {})['P3'] = dict(unh_entry)

    # 5. PGR (The Progressive Corp)
    pgr_entry = next((c for c in cqv_data if c.get('ticker') == 'PGR'), None)
    if pgr_entry:
        pgr_entry.update({
            "quarter": "P3 2026",
            "f1": 9.40, "f2": 9.45, "f3": 9.25, "f4": 9.30,
            "f5": 9.20, "f6": 9.35, "f7": 8.60, "f8": 9.20,
            "cqv_v5": 9.28, "cqv": 9.28, "clasificacion": "ÉLITE",
            "price": 242.83, "pe": 17.50, "pe_forward": 15.20,
            "eps_trailing": 13.88, "eps_forward": 15.98, "eps_growth_ntm_pct": 18.5, "growth_eps": 18.5,
            "market_cap_b": 142.0, "market_cap": 142000.0,
            "ocf_ttm_m": 8500.0, "maint_capex_m": 700.0, "owner_earnings_m": 7800.0, "owner_earnings": 7800.0,
            "fcf_yield_pct": 5.49, "score_fcf_yield": 7.80, "score_mos": 5.42,
            "intrinsic_value": 290.0, "intrinsic_value_base": 290.0, "intrinsic_value_expected": 295.0,
            "mos_pct": 16.27, "mos_base_pct": 16.27, "mos_esperado_pct": 17.68,
            "score_crecimiento_multiplo_bruto": 12.17, "score_crecimiento_multiplo": 10.0,
            "value_score": 7.75, "verdict": "Acumular",
            "publication_date": "15/10/2026", "valuation_date": "15/10/2026", "price_date": "15/10/2026",
            "price_source": "NYSE Closing Price post-earnings release", "price_currency": "USD",
            "data_confidence": "Alta", "metodologia_version": "v5.0", "status": "Success"
        })
        cqv_history.setdefault('PGR', {}).setdefault('2026', {})['P3'] = dict(pgr_entry)

    # 6. BLK (BlackRock, Inc.)
    blk_entry = next((c for c in cqv_data if c.get('ticker') == 'BLK'), None)
    if blk_entry:
        blk_entry.update({
            "quarter": "P3 2026",
            "f1": 9.25, "f2": 9.10, "f3": 9.35, "f4": 8.20,
            "f5": 8.10, "f6": 9.30, "f7": 5.00, "f8": 8.10,
            "cqv_v5": 8.60, "cqv": 8.60, "clasificacion": "ALTA CALIDAD",
            "price": 990.26, "pe": 24.50, "pe_forward": 21.50,
            "eps_trailing": 40.42, "eps_forward": 46.06, "eps_growth_ntm_pct": 14.0, "growth_eps": 14.0,
            "market_cap_b": 148.0, "market_cap": 148000.0,
            "ocf_ttm_m": 6600.0, "maint_capex_m": 400.0, "owner_earnings_m": 6200.0, "owner_earnings": 6200.0,
            "fcf_yield_pct": 4.19, "score_fcf_yield": 6.80, "score_mos": 4.63,
            "intrinsic_value": 1150.0, "intrinsic_value_base": 1150.0, "intrinsic_value_expected": 1120.0,
            "mos_pct": 13.89, "mos_base_pct": 13.89, "mos_esperado_pct": 11.58,
            "score_crecimiento_multiplo_bruto": 6.51, "score_crecimiento_multiplo": 6.51,
            "value_score": 6.06, "verdict": "Acumular",
            "publication_date": "11/10/2026", "valuation_date": "11/10/2026", "price_date": "11/10/2026",
            "price_source": "NYSE Closing Price post-earnings release", "price_currency": "USD",
            "data_confidence": "Alta", "metodologia_version": "v5.0", "status": "Success"
        })
        cqv_history.setdefault('BLK', {}).setdefault('2026', {})['P3'] = dict(blk_entry)

    # 7. FAST (Fastenal Company)
    fast_entry = next((c for c in cqv_data if c.get('ticker') == 'FAST'), None)
    if fast_entry:
        fast_entry.update({
            "quarter": "P3 2026",
            "f1": 8.85, "f2": 8.80, "f3": 9.00, "f4": 8.00,
            "f5": 8.00, "f6": 8.95, "f7": 5.00, "f8": 8.00,
            "cqv_v5": 8.38, "cqv": 8.38, "clasificacion": "ALTA CALIDAD",
            "price": 78.18, "pe": 37.50, "pe_forward": 33.50,
            "eps_trailing": 2.08, "eps_forward": 2.33, "eps_growth_ntm_pct": 9.0, "growth_eps": 9.0,
            "market_cap_b": 44.8, "market_cap": 44800.0,
            "ocf_ttm_m": 1250.0, "maint_capex_m": 220.0, "owner_earnings_m": 1030.0, "owner_earnings": 1030.0,
            "fcf_yield_pct": 2.30, "score_fcf_yield": 4.50, "score_mos": 2.31,
            "intrinsic_value": 84.0, "intrinsic_value_base": 84.0, "intrinsic_value_expected": 82.0,
            "mos_pct": 6.93, "mos_base_pct": 6.93, "mos_esperado_pct": 4.66,
            "score_crecimiento_multiplo_bruto": 2.69, "score_crecimiento_multiplo": 2.69,
            "value_score": 3.30, "verdict": "Mantener",
            "publication_date": "11/10/2026", "valuation_date": "11/10/2026", "price_date": "11/10/2026",
            "price_source": "NASDAQ Closing Price post-earnings release", "price_currency": "USD",
            "data_confidence": "Alta", "metodologia_version": "v5.0", "status": "Success"
        })
        cqv_history.setdefault('FAST', {}).setdefault('2026', {})['P3'] = dict(fast_entry)

    # 8. IBKR (Interactive Brokers Group)
    ibkr_entry = next((c for c in cqv_data if c.get('ticker') == 'IBKR'), None)
    if ibkr_entry:
        ibkr_entry.update({
            "quarter": "P3 2026",
            "f1": 10.0, "f2": 9.30, "f3": 9.40, "f4": 8.20,
            "f5": 8.10, "f6": 9.70, "f7": 4.50, "f8": 8.10,
            "cqv_v5": 8.81, "cqv": 8.81, "clasificacion": "ALTA CALIDAD",
            "price": 89.24, "pe": 20.50, "pe_forward": 17.00,
            "eps_trailing": 4.35, "eps_forward": 5.25, "eps_growth_ntm_pct": 16.5, "growth_eps": 16.5,
            "market_cap_b": 38.0, "market_cap": 38000.0,
            "ocf_ttm_m": 2900.0, "maint_capex_m": 120.0, "owner_earnings_m": 2780.0, "owner_earnings": 2780.0,
            "fcf_yield_pct": 7.32, "score_fcf_yield": 9.30, "score_mos": 5.79,
            "intrinsic_value": 108.0, "intrinsic_value_base": 108.0, "intrinsic_value_expected": 105.0,
            "mos_pct": 17.37, "mos_base_pct": 17.37, "mos_esperado_pct": 15.01,
            "score_crecimiento_multiplo_bruto": 9.71, "score_crecimiento_multiplo": 9.71,
            "value_score": 8.37, "verdict": "Acumular",
            "publication_date": "15/10/2026", "valuation_date": "15/10/2026", "price_date": "15/10/2026",
            "price_source": "NASDAQ Closing Price post-earnings release", "price_currency": "USD",
            "data_confidence": "Alta", "metodologia_version": "v5.0", "status": "Success"
        })
        cqv_history.setdefault('IBKR', {}).setdefault('2026', {})['P3'] = dict(ibkr_entry)

    # 9. BAC (Bank of America Corporation) - Incorporación al Universo
    bac_entry = next((c for c in cqv_data if c.get('ticker') == 'BAC'), None)
    if not bac_entry:
        bac_entry = {
            "ticker": "BAC",
            "name": "Bank of America Corporation",
            "sector": "Financial Services / Diversified Banking & Wealth Management",
        }
        cqv_data.append(bac_entry)
        
    bac_entry.update({
        "quarter": "P3 2026",
        "f1": 8.20, "f2": 8.90, "f3": 7.80, "f4": 8.60,
        "f5": 8.00, "f6": 8.50, "f7": 7.50, "f8": 8.80,
        "cqv_v5": 8.34, "cqv": 8.34, "clasificacion": "ALTA CALIDAD",
        "price": 41.82, "pe": 13.50, "pe_forward": 11.50,
        "eps_trailing": 3.10, "eps_forward": 3.64, "eps_growth_ntm_pct": 10.0, "growth_eps": 10.0,
        "market_cap_b": 328.0, "market_cap": 328000.0,
        "ocf_ttm_m": 22000.0, "maint_capex_m": 1800.0, "owner_earnings_m": 20200.0, "owner_earnings": 20200.0,
        "fcf_yield_pct": 6.16, "score_fcf_yield": 8.20, "score_mos": 4.59,
        "intrinsic_value": 48.50, "intrinsic_value_base": 48.50, "intrinsic_value_expected": 47.0,
        "mos_pct": 13.77, "mos_base_pct": 13.77, "mos_esperado_pct": 11.02,
        "score_crecimiento_multiplo_bruto": 8.70, "score_crecimiento_multiplo": 8.70,
        "value_score": 7.27, "verdict": "Acumular",
        "publication_date": "15/10/2026", "valuation_date": "15/10/2026", "price_date": "15/10/2026",
        "price_source": "NYSE Closing Price post-earnings release", "price_currency": "USD",
        "data_confidence": "Alta", "metodologia_version": "v5.0", "status": "Success"
    })
    cqv_history.setdefault('BAC', {}).setdefault('2026', {})['P3'] = dict(bac_entry)

    with open('cqv_data.json', 'w', encoding='utf-8') as f:
        json.dump(cqv_data, f, indent=2, ensure_ascii=False)
        
    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(cqv_history, f, indent=2, ensure_ascii=False)
        
    print("cqv_data.json y cqv_history.json actualizados exitosamente.")

if __name__ == '__main__':
    update_p3_ssot()
