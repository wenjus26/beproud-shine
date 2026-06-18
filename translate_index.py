import os

path = r'C:\Users\user\Downloads\stitch_be_proud_shine_academy\beproud-shine\index.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

reps = {
    "Lead with <span class=\"text-secondary italic\">Confidence</span>, Shine with Purpose.": "Dirigez avec <span class=\"text-secondary italic\">Confiance</span>, Rayonnez avec Sens.",
    "Join an elite network of African women leaders transforming industries through visionary thinking, mentorship, and excellence.": "Rejoignez un cercle intime de femmes africaines inspirantes, transformant le monde par leur bienveillance, leur vision et leur excellence.",
    "Start Your Journey": "Commencer mon voyage",
    "Explore Programs": "Explorer nos univers",
    "Accredited": "Reconnu",
    "Leadership Excellence": "Excellence & Bienveillance",
    "Active Community Members": "Sœurs Épanouies",
    "Empowered Members": "Femmes Épanouies",
    "Expert Mentors": "Mentors Inspirantes",
    "Career Success Rate": "Taux d'Épanouissement",
    "Shine Academy: Your Growth Map": "Académie : Votre Chemin de Croissance",
    "Curated programs designed by global executives to accelerate your professional journey.": "Des programmes conçus avec amour par des leaders mondiales pour nourrir votre voyage professionnel et personnel.",
    "ADVANCED": "AVANCÉ",
    "12-Week Immersion": "Immersion Douce de 12 Semaines",
    "Executive Leadership Mastery": "Maîtrise du Leadership Inspirant",
    "Strategic thinking, emotional intelligence, and board-level presence for senior leaders.": "Pensée stratégique, intelligence émotionnelle et posture bienveillante pour les leaders de demain.",
    "BEGINNER": "INITIATION",
    "8-Week Core": "Socle de 8 Semaines",
    "Emerging Leaders Incubator": "Incubateur des Talents Éclos",
    "Foundational skills in team management, communication, and personal branding.": "Des bases solides en gestion d'équipe, communication douce et affirmation de soi.",
    "ALL LEVELS": "TOUS NIVEAUX",
    "Self-Paced": "À votre rythme",
    "Digital Transformation & Innovation": "Innovation & Transformation Digitale",
    "Navigating the future of work with tech-driven strategies and agile methodologies.": "Naviguer vers l'avenir avec agilité, créativité et des stratégies centrées sur l'humain.",
    "THE GLOBAL FELLOWSHIP 2024": "LE CERCLE GLOBAL 2024",
    "href=\"#\"": "href=\"program-details.html\"" # Just updating some empty links to program details for now
}

for k, v in reps.items():
    c = c.replace(k, v)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print("index.html translated.")
