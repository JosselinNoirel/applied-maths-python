# Numerical comparison and interpolation

```{raw} html
<p class="language-switch"><a href="../../fr/reference/numpy-comparison-interpolation.html">Français</a></p>
```

## Floating-point comparison

```{py:function} numpy.isclose(a, b, rtol=1e-5, atol=1e-8)

Compare values element by element within relative and absolute tolerances.
```

```{py:function} numpy.allclose(a, b, rtol=1e-5, atol=1e-8)

Return one Boolean stating whether all element-wise comparisons are close.
```

```python
import numpy as np

comparison = np.isclose([0.1 + 0.2, 1.0], [0.3, 1.001])
all_match = np.allclose([0.1 + 0.2, 1.0], [0.3, 1.001])
```

Choose `atol` according to the scale of the problem. Defaults can be misleading
when the expected value is close to zero.

## Linear interpolation

```{py:function} numpy.interp(x, xp, fp)

Linearly interpolate values `x` from increasing sample coordinates `xp` and
sample values `fp`.
```

```python
xp = np.array([0.0, 1.0, 2.0])
fp = np.array([0.0, 1.0, 4.0])
y = np.interp(1.5, xp, fp)
```

`xp` must be increasing. By default, values outside the sample interval use the
first or last sample value rather than continuing the end segment.

