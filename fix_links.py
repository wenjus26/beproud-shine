import os
import glob
import re

directory = r'C:\Users\user\Downloads\stitch_be_proud_shine_academy\beproud-shine'

# Create Privacy and Terms pages using contact.html as a template
with open(os.path.join(directory, 'contact.html'), 'r', encoding='utf-8') as f:
    contact_content = f.read()

header_match = re.search(r'<header.*?</header>\n<!-- Mobile Nav -->.*?</div>\n</div>', contact_content, re.DOTALL)
footer_match = re.search(r'<footer.*?</html>', contact_content, re.DOTALL)

header = contact_content[:header_match.end()] if header_match else ""
footer = contact_content[footer_match.start():] if footer_match else ""

privacy_body = '''
<main class="pt-32 pb-24 min-h-screen bg-surface-container-lowest">
    <div class="max-w-4xl mx-auto px-margin-mobile">
        <h1 class="font-display-lg text-primary mb-6">Politique de Confidentialité</h1>
        <div class="glass-card p-10 rounded-3xl shadow-lg border border-outline-variant/30 text-on-surface-variant font-body-lg space-y-6">
            <p>Chez <strong>Be Proud &amp; Shine</strong>, nous accordons une importance primordiale à la protection de vos données personnelles et à votre intimité.</p>
            <h2 class="font-headline-md text-primary mt-8">1. Collecte des données</h2>
            <p>Nous collectons les informations que vous nous confiez volontairement (nom, prénom, email) dans le seul but de vous offrir une expérience chaleureuse et personnalisée au sein de notre communauté.</p>
            <h2 class="font-headline-md text-primary mt-8">2. Utilisation bienveillante</h2>
            <p>Vos données ne seront jamais vendues. Elles servent uniquement à vous envoyer des nouvelles douces et à gérer votre parcours d'apprentissage.</p>
            <h2 class="font-headline-md text-primary mt-8">3. Vos droits</h2>
            <p>Vous avez le plein pouvoir sur vos informations. Vous pouvez à tout moment nous demander de les modifier ou de les effacer en nous écrivant à <em>bonjour@beproud-shine.org</em>.</p>
        </div>
    </div>
</main>
'''

terms_body = '''
<main class="pt-32 pb-24 min-h-screen bg-surface-container-lowest">
    <div class="max-w-4xl mx-auto px-margin-mobile">
        <h1 class="font-display-lg text-primary mb-6">Conditions Générales</h1>
        <div class="glass-card p-10 rounded-3xl shadow-lg border border-outline-variant/30 text-on-surface-variant font-body-lg space-y-6">
            <p>Bienvenue dans la communauté <strong>Be Proud &amp; Shine</strong>. En naviguant sur ce site, vous acceptez nos conditions d'utilisation, fondées sur le respect, la bienveillance et la sororité.</p>
            <h2 class="font-headline-md text-primary mt-8">1. Comportement et Respect</h2>
            <p>Notre espace est un lieu sûr. Tout comportement irrespectueux entraînera une exclusion immédiate. Nous cultivons l'entraide et l'écoute.</p>
            <h2 class="font-headline-md text-primary mt-8">2. Propriété Intellectuelle</h2>
            <p>Le contenu de nos programmes, articles et fiches est créé avec amour. Il reste la propriété exclusive de Be Proud &amp; Shine et ne peut être partagé sans notre accord doux mais ferme.</p>
            <h2 class="font-headline-md text-primary mt-8">3. Engagements</h2>
            <p>En rejoignant un de nos programmes, vous vous engagez à y participer avec le cœur ouvert et la volonté de grandir.</p>
        </div>
    </div>
</main>
'''

with open(os.path.join(directory, 'privacy.html'), 'w', encoding='utf-8') as f:
    f.write(header + '\n' + privacy_body + '\n' + footer)

with open(os.path.join(directory, 'terms.html'), 'w', encoding='utf-8') as f:
    f.write(header + '\n' + terms_body + '\n' + footer)

# Now replace all href="#" in all html files
html_files = glob.glob(os.path.join(directory, '*.html'))

replacements = [
    (r'<a([^>]*)href="#"([^>]*)>Instagram</a>', r'<a\1href="https://instagram.com/beproudshine"\2>Instagram</a>'),
    (r'<a([^>]*)href="#"([^>]*)>LinkedIn</a>', r'<a\1href="https://linkedin.com/company/beproudshine"\2>LinkedIn</a>'),
    (r'<a([^>]*)href="#"([^>]*)>Podcast</a>', r'<a\1href="https://spotify.com"\2>Podcast</a>'),
    (r'<a([^>]*)href="#"([^>]*)>Politique de confidentialité</a>', r'<a\1href="privacy.html"\2>Politique de confidentialité</a>'),
    (r'<a([^>]*)href="#"([^>]*)>Politique de confidentialit.</a>', r'<a\1href="privacy.html"\2>Politique de confidentialité</a>'),
    (r'<a([^>]*)href="#"([^>]*)>Conditions générales</a>', r'<a\1href="terms.html"\2>Conditions générales</a>'),
    (r'<a([^>]*)href="#"([^>]*)>Conditions g.n.rales</a>', r'<a\1href="terms.html"\2>Conditions générales</a>'),
    # Catch-all remaining simple ones:
    # Just replace all remaining href="#" with href="index.html" to avoid broken links
    (r'href="#"', r'href="index.html"')
]

for path in html_files:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    for pat, rep in replacements:
        c = re.sub(pat, rep, c)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

print("Created privacy and terms pages, and resolved all empty # links.")
