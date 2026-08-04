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

## Exemple : une fonction avec une singularité

Considérons $f(x)=1/(x-1)$ sur $[-4,6]$. La singularité en $x=1$ impose de
séparer les deux branches de la courbe :

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (x - 1)

x = np.linspace(-4, 6, 500)
left = x < 1
right = x > 1

fig, ax = plt.subplots()
ax.plot(x[left], f(x[left]), color="black", label="f(x)")
ax.plot(x[right], f(x[right]), color="black")
ax.axhline(0, color="gray", linewidth=0.8)
ax.axvline(1, color="lightgray", linestyle="--", label="asymptote")
ax.set(xlabel="x", ylabel="f(x)", ylim=(-5, 5))
ax.legend()
plt.show()
```

Tracer toutes les valeurs en une seule fois créerait un segment trompeur à
travers la discontinuité. Un graphique est un outil d'analyse : il faut tenir
compte du domaine de définition, des singularités et de l'échelle.

## Courbes, points et échelles

- `ax.plot(x, y)` relie les valeurs par des segments ;
- `ax.scatter(x, y)` affiche un nuage de points ;
- `ax.set_xscale("log")` ou `ax.set_yscale("log")` utilise une échelle
  logarithmique lorsque les valeurs sont strictement positives ;
- l'argument `label` et `ax.legend()` construisent une légende.
