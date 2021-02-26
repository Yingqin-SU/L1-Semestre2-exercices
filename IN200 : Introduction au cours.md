# IN200 : introduction au cours

## 1. Objectifs du cours
---

* Programmation en Python
* Pas ou peu de contenu supplémentaire par rapport au cours du premier semestre IN100:
    * les contenus de IN100 sont sur [cette page](https://github.com/uvsq-info/l1-python)
    * variables, expressions, structures itératives et de contrôle, fonctions, listes, librairie graphique tkinter, outils de programmation (debugger, linter flake8, git)
* Apprendre à construire un programme conséquent (projet) et à travailler à plusieurs:
    * un premier projet d’entraînement durant la première partie du semestre non évalué
    * un deuxième projet sur la deuxième partie qui sera évalué par une soutenance

## 2. Organisation des cours et TDs
---

* 6 CM qui ont lieu une semaine sur 2 (donc le prochain cours aura lieu la semaine du 15 février):
    * compléments de cours
    * correction d’une partie des exercices à travailler entre les cours
    * développement d’un projet
* 4 TDs dont les dates ne sont pas encore complètement arrêtées:
    * le premier a lieu la semaine du 8 février ou du 15 février selon les groupes
* dans la situation actuelle, les cours ont lieu à distance, et les TDs en présentiel, peut-être en demi-groupe.
* [Emploi du temps officiel](https://edt.uvsq.fr/cal?vt=month&dt=2021-02-01&et=module&fid0=LSIN200%20); ce module s’appelle LSIN200 (mais l’emploi du temps n’est pas à jour pour le moment).
* Chaque créneau dure 1 heure et 20 minutes.

### Contenu des 4 séances de TD
---

* TD 1: démarrage du premier projet
* TD 2 (vers la fin du premier projet): évaluation individuelle sur machine type colle
* TD 3 (au milieu du deuxième projet): soutien sur le projet
* TD 4: soutenance du deuxième projet

### Evaluation
---

* Deux évaluations en TD:
    * kholle
    * soutenance de projet
* Deux évaluations sur Moodle samedi matin
* 4 notes au total, et l’on prend les 3 meilleures pour la moyenne (pas de rattrapage)
* le niveau d’exigence sera plus élevé que celui du cours IN100

### Communication
---

* page Moodle du cours:
    * contenus du cours
    * exercices de programmation à faire pour préparer les évaluations
    * sujets de projet
    * liens de visioconférence
    * notes aux évaluations
    * forum
* forum: toute question non personnelle doit être prioritairement posée sur ce forum, après avoir vérifié qu’elle n’a pas déjà été posée
* pas de réponse par mail, sauf s’il s’agit d’une question personnelle. Dans ce cas utiliser les questions via Moodle ou bien le mail en utilisant votre adresse uvsq.
* des espaces Moodle par groupes seront créés pour la communication avec vos chargés de TD
* si vous créez un serveur discord (ou équivalent) pour la promotion vous pouvez m’inviter pour répondre à vos questions (idem pour les groupes de TD)

### Environnement de programmation
---

* On utilise le même environnement que pour IN100 ([manuel d’installation](https://github.com/uvsq-info/l1-python/blob/master/INSTALL.md))
* Possibilité de prêt d’ordinateur par l’université: se signaler
* Sur le campus, prêt d’ordinateur par la BU (cartable numérique)
* Si vous ne parvenez pas à installer l’environnement, vous pouvez programmer en ligne sur le site https://repl.it/
    * créer un compte
    * créer un “new REPL” et choisir le langage Tkinter (en fait Python3 avec tkinter)

## 3. Travailler en groupe sur un projet
---

* pédagogie adaptée à l’informatique pour acquérir de l’autonomie en programmation
* ne pas hésiter à chercher des ressources sur internet
* utile quel que soit le langage de programmation
* encadrement minimal (manque de moyens)
* les groupes de 5-6 étudiants sont choisis (presque) au hasard pour le semestre; vous ne pouvez pas en changer;
* ne fonctionne que s’il y a une bonne communication dans le groupe
    * apprentissage par les pairs
    * utilisation d’outils adaptés: visio, forum chat… par exemple discord est adapté pour tout ça, et git bien sûr
* les enseignants sont là pour vous aider, encore faut-il les contacter, et pas (que) au dernier moment

### Les projets
---

* premier projet commun pour tout le monde: simulation de la propagation d’un incendie
    * projet d’entraînement non noté mais indispensable à faire pour la suite
    * inutile d’aller copier sur les autres groupes, mais cela ne vous empêche pas de vous entraider
* deuxième projet: un sujet par groupe de projet
* dans chaque groupe, il faudra désigner
    * un responsable GitHub: c’est lui qui hébergera le projet sur son compte GitHub et invitera les autres membres; il vérifiera que les commits qui sont poussés sont bien fonctionnels, et qu’ils ne contiennent que des sources du projet
    * un responsable de la qualité du code: vérifier que les règles de style sont bien respectées (PEP8), ainsi que les bonnes pratiques de programmation (nommage des fonctions et variables, docstring dans les fonctions, etc.)