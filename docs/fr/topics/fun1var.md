# Fonction d'une variable

```{raw} html
<p class="language-switch"><a href="../../en/topics/fun1var.html">English</a></p>
```

## Définir la fonction

Il est souvent utile de définir une fonction Python qui traduit directement
la fonction mathématique que l'on souhaite étudier : cela rend le code plus
lisible et évite de recopier la même expression dans plusieurs calculs.

Par exemple, pour $f(t)=\sin^2(t)\exp(-t)$ :

```python
import numpy as np

def f(t):
    return np.sin(t)**2 * np.exp(-t)
```

`**2` représente le carré, et les fonctions trigonométriques de NumPy
utilisent des angles en radians. Avec ces opérations NumPy, `f` accepte aussi
bien un nombre qu'un tableau : dans ce dernier cas, elle calcule une valeur
pour chaque élément, sans boucle explicite.

```python
value = f(1.0)
values = f(np.array([0.0, 1.0, 2.0]))
```

Avant de choisir les valeurs de l'argument, vérifiez le domaine de définition :
par exemple, un logarithme réel exige un argument strictement positif et un
dénominateur ne doit pas être nul. Voir aussi les
[fonctions définies par l'utilisateur](user-functions.md).

## Courbe représentative

La représentation graphique aide à construire son intuition mathématique et
constitue souvent la première étape de l'analyse. Choisissez un intervalle,
puis construisez une grille de valeurs avec
[`numpy.linspace`](../reference/numpy-linspace.md).

```python
import matplotlib.pyplot as plt

t = np.linspace(0, np.pi, 200)
fig, ax = plt.subplots()
ax.plot(t, f(t))
ax.set_xlabel("t")
ax.set_ylabel("f(t)")
ax.grid(True)
plt.show()
```

Ici, `t` contient 200 points régulièrement espacés entre $0$ et $\pi$,
bornes comprises. `f(t)` contient les 200 valeurs correspondantes, et
`ax.plot` relie les points par des segments.

Pour une fonction variant rapidement, augmentez le nombre de points et
comparez les tracés obtenus. Un graphique peut manquer une oscillation ou un
maximum situé entre deux points : il suggère un comportement, mais ne
constitue pas une démonstration. En présence d'une discontinuité ou d'une
singularité, tracez séparément les intervalles où la fonction est continue
pour éviter de relier artificiellement les deux côtés.
