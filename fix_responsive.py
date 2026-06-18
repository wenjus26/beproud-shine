import os
import re

directory = r'C:\Users\user\Downloads\stitch_be_proud_shine_academy\beproud-shine'
html_files = ['index.html', 'mentorship.html', 'events.html', 'dashboard.html']

mobile_menu_html = '''
<!-- Mobile Nav -->
<div id="mobile-menu" class="hidden md:hidden fixed inset-0 top-20 bg-surface/95 backdrop-blur-2xl z-40 overflow-y-auto pb-20 border-t border-outline-variant/20 shadow-2xl">
    <div class="flex flex-col p-8 gap-8 text-center mt-4">
        <a class="font-headline-md text-primary font-bold" href="index.html">Home</a>
        <a class="font-headline-md text-on-surface-variant hover:text-secondary transition-colors" href="mentorship.html">Mentorship</a>
        <a class="font-headline-md text-on-surface-variant hover:text-secondary transition-colors" href="events.html">Events</a>
        <a class="font-headline-md text-on-surface-variant hover:text-secondary transition-colors" href="dashboard.html">Dashboard</a>
        <button class="primary-gradient-btn shine-effect text-white px-8 py-4 rounded-full font-label-md mt-4 mx-auto w-full max-w-sm shadow-xl">
            Join Network
        </button>
    </div>
</div>
'''

js_code = '''
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        if (mobileMenuBtn && mobileMenu) {
            mobileMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
                const icon = mobileMenuBtn.querySelector('.material-symbols-outlined');
                if(mobileMenu.classList.contains('hidden')){
                    icon.textContent = 'menu';
                } else {
                    icon.textContent = 'close';
                }
            });
        }
    });
</script>
'''

for file in html_files:
    path = os.path.join(directory, file)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Increase mobile margin for a softer feel
    content = content.replace('\"margin-mobile\": \"16px\"', '\"margin-mobile\": \"24px\"')
    
    # Add id and soft hover effect to hamburger
    content = re.sub(
        r'<button class=\"md:hidden[^\"]*\">',
        '<button id=\"mobile-menu-btn\" class=\"md:hidden p-3 text-on-surface-variant hover:bg-surface-container-high rounded-full transition-colors\">',
        content
    )

    # Insert mobile menu HTML after </header>
    if '<div id=\"mobile-menu\"' not in content:
        content = content.replace('</header>', '</header>\n' + mobile_menu_html)
    
    # Insert JS right before </body>
    if 'mobileMenuBtn' not in content:
        content = content.replace('</body>', js_code + '\n</body>')

    # Additional soft design adjustments: slightly more rounding on cards
    content = content.replace('rounded-[2rem]', 'rounded-[2.5rem]')
    content = content.replace('rounded-2xl', 'rounded-3xl')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Modification done.")
