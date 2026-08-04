# Systèmes d'équations linéaires

```{raw} html
<p class="language-switch"><a href="../../en/topics/systems-of-equations.html">English</a></p>
```

Un système linéaire s'écrit $Ax=b$. Placez les coefficients dans un tableau
NumPy bidimensionnel et le second membre dans un tableau unidimensionnel, puis
utilisez [`numpy.linalg.solve`](../reference/numpy-linalg-solve.md).

```python
import numpy as np

A = np.array([[3.0, -1.0], [2.0, 4.0]])
b = np.array([7.0, 10.0])
x = np.linalg.solve(A, b)
```

Vérifiez toujours les dimensions et calculez le résidu $Ax-b$. Un résidu très
petit confirme que le vecteur calculé satisfait le système numérique ; il ne
garantit pas à lui seul la validité du modèle ou des données.

