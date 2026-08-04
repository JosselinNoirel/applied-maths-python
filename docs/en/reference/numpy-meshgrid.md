# `numpy.meshgrid`

```{raw} html
<p class="language-switch"><a href="../../fr/reference/numpy-meshgrid.html">Français</a></p>
```

```{py:function} numpy.meshgrid(*coordinates, indexing='xy')

Turn one-dimensional coordinate arrays into coordinate matrices for evaluating
a function or vector field on a grid.
```

```python
import numpy as np

x = np.linspace(-2, 2, 21)
y = np.linspace(-1, 1, 11)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
```

With the default Cartesian `indexing="xy"`, `X`, `Y` and `Z` have shape
`(len(y), len(x))`. Use `indexing="ij"` when array-axis order should follow the
input coordinate order.

See the [official NumPy reference](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html).

