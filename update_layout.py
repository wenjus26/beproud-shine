import os
import re

directory = r'C:\Users\user\Downloads\stitch_be_proud_shine_academy\beproud-shine'

header_html = '''
<!-- TopAppBar Shell -->
<header class="fixed top-0 w-full z-50 bg-surface/80 backdrop-blur-xl border-b border-white/40 shadow-sm">
<div class="flex justify-between items-center px-margin-mobile md:px-margin-desktop h-20 max-w-max-width mx-auto">
<div class="flex items-center gap-4">
<div class="w-10 h-10 rounded-full overflow-hidden border-2 border-primary/20">
<img class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuC_aVHensOGCjRtx4UImzqs-o7ygBqOKC4gaXwpfj4Okxljn6zXhC4_-3geLu5N-op7K7-c__I0RJVH62_nJNk0kBzWcKfjLaHozujaiBvZyFtAbIJj6MSfjrP3hpufSb-72OSIVcFoO3jJes7hMDdOgPQ_g741g7P4TNPuMTn8WNxgfPGJSlHGj4DdpB-pzn49v_YqJwAEsezBon9jUIE0EjrWHtVtJT28M-pvLVUsOH6kuBRGZ-swUiNUDskiiqDUvYMMKRLdHVSJ"/>
</div>
<span class="font-headline-md text-headline-md font-bold tracking-tight text-primary">Be Proud &amp; Shine</span>
</div>
<!-- Desktop Nav -->
<nav class="hidden md:flex items-center gap-8">
<a class="font-label-md text-label-md text-on-surface-variant hover:text-secondary transition-colors duration-300" href="index.html">Accueil</a>
<a class="font-label-md text-label-md text-on-surface-variant hover:text-secondary transition-colors duration-300" href="mentorship.html">Mentorat</a>
<a class="font-label-md text-label-md text-on-surface-variant hover:text-secondary transition-colors duration-300" href="events.html">Événements</a>
<a class="font-label-md text-label-md text-on-surface-variant hover:text-secondary transition-colors duration-300" href="dashboard.html">Mon Espace</a>
<a class="font-label-md text-label-md text-on-surface-variant hover:text-secondary transition-colors duration-300" href="contact.html">Contact</a>
</nav>
<div class="flex items-center gap-4">
<button class="p-2 text-on-surface-variant hover:text-primary transition-colors active:scale-95">
<span class="material-symbols-outlined">notifications</span>
</button>
<a href="register.html" class="primary-gradient-btn shine-effect text-white px-6 py-2 rounded-full font-label-md hidden md:block text-center">
    Rejoindre le Cercle
</a>
<button id="mobile-menu-btn" class="md:hidden p-3 text-on-surface-variant hover:bg-surface-container-high rounded-full transition-colors">
<span class="material-symbols-outlined">menu</span>
</button>
</div>
</div>
</header>
<!-- Mobile Nav -->
<div id="mobile-menu" class="hidden md:hidden fixed inset-0 top-20 bg-surface/95 backdrop-blur-2xl z-40 overflow-y-auto pb-20 border-t border-outline-variant/20 shadow-2xl">
    <div class="flex flex-col p-8 gap-8 text-center mt-4">
        <a class="font-headline-md text-primary font-bold" href="index.html">Accueil</a>
        <a class="font-headline-md text-on-surface-variant hover:text-secondary transition-colors" href="mentorship.html">Mentorat</a>
        <a class="font-headline-md text-on-surface-variant hover:text-secondary transition-colors" href="events.html">Événements</a>
        <a class="font-headline-md text-on-surface-variant hover:text-secondary transition-colors" href="dashboard.html">Mon Espace</a>
        <a class="font-headline-md text-on-surface-variant hover:text-secondary transition-colors" href="contact.html">Nous Contacter</a>
        <a href="register.html" class="primary-gradient-btn shine-effect text-white px-8 py-4 rounded-full font-label-md mt-4 mx-auto w-full max-w-sm shadow-xl block text-center">
            Rejoindre le Cercle
        </a>
    </div>
</div>
'''

