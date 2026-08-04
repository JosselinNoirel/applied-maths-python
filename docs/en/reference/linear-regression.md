# Linear regression and polynomial fitting

```{raw} html
<p class="language-switch"><a href="../../fr/reference/linear-regression.html">Français</a></p>
```

```{py:function} numpy.polyfit(x, y, deg)

Fit polynomial coefficients by least squares, ordered from the highest power to
the constant term.
```

```python
import numpy as np

x = np.array([0.0, 1.0, 2.0, 3.0])
y = np.array([1.1, 2.9, 5.2, 6.8])
slope, intercept = np.polyfit(x, y, deg=1)
```

For polynomial evaluation, use `numpy.polyval`. High-degree polynomial fitting
can be poorly conditioned; rescale the coordinates or use NumPy's newer
polynomial API for demanding applications.

```{py:function} scipy.stats.linregress(x, y)

Calculate a linear least-squares regression and return slope, intercept,
correlation, hypothesis-test and standard-error information.
```

```python
from scipy.stats import linregress

result = linregress(x, y)
y_fit = result.intercept + result.slope * x
r_squared = result.rvalue**2
```

Use `polyfit(..., deg=1)` for simple coefficients. Use `linregress` when the
statistical outputs—such as standard errors or the slope-test p-value—matter.

See the [official `linregress` reference](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html).

