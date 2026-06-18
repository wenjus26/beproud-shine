import os
import re

directory = r'C:\Users\user\Downloads\stitch_be_proud_shine_academy\beproud-shine'
index_path = os.path.join(directory, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need everything from start up to the end of <header> and the Mobile Nav.
# We'll split the content string based on '<main' to get the exact top part,
# because <main> comes right after the header and mobile nav.
top_part = content.split('<main')[0]

# For the bottom part, we want everything from <footer to the end.
bottom_part = '<footer' + content.split('<footer')[1]

broken_files = ['contact.html', 'register.html', 'program-details.html', 'privacy.html', 'terms.html']

for file in broken_files:
    path = os.path.join(directory, file)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        broken_content = f.read()

    # Extract just the <main>...</main> part from the broken file
    main_match = re.search(r'<main.*?</main>', broken_content, re.DOTALL)
    if main_match:
        main_part = main_match.group(0)
    else:
        print(f"Warning: No main tag found in {file}")
        continue

    # Reconstruct the file properly
    fixed_content = top_part + main_part + '\n' + bottom_part

    with open(path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

print("Fixed broken HTML pages by injecting proper head, header, footer, and JS.")
