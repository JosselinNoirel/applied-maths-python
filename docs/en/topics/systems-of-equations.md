# Systems of linear equations

```{raw} html
<p class="language-switch"><a href="../../fr/topics/systems-of-equations.html">Français</a></p>
```

A linear system is written $Ax=b$. Store the coefficients in a two-dimensional
NumPy array and the right-hand side in a one-dimensional array, then use
[`numpy.linalg.solve`](../reference/numpy-linalg-solve.md).

```python
import numpy as np

A = np.array([[3.0, -1.0], [2.0, 4.0]])
b = np.array([7.0, 10.0])
x = np.linalg.solve(A, b)
```

Always verify the dimensions and calculate the residual $Ax-b$. A very small
residual confirms that the computed vector satisfies the numerical system; it
does not by itself guarantee that the model or data are correct.