footer_html = '''
<footer class="bg-surface-container-low pt-24 pb-12 mt-auto">
<div class="max-w-max-width mx-auto px-margin-mobile md:px-margin-desktop">
<div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-16">
<div class="md:col-span-1">
<span class="font-headline-md text-primary font-bold tracking-tight mb-6 block">Be Proud &amp; Shine</span>
<p class="font-body-md text-on-surface-variant mb-6">Élever la voix des femmes africaines par l'excellence, la sororité, et un leadership bienveillant et inspirant.</p>
</div>
<div>
<h4 class="font-label-md text-primary mb-6 uppercase tracking-wider">Ressources</h4>
<ul class="space-y-4 font-body-md text-on-surface-variant">
<li><a class="hover:text-secondary transition-colors" href="program-details.html">Formations</a></li>
<li><a class="hover:text-secondary transition-colors" href="mentorship.html">Mentorat</a></li>
<li><a class="hover:text-secondary transition-colors" href="events.html">Agenda</a></li>
<li><a class="hover:text-secondary transition-colors" href="dashboard.html">Espace Membre</a></li>
</ul>
</div>
<div>
<h4 class="font-label-md text-primary mb-6 uppercase tracking-wider">Lien direct</h4>
<ul class="space-y-4 font-body-md text-on-surface-variant">
<li><a class="hover:text-secondary transition-colors" href="contact.html">Nous écrire</a></li>
<li><a class="hover:text-secondary transition-colors" href="#">Instagram</a></li>
<li><a class="hover:text-secondary transition-colors" href="#">LinkedIn</a></li>
<li><a class="hover:text-secondary transition-colors" href="#">Podcast</a></li>
</ul>
</div>
<div class="md:col-span-1">
<h4 class="font-label-md text-primary mb-6 uppercase tracking-wider">Restons connectées</h4>
<p class="font-body-md text-on-surface-variant mb-4">Inscrivez-vous à notre newsletter pour recevoir notre dose d'inspiration hebdomadaire.</p>
<form class="flex flex-col gap-3">
    <input type="email" placeholder="Votre adresse douce@email.com" class="w-full px-4 py-3 rounded-2xl border-none bg-white shadow-sm focus:ring-2 focus:ring-secondary text-on-surface" required>
    <button type="submit" class="w-full primary-gradient-btn text-white px-4 py-3 rounded-2xl font-label-md shadow-md hover:shadow-lg transition-all">S'épanouir avec nous</button>
</form>
</div>
</div>
<div class="flex flex-col md:flex-row justify-between items-center pt-8 border-t border-outline-variant/20 text-[12px] font-label-md text-on-surface-variant opacity-60">
<p>© 2024 Be Proud &amp; Shine. Tous droits réservés avec amour.</p>
<div class="flex gap-6 mt-4 md:mt-0">
<a href="#" class="hover:text-primary">Politique de confidentialité</a>
<a href="#" class="hover:text-primary">Conditions générales</a>
</div>
</div>
</div>
</footer>
'''

html_files = ['index.html', 'mentorship.html', 'events.html', 'dashboard.html']

for file in html_files:
    path = os.path.join(directory, file)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract everything from <body> to <header>
    # Actually, we replace everything between <header> and </header>
    content = re.sub(r'<header.*?</header>', header_html, content, flags=re.DOTALL)
    
    # Replace Mobile Nav if it exists
    content = re.sub(r'<!-- Mobile Nav -->.*?</div>\n</div>', '', content, flags=re.DOTALL)
    
    # Replace footer
    content = re.sub(r'<footer.*?</footer>', footer_html, content, flags=re.DOTALL)

    # Some general soft translations for buttons globally:
    content = content.replace('Join Network', 'Rejoindre le Cercle')
    content = content.replace('Enroll Now', 'M\'inscrire avec joie')
    content = content.replace('View All Programs', 'Découvrir nos pépites')
    content = content.replace('Course Details', 'Voir les détails')
    content = content.replace('Register Now', 'Réserver ma place')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Base layout translations and structures applied.")
