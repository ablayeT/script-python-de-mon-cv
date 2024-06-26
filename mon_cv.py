from rich.console import Console
from rich.table import Table
from rich.text import Text

# Initialisation de Rich
console = Console()

# Création de la table principale avec des lignes de séparation visibles
table = Table(expand=True, show_lines=True)

# Ajout des colonnes pour la table principale
table.add_column("Section", justify="left", style="bold cyan")
table.add_column("Contenu", justify="left")

# Construction du contenu avec des styles sélectifs pour les compétences
content_text = Text()
content_text.append("Langages informatiques: ", style="black on white underline")
content_text.append("HTML/CSS, Javascript, React,Node JS, Express, MongoDB, MySQL, Python, PHP\n")
content_text.append("Savoir-faire: ", style="black on white underline")
content_text.append("autonomie, rigueur, discrétion,curiosié, résolution de problèmes")

# Ajout des données pour la table principale
sections = [
    ("Informations de contact", "Nom: Abdoulaye\nPrénom: Toure\nEmail: ablayetoure2014@gmail.com\nTéléphone: 0644932627"),
    ("Soft-skills", content_text),
    ("Langues parlées", "Anglais (courant), Espagnol (intermédiaire), Wolof (courant)"),
    ("Centres d'intérêts", "Taekwondo, Baseball, Course à pieds, Lecture")
]

# Ajout des données pour chaque section dans la table principale
for section, contenu in sections:
    table.add_row(section, contenu)

# Ajouter un titre de section pour expériences et formations, avec texte en orange foncé
exp_form_title = Text("Expériences professionnelles & Formation", style="bold #FF8C00")
# Appliquer un fond blanc uniquement à la deuxième colonne
table.add_row(exp_form_title, Text("", style="on white"))

# Construction du contenu pour 'Expériences professionnelles'
exp_text = Text()
exp_text.append("→Développeurweb eet web mobile -  Entourage--0ct2022-Nov2023b\n")
exp_text.append("→Fondateur et gérant d'un commerc - Toure_multiservices - Mai2017-Nov2019l\n")
exp_text.append("→Professeur d'anglai -  Barnes_English_centeer - Sept2017 - Nov2019")

# Construction du contenu pour 'Formation'
form_text = Text()
form_text.append("→Développeur web et web mobileX -WEBFOREC,Paris\n")
form_text.append("→Développeur intégrateur webY -OPENCLASSROOM, Paris\n")
form_text.append("→Master II: Littérature et civilisation américaine et caribéeeneZ -UCAD, Dakar, SENEGAL\n")

# Ajout des expériences professionnelles et formations
table.add_row("Expériences professionnelles", exp_text)
table.add_row("Formation", form_text)

# Affichage de la table
console.print(table)

