# Structures de contrôle

```{raw} html
<p class="language-switch"><a href="../../en/topics/control-flow.html">English</a></p>
```

Les [structures de contrôle](https://docs.python.org/3/tutorial/controlflow.html#match-statements) déterminent quelles instructions sont exécutées et
combien de fois. Elles s'écrivent sous la forme d'un instruction suivie de blocs indentés d'une ou plusieurs lignes.

````{warning}
Il n'est pas possible d'utiliser un bloc vide. Python fournit la commande `pass` (qui ne fait strictement rien) pour des blocs fonctionnellement vides.

```Python
if n is None:
    pass
else:
    x = np.linspace(0, 1, num=param)
```
````

Les expressions utilisées après `if` et `while` doivent être des booléens et sont détaillées dans
[Conditions booléennes](boolean-conditions.md).

## Conditions *if - then - else*

Les conditions if - then - else ont la structure suivante

```python
if fa * gc > 0:
    a = c
    fa = fc
else:
    b = c
    fb = fc
```

La partie `else`

```python
if param is None:
    param = 1.0
```

````{note}
:class: dropdown

Il existe également un mot clef `elif` permettant de faire plusieurs tests à la suite

```Python
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
```

Une structure proche est `match`

```Python
match status:
    case 400:
        return "Bad request"
    case 401 | 403 | 404:
        return "Not allowed"
    case 404:
        return "Not found"
    case 418:
        return "I'm a teapot"
    case _:
        return "Something's wrong with the internet"
```
````

## Boucle *for*

Utilisez une boucle `for` pour parcourir des valeurs connues. Cela peut être les valeurs contenues dans une liste,
les valeurs contenues dans un tableau NumPy ou encore des valeurs produites par des *itérateurs* comme `range`:

```python
squares = []
for k in range(5):
    squares.append(k**2)
```

Dans cet exemple, {funcindex}`range` produit une séquence d'entiers $k$ de $0$ à $4$
(cf. [Fonctions usuelles](common-functions.md) et la [référence de `range` et `enumerate`](../reference/python-builtins.md)) et
la méthode `append` permet d'aggréger chaque carré dans la list `squares`
(cf. [Objets Python](python-objects.md)).

Il est fréquent que `range` prenne pour argument la longueur d'une liste ou d'un tableau

```Python
s = 0.
for k in range(len(squares)):
    s += 1/squares[k]
```

Lorsque la position et la valeur sont toutes deux nécessaires, utilisez
`enumerate`:

```python
values = [2.0, 3.5, 4.1]
for k, value in enumerate(values):
    print(k, value)
```

Voir la [référence de `range` et `enumerate`](../reference/python-builtins.md).

## Boucle *while*

Utilisez `while` lorsque la répétition continue jusqu'à ce qu'une condition
devienne fausse. La boucle suivante se lit ainsi «améliorer les bornes $a$ et $b$ tant que la précision n'est pas satisfaisante»:

```Python
while abs(b - a) > tol:
    a = lowerbound(f, a, b)
    b = upperbound(f, a, b)
```

Vérifiez que le corps de la boucle peut rendre cette condition fausse (sinon vous entrez dans une boucle infinie, cf. [Erreurs classiques](common-errors.md)). Une utilisation classique en est la lecture d'un fichier jusqu'à épuisement des données:

```Python
with open('dictionary.txt', 'r') as file:
    while line := file.readline():
        line.rstrip()

        # Process line
```

(Noter l'utilisation de l'[affectation](variables.md) avec `:=`)

TODO: Truthiness de `line := file.readline()`.
