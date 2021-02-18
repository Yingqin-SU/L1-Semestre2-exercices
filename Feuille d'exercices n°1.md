# Feuille d’exercices n∘1
Ces exercices sont à traiter de manière autonome. Une partie sera traitée en cours.

Pour chaque exercice, vous écrirez le programme qui réalise ce qui est demandé.

## Exercice 1

1. Votre fenêtre graphique doit contenir un canevas de couleur de fond noire et de taille 500x500 ainsi qu’un bouton avec le texte “Recommencer” placé en dessous du canevas.
2. Dessiner un rectangle rempli de rouge sur le canvas (la taille et la position sont au choix).
3. A chaque clic de l’utilisateur dans le rectangle, le rectangle devient bleu, puis rouge alternativement.
4. Si l’utilisateur clique en dehors du rectangle alors le rectangle est figé: c’est-à-dire que si on reclique à l’intérieur de celui-ci, rien ne se passe.
5. A tout moment, si l’utilisateur clique sur le bouton “recommencer”, alors on recommence du début avec le rectangle rempli de rouge dessiné.

## Exercice 2

1. Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 500x500 ainsi qu’un bouton avec le texte “Pause” placé en dessous du canevas.
2. Attendre deux clics de l’utilisateur.
3. Afficher une ligne bleue entre les deux points cliqués.
4. Attendre de nouveau deux clics.
5. Afficher une ligne rouge entre les deux nouveaux points cliqués.
6. Au clic suivant, les deux lignes sont effacées et on recommence (c’est-à-dire on attend de nouveau 2 clics comme au point 2.)
7. Si l’utilisateur clique sur le bouton “Pause”, alors le programme est suspendu (c’est-à-dire que cliquer ne modifie pas la fenêtre graphique) et le nom du bouton devient “Restart”.
8. Si l’utilisateur clique de nouveau sur le bouton “Restart” alors que le programme était suspendu, alors le programme reprend là où il en était, et le nom du bouton redevient “Pause”.

## Exercice 3

1. Votre fenêtre graphique doit contenir un canevas de couleur de fond noire et de taille 500x500 ainsi qu’un bouton avec le texte “Redémarrer” placé en dessous du canevas.
2. Diviser la fenêtre en 3 en affichant deux traits verticaux blancs.
3. Tant qu’il y a strictement moins de 2 croix, un clic dans la partie gauche affiche une croix bleue inscrite dans un carré de côté 50 centré sur le clic, et sinon ça ne fait rien.
4. Tant qu’il y a strictement moins de 3 carrés, un clic dans la partie du milieu affiche un carré vert de côté 50 centré sur le clic, et sinon ça ne fait rien.
5. Tant qu’il y a strictement moins de 3 cercles, un clic dans la partie droite affiche un cercle rouge de rayon 50 centré sur le clic, et sinon ça ne fait rien.
6. A tout moment, si l’utilisateur clique sur le bouton “Redémarrer”, alors tous les cercles, les carrés et les croix s’effacent.

## Exercice 4

1. Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 500x500 ainsi qu’un bouton avec le texte “Pause” placé en dessous du canevas.
2. Afficher un carré rempli de rouge de côté 50 au milieu du canevas.
3. Si l’utilisateur clique à l’intérieur du carré et que le côté du carré est au moins égale à 20, alors le côté du carré diminue de 10 (effacer et réafficher).
4. Si l’utilisateur clique à l’extérieur du carré et que le côté du carré est au plus égal à 100, alors le côté du carré augmente de 10 (effacer et réafficher).
5. Si l’utilisateur clique sur le bouton “Pause”, alors le programme est suspendu (c’est-à-dire que cliquer ne modifie plus le carré) et le nom du bouton devient “Restart”.
6. Si l’utilisateur clique de nouveau sur le bouton “Restart” alors que le programme était suspendu, alors le programme reprend là où il en était, et le nom du bouton redevient “Pause”.

## Exercice 5

1. Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 600x600 ainsi qu’un bouton avec le texte “Recommencer” placé en dessous du canevas.
2. Afficher deux lignes verticales séparant le canevas en trois parties égales. Celle de gauche est rouge, et celle de droite est bleu.
3. A chaque fois que l’utilisateur clique sur le canevas, les lignes verticales se déplacent de 10 pixels vers l’endroit cliqué: par exemple si le clic est entre les deux lignes, celle de gauche se déplace vers la droite, et celle de droite se déplace vers la gauche. De plus, les couleurs des lignes sont échangées.
4. Si l’utilisateur clique sur le bouton “Recommencer”, alors les 2 lignes verticales retournent à leur position initiale.

## Exercice 6

1. Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 500x500 ainsi qu’un bouton avec le texte “Annuler” placé à gauche du canevas.
2. Afficher en haut à gauche du canevas 3 carrés juxtaposés de côté 50 et de couleur verte jaune et bleu.
3. Afficher un cercle noir de rayon 50 au centre du canevas.
4. Si l’utilisateur clique dans un des carrés du bas, le cercle prend la couleur du carré sur lequel l’utilisateur a cliqué.
5. Si l’utilisateur clique en dehors des carrés alors le cercle devient noir.
6. Si l’utilisateur clique sur le bouton “Annuler” alors le cercle reprend la couleur qu’il avait avant le dernier changement de couleur. Il doit être possible d’annuler tous les changements de couleur jusqu’au début.