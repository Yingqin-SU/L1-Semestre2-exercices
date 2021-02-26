# IN200: projet de simulation de la propagation d’un incendie

Ce premier projet a pour objectif de vous apprendre à construire un programme réalisant ce qui est indiqué dans le sujet. Le sujet vous donne des indications sur la manière de construire votre programme et il doit être lu attentivement. Bien qu’il ne soit pas noté, ce projet vous prépare pour le deuxième projet du semestre qui sera évalué lors d’une soutenance. Ces deux projets se font en groupe de 5 ou 6 étudiants. Les membres de votre groupe sont choisis par votre chargé de TD, et vous ne devez pas en changer durant le semestre.

Le projet doit être écrit en Python. Les compétences techniques attendues sont celles du cours IN100 du premier semestre. Quelques compléments pourront être apportés en cours sur des points précis de programmation en Python. Vous devez utiliser les outils de programmation étudiés en IN100, à savoir le gestionnaire de version git couplé au dépôt GitHub, le linter flake8 qui doit être installé avec votre environnement VSCode, et le debugger fourni avec VSCode.

# Avant de commencer

Toutes les étapes de cette partie doivent être réalisées en TD avant de commencer la programmation en tant que telle. Appelez votre chargé de TD en cas de difficultés.

1. Votre chargé de TD vous répartit en groupes de 5 ou 6. Une fois cela fait, regroupez vous tout en conservant des distances de sécurité suffisantes.

2. Vérifier que votre environnement de programmation est correctement installé. Sinon reprenez le lien pour les instructions d’installation. Pour savoir si votre environnement vous permet de faire ce qui vous sera demandé durant le semestre, vérifiez que, dans le répertoire examples du projet l1-python, les programmes des dossiers hello et gui s’exécutent normalement. Entraidez-vous pour tenter de résoudre les éventuels problèmes des membres de votre groupe.

3. Dès maintenant, choisissez 2 responsables pour les tâches suivantes:
    * responsabilité du dépôt GitHub: vous hébergez le projet sur votre compte et devez donc inviter les autres membres à participer au projet; vous vous assurez que les commits qui sont “poussés” sur le dépôt sont bien fonctionnels (rappel: on ne doit pas faire de commit d’un programme qui ne fonctionne pas); de plus, le dépôt ne doit contenir que les sources du projet et non les éventuels fichiers générés par le projet (fichier de sauvegarde par exemple).
    * responsabilité de la mise en forme du code: vous vous assurez que le code satisfait bien les règles de style de la PEP8 (le linter flake8 ne doit retourner aucun warning) et que les bonnes pratiques de programmation sont respectées (nommage cohérent des variables et des fonctions, documentation du code avec des docstrings pour les fonctions…)

4. Le responsable du dépôt GitHub créée un nouveau projet intitulé projet_incendie sous GitHub, en se connectant à son compte, puis en choisissant New repository dans le menu accessible via le signe + en haut à droite de GitHub (attention à ne pas choisir New project dans ce menu). En créant un nouveau projet, GitHub propose d’initialiser le dépot avec un README. Faites le et remplissez ce fichier avec une brève description du projet. Plus tard, vous ajouterez des précisions, notamment sur la manière d’utiliser le projet. N’ajoutez pas de gitignore ou de licence.

5. Toujours sous GitHub, le responsable invite les autres membres du groupe à participer au projet. Pour cela, sur la page du projet, aller dans le menu “Settings”, puis choisir “Manage access”, puis le bouton vert “invite a collaborator”, et enfin, inscrire les noms d’utilisateur GitHub (devant être sous la forme uvsqXXX, où XXX est le numéro d’étudiant).

6. Les autres membres du groupe doivent accepter l’invitation depuis leur boîte mail ou bien les notifications sur leur compte GitHub (cloche en haut a gauche). À cette étape, tous le monde a les droits d’écriture sur le dépôt du projet.

7. Tous les membres réalisent le premier clône du projet.

8. Le responsable du dépôt ajoute alors le fichier incendie.py en y indiquant au début le groupe de TD, les noms des membres du projet et l’url du dépôt GitHub sous le format suivant:

```
#########################################
# groupe MPCI 3
# Toto LEHERO
# Titi LEVAINQUEUR
# etc...
# https://github.com/uvsq-info/l1-python
#########################################
```

