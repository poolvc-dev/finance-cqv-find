import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

for m in re.finditer(r'<script.*?>', html):
    pos = m.start()
    line_no = html[:pos].count('\n') + 1
    snippet = html[max(0, pos-40):min(len(html), pos+100)].replace('\n', ' ')
    print(f"Line {line_no}: {snippet}")
