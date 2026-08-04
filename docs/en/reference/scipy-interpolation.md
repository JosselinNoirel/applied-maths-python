# One-dimensional interpolation

```{raw} html
<p class="language-switch"><a href="../../fr/reference/scipy-interpolation.html">Français</a></p>
```

```{py:function} scipy.interpolate.interp1d(x, y, kind='linear', **options)

Construct a callable interpolant from sampled one-dimensional data.
```

```python
import numpy as np
from scipy.interpolate import interp1d

x = np.array([0.0, 1.0, 2.0, 3.0])
y = x**2
interpolant = interp1d(x, y)
y_half = interpolant(1.5)
```

`interp1d` occurs in the notebooks but is now a legacy interface. It remains
available, yet new linear-interpolation code should normally use `numpy.interp`;
for spline interpolation, use `scipy.interpolate.make_interp_spline`.

Do not extrapolate unintentionally. By default, evaluation outside the sampled
interval may raise an error or require explicit bounds options.

See SciPy's [one-dimensional interpolation guide](https://docs.scipy.org/doc/scipy/tutorial/interpolate/1D.html).