9. Ensuite, le responsable ajoute ce fichier sur le dépôt avec la commande sync après l’avoir commit.

10. Tous les autres font alors un pull pour récupérer la dernière version du dépôt. A partir de maintenant, vous pouvez travailler séparément sur le projet.

# Description du projet

Le projet a pour objet la simulation de la propagation d’un incendie. Il comporte une partie graphique qui permettra de visualiser ce que l’on cherche à simuler, ainsi qu’un ensemble de fonctionnalités qui enrichiront le programme.

## Contraintes de programmation
---

Bien que ce ne soit pas la meilleure façon de programmer et même si vous savez faire autrement, vous respecterez les contraintes suivantes liées aux prérequis attendus pour faire le projet:

* le programme doit être écrit dans un unique fichier qui s’appelle incendie.py;

* le programme ne doit pas définir de classes d’objets;

* vous devez utiliser la librairie graphique tkinter;

* quand ce n’est pas possible de faire autrement (notamment pour les widgets graphiques mais pas uniquement), vous pouvez utiliser des variables globales;

* le programme sera découpé de la manière suivante (chaque partie devant apparaître bien distinctement en utilisant des commentaires):
    * informations liées au groupe
    * import des librairies
    * définition des constantes (écrites en majuscule)
    * définition des variables globales
    * définition des fonctions (chaque fonction devra contenir une docstring)
    * programme principal contenant la définition des widgets et des événements qui leur sont liés et l’appel à la boule de gestion des événements

## Sujet
---

On considère un terrain rectangulaire constitué de LARGEUR x HAUTEUR parcelles, où LARGEUR et HAUTEUR sont des constantes définies au début du programme et laissées à votre appréciation. Chaque parcelle est représentée par un carré dont la couleur est donnée par le type du terrain, couleurs données par le tableau suivant:

|Type	            |Couleur	|Durée de l’état        |
| ------------------|:---------:| -------------:        |
|Eau	            |Bleu       | + ∞                   |
|Forêt	            |Vert	    |Dépend des voisins     |
|Feu	            |Rouge	    |Constante DUREE_FEU    |
|Prairie	        |Jaune	    |Dépend des voisins     |
|Cendres tièdes	    |Gris	    |Constante DUREE_CENDRE |
|Cendres éteintes	|Noir       |+ ∞                    |



\
Les règles d’évolution sont les suivantes:

* une parcelle d’eau reste une parcelle d’eau durant toute la simulation;
* une parcelle qui devient en feu reste en feu durant la durée DUREE_FEU avant de devenir des cendres tièdes pendant la durée DUREE_CENDRE et enfin devenir des cendres éteintes durant le reste de la simulation; les valeurs de ces deux constantes sont à définir et laissées à votre appréciation;
* une parcelle de prairie prend feu dès qu’une des 4 cases voisines (gauche, droite, haut, bas) est en feu;
* une parcelle de forêt prend feu avec la probabilité 0.1 × nf où nf est le nombre de ses voisins en feu;

On considère que les bords du terrain ne peuvent pas brûler et qu’ils n’interviennent pas dans la propagation du feu. Le programme doit malgré tout être adapté pour les parcelles du bord.

Votre programme devra contenir les fonctionnalités suivantes:

* fonctionnalités liées au choix du terrain:
    * un bouton qui génère un terrain au hasard avec des parcelles d’eau, de forêt et de prairie;
    * un clic sur une parcelle de forêt ou de prairie la transforme en parcelle en feu;
    * un bouton pour sauvegarder l’état du terrain dans un fichier;
    * un bouton pour charger un terrain depuis un fichier;
* fonctionnalités liées à la simulation:
    * un bouton permet d’effectuer une étape de simulation; cela doit aussi être possible en appuyant sur une touche du clavier (à définir);
    * un bouton qui permet de démarrer une simulation; le nombre d’étapes doit alors s’afficher, ainsi que le nombre de parcelles en feu, et la simulation s’arrête quand il n’y a plus de parcelle en feu;
    * un bouton pour arrêter la simulation;
    * une touche (à définir) pour accélérer la vitesse de la simulation et une touche (à définir) pour la réduire; la vitesse de simulation doit être affichée en nombre d’étapes par secondes;
