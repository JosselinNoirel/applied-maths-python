# `numpy.meshgrid`

```{raw} html
<p class="language-switch"><a href="../../en/reference/numpy-meshgrid.html">English</a></p>
```

```{py:function} numpy.meshgrid(*coordinates, indexing='xy')

Transforme des coordonnées unidimensionnelles en matrices de coordonnées pour
évaluer une fonction ou un champ de vecteurs sur une grille.
```

```python
import numpy as np

x = np.linspace(-2, 2, 21)
y = np.linspace(-1, 1, 11)
X, Y = np.meshgrid(x, y, indexing='ij')
Z = X**2 + Y**2
```

Utilisez `indexing='ij'` lorsque l'ordre des axes du tableau doit suivre celui des coordonnées fournies;
avec l'indexation cartésienne `indexing='xy'` utilisée par défaut, `X`, `Y` et
`Z` ont la forme `(len(y), len(x))` (ce qui peut surprendre).

Voir la [référence officielle NumPy](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html).

