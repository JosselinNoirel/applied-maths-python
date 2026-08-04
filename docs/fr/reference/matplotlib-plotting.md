# Tracés de base avec Matplotlib

```{raw} html
<p class="language-switch"><a href="../../en/reference/matplotlib-plotting.html">English</a></p>
```

```{py:function} matplotlib.pyplot.subplots(nrows=1, ncols=1, **options)

Crée une figure et un ou plusieurs axes. Pour un seul graphique, renvoie
`(fig, ax)`.
```

```{py:function} matplotlib.pyplot.plot(x, y, **style)

Trace les valeurs sous forme de courbe, éventuellement avec des marqueurs.
```

```{py:function} matplotlib.pyplot.scatter(x, y, **style)

Trace des marqueurs séparés sans les relier.
```

```{py:function} matplotlib.pyplot.show()

Affiche toutes les figures ouvertes. Certains environnements Jupyter les
affichent automatiquement, mais `show` rend la sortie attendue explicite.
```

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin(x)")
ax.scatter(x[::10], np.sin(x[::10]), color="black")
ax.legend()
plt.show()
```

La forme orientée objet `ax.plot` est recommandée pour les figures structurées ;
`plt.plot` est pratique pour une exploration courte.

