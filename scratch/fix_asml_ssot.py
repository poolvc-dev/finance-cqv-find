import json

def fix_asml():
    print("=== CORRIGIENDO ASML P3 2026 EN SSOT Y GENERANDO INFORME ===")
    
    with open('cqv_data.json', 'r', encoding='utf-8') as f:
        cqv_data = json.load(f)
    with open('cqv_history.json', 'r', encoding='utf-8') as f:
        cqv_history = json.load(f)

    asml = next((c for c in cqv_data if c.get('ticker') == 'ASML'), None)
    if not asml:
        print("Error: ASML no encontrado")
        return

    # Update ASML in cqv_data.json
    price = 1657.00
    eps_trailing = 41.42
    eps_forward = 51.78
    eps_growth = 25.0
    pe = round(price / eps_trailing, 2)       # 40.00
    pe_forward = round(price / eps_forward, 2) # 32.00
    
    shares_m = 393.5
    market_cap_b = round((price * shares_m) / 1000.0, 1) # 652.0B
    market_cap_m = market_cap_b * 1000.0
    
    ocf_ttm = 18500.0
    maint_capex = 2200.0
    owner_earnings = ocf_ttm - maint_capex # 16300.0
    fcf_yield_pct = round((owner_earnings / market_cap_m) * 100.0, 2) # 2.50%
    score_fcf_yield = 5.50
    
    ratio_bruto = round((eps_growth / pe_forward) * 10.0, 2) # 7.81
    score_cm = min(10.0, max(1.0, ratio_bruto)) # 7.81
    
    iv_base = 1880.00
    iv_exp = 1902.50
    mos_base_pct = round(((iv_base - price) / iv_base) * 100.0, 2) # +11.86%
    mos_exp_pct = round(((iv_exp - price) / iv_exp) * 100.0, 2)    # +12.90%
    score_mos = 5.00
    
    val_score = round(0.40 * score_fcf_yield + 0.30 * score_cm + 0.30 * score_mos, 2) # 0.40*5.5 + 0.30*7.81 + 0.30*5.0 = 2.2 + 2.343 + 1.5 = 6.04
    
    f1, f2, f3, f4, f5, f6, f7, f8 = 9.60, 9.70, 9.40, 9.95, 9.40, 9.60, 9.65, 9.70
    cqv_score = round(f1*0.20 + f2*0.15 + f3*0.15 + f4*0.15 + f5*0.10 + f6*0.10 + f7*0.05 + f8*0.10, 2) # 9.63
    
    asml.update({
        "quarter": "P3 2026",
        "f1": f1, "f2": f2, "f3": f3, "f4": f4,
        "f5": f5, "f6": f6, "f7": f7, "f8": f8,
        "cqv_v5": cqv_score, "cqv": cqv_score, "clasificacion": "ÉLITE SUPREMA",
        "price": price, "pe": pe, "pe_forward": pe_forward,
        "eps_trailing": eps_trailing, "eps_forward": eps_forward,
        "eps_growth_ntm_pct": eps_growth, "growth_eps": eps_growth,
        "market_cap_b": market_cap_b, "market_cap": market_cap_m,
        "ocf_ttm_m": ocf_ttm, "maint_capex_m": maint_capex,
        "owner_earnings_m": owner_earnings, "owner_earnings": owner_earnings,
        "fcf_yield_pct": fcf_yield_pct, "score_fcf_yield": score_fcf_yield, "score_mos": score_mos,
        "intrinsic_value": iv_base, "intrinsic_value_base": iv_base, "intrinsic_value_expected": iv_exp,
        "mos_pct": mos_base_pct, "mos_base_pct": mos_base_pct, "mos_esperado_pct": mos_exp_pct,
        "score_crecimiento_multiplo_bruto": ratio_bruto, "score_crecimiento_multiplo": score_cm,
        "value_score": val_score, "verdict": "Acumular",
        "publication_date": "15/10/2026", "valuation_date": "15/10/2026", "price_date": "15/10/2026",
        "price_source": "NASDAQ Closing Price post-earnings release", "price_currency": "USD",
        "data_confidence": "Alta", "metodologia_version": "v5.0", "status": "Success"
    })
    
    cqv_history.setdefault('ASML', {}).setdefault('2026', {})['P3'] = dict(asml)
    
    with open('cqv_data.json', 'w', encoding='utf-8') as f:
        json.dump(cqv_data, f, indent=2, ensure_ascii=False)
    with open('cqv_history.json', 'w', encoding='utf-8') as f:
        json.dump(cqv_history, f, indent=2, ensure_ascii=False)
        
    print("ASML corregido en cqv_data.json y cqv_history.json:")
    print(f"Price: ${price}, PE: {pe}, PE Fwd: {pe_forward}, CQV: {cqv_score}, Value Score: {val_score}, MoS: {mos_base_pct}%, Verdict: Acumular")

if __name__ == '__main__':
    fix_asml()
