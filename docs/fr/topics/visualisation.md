# Graphiques et visualisation

```{raw} html
<p class="language-switch"><a href="../../en/topics/visualisation.html">English</a></p>
```

Matplotlib représente les données au moyen de figures et d'axes. Pour un premier
graphique, créez les points d'échantillonnage, calculez les valeurs et légendez
les deux axes.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(xlabel="x", ylabel="sin(x)", title="Fonction sinus")
ax.grid()
plt.show()
```

Indiquez toujours la grandeur représentée et, le cas échéant, son unité physique.

