# Syntaxe Python

```{raw} html
<p class="language-switch"><a href="../../en/topics/python-syntax.html">English</a></p>
```

Python lit généralement un programme ligne par ligne. Chaque ligne contient une
instruction complète, sauf lorsqu'une parenthèse ouverte indique que
l'instruction continue sur la ligne suivante.

## Contenu d'un programme

Un programme consiste en une suite d'**instructions**. Ces instructions permettent de

-   importer des bibliothèques,
-   affecter de [variable](variables.md),
-   opérations faisant appel à des **opérateurs**
-   appeler des fonctions,
    -   soit des fonctions prédéfinies (par exemple,
        `len()` ; voir les [fonctions Python](../reference/python-builtins.md)),
    -   soit des fonctions définies par une bibliothèque (par exemple,
        [`linspace()`](../reference/numpy-linspace.md)),
    -   soit encore des fonctions définies par l'utilisateur (cf.
        [fonctions](user-functions.md)),
-   on peut trouver des [structures de contrôle](control-flow.md)
    (if-then-else, boucles for ou while).

## Commentaires

Un `#` (*croisillon* ou *hash sign*) initie sur la ligne un
{concept}`commentaire`, c'est-à-dire une portion de code qui n'est pas lue par
Python mais peut accueillir une annotation destinée au lecteur.

```python
x = x + 1 # Increment x by one
```

Un bon commentaire explique l'intention du calcul plutôt que de répéter en mots le code. (L'exemple précédent est donc mauvais car le code est tout à fait transparent.)

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

Les parenthèses caractérisent l'appel d'une fonction:

```python
function(argument_1, argument_2)
```

Une fonction peut être programmée de façon à utiliser zéro `function()`, un ou plusieurs arguments.
Les arguments positionnels doivent respecter l'ordre prévu. Les arguments nommés
peuvent être écrits dans un ordre différent (c'est le cas d'un certain nombre de fonctions de [NumPy](numpy.md)):

```python
import numpy as np

x = np.linspace(start=0, stop=10, num=21)
```

Les arguments optionnels possèdent une valeur par défaut. Par exemple,
prenons l'exemple de la fonction {funcindex}`np.linspace` qui revient souvent:
`np.linspace(0, 10)` utilise par défaut `num=50` et `endpoint=True` (cf. [Aide et documentation](help.md) pour savoir).

Voir aussi les pages [Variables](variables.md), [Fonctions définies par
l'utilisateur](user-functions.md) et [Fonctions usuelles](common-functions.md).

## Blocs et indentation

Python organise les instructions d’un programme en **blocs**. Contrairement à d’autres langages, qui utilisent par exemple des accolades `{...}`, Python délimite ces blocs à l’aide de l’**indentation**, c’est-à-dire des espaces placés au début des lignes.

Les instructions situées au niveau principal du programme commencent normalement tout à gauche. Certaines constructions, comme `if`, `else`, `for`, `while` ou `def`, se terminent par le caractère `:` et introduisent un bloc indenté. Toutes les instructions appartenant à ce bloc doivent avoir le même niveau d’indentation.

Dans l’exemple suivant, les deux affectations placées après `if` appartiennent au premier bloc, tandis que celles placées après `else` appartiennent au second :

```python
if fa * fc > 0:
    a = c
    fa = fc
else:
    b = c
    fb = fc

c = (a + b) / 2
fc = f(c)
```

Les deux dernières instructions ne sont plus indentées : elles se trouvent donc en dehors de la structure conditionnelle et sont exécutées après celle-ci, quelle que soit la branche choisie.

Un bloc peut lui-même contenir d’autres blocs. Chaque niveau d’imbrication reçoit alors une indentation supplémentaire :

```python
if x >= 0:
    if x == 0:
        print("x is zero")
    else:
        print("x is positive")
else:
    print("x is negative")
```

La convention recommandée consiste à utiliser **quatre espaces par niveau d’indentation**, conformément à la section [Indentation de la PEP 8](https://peps.python.org/pep-0008/#indentation). Il est déconseillé d’utiliser des tabulations et, surtout, de mélanger espaces et tabulations dans un même fichier.

L’indentation n’est donc pas seulement une question de présentation : elle détermine directement la structure et le sens du programme. Une indentation absente ou incohérente provoque généralement une `IndentationError`. Le mélange ambigu de tabulations et d’espaces peut produire une `TabError`. Une indentation syntaxiquement valide mais placée au mauvais niveau peut être plus difficile à détecter : le programme s’exécute, mais son comportement ne correspond pas nécessairement à celui qui était attendu. Voir la page consacrée aux [erreurs classiques](common-errors.md).

Les lignes vides n’interrompent pas un bloc. En pratique, elles peuvent être utilisées avec modération pour séparer visuellement les différentes étapes d’un programme. Pour les structures nécessitant des blocs plus élaborés, voir les [structures de contrôle](control-flow.md).
