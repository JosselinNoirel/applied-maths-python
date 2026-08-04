# Vector-field plots

```{raw} html
<p class="language-switch"><a href="../../fr/reference/matplotlib-vector-fields.html">Français</a></p>
```

```{py:function} matplotlib.pyplot.quiver(X, Y, U, V, **style)

Draw an arrow `(U, V)` at every coordinate `(X, Y)`.
```

```{py:function} matplotlib.pyplot.streamplot(X, Y, U, V, **style)

Draw streamlines tangent to a two-dimensional vector field.
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

`X`, `Y`, `U` and `V` must have compatible shapes. Use `quiver` to see local
direction and magnitude; use `streamplot` to emphasise trajectories.

