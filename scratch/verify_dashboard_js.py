import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check populateHistoryCompanySelect in dashboard.html
pos1 = html.find('function populateHistoryCompanySelect()')
if pos1 != -1:
    print("Found populateHistoryCompanySelect block:")
    print(html[pos1:pos1+600])

pos2 = html.find('function switchTab(tabId)')
if pos2 != -1:
    print("\nFound switchTab block:")
    print(html[pos2:pos2+700])
