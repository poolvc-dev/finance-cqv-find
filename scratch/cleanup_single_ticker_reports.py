import os, re

inform_dir = 'inform'
all_files = os.listdir(inform_dir)

pattern = r'^[A-Za-z0-9\.-]+_\d{4}_Q[1-4]\.md$'
deleted_count = 0

for fn in all_files:
    if not fn.endswith('.md') or fn == 'template.md':
        continue
    if not re.match(pattern, fn, re.IGNORECASE):
        file_path = os.path.join(inform_dir, fn)
        os.remove(file_path)
        deleted_count += 1

print(f"Successfully deleted {deleted_count} non-standard single-ticker Markdown files from inform/!")
