# Fonctions Python fréquemment utilisées

```{raw} html
<p class="language-switch"><a href="../../en/reference/python-builtins.html">English</a></p>
```

Ces fonctions intégrées ne nécessitent aucun import.

## `range`

```{py:function} range(start, stop, step=1)

Produit une séquence immuable d'entiers allant de `start` jusqu'à `stop` exclu.
Avec un seul argument, `start` vaut `0`.
```

```python
for k in range(1, 6):
    print(k**2)
```

Utilisez `range` pour les indices de boucle. Utilisez `numpy.arange` ou
`numpy.linspace` lorsqu'un tableau numérique doit participer à des calculs.

## `print`

```{py:function} print(*objects, sep=' ', end='\n')

Affiche un ou plusieurs objets sous forme de texte.
```

```python
iteration = 4
erreur = 2.3e-5
print("itération :", iteration, "erreur :", erreur)
```

`print` aide à examiner des résultats intermédiaires, mais une fonction doit en
général renvoyer son résultat plutôt que seulement l'afficher.

## `abs`

```{py:function} abs(x)

Renvoie la valeur absolue d'un nombre.
```

```python
erreur_absolue = abs(approximation - valeur_exacte)
```

Utilisez `numpy.abs` pour les tableaux.

## `len`

```{py:function} len(object)

Renvoie le nombre d'éléments d'un conteneur.
```

```python
valeurs = [2.0, 3.5, 4.1]
n = len(valeurs)
```

Pour un tableau NumPy multidimensionnel, `len(a)` ne donne que la taille du
premier axe ; consultez `a.shape` pour toutes les dimensions.

## `min` et `max`

```{py:function} min(iterable)

Renvoie le plus petit élément d'un itérable.
```

```{py:function} max(iterable)

Renvoie le plus grand élément d'un itérable.
```

```python
temperatures = [12.4, 9.8, 14.1, 11.3]
minimum = min(temperatures)
maximum = max(temperatures)
```

Pour un tableau NumPy, préférez `numpy.min` et `numpy.max`, en particulier pour
réduire les valeurs suivant un axe choisi.

## `enumerate`

```{py:function} enumerate(iterable, start=0)

Parcourt des couples `(indice, valeur)` sans mettre à jour manuellement un
compteur.
```

```python
valeurs = [2.0, 3.5, 4.1]
for indice, valeur in enumerate(valeurs):
    print(indice, valeur)
```

Voir les [fonctions intégrées officielles de Python](https://docs.python.org/fr/3/library/functions.html).
