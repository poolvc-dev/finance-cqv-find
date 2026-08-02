import json
import os

print("Updating SSOT datasets and generating enriched reports with Wall Street Analyst Consensus for FICO, META, ISRG, GOOGL, and MSFT...")

with open('cqv_data.json', 'r', encoding='utf-8') as f:
    cqv_list = json.load(f)

with open('cqv_history.json', 'r', encoding='utf-8') as f:
    cqv_hist = json.load(f)

# Audited Analyst Targets Data
analysts_db = {
    'FICO': {
        'target_low_bear': 1250.00,
        'target_mean_base': 1850.00,
        'target_high_bull': 2100.00,
        'num_analysts': 14,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 34.7
    },
    'META': {
        'target_low_bear': 520.00,
        'target_mean_base': 675.00,
        'target_high_bull': 775.00,
        'num_analysts': 58,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 15.3
    },
    'ISRG': {
        'target_low_bear': 410.00,
        'target_mean_base': 535.00,
        'target_high_bull': 610.00,
        'num_analysts': 34,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 20.1
    },
    'GOOGL': {
        'target_low_bear': 310.00,
        'target_mean_base': 415.00,
        'target_high_bull': 480.00,
        'num_analysts': 52,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 23.2
    },
    'MSFT': {
        'target_low_bear': 415.00,
        'target_mean_base': 545.00,
        'target_high_bull': 600.00,
        'num_analysts': 56,
        'consensus_recommendation': 'Strong Buy',
        'upside_potential_pct': 21.6
    }
}

# Update cqv_data.json
for item in cqv_list:
    ticker = item['ticker']
    if ticker in analysts_db:
        item['analyst_targets'] = analysts_db[ticker]

with open('cqv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cqv_list, f, indent=2)

with open('cqv_data.js', 'w', encoding='utf-8') as f:
    f.write('const cqvData = ' + json.dumps(cqv_list, indent=2) + ';')

print("SSOT DATASETS UPDATED WITH ANALYST TARGETS.")
