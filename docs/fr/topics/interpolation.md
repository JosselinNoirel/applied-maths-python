# Interpolation

```{raw} html
<p class="language-switch"><a href="../../en/topics/interpolation.html">English</a></p>
```

L'interpolation estime des valeurs entre des échantillons connus. Elle se
distingue de l'extrapolation hors de l'intervalle échantillonné.

Les notebooks utilisent [`scipy.interpolate.interp1d`](../reference/scipy-interpolation.md),
qui est désormais une interface ancienne. Pour une nouvelle interpolation
linéaire, préférez {py:func}`numpy.interp` ; utilisez
`scipy.interpolate.make_interp_spline` lorsqu'une spline est nécessaire.

```python
import numpy as np

x = np.array([0.0, 1.0, 2.0])
y = np.array([0.0, 1.0, 4.0])
y_new = np.interp(1.5, x, y)
```

Examinez toujours la densité d'échantillonnage et le comportement attendu entre
les points.
