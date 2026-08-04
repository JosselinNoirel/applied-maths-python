# Basic mathematical operations

```{raw} html
<p class="language-switch"><a href="../../fr/topics/basic-mathematics.html">Français</a></p>
```

For a Python list or another ordinary iterable, use the built-in functions
{py:func}`min`, {py:func}`max`, `sum` and `abs`.

For NumPy arrays, use `np.min`, `np.max`, `np.sum` and `np.abs`. NumPy functions
can reduce an entire array or a selected axis:

```python
import numpy as np

A = np.array([[3.0, -1.0], [7.0, 2.0]])
column_minima = np.min(A, axis=0)
row_maxima = np.max(A, axis=1)
total = np.sum(A)
```

See [basic NumPy statistics](../reference/numpy-statistics.md) for `np.mean` and
`np.std`, and [numerical comparison and interpolation](../reference/numpy-comparison-interpolation.md)
for `np.isclose`, `np.allclose` and `np.interp`.
