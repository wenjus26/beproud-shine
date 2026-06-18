import os
import glob

directory = r'C:\Users\user\Downloads\stitch_be_proud_shine_academy\beproud-shine'
html_files = glob.glob(os.path.join(directory, '*.html'))

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the copyright text
    content = content.replace('© 2024 Be Proud &amp; Shine. Tous droits réservés avec amour.', '© 2026 Tous droits réservés par REJUSTE WENOUMI.')
    content = content.replace('© 2024 Be Proud & Shine. All Rights Reserved.', '© 2026 Tous droits réservés par REJUSTE WENOUMI.')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Copyright updated.")