* le fichier README.md doit contenir les détails d’utilisation du programme, en particulier les touches à utiliser pour les différentes fonctionnalités;


## Indications
---

De manière générale, votre programme doit être découpé en fonctions courtes qui font des tâches bien définies et décrites dans une docstring. Chaque fonction doit être testée par la personne qui l’écrit avant d’être commitée sur le dépôt GitHub. Vous devez décider collecivement du choix de découpage du projet en fonctions.

De pair avec le choix des fonctions, vous devez décider de la manière de coder l’état du terrain. L’état du terrain à une étape de la simulation est donné par l’ensemble des états de chaque parcelle. L’état d’une parcelle est sa couleur et la durée restante avant de changer d’état. Pour coder cette information, vous pouvez utiliser une liste à deux dimensions (une “liste de listes”) qui contiendra les informations de couleur et de durée restante de chaque parcelle du terrain. Vous pouvez y ajouter l’identifiant de l’objet graphique créé par tkinter pour chaque parcelle afin de pouvoir modifier sa couleur. Par exemple, l’état d’une parcelle peut être la liste ["red", 8, 17], où "red" est la couleur de la case, 8 le nombre d’étapes avant que la cellule ne devienne en cendres tièdes, et 17 est l’identifiant de l’objet du canevas qui représente cette cellule (valeur retournée par la méthode canvas.create_rectangle(...)). Une alternative, plus efficace en temps de calcul, est de ne conserver dans une liste que les éléments qui sont modifiés et en inspectant les voisins des cellules en feu pour voir s’ils prennent feu et doivent alors être ajoutés à la liste.

Pour la sauvegarde dans un fichier, pensez à conserver la hauteur et la largeur du terrain. Vous pouvez ensuite écrire sur chaque ligne l’état (couleur + durée) des parcelles. Pour vérifier le bon fonctionnement de la sauvegarde et de l’ouverture de fichier, vous pouvez sauvegarder dans un fichier test2.txt un terrain que vous avez ouvert depuis le fichier test1.txt et vérifier ensuite que les 2 fichiers sont identiques, par exemple en tapant la commande diff test1.txt test2.txt dans le terminal. Les fichiers de sauvegarde ne doivent pas être inclus dans la gestion de version. Pour les exclure, vous pouvez ajouter un fichier .gitignore (le point indique que c’est un fichier caché), et écrire la ligne *.txt qui aura pour effet d’exclure tous les fichiers terminant par le suffixe .txt. Le fichier .gitignore doit être ajouté sur GitHub.

Pour choisir un élément au hasard dans un ensemble, vous pouvez utiliser la fonction random.choice(liste) du module random pour choisir un élément au hasard (uniformément) dans la liste. La méthode random.choices(liste,...) permet de choisir au hasard avec des pondérations données (chercher de la documentation par exemple ici). Cela peut être utile pour générer un terrain aléatoire en choisissant la proportion approximative de chaque type de parcelle.

Pour copier une liste de manière récursive, c’est-à-dire en impliquant également les sous-listes, les sous-sous-listes, etc., vous pouvez utiliser la méthode copy.deepcopy(objet) du module copy qui renvoie une copie récursive de l’objet passé en argument. La copie peut être nécessaire pour calculer le nouvel état d’un terrain à partir de son état précédent.

## Améliorations
---

* analyse de la simulation: on pourra s’intéresser à la question de savoir pour quelles proportions de prairie et forêt le feu se propage presque entièrement sur le terrain. On considèrera que le feu s’est propagé presque entièrement si il y a au moins une parcelle en cendres sur chaque bord du terrain. Pour faire cela, on peut simplifier la simulation en ne considérant que des prairies sans forêt pour les parcelles qui brûlent puis en faisant varier leur proportion initiale sur des terrains choisis au hasard jusqu’à observer ce phénomène. Le résultat étant aléatoire, on peut répéter plusieurs fois l’expérience pour estimer la probabilité que ce phénomène apparaisse;

* ajouter un mode d’édition du terrain accessible depuis un bouton; celui ci peut par exemple fonctionner en choisissant un type de terrain puis en cliquant sur une case ou en sélectionnant un groupe de cases en appuyant et déplaçant la souris;