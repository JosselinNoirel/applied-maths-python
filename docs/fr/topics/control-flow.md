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
    etat = "glace"
else:
    etat = "eau liquide"
```

## Boucles

Utilisez une boucle `for` pour parcourir des valeurs connues :

```python
carres = []
for n in range(5):
    carres.append(n**2)
```

Utilisez `while` lorsque la répétition continue jusqu'à ce qu'une condition
change. Vérifiez que le corps de la boucle peut rendre cette condition fausse.
