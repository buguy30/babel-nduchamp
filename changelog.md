17/12/2019
---------------------------------------------------------------
- Algorythme chaine de caractère "<Firstname> <Middle> <Lastname>
fullname avec input()
- Dictionnaire est une liste de key/values définit via {}
Le dictionnaire ne possède pas de tri
- Import de modules : sys, os
- Fonction print avec f"{variable}"
                       "{}.format(variable)
- Fonction split : séparation chaine de caractère par un séparateur, par défaut " " (espace)
- Type(a) premet de saisir la classe,
inistance (a,class)
objet de classe int, string, booléan, dict, list, def():
- Opérateurs = assigné
< >
+, *
- Regex - Expressions régulières
- Install Python 3.8
_______________________________________________________________


18/12/2019
---------------------------------------------------------------
- Test unitaire dont assertEqual
- Try, Exception
- Git, Github
- Fonctions avec des dates dont calcul entre 2 dates
- MVC - Design Patterns sur traitement d'une classe et de son  affichage avec un controller
- Syntaxe du while
- Tester la classe d'un objet isintance (a, class)
- Readme.md en format markdown
_______________________________________________________________


19/12/2019
---------------------------------------------------------------
- package BeautifulSoup : 
    vient de pypi.org - installé avec pip
    -> outil de scraping : récupère les contenus du web
    -> format HTML en entrée
        -> analyse le DOM (Document Object Model)
        -> organise les balises HTML en un arbre
        -> soup.title
        -> soup.findall (H1, class, p, id...)
- débuguer :
    -> script exécuté sous windows, accès autorisé
    -> enlever le warning W291 (mettre un \n en fin de pose) chez Flake8 -> Lint
- Pipenv -> VirtualEnvironnement
    -> environnement Python "propre" (version précise) = version downloadable de Python.org
    -> répertoire de stockage de votre environnement se trouve dans /user/utilisateur...
    -> Pipfile : version humaine
    -> Pipfile.lock : version machine
    -> connecté à pypi.org
- Consulter les sources opensource de python dont datetime.py
    \python38\lib\...
- Package request
    HTTP get url...
- Blake -> aide à la réindentation et à la cosmétique, la lisibilité du code Format
__________________________________________________________________


20/12/2019
------------------------------------------------------------------
- Django 2h :
    - create superuser admin :  ~ authentification
                                ~ crud
                                ~ model (bdd)
    - create user
    - settings.py (config Django)
    - view home : affiche contenu json checkurl
        py def home() -> url
    - template home.html
__________________________________________________________________


07/01/2020
------------------------------------------------------------------
Construction interface backoffice pour la gestion du catalogue d'une médiathèque
Fichiers : admin.py, models.py
- Algorithme tuple
- Modèle BDD
    -> définition ORM des champs et relations dans SQL table
    -> propriétés, attributs, variables
    -> fonctions préalables héritées de la classe models.Model
    -> nos fonctions
- images
- amélioration interface-utilisateur et de l'existence utilisateur
        -> admin table Publication, Author, Dewey
        -> aide à la saisie
- architecture
    -> besoin du client
    -> expression schéma utilisateur (2 persona)
    -> nomenclature code et entreprise
    -> objet
- Dewey :
    -> classement niveau 2 (800 catégories)
    besoin d'un fichier csv ou xls
    -> code couleur
- Publication
    -> ISBN
    -> Statut (emprunté, disponible)
        Intégration au système existant
__________________________________________________________________


08/01/2020
------------------------------------------------------------------
- Algorithme pour déterminer le siècle en fonction d'une date
- BDD : modèle de l'application, catalogue : (makemigrations, migrate)
    - Dewey
    - Author
    - Publication
- Author ajout de la fonction siècle
- Dewey : fonction pour le code couleur du classement
- Saisie formulaire :
    - réflexion sur les choix à prendre sur les fonctionalités à intégrer
        - parfois des dév spécifiques s'évitent par formation/accompagnement de l'utilisation final
        - retour de l'expérience métier, permet de corriger ou orienter le dév
        - regrouper en temps 1,2,3 les dév 
- Admin formulaire = définition d'un modèle (table)
- Admin regrouper en section zone de saisie
__________________________________________________________________


09/01/2020
------------------------------------------------------------------
- Algo pour récupérer les données via la techno de scrapping html à à partir d'une URL :
    - titre
    - meta description du <head>
    - image meta opengraph
    - url
- Django html : création d'un composant html pour afficher les données liste de scrap url
- Settings Django
    - Media : transfert de fichier, d'image dit utilisateur, file upload
    - Static : 
        - CSS, js, font, jpg
        - ressources statique de l'application
        - accès public
 - Eléments html -> interface utilisateur
 - Traduction des libellés d'anglais à français sur les formulaires (auteur, publication, dewey)
 - Fonction couleur pour associer les couleurs au code selon la convention Dewey
__________________________________________________________________


10/01/2020
------------------------------------------------------------------
- Front template HTML
- Query liste de données
- urls : aiguillage d'urls
- structure des données, des tables
- backoffice pour l'admin
__________________________________________________________________


22/01/2020
------------------------------------------------------------------
- cloud hébergement sur serveur
    - heroku
    - settings.py
    - package gunicorn,dj
    - manage collectstatic
    
