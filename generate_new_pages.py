import os
import re

directory = r'C:\Users\user\Downloads\stitch_be_proud_shine_academy\beproud-shine'
source = os.path.join(directory, 'events.html')

with open(source, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header and footer bounds
header_match = re.search(r'<header.*?</header>\n<!-- Mobile Nav -->.*?</div>\n</div>', content, re.DOTALL)
footer_match = re.search(r'<footer.*?</html>', content, re.DOTALL)

header = content[:header_match.end()] if header_match else ""
footer = content[footer_match.start():] if footer_match else ""

register_body = '''
<main class="pt-32 pb-24 min-h-screen bg-surface-container-lowest">
    <div class="max-w-xl mx-auto px-margin-mobile">
        <div class="glass-card p-10 rounded-3xl shadow-xl border border-primary/10">
            <h1 class="font-display-lg text-primary mb-4 text-center">Rejoindre le Cercle</h1>
            <p class="font-body-md text-on-surface-variant text-center mb-8">Nous sommes tellement heureuses de vous accueillir. Parlez-nous un peu de vous.</p>
            <form class="flex flex-col gap-6">
                <div>
                    <label class="font-label-md text-on-surface-variant mb-2 block">Votre beau prénom</label>
                    <input type="text" class="w-full px-4 py-3 rounded-2xl border border-outline-variant bg-surface-bright focus:ring-2 focus:ring-secondary focus:border-transparent outline-none transition-all" required>
                </div>
                <div>
                    <label class="font-label-md text-on-surface-variant mb-2 block">Adresse email (pour nos doux échanges)</label>
                    <input type="email" class="w-full px-4 py-3 rounded-2xl border border-outline-variant bg-surface-bright focus:ring-2 focus:ring-secondary focus:border-transparent outline-none transition-all" required>
                </div>
                <div>
                    <label class="font-label-md text-on-surface-variant mb-2 block">Qu'est-ce qui vous inspire le plus aujourd'hui ?</label>
                    <textarea class="w-full px-4 py-3 rounded-2xl border border-outline-variant bg-surface-bright focus:ring-2 focus:ring-secondary focus:border-transparent outline-none transition-all min-h-[100px]"></textarea>
                </div>
                <button type="submit" class="w-full primary-gradient-btn shine-effect text-white px-8 py-4 rounded-full font-label-md text-lg mt-4 shadow-xl active:scale-95 transition-transform">
                    Soumettre avec joie
                </button>
            </form>
        </div>
    </div>
</main>
'''

contact_body = '''
<main class="pt-32 pb-24 min-h-screen bg-surface-container-lowest">
    <div class="max-w-4xl mx-auto px-margin-mobile grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
        <div>
            <h1 class="font-display-lg text-primary mb-6">Un petit mot doux ?</h1>
            <p class="font-body-lg text-on-surface-variant mb-8">Que vous souhaitiez devenir partenaire, mentore, ou simplement nous dire bonjour, notre porte (et notre cœur) vous est grande ouverte.</p>
            <div class="flex items-center gap-4 mb-6">
                <div class="w-12 h-12 rounded-full bg-secondary-container flex items-center justify-center">
                    <span class="material-symbols-outlined text-on-secondary-container">mail</span>
                </div>
                <div>
                    <p class="font-label-md text-on-surface-variant">Notre boîte magique</p>
                    <p class="font-headline-md text-primary">bonjour@beproud-shine.org</p>
                </div>
            </div>
        </div>
        <div class="glass-card p-10 rounded-3xl shadow-2xl border border-secondary/20">
            <form class="flex flex-col gap-6">
                <input type="text" placeholder="Votre nom complet" class="w-full px-4 py-3 rounded-2xl border border-outline-variant bg-surface-bright focus:ring-2 focus:ring-secondary outline-none transition-all" required>
                <input type="email" placeholder="Votre email" class="w-full px-4 py-3 rounded-2xl border border-outline-variant bg-surface-bright focus:ring-2 focus:ring-secondary outline-none transition-all" required>
                <textarea placeholder="Votre message bienveillant..." class="w-full px-4 py-3 rounded-2xl border border-outline-variant bg-surface-bright focus:ring-2 focus:ring-secondary outline-none transition-all min-h-[150px]"></textarea>
                <button type="submit" class="w-full primary-gradient-btn shine-effect text-white px-8 py-4 rounded-full font-label-md text-lg shadow-xl active:scale-95 transition-transform">
                    Envoyer avec amour
                </button>
            </form>
        </div>
    </div>
</main>
'''

program_details_body = '''
<main class="pt-32 pb-24 bg-surface-container-lowest">
    <div class="max-w-4xl mx-auto px-margin-mobile">
        <span class="font-label-md text-secondary bg-secondary-container/30 px-4 py-2 rounded-full inline-block mb-6">PROGRAMME PHARE</span>
        <h1 class="font-display-lg text-primary mb-6">Immersion Douce de 12 Semaines</h1>
        <p class="font-body-lg text-on-surface-variant mb-12">Un voyage intérieur et professionnel conçu avec amour pour vous aider à affirmer votre posture, libérer votre voix et diriger avec une profonde intelligence émotionnelle.</p>
        
        <div class="glass-card p-10 rounded-3xl mb-12 shadow-lg">
            <h2 class="font-headline-lg text-primary mb-6">Ce que vous allez vivre</h2>
            <ul class="space-y-4">
                <li class="flex items-start gap-4">
                    <span class="material-symbols-outlined text-secondary mt-1">favorite</span>
                    <p class="font-body-md text-on-surface-variant">Des cercles de parole hebdomadaires intimes et bienveillants.</p>
                </li>
                <li class="flex items-start gap-4">
                    <span class="material-symbols-outlined text-secondary mt-1">psychology</span>
                    <p class="font-body-md text-on-surface-variant">Des ateliers profonds sur la connaissance de soi et le syndrome de l'imposteur.</p>
                </li>
                <li class="flex items-start gap-4">
                    <span class="material-symbols-outlined text-secondary mt-1">trending_up</span>
                    <p class="font-body-md text-on-surface-variant">Un plan de croissance personnalisé co-construit avec votre mentore.</p>
                </li>
            </ul>
        </div>
        
        <div class="text-center">
            <a href="register.html" class="primary-gradient-btn shine-effect text-white px-10 py-5 rounded-full font-label-md text-xl shadow-2xl inline-block active:scale-95 transition-transform">
                Réserver ma place pour le prochain voyage
            </a>
        </div>
    </div>
</main>
'''

files_to_create = {
    'register.html': header + '\n' + register_body + '\n' + footer,
    'contact.html': header + '\n' + contact_body + '\n' + footer,
    'program-details.html': header + '\n' + program_details_body + '\n' + footer,
}

for filename, content in files_to_create.items():
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated new pages successfully.")
