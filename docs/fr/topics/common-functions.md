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

