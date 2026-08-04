# Basic statistics with NumPy

```{raw} html
<p class="language-switch"><a href="../../fr/reference/numpy-statistics.html">Français</a></p>
```

```{py:function} numpy.min(a, axis=None)

Return the minimum of an array, or minima along an axis.
```

```{py:function} numpy.max(a, axis=None)

Return the maximum of an array, or maxima along an axis.
```

```{py:function} numpy.mean(a, axis=None)

Return the arithmetic mean, optionally along an axis.
```

```{py:function} numpy.std(a, axis=None, ddof=0)

Return the standard deviation. The default `ddof=0` uses the population
definition; use `ddof=1` for the common corrected sample standard deviation.
```

The total is calculated with {py:func}`numpy.sum`.

```python
import numpy as np

data = np.array([2.1, 2.4, 2.5, 3.0])
summary = {
    "minimum": np.min(data),
    "maximum": np.max(data),
    "mean": np.mean(data),
    "standard_deviation": np.std(data),
    "sum": np.sum(data),
}
```

When `NaN` represents missing data, ordinary reductions propagate it. Functions
such as `numpy.nanmean` and `numpy.nanstd` explicitly ignore `NaN` values.
