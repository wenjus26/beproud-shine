import os
import re

directory = r'C:\Users\user\Downloads\stitch_be_proud_shine_academy\beproud-shine'
html_files = ['index.html', 'mentorship.html', 'events.html', 'dashboard.html']

for file in html_files:
    path = os.path.join(directory, file)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace specific casing
    content = content.replace('SHINE LEADERSHIP', 'Be Proud &amp; Shine')
    content = content.replace('Shine Leadership', 'Be Proud &amp; Shine')
    content = content.replace('Shine Academy', 'Be Proud &amp; Shine Academy')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Text replaced successfully.")
