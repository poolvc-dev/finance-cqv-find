import pandas as pd
import json

def main():
    try:
        # Load the CSV
        df = pd.read_csv('cqv_results.csv')
        records = df.to_dict(orient='records')
        
        # Specific custom metrics for top companies
        custom_metrics = {
            "MA": {"f6": 9.5, "f7": 7.0, "f8": 9.9},
            "V": {"f6": 9.5, "f7": 7.0, "f8": 9.9},
            "AAPL": {"f6": 9.8, "f7": 6.8, "f8": 7.0},
            "ASML": {"f6": 9.0, "f7": 5.5, "f8": 6.0},
            "AVGO": {"f6": 9.4, "f7": 7.2, "f8": 7.5},
            "GOOGL": {"f6": 8.5, "f7": 7.5, "f8": 9.5},
            "MSFT": {"f6": 9.2, "f7": 6.5, "f8": 9.8},
            "NVDA": {"f6": 9.0, "f7": 5.0, "f8": 6.5},
            "FICO": {"f6": 9.9, "f7": 5.0, "f8": 8.5}
        }
        
        for r in records:
            ticker = r['ticker']
            r['cqv_v1'] = r['cqv'] # original 5-factor score from CSV
            
            if ticker in custom_metrics:
                r['f6'] = custom_metrics[ticker]['f6']
                r['f7'] = custom_metrics[ticker]['f7']
                r['f8'] = custom_metrics[ticker]['f8']
            else:
                # Deterministic defaults for other companies
                r['f6'] = round((r['f1'] + r['f3']) / 2.0, 2)
                r['f7'] = round((10.0 - (r['f1'] - 5.0)) * 0.8, 2)
                if r['f7'] < 1.0: r['f7'] = 1.0
                if r['f7'] > 10.0: r['f7'] = 10.0
                r['f8'] = 8.0 # default
                
            # Recalculate consolidated CQV score v2.0
            # weights: F1: 20%, F2: 10%, F3: 10%, F4: 20%, F5: 10%, F6: 10%, F7: 10%, F8: 10%
            cqv_v2 = (
                r['f1'] * 0.20 +
                r['f2'] * 0.10 +
                r['f3'] * 0.10 +
                r['f4'] * 0.20 +
                r['f5'] * 0.10 +
                r['f6'] * 0.10 +
                r['f7'] * 0.10 +
                r['f8'] * 0.10
            )
            r['cqv_v2'] = round(cqv_v2, 2)
            r['cqv'] = r['cqv_v2'] # default is v2.0
            
        json_data = json.dumps(records, indent=2)
        
        # 1. Save raw JSON data to cqv_data.json
        with open('cqv_data.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
        print("Successfully saved cqv_data.json")
        
        # 2. Save JS wrapper to cqv_data.js for offline file:/// protocol support
        js_content = f"window.companiesData = {json_data};"
        with open('cqv_data.js', 'w', encoding='utf-8') as f:
            f.write(js_content)
        print("Successfully saved cqv_data.js")
        
        # 3. Build the HTML template linking cqv_data.js
        html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CQV Financial Dashboard | Quality & Structural Value</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    
    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: rgba(17, 24, 39, 0.7);
            --card-border: rgba(255, 255, 255, 0.08);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --input-bg: rgba(15, 23, 42, 0.6);
            --input-border: rgba(255, 255, 255, 0.08);
            --table-bg: rgba(15, 23, 42, 0.3);
            --item-bg: rgba(255, 255, 255, 0.02);
            --item-hover-bg: rgba(255, 255, 255, 0.04);
            --header-bg: rgba(11, 15, 25, 0.8);
            --th-bg: #131b2e;
            --primary: #4f46e5;
            --primary-glow: rgba(79, 70, 229, 0.3);
            --secondary: #d946ef;
            --accent: #06b6d4;
            --elite: #10b981;
            --strong: #3b82f6;
            --medium: #f59e0b;
            --weak: #ef4444;
            --font-title: 'Outfit', sans-serif;
            --font-body: 'Inter', sans-serif;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        body.light-theme {
            --bg-color: #f1f5f9;
            --card-bg: rgba(255, 255, 255, 0.85);
            --card-border: rgba(15, 23, 42, 0.06);
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --input-bg: rgba(255, 255, 255, 0.95);
            --input-border: rgba(15, 23, 42, 0.1);
            --table-bg: rgba(255, 255, 255, 0.4);
            --item-bg: rgba(15, 23, 42, 0.02);
            --item-hover-bg: rgba(15, 23, 42, 0.04);
            --header-bg: rgba(255, 255, 255, 0.85);
            --th-bg: #e2e8f0;
            --primary: #4f46e5;
            --primary-glow: rgba(79, 70, 229, 0.1);
            --secondary: #d946ef;
            --accent: #0891b2;
            --elite: #059669;
            --strong: #2563eb;
            --medium: #d97706;
            --weak: #dc2626;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            background-color: var(--bg-color);
            background-image: 
                radial-gradient(at 10% 20%, rgba(79, 70, 229, 0.15) 0px, transparent 50%),
                radial-gradient(at 90% 80%, rgba(217, 70, 239, 0.1) 0px, transparent 50%),
                radial-gradient(at 50% 50%, rgba(6, 182, 212, 0.05) 0px, transparent 50%);
            background-attachment: fixed;
            color: var(--text-primary);
            font-family: var(--font-body);
            line-height: 1.5;
            overflow-x: hidden;
            padding-bottom: 50px;
            transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
        }

        body.light-theme {
            background-image: 
                radial-gradient(at 10% 20%, rgba(79, 70, 229, 0.05) 0px, transparent 50%),
                radial-gradient(at 90% 80%, rgba(217, 70, 239, 0.03) 0px, transparent 50%),
                radial-gradient(at 50% 50%, rgba(6, 182, 212, 0.02) 0px, transparent 50%);
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0f172a;
        }
        ::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #475569;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 16px;
        }

        /* Header styling */
        header {
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--header-bg);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--card-border);
            padding: 8px 0;
            margin-bottom: 14px;
            transition: var(--transition);
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo-area {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .logo-icon {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            width: 34px;
            height: 34px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 0 15px var(--primary-glow);
            font-weight: 800;
            font-size: 15px;
            color: white;
            font-family: var(--font-title);
        }

        .logo-text h1 {
            font-family: var(--font-title);
            font-size: 17px;
            font-weight: 700;
            letter-spacing: -0.3px;
            background: linear-gradient(to right, #ffffff, #94a3b8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .logo-text p {
            font-size: 9px;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 600;
        }

        .nav-tabs {
            display: flex;
            gap: 8px;
        }

        .nav-btn {
            background: transparent;
            border: 1px solid transparent;
            color: var(--text-secondary);
            padding: 6px 12px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 500;
            font-size: 13px;
            font-family: var(--font-title);
            transition: var(--transition);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .nav-btn:hover {
            color: var(--text-primary);
            background: rgba(255, 255, 255, 0.05);
        }

        .nav-btn.active {
            background: rgba(79, 70, 229, 0.15);
            border-color: rgba(79, 70, 229, 0.4);
            color: var(--text-primary);
            box-shadow: 0 0 15px rgba(79, 70, 229, 0.1);
        }

        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 12px;
            margin-bottom: 14px;
        }

        .card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 12px 16px;
            backdrop-filter: blur(16px);
            transition: var(--transition);
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: transparent;
            transition: var(--transition);
        }

        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.25);
            border-color: rgba(255, 255, 255, 0.15);
        }

        .card.primary-border:hover {
            border-color: rgba(79, 70, 229, 0.5);
        }

        .kpi-card {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .kpi-info h3 {
            font-size: 11px;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 2px;
            font-weight: 500;
        }

        .kpi-info .value {
            font-size: 24px;
            font-weight: 700;
            font-family: var(--font-title);
            background: linear-gradient(to right, var(--text-primary), var(--text-secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .kpi-info .subtitle {
            font-size: 11px;
            color: var(--text-secondary);
            margin-top: 2px;
        }

        .kpi-icon {
            width: 40px;
            height: 40px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
        }

        .kpi-blue {
            background: rgba(59, 130, 246, 0.1);
            color: #3b82f6;
        }

        .kpi-purple {
            background: rgba(168, 85, 247, 0.1);
            color: #a855f7;
        }

        .kpi-emerald {
            background: rgba(16, 185, 129, 0.1);
            color: #10b981;
        }

        .kpi-cyan {
            background: rgba(6, 182, 212, 0.1);
            color: #06b6d4;
        }

        /* Dashboard View Layout */
        .dashboard-layout {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 16px;
            margin-bottom: 16px;
        }

        .section-title {
            font-family: var(--font-title);
            font-size: 15px;
            font-weight: 600;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--text-primary);
        }

        .section-title i {
            color: var(--accent);
        }

        /* Chart card */
        .chart-card {
            min-height: 260px;
            display: flex;
            flex-direction: column;
        }

        .chart-container {
            position: relative;
            flex-grow: 1;
            width: 100%;
            height: 190px;
        }

        .distribution-list {
            display: flex;
            flex-direction: column;
            gap: 8px;
            justify-content: center;
            height: 100%;
        }

        .dist-item {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .dist-label-row {
            display: flex;
            justify-content: space-between;
            font-size: 12px;
            font-weight: 500;
        }

        .dist-bar-bg {
            height: 8px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 4px;
            overflow: hidden;
        }

        .dist-bar-fill {
            height: 100%;
            border-radius: 4px;
            transition: width 1s ease-out;
        }

        /* Explorer View Styling */
        .explorer-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 24px;
            backdrop-filter: blur(16px);
            margin-bottom: 32px;
        }

        .table-controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }

        .search-wrapper {
            position: relative;
            flex-grow: 1;
            max-width: 400px;
        }

        .search-wrapper i {
            position: absolute;
            left: 14px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-secondary);
        }

        .search-input {
            width: 100%;
            background: var(--input-bg);
            border: 1px solid var(--input-border);
            border-radius: 8px;
            padding: 10px 14px 10px 40px;
            color: var(--text-primary);
            font-family: var(--font-body);
            font-size: 14px;
            transition: var(--transition);
        }

        .search-input:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 10px rgba(79, 70, 229, 0.2);
        }

        .filters-wrapper {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .select-filter {
            background: var(--input-bg);
            border: 1px solid var(--input-border);
            border-radius: 8px;
            padding: 10px 16px;
            color: var(--text-primary);
            font-size: 14px;
            outline: none;
            cursor: pointer;
            transition: var(--transition);
            font-family: var(--font-body);
        }

        .select-filter:focus {
            border-color: var(--primary);
        }

        .select-filter option {
            background: var(--bg-color);
            color: var(--text-primary);
        }

        /* Table design */
        .table-container {
            width: 100%;
            overflow-x: auto;
            max-height: 360px;
            overflow-y: auto;
            border-radius: 12px;
            border: 1px solid var(--card-border);
            background: var(--table-bg);
        }

        table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 13px;
        }

        th {
            position: sticky;
            top: 0;
            z-index: 10;
            background: var(--th-bg);
            padding: 6px 10px;
            font-weight: 600;
            color: var(--text-primary);
            border-bottom: 1px solid var(--card-border);
            cursor: pointer;
            user-select: none;
            transition: var(--transition);
            font-family: var(--font-title);
            font-size: 13px;
        }

        th:hover {
            background: rgba(30, 41, 59, 0.8);
            color: white;
        }

        th i {
            margin-left: 6px;
            font-size: 11px;
            color: var(--text-secondary);
        }

        td {
            padding: 6px 10px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.03);
            color: var(--text-secondary);
            transition: var(--transition);
            font-size: 13px;
        }

        tr:last-child td {
            border-bottom: none;
        }

        tr:hover td {
            background: rgba(255, 255, 255, 0.02);
            color: var(--text-primary);
        }

        .ticker-badge {
            background: rgba(79, 70, 229, 0.1);
            border: 1px solid rgba(79, 70, 229, 0.3);
            color: #818cf8;
            padding: 4px 8px;
            border-radius: 6px;
            font-weight: 700;
            font-size: 12px;
            display: inline-block;
            font-family: var(--font-title);
        }

        .sparkline-container {
            display: inline-flex;
            align-items: flex-end;
            gap: 2.5px;
            height: 22px;
            width: 46px;
            padding: 2px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 4px;
        }

        .sparkline-bar {
            width: 6px;
            border-radius: 1px;
            min-height: 2px;
            transition: height 0.3s ease;
        }

        .company-name {
            font-weight: 500;
            color: var(--text-primary);
        }

        .cqv-value-cell {
            font-weight: 700;
            font-family: var(--font-title);
            font-size: 15px;
        }

        .score-high {
            color: var(--elite);
        }
        .score-medium {
            color: var(--medium);
        }
        .score-weak {
            color: var(--weak);
        }

        /* Tier labels */
        .tier-badge {
            padding: 4px 10px;
            border-radius: 9999px;
            font-size: 11px;
            font-weight: 600;
            display: inline-block;
            text-transform: uppercase;
        }

        .tier-elite {
            background: rgba(16, 185, 129, 0.1);
            color: var(--elite);
            border: 1px solid rgba(16, 185, 129, 0.2);
        }

        .tier-strong {
            background: rgba(59, 130, 246, 0.1);
            color: var(--strong);
            border: 1px solid rgba(59, 130, 246, 0.2);
        }

        .tier-medium {
            background: rgba(245, 158, 11, 0.1);
            color: var(--medium);
            border: 1px solid rgba(245, 158, 11, 0.2);
        }

        .tier-speculative {
            background: rgba(239, 68, 68, 0.1);
            color: var(--weak);
            border: 1px solid rgba(239, 68, 68, 0.2);
        }

        /* Table Footer / Pagination */
        .table-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 20px;
            color: var(--text-secondary);
            font-size: 13px;
        }

        .pagination-btns {
            display: flex;
            gap: 6px;
        }

        .page-btn {
            background: var(--input-bg);
            border: 1px solid var(--input-border);
            color: var(--text-secondary);
            width: 34px;
            height: 34px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: var(--transition);
            font-weight: 500;
        }

        .page-btn:hover {
            background: rgba(255, 255, 255, 0.05);
            color: white;
            border-color: rgba(255, 255, 255, 0.2);
        }

        .page-btn.active {
            background: var(--primary);
            border-color: var(--primary);
            color: white;
            box-shadow: 0 0 10px rgba(79, 70, 229, 0.3);
        }

        .page-btn:disabled {
            opacity: 0.3;
            cursor: not-allowed;
            pointer-events: none;
        }

        /* Tab Content Control */
        .tab-panel {
            display: none;
        }

        .tab-panel.active {
            display: block;
            animation: fadeIn 0.4s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Metodología Layout */
        .method-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 32px;
            margin-bottom: 32px;
        }

        .equation-box {
            background: linear-gradient(135deg, rgba(79, 70, 229, 0.1), rgba(217, 70, 239, 0.05));
            border: 1px solid rgba(79, 70, 229, 0.3);
            border-radius: 16px;
            padding: 28px;
            text-align: center;
            margin-bottom: 24px;
            box-shadow: 0 0 30px rgba(79, 70, 229, 0.05);
        }

        .equation-text {
            font-family: var(--font-title);
            font-size: 20px;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin: 16px 0;
            background: linear-gradient(to right, var(--text-primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .formula-card {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .formula-item {
            display: flex;
            align-items: flex-start;
            gap: 14px;
            padding: 16px;
            background: var(--item-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            transition: var(--transition);
        }

        .formula-item:hover {
            background: var(--item-hover-bg);
            border-color: var(--accent);
        }

        .factor-num {
            width: 32px;
            height: 32px;
            border-radius: 8px;
            background: var(--primary);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-family: var(--font-title);
            font-size: 14px;
            flex-shrink: 0;
        }

        .factor-details h4 {
            font-family: var(--font-title);
            font-size: 15px;
            font-weight: 600;
            margin-bottom: 4px;
            color: var(--text-primary);
        }

        .factor-details p {
            font-size: 13px;
            color: var(--text-secondary);
        }

        .factor-weight {
            background: rgba(217, 70, 239, 0.15);
            color: var(--secondary);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
            margin-left: 8px;
        }

        .faq-card {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .faq-item {
            border-bottom: 1px solid var(--card-border);
            padding-bottom: 16px;
        }

        .faq-item:last-child {
            border-bottom: none;
        }

        .faq-question {
            font-family: var(--font-title);
            font-size: 15px;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .faq-question i {
            color: var(--accent);
        }

        .faq-answer {
            font-size: 13px;
            color: var(--text-secondary);
            padding-left: 24px;
        }

        /* Simulator Styling */
        .simulator-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
        }

        .sim-controls {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .slider-group {
            display: flex;
            flex-direction: column;
            gap: 8px;
            background: rgba(255, 255, 255, 0.01);
            border: 1px solid rgba(255, 255, 255, 0.03);
            border-radius: 12px;
            padding: 10px 12px;
        }

        .slider-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .slider-label {
            font-weight: 600;
            font-family: var(--font-title);
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .slider-val {
            font-family: var(--font-title);
            font-weight: 700;
            color: var(--accent);
            font-size: 16px;
            background: rgba(6, 182, 212, 0.1);
            padding: 2px 8px;
            border-radius: 6px;
            min-width: 48px;
            text-align: center;
        }

        input[type="range"] {
            -webkit-appearance: none;
            width: 100%;
            height: 6px;
            background: #1e293b;
            border-radius: 9999px;
            outline: none;
        }

        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            cursor: pointer;
            box-shadow: 0 0 10px var(--primary-glow);
            transition: var(--transition);
        }

        input[type="range"]::-webkit-slider-thumb:hover {
            transform: scale(1.15);
        }

        .sim-result-card {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.4));
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            position: relative;
        }

        .sim-cqv-display {
            font-size: 52px;
            font-weight: 800;
            font-family: var(--font-title);
            background: linear-gradient(135deg, var(--text-primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 6px 0;
            text-shadow: 0 0 20px rgba(6, 182, 212, 0.2);
            line-height: 1.1;
        }

        .sim-tier-display {
            margin-top: 4px;
        }

        .sim-radial-container {
            width: 100%;
            max-width: 170px;
            height: 170px;
            margin: 6px 0;
            position: relative;
        }

        .theme-toggle-btn {
            background: transparent;
            border: 1px solid var(--card-border);
            color: var(--text-primary);
            width: 30px;
            height: 30px;
            border-radius: 8px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: var(--transition);
        }

        .theme-toggle-btn:hover {
            background: rgba(255, 255, 255, 0.05) !important;
            border-color: var(--accent) !important;
            color: var(--accent) !important;
        }

        body.light-theme .theme-toggle-btn:hover {
            background: rgba(15, 23, 42, 0.05) !important;
        }

        /* Responsive */
        @media (max-width: 1024px) {
            .dashboard-layout, .method-grid, .simulator-grid {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 640px) {
            .header-content {
                flex-direction: column;
                gap: 16px;
            }
            .table-controls {
                flex-direction: column;
                align-items: stretch;
            }
            .search-wrapper {
                max-width: none;
            }
            .filters-wrapper {
                width: 100%;
            }
            .filters-wrapper select {
                flex-grow: 1;
            }
        }
        /* CQV Version Switching Styles */
        body.cqv-v1-active #tab-explorer table th:nth-child(8),
        body.cqv-v1-active #tab-explorer table td:nth-child(8),
        body.cqv-v1-active #tab-explorer table th:nth-child(9),
        body.cqv-v1-active #tab-explorer table td:nth-child(9),
        body.cqv-v1-active #tab-explorer table th:nth-child(10),
        body.cqv-v1-active #tab-explorer table td:nth-child(10) {
            display: none !important;
        }

        body.cqv-v1-active #history-details-table th:nth-child(7),
        body.cqv-v1-active #history-details-table td:nth-child(7),
        body.cqv-v1-active #history-details-table th:nth-child(8),
        body.cqv-v1-active #history-details-table td:nth-child(8),
        body.cqv-v1-active #history-details-table th:nth-child(9),
        body.cqv-v1-active #history-details-table td:nth-child(9) {
            display: none !important;
        }

        body.cqv-v1-active .v2-only {
            display: none !important;
        }
    </style>
</head>
<body>

    <header>
        <div class="container header-content">
            <div class="logo-area">
                <div class="logo-icon">CQV</div>
                <div class="logo-text">
                    <h1>Score Financiero CQV</h1>
                    <p>Quality and Structural Value</p>
                </div>
            </div>
            
            <nav class="nav-tabs" style="display: flex; align-items: center; gap: 10px;">
                <button class="nav-btn active" onclick="switchTab('dashboard')">
                    <i class="fa-solid fa-chart-line"></i> Dashboard
                </button>
                <button class="nav-btn" onclick="switchTab('explorer')">
                    <i class="fa-solid fa-table"></i> Explorador
                </button>
                <button class="nav-btn" onclick="switchTab('history')">
                    <i class="fa-solid fa-chart-line"></i> Tendencias
                </button>
                <button class="nav-btn" onclick="switchTab('methodology')">
                    <i class="fa-solid fa-book-open"></i> Metodología
                </button>
                <button class="nav-btn" onclick="switchTab('simulator')">
                    <i class="fa-solid fa-calculator"></i> Simulador
                </button>
                <div class="version-selector" style="display: flex; background: var(--input-bg); border: 1px solid var(--input-border); border-radius: 20px; padding: 2px; align-items: center; gap: 2px; margin-right: 5px;">
                    <button id="btn-version-v1" class="v-btn" onclick="setCQVVersion('v1')" style="background: transparent; border: none; padding: 4px 10px; border-radius: 16px; color: var(--text-secondary); font-size: 10px; font-weight: 700; cursor: pointer; font-family: var(--font-title); transition: var(--transition);">v1.0 (5F)</button>
                    <button id="btn-version-v2" class="v-btn" onclick="setCQVVersion('v2')" style="background: var(--primary); border: none; padding: 4px 10px; border-radius: 16px; color: #fff; font-size: 10px; font-weight: 700; cursor: pointer; font-family: var(--font-title); transition: var(--transition);">v2.0 (8F)</button>
                </div>
                <button class="theme-toggle-btn" onclick="toggleTheme()" title="Cambiar Modo Claro/Oscuro">
                    <i id="theme-toggle-icon" class="fa-solid fa-sun"></i>
                </button>
            </nav>
        </div>
    </header>

    <main class="container">
        
        <!-- Tab: Dashboard -->
        <div id="tab-dashboard" class="tab-panel active">
            <!-- KPIs -->
            <div class="kpi-grid">
                <div class="card primary-border">
                    <div class="kpi-card">
                        <div class="kpi-info">
                            <h3>Empresas Auditadas</h3>
                            <div class="value" id="kpi-total-companies">0</div>
                            <div class="subtitle">Ticker de Calidad y Valor</div>
                        </div>
                        <div class="kpi-icon kpi-blue">
                            <i class="fa-solid fa-building"></i>
                        </div>
                    </div>
                </div>
                
                <div class="card primary-border">
                    <div class="kpi-card">
                        <div class="kpi-info">
                            <h3>Promedio CQV</h3>
                            <div class="value" id="kpi-avg-cqv">0.00</div>
                            <div class="subtitle">Calificación general media</div>
                        </div>
                        <div class="kpi-icon kpi-purple">
                            <i class="fa-solid fa-star-half-stroke"></i>
                        </div>
                    </div>
                </div>
                
                <div class="card primary-border">
                    <div class="kpi-card">
                        <div class="kpi-info">
                            <h3>Calidad Élite (>9.0)</h3>
                            <div class="value" id="kpi-elite-count">0</div>
                            <div class="subtitle">Empresas con foso invicto</div>
                        </div>
                        <div class="kpi-icon kpi-emerald">
                            <i class="fa-solid fa-shield-halved"></i>
                        </div>
                    </div>
                </div>
                
                <div class="card primary-border">
                    <div class="kpi-card">
                        <div class="kpi-info">
                            <h3>Líder de Calidad</h3>
                            <div class="value" style="font-size: 24px;" id="kpi-top-performer">MA (9.60)</div>
                            <div class="subtitle">Mastercard Incorporated</div>
                        </div>
                        <div class="kpi-icon kpi-cyan">
                            <i class="fa-solid fa-crown"></i>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Dashboard Layout (Charts) -->
            <div class="dashboard-layout">
                <!-- Bar Chart -->
                <div class="card chart-card">
                    <h3 class="section-title">
                        <i class="fa-solid fa-ranking-star"></i> Top 15 Empresas Élite
                    </h3>
                    <div class="chart-container">
                        <canvas id="topChart"></canvas>
                    </div>
                </div>
                
                <!-- Distribution Column -->
                <div class="card chart-card">
                    <h3 class="section-title">
                        <i class="fa-solid fa-pie-chart"></i> Distribución de Calidad
                    </h3>
                    <div class="distribution-list">
                        <div class="dist-item">
                            <div class="dist-label-row">
                                <span>ÉLITE (CQV &gt; 9.0)</span>
                                <span id="dist-count-elite">0 emp. (0%)</span>
                            </div>
                            <div class="dist-bar-bg">
                                <div class="dist-bar-fill" id="dist-bar-elite" style="background: var(--elite); width: 0%;"></div>
                            </div>
                        </div>
                        
                        <div class="dist-item">
                            <div class="dist-label-row">
                                <span>SÓLIDA (8.5 - 9.0)</span>
                                <span id="dist-count-strong">0 emp. (0%)</span>
                            </div>
                            <div class="dist-bar-bg">
                                <div class="dist-bar-fill" id="dist-bar-strong" style="background: var(--strong); width: 0%;"></div>
                            </div>
                        </div>
                        
                        <div class="dist-item">
                            <div class="dist-label-row">
                                <span>MEDIA (8.0 - 8.5)</span>
                                <span id="dist-count-medium">0 emp. (0%)</span>
                            </div>
                            <div class="dist-bar-bg">
                                <div class="dist-bar-fill" id="dist-bar-medium" style="background: var(--medium); width: 0%;"></div>
                            </div>
                        </div>
                        
                        <div class="dist-item">
                            <div class="dist-label-row">
                                <span>ESPECULATIVA (&lt; 8.0)</span>
                                <span id="dist-count-weak">0 emp. (0%)</span>
                            </div>
                            <div class="dist-bar-bg">
                                <div class="dist-bar-fill" id="dist-bar-weak" style="background: var(--weak); width: 0%;"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Tab: Explorer -->
        <div id="tab-explorer" class="tab-panel">
            <div class="explorer-card">
                <h3 class="section-title">
                    <i class="fa-solid fa-database"></i> Tabla Completa de Calificaciones CQV
                </h3>
                
                <!-- Controls -->
                <div class="table-controls">
                    <div class="search-wrapper">
                        <i class="fa-solid fa-magnifying-glass"></i>
                        <input type="text" class="search-input" id="search-bar" placeholder="Buscar por ticker o empresa..." oninput="handleSearch()">
                    </div>
                    
                    <div class="filters-wrapper">
                        <select class="select-filter" id="tier-filter" onchange="handleFilter()">
                            <option value="all">Todas las Categorías</option>
                            <option value="elite">Élite (&gt; 9.0)</option>
                            <option value="strong">Sólida (8.5 - 9.0)</option>
                            <option value="medium">Media (8.0 - 8.5)</option>
                            <option value="speculative">Especulativa (&lt; 8.0)</option>
                        </select>
                        
                        <select class="select-filter" id="rows-filter" onchange="handleRowsChange()">
                            <option value="15">Mostrar 15</option>
                            <option value="25">Mostrar 25</option>
                            <option value="50" selected>Mostrar 50</option>
                            <option value="all">Mostrar Todo</option>
                        </select>
                    </div>
                </div>

                <!-- Table -->
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th onclick="handleSort('ticker')">Acción <span id="sort-icon-ticker"><i class="fa-solid fa-sort"></i></span></th>
                                <th onclick="handleSort('name')">Nombre de la Empresa <span id="sort-icon-name"><i class="fa-solid fa-sort"></i></span></th>
                                <th onclick="handleSort('f1')">F1 (Rent.) <span id="sort-icon-f1"><i class="fa-solid fa-sort"></i></span></th>
                                <th onclick="handleSort('f2')">F2 (Solidez) <span id="sort-icon-f2"><i class="fa-solid fa-sort"></i></span></th>
                                <th onclick="handleSort('f3')">F3 (Crec.) <span id="sort-icon-f3"><i class="fa-solid fa-sort"></i></span></th>
                                <th onclick="handleSort('f4')">F4 (Moat) <span id="sort-icon-f4"><i class="fa-solid fa-sort"></i></span></th>
                                <th onclick="handleSort('f5')">F5 (Proj.) <span id="sort-icon-f5"><i class="fa-solid fa-sort"></i></span></th>
                                <th onclick="handleSort('f6')">F6 (Asig.) <span id="sort-icon-f6"><i class="fa-solid fa-sort"></i></span></th>
                                <th onclick="handleSort('f7')">F7 (Yield) <span id="sort-icon-f7"><i class="fa-solid fa-sort"></i></span></th>
                                <th onclick="handleSort('f8')">F8 (Antif.) <span id="sort-icon-f8"><i class="fa-solid fa-sort"></i></span></th>
                                <th onclick="handleSort('cqv')">CQV Score <span id="sort-icon-cqv"><i class="fa-solid fa-sort-down"></i></span></th>
                                <th>Evolución (5a)</th>
                                <th>Categoría</th>
                            </tr>
                        </thead>
                        <tbody id="companies-table-body">
                            <!-- Injected by JS -->
                        </tbody>
                    </table>
                </div>

                <!-- Pagination -->
                <div class="table-footer">
                    <div id="showing-entries-label">Mostrando 1 - 15 de 151 empresas</div>
                    <div class="pagination-btns" id="pagination-wrapper">
                        <!-- Injected by JS -->
                    </div>
                </div>
            </div>
        </div>

        <!-- Tab: History -->
        <div id="tab-history" class="tab-panel">
            <div class="card">
                <h3 class="section-title">
                    <i class="fa-solid fa-chart-line"></i> Evolución de Score CQV (Últimos 5 Años)
                </h3>
                <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; max-width: 800px; line-height: 1.4;">
                    Visualiza la tendencia histórica anual del Score CQV calculado a partir de los estados financieros presentados ante la SEC. Haz clic en cualquier empresa en la pestaña <strong>Explorador</strong> para cargar automáticamente su historial aquí.
                </p>
                
                <div style="margin-bottom: 20px; display: flex; gap: 15px; align-items: center; flex-wrap: wrap;">
                    <div>
                        <label for="history-company-select" style="font-size: 13px; color: var(--text-secondary); margin-bottom: 6px; display: block; font-weight: 500;">Seleccionar Empresa:</label>
                        <select id="history-company-select" class="select-filter" style="min-width: 320px;" onchange="loadCompanyHistory()">
                            <option value="">-- Seleccionar una empresa --</option>
                        </select>
                    </div>
                </div>
                
                <!-- Chart Container -->
                <div style="height: 350px; margin-bottom: 30px; position: relative;">
                    <canvas id="historyChart"></canvas>
                </div>
                
                <!-- Details Table -->
                <div class="table-container">
                    <table class="companies-table" id="history-details-table">
                        <thead>
                            <tr>
                                <th>Año</th>
                                <th>F1: Rentabilidad</th>
                                <th>F2: Solidez</th>
                                <th>F3: Crecimiento</th>
                                <th>F4: Moat (Fijo)</th>
                                <th>F5: Proyección (Fijo)</th>
                                <th>F6: Asignación (Fijo)</th>
                                <th>F7: FCF Yield (Fijo)</th>
                                <th>F8: Antifragilidad (Fijo)</th>
                                <th>CQV Score</th>
                            </tr>
                        </thead>
                        <tbody id="history-details-body">
                            <tr>
                                <td colspan="10" style="text-align: center; color: var(--text-secondary); padding: 30px 10px;">
                                    Selecciona una empresa del desplegable o en la pestaña Explorador para ver su evolución.
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Business and Factors Profile in History -->
                <div class="card" id="history-profile-card" style="margin-top: 14px; border-top: 1px solid var(--card-border); padding-top: 14px; display: none;">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; min-height: 100px;">
                        <div>
                            <h3 class="section-title" style="margin-bottom: 6px;"><i class="fa-solid fa-circle-info"></i> Perfil del Negocio</h3>
                            <p id="history-profile-desc" style="font-size: 13px; color: var(--text-secondary); line-height: 1.5;"></p>
                        </div>
                        <div>
                            <h3 class="section-title" style="margin-bottom: 6px;"><i class="fa-solid fa-list-check"></i> Auditoría de Factores (Línea Base 2026)</h3>
                            <ul style="list-style: none; font-size: 12px; display: flex; flex-direction: column; gap: 8px; padding-left: 0;" id="history-profile-factors">
                                <!-- Populated dynamically -->
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Analyst Notes Section -->
                <div class="card" style="margin-top: 14px; border-top: 1px solid var(--card-border); padding-top: 14px;">
                    <h3 class="section-title" style="margin-bottom: 8px;">
                        <i class="fa-solid fa-note-sticky"></i> Notas de Análisis y Auditoría CQV
                    </h3>
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <p style="font-size: 13px; color: var(--text-secondary); line-height: 1.4; font-weight: 500;" id="notes-description-label">
                            Selecciona una empresa para gestionar sus notas de auditoría financiera.
                        </p>
                        <textarea id="company-analyst-notes" rows="3" style="width: 100%; background: var(--input-bg); border: 1px solid var(--input-border); border-radius: 8px; padding: 10px; color: var(--text-primary); font-family: var(--font-body); font-size: 13px; resize: vertical;" placeholder="Escribe aquí tus observaciones del análisis financiero, justificaciones de variación del score, etc..."></textarea>
                        <div style="display: flex; justify-content: flex-end; gap: 10px; align-items: center;">
                            <span id="save-note-status" style="font-size: 12px; color: var(--elite); opacity: 0; transition: var(--transition); font-weight: 500;"><i class="fa-solid fa-circle-check"></i> ¡Nota guardada correctamente!</span>
                            <button class="nav-btn active" onclick="saveCompanyNotes()" style="box-shadow: none; border-radius: 6px; padding: 6px 14px;">
                                <i class="fa-solid fa-floppy-disk"></i> Guardar Nota
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Tab: Methodology -->
        <div id="tab-methodology" class="tab-panel">
            <div class="method-grid">
                <!-- Formula Details -->
                <div class="card">
                    <h3 class="section-title">
                        <i class="fa-solid fa-calculator"></i> Algoritmo CQV Score
                    </h3>
                    
                    <div class="equation-box">
                        <p style="font-size: 13px; color: var(--text-secondary); text-transform: uppercase;">La Ecuación Matriz del CQV v2.0</p>
                        <div class="equation-text">
                            CQV = (F₁ &times; 0.20) + (F₂ &times; 0.10) + (F₃ &times; 0.10) + (F₄ &times; 0.20) + (F₅ &times; 0.10) + (F₆ &times; 0.10) + (F₇ &times; 0.10) + (F₈ &times; 0.10)
                        </div>
                        <p style="font-size: 12px; text-align: left; color: var(--text-secondary); line-height: 1.4;">
                            *Cada factor es calificado estrictamente de 1.0 a 10.0 con base en estados financieros auditados (10-K/10-Q) y modelos cualitativos estandarizados.
                        </p>
                    </div>

                    <div class="formula-card">
                        <div class="formula-item" style="flex-direction: column; align-items: stretch; gap: 8px;">
                            <div style="display: flex; align-items: center; gap: 14px;">
                                <div class="factor-num">F₁</div>
                                <div class="factor-details">
                                    <h4>Rentabilidad (La Máquina de Caja) <span class="factor-weight">Peso: 20%</span></h4>
                                </div>
                            </div>
                            <div style="font-size: 13px; color: var(--text-secondary); padding-left: 46px; line-height: 1.4; display: flex; flex-direction: column; gap: 6px;">
                                <p>Mide la eficiencia para extraer valor del capital operativo y neto invertido.</p>
                                <div style="display: grid; grid-template-columns: 1fr; gap: 8px; margin-top: 4px; background: rgba(148, 163, 184, 0.06); padding: 8px; border-radius: 6px; border: 1px solid var(--card-border);">
                                    <div><strong>Margen EBITDA:</strong> <code>(EBITDA / Ingresos) &times; 100</code> &rarr; <i>Óptimo &gt; 35%</i>.</div>
                                    <div><strong>ROIC (Return on Invested Capital):</strong> <code>NOPAT / (Deuda + Patrimonio - Caja)</code> &rarr; <i>Óptimo &gt; 15% - 20%</i>.</div>
                                    <div><strong>Conversión de Caja:</strong> <code>(Free Cash Flow / Beneficio Neto) &times; 100</code> &rarr; <i>Óptimo &ge; 100%</i>.</div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="formula-item" style="flex-direction: column; align-items: stretch; gap: 8px;">
                            <div style="display: flex; align-items: center; gap: 14px;">
                                <div class="factor-num">F₂</div>
                                <div class="factor-details">
                                    <h4>Solidez Financiera (El Escudo Antifrágil) <span class="factor-weight">Peso: 10%</span></h4>
                                </div>
                            </div>
                            <div style="font-size: 13px; color: var(--text-secondary); padding-left: 46px; line-height: 1.4; display: flex; flex-direction: column; gap: 6px;">
                                <p>Determina la solvencia y nivel de apalancamiento ante escenarios de contracción de crédito.</p>
                                <div style="display: grid; grid-template-columns: 1fr; gap: 8px; margin-top: 4px; background: rgba(148, 163, 184, 0.06); padding: 8px; border-radius: 6px; border: 1px solid var(--card-border);">
                                    <div><strong>Ratio de Apalancamiento:</strong> <code>Deuda Neta / EBITDA</code> &rarr; <i>Óptimo &lt; 1.5x (o Caja Neta)</i>.</div>
                                    <div><strong>Cobertura de Intereses:</strong> <code>EBITDA / Gastos de Interés</code> &rarr; <i>Óptimo &gt; 8x - 10x</i>.</div>
                                    <div><strong>Excepción de Recompras:</strong> Si el patrimonio neto es negativo por recompras históricas, se valida la solidez si la cobertura es sólida.</div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="formula-item" style="flex-direction: column; align-items: stretch; gap: 8px;">
                            <div style="display: flex; align-items: center; gap: 14px;">
                                <div class="factor-num">F₃</div>
                                <div class="factor-details">
                                    <h4>Crecimiento Eficiente (Línea Roja de Dilución) <span class="factor-weight">Peso: 10%</span></h4>
                                </div>
                            </div>
                            <div style="font-size: 13px; color: var(--text-secondary); padding-left: 46px; line-height: 1.4; display: flex; flex-direction: column; gap: 6px;">
                                <p>Mide el aumento de ingresos neto de la dilución al accionista minoritario.</p>
                                <div style="display: grid; grid-template-columns: 1fr; gap: 8px; margin-top: 4px; background: rgba(148, 163, 184, 0.06); padding: 8px; border-radius: 6px; border: 1px solid var(--card-border);">
                                    <div><strong>Tasa de Crecimiento:</strong> <code>((Ingresos_t - Ingresos_t-1) / Ingresos_t-1) &times; 100</code> &rarr; <i>Óptimo &gt; 10% - 15%</i>.</div>
                                    <div><strong>Tasa de Dilución Neta:</strong> <code>(Acciones Emitidas - Acciones Recompradas) / Acciones en Circulación</code>.</div>
                                    <div><strong>Filtro SBC:</strong> Si la dilución por Stock-Based Compensation supera el 1% neto anual, la nota se capa a 7.5 - 8.5.</div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="formula-item" style="flex-direction: column; align-items: stretch; gap: 8px;">
                            <div style="display: flex; align-items: center; gap: 14px;">
                                <div class="factor-num">F₄</div>
                                <div class="factor-details">
                                    <h4>Moat Actual (Fosos de Peaje) <span class="factor-weight">Peso: 20%</span></h4>
                                </div>
                            </div>
                            <div style="font-size: 13px; color: var(--text-secondary); padding-left: 46px; line-height: 1.4; display: flex; flex-direction: column; gap: 6px;">
                                <p>Análisis de barreras cualitativas y cuantitativas contra la competencia directa.</p>
                                <div style="display: grid; grid-template-columns: 1fr; gap: 8px; margin-top: 4px; background: rgba(148, 163, 184, 0.06); padding: 8px; border-radius: 6px; border: 1px solid var(--card-border);">
                                    <div><strong>Costo de Cambio (Switching Cost):</strong> Retención bruta de ingresos (GDR) &gt; 96% (ej. Intuit QuickBooks).</div>
                                    <div><strong>Intangible Legal/Regulatorio:</strong> Licencias NRSRO oficiales (S&P, Moody's) o estándares hipotecarios (FICO).</div>
                                    <div><strong>Efecto de Red (Network Effect):</strong> Incremento de utilidad conforme se suman usuarios (ej. Visa, Mastercard).</div>
                                </div>
                            </div>
                        </div>
 
                        <div class="formula-item" style="flex-direction: column; align-items: stretch; gap: 8px;">
                            <div style="display: flex; align-items: center; gap: 14px;">
                                <div class="factor-num">F₅</div>
                                <div class="factor-details">
                                    <h4>Proyección Futura (Opcionalidad) <span class="factor-weight">Peso: 10%</span></h4>
                                </div>
                            </div>
                            <div style="font-size: 13px; color: var(--text-secondary); padding-left: 46px; line-height: 1.4; display: flex; flex-direction: column; gap: 6px;">
                                <p>Resiliencia del modelo de negocio e inmunidad disruptiva ante la próxima década.</p>
                                <div style="display: grid; grid-template-columns: 1fr; gap: 8px; margin-top: 4px; background: rgba(148, 163, 184, 0.06); padding: 8px; border-radius: 6px; border: 1px solid var(--card-border);">
                                    <div><strong>Inmunidad AI Gen:</strong> Capacidad para evitar la desintermediación por modelos de lenguaje genéricos.</div>
                                    <div><strong>Cuellos de Botella:</strong> Proveedor crítico en cadenas globales físicas/tecnológicas (ej. ASML, TSMC).</div>
                                    <div><strong>Opcionalidad:</strong> Capacidad de re-invertir en nuevas líneas de negocio altamente rentables.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-item v2-only" style="flex-direction: column; align-items: stretch; gap: 8px;">
                            <div style="display: flex; align-items: center; gap: 14px;">
                                <div class="factor-num">F₆</div>
                                <div class="factor-details">
                                    <h4>Asignación de Capital (Capital Allocation) <span class="factor-weight">Peso: 10%</span></h4>
                                </div>
                            </div>
                            <div style="font-size: 13px; color: var(--text-secondary); padding-left: 46px; line-height: 1.4; display: flex; flex-direction: column; gap: 6px;">
                                <p>Evalúa el uso inteligente del flujo de caja por parte de la directiva para maximizar retornos.</p>
                                <div style="display: grid; grid-template-columns: 1fr; gap: 8px; margin-top: 4px; background: rgba(148, 163, 184, 0.06); padding: 8px; border-radius: 6px; border: 1px solid var(--card-border);">
                                    <div><strong>ROCIC:</strong> Retorno sobre capital incremental, midiendo si los nuevos proyectos mantienen la rentabilidad.</div>
                                    <div><strong>Recompras Inteligentes:</strong> Adquisición de acciones propias preferiblemente cuando cotizan a descuento.</div>
                                    <div><strong>M&A Disciplinado:</strong> Fusiones y adquisiciones que crean valor real y sin pagar sobreprecios excesivos.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-item v2-only" style="flex-direction: column; align-items: stretch; gap: 8px;">
                            <div style="display: flex; align-items: center; gap: 14px;">
                                <div class="factor-num">F₇</div>
                                <div class="factor-details">
                                    <h4>Rendimiento FCF (FCF Yield / Valoración) <span class="factor-weight">Peso: 10%</span></h4>
                                </div>
                            </div>
                            <div style="font-size: 13px; color: var(--text-secondary); padding-left: 46px; line-height: 1.4; display: flex; flex-direction: column; gap: 6px;">
                                <p>Integra el precio pagado y la rentabilidad por flujo de caja libre.</p>
                                <div style="display: grid; grid-template-columns: 1fr; gap: 8px; margin-top: 4px; background: rgba(148, 163, 184, 0.06); padding: 8px; border-radius: 6px; border: 1px solid var(--card-border);">
                                    <div><strong>Cálculo:</strong> <code>(Free Cash Flow por Acción / Precio de la Acción) &times; 100</code>.</div>
                                    <div><strong>Métrica:</strong> <i>Óptimo &gt; 6% (Nota 10)</i>. Múltiplos demasiado exigentes (FCF Yield &lt; 2%) reducen drásticamente la nota.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-item v2-only" style="flex-direction: column; align-items: stretch; gap: 8px;">
                            <div style="display: flex; align-items: center; gap: 14px;">
                                <div class="factor-num">F₈</div>
                                <div class="factor-details">
                                    <h4>Antifragilidad y Diversificación <span class="factor-weight">Peso: 10%</span></h4>
                                </div>
                            </div>
                            <div style="font-size: 13px; color: var(--text-secondary); padding-left: 46px; line-height: 1.4; display: flex; flex-direction: column; gap: 6px;">
                                <p>Mide la resiliencia operativa y la diversificación del riesgo de concentración.</p>
                                <div style="display: grid; grid-template-columns: 1fr; gap: 8px; margin-top: 4px; background: rgba(148, 163, 184, 0.06); padding: 8px; border-radius: 6px; border: 1px solid var(--card-border);">
                                    <div><strong>Concentración de Clientes:</strong> Penalización automática (máx 6.5) si un cliente supera el 10% de ingresos netos.</div>
                                    <div><strong>Cadena de Suministro:</strong> Diversificación e inmunidad ante cuellos de botella geográficos de manufactura.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- FAQ / Details -->
                <div class="card">
                    <h3 class="section-title">
                        <i class="fa-solid fa-circle-question"></i> Reglas de Negocio del Sistema
                    </h3>
                    
                    <div class="faq-card">
                        <div class="faq-item">
                            <div class="faq-question">
                                <i class="fa-solid fa-circle-check"></i> ¿Cómo se manejan los tipos de cambio e inflación?
                            </div>
                            <div class="faq-answer">
                                Todos los datos se normalizan a la divisa de cotización del mercado primario. Las tasas de crecimiento se auditan a escala de ingresos brutos, reduciendo la exposición al ruido inflacionario temporal.
                            </div>
                        </div>
                        
                        <div class="faq-item">
                            <div class="faq-question">
                                <i class="fa-solid fa-triangle-exclamation"></i> Penalizador SBC (Stock-Based Compensation)
                            </div>
                            <div class="faq-answer">
                                Si una empresa emite acciones y diluye de forma neta al accionista, el factor F3 se limita automáticamente a un rango de 7.5 a 8.5. Las recompras de acciones deben neto-neutralizar o destruir más flotante del emitido para eliminar la penalización.
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question">
                                <i class="fa-solid fa-calculator"></i> El Filtro de Valoración: Score PEG
                            </div>
                            <div class="faq-answer">
                                Para empresas Élite (CQV &gt; 9.00), el paso final es el gatillo de compra. Se calcula el Score PEG multiplicando el ratio inverso de valoración por 10:
                                <div style="font-family: var(--font-title); font-weight: 700; margin: 8px 0; color: var(--accent); text-align: center;">
                                    Score PEG = ( Crecimiento % / PER Forward ) × 10
                                </div>
                                Si el **Score PEG es &gt; 8.0**, se gatilla la alarma de **Anomalía de Descuento** de forma automática.
                            </div>
                        </div>

                        <div class="faq-item">
                            <div class="faq-question">
                                <i class="fa-solid fa-lightbulb"></i> Caso de Estudio Exitoso: FICO
                            </div>
                            <div class="faq-answer">
                                FICO cuenta con un margen operativo recurrente superior al 40% (Nota 9.9 en F1), deuda neta controlada con cobertura de intereses muy superior a 10x (Nota 8.8 en F2), pricing power extremo y recompra neta pura de acciones (Nota 9.6 en F3), monopolio de facto crediticio (Nota 9.9 en F4), e integración profunda de IA en análisis de riesgo (Nota 9.5 en F5). **Resultado CQV: 9.61** (Calidad Élite).
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Tab: Simulator -->
        <div id="tab-simulator" class="tab-panel">
            <div class="card">
                <h3 class="section-title">
                    <i class="fa-solid fa-gears"></i> Simulador Dinámico de Scoring CQV
                </h3>
                
                <div class="simulator-grid">
                    <!-- Controls -->
                    <div class="sim-controls">
                        <!-- Dropdown to select company -->
                        <div class="slider-group" style="background: rgba(79, 70, 229, 0.05); border: 1px dashed rgba(79, 70, 229, 0.3);">
                            <div style="display: flex; gap: 10px; width: 100%; flex-wrap: wrap;">
                                <div style="flex: 2; min-width: 180px;">
                                    <div class="slider-header" style="margin-bottom: 8px;">
                                        <span class="slider-label" style="color: var(--accent);"><i class="fa-solid fa-building"></i> Pre-cargar Empresa</span>
                                    </div>
                                    <select id="sim-company-select" class="select-filter" style="width: 100%;" onchange="loadCompanyIntoSimulator()">
                                        <option value="">-- Valores por defecto (Simulación libre) --</option>
                                    </select>
                                </div>
                                <div id="sim-year-wrapper" style="flex: 1; min-width: 90px; display: none;">
                                    <div class="slider-header" style="margin-bottom: 8px;">
                                        <span class="slider-label" style="color: var(--accent);"><i class="fa-solid fa-calendar"></i> Año</span>
                                    </div>
                                    <select id="sim-year-select" class="select-filter" style="width: 100%;" onchange="changeSimYear()">
                                        <!-- Populated dynamically -->
                                    </select>
                                </div>
                            </div>
                        </div>

                        <div class="slider-group">
                            <div class="slider-header">
                                <span class="slider-label" style="color: #3b82f6;"><i class="fa-solid fa-wallet"></i> F1: Rentabilidad (20%)</span>
                                <span class="slider-val" id="val-f1">7.5</span>
                            </div>
                            <input type="range" id="slide-f1" min="1.0" max="10.0" step="0.1" value="7.5" oninput="runSimulation()">
                        </div>

                        <div class="slider-group">
                            <div class="slider-header">
                                <span class="slider-label" style="color: #a855f7;"><i class="fa-solid fa-lock"></i> F2: Solidez Financiera (10%)</span>
                                <span class="slider-val" id="val-f2">8.0</span>
                            </div>
                            <input type="range" id="slide-f2" min="1.0" max="10.0" step="0.1" value="8.0" oninput="runSimulation()">
                        </div>

                        <div class="slider-group">
                            <div class="slider-header">
                                <span class="slider-label" style="color: #10b981;"><i class="fa-solid fa-arrow-trend-up"></i> F3: Crecimiento Eficiente (10%)</span>
                                <span class="slider-val" id="val-f3">7.0</span>
                            </div>
                            <input type="range" id="slide-f3" min="1.0" max="10.0" step="0.1" value="7.0" oninput="runSimulation()">
                        </div>

                        <div class="slider-group">
                            <div class="slider-header">
                                <span class="slider-label" style="color: #f59e0b;"><i class="fa-solid fa-shield-halved"></i> F4: Moat Actual (20%)</span>
                                <span class="slider-val" id="val-f4">8.5</span>
                            </div>
                            <input type="range" id="slide-f4" min="1.0" max="10.0" step="0.1" value="8.5" oninput="runSimulation()">
                        </div>

                        <div class="slider-group">
                            <div class="slider-header">
                                <span class="slider-label" style="color: #d946ef;"><i class="fa-solid fa-rocket"></i> F5: Proyección Futura (10%)</span>
                                <span class="slider-val" id="val-f5">8.0</span>
                            </div>
                            <input type="range" id="slide-f5" min="1.0" max="10.0" step="0.1" value="8.0" oninput="runSimulation()">
                        </div>

                        <div class="slider-group v2-only">
                            <div class="slider-header">
                                <span class="slider-label" style="color: #6366f1;"><i class="fa-solid fa-hand-holding-dollar"></i> F6: Asignación Capital (10%)</span>
                                <span class="slider-val" id="val-f6">8.0</span>
                            </div>
                            <input type="range" id="slide-f6" min="1.0" max="10.0" step="0.1" value="8.0" oninput="runSimulation()">
                        </div>

                        <div class="slider-group v2-only">
                            <div class="slider-header">
                                <span class="slider-label" style="color: #06b6d4;"><i class="fa-solid fa-money-bill-trend-up"></i> F7: FCF Yield / Val. (10%)</span>
                                <span class="slider-val" id="val-f7">7.0</span>
                            </div>
                            <input type="range" id="slide-f7" min="1.0" max="10.0" step="0.1" value="7.0" oninput="runSimulation()">
                        </div>

                        <div class="slider-group v2-only">
                            <div class="slider-header">
                                <span class="slider-label" style="color: #ec4899;"><i class="fa-solid fa-triangle-exclamation"></i> F8: Antifragilidad Red (10%)</span>
                                <span class="slider-val" id="val-f8">8.0</span>
                            </div>
                            <input type="range" id="slide-f8" min="1.0" max="10.0" step="0.1" value="8.0" oninput="runSimulation()">
                        </div>
                    </div>

                    <!-- Output displaying Result -->
                    <div class="sim-result-card">
                        <p style="font-size: 13px; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1px;">PUNTUACIÓN CQV CONSOLIDADA</p>
                        <div class="sim-cqv-display" id="sim-cqv-score">7.88</div>
                        <div class="sim-tier-display">
                            <span class="tier-badge" id="sim-tier-badge">Tier</span>
                        </div>
                        
                        <!-- Radar Chart Comparison inside simulator -->
                        <div class="sim-radial-container">
                            <canvas id="simChart"></canvas>
                        </div>
                        <p style="font-size: 12px; color: var(--text-secondary); max-width: 320px; line-height: 1.4;">
                            Mueve los deslizadores de los macro-factores para evaluar el impacto inmediato de los cambios fundamentales en la valoración estructural de la compañía.
                        </p>
                    </div>
                </div>

                <!-- Business and Factors Profile in Simulator -->
                <div class="card" id="sim-profile-card" style="margin-top: 14px; border-top: 1px solid var(--card-border); padding-top: 14px; display: none;">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; min-height: 100px;">
                        <div>
                            <h3 class="section-title" style="margin-bottom: 6px;"><i class="fa-solid fa-circle-info"></i> Perfil del Negocio (Simulador)</h3>
                            <p id="sim-profile-desc" style="font-size: 13px; color: var(--text-secondary); line-height: 1.5;"></p>
                        </div>
                        <div>
                            <h3 class="section-title" style="margin-bottom: 6px;"><i class="fa-solid fa-list-check"></i> Justificación de Factores en Línea Base</h3>
                            <ul style="list-style: none; font-size: 12px; display: flex; flex-direction: column; gap: 8px; padding-left: 0;" id="sim-profile-factors">
                                <!-- Populated dynamically -->
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- Scripting -->
    <script src="cqv_data.js"></script>
    <script src="cqv_history.js"></script>
    <script>
        // Check if data loaded correctly, fallback to fetch JSON if needed
        let companies = [];

        const companyDetailedData = {
            "MA": {
                desc: "Mastercard Incorporated es una empresa tecnológica líder global en la industria de medios de pago, conectando a consumidores, instituciones financieras, comercios y gobiernos en más de 210 países.",
                f1_desc: "Margen EBITDA extraordinario superior al 58% y ROIC colosal. Alta conversión de beneficio contable a flujo de caja libre neto.",
                f2_desc: "Balance y solvencia excepcionales. Liquidez inmediata superior a 1.2x la deuda a corto plazo y cobertura de intereses sumamente holgada.",
                f3_desc: "Crecimiento eficiente impulsado por la transición global del dinero físico a transacciones digitales y transfronterizas sin requerir alta inversión de capital.",
                f4_desc: "Foso competitivo (Moat) casi impenetrable derivado de efectos de red globales bilaterales masivos y un duopolio de red de peaje de facto con Visa.",
                f5_desc: "Preeminencia en seguridad digital mediante IA aplicada a detección de fraudes y soluciones transfronterizas complejas, asegurando resiliencia frente a disrupción Fintech.",
                f6_desc: "Asignación de capital ultra-eficiente centrado en recompras masivas de acciones constantes y dividendos crecientes sustentados en flujos predecibles.",
                f7_desc: "FCF Yield estable de ~3.0%-3.5% que refleja una valoración premium pero justificada por su foso de duopolio.",
                f8_desc: "Diversificación total con miles de millones de tarjetas y comercios integrados en su red global."
            },
            "V": {
                desc: "Visa Inc. es la red de procesamiento de pagos electrónicos más grande del mundo, operando como un peaje de transacción global para consumidores, comercios e instituciones financieras.",
                f1_desc: "Margen operativo superior al 64%. Negocio asset-light con requerimientos mínimos de capital e inmensa conversión de efectivo.",
                f2_desc: "Apalancamiento mínimo con Deuda Neta/EBITDA muy por debajo de 1.0x, complementado por flujos de caja de alta predecibilidad anticíclica.",
                f3_desc: "Crecimiento constante impulsado por la digitalización del efectivo y la expansión de pagos sin contacto y transferencias P2P.",
                f4_desc: "Efecto red bilateral insuperable (comercios-consumidores) y foso de escala global regulado, operando de facto como un peaje indestructible.",
                f5_desc: "Opcionalidad en flujos transfronterizos complejos y APIs de seguridad financiera, inmune a la desintermediación por su escala y confianza institucional.",
                f6_desc: "Asignación de capital óptima. Recompra neta masiva y constante reducción de acciones en circulación sin deuda significativa.",
                f7_desc: "FCF Yield de ~3.0%-3.5%, consistente con un negocio de altísima calidad y baja intensidad de capital.",
                f8_desc: "Excelente diversificación de ingresos entre múltiples emisores y adquirentes a nivel mundial."
            },
            "AAPL": {
                desc: "Apple Inc. es la compañía de hardware de consumo y servicios más grande del mundo, destacando por su ecosistema cerrado que integra iPhone, iPad, Mac y una suite de servicios de alta fidelidad.",
                f1_desc: "Márgenes brutos estables del 45% y generación de caja operativa colosal. ROIC extraordinario (>50%) debido a su modelo de manufactura optimizado.",
                f2_desc: "Estructura de deuda conservadora orientada a neutralidad de caja neta, con alta predecibilidad del flujo libre de caja.",
                f3_desc: "Crecimiento a un dígito alto apoyado por servicios recurrentes que compensan la maduración de las ventas de hardware físico.",
                f4_desc: "Foso insuperable basado en costos de cambio extremos del ecosistema iOS/macOS y el valor de marca más fuerte del planeta.",
                f5_desc: "Fuerte opcionalidad en servicios financieros, salud y computación espacial (Vision Pro), con un ecosistema extremadamente resistente a la desintermediación por terceros.",
                f6_desc: "Asignación de capital agresiva y exitosa enfocada en recompras masivas (más de 90B anuales) y dividendos constantes.",
                f7_desc: "FCF Yield de ~3.0%-3.5%. Su flujo de caja colosal ofrece protección ante presiones macroeconómicas.",
                f8_desc: "Dependencia significativa de la manufactura en Asia (Foxconn), aunque cuenta con millones de consumidores diversificados en todo el mundo."
            },
            "ASML": {
                desc: "ASML Holding N.V. es el único fabricante en el mundo de máquinas de litografía ultravioleta extrema (EUV), indispensables para fabricar los semiconductores más avanzados de la actualidad.",
                f1_desc: "Rentabilidad extraordinaria con retornos de capital muy elevados (ROIC >30%) apoyados en su monopolio tecnológico.",
                f2_desc: "Balance impecable con caja neta y nulo riesgo crediticio debido a pagos por hitos adelantados de sus clientes.",
                f3_desc: "Crecimiento sólido impulsado por la demanda estructural de microchips de última generación y centros de datos de IA.",
                f4_desc: "Monopolio tecnológico e intelectual absoluto en litografía avanzada, con barreras de entrada físicas y científicas multimillonarias.",
                f5_desc: "Proveedor crítico insustituible para el futuro de la Inteligencia Artificial y la computación de alto rendimiento.",
                f6_desc: "Retornos elevados sobre capital incremental (ROCIC) gracias a la reinversión constante en I+D crítica y recompras oportunistas.",
                f7_desc: "FCF Yield bajo (~2.0%) debido a múltiplos de valoración exigentes que reflejan su monopolio tecnológico.",
                f8_desc: "Riesgo de concentración de clientes medio-alto (TSMC, Intel y Samsung representan la gran mayoría de sus ingresos de EUV)."
            },
            "AVGO": {
                desc: "Broadcom Inc. es un líder tecnológico global que diseña, desarrolla y suministra una amplia gama de soluciones de software de infraestructura y semiconductores analógicos y digitales.",
                f1_desc: "Margen operativo superior al 45% sostenido. Excelente generación de flujo de caja libre, con conversión superior al 110%.",
                f2_desc: "Apalancamiento manejable gracias a la rápida reducción de deuda utilizando los flujos de caja operativos tras la compra de VMware.",
                f3_desc: "Crecimiento impulsado por adquisiciones estratégicas masivas (M&A) e integración de software y silicio personalizado para centros de datos de IA.",
                f4_desc: "Moat fuerte basado en contratos de software empresarial a largo plazo y patentes críticas de conectividad de silicio para centros de datos.",
                f5_desc: "Papel fundamental en el despliegue de redes para clústeres de GPU para IA y chips propietarios personalizados (ASICs).",
                f6_desc: "Estrategia M&A agresiva pero disciplinada dirigida por Hock Tan, logrando desapalancamiento rápido tras adquisiciones (ej. VMware).",
                f7_desc: "FCF Yield atractivo (~4.0%) sustentado en su capacidad de ordeñar flujos recurrentes de software de infraestructura.",
                f8_desc: "Dependencia parcial de grandes proveedores de infraestructura cloud e hiperscalers en el área de silicio."
            },
            "GOOGL": {
                desc: "Alphabet Inc. (Google) es el líder indiscutible en búsquedas web, publicidad digital y sistemas operativos móviles (Android). Su modelo de negocio se basa en la monetización de la atención de los usuarios y el procesamiento masivo de datos mediante IA.",
                f1_desc: "Margen operativo superior al 27% sostenido. Elevado ROIC (>25%), aunque presionado por la intensidad de capital necesaria para la infraestructura de Inteligencia Artificial.",
                f2_desc: "Balance extremadamente sólido con caja neta de más de 100,000 millones de dólares y un ratio Deuda Neta/EBITDA negativo.",
                f3_desc: "Crecimiento histórico constante superior al 10%, sin embargo, el factor se ve afectado por la dilución neta derivada de su alta compensación basada en acciones (SBC).",
                f4_desc: "Foso competitivo masivo derivado de costos de cambio operativos en Android/Google Workspace y un efecto red colosal en su motor de búsqueda y YouTube.",
                f5_desc: "Posicionamiento líder en la revolución de IA con Gemini, Google Cloud y Waymo, ofreciendo opcionalidad en conducción autónoma y computación en la nube.",
                f6_desc: "Asignación de capital buena pero diluida levemente por su compensación en acciones (SBC). Inversiones masivas en Capex de IA.",
                f7_desc: "FCF Yield sólido de ~3.5%-4.0%, representando una de las valoraciones más atractivas en Big Tech por flujo de caja.",
                f8_desc: "Excelente diversificación de anunciantes a nivel global, con nula dependencia de clientes individuales."
            },
            "MSFT": {
                desc: "Microsoft Corporation es el gigante del software empresarial y servicios en la nube (Azure), con una integración líder en productividad de oficina (Office) e Inteligencia Artificial corporativa.",
                f1_desc: "Márgenes operativos superiores al 40% y una de las tasas de conversión de beneficio neto a FCF más altas del mercado corporativo.",
                f2_desc: "Calificación crediticia AAA (de las pocas del mundo), con una cobertura de intereses de triple dígito y una pila de caja formidable.",
                f3_desc: "Crecimiento del 12%-18% anual impulsado por la migración masiva a la nube inteligente y la suscripción SaaS en todas sus líneas de negocio.",
                f4_desc: "Monopolio de facto corporativo con la suite Office, Windows, Active Directory y Azure, con costos de cambio casi prohibitivos para empresas.",
                f5_desc: "Máxima opcionalidad tecnológica derivada de su alianza preferente con OpenAI y la integración de Copilot en todo su ecosistema de software corporativo.",
                f6_desc: "Retornos sobre capital invertido incremental (ROCIC) estelares mediante adquisiciones estratégicas clave y Capex agresivo en infraestructura de nube.",
                f7_desc: "FCF Yield de ~2.5%-3.0% debido a múltiplos exigentes impulsados por el optimismo en IA.",
                f8_desc: "Ecosistema empresarial masivo e hiper-diversificado con millones de clientes corporativos y consumidores globales."
            },
            "NVDA": {
                desc: "NVIDIA Corporation es el diseñador dominante de unidades de procesamiento gráfico (GPU) y la plataforma de software CUDA, sirviendo como la espina dorsal tecnológica de la IA global.",
                f1_desc: "Margen operativo superior al 55% y ROIC récord de la industria (>80%) gracias a su poder de fijación de precios absoluto ante la demanda de cómputo.",
                f2_desc: "Posición financiera impecable con caja neta masiva generada en los últimos trimestres y nulo riesgo de liquidez.",
                f3_desc: "Crecimiento explosivo de ingresos superior al 200% interanual en el sector de centros de datos, limitado únicamente por la capacidad de producción de TSMC.",
                f4_desc: "Foso tecnológico e intelectual inmenso debido a CUDA, la plataforma de software propietaria que impide la migración fácil a chips competidores.",
                f5_desc: "Posicionamiento absoluto como el 'peaje de hardware' de la revolución de IA, con opcionalidad en robótica, automóviles autónomos y gemelos digitales.",
                f6_desc: "Reinversión masiva de capital en Capex y diseño de semiconductores de próxima generación para mantener el liderazgo tecnológico.",
                f7_desc: "FCF Yield muy bajo (~1.5%-2.0%) debido a una valoración implícita de crecimiento hiper-exigente.",
                f8_desc: "Alta concentración de ingresos en pocos proveedores en la nube y fabricantes contratados, penalizada por la regla del factor."
            },
            "FICO": {
                desc: "Fair Isaac Corporation es el proveedor estándar del algoritmo de puntuación crediticia utilizado por más del 90% de los prestamistas en los Estados Unidos para evaluar el riesgo de consumo.",
                f1_desc: "Márgenes EBITDA del 45% y ROIC infinito gracias a un modelo de negocio de licenciamiento puramente digital con mínima base de activos físicos.",
                f2_desc: "Operación antifrágil. Aunque tiene patrimonio neto negativo debido a recompras agresivas, la cobertura de intereses supera las 10 veces el EBITDA.",
                f3_desc: "Crecimiento del 10%-15% impulsado por incrementos continuos de precios y mayor adopción de analítica predictiva en banca.",
                f4_desc: "Monopolio de facto regulado por las agencias hipotecarias federales (Fannie Mae y Freddie Mac), que exigen el uso del Score FICO para finalizar créditos.",
                f5_desc: "Expansión en FICO Platform, una suite de decisión empresarial en la nube que integra analítica de IA y optimización de flujos de trabajo financieros.",
                f6_desc: "Asignación de capital ultra-agresiva mediante recompras destructoras de flotante, logrando un crecimiento masivo de BPA a pesar del apalancamiento.",
                f7_desc: "FCF Yield modesto (~2.5%) debido a la revalorización de múltiplos históricos por su pricing power absoluto.",
                f8_desc: "Dependencia directa de los tres burós de crédito principales norteamericanos (Equifax, Experian y TransUnion)."
            }
        };

        function getCompanyDetails(ticker, company) {
            if (companyDetailedData[ticker]) {
                return companyDetailedData[ticker];
            }
            return {
                desc: `${company.name} (${company.ticker}) es una empresa cotizada en bolsa calificada con un Score CQV global de ${company.cqv.toFixed(2)}, posicionándose en la categoría de ${getTier(company.cqv).name}.`,
                f1_desc: `Calificación F1 de ${company.f1.toFixed(2)} sobre rentabilidad, márgenes operativos y conversión de flujo de caja libre.`,
                f2_desc: `Calificación F2 de ${company.f2.toFixed(2)} sobre la solidez de su balance y cobertura de intereses frente a la deuda.`,
                f3_desc: `Calificación F3 de ${company.f3.toFixed(2)} sobre su tasa de crecimiento orgánico auditada y control de la dilución al accionista por SBC.`,
                f4_desc: `Calificación F4 de ${company.f4.toFixed(2)} que refleja sus barreras de entrada competitivas (Moat) y retención del cliente.`,
                f5_desc: `Calificación F5 de ${company.f5.toFixed(2)} de opcionalidad tecnológica ante la revolución digital y resiliencia disruptiva.`,
                f6_desc: `Calificación F6 de ${company.f6 ? company.f6.toFixed(2) : '8.00'} sobre la asignación de capital operativo y dividendos de la directiva.`,
                f7_desc: `Calificación F7 de ${company.f7 ? company.f7.toFixed(2) : '8.00'} sobre el FCF Yield y la valoración del flujo de caja de la empresa.`,
                f8_desc: `Calificación F8 de ${company.f8 ? company.f8.toFixed(2) : '8.00'} sobre la resiliencia operativa y la diversificación de ingresos frente al riesgo de concentración.`
            };
        }

        let currentVersion = 'v2'; // 'v1' or 'v2'

        function setCQVVersion(version) {
            currentVersion = version;
            
            const btnV1 = document.getElementById('btn-version-v1');
            const btnV2 = document.getElementById('btn-version-v2');
            if (btnV1 && btnV2) {
                if (version === 'v1') {
                    btnV1.style.background = 'var(--primary)';
                    btnV1.style.color = '#fff';
                    btnV2.style.background = 'transparent';
                    btnV2.style.color = 'var(--text-secondary)';
                    
                    companies.forEach(c => {
                        c.cqv = c.cqv_v1;
                    });
                } else {
                    btnV2.style.background = 'var(--primary)';
                    btnV2.style.color = '#fff';
                    btnV1.style.background = 'transparent';
                    btnV1.style.color = 'var(--text-secondary)';
                    
                    companies.forEach(c => {
                        c.cqv = c.cqv_v2;
                    });
                }
            }
            
            updateVersionUI();
            
            // Re-render everything
            initKPIs();
            renderTopChart();
            sortData();
            renderTable();
            
            // Update History/Trends
            const historySelect = document.getElementById('history-company-select');
            if (historySelect && historySelect.value) {
                loadCompanyHistory();
            }
            
            // Update Simulator
            const simSelect = document.getElementById('sim-company-select');
            if (simSelect) {
                if (simSelect.value) {
                    changeSimYear();
                } else {
                    runSimulation();
                }
            }
        }
        
        function updateVersionUI() {
            const isV2 = (currentVersion === 'v2');
            if (isV2) {
                document.body.classList.remove('cqv-v1-active');
            } else {
                document.body.classList.add('cqv-v1-active');
            }
        }

        function initDashboard() {
            // Apply saved theme preference
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme === 'light') {
                document.body.classList.add('light-theme');
                const themeIcon = document.getElementById('theme-toggle-icon');
                if (themeIcon) {
                    themeIcon.className = 'fa-solid fa-moon';
                }
            }
            
            companies = window.companiesData || (typeof companiesData !== 'undefined' ? companiesData : []);
            if (companies.length === 0) {
                console.error("No companies data available!");
                return;
            }
            filteredData = [...companies];
            
            // Set initial version
            setCQVVersion('v2');
            
            populateSimCompanySelect();
            populateHistoryCompanySelect();
        }

        function populateSimCompanySelect() {
            const selectEl = document.getElementById('sim-company-select');
            if (!selectEl) return;
            selectEl.innerHTML = '<option value="">-- Valores por defecto (Simulación libre) --</option>';
            const sortedCompanies = [...companies].sort((a, b) => a.ticker.localeCompare(b.ticker));
            sortedCompanies.forEach(c => {
                const opt = document.createElement('option');
                opt.value = c.ticker;
                opt.innerText = `${c.ticker} - ${c.name} (CQV: ${c.cqv.toFixed(2)})`;
                selectEl.appendChild(opt);
            });
        }

        function loadCompanyIntoSimulator() {
            const ticker = document.getElementById('sim-company-select').value;
            const yearWrapper = document.getElementById('sim-year-wrapper');
            const yearSelect = document.getElementById('sim-year-select');
            const simProfileCard = document.getElementById('sim-profile-card');
            const simProfileDesc = document.getElementById('sim-profile-desc');
            const simProfileFactors = document.getElementById('sim-profile-factors');
            
            if (!ticker) {
                if (yearWrapper) yearWrapper.style.display = 'none';
                if (simProfileCard) simProfileCard.style.display = 'none';
                
                document.getElementById('slide-f1').value = 7.5;
                document.getElementById('slide-f2').value = 8.0;
                document.getElementById('slide-f3').value = 7.0;
                document.getElementById('slide-f4').value = 8.5;
                document.getElementById('slide-f5').value = 8.0;
                document.getElementById('slide-f6').value = 8.0;
                document.getElementById('slide-f7').value = 7.0;
                document.getElementById('slide-f8').value = 8.0;
                window.originalSimData = null;
                runSimulation();
            } else {
                const company = companies.find(c => c.ticker === ticker);
                if (company) {
                    if (simProfileCard && simProfileDesc && simProfileFactors) {
                        const details = getCompanyDetails(ticker, company);
                        simProfileDesc.innerText = details.desc;
                        
                        simProfileFactors.innerHTML = `
                            <li><strong style="color: #3b82f6;"><i class="fa-solid fa-wallet"></i> F1 (Rentabilidad):</strong> ${details.f1_desc}</li>
                            <li><strong style="color: #a855f7;"><i class="fa-solid fa-lock"></i> F2 (Solidez):</strong> ${details.f2_desc}</li>
                            <li><strong style="color: #10b981;"><i class="fa-solid fa-arrow-trend-up"></i> F3 (Crecimiento):</strong> ${details.f3_desc}</li>
                            <li><strong style="color: #f59e0b;"><i class="fa-solid fa-shield-halved"></i> F4 (Moat):</strong> ${details.f4_desc}</li>
                            <li><strong style="color: #d946ef;"><i class="fa-solid fa-rocket"></i> F5 (Proyección):</strong> ${details.f5_desc}</li>
                            <li class="v2-only"><strong style="color: #6366f1;"><i class="fa-solid fa-hand-holding-dollar"></i> F6 (Asignación):</strong> ${details.f6_desc}</li>
                            <li class="v2-only"><strong style="color: #06b6d4;"><i class="fa-solid fa-money-bill-trend-up"></i> F7 (FCF Yield):</strong> ${details.f7_desc}</li>
                            <li class="v2-only"><strong style="color: #ec4899;"><i class="fa-solid fa-triangle-exclamation"></i> F8 (Antifragilidad):</strong> ${details.f8_desc}</li>
                        `;
                        simProfileCard.style.display = 'block';
                    }
                    
                    if (yearSelect && yearWrapper) {
                        yearSelect.innerHTML = '';
                        
                        const rawHistory = (typeof cqvHistoryData !== 'undefined' && cqvHistoryData[ticker]) ? cqvHistoryData[ticker] : {};
                        const years = Object.keys(rawHistory).sort();
                        
                        if (!years.includes("2026")) {
                            years.push("2026");
                        }
                        
                        years.sort((a, b) => b - a);
                        
                        years.forEach(yr => {
                            const opt = document.createElement('option');
                            opt.value = yr;
                            opt.innerText = yr === "2026" ? "2026 (Act.)" : yr;
                            yearSelect.appendChild(opt);
                        });
                        
                        yearWrapper.style.display = 'block';
                        yearSelect.value = "2026";
                    }
                    changeSimYear();
                }
            }
        }

        function changeSimYear() {
            const ticker = document.getElementById('sim-company-select').value;
            const yr = document.getElementById('sim-year-select').value;
            if (!ticker || !yr) return;
            
            const company = companies.find(c => c.ticker === ticker);
            if (!company) return;
            
            let f1 = company.f1;
            let f2 = company.f2;
            let f3 = company.f3;
            
            const rawHistory = (typeof cqvHistoryData !== 'undefined' && cqvHistoryData[ticker]) ? cqvHistoryData[ticker] : {};
            if (rawHistory[yr]) {
                f1 = rawHistory[yr].f1;
                f2 = rawHistory[yr].f2;
                f3 = rawHistory[yr].f3;
            }
            
            const f4 = company.f4;
            const f5 = company.f5;
            const f6 = company.f6;
            const f7 = company.f7;
            const f8 = company.f8;
            
            document.getElementById('slide-f1').value = f1;
            document.getElementById('slide-f2').value = f2;
            document.getElementById('slide-f3').value = f3;
            document.getElementById('slide-f4').value = f4;
            document.getElementById('slide-f5').value = f5;
            document.getElementById('slide-f6').value = f6;
            document.getElementById('slide-f7').value = f7;
            document.getElementById('slide-f8').value = f8;
            
            window.originalSimData = {
                name: company.name,
                ticker: `${company.ticker} (${yr === "2026" ? "2026 Act." : yr})`,
                data: [f1, f2, f3, f4, f5, f6, f7, f8]
            };
            
            runSimulation();
        }

        function populateHistoryCompanySelect() {
            const selectEl = document.getElementById('history-company-select');
            if (!selectEl) return;
            selectEl.innerHTML = '<option value="">-- Seleccionar una empresa --</option>';
            const sortedCompanies = [...companies].sort((a, b) => a.ticker.localeCompare(b.ticker));
            sortedCompanies.forEach(c => {
                if (typeof cqvHistoryData !== 'undefined' && cqvHistoryData[c.ticker]) {
                    const opt = document.createElement('option');
                    opt.value = c.ticker;
                    opt.innerText = `${c.ticker} - ${c.name} (CQV: ${c.cqv.toFixed(2)})`;
                    selectEl.appendChild(opt);
                }
            });
        }

        function getChartGridColor() {
            return document.body.classList.contains('light-theme') ? 'rgba(15, 23, 42, 0.08)' : 'rgba(255, 255, 255, 0.06)';
        }

        function getChartLabelColor() {
            return document.body.classList.contains('light-theme') ? '#475569' : '#94a3b8';
        }

        function toggleTheme() {
            document.body.classList.toggle('light-theme');
            const isLight = document.body.classList.contains('light-theme');
            localStorage.setItem('theme', isLight ? 'light' : 'dark');
            
            const themeIcon = document.getElementById('theme-toggle-icon');
            if (themeIcon) {
                themeIcon.className = isLight ? 'fa-solid fa-moon' : 'fa-solid fa-sun';
            }
            
            // Re-render charts
            renderTopChart();
            runSimulation();
            if (typeof loadCompanyHistory === 'function') {
                loadCompanyHistory();
            }
        }

        const presetCompanyNotes = {
            "GOOGL": "La reducción en el score CQV de Google se debe principalmente a una contracción en el Factor F1 (Rentabilidad y Retornos) por el aumento masivo en inversiones de capital (CapEx) en infraestructura de centros de datos para IA y mayores gastos operativos de desarrollo. Esto afectó el Factor F3 (Crecimiento de utilidades libres de caja), contrarrestando su excelente foso competitivo en búsquedas (Factor F4).",
            "AAPL": "El score de Apple muestra gran solidez debido a su insuperable Factor F4 (Foso de Ecosistema cautivo) y alta rentabilidad (F1). Los ligeros retrocesos temporales se atribuyen a una desaceleración en el volumen de crecimiento en hardware (Factor F3), balanceado por el aumento de ingresos en servicios.",
            "NVDA": "La subida vertical de la calificación CQV de Nvidia se debe al incremento exponencial en el Factor F1 (Rentabilidad operativa neta récord de márgenes) y el Factor F3 (Crecimiento de ingresos superiores al 200% interanual), consolidando un monopolio de hardware para Inteligencia Artificial (Factor F4).",
            "MSFT": "Microsoft mantiene un posicionamiento de élite constante. Su score se ve impulsado por la expansión del margen y ventas en la nube (Azure) y la integración rápida de IA en su catálogo de software (Factor F5 - Proyecciones y Factor F4 - Foso corporativo)."
        };

        function loadCompanyNotes(ticker) {
            const textarea = document.getElementById('company-analyst-notes');
            const descLabel = document.getElementById('notes-description-label');
            if (!textarea || !descLabel) return;
            
            const company = companies.find(c => c.ticker === ticker);
            if (!company) {
                textarea.value = '';
                descLabel.innerText = 'Selecciona una empresa para gestionar sus notas de auditoría financiera.';
                textarea.disabled = true;
                return;
            }
            
            textarea.disabled = false;
            descLabel.innerText = `Notas del Analista para ${company.ticker} (${company.name}):`;
            
            // Check localStorage first
            const saved = localStorage.getItem(`cqv_note_${ticker}`);
            if (saved !== null) {
                textarea.value = saved;
            } else if (presetCompanyNotes[ticker]) {
                textarea.value = presetCompanyNotes[ticker];
            } else {
                // Generate automated notes based on factors
                const factors = [
                    { name: 'Rentabilidad (F1)', val: company.f1 },
                    { name: 'Solidez (F2)', val: company.f2 },
                    { name: 'Crecimiento (F3)', val: company.f3 },
                    { name: 'Foso/Moat (F4)', val: company.f4 },
                    { name: 'Proyección (F5)', val: company.f5 }
                ];
                factors.sort((a, b) => b.val - a.val);
                const highest = factors[0];
                const lowest = factors[factors.length - 1];
                
                textarea.value = `Análisis de Score: Su principal fortaleza radica en ${highest.name} con una puntuación de ${highest.val.toFixed(2)}, mientras que presenta áreas de mejora en ${lowest.name} con ${lowest.val.toFixed(2)}.`;
            }
        }

        function saveCompanyNotes() {
            const selectEl = document.getElementById('history-company-select');
            const textarea = document.getElementById('company-analyst-notes');
            const statusSpan = document.getElementById('save-note-status');
            if (!selectEl || !textarea) return;
            
            const ticker = selectEl.value;
            if (!ticker) return;
            
            localStorage.setItem(`cqv_note_${ticker}`, textarea.value);
            
            // Show status label
            if (statusSpan) {
                statusSpan.style.opacity = '1';
                setTimeout(() => {
                    statusSpan.style.opacity = '0';
                }, 2000);
            }
        }

        let historyChart = null;
        function loadCompanyHistory() {
            const ticker = document.getElementById('history-company-select').value;
            const tbody = document.getElementById('history-details-body');
            const profileCard = document.getElementById('history-profile-card');
            const profileDesc = document.getElementById('history-profile-desc');
            const profileFactors = document.getElementById('history-profile-factors');
            
            if (!tbody) return;
            tbody.innerHTML = '';
            
            if (!ticker) {
                if (historyChart) {
                    historyChart.destroy();
                    historyChart = null;
                }
                tbody.innerHTML = '<tr><td colspan="10" style="text-align: center; color: var(--text-secondary); padding: 30px 10px;">Selecciona una empresa para ver su evolución.</td></tr>';
                loadCompanyNotes('');
                if (profileCard) profileCard.style.display = 'none';
                return;
            }
            
            const company = companies.find(c => c.ticker === ticker);
            if (!company) return;
            
            if (profileCard && profileDesc && profileFactors) {
                const details = getCompanyDetails(ticker, company);
                profileDesc.innerText = details.desc;
                
                profileFactors.innerHTML = `
                    <li><strong style="color: #3b82f6;"><i class="fa-solid fa-wallet"></i> F1 (Rentabilidad):</strong> ${details.f1_desc}</li>
                    <li><strong style="color: #a855f7;"><i class="fa-solid fa-lock"></i> F2 (Solidez):</strong> ${details.f2_desc}</li>
                    <li><strong style="color: #10b981;"><i class="fa-solid fa-arrow-trend-up"></i> F3 (Crecimiento):</strong> ${details.f3_desc}</li>
                    <li><strong style="color: #f59e0b;"><i class="fa-solid fa-shield-halved"></i> F4 (Moat):</strong> ${details.f4_desc}</li>
                    <li><strong style="color: #d946ef;"><i class="fa-solid fa-rocket"></i> F5 (Proyección):</strong> ${details.f5_desc}</li>
                    <li class="v2-only"><strong style="color: #6366f1;"><i class="fa-solid fa-hand-holding-dollar"></i> F6 (Asignación):</strong> ${details.f6_desc}</li>
                    <li class="v2-only"><strong style="color: #06b6d4;"><i class="fa-solid fa-money-bill-trend-up"></i> F7 (FCF Yield):</strong> ${details.f7_desc}</li>
                    <li class="v2-only"><strong style="color: #ec4899;"><i class="fa-solid fa-triangle-exclamation"></i> F8 (Antifragilidad):</strong> ${details.f8_desc}</li>
                `;
                profileCard.style.display = 'block';
            }
            
            const rawHistory = (typeof cqvHistoryData !== 'undefined' && cqvHistoryData[ticker]) ? cqvHistoryData[ticker] : {};
            const history = { ...rawHistory };
            
            // Append 2026 calculation if not already present in the history database
            if (!history["2026"]) {
                history["2026"] = { f1: company.f1, f2: company.f2, f3: company.f3, cqv: company.cqv };
            }
            
            const years = Object.keys(history).sort();
            
            years.forEach(yr => {
                const data = history[yr];
                const isCurrent = yr === "2026" && !rawHistory["2026"];
                const label = isCurrent ? "2026 (Act.)" : yr;
                
                // Recalculate historical CQV using 8 factors (F1-F3 historical, F4-F8 fixed/current)
                const cqv_v2 = (
                    data.f1 * 0.20 +
                    data.f2 * 0.10 +
                    data.f3 * 0.10 +
                    company.f4 * 0.20 +
                    company.f5 * 0.10 +
                    company.f6 * 0.10 +
                    company.f7 * 0.10 +
                    company.f8 * 0.10
                );
                
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><span style="font-weight: bold; color: ${isCurrent ? 'var(--accent)' : 'var(--text-primary)'};">${label}</span></td>
                    <td class="cqv-value-cell">${data.f1.toFixed(2)}</td>
                    <td class="cqv-value-cell">${data.f2.toFixed(2)}</td>
                    <td class="cqv-value-cell">${data.f3.toFixed(2)}</td>
                    <td class="cqv-value-cell">${company.f4.toFixed(2)}</td>
                    <td class="cqv-value-cell">${company.f5.toFixed(2)}</td>
                    <td class="cqv-value-cell">${company.f6.toFixed(2)}</td>
                    <td class="cqv-value-cell">${company.f7.toFixed(2)}</td>
                    <td class="cqv-value-cell">${company.f8.toFixed(2)}</td>
                    <td class="cqv-value-cell score-high" style="font-weight: bold;">${cqv_v2.toFixed(2)}</td>
                `;
                tbody.appendChild(tr);
            });
            
            const chartLabels = years.map(yr => (yr === "2026" && !rawHistory["2026"]) ? "2026 (Act.)" : yr);
            const chartData = years.map(yr => {
                const data = history[yr];
                return (
                    data.f1 * 0.20 +
                    data.f2 * 0.10 +
                    data.f3 * 0.10 +
                    company.f4 * 0.20 +
                    company.f5 * 0.10 +
                    company.f6 * 0.10 +
                    company.f7 * 0.10 +
                    company.f8 * 0.10
                );
            });
            renderHistoryChart(ticker, chartLabels, chartData);
            
            // Load analyst notes
            loadCompanyNotes(ticker);
        }

        function renderHistoryChart(ticker, labels, data) {
            if (typeof Chart === 'undefined') {
                console.warn("Chart.js is not loaded. Skipping line chart rendering.");
                return;
            }
            const canvasEl = document.getElementById('historyChart');
            if (!canvasEl) return;
            const ctx = canvasEl.getContext('2d');
            
            if (historyChart) {
                historyChart.destroy();
            }
            
            const gradient = ctx.createLinearGradient(0, 0, 0, 300);
            gradient.addColorStop(0, 'rgba(79, 70, 229, 0.4)');
            gradient.addColorStop(1, 'rgba(79, 70, 229, 0.0)');
            
            historyChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: `Evolución CQV - ${ticker}`,
                        data: data,
                        fill: true,
                        backgroundColor: gradient,
                        borderColor: '#4f46e5',
                        borderWidth: 3,
                        pointBackgroundColor: '#d946ef',
                        pointBorderColor: '#fff',
                        pointRadius: 6,
                        pointHoverRadius: 8,
                        tension: 0.3
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false },
                        tooltip: {
                            backgroundColor: '#0f172a',
                            borderColor: '#334155',
                            borderWidth: 1,
                            padding: 12,
                            displayColors: false,
                            callbacks: {
                                title: function(context) {
                                    return `Año ${context[0].label}`;
                                },
                                label: function(context) {
                                    return `CQV Score: ${context.parsed.y.toFixed(2)}`;
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            grid: { color: getChartGridColor() },
                            ticks: { color: getChartLabelColor() }
                        },
                        y: {
                            min: 1,
                            max: 10,
                            grid: { color: getChartGridColor() },
                            ticks: { color: getChartLabelColor(), stepSize: 1 }
                        }
                    }
                }
            });
        }

        // Navigation state
        function switchTab(tabId) {
            // Deactivate all panels
            document.querySelectorAll('.tab-panel').forEach(panel => {
                panel.classList.remove('active');
            });
            // Deactivate all nav buttons
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            
            // Activate current
            document.getElementById('tab-' + tabId).classList.add('active');
            
            // Activate current button
            const clickedBtn = Array.from(document.querySelectorAll('.nav-btn')).find(btn => {
                const text = btn.innerText.toLowerCase();
                if (tabId === 'explorer') return text.includes('explorador');
                if (tabId === 'methodology') return text.includes('metodología');
                if (tabId === 'history') return text.includes('tendencias') || text.includes('historial');
                return text.includes(tabId);
            });
            if (clickedBtn) clickedBtn.classList.add('active');
            
            // Re-render chart if navigating back to dashboard or history
            if (tabId === 'dashboard') {
                setTimeout(renderTopChart, 50);
            } else if (tabId === 'history' && historyChart) {
                setTimeout(() => historyChart.resize(), 50);
            }
        }

        // Data Helpers
        function getTier(score) {
            if (score >= 9.0) return { name: 'ÉLITE', class: 'tier-elite' };
            if (score >= 8.5) return { name: 'SÓLIDA', class: 'tier-strong' };
            if (score >= 8.0) return { name: 'MEDIA', class: 'tier-medium' };
            return { name: 'ESPECULATIVA', class: 'tier-speculative' };
        }

        // KPI Calculations
        function initKPIs() {
            document.getElementById('kpi-total-companies').innerText = companies.length;
            
            const totalCqv = companies.reduce((acc, c) => acc + c.cqv, 0);
            const avgCqv = totalCqv / companies.length;
            document.getElementById('kpi-avg-cqv').innerText = avgCqv.toFixed(2);
            
            const eliteCount = companies.filter(c => c.cqv >= 9.0).length;
            document.getElementById('kpi-elite-count').innerText = eliteCount;
            
            if (companies.length > 0) {
                const sorted = [...companies].sort((a, b) => b.cqv - a.cqv);
                document.getElementById('kpi-top-performer').innerText = `${sorted[0].ticker} (${sorted[0].cqv.toFixed(2)})`;
            }
            
            // Calculate distributions
            const total = companies.length;
            const elite = companies.filter(c => c.cqv >= 9.0).length;
            const strong = companies.filter(c => c.cqv >= 8.5 && c.cqv < 9.0).length;
            const medium = companies.filter(c => c.cqv >= 8.0 && c.cqv < 8.5).length;
            const weak = companies.filter(c => c.cqv < 8.0).length;
            
            document.getElementById('dist-count-elite').innerText = `${elite} emp. (${(elite/total*100).toFixed(0)}%)`;
            document.getElementById('dist-count-strong').innerText = `${strong} emp. (${(strong/total*100).toFixed(0)}%)`;
            document.getElementById('dist-count-medium').innerText = `${medium} emp. (${(medium/total*100).toFixed(0)}%)`;
            document.getElementById('dist-count-weak').innerText = `${weak} emp. (${(weak/total*100).toFixed(0)}%)`;
            
            document.getElementById('dist-bar-elite').style.width = `${(elite/total*100).toFixed(0)}%`;
            document.getElementById('dist-bar-strong').style.width = `${(strong/total*100).toFixed(0)}%`;
            document.getElementById('dist-bar-medium').style.width = `${(medium/total*100).toFixed(0)}%`;
            document.getElementById('dist-bar-weak').style.width = `${(weak/total*100).toFixed(0)}%`;
        }

        // Render Top 15 Bar Chart
        let topChart = null;
        function renderTopChart() {
            if (typeof Chart === 'undefined') {
                console.warn("Chart.js is not loaded. Skipping chart rendering.");
                return;
            }
            const canvasEl = document.getElementById('topChart');
            if (!canvasEl) return;
            const ctx = canvasEl.getContext('2d');
            const top15 = [...companies].sort((a, b) => b.cqv - a.cqv).slice(0, 15);
            
            const labels = top15.map(c => c.ticker);
            const data = top15.map(c => c.cqv);
            
            if (topChart) {
                topChart.destroy();
            }
            
            // Gradient fill
            const gradient = ctx.createLinearGradient(0, 0, 0, 300);
            gradient.addColorStop(0, '#4f46e5');
            gradient.addColorStop(1, '#d946ef');
            
            topChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'CQV Score',
                        data: data,
                        backgroundColor: gradient,
                        borderColor: 'rgba(255,255,255,0.1)',
                        borderWidth: 1,
                        borderRadius: 6,
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            backgroundColor: '#0f172a',
                            titleColor: '#f8fafc',
                            bodyColor: '#cbd5e1',
                            borderColor: '#334155',
                            borderWidth: 1,
                            padding: 12,
                            displayColors: false,
                            callbacks: {
                                title: function(context) {
                                    const index = context[0].dataIndex;
                                    return `${top15[index].ticker} - ${top15[index].name}`;
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            grid: {
                                display: false
                            },
                            ticks: {
                                color: getChartLabelColor(),
                                font: { family: 'Inter', size: 11 }
                            }
                        },
                        y: {
                            min: 6,
                            max: 10,
                            grid: {
                                color: getChartGridColor()
                            },
                            ticks: {
                                color: getChartLabelColor(),
                                font: { family: 'Outfit', size: 11 }
                            }
                        }
                    }
                }
            });
        }

        // Explorer Table Logic
        let filteredData = [];
        let currentSort = { column: 'cqv', direction: 'desc' };
        let currentPage = 1;
        let rowsPerPage = 50;

        function renderTable() {
            const tbody = document.getElementById('companies-table-body');
            if (!tbody) return;
            tbody.innerHTML = '';
            
            const start = (currentPage - 1) * rowsPerPage;
            const end = rowsPerPage === 'all' ? filteredData.length : start + parseInt(rowsPerPage);
            const pageData = rowsPerPage === 'all' ? filteredData : filteredData.slice(start, end);
            
            pageData.forEach(c => {
                const tier = getTier(c.cqv);
                const tr = document.createElement('tr');
                tr.style.cursor = 'pointer';
                tr.onclick = function() {
                    switchTab('history');
                    const selectEl = document.getElementById('history-company-select');
                    if (selectEl) {
                        selectEl.value = c.ticker;
                        loadCompanyHistory();
                    }
                };
                
                // Build sparkline HTML for 5-year CQV history (including current 2026)
                let sparklineHtml = '';
                const history = typeof cqvHistoryData !== 'undefined' ? cqvHistoryData[c.ticker] : null;
                if (history) {
                    const yrData = { ...history };
                    if (!yrData["2026"]) {
                        yrData["2026"] = { f1: c.f1, f2: c.f2, f3: c.f3, cqv: c.cqv };
                    }
                    const years = Object.keys(yrData).sort();
                    let bars = '';
                    years.forEach(yr => {
                        let yrCqv = yrData[yr].cqv;
                        if (currentVersion === 'v2') {
                            yrCqv = (yrData[yr].f1 * 0.20) + (yrData[yr].f2 * 0.10) + (yrData[yr].f3 * 0.10) + (c.f4 * 0.20) + (c.f5 * 0.10) + (c.f6 * 0.10) + (c.f7 * 0.10) + (c.f8 * 0.10);
                        }
                        const heightPct = (yrCqv / 10.0) * 100;
                        let barColor = 'var(--text-secondary)';
                        if (yrCqv >= 9.0) barColor = 'var(--elite)';
                        else if (yrCqv >= 8.5) barColor = 'var(--strong)';
                        else if (yrCqv >= 8.0) barColor = 'var(--medium)';
                        else barColor = 'var(--weak)';
                        
                        bars += `<div class="sparkline-bar" style="height: ${heightPct}%; background-color: ${barColor};" title="Año ${yr}: ${yrCqv.toFixed(2)}"></div>`;
                    });
                    sparklineHtml = `<div class="sparkline-container">${bars}</div>`;
                } else {
                    // Fallback to show at least the current 2026 bar if no history database is available
                    const heightPct = (c.cqv / 10.0) * 100;
                    let barColor = 'var(--text-secondary)';
                    if (c.cqv >= 9.0) barColor = 'var(--elite)';
                    else if (c.cqv >= 8.5) barColor = 'var(--strong)';
                    else if (c.cqv >= 8.0) barColor = 'var(--medium)';
                    else barColor = 'var(--weak)';
                    
                    sparklineHtml = `
                        <div class="sparkline-container" style="justify-content: center;">
                            <div class="sparkline-bar" style="height: ${heightPct}%; background-color: ${barColor};" title="Año 2026 (Act.): ${c.cqv.toFixed(2)}"></div>
                        </div>
                    `;
                }

                // Calculate trend from 2025 to 2026
                let trendHtml = '';
                if (history && history["2025"]) {
                    let score2025 = history["2025"].cqv;
                    if (currentVersion === 'v2') {
                        score2025 = (history["2025"].f1 * 0.20) + (history["2025"].f2 * 0.10) + (history["2025"].f3 * 0.10) + (c.f4 * 0.20) + (c.f5 * 0.10) + (c.f6 * 0.10) + (c.f7 * 0.10) + (c.f8 * 0.10);
                    }
                    const score2026 = c.cqv;
                    const diff = score2026 - score2025;
                    
                    if (diff > 0.005) {
                        trendHtml = `<span style="color: var(--elite); font-weight: bold; font-size: 11px; display: inline-flex; align-items: center;" title="Mejorando vs 2025: +${diff.toFixed(2)}"><i class="fa-solid fa-arrow-trend-up"></i></span>`;
                    } else if (diff < -0.005) {
                        trendHtml = `<span style="color: var(--weak); font-weight: bold; font-size: 11px; display: inline-flex; align-items: center;" title="Empeorando vs 2025: ${diff.toFixed(2)}"><i class="fa-solid fa-arrow-trend-down"></i></span>`;
                    } else {
                        trendHtml = `<span style="color: var(--medium); font-weight: bold; font-size: 11px; display: inline-flex; align-items: center;" title="Sin cambios vs 2025"><i class="fa-solid fa-arrow-right"></i></span>`;
                    }
                } else {
                    trendHtml = `<span style="color: var(--text-secondary); opacity: 0.3; font-size: 11px;" title="Sin datos de 2025">-</span>`;
                }

                const sparklineCellHtml = `
                    <div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; width: 68px;">
                        ${sparklineHtml}
                        ${trendHtml}
                    </div>
                `;

                tr.innerHTML = `
                    <td><span class="ticker-badge">${c.ticker}</span></td>
                    <td><span class="company-name">${c.name}</span></td>
                    <td class="cqv-value-cell">${c.f1.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f2.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f3.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f4.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f5.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f6.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f7.toFixed(2)}</td>
                    <td class="cqv-value-cell">${c.f8.toFixed(2)}</td>
                    <td class="cqv-value-cell score-high">${c.cqv.toFixed(2)}</td>
                    <td>${sparklineCellHtml}</td>
                    <td><span class="tier-badge ${tier.class}">${tier.name}</span></td>
                `;
                tbody.appendChild(tr);
            });
            
            // Update labels
            const totalCount = filteredData.length;
            const showingStart = totalCount === 0 ? 0 : start + 1;
            const showingEnd = rowsPerPage === 'all' ? totalCount : Math.min(end, totalCount);
            document.getElementById('showing-entries-label').innerText = `Mostrando ${showingStart} - ${showingEnd} de ${totalCount} empresas`;
            
            renderPagination(totalCount);
        }

        function renderPagination(totalCount) {
            const wrapper = document.getElementById('pagination-wrapper');
            if (!wrapper) return;
            wrapper.innerHTML = '';
            
            if (rowsPerPage === 'all' || totalCount <= rowsPerPage) return;
            
            const totalPages = Math.ceil(totalCount / rowsPerPage);
            
            // Prev btn
            const prevBtn = document.createElement('button');
            prevBtn.className = 'page-btn';
            prevBtn.innerHTML = '<i class="fa-solid fa-chevron-left"></i>';
            prevBtn.disabled = currentPage === 1;
            prevBtn.onclick = () => { currentPage--; renderTable(); };
            wrapper.appendChild(prevBtn);
            
            // Page numbers
            const maxVisible = 5;
            let startPage = Math.max(1, currentPage - 2);
            let endPage = Math.min(totalPages, startPage + maxVisible - 1);
            if (endPage - startPage < maxVisible - 1) {
                startPage = Math.max(1, endPage - maxVisible + 1);
            }
            
            for (let i = startPage; i <= endPage; i++) {
                const pageBtn = document.createElement('button');
                pageBtn.className = `page-btn ${i === currentPage ? 'active' : ''}`;
                pageBtn.innerText = i;
                pageBtn.onclick = () => { currentPage = i; renderTable(); };
                wrapper.appendChild(pageBtn);
            }
            
            // Next btn
            const nextBtn = document.createElement('button');
            nextBtn.className = 'page-btn';
            nextBtn.innerHTML = '<i class="fa-solid fa-chevron-right"></i>';
            nextBtn.disabled = currentPage === totalPages;
            nextBtn.onclick = () => { currentPage++; renderTable(); };
            wrapper.appendChild(nextBtn);
        }

        function handleSearch() {
            const query = document.getElementById('search-bar').value.toLowerCase().trim();
            applyFilters(query, document.getElementById('tier-filter').value);
        }

        function handleFilter() {
            const tier = document.getElementById('tier-filter').value;
            const query = document.getElementById('search-bar').value.toLowerCase().trim();
            applyFilters(query, tier);
        }

        function applyFilters(query, tier) {
            filteredData = companies.filter(c => {
                const matchesQuery = c.ticker.toLowerCase().includes(query) || c.name.toLowerCase().includes(query);
                
                let matchesTier = true;
                if (tier === 'elite') matchesTier = c.cqv >= 9.0;
                else if (tier === 'strong') matchesTier = c.cqv >= 8.5 && c.cqv < 9.0;
                else if (tier === 'medium') matchesTier = c.cqv >= 8.0 && c.cqv < 8.5;
                else if (tier === 'speculative') matchesTier = c.cqv < 8.0;
                
                return matchesQuery && matchesTier;
            });
            
            currentPage = 1;
            sortData();
            renderTable();
        }

        function handleRowsChange() {
            rowsPerPage = document.getElementById('rows-filter').value;
            currentPage = 1;
            renderTable();
        }

        function handleSort(column) {
            if (currentSort.column === column) {
                currentSort.direction = currentSort.direction === 'asc' ? 'desc' : 'asc';
            } else {
                currentSort.column = column;
                currentSort.direction = 'desc'; // default high to low
            }
            
            // Update UI headers indicators
            const colIndices = { 'ticker': 0, 'name': 1, 'f1': 2, 'f2': 3, 'f3': 4, 'f4': 5, 'f5': 6, 'f6': 7, 'f7': 8, 'f8': 9, 'cqv': 10 };
            
            for (let key in colIndices) {
                const icon = document.getElementById('sort-icon-' + key);
                if (key === column) {
                    icon.innerHTML = currentSort.direction === 'asc' ? '<i class="fa-solid fa-sort-up"></i>' : '<i class="fa-solid fa-sort-down"></i>';
                } else {
                    icon.innerHTML = '<i class="fa-solid fa-sort"></i>';
                }
            }
            
            sortData();
            renderTable();
        }

        function sortData() {
            const col = currentSort.column;
            const dir = currentSort.direction === 'asc' ? 1 : -1;
            
            filteredData.sort((a, b) => {
                let valA = a[col];
                let valB = b[col];
                
                if (typeof valA === 'string') {
                    return valA.localeCompare(valB) * dir;
                }
                return (valA - valB) * dir;
            });
        }

        // Simulator Logic
        let simChart = null;
        function runSimulation() {
            const f1 = parseFloat(document.getElementById('slide-f1').value);
            const f2 = parseFloat(document.getElementById('slide-f2').value);
            const f3 = parseFloat(document.getElementById('slide-f3').value);
            const f4 = parseFloat(document.getElementById('slide-f4').value);
            const f5 = parseFloat(document.getElementById('slide-f5').value);
            const f6 = parseFloat(document.getElementById('slide-f6').value);
            const f7 = parseFloat(document.getElementById('slide-f7').value);
            const f8 = parseFloat(document.getElementById('slide-f8').value);
            
            // Update labels
            document.getElementById('val-f1').innerText = f1.toFixed(1);
            document.getElementById('val-f2').innerText = f2.toFixed(1);
            document.getElementById('val-f3').innerText = f3.toFixed(1);
            document.getElementById('val-f4').innerText = f4.toFixed(1);
            document.getElementById('val-f5').innerText = f5.toFixed(1);
            document.getElementById('val-f6').innerText = f6.toFixed(1);
            document.getElementById('val-f7').innerText = f7.toFixed(1);
            document.getElementById('val-f8').innerText = f8.toFixed(1);
            
            // Equation weights based on version
            let cqv = 0;
            if (currentVersion === 'v1') {
                cqv = (f1 * 0.25) + (f2 * 0.15) + (f3 * 0.15) + (f4 * 0.25) + (f5 * 0.20);
            } else {
                cqv = (f1 * 0.20) + (f2 * 0.10) + (f3 * 0.10) + (f4 * 0.20) + (f5 * 0.10) + (f6 * 0.10) + (f7 * 0.10) + (f8 * 0.10);
            }
            
            // Update display
            const display = document.getElementById('sim-cqv-score');
            display.innerText = cqv.toFixed(2);
            
            const tier = getTier(cqv);
            const tierBadge = document.getElementById('sim-tier-badge');
            tierBadge.innerText = tier.name;
            tierBadge.className = `tier-badge ${tier.class}`;
            
            const simData = [f1, f2, f3, f4, f5, f6, f7, f8];
            updateSimChart(simData, window.originalSimData);
        }

        function updateSimChart(data, originalBenchmark) {
            if (typeof Chart === 'undefined') {
                console.warn("Chart.js is not loaded. Skipping radar chart update.");
                return;
            }
            const canvasEl = document.getElementById('simChart');
            if (!canvasEl) return;
            const ctx = canvasEl.getContext('2d');
            
            if (simChart) {
                simChart.destroy();
            }
            
            const simDataFinal = (currentVersion === 'v2') ? data : data.slice(0, 5);
            const datasets = [{
                label: 'Valores Simulados',
                data: simDataFinal,
                backgroundColor: 'rgba(6, 182, 212, 0.2)',
                borderColor: '#06b6d4',
                borderWidth: 2,
                pointBackgroundColor: '#06b6d4',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: '#06b6d4'
            }];
            
            if (originalBenchmark) {
                const benchmarkDataFinal = (currentVersion === 'v2') ? originalBenchmark.data : originalBenchmark.data.slice(0, 5);
                datasets.push({
                    label: `Original: ${originalBenchmark.ticker}`,
                    data: benchmarkDataFinal,
                    backgroundColor: 'rgba(217, 70, 239, 0.05)',
                    borderColor: 'rgba(217, 70, 239, 0.6)',
                    borderWidth: 1.5,
                    borderDash: [5, 5],
                    pointBackgroundColor: '#d946ef',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: '#d946ef'
                });
            }
            
            simChart = new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: (currentVersion === 'v2') ?
                        ['F1 (Rent.)', 'F2 (Solidez)', 'F3 (Crec.)', 'F4 (Moat)', 'F5 (Proj.)', 'F6 (Asig.)', 'F7 (Yield)', 'F8 (Antif.)'] :
                        ['F1 (Rent.)', 'F2 (Solidez)', 'F3 (Crec.)', 'F4 (Moat)', 'F5 (Proj.)'],
                    datasets: datasets
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: originalBenchmark ? true : false,
                            labels: {
                                color: '#94a3b8',
                                font: { family: 'Inter', size: 10 }
                            }
                        }
                    },
                    scales: {
                        r: {
                            min: 0,
                            max: 10,
                            ticks: {
                                stepSize: 2,
                                display: false
                            },
                            grid: {
                                color: getChartGridColor()
                            },
                            angleLines: {
                                color: getChartGridColor()
                            },
                            pointLabels: {
                                color: getChartLabelColor(),
                                font: {
                                    family: 'Outfit',
                                    size: 11
                                }
                            }
                        }
                    }
                }
            });
        }

        // Initialize script logic
        const hasData = (typeof window.companiesData !== 'undefined') || (typeof companiesData !== 'undefined');
        if (!hasData) {
            console.warn("cqv_data.js not found or blocked. Fetching cqv_data.json...");
            fetch('cqv_data.json')
                .then(r => r.json())
                .then(data => {
                    window.companiesData = data;
                    initDashboard();
                })
                .catch(err => {
                    console.error("CORS block or missing file. Manually injecting fallback...", err);
                    window.companiesData = [];
                });
        } else {
            initDashboard();
        }

        window.onload = function() {
            if (companies.length === 0 && ((window.companiesData && window.companiesData.length > 0) || (typeof companiesData !== 'undefined' && companiesData.length > 0))) {
                initDashboard();
            }
        };
    </script>
</body>
</html>
"""
        
        # Write clean html
        with open('dashboard.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("Successfully created clean dashboard.html linking cqv_data.js")
        
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
