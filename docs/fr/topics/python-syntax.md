# Syntaxe Python

```{raw} html
<p class="language-switch"><a href="../../en/topics/python-syntax.html">English</a></p>
```

Python lit généralement un programme ligne par ligne. Chaque ligne contient une
instruction complète, sauf lorsqu'une parenthèse ouverte indique que
l'instruction continue sur la ligne suivante.

## Instructions et commentaires

Un programme est une suite d'instructions : affectations, opérations, appels de
fonctions et structures de contrôle. Le caractère `#` commence un commentaire
que Python ignore :

```python
x = x + 1  # Increment x by one
```

Un bon commentaire explique l'intention du calcul plutôt que de répéter le code.

## Opérateurs arithmétiques

| Python | Opération |
|---|---|
| `x + y`, `x - y` | addition, soustraction |
| `x * y`, `x / y` | multiplication, division |
| `x**a` | puissance $x^a$ |
| `-x` | opposé de $x$ |
| `n % m` | reste de la division euclidienne |
| `n // m` | quotient entier |

Pour une racine $n$-ième, utilisez $x^{1/n}$, écrit `x**(1/n)`. Les
parenthèses sont importantes : si `n` est une variable, elles rendent
l'intention explicite.

Avec des tableaux NumPy, ces opérateurs agissent terme à terme.

## Appeler une fonction

Les parenthèses caractérisent l'appel d'une fonction :

```python
function(argument_1, argument_2)
```

Les arguments positionnels doivent respecter l'ordre prévu. Les arguments nommés
peuvent être écrits dans un ordre différent :

```python
import numpy as np

x = np.linspace(start=0, stop=10, num=21)
```

Les arguments optionnels possèdent une valeur par défaut. Par exemple,
{funcindex}`np.linspace`(`0, 10`) utilise par défaut `num=50` et `endpoint=True`.

Voir aussi les pages [Variables](variables.md), [Fonctions définies par
l'utilisateur](user-functions.md) et [Fonctions usuelles](common-functions.md).
