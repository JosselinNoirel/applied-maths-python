# Conditions booléennes

```{raw} html
<p class="language-switch"><a href="../../en/topics/boolean-conditions.html">English</a></p>
```

Une condition booléenne pose une question dont la réponse vaut *True* ou
*False*. Par exemple, `x > 0` demande si la valeur de $x$ est strictement
positive.

## Comparaisons

| Python | Signification |
|---|---|
| `a < b` | $a < b$ |
| `a <= b` | $a \leq b$ |
| `a == b` | égalité |
| `a != b` | $a \neq b$ |
| `a >= b` | $a \geq b$ |
| `a > b` | $a > b$ |

Il ne faut pas confondre l'affectation `=` (cf. [Variables](variables.md)) et la comparaison `==`.

Les erreurs d'arrondi rendent l'égalité exacte des flottants fragile.
Il faut donc ressortir à des comparaisons telles que `abs(a - b) < tol` ou `np.abs(a - b) < tol`;
préférez `np.isclose(a, b)` :

```python
import numpy as np

np.isclose(0.1 + 0.2, 0.3)
```

## Appartenance et valeur absente

```python
3 in [1, 2, 3]
option is None
```

`in` teste l'appartenance. `x is None` vérifie qu'une variable contient la valeur
spéciale *None*.

```{warning}
Quoi que *None* puisse être très utile, dans le cadre du traitement de données, les valeurs manquantes d'un jeu de données sont codées différemment par Pandas.
```

## Combiner des conditions

Les opérateurs `and`, `or` et `not` combinent ou inversent des conditions :

```python
inside = x >= 0 and x <= 1
outside = x < 0 or x > 1
not_inside = not inside
```

```{warning}
Pour les tableaux NumPy, utilisez `&`, `|` et `~` avec une paire de parenthèses
autour de chaque comparaison.
```
