# Opérations mathématiques élémentaires

```{raw} html
<p class="language-switch"><a href="../../en/topics/basic-mathematics.html">English</a></p>
```

Pour une liste Python ou un autre itérable ordinaire, utilisez les fonctions
intégrées {py:func}`min`, {py:func}`max`, `sum` et `abs`.

Pour les tableaux NumPy, utilisez `np.min`, `np.max`, `np.sum` et `np.abs`. Les
fonctions NumPy peuvent réduire tout le tableau ou un axe choisi :

```python
import numpy as np

A = np.array([[3.0, -1.0], [7.0, 2.0]])
minimum_colonnes = np.min(A, axis=0)
maximum_lignes = np.max(A, axis=1)
total = np.sum(A)
```

Consultez les [statistiques NumPy élémentaires](../reference/numpy-statistics.md)
pour `np.mean` et `np.std`, et la page [comparaison numérique et interpolation](../reference/numpy-comparison-interpolation.md)
pour `np.isclose`, `np.allclose` et `np.interp`.
