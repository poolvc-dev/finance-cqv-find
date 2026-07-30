import json
import os
import re

# Update MSFT report to v4.0
with open('inform/msft_2026_q2.md', 'r', encoding='utf-8') as f:
    msft_doc = f.read()

msft_doc = msft_doc.replace('CQV v3.0 (Quality and Structural Value)', 'CQV v4.0 (Quality, Resilience and Value)')
msft_doc = msft_doc.replace('CQV v3.0', 'CQV v4.0')
msft_doc = msft_doc.replace('CQV v3.0 FINAL', 'CQV v4.0 FINAL')

with open('inform/msft_2026_q2.md', 'w', encoding='utf-8') as f:
    f.write(msft_doc)

# Update FTNT report to v4.0
with open('inform/ftnt_2026_q2.md', 'r', encoding='utf-8') as f:
    ftnt_doc = f.read()

ftnt_doc = ftnt_doc.replace('CQV v3.0 (Quality and Structural Value)', 'CQV v4.0 (Quality, Resilience and Value)')
ftnt_doc = ftnt_doc.replace('9.48/10 (ÉLITE)', '9.53/10 (ÉLITE)')
ftnt_doc = ftnt_doc.replace('9.480', '9.530')
ftnt_doc = ftnt_doc.replace('CQV v3.0', 'CQV v4.0')

with open('inform/ftnt_2026_q2.md', 'w', encoding='utf-8') as f:
    f.write(ftnt_doc)

# Update GOOGL report to v4.0 if present
if os.path.exists('inform/googl_2026_q2.md'):
    with open('inform/googl_2026_q2.md', 'r', encoding='utf-8') as f:
        g_doc = f.read()
    g_doc = g_doc.replace('CQV v3.0', 'CQV v4.0')
    g_doc = g_doc.replace('9.41', '9.41')
    with open('inform/googl_2026_q2.md', 'w', encoding='utf-8') as f:
        f.write(g_doc)

# Update META report to v4.0
if os.path.exists('inform/meta_2026_q2.md'):
    with open('inform/meta_2026_q2.md', 'r', encoding='utf-8') as f:
        m_doc = f.read()
    m_doc = m_doc.replace('CQV v3.0', 'CQV v4.0')
    m_doc = m_doc.replace('9.37', '9.16')
    with open('inform/meta_2026_q2.md', 'w', encoding='utf-8') as f:
        f.write(m_doc)

# Update ORLY report to v4.0
if os.path.exists('inform/orly_2026_q2.md'):
    with open('inform/orly_2026_q2.md', 'r', encoding='utf-8') as f:
        o_doc = f.read()
    o_doc = o_doc.replace('CQV v3.0', 'CQV v4.0')
    o_doc = o_doc.replace('9.20', '9.18')
    with open('inform/orly_2026_q2.md', 'w', encoding='utf-8') as f:
        f.write(o_doc)

print("UPDATED_INVESTMENT_REPORTS_TO_CQV_V4_SUCCESSFULLY")
