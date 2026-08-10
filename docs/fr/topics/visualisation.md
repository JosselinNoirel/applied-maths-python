# Graphiques et visualisation

```{raw} html
<p class="language-switch"><a href="../../en/topics/visualisation.html">English</a></p>
```

La visualisation nécessite pour l'essentiel deux bibliothèques: NumPy pour la formation et la manipulation de listes de valeurs (des tableaux ou arrays dans le jargon NumPy) et Maplotlib pour la partie graphique proprement dite.
On importe donc ces bibliothèques dans une cellule de code généralement assez haut dans le carnet Jupyter:

```Python
import numpy as np
import matplotlib.pyplot as plt
```

Le choix des raccourcis `np` et `plt` est conventionnel.

* Pour la représentation des fonctions mathématiques, on aura recours à `plt.plot()`.
* Pour la représentation des données, on aura recours à `plt.scatter()`.

### Représentation d'une fonction mathématique d'une variable

Soit à représenter graphiquement la fonction
$$
  f(x) := \frac{1}{x - 1}
$$

```Python
def f(x):
    '''Function of interest, returns 1/(x - 1) with x a number or NumPy array'''
    return 1/(x - 1)
```

L'intervalle sur lequel représenter la fonction peut être connu à l'avance ou alors il peut être à la charge de l'utilisateur de trouver un intervalle représentatif ou intéressant.

**Choix de l'intervalle.** S'il faut choisir un intervalle, on peut procéder par tâtonnement ou se laisser guider par certaines valeurs remarquables. Dans l'exemple présenté ci-dessous, il est assez clair qu'il y a une singularité en $x = 1$ et il paraît par conséquent assez naturel de représenter la fonction sur un intervalle contenant la valeur $x = 1$. Nous choisirons de représenter la fonction sur l'intervalle $[-4, +6]$. C'est la fonction {funcindex}`np.linspace` qui nous sert ici:

Pour la représentation, la variable `x` — un tableau NumPy $(x_i)$ — accueille une grille de valeurs régulièrement réparties sur l'intervalle choisi $[-4, +6]$;
`y = f(x)` permet de calculer toutes les images de toutes les valeurs contenues dans `x` et de les stocker dans la variable `y`  — un tableau NumPy $(y_i)$.
Enfin {funcindex}`plt.plot` est utilisée pour générer une ligne brisée reliant tous les points $(x_i, y_i)$. Lorsque la fonction est continue et ne varie pas trop vite, la ligne brisée donne l'impression d'une courbe.

```Python
x = np.linspace(-4, +6)
y = f(x)
plt.plot(x, y)
```

Si la courbe est continue mais varie trop rapidement, une grille de valeurs plus dense peut se révéler nécessaire:

```Python
x = np.linspace(-4, +6, num=1024)
y = f(x)
plt.plot(x, y)
```

<details>
<summary>Comment gérer la singularité</summary>
Le rendu précédent met en évidence la singularité et le plus important est que vous vous en rendiez compte.
Si l'on souhaite néanmoins améliorer la représentation graphique, la singularité en $x=1$ impose de séparer les deux branches de la courbe:

```python
L = x < 1
R = x > 1

plt.plot(x[L], y[L], color='black')
plt.plot(x[R], y[R], color='black')
```

on peut reprendre ces commandes et y adjoindre une consigne permettant de restreindre la fenêtre sur l'axe des ordonnées:

```Python
plt.ylim(-6, +6)
```

Encore quelques commandes pour perfectionner la visualisation:

```
plt.axhline(0, color='black', lw=.25) # x = 0
plt.axvline(0, color='black', lw=.25) # y = 0
plt.title('$f(x) = 1/(x - 1)$')
```
</details>

```{warning}
Il se peut que la fonction ne soit pas définie sur l'ensemble des valeurs de l'intervalle en raison d'un logarithme ou d'une racine carrée. Python produira tout de même le graphique mais l'accompagnera d'un avertissement.
```

## Représenter plusieurs fonctions d'une variable

Pour représenter deux fonctions, il suffit que la cellule appelle deux fois la fonction `plt.plot()`.

```Python
def P(x):
    '''Power series expansion for sine function around x = 0.
       Accepts numbers of NumPy arrays.'''
    return x - 1/6 * x**3 + 1/120 * x**5

x = np.linspace(-np.pi, +np.pi)
plt.plot(x, np.sin(x), label='Sine')
plt.plot(x, P(x), label='Polynomial approximation')
plt.legend()
```

```{note}
On peut même utiliser deux grilles de points différentes si cela est utile.
```

## Axes logarithmiques

S'il est utile qu'un ou les deux axes utilisent une échelle logarithmique, on peut faire appel aux fonctions `plt.xscale` et `plt.yscale`:

```Python
def P(x):
    '''Power series expansion for sine function around x = 0.
       Accepts numbers of NumPy arrays.'''
    return x - 1/6 * x**3 + 1/120 * x**5

x = np.linspace(0, +np.pi)
plt.plot(x, P(x) - np.sin(x), label='Error')
plt.yscale('log')
plt.legend()
```

## Représenter des points

Si des points isolés sont souhaités plutôt qu'une ligne brisée ou une courbe, on utilise la fonction `plt.scatter`.

```python
x = np.linspace(-np.pi, +np.pi, 10)
y = np.sin(x)

plt.scatter(x, np.sin(x))
```

Ce genre de représentation est utile notamment lorsque l'on représente des données
(cf. [Importer des données](data.md)). Néanmoins, la bibliothèque Pandas devient progressivement plus indiquée.

## Champs de vecteurs

TODO.

Références détaillées :

- [Tracés de base : `subplots`, `plot`, `scatter`, `show`](../reference/matplotlib-plotting.md)
- [Titres, légendes, limites et annotations](../reference/matplotlib-annotation.md)
- [Champs de vecteurs avec `quiver` et `streamplot`](../reference/matplotlib-vector-fields.md)
