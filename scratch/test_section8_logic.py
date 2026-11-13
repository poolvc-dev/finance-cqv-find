import json

hist = json.load(open('cqv_history.json', encoding='utf-8'))

for ticker in ['MSFT', 'GOOGL', 'V', 'KLAC', 'ODFL', 'BSX', 'ORLY', 'KO', 'SPGI', 'VRT', 'CDNS', 'NOW']:
    hist_ticker = hist.get(ticker, {})
    hist_rows = []
    mermaid_labels = []
    mermaid_points = []
    for yr in sorted(hist_ticker.keys()):
        if yr.startswith('_') or yr in ['annual_legacy']: continue
        yr_obj = hist_ticker[yr]
        if isinstance(yr_obj, dict):
            for p_name in ['P1', 'P2', 'P3', 'P4']:
                if yr == '2026' and p_name == 'P4': continue
                snap = yr_obj.get(p_name)
                if snap and isinstance(snap, dict):
                    sc = snap.get('cqv_v5', snap.get('cqv', snap.get('cqv_v4', 'N/D')))
                    vs = snap.get('value_score', 'N/D')
                    cl = snap.get('clasificacion', 'N/D')
                    vd = snap.get('verdict', 'N/D')
                    f1 = snap.get('f1', '-')
                    f2 = snap.get('f2', '-')
                    f3 = snap.get('f3', '-')
                    f4 = snap.get('f4', '-')
                    f5 = snap.get('f5', '-')
                    f6 = snap.get('f6', '-')
                    f7 = snap.get('f7', '-')
                    f8 = snap.get('f8', '-')
                    
                    sc_str = f"{sc:.2f}" if isinstance(sc, (int, float)) else str(sc)
                    vs_str = f"{vs:.2f}" if isinstance(vs, (int, float)) else str(vs)
                    
                    hist_rows.append(f"| **{yr} {p_name}** | {f1} | {f2} | {f3} | {f4} | {f5} | {f6} | {f7} | {f8} | **{sc_str}** | {vs_str} | {cl} | {vd} |")
                    if isinstance(sc, (int, float)):
                        mermaid_labels.append(f'"{yr} {p_name}"')
                        mermaid_points.append(f"{sc:.2f}")

    print(f"=== {ticker} ===")
    print("Total rows:", len(hist_rows))
    print("Sample row:", hist_rows[-1])
    print("Mermaid labels len:", len(mermaid_labels[-6:]), "points len:", len(mermaid_points[-6:]))
    print("Labels:", mermaid_labels[-6:])
    print("Points:", mermaid_points[-6:])
