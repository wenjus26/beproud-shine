import os
import re

reps = {
    "Discover your potential through guided mentorship from industry leaders.": "Révélez votre potentiel grâce à l'accompagnement bienveillant de nos mentores.",
    "Find a Mentor": "Trouver ma Mentore",
    "Become a Mentor": "Devenir Mentore",
    "Our Mentorship Approach": "Notre Approche du Mentorat",
    "We believe in transformative connections. Our mentorship program matches aspiring leaders with seasoned executives for a 6-month journey of growth, strategic guidance, and empowerment.": "Nous croyons aux rencontres qui transforment. Notre programme vous met en relation avec des dirigeantes inspirantes pour 6 mois d'évolution, de conseils stratégiques et d'épanouissement.",
    "Personalized Matching": "Un Jumelage Sur-Mesure",
    "Algorithm-driven and human-verified matching to ensure aligned goals and values.": "Un jumelage attentif, basé sur vos valeurs profondes et vos aspirations.",
    "Structured Framework": "Un Cadre Sécurisant",
    "Monthly milestones, guided reflection templates, and clear progression paths.": "Des étapes mensuelles, des espaces de réflexion et un cheminement tout en douceur.",
    "Exclusive Community": "Une Sororité Exclusive",
    "Access to private masterclasses and peer-to-peer networking events.": "Accès à des cercles privés et des événements de partage entre sœurs.",
    "Featured Mentors": "Nos Mentores Inspirantes",
    "Learn from women who have shattered glass ceilings.": "Apprenez auprès de femmes qui ouvrent la voie avec audace et humanité.",
    "Tech Innovation Lead": "Leader en Innovation Tech",
    "Global Finance Director": "Directrice Financière Globale",
    "Social Impact Founder": "Fondatrice à Impact Social",
    "Availability:": "Disponibilité :",
    "2 Spots Left": "2 places disponibles",
    "Full": "Complet",
    "1 Spot Left": "1 place disponible",
    "Request Mentorship": "Demander un Mentorat",
    "Success Stories": "Leurs Belles Histoires",
    "The mentorship program was a turning point. My mentor didn't just give advice; she helped me find my own voice and confidence to step into a C-level role.": "Ce mentorat a été une révélation. Ma mentore m'a aidée à trouver ma propre voix et la confiance nécessaire pour briller.",
    "Upcoming Events & Masterclasses": "Nos Prochains Événements",
    "Connect, learn, and grow with our vibrant community.": "Connectez-vous, apprenez et grandissez avec notre belle communauté.",
    "Filter by:": "Filtrer par :",
    "All Events": "Tous",
    "Workshops": "Ateliers",
    "Networking": "Rencontres",
    "Virtual": "En ligne",
    "In-Person": "Présentiel",
    "Featured Event": "Événement Phare",
    "Annual African Women in Tech Summit": "Sommet Annuel des Femmes dans la Tech",
    "Nairobi, Kenya + Virtual": "Nairobi, Kenya + En ligne",
    "Join 500+ leaders for 2 days of keynotes, panels, and intense networking focused on AI, sustainability, and funding for female founders.": "Rejoignez 500+ leaders pour 2 jours d'inspiration, centrés sur l'IA, l'impact positif et le financement au féminin.",
    "Speakers": "Intervenantes",
    "Register for Summit": "Réserver ma place",
    "More Upcoming Events": "Plus d'Événements Doux",
    "Masterclass: Negotiation Strategies for Executives": "Masterclass : L'Art de la Négociation Douce",
    "Virtual (Zoom)": "En Ligne (Zoom)",
    "Learn frameworks to advocate for your worth and close high-stakes deals.": "Découvrez comment valoriser votre potentiel et négocier avec cœur et assurance.",
    "Register": "M'inscrire",
    "Founders Networking Breakfast": "Petit-Déjeuner des Fondatrices",
    "Lagos, Nigeria": "Lagos, Nigeria",
    "An intimate morning of connections for early-stage startup founders.": "Une matinée intime et chaleureuse pour les fondatrices de startups.",
    "Welcome back,": "Heureuse de vous revoir,",
    "Your Dashboard": "Votre Cocon Personnel",
    "Track your progress, access resources, and connect with your cohort.": "Suivez votre évolution, accédez à vos ressources et connectez-vous avec vos sœurs.",
    "Complete Profile": "Compléter mon profil",
    "View Profile": "Voir mon profil",
    "Current Program Focus": "Votre Programme Actuel",
    "Week 4: Emotional Intelligence in Leadership": "Semaine 4 : Intelligence Émotionnelle",
    "Resume Learning": "Reprendre l'apprentissage",
    "Your Mentorship": "Votre Mentorat",
    "Next Session: Strategic Planning": "Prochaine séance : Vision Stratégique",
    "Prepare Notes": "Préparer mes notes",
    "Upcoming Cohort Meetup": "Prochaine rencontre",
    "Virtual Coffee Chat - Group A": "Café Virtuel - Groupe A",
    "Join Call": "Rejoindre l'appel",
    "Your Growth Metrics": "Vos Belles Victoires",
    "Modules Completed": "Modules Complétés",
    "Keep it up!": "Continuez ainsi !",
    "Connections Made": "Belles Rencontres",
    "Network expanding": "Votre cercle s'agrandit",
    "Action Items Completed": "Actions Réalisées",
    "On track": "Sur la bonne voie",
    "Recommended Resources": "Ressources Douces Recommandées",
    "Curated for your current journey stage.": "Sélectionnées avec soin pour vous accompagner.",
    "Read Article": "Lire l'article",
    "Listen": "Écouter"
}

html_files = [
    r'C:\Users\user\Downloads\stitch_be_proud_shine_academy\beproud-shine\mentorship.html',
    r'C:\Users\user\Downloads\stitch_be_proud_shine_academy\beproud-shine\events.html',
    r'C:\Users\user\Downloads\stitch_be_proud_shine_academy\beproud-shine\dashboard.html'
]

for path in html_files:
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    for k, v in reps.items():
        c = c.replace(k, v)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

print("Mentorship, events, dashboard translated.")
