# Variables définies par l'utilisateur

```{raw} html
<p class="language-switch"><a href="../../en/topics/variables.html">English</a></p>
```

Une variable associe un nom à un objet. L'affectation utilise `=` ; l'égalité
mathématique se teste avec `==`.

```python
mass = 2.5
acceleration = 9.81
force = mass * acceleration

force == 24.525
```

Choisissez des noms explicites comme `vitesse_initiale`. Un nom ne peut ni
contenir d'espace ni commencer par un chiffre. Python distingue les majuscules
des minuscules.

Une affectation peut réutiliser la valeur précédente :

```python
k = 10
k = k + 1
```

Le résultat est `11`. Cette instruction Python n'est pas l'équation mathématique
$k=k+1$ : elle calcule d'abord le membre de droite, puis remplace la valeur de
`k`.

## Bien nommer une variable

Des noms courts comme `i`, `j`, `k`, `x` et `y` conviennent aux indices et aux
quantités mathématiques éphémères. Pour une valeur conservée plus longtemps,
préférez un nom descriptif comme `nombre_points` ou `vitesse_initiale`. Évitez de
réutiliser le nom d'une fonction comme {funcindex}`sum`, {funcindex}`min` ou {funcindex}`max`.

## Portée locale

Une variable créée dans une fonction est locale à cette fonction. Elle n'est pas
accessible après l'appel, sauf si la fonction la renvoie avec `return`.
