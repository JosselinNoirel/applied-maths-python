# Représenter un champ de vecteurs

```{raw} html
<p class="language-switch"><a href="../../en/reference/matplotlib-vector-fields.html">English</a></p>
```

```{py:function} matplotlib.pyplot.quiver(X, Y, U, V, **style)

Trace une flèche `(U, V)` à chaque coordonnée `(X, Y)`.
```

```{py:function} matplotlib.pyplot.streamplot(X, Y, U, V, **style)

Trace des lignes de courant tangentes à un champ de vecteurs bidimensionnel.
```

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 21)
y = np.linspace(-2, 2, 21)
X, Y = np.meshgrid(x, y)
U, V = Y, -X

plt.quiver(X, Y, U, V)
plt.show()
```

`X`, `Y`, `U` et `V` doivent avoir des formes compatibles. Utilisez `quiver`
pour voir la direction et l'amplitude locales ; utilisez `streamplot` pour mettre
les trajectoires en évidence.

