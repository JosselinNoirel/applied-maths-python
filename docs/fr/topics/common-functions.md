# Fonctions usuelles

```{raw} html
<p class="language-switch"><a href="../../en/topics/common-functions.html">English</a></p>
```

Python, NumPy et Matplotlib fournissent des fonctions réutilisables pour créer
des données, effectuer des calculs et afficher des résultats. On importe
habituellement NumPy avec l'alias `np` :

```python
import numpy as np
```

## Construire un intervalle régulièrement discrétisé

[`numpy.linspace`](../reference/numpy-linspace.md) construit un nombre choisi de
valeurs régulièrement espacées entre deux bornes.

```python
import numpy as np

x = np.linspace(-1, 1, 5)
```

Ici, `x` vaut `array([-1. , -0.5, 0. , 0.5, 1. ])`. Consultez la
[fiche complète de `numpy.linspace`](../reference/numpy-linspace.md) pour les
règles sur les bornes, la valeur renvoyée, les exemples et les erreurs courantes.

## Choisir une fonction

Préférez une fonction qui exprime directement l'intention mathématique. Utilisez
par exemple `np.linspace(a, b, n)` lorsque le nombre de points importe, et
`np.arange(debut, fin, pas)` lorsque c'est l'incrément qui importe.

## Fonctions Python fondamentales

- `len(x)` donne le nombre d'éléments ;
- `type(x)` indique le type de l'objet ;
- `abs(x)` calcule une valeur absolue ;
- `min(x)` et `max(x)` donnent les valeurs extrêmes ;
- `round(x)` arrondit une valeur.

## Importer une bibliothèque

```python
import numpy as np
import matplotlib.pyplot as plt
```

Les alias `np` et `plt` sont des conventions largement utilisées. Ils évitent
des noms trop longs tout en gardant visible l'origine de chaque fonction. Évitez
`from numpy import *`, qui mélange les espaces de noms et peut masquer des
fonctions existantes.

Pour la création et le calcul sur les tableaux, consultez la page
[Bibliothèque NumPy](numpy.md). Pour la représentation des données, consultez
[Graphiques et visualisation](visualisation.md).
