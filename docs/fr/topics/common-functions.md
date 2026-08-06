# Fonctions usuelles

```{raw} html
<p class="language-switch"><a href="../../en/topics/common-functions.html">English</a></p>
```

Python (et ses bibliothèques) fournissent des fonctions réutilisables pour créer
des données, effectuer des calculs et afficher des résultats.

## Fonctions Python fondamentales

Les fonctions fournies par Python sont peu nombreuses (cf. la liste des [fonctions natives](https://docs.python.org/fr/3/library/functions.html)). Les plus utiles sont

- {funcindex}`print` affiche à l'écran ses arguments (cette fonction est peu utile dans le contexte interactif sauf pour [débugguer](debug.md)).
- {funcindex}`len` donne le nombre d'éléments d'une liste, d'un tableau NumPy ou le nombre de caractères d'une chaîne de caractères;
- {funcindex}`sum` donne la sommes des éléments d'une liste ou d'un tableau NumPy;
- {funcindex}`type` indique le type de l'objet;
- {funcindex}`abs` calcule une valeur absolue;
- {funcindex}`min` et {funcindex}`max` donnent les valeurs extrêmes;
- {funcindex}`round` arrondit une valeur;
- {funcindex}`range` produit une séquence d'entiers;
- {funcindex}`divmod` donne le quotient et le reste de la division euclidienne de deux entiers.

Cf. les [fonctions Python fréquemment utilisées](../reference/python-builtins.md).

Pour les conversions:

- {funcindex}`int` pour convertir en un entier `int('10')` ou `int(10.0)`
- {funcindex}`float` pour convertir en un nombre à virgule `float(10)` ou `float('1.4e3`)`

Cf. les [Objets Python](python-objects.md).

## Fonctions mathématiques

Les fonctions mathématiques sont fournies par des bibliothèques. Dans le cadre des cours de mathématiques appliquées, ce sera souvent celles de NumPy (`np.exp` pour une exponentielle).
Cf. la page [NumPy](numpy.md). D'autres bibliothèques fournissent des outils mathématiques, cf. [Bibliothèques Python](libs.md).

## Fonctions définies par l'utilisateurs

Cf. [Fonctions définies par l'utilisateur](user-functions.md).
