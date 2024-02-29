# Algorithme A\*

L’algorithme A\* est un algorithme heuristique qui permet de trouver **très rapidement** un plus court chemin entre deux points avec d’éventuels obstacles. Outre sa vitesse, cet algorithme est réputé pour **garantir** une solution en sortie.

# Sujet

**Contexte** : Rodolphe est un nain, il cherche le chemin le plus court pour aller dans sa
taverne favorite en évitant les arbres qui sont les amis des elfs, quels horreurs !

**Consigne** : le but de ce TP est d'implémenter l'algorithme A\* sur une grille 2D. Elle
contiendra des obstacles que l'algorithme devra contourner pour atteindre le point
d'arrivée.

**Description de la grille** :

- La grille est un tableau 2D de dimensions 10x10.
- Les cellules de la grille peuvent être vides ou contenir un obstacle.
- Le point de départ est aléatoire (l’alcool est dangereux pour la santé).
- Le point d'arrivée est situé dans le coin inférieur droit de la grille (9,9).
