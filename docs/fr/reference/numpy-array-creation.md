# Créer des tableaux NumPy

```{raw} html
<p class="language-switch"><a href="../../en/reference/numpy-array-creation.html">English</a></p>
```

```{py:function} numpy.array(object, dtype=None)

Crée un tableau NumPy à partir d'une séquence ou d'un autre objet compatible.
```

```python
import numpy as np

A = np.array([[2.0, 1.0], [-1.0, 3.0]])
```

Les lignes doivent avoir des longueurs compatibles. Un tableau numérique possède
généralement un type commun, accessible avec `A.dtype`.

```{py:function} numpy.zeros(shape, dtype=float)

Crée un tableau de la forme demandée rempli de zéros.
```

```python
etat = np.zeros(100)
matrice = np.zeros((3, 4))
```

```{py:function} numpy.empty(shape, dtype=float)

Alloue un tableau sans initialiser ses valeurs.
```

```python
travail = np.empty(100)
travail[:] = 0.0
```

Ne lisez jamais les valeurs de `empty` avant de les remplacer. Préférez `zeros`
si le tableau n'est pas immédiatement rempli.

```{py:function} numpy.arange(start, stop, step=1)

Renvoie des valeurs séparées par `step` dans l'intervalle semi-ouvert
`[start, stop)`.
```

```python
indices = np.arange(0, 10, 2)
```

Pour une grille flottante dont les bornes importent, préférez
[`numpy.linspace`](numpy-linspace.md).

