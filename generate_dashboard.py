import os
import json
import pandas as pd

def main():
    try:
        records = []
        if os.path.exists('cqv_data.json'):
            with open('cqv_data.json', 'r', encoding='utf-8') as f:
                records = json.load(f)

        history_db = {}
        if os.path.exists('cqv_history.json'):
            with open('cqv_history.json', 'r', encoding='utf-8') as hf:
                history_db = json.load(hf)

        theses_dict = {}
        inform_dir = 'inform'
        if os.path.exists(inform_dir):
            for fn in os.listdir(inform_dir):
                if fn.endswith('.md') and fn != 'template.md':
                    base_key = fn.replace('.md', '').upper()
                    ticker = base_key.split('_')[0]
                    with open(os.path.join(inform_dir, fn), 'r', encoding='utf-8') as tf:
                        content = tf.read()
                        theses_dict[base_key] = content
                        if ticker not in theses_dict:
                            theses_dict[ticker] = content

        json_data = json.dumps(records, indent=2, ensure_ascii=False)

        js_content = f"window.companiesData = {json_data};\nwindow.cqvHistoryData = {json.dumps(history_db, indent=2)};\nwindow.investmentTheses = {json.dumps(theses_dict, indent=2)};"
        with open('cqv_data.js', 'w', encoding='utf-8') as f:
            f.write(js_content)
        print("Successfully saved cqv_data.js and cqv_history.js wrapper")

        html_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CQV Financial Dashboard v4.0 | Quality & Structural Value</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Vue.js 3 CDN -->
    <script src="https://cdn.jsdelivr.net/npm/vue@3/dist/vue.global.js"></script>
    <!-- Marked.js (Markdown renderer) -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <!-- Mermaid.js (Diagrams & Charts renderer) -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>

    <!-- Data Injections -->
    <script src="cqv_data.js"></script>
    <script src="cqv_history.js"></script>
    
    <script>
        window.companiesData = __INJECTED_COMPANIES__;
        window.cqvHistoryData = __INJECTED_HISTORY__;
        window.investmentTheses = __INJECTED_THESES__;
    </script>

    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: rgba(17, 24, 39, 0.75);
            --card-border: rgba(255, 255, 255, 0.08);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --input-bg: rgba(15, 23, 42, 0.6);
            --input-border: rgba(255, 255, 255, 0.08);
            --table-bg: rgba(15, 23, 42, 0.3);
            --item-bg: rgba(255, 255, 255, 0.02);
            --item-hover-bg: rgba(255, 255, 255, 0.05);
            --header-bg: rgba(11, 15, 25, 0.85);
            --th-bg: #131b2e;
            --primary: #6366f1;
            --primary-glow: rgba(99, 102, 241, 0.3);
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
            --card-bg: rgba(255, 255, 255, 0.9);
            --card-border: rgba(15, 23, 42, 0.08);
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --input-bg: rgba(255, 255, 255, 0.9);
            --input-border: rgba(0, 0, 0, 0.12);
            --table-bg: rgba(255, 255, 255, 0.6);
            --item-bg: rgba(0, 0, 0, 0.02);
            --item-hover-bg: rgba(0, 0, 0, 0.05);
            --header-bg: rgba(241, 245, 249, 0.9);
            --th-bg: #e2e8f0;
            --primary: #4f46e5;
            --primary-glow: rgba(79, 70, 229, 0.2);
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: var(--font-body);
            background-color: var(--bg-color);
            color: var(--text-primary);
            min-height: 100vh;
            overflow-x: hidden;
            line-height: 1.5;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        #app { display: flex; flex-direction: column; min-height: 100vh; }
        
        header {
            position: sticky; top: 0; z-index: 100;
            background: var(--header-bg);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--card-border);
            padding: 0.85rem 2rem;
            display: flex; justify-content: space-between; align-items: center;
        }
        .brand { display: flex; align-items: center; gap: 0.75rem; }
        .brand-icon {
            width: 40px; height: 40px; border-radius: 10px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            display: flex; align-items: center; justify-content: center;
            color: #fff; font-size: 1.25rem; font-weight: bold;
            box-shadow: 0 4px 14px var(--primary-glow);
        }
        .brand-title { font-family: var(--font-title); font-size: 1.4rem; font-weight: 800; letter-spacing: -0.02em; }
        .brand-subtitle { font-size: 0.75rem; color: var(--text-secondary); display: block; }

        nav { display: flex; gap: 0.5rem; }
        .nav-btn {
            background: transparent; border: none; color: var(--text-secondary);
            padding: 0.6rem 1.1rem; border-radius: 8px; font-family: var(--font-title);
            font-weight: 600; font-size: 0.9rem; cursor: pointer; transition: var(--transition);
            display: flex; align-items: center; gap: 0.5rem;
        }
        .nav-btn:hover { color: var(--text-primary); background: var(--item-hover-bg); }
        .nav-btn.active { color: #fff; background: var(--primary); box-shadow: 0 4px 12px var(--primary-glow); }

        .header-actions { display: flex; align-items: center; gap: 1rem; }
        .theme-btn {
            background: var(--card-bg); border: 1px solid var(--card-border);
            color: var(--text-primary); width: 38px; height: 38px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center; cursor: pointer;
            transition: var(--transition);
        }
        .theme-btn:hover { transform: scale(1.05); border-color: var(--primary); }

        main { flex: 1; padding: 2rem; max-width: 1600px; margin: 0 auto; width: 100%; }

        .card {
            background: var(--card-bg); border: 1px solid var(--card-border);
            border-radius: 16px; padding: 1.5rem; backdrop-filter: blur(12px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2); transition: var(--transition);
        }
        .card:hover { border-color: rgba(255, 255, 255, 0.15); }
        
        .kpi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.25rem; margin-bottom: 2rem; }
        .kpi-card { display: flex; align-items: center; gap: 1.25rem; }
        .kpi-icon {
            width: 52px; height: 52px; border-radius: 14px;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.5rem; background: var(--item-bg); color: var(--primary);
        }
        .kpi-value { font-family: var(--font-title); font-size: 1.8rem; font-weight: 800; line-height: 1.1; }
        .kpi-label { font-size: 0.8rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; }
        .kpi-sub { font-size: 0.75rem; color: var(--text-secondary); margin-top: 0.2rem; }

        .showcase-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.25rem; margin-bottom: 2rem; }
        .top20-card {
            background: var(--card-bg); border: 1px solid var(--card-border);
            border-radius: 14px; padding: 1.25rem; cursor: pointer; transition: var(--transition);
            position: relative; overflow: hidden;
        }
        .top20-card:hover { transform: translateY(-4px); border-color: var(--primary); box-shadow: 0 12px 24px var(--primary-glow); }
        .top20-rank {
            position: absolute; top: 1rem; right: 1rem; font-family: var(--font-title);
            font-weight: 800; font-size: 0.9rem; color: var(--text-secondary); opacity: 0.6;
        }
        .top20-ticker { font-family: var(--font-title); font-weight: 800; font-size: 1.4rem; color: var(--text-primary); }
        .top20-name { font-size: 0.8rem; color: var(--text-secondary); margin-bottom: 1rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .top20-scores { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 1rem; }
        .top20-score-num { font-family: var(--font-title); font-size: 1.6rem; font-weight: 800; color: var(--elite); }

        .metrics-pills { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem; }
        .pill { background: var(--item-bg); padding: 0.4rem 0.6rem; border-radius: 6px; font-size: 0.75rem; display: flex; justify-content: space-between; }
        .pill-lbl { color: var(--text-secondary); }
        .pill-val { font-weight: 700; font-family: var(--font-title); }

        .charts-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(500px, 1fr)); gap: 1.5rem; margin-bottom: 2rem; }
        .chart-container { position: relative; height: 320px; width: 100%; }

        .controls-bar { display: flex; flex-wrap: wrap; gap: 1rem; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }
        .search-box { position: relative; flex: 1; min-width: 280px; }
        .search-box i { position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); color: var(--text-secondary); }
        .input-field {
            width: 100%; background: var(--input-bg); border: 1px solid var(--input-border);
            color: var(--text-primary); padding: 0.75rem 1rem 0.75rem 2.8rem; border-radius: 10px;
            font-size: 0.9rem; transition: var(--transition);
        }
        .input-field:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px var(--primary-glow); }

        .select-field {
            background: var(--input-bg); border: 1px solid var(--input-border);
            color: var(--text-primary); padding: 0.75rem 1rem; border-radius: 10px;
            font-size: 0.9rem; outline: none; cursor: pointer;
        }

        .table-responsive { overflow-x: auto; border-radius: 12px; border: 1px solid var(--card-border); }
        table { width: 100%; border-collapse: collapse; text-align: left; font-size: 0.82rem; }
        th {
            background: var(--th-bg); color: var(--text-secondary); font-family: var(--font-title);
            font-weight: 700; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.05em;
            padding: 0.8rem 0.6rem; cursor: pointer; user-select: none; border-bottom: 1px solid var(--card-border);
            white-space: nowrap;
        }
        th:hover { color: var(--text-primary); }
        td { padding: 0.8rem 0.6rem; border-bottom: 1px solid var(--card-border); white-space: nowrap; }
        tbody tr { transition: var(--transition); cursor: pointer; }
        tbody tr:hover { background: var(--item-hover-bg); }

        .explorer-table { width: 100%; border-collapse: collapse; text-align: left; font-size: 0.78rem; table-layout: auto; }
        .explorer-table th {
            background: var(--th-bg); color: var(--text-secondary); font-family: var(--font-title);
            font-weight: 700; text-transform: uppercase; font-size: 0.72rem; letter-spacing: 0.03em;
            padding: 0.6rem 0.35rem; cursor: pointer; user-select: none; border-bottom: 1px solid var(--card-border);
            white-space: nowrap; text-align: center; transition: var(--transition);
        }
        .explorer-table th:hover { color: var(--text-primary); }
        .explorer-table td { padding: 0.45rem 0.35rem; border-bottom: 1px solid var(--card-border); white-space: nowrap; text-align: center; font-size: 0.78rem; }
        
        .explorer-table .cell-ticker { font-weight: 800; color: var(--primary); text-align: left; }
        .explorer-table .cell-name { max-width: 130px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; text-align: left; }
        .explorer-table .cell-sector { max-width: 105px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; text-align: left; font-size: 0.72rem; color: var(--text-secondary); }
        
        .explorer-table.vertical-headers th {
            height: 105px; vertical-align: bottom; padding: 0.5rem 0.15rem;
        }
        .explorer-table.vertical-headers th .th-content {
            writing-mode: vertical-rl; transform: rotate(180deg);
            white-space: nowrap; display: inline-flex; align-items: center; justify-content: flex-start;
            gap: 0.3rem; max-height: 95px; margin: 0 auto;
        }
        .explorer-table th .th-content {
            display: inline-flex; align-items: center; justify-content: center; gap: 0.25rem;
        }

        .badge {
            display: inline-block; padding: 0.25rem 0.6rem; border-radius: 6px;
            font-size: 0.75rem; font-weight: 700; font-family: var(--font-title); text-align: center;
        }
        .tier-elite-suprema { background: rgba(16, 185, 129, 0.22); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.6); box-shadow: 0 0 10px rgba(16, 185, 129, 0.3); font-weight: 800; }
        .tier-elite { background: rgba(132, 204, 22, 0.2); color: #84cc16; border: 1px solid rgba(132, 204, 22, 0.45); font-weight: 700; }
        .tier-strong { background: rgba(59, 130, 246, 0.15); color: #3b82f6; border: 1px solid rgba(59, 130, 246, 0.3); }
        .tier-medium { background: rgba(245, 158, 11, 0.15); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.3); }
        .tier-speculative { background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3); }

        .has-tooltip {
            position: relative;
            cursor: help;
        }
        .has-tooltip:hover::after {
            content: attr(data-tooltip);
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            margin-top: 6px;
            background: #0f172a;
            color: #f8fafc;
            padding: 0.65rem 0.9rem;
            border-radius: 8px;
            font-size: 0.76rem;
            font-weight: 500;
            white-space: normal;
            width: max-content;
            max-width: 250px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.2);
            z-index: 999999;
            pointer-events: none;
            text-transform: none;
            letter-spacing: normal;
            line-height: 1.4;
            display: block !important;
            opacity: 1 !important;
            visibility: visible !important;
        }
        .has-tooltip:hover::before {
            content: '';
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            margin-top: 0px;
            border-width: 6px;
            border-style: solid;
            border-color: transparent transparent #0f172a transparent;
            z-index: 1000000;
            pointer-events: none;
            display: block !important;
        }

        .verdict-buy { background: rgba(16, 185, 129, 0.2); color: #34d399; font-weight: 800; }
        .verdict-hold { background: rgba(245, 158, 11, 0.2); color: #fbbf24; font-weight: 800; }
        .verdict-avoid { background: rgba(239, 68, 68, 0.2); color: #f87171; font-weight: 800; }

        .pagination { display: flex; justify-content: space-between; align-items: center; margin-top: 1.5rem; }
        .page-btns { display: flex; gap: 0.4rem; }
        .page-btn {
            background: var(--input-bg); border: 1px solid var(--input-border); color: var(--text-primary);
            width: 34px; height: 34px; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center;
        }
        .page-btn.active { background: var(--primary); border-color: var(--primary); }

        .thesis-body {
            background: var(--table-bg); border-radius: 12px; padding: 2rem;
            line-height: 1.7; color: var(--text-primary); max-height: 850px; overflow-y: auto;
            border: 1px solid var(--card-border);
        }
        .thesis-body h1, .thesis-body h2, .thesis-body h3 { font-family: var(--font-title); margin-top: 1.5rem; margin-bottom: 0.75rem; color: var(--text-primary); }
        .thesis-body h1 { border-bottom: 1px solid var(--card-border); padding-bottom: 0.5rem; font-size: 1.6rem; color: var(--primary); }
        .thesis-body h2 { font-size: 1.3rem; color: var(--accent); }
        .thesis-body table { width: 100%; margin: 1rem 0; font-size: 0.85rem; border-collapse: collapse; }
        .thesis-body th, .thesis-body td { padding: 0.6rem; border: 1px solid var(--card-border); }

        .markdown-alert { padding: 1rem; border-radius: 8px; margin: 1.25rem 0; border-left: 4px solid var(--primary); background: var(--item-bg); }
        .markdown-alert-note { border-left-color: #3b82f6; background: rgba(59, 130, 246, 0.1); }
        .markdown-alert-warning { border-left-color: #ef4444; background: rgba(239, 68, 68, 0.1); }
        .markdown-alert-tip { border-left-color: #10b981; background: rgba(16, 185, 129, 0.1); }
        .markdown-alert-important { border-left-color: #8b5cf6; background: rgba(139, 92, 246, 0.1); }

        .cqv-floating-tooltip {
            position: fixed;
            transform: translate(-50%, -100%);
            background: #0f172a;
            color: #f8fafc;
            padding: 0.65rem 0.9rem;
            border-radius: 10px;
            font-size: 0.78rem;
            max-width: 260px;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.2);
            z-index: 999999;
            pointer-events: none;
            line-height: 1.45;
            backdrop-filter: blur(12px);
            transition: opacity 0.15s ease, transform 0.1s ease;
        }

        .quarter-pill {
            padding: 0.4rem 0.8rem; border-radius: 8px; font-size: 0.8rem; font-family: var(--font-title);
            font-weight: 700; cursor: pointer; border: 1px solid var(--card-border); background: var(--input-bg);
            color: var(--text-secondary); transition: var(--transition);
        }
        .quarter-pill:hover { color: var(--text-primary); border-color: var(--primary); }
        .quarter-pill.active { background: var(--primary); color: #fff; border-color: var(--primary); box-shadow: 0 2px 8px var(--primary-glow); }

        footer { text-align: center; padding: 2rem; border-top: 1px solid var(--card-border); color: var(--text-secondary); font-size: 0.8rem; margin-top: auto; }
    </style>
</head>
<body>
    <div id="app">
        <!-- Floating Tooltip Container -->
        <div 
            v-if="tooltipText" 
            class="cqv-floating-tooltip" 
            :style="{ top: tooltipY + 'px', left: tooltipX + 'px' }"
        >
            <div style="font-weight: 700; color: #38bdf8; margin-bottom: 2px;">{{ tooltipTitle }}</div>
            <div>{{ tooltipText }}</div>
        </div>

        <!-- Header -->
        <header>
            <div class="brand">
                <div class="brand-icon"><i class="fa-solid fa-chart-line"></i></div>
                <div>
                    <div class="brand-title">CQV FINANCIAL DASHBOARD</div>
                    <span class="brand-subtitle">Quality & Structural Value Model v4.0</span>
                </div>
            </div>
            
            <nav>
                <button class="nav-btn" :class="{ active: activeTab === 'dashboard' }" @click="selectTab('dashboard')">
                    <i class="fa-solid fa-gauge-high"></i> Resumen
                </button>
                <button class="nav-btn" :class="{ active: activeTab === 'explorer' }" @click="selectTab('explorer')">
                    <i class="fa-solid fa-table-list"></i> Explorador
                </button>
                <button class="nav-btn" :class="{ active: activeTab === 'history' }" @click="selectTab('history')">
                    <i class="fa-solid fa-clock-rotate-left"></i> Historial & Tesis
                </button>
            </nav>

            <div class="header-actions">
                <button class="theme-btn" @click="toggleTheme" title="Cambiar tema">
                    <i :class="isLightTheme ? 'fa-solid fa-moon' : 'fa-solid fa-sun'"></i>
                </button>
            </div>
        </header>

        <!-- Main Content Views -->
        <main>
            <!-- TAB 1: DASHBOARD SHOWCASE -->
            <div v-show="activeTab === 'dashboard'">
                <div class="kpi-grid">
                    <div class="card kpi-card">
                        <div class="kpi-icon"><i class="fa-solid fa-building"></i></div>
                        <div>
                            <div class="kpi-value">{{ totalCompanies }}</div>
                            <div class="kpi-label">Empresas Evaluadas</div>
                            <div class="kpi-sub">Dataset SSOT Auditado v4.0</div>
                        </div>
                    </div>
                    <div class="card kpi-card">
                        <div class="kpi-icon" style="color: var(--primary);"><i class="fa-solid fa-star"></i></div>
                        <div>
                            <div class="kpi-value">{{ formatScore(avgCqv) }} / 10</div>
                            <div class="kpi-label">Promedio CQV Calidad</div>
                            <div class="kpi-sub">Media Ponderada F1-F8</div>
                        </div>
                    </div>
                    <div class="card kpi-card">
                        <div class="kpi-icon" style="color: #10b981;"><i class="fa-solid fa-crown"></i></div>
                        <div>
                            <div class="kpi-value" style="color: #10b981;">{{ eliteSupremaCount }}</div>
                            <div class="kpi-label">Élite Suprema</div>
                            <div class="kpi-sub">Score CQV v4.0 ≥ 9.50</div>
                        </div>
                    </div>
                    <div class="card kpi-card">
                        <div class="kpi-icon" style="color: #84cc16;"><i class="fa-solid fa-trophy"></i></div>
                        <div>
                            <div class="kpi-value" style="color: #84cc16;">{{ eliteCount }}</div>
                            <div class="kpi-label">Empresas Élite</div>
                            <div class="kpi-sub">Score CQV v4.0 (9.00 - 9.49)</div>
                        </div>
                    </div>
                    <div class="card kpi-card" v-if="topCompany">
                        <div class="kpi-icon" style="color: var(--secondary);"><i class="fa-solid fa-crown"></i></div>
                        <div>
                            <div class="kpi-value" style="color: var(--secondary);">{{ topCompany.ticker }} ({{ formatScore(topCompany.cqv) }})</div>
                            <div class="kpi-label">Líder #1 Global</div>
                            <div class="kpi-sub">{{ topCompany.name }}</div>
                        </div>
                    </div>
                </div>

                <h2 style="font-family: var(--font-title); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                    <i class="fa-solid fa-fire" style="color: var(--secondary);"></i> Top 20 Empresas de Mayor Calidad CQV v4.0
                </h2>
                <div class="showcase-grid">
                    <div class="top20-card" v-for="(c, idx) in top20Companies" :key="c.ticker" @click="selectCompanyHistory(c.ticker)">
                        <div class="top20-rank">#{{ idx + 1 }}</div>
                        <div class="top20-ticker">{{ c.ticker }}</div>
                        <div class="top20-name">{{ c.name }}</div>
                        <div class="top20-scores">
                            <span class="badge" :class="getTierInfo(c.cqv).class">{{ getTierInfo(c.cqv).name }}</span>
                            <span class="top20-score-num">{{ formatScore(c.cqv) }}</span>
                        </div>
                        <div class="metrics-pills">
                            <div class="pill"><span class="pill-lbl">F1 Rentab.</span><span class="pill-val">{{ formatNum(c.f1, 1) }}</span></div>
                            <div class="pill"><span class="pill-lbl">F2 Solidez</span><span class="pill-val">{{ formatNum(c.f2, 1) }}</span></div>
                            <div class="pill"><span class="pill-lbl">F4 Moat</span><span class="pill-val">{{ formatNum(c.f4, 1) }}</span></div>
                            <div class="pill"><span class="pill-lbl">PER Forward</span><span class="pill-val">{{ formatNum(c.pe_forward, 1, 'x') }}</span></div>
                        </div>
                    </div>
                </div>

                <div class="charts-grid">
                    <div class="card">
                        <h3 style="font-family: var(--font-title); margin-bottom: 1rem;">Ranking Top 20: Score CQV Calidad v4.0</h3>
                        <div class="chart-container"><canvas id="chartTop20"></canvas></div>
                    </div>
                    <div class="card">
                        <h3 style="font-family: var(--font-title); margin-bottom: 1rem;">Distribución Sectorial Top 20</h3>
                        <div class="chart-container"><canvas id="chartSectors"></canvas></div>
                    </div>
                </div>
            </div>

            <!-- TAB 2: EXPLORADOR DE EMPRESAS -->
            <div v-show="activeTab === 'explorer'">
                <div class="card">
                    <div class="controls-bar">
                        <div class="search-box">
                            <i class="fa-solid fa-magnifying-glass"></i>
                            <input type="text" class="input-field" v-model="searchQuery" placeholder="Buscar por Ticker, Nombre o Sector...">
                        </div>
                        <select class="select-field" v-model="selectedSector">
                            <option value="all">Todos los Sectores</option>
                            <option v-for="sec in sectors" :key="sec" :value="sec">{{ sec }}</option>
                        </select>
                        <select class="select-field" v-model="rowsPerPage">
                            <option :value="25">25 por pág.</option>
                            <option :value="50">50 por pág.</option>
                            <option :value="100">100 por pág.</option>
                            <option value="all">Ver todas</option>
                        </select>
                    </div>

                    <div class="table-responsive">
                        <table class="explorer-table">
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th @click="toggleSort('ticker')">Ticker</th>
                                    <th @click="toggleSort('name')">Nombre</th>
                                    <th @click="toggleSort('sector')">Sector</th>
                                    <th @click="toggleSort('quarter')">Trimestre</th>
                                    <th @click="toggleSort('f1')" title="F1: Economía del Negocio & Rentabilidad (Margen Operativo, ROIC, Conversión FCF)" @mouseenter="showTooltip($event, 'F1: Economía del Negocio & Rentabilidad', 'Margen Operativo ajustado, ROIC (Retorno sobre Capital Invertido) y conversión de beneficios a Flujo de Caja Libre (FCF). Peso: 20%.')" @mouseleave="hideTooltip">F1 <i class="fa-solid fa-circle-info" style="font-size: 0.65rem; opacity: 0.75; color: var(--primary);"></i></th>
                                    <th @click="toggleSort('f2')" title="F2: Solidez Financiera & Balance (Deuda Neta/EBITDA, Cobertura, Liquidez)" @mouseenter="showTooltip($event, 'F2: Solidez Financiera & Balance', 'Ratios de endeudamiento (Deuda Neta/EBITDA), cobertura de intereses, liquidez corriente y solidez del balance. Peso: 15%.')" @mouseleave="hideTooltip">F2 <i class="fa-solid fa-circle-info" style="font-size: 0.65rem; opacity: 0.75; color: var(--primary);"></i></th>
                                    <th @click="toggleSort('f3')" title="F3: Crecimiento Durable (Crecimiento orgánico sostenido y CAGR multianual)" @mouseenter="showTooltip($event, 'F3: Crecimiento Durable', 'Crecimiento orgánico sostenido de ingresos y beneficios, predictibilidad y CAGR multianual. Peso: 15%.')" @mouseleave="hideTooltip">F3 <i class="fa-solid fa-circle-info" style="font-size: 0.65rem; opacity: 0.75; color: var(--primary);"></i></th>
                                    <th @click="toggleSort('f4')" title="F4: Moat Competitivo & Foso (Ventajas estructurales y costes de cambio)" @mouseenter="showTooltip($event, 'F4: Moat Competitivo & Foso', 'Ventajas competitivas estructurales, foso (red, economías de escala, marca) y altos costes de cambio. Peso: 15%.')" @mouseleave="hideTooltip">F4 <i class="fa-solid fa-circle-info" style="font-size: 0.65rem; opacity: 0.75; color: var(--primary);"></i></th>
                                    <th @click="toggleSort('f5')" title="F5: Asignación de Capital (Recompras de acciones, dividendos y M&A)" @mouseenter="showTooltip($event, 'F5: Asignación de Capital', 'Disciplina de la directiva en recompras de acciones, pago de dividendos y retorno de inversiones M&A/CapEx. Peso: 10%.')" @mouseleave="hideTooltip">F5 <i class="fa-solid fa-circle-info" style="font-size: 0.65rem; opacity: 0.75; color: var(--primary);"></i></th>
                                    <th @click="toggleSort('f6')" title="F6: Dirección & Ejecución (Calidad directiva y alineación de incentivos)" @mouseenter="showTooltip($event, 'F6: Dirección & Ejecución', 'Calidad del equipo directivo, visión estratégica, historial de ejecución y alineación de incentivos. Peso: 10%.')" @mouseleave="hideTooltip">F6 <i class="fa-solid fa-circle-info" style="font-size: 0.65rem; opacity: 0.75; color: var(--primary);"></i></th>
                                    <th @click="toggleSort('f7')" title="F7: Opcionalidad Futura (Nuevos mercados, innovación y líneas de crecimiento)" @mouseenter="showTooltip($event, 'F7: Opcionalidad Futura', 'Capacidad de expandirse hacia nuevos mercados adyacentes, innovación tecnológica y nuevas líneas de negocio. Peso: 5%.')" @mouseleave="hideTooltip">F7 <i class="fa-solid fa-circle-info" style="font-size: 0.65rem; opacity: 0.75; color: var(--primary);"></i></th>
                                    <th @click="toggleSort('f8')" title="F8: Antifragilidad & Recurrencia (Predictibilidad de ingresos y resiliencia macro)" @mouseenter="showTooltip($event, 'F8: Antifragilidad & Recurrencia', 'Porcentaje de ingresos recurrentes (suscripciones), resistencia a recesiones macro y poder de fijación de precios. Peso: 10%.')" @mouseleave="hideTooltip">F8 <i class="fa-solid fa-circle-info" style="font-size: 0.65rem; opacity: 0.75; color: var(--primary);"></i></th>
                                    <th @click="toggleSort('cqv')" title="CQV Calidad v4.0: Suma ponderada de F1-F8 (0 a 10)" @mouseenter="showTooltip($event, 'CQV Calidad v4.0', 'Puntuación fundamental ponderada de los 8 factores (F1 a F8) en escala de 0.00 a 10.00.')" @mouseleave="hideTooltip">CQV v4.0 <i class="fa-solid fa-circle-info" style="font-size: 0.65rem; opacity: 0.75; color: var(--primary);"></i></th>
                                    <th @click="toggleSort('pe')" title="PER Trailing: Múltiplo sobre beneficios netos de los últimos 12 meses (TTM)" @mouseenter="showTooltip($event, 'PER Trailing (PER TTM)', 'Cotización actual dividida entre el Beneficio Neto por Acción acumulado de los últimos 12 meses reportados (TTM).')" @mouseleave="hideTooltip">PER Trail <i class="fa-solid fa-circle-info" style="font-size: 0.65rem; opacity: 0.75; color: var(--primary);"></i></th>
                                    <th @click="toggleSort('pe_forward')" title="PER Forward: Múltiplo sobre estimaciones de beneficio neto NTM (próximos 12 meses)" @mouseenter="showTooltip($event, 'PER Forward (PER NTM)', 'Cotización actual dividida entre las estimaciones del consenso de Beneficio Neto por Acción a 12 meses vista (NTM).')" @mouseleave="hideTooltip">PER Fwd <i class="fa-solid fa-circle-info" style="font-size: 0.65rem; opacity: 0.75; color: var(--primary);"></i></th>
                                    <th @click="toggleSort('value_score')" title="Value Score: Score ponderado de valoración (0.40 FCF Yield + 0.30 Score PEG + 0.30 Score MoS)" @mouseenter="showTooltip($event, 'Value Score (Capa Valoración)', 'Puntuación de valoración calculada como: 0.40(Score FCF Yield) + 0.30(Score PEG) + 0.30(Score MoS).')" @mouseleave="hideTooltip">Value Score <i class="fa-solid fa-circle-info" style="font-size: 0.65rem; opacity: 0.75; color: var(--primary);"></i></th>
                                    <th @click="toggleSort('verdict')">Veredicto</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(c, idx) in paginatedCompanies" :key="c.ticker" @click="selectCompanyHistory(c.ticker)">
                                    <td>{{ (currentPage - 1) * (rowsPerPage === 'all' ? 0 : rowsPerPage) + idx + 1 }}</td>
                                    <td class="cell-ticker">{{ c.ticker }}</td>
                                    <td class="cell-name">{{ c.name }}</td>
                                    <td class="cell-sector">{{ c.sector }}</td>
                                    <td>{{ c.quarter || 'Q2 2026' }}</td>
                                    <td>{{ formatNum(c.f1, 1) }}</td>
                                    <td>{{ formatNum(c.f2, 1) }}</td>
                                    <td>{{ formatNum(c.f3, 1) }}</td>
                                    <td>{{ formatNum(c.f4, 1) }}</td>
                                    <td>{{ formatNum(c.f5, 1) }}</td>
                                    <td>{{ formatNum(c.f6, 1) }}</td>
                                    <td>{{ formatNum(c.f7, 1) }}</td>
                                    <td>{{ formatNum(c.f8, 1) }}</td>
                                    <td><span class="badge" :class="getTierInfo(c.cqv).class">{{ formatScore(c.cqv) }}</span></td>
                                    <td>{{ formatNum(c.pe, 1, 'x') }}</td>
                                    <td>{{ formatNum(c.pe_forward, 1, 'x') }}</td>
                                    <td><strong style="color: var(--accent);">{{ formatNum(c.value_score, 2) }}</strong></td>
                                    <td><span class="badge" :class="getVerdictClass(c.verdict)">{{ c.verdict || 'N/D' }}</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- TAB 3: HISTORIAL TRIMESTRAL & TESIS -->
            <div v-show="activeTab === 'history'">
                <div class="card" style="margin-bottom: 1.5rem;">
                    <div style="display: flex; gap: 1.5rem; align-items: center; flex-wrap: wrap; justify-content: space-between;">
                        <div style="display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;">
                            <label style="font-family: var(--font-title); font-weight: 700;">Empresa:</label>
                            <select class="select-field" style="min-width: 280px;" v-model="selectedTicker" @change="onHistoryTickerChange">
                                <option v-for="c in sortedAllCompanies" :key="c.ticker" :value="c.ticker">{{ c.ticker }} - {{ c.name }}</option>
                            </select>
                        </div>

                        <div style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap;" v-if="availableQuartersForTicker.length > 0">
                            <span style="font-size: 0.8rem; color: var(--text-secondary); font-weight: 600;">Presentaciones Trimestrales (Q):</span>
                            <span 
                                class="quarter-pill" 
                                v-for="qItem in availableQuartersForTicker" 
                                :key="qItem.label"
                                :class="{ active: selectedQuarterLabel === qItem.label }"
                                @click="selectQuarter(qItem.label)"
                            >
                                <i class="fa-solid fa-calendar-minus"></i> {{ qItem.label }}
                            </span>
                        </div>
                    </div>
                </div>

                <div class="card" v-if="selectedCompanyObj" style="margin-bottom: 1.5rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                        <div>
                            <h2 style="font-family: var(--font-title); font-size: 1.6rem;">
                                {{ selectedCompanyObj.name }} <span style="color: var(--text-secondary);">({{ selectedCompanyObj.ticker }})</span>
                            </h2>
                            <p style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 0.25rem;">
                                Sector: {{ selectedCompanyObj.sector }} | 
                                <strong style="color: var(--primary);">Trimestre Seleccionado: {{ selectedQuarterLabel }}</strong>
                            </p>
                        </div>
                        <div style="display: flex; align-items: center; gap: 1.5rem;">
                            <div style="text-align: right;">
                                <div style="font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase;">Score CQV Calidad ({{ selectedQuarterLabel }})</div>
                                <div style="font-size: 2rem; font-weight: 800; color: var(--elite); font-family: var(--font-title);">{{ formatScore(activeQuarterSnapshot.cqv_v4 || selectedCompanyObj.cqv) }}</div>
                            </div>
                            <span class="badge" :class="getTierInfo(activeQuarterSnapshot.cqv_v4 || selectedCompanyObj.cqv).class" style="font-size: 0.9rem; padding: 0.5rem 1rem;">
                                {{ getTierInfo(activeQuarterSnapshot.cqv_v4 || selectedCompanyObj.cqv).name }}
                            </span>
                        </div>
                    </div>
                </div>

                <div class="card" style="margin-bottom: 1.5rem;" v-if="quarterlyBreakdownRows.length > 0">
                    <h3 style="font-family: var(--font-title); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                        <i class="fa-solid fa-list-check" style="color: var(--elite);"></i> Registro Histórico Auditado por Trimestres (Q1, Q2, Q3, Q4)
                    </h3>
                    <div class="table-responsive">
                        <table>
                            <thead>
                                <tr>
                                    <th>Periodo / Trimestre</th>
                                    <th>F1 Rent.</th>
                                    <th>F2 Sol.</th>
                                    <th>F3 Crec.</th>
                                    <th>F4 Moat</th>
                                    <th>F5 Asign.</th>
                                    <th>F6 Direc.</th>
                                    <th>F7 Opcion.</th>
                                    <th>F8 Antif.</th>
                                    <th>CQV v4.0</th>
                                    <th>PER Trail</th>
                                    <th>PER Fwd</th>
                                    <th>Value Score</th>
                                    <th>Veredicto</th>
                                    <th>Acción</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr 
                                    v-for="qRow in quarterlyBreakdownRows" 
                                    :key="qRow.period"
                                    :style="{ background: selectedQuarterLabel === qRow.period ? 'var(--item-hover-bg)' : 'transparent' }"
                                >
                                    <td><strong style="color: var(--primary); font-family: var(--font-title);">{{ qRow.period }}</strong></td>
                                    <td>{{ formatNum(qRow.f1, 1) }}</td>
                                    <td>{{ formatNum(qRow.f2, 1) }}</td>
                                    <td>{{ formatNum(qRow.f3, 1) }}</td>
                                    <td>{{ formatNum(qRow.f4, 1) }}</td>
                                    <td>{{ formatNum(qRow.f5, 1) }}</td>
                                    <td>{{ formatNum(qRow.f6, 1) }}</td>
                                    <td>{{ formatNum(qRow.f7, 1) }}</td>
                                    <td>{{ formatNum(qRow.f8, 1) }}</td>
                                    <td><span class="badge" :class="getTierInfo(qRow.cqv_v4).class">{{ formatScore(qRow.cqv_v4) }}</span></td>
                                    <td>{{ formatNum(qRow.pe, 1, 'x') }}</td>
                                    <td>{{ formatNum(qRow.pe_forward, 1, 'x') }}</td>
                                    <td><strong style="color: var(--accent);">{{ formatNum(qRow.value_score, 2) }}</strong></td>
                                    <td><span class="badge" :class="getVerdictClass(qRow.verdict)">{{ qRow.verdict || 'N/D' }}</span></td>
                                    <td>
                                        <button class="quarter-pill" style="padding: 0.2rem 0.5rem; font-size: 0.75rem;" @click="selectQuarter(qRow.period)">
                                            Ver Tesis
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div class="card">
                    <h3 style="font-family: var(--font-title); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                        <i class="fa-solid fa-file-lines" style="color: var(--primary);"></i> Informe de Tesis de Inversión ({{ selectedQuarterLabel }})
                    </h3>
                    <div class="thesis-body" id="thesisViewer" v-html="renderedThesis"></div>
                </div>
            </div>
        </main>
        <footer>
            <p>CQV Financial Platform v4.0 | Modelo de Calidad, Resiliencia y Valoración Multifactorial © 2026</p>
        </footer>
    </div>

    <script>
        const { createApp, ref, computed, watch, onMounted, nextTick } = Vue;

        createApp({
            setup() {
                const activeTab = ref('dashboard');
                const isLightTheme = ref(false);
                const companies = ref(window.companiesData || []);
                const historyDb = ref(window.cqvHistoryData || {});
                const theses = ref(window.investmentTheses || {});

                const searchQuery = ref('');
                const selectedSector = ref('all');
                const rowsPerPage = ref(25);
                const currentPage = ref(1);

                const sortKey = ref('cqv');
                const sortAsc = ref(false);

                const selectedTicker = ref(companies.value[0]?.ticker || 'AAPL');
                const selectedQuarterLabel = ref('2026 Q2');

                let chartTop20Inst = null;
                let chartSectorsInst = null;

                const toggleTheme = () => {
                    isLightTheme.value = !isLightTheme.value;
                    document.body.classList.toggle('light-theme', isLightTheme.value);
                    nextTick(() => renderAllCharts());
                };

                const selectTab = (tab) => {
                    activeTab.value = tab;
                    nextTick(() => renderAllCharts());
                };

                const selectCompanyHistory = (ticker) => {
                    selectedTicker.value = ticker;
                    activeTab.value = 'history';
                    onHistoryTickerChange();
                };

                const selectedCompanyObj = computed(() => {
                    return companies.value.find(c => c.ticker === selectedTicker.value) || companies.value[0];
                });

                const sortedAllCompanies = computed(() => {
                    return [...companies.value].sort((a, b) => (a.ticker || '').localeCompare(b.ticker || ''));
                });

                const quarterlyBreakdownRows = computed(() => {
                    const ticker = selectedTicker.value;
                    const rows = [];
                    const hist = historyDb.value[ticker];

                    if (hist) {
                        Object.keys(hist).sort().reverse().forEach(yr => {
                            const yrObj = hist[yr];
                            ['Q4', 'Q3', 'Q2', 'Q1'].forEach(q => {
                                if (yrObj[q] && (yrObj[q].cqv_v4 !== undefined || yrObj[q].cqv !== undefined)) {
                                    rows.push({
                                        period: `${yr} ${q}`,
                                        year: yr, quarter: q,
                                        ...yrObj[q]
                                    });
                                }
                            });
                        });
                    }
                    if (rows.length === 0 && selectedCompanyObj.value) {
                        const c = selectedCompanyObj.value;
                        rows.push({
                            period: c.quarter || '2026 Q2',
                            year: '2026', quarter: 'Q2',
                            f1: c.f1, f2: c.f2, f3: c.f3, f4: c.f4, f5: c.f5, f6: c.f6, f7: c.f7, f8: c.f8,
                            cqv_v4: c.cqv, pe: c.pe, pe_forward: c.pe_forward, value_score: c.value_score,
                            mos_pct: c.mos_pct, verdict: c.verdict, intrinsic_value: c.intrinsic_value
                        });
                    }
                    return rows;
                });

                const availableQuartersForTicker = computed(() => {
                    return quarterlyBreakdownRows.value.map(r => ({ label: r.period }));
                });

                const activeQuarterSnapshot = computed(() => {
                    const found = quarterlyBreakdownRows.value.find(r => r.period === selectedQuarterLabel.value);
                    if (found) return found;
                    if (quarterlyBreakdownRows.value.length > 0) return quarterlyBreakdownRows.value[0];
                    return selectedCompanyObj.value || {};
                });

                const renderedThesis = computed(() => {
                    const ticker = selectedTicker.value;
                    if (!ticker) return '';
                    const qLabel = selectedQuarterLabel.value || '';
                    const parts = qLabel.split(' ');
                    let qSuffix = '2026_Q2';
                    if (parts.length === 2) {
                        qSuffix = `${parts[0]}_${parts[1]}`;
                    }

                    const key1 = `${ticker}_${qSuffix}`;
                    const key2 = `${ticker.toLowerCase()}_${qSuffix.toLowerCase()}`;
                    const key3 = ticker;
                    const key4 = ticker.toLowerCase();

                    let raw = theses.value[key1] 
                           || theses.value[key2]
                           || theses.value[key3]
                           || theses.value[key4];

                    if (!raw && theses.value) {
                        const upperTicker = ticker.toUpperCase();
                        const keys = Object.keys(theses.value);
                        const matchKey = keys.find(k => k.startsWith(upperTicker + '_') || k === upperTicker);
                        if (matchKey) raw = theses.value[matchKey];
                    }

                    if (raw && typeof marked !== 'undefined') {
                        let parsedHtml = marked.parse(raw);
                        parsedHtml = parsedHtml
                            .replace(/<blockquote>\\s*<p>\\[!NOTE\\]/g, '<div class="markdown-alert markdown-alert-note"><p><strong><i class="fa-solid fa-circle-info"></i> NOTA AUDITADA:</strong>')
                            .replace(/<blockquote>\\s*<p>\\[!WARNING\\]/g, '<div class="markdown-alert markdown-alert-warning"><p><strong><i class="fa-solid fa-triangle-exclamation"></i> ALERTA / LÍNEA ROJA:</strong>')
                            .replace(/<blockquote>\\s*<p>\\[!TIP\\]/g, '<div class="markdown-alert markdown-alert-tip"><p><strong><i class="fa-solid fa-lightbulb"></i> RECOMENDACIÓN:</strong>')
                            .replace(/<blockquote>\\s*<p>\\[!IMPORTANT\\]/g, '<div class="markdown-alert markdown-alert-important"><p><strong><i class="fa-solid fa-circle-exclamation"></i> IMPORTANTE:</strong>')
                            .replace(/<\\/blockquote>/g, '</div>');
                        return parsedHtml;
                    } else if (raw) {
                        return `<div style="white-space: pre-wrap;">${raw}</div>`;
                    }
                    return `<div style="text-align: center; padding: 2.5rem 1rem; color: var(--text-secondary);"><i class="fa-solid fa-file-circle-xmark" style="font-size: 2.5rem; margin-bottom: 0.75rem; color: var(--medium); display: block;"></i><strong style="font-size: 1.1rem; color: var(--text-primary); display: block; margin-bottom: 0.5rem;">Informe de Tesis para ${ticker} (${qLabel})</strong>El informe de tesis detallado está disponible cuantitativamente en las métricas de la tabla superior.</div>`;
                });

                watch(renderedThesis, () => {
                    nextTick(() => {
                        if (typeof mermaid !== 'undefined') {
                            try {
                                mermaid.init(undefined, document.querySelectorAll('.thesis-body .language-mermaid'));
                            } catch (e) {}
                        }
                    });
                });

                const tooltipTitle = ref('');
                const tooltipText = ref('');
                const tooltipX = ref(0);
                const tooltipY = ref(0);

                const showTooltip = (evt, title, text) => {
                    tooltipTitle.value = title;
                    tooltipText.value = text;
                    const rect = evt.currentTarget.getBoundingClientRect();
                    tooltipX.value = rect.left + rect.width / 2;
                    tooltipY.value = rect.top - 8;
                };

                const hideTooltip = () => {
                    tooltipText.value = '';
                };

                const selectQuarter = (qLabel) => {
                    selectedQuarterLabel.value = qLabel;
                };

                const onHistoryTickerChange = () => {
                    nextTick(() => {
                        if (availableQuartersForTicker.value.length > 0) {
                            selectedQuarterLabel.value = availableQuartersForTicker.value[0].label;
                        } else {
                            selectedQuarterLabel.value = '2026 Q2';
                        }
                    });
                };

                const formatScore = (val) => val ? Number(val).toFixed(2) : 'N/D';
                const formatNum = (val, dec = 2, suffix = '') => (val !== null && val !== undefined && !isNaN(val)) ? (Number(val).toFixed(dec) + suffix) : 'N/D';
                
                const getTierInfo = (score) => {
                    const s = Number(score) || 0;
                    if (s >= 9.50) return { name: 'ÉLITE SUPREMA', class: 'tier-elite-suprema' };
                    if (s >= 9.00) return { name: 'ÉLITE', class: 'tier-elite' };
                    if (s >= 8.00) return { name: 'ALTA CALIDAD', class: 'tier-strong' };
                    if (s >= 7.00) return { name: 'CALIDAD MEDIA', class: 'tier-medium' };
                    return { name: 'EN OBSERVACIÓN', class: 'tier-speculative' };
                };

                const getVerdictClass = (v) => {
                    if (!v) return 'tier-medium';
                    if (v.includes('Comprar')) return 'verdict-buy';
                    if (v.includes('Acumular') || v.includes('Mantener')) return 'verdict-hold';
                    return 'verdict-avoid';
                };

                const totalCompanies = computed(() => companies.value.length);
                const avgCqv = computed(() => {
                    if (companies.value.length === 0) return 0;
                    const sum = companies.value.reduce((acc, c) => acc + (Number(c.cqv) || 0), 0);
                    return sum / companies.value.length;
                });
                const eliteSupremaCount = computed(() => companies.value.filter(c => (Number(c.cqv) || 0) >= 9.50).length);
                const eliteCount = computed(() => companies.value.filter(c => (Number(c.cqv) || 0) >= 9.00 && (Number(c.cqv) || 0) < 9.50).length);
                const topCompany = computed(() => companies.value[0] || null);
                const top20Companies = computed(() => companies.value.slice(0, 20));

                const sectors = computed(() => {
                    const set = new Set(companies.value.map(c => c.sector).filter(Boolean));
                    return Array.from(set).sort();
                });

                const filteredCompanies = computed(() => {
                    return companies.value.filter(c => {
                        const q = searchQuery.value.toLowerCase();
                        const matchesSearch = !q || (c.ticker && c.ticker.toLowerCase().includes(q)) || (c.name && c.name.toLowerCase().includes(q)) || (c.sector && c.sector.toLowerCase().includes(q));
                        const matchesSector = selectedSector.value === 'all' || c.sector === selectedSector.value;
                        return matchesSearch && matchesSector;
                    });
                });

                const sortedCompanies = computed(() => {
                    return [...filteredCompanies.value].sort((a, b) => {
                        let va = a[sortKey.value];
                        let vb = b[sortKey.value];
                        if (typeof va === 'string') va = va.toLowerCase();
                        if (typeof vb === 'string') vb = vb.toLowerCase();
                        if (va < vb) return sortAsc.value ? -1 : 1;
                        if (va > vb) return sortAsc.value ? 1 : -1;
                        return 0;
                    });
                });

                const totalPages = computed(() => {
                    if (rowsPerPage.value === 'all') return 1;
                    return Math.ceil(sortedCompanies.value.length / rowsPerPage.value) || 1;
                });

                const paginatedCompanies = computed(() => {
                    if (rowsPerPage.value === 'all') return sortedCompanies.value;
                    const start = (currentPage.value - 1) * rowsPerPage.value;
                    return sortedCompanies.value.slice(start, start + rowsPerPage.value);
                });

                const toggleSort = (key) => {
                    if (sortKey.value === key) {
                        sortAsc.value = !sortAsc.value;
                    } else {
                        sortKey.value = key;
                        sortAsc.value = false;
                    }
                };

                const getLabelColor = () => isLightTheme.value ? '#475569' : '#94a3b8';
                const getGridColor = () => isLightTheme.value ? 'rgba(0,0,0,0.06)' : 'rgba(255,255,255,0.08)';

                const renderDashboardCharts = () => {
                    if (typeof Chart === 'undefined') return;
                    const top20 = top20Companies.value;
                    const labelColor = getLabelColor();
                    const gridColor = getGridColor();

                    const canvas1 = document.getElementById('chartTop20');
                    if (canvas1) {
                        if (chartTop20Inst) chartTop20Inst.destroy();
                        chartTop20Inst = new Chart(canvas1.getContext('2d'), {
                            type: 'bar',
                            data: {
                                labels: top20.map(c => c.ticker),
                                datasets: [{
                                    label: 'Score CQV v4.0',
                                    data: top20.map(c => c.cqv),
                                    backgroundColor: '#6366f1',
                                    borderRadius: 6
                                }]
                            },
                            options: {
                                responsive: true, maintainAspectRatio: false,
                                plugins: { legend: { labels: { color: labelColor } } },
                                scales: {
                                    x: { grid: { display: false }, ticks: { color: labelColor } },
                                    y: { min: 8, max: 10, grid: { color: gridColor }, ticks: { color: labelColor } }
                                }
                            }
                        });
                    }

                    const canvas2 = document.getElementById('chartSectors');
                    if (canvas2) {
                        const secCounts = {};
                        top20.forEach(c => { secCounts[c.sector] = (secCounts[c.sector] || 0) + 1; });
                        if (chartSectorsInst) chartSectorsInst.destroy();
                        chartSectorsInst = new Chart(canvas2.getContext('2d'), {
                            type: 'doughnut',
                            data: {
                                labels: Object.keys(secCounts),
                                datasets: [{
                                    data: Object.values(secCounts),
                                    backgroundColor: ['#6366f1', '#10b981', '#3b82f6', '#f59e0b', '#ec4899', '#8b5cf6', '#14b8a6']
                                }]
                            },
                            options: {
                                responsive: true, maintainAspectRatio: false,
                                plugins: { legend: { position: 'right', labels: { color: labelColor } } },
                                cutout: '60%'
                            }
                        });
                    }
                };

                const renderAllCharts = () => {
                    if (activeTab.value === 'dashboard') renderDashboardCharts();
                };

                onMounted(() => {
                    onHistoryTickerChange();
                    nextTick(() => {
                        renderDashboardCharts();
                    });
                });

                return {
                    activeTab, isLightTheme, toggleTheme, selectTab, selectCompanyHistory,
                    companies, sortedAllCompanies, totalCompanies, avgCqv, eliteSupremaCount, eliteCount, topCompany, top20Companies,
                    searchQuery, selectedSector, sectors, rowsPerPage, currentPage, totalPages,
                    filteredCompanies, sortedCompanies, paginatedCompanies, toggleSort,
                    selectedTicker, selectedCompanyObj, selectedQuarterLabel, availableQuartersForTicker,
                    quarterlyBreakdownRows, activeQuarterSnapshot, renderedThesis, selectQuarter, onHistoryTickerChange,
                    formatScore, formatNum, getTierInfo, getVerdictClass,
                    tooltipTitle, tooltipText, tooltipX, tooltipY, showTooltip, hideTooltip
                };
            }
        }).mount('#app');
    </script>
</body>
</html>
"""

        html_out = html_template.replace('__INJECTED_COMPANIES__', json_data)
        html_out = html_out.replace('__INJECTED_HISTORY__', json.dumps(history_db, indent=2))
        html_out = html_out.replace('__INJECTED_THESES__', json.dumps(theses_dict, indent=2))

        with open('dashboard.html', 'w', encoding='utf-8') as f:
            f.write(html_out)
        print("Successfully generated clean Vue 3 powered dashboard.html!")

    except Exception as e:
        print("Error during dashboard generation:", e)

if __name__ == "__main__":
    main()
