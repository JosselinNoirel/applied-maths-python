# `numpy.linalg.solve`

```{raw} html
<p class="language-switch"><a href="../../en/reference/numpy-linalg-solve.html">English</a></p>
```

```{py:function} numpy.linalg.solve(a, b)

Résout le système linéaire carré $Ax=b$.
```

```python
import numpy as np

A = np.array([[2.0, 1.0], [1.0, -1.0]])
b = np.array([5.0, 1.0])
x = np.linalg.solve(A, b)
```

`A` doit être carrée et inversible ; la première dimension de `b` doit être
compatible avec `A`. Vérifiez le résultat avec `A @ x` ou un résidu :

```python
residu = np.linalg.norm(A @ x - b)
```

Ne calculez pas `np.linalg.inv(A) @ b` : résoudre directement le système est
plus clair et généralement plus précis.

Voir la [référence officielle NumPy](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html).

