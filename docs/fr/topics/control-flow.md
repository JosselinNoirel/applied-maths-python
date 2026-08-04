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

Utilisez une boucle `for` pour parcourir des valeurs connues :

```python
squares = []
for n in range(5):
    squares.append(n**2)
```

Lorsque la position et la valeur sont toutes deux nécessaires, utilisez
`enumerate` plutôt qu'un compteur mis à jour manuellement :

```python
values = [2.0, 3.5, 4.1]
for index, value in enumerate(values):
    print(index, value)
```

Voir la [référence de `range` et `enumerate`](../reference/python-builtins.md).

Utilisez `while` lorsque la répétition continue jusqu'à ce qu'une condition
change. Vérifiez que le corps de la boucle peut rendre cette condition fausse.
