# `numpy.linalg.solve`

```{raw} html
<p class="language-switch"><a href="../../fr/reference/numpy-linalg-solve.html">Français</a></p>
```

```{py:function} numpy.linalg.solve(a, b)

Solve the square linear system $Ax=b$.
```

```python
import numpy as np

A = np.array([[2.0, 1.0], [1.0, -1.0]])
b = np.array([5.0, 1.0])
x = np.linalg.solve(A, b)
```

`A` must be square and nonsingular, and the first dimension of `b` must be
compatible with `A`. Check the result with `A @ x` or a residual:

```python
residual = np.linalg.norm(A @ x - b)
```

Do not calculate `np.linalg.inv(A) @ b`; solving the system directly is clearer
and normally more accurate.

See the [official NumPy reference](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html).

