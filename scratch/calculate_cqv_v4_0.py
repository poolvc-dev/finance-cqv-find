"""
Algoritmo Standalone: CQV v4.0 (Estándar Operativo de Calidad, Resiliencia y Valor)
Metodología: metodo_v4.0.md
Fórmula: CQV v4.0 = (F1*0.20) + (F2*0.15) + (F3*0.15) + (F4*0.15) + (F5*0.10) + (F6*0.10) + (F7*0.05) + (F8*0.10)
Pesos:
  F1 (Economía del negocio & Rentabilidad): 20%
  F2 (Solidez financiera): 15%
  F3 (Crecimiento durable): 15%
  F4 (Moat competitivo): 15%
  F5 (Asignación & Reinversión de capital): 10%
  F6 (Antifragilidad & Resiliencia): 10%
  F7 (Opcionalidad futura & Disrupción): 5%
  F8 (Valoración): 10%
Filtro: Si F2 < 4.0 o F4 < 4.0 => CQV v4.0 = min(CQV v4.0, 6.99)
"""

import sys
import json
import os

def calculate_cqv_v4_0(f1, f2, f3, f4, f5, f6, f7, f8):
    """
    Calcula el score CQV v4.0 oficial con ponderación auditada de 8 factores.
    """
    score = (f1 * 0.20) + (f2 * 0.15) + (f3 * 0.15) + (f4 * 0.15) + (f5 * 0.10) + (f6 * 0.10) + (f7 * 0.05) + (f8 * 0.10)
    
    # Filtro de Seguridad v4.0
    if f2 < 4.0 or f4 < 4.0:
        score = min(score, 6.99)
        
    return round(score, 2)

if __name__ == '__main__':
    ticker = sys.argv[1] if len(sys.argv) > 1 else 'FICO'
    print(f"=== CALCULADORA STANDALONE CQV v4.0 (ESTÁNDAR OFICIAL): {ticker} ===")
    
    f1, f2, f3, f4, f5, f6, f7, f8 = 10.00, 9.36, 9.82, 9.91, 9.69, 9.51, 9.45, 8.66
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
            f6 = t_cfg.get('f6', f6)
            f7 = t_cfg.get('f7', f7)
            f8 = t_cfg.get('f8', f8)

    cqv_v4 = calculate_cqv_v4_0(f1, f2, f3, f4, f5, f6, f7, f8)
    print(f"Factores v4.0: F1={f1}, F2={f2}, F3={f3}, F4={f4}, F5={f5}, F6={f6}, F7={f7}, F8={f8}")
    print(f"CQV v4.0 Score: {cqv_v4} / 10.00")
