# Statistiques élémentaires

```{raw} html
<p class="language-switch"><a href="../../en/topics/basic-statistics.html">English</a></p>
```

Pour un échantillon numérique $x_1,\ldots,x_n$, les premiers résumés utiles sont
sa taille, son minimum, son maximum, sa somme, sa moyenne arithmétique et son
écart type.

```python
import numpy as np

data = np.array([4.1, 3.8, 4.4, 5.0, 4.2])
n = len(data)
minimum = np.min(data)
maximum = np.max(data)
total = np.sum(data)
mean = np.mean(data)
standard_deviation = np.std(data, ddof=1)
```

Le choix entre `ddof=0` et `ddof=1` dépend du fait que les valeurs représentent
la population complète ou un échantillon servant à estimer sa variabilité. Voir
la [référence des fonctions](../reference/numpy-statistics.md).

Pour décrire une relation linéaire entre deux mesures appariées, poursuivez avec
la [régression linéaire et l'ajustement polynomial](../reference/linear-regression.md).

