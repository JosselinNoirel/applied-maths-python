# Bibliothèques Python

```{raw} html
<p class="language-switch"><a href="../genindex.html">Index</a> · <a href="../../en/topics/libs.html">English</a></p>
```

Une {concept}`bibliothèque` est un ensemble de code réutilisable qui apporte des
fonctions, des classes ou des données à un programme. En pratique, une
bibliothèque peut contenir plusieurs **modules** et **paquets**. Un module est
souvent un fichier Python, tandis qu'un paquet organise plusieurs modules dans
une même arborescence. Le mot *bibliothèque* est un terme général plutôt
qu'une catégorie syntaxique propre à Python.

La bibliothèque standard, dont `math` et `statistics` font partie, est installée
avec Python. Les bibliothèques tierces comme NumPy, SciPy ou pandas doivent être
installées séparément, même si elles sont déjà présentes dans de nombreuses
distributions scientifiques et plateformes Jupyter.

## Importer une bibliothèque

### Exemple simple

L'instruction {funcindex}`import` rend un module disponible dans le programme :

```python
import math

result = math.exp(1.0)
```

L'importation crée ici le nom `math`. Les objets du module sont accessibles en
préfixant leur nom par `math.`, par exemple `math.exp` ou `math.pi`. Cette
écriture indique immédiatement l'origine de l'objet utilisé.

### Espaces de noms

Un {concept}`espace de noms` (*namespace*) associe des noms à des objets. Chaque
module possède son propre espace de noms : `math.exp` et une fonction
personnelle appelée `exp` peuvent donc coexister sans se remplacer. Cette
séparation limite les collisions et rend le programme plus lisible. Voir aussi
les [fonctions définies par l'utilisateur](user-functions.md).

Pour certaines bibliothèques, on emploie conventionnellement un alias court :

```python
import numpy as np
import matplotlib.pyplot as plt
```

On peut aussi importer directement quelques objets dans l'espace de noms
courant :

```python
from math import exp, log

result = exp(1.0) + log(2.0)
```

Un dernier exemple, en outre, importe l'objet sous un autre nom

```Python
from numpy import pi as π
```

Occasionnellement, on choisira d'importer tous les objets (mais cela est peu recommandé):

```{autolink-skip}
```

```Python
from sympy import *
```

## Bibliothèques classiques

### Mathématiques et calcul scientifique

- [`math`](https://docs.python.org/3/library/math.html) fournit les fonctions
  mathématiques usuelles pour des nombres réels scalaires ; il appartient à la
  bibliothèque standard.
- [`cmath`](https://docs.python.org/3/library/cmath.html) fournit leurs variantes
  adaptées aux nombres complexes scalaires.
- [NumPy](https://numpy.org/doc/stable/) fournit les tableaux multidimensionnels,
  le calcul terme à terme, l'algèbre linéaire élémentaire, les FFT et des outils
  statistiques. Ses fonctions sont adaptées aux calculs vectorisés.
- [SciPy](https://docs.scipy.org/doc/scipy/) complète NumPy avec des algorithmes
  d'intégration, d'interpolation, d'optimisation, de traitement du signal,
  d'équations différentielles et de statistiques.
- [SymPy](https://docs.sympy.org/latest/) permet le calcul symbolique :
  simplification d'expressions, dérivation, intégration et résolution exacte
  lorsque cela est possible.
- [Autograd](https://autograd.readthedocs.io/en/latest/) réalise la
  différentiation automatique de fonctions numériques écrites avec une partie
  de l'interface NumPy.

Pour la création et le calcul sur les tableaux, voir la [bibliothèque
NumPy](numpy.md).

### Traitement des données et statistiques

- [NumPy](https://numpy.org/doc/stable/reference/routines.statistics.html)
  calcule efficacement sommes, moyennes, écarts-types, quantiles et autres
  résumés sur des tableaux numériques homogènes.
- [Pandas](https://pandas.pydata.org/docs/) fournit les objets `Series` et
  `DataFrame` pour importer, nettoyer, sélectionner, regrouper et agréger des
  données tabulaires avec des lignes et colonnes étiquetées.
- [random](https://docs.python.org/3/library/random.html) génère des nombres
  pseudo-aléatoires, souvent pour réaliser des tests statistiques ou faire de
  l'optimisation.
- [`statistics`](https://docs.python.org/3/library/statistics.html), dans la
  bibliothèque standard, propose des statistiques descriptives simples sur des
  données Python ordinaires.
- [`scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html) fournit
  des lois de probabilité, des statistiques descriptives, des tests et plusieurs
  méthodes d'estimation.
- [statsmodels](https://www.statsmodels.org/stable/) est destiné à la
  modélisation statistique, notamment aux régressions et à l'analyse de séries
  temporelles.

### Visualisation

- [Matplotlib](https://matplotlib.org/stable/) est la bibliothèque de référence
  pour construire et personnaliser des graphiques scientifiques en Python.
- [Pandas](https://pandas.pydata.org/docs/user_guide/visualization.html) propose
  des méthodes de tracé directement associées aux `Series` et `DataFrame` ;
  elles utilisent généralement Matplotlib.
- [seaborn](https://seaborn.pydata.org/) fournit une interface de plus haut
  niveau pour les graphiques statistiques et facilite l'utilisation des données
  tabulaires pandas.

Pour les premiers tracés du cours, voir [Graphiques et
visualisation](visualisation.md).
