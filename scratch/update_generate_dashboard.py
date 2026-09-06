with open('generate_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update thesis directory loading to prioritize inform/cqv_v5
old_theses_block = """        inform_dir = 'inform'
        if os.path.exists(inform_dir):
            for fn in os.listdir(inform_dir):
                if fn.endswith('.md') and fn != 'template.md':
                    base_key = fn.replace('.md', '').upper()
                    ticker = base_key.split('_')[0]
                    with open(os.path.join(inform_dir, fn), 'r', encoding='utf-8') as tf:
                        content = tf.read()
                        theses_dict[base_key] = content
                        if ticker not in theses_dict:
                            theses_dict[ticker] = content"""

new_theses_block = """        # Load theses from inform/cqv_v5 and inform
        dirs_to_check = ['inform/cqv_v5', 'inform']
        for d in dirs_to_check:
            if os.path.exists(d):
                for fn in os.listdir(d):
                    if fn.endswith('.md') and fn != 'template.md':
                        base_key = fn.replace('.md', '').upper()
                        ticker = base_key.split('_')[0]
                        with open(os.path.join(d, fn), 'r', encoding='utf-8') as tf:
                            content = tf.read()
                            theses_dict[base_key] = content
                            if ticker not in theses_dict:
                                theses_dict[ticker] = content"""

if old_theses_block in text:
    text = text.replace(old_theses_block, new_theses_block)

# 2. Update all v4 titles and labels to v5
text = text.replace('CQV Financial Dashboard v4.0 / v5.0', 'CQV Financial Dashboard v5.0')
text = text.replace('CQV Financial Dashboard v4.0', 'CQV Financial Dashboard v5.0')
text = text.replace('Quality & Structural Value Model v4.0 / v5.0', 'Quality & Structural Value Model v5.0')
text = text.replace('Quality & Structural Value Model v4.0', 'Quality & Structural Value Model v5.0')
text = text.replace('Dataset SSOT Auditado v4.0', 'Dataset SSOT Auditado v5.0')
text = text.replace('Score CQV v4.0 ≥ 9.50', 'Score CQV v5.0 ≥ 9.50')
text = text.replace('Score CQV v4.0 (9.00 - 9.49)', 'Score CQV v5.0 (9.00 - 9.49)')
text = text.replace('Score CQV Calidad v4.0', 'Score CQV Calidad v5.0')
text = text.replace('CQV Calidad v4.0: Suma ponderada', 'CQV Calidad v5.0: Suma ponderada')
text = text.replace('CQV Calidad v4.0', 'CQV Calidad v5.0')
text = text.replace('<th>CQV v4.0</th>', '<th>CQV v5.0</th>')
text = text.replace("label: 'Score CQV v4.0'", "label: 'Score CQV v5.0'")
text = text.replace('CQV Financial Platform v4.0', 'CQV Financial Platform v5.0')

# 3. Update active snapshot and row fields
text = text.replace('activeQuarterSnapshot.cqv_v4', 'activeQuarterSnapshot.cqv_v5 || activeQuarterSnapshot.cqv')
text = text.replace('formatScore(qRow.cqv_v4)', 'formatScore(qRow.cqv_v5 || qRow.cqv)')
text = text.replace('getTierInfo(qRow.cqv_v4)', 'getTierInfo(qRow.cqv_v5 || qRow.cqv)')

# 4. Update quarterlyBreakdownRows to iterate over P4, P3, P2, P1
text = text.replace("['Q4', 'Q3', 'Q2', 'Q1']", "['P4', 'P3', 'P2', 'P1']")
text = text.replace("yrObj[q].cqv_v4 !== undefined", "yrObj[q].cqv_v5 !== undefined")
text = text.replace("cqv_v4: c.cqv", "cqv_v5: c.cqv_v5 || c.cqv")
text = text.replace("Trimestres (Q1, Q2, Q3, Q4)", "Periodos (P1, P2, P3, P4)")

with open('generate_dashboard.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated generate_dashboard.py successfully.')
