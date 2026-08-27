import os

inform_dir = 'inform'
files = os.listdir(inform_dir)

renamed = 0
for f in files:
    if f.endswith('_2026_q2.md') or f.endswith('_2026_Q2.md'):
        prefix = f.split('_')[0].upper()
        new_name = f"{prefix}_2026_Q2.md"
        if f != new_name:
            old_path = os.path.join(inform_dir, f)
            tmp_path = os.path.join(inform_dir, f + ".tmp")
            target_path = os.path.join(inform_dir, new_name)
            os.rename(old_path, tmp_path)
            os.rename(tmp_path, target_path)
            renamed += 1

print(f"Renamed {renamed} files to UPPERCASE format.")
