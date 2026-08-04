# Comparaison numérique et interpolation

```{raw} html
<p class="language-switch"><a href="../../en/reference/numpy-comparison-interpolation.html">English</a></p>
```

## Comparaison de flottants

```{py:function} numpy.isclose(a, b, rtol=1e-5, atol=1e-8)

Compare des valeurs terme à terme avec des tolérances relative et absolue.
```

```{py:function} numpy.allclose(a, b, rtol=1e-5, atol=1e-8)

Renvoie un booléen indiquant si toutes les comparaisons terme à terme sont
proches.
```

```python
import numpy as np

comparaison = np.isclose([0.1 + 0.2, 1.0], [0.3, 1.001])
tout_proche = np.allclose([0.1 + 0.2, 1.0], [0.3, 1.001])
```

Choisissez `atol` selon l'échelle du problème. Les valeurs par défaut peuvent
être trompeuses lorsque la valeur attendue est proche de zéro.

## Interpolation linéaire

```{py:function} numpy.interp(x, xp, fp)

Interpole linéairement les valeurs `x` à partir des coordonnées croissantes
`xp` et des valeurs échantillonnées `fp`.
```

```python
xp = np.array([0.0, 1.0, 2.0])
fp = np.array([0.0, 1.0, 4.0])
y = np.interp(1.5, xp, fp)
```

`xp` doit être croissant. Par défaut, les valeurs hors de l'intervalle utilisent
la première ou la dernière valeur échantillonnée plutôt que de prolonger le
segment extrême.

