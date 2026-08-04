# Fonctions mathématiques avec NumPy

```{raw} html
<p class="language-switch"><a href="../../en/reference/numpy-mathematics.html">English</a></p>
```

Les fonctions suivantes agissent terme à terme sur les tableaux et acceptent
également des nombres scalaires.

```{py:function} numpy.exp(x)

Calcule $e^x$ terme à terme.
```

```{py:function} numpy.log(x)

Calcule le logarithme naturel. Les entrées réelles doivent être positives ; zéro
produit `-inf` et les entrées réelles négatives produisent `nan`.
```

```{py:function} numpy.sqrt(x)

Calcule la racine carrée principale. Une entrée réelle négative produit `nan`,
sauf si le tableau possède un type complexe.
```

```{py:function} numpy.sin(x)

Calcule le sinus d'angles exprimés en radians.
```

```{py:function} numpy.cos(x)

Calcule le cosinus d'angles exprimés en radians.
```

```{py:function} numpy.abs(x)

Calcule la valeur absolue, ou le module pour une valeur complexe.
```

```{py:function} numpy.sum(a, axis=None)

Additionne les valeurs du tableau. Avec `axis=None`, toutes les valeurs sont
additionnées ; sinon, la réduction suit l'axe choisi.
```

```python
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.exp(-x) * np.cos(x)
total = np.sum(y)
```

Préférez les versions NumPy aux fonctions de `math` lorsque l'argument peut être
un tableau.

