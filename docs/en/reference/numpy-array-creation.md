# Creating NumPy arrays

```{raw} html
<p class="language-switch"><a href="../../fr/reference/numpy-array-creation.html">Français</a></p>
```

```{py:function} numpy.array(object, dtype=None)

Create a NumPy array from a sequence or another array-like object.
```

```python
import numpy as np

A = np.array([[2.0, 1.0], [-1.0, 3.0]])
```

Rows must have compatible lengths. A numeric array normally has one shared data
type, available as `A.dtype`.

```{py:function} numpy.zeros(shape, dtype=float)

Create an array of the requested shape filled with zeros.
```

```python
state = np.zeros(100)
matrix = np.zeros((3, 4))
```

```{py:function} numpy.empty(shape, dtype=float)

Allocate an array without initialising its entries.
```

```python
workspace = np.empty(100)
workspace[:] = 0.0
```

Never read values from `empty` before replacing them. Prefer `zeros` unless the
array will be filled immediately.

```{py:function} numpy.arange(start, stop, step=1)

Return values separated by `step` in the half-open interval `[start, stop)`.
```

```python
indices = np.arange(0, 10, 2)
```

For floating-point grids with important endpoints, prefer
[`numpy.linspace`](numpy-linspace.md).

