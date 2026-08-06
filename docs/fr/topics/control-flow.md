# Structures de contrôle

```{raw} html
<p class="language-switch"><a href="../../en/topics/control-flow.html">English</a></p>
```

Les structures de contrôle déterminent quelles instructions sont exécutées et
combien de fois.

Les expressions utilisées après `if` et `while` sont détaillées dans
[Conditions booléennes](boolean-conditions.md).

## Conditions

```python
temperature = 1.5

if temperature < 0:
    state = "ice"
else:
    state = "liquid water"
```

## Boucles

Utilisez une boucle `for` pour parcourir des valeurs connues:

```python
squares = []
for n in range(5):
    squares.append(n**2)
```

Dans cet exemple, {funcindex}`range` produit une séquence d'entiers de $0$ à $4$
(cf. [Fonctions usuelles](common-functions.md) et la [référence de `range` et `enumerate`](../reference/python-builtins.md)) et
la méthode {funcindex}`append` permet d'aggréger chaque carré dans la list `squares`
(cf. [Objets Python](python-objects.md)).

Lorsque la position et la valeur sont toutes deux nécessaires, utilisez
`enumerate`:

```python
values = [2.0, 3.5, 4.1]
for index, value in enumerate(values):
    print(index, value)
```

Voir la [référence de `range` et `enumerate`](../reference/python-builtins.md).

Utilisez `while` lorsque la répétition continue jusqu'à ce qu'une condition
devienne fausse. Vérifiez que le corps de la boucle peut rendre cette condition fausse (sinon vous entrez dans une boucle infinie, cf. [Erreurs classiques](common-errors.md)). Une utilisation classique en est la lecture d'un fichier jusqu'à épuisement des données:

```Python
with open('dictionary.txt', 'r') as file:
    while line := file.readline():
        line.rstrip()

        # Process line
```

(Noter l'utilisation de l'[affectation](variables.md) avec `:=`)
