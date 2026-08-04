# Interpolation unidimensionnelle

```{raw} html
<p class="language-switch"><a href="../../en/reference/scipy-interpolation.html">English</a></p>
```

```{py:function} scipy.interpolate.interp1d(x, y, kind='linear', **options)

Construit une fonction interpolante à partir de données unidimensionnelles
échantillonnées.
```

```python
import numpy as np
from scipy.interpolate import interp1d

x = np.array([0.0, 1.0, 2.0, 3.0])
y = x**2
interpolant = interp1d(x, y)
y_half = interpolant(1.5)
```

`interp1d` apparaît dans les notebooks mais constitue désormais une interface
ancienne. Elle reste disponible ; pour une nouvelle interpolation linéaire,
préférez normalement `numpy.interp`, et pour une interpolation spline,
`scipy.interpolate.make_interp_spline`.

N'extrapolez pas involontairement. Par défaut, une évaluation hors de
l'intervalle échantillonné peut lever une erreur ou demander des options
explicites sur les bornes.

Voir le [guide SciPy de l'interpolation unidimensionnelle](https://docs.scipy.org/doc/scipy/tutorial/interpolate/1D.html).

