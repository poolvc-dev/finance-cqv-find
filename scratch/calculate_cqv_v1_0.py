"""
Algoritmo Standalone: CQV v1.0 (5 Macro-Factores Legacy)
Metodología: metodo_v1.0.md
Fórmula: CQV v1.0 = (F1 * 0.25) + (F2 * 0.15) + (F3 * 0.15) + (F4 * 0.25) + (F5 * 0.20)
"""

import sys
import json
import os

def calculate_cqv_v1_0(f1, f2, f3, f4, f5):
    """
    Calcula el score CQV v1.0 a partir de los 5 factores base (1.0 a 10.0).
    """
    score = (f1 * 0.25) + (f2 * 0.15) + (f3 * 0.15) + (f4 * 0.25) + (f5 * 0.20)
    return round(score, 2)

def calculate_peg_score_v1_0(pe_forward, eps_growth_pct):
    """
    Calcula el Score PEG Normalizado (escala 1.0 a 10.0).
    Score PEG = min(10.0, max(1.0, (eps_growth_pct / pe_forward) * 10.0))
    """
    if not pe_forward or pe_forward <= 0 or not eps_growth_pct or eps_growth_pct <= 0:
        return 5.00
    val = (eps_growth_pct / pe_forward) * 10.0
    return round(max(1.0, min(10.0, val)), 2)

if __name__ == '__main__':
    ticker = sys.argv[1] if len(sys.argv) > 1 else 'FICO'
    print(f"=== CALCULADORA STANDALONE CQV v1.0: {ticker} ===")
    
    # Intentar cargar datos de cqv_qualitative_config.json o cqv_data.json
    f1, f2, f3, f4, f5 = 9.90, 8.80, 9.60, 9.90, 9.50
    if os.path.exists('cqv_qualitative_config.json'):
        with open('cqv_qualitative_config.json', 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        if ticker in cfg:
            t_cfg = cfg[ticker]
            f1 = t_cfg.get('f1', f1)
            f2 = t_cfg.get('f2', f2)
            f3 = t_cfg.get('f3', f3)
            f4 = t_cfg.get('f4', f4)
            f5 = t_cfg.get('f5', f5)

    cqv_v1 = calculate_cqv_v1_0(f1, f2, f3, f4, f5)
    print(f"Factores v1.0: F1={f1}, F2={f2}, F3={f3}, F4={f4}, F5={f5}")
    print(f"CQV v1.0 Score: {cqv_v1} / 10.00")
