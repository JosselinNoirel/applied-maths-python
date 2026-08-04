# Fonctions définies par l'utilisateur

```{raw} html
<p class="language-switch"><a href="../../en/topics/user-functions.html">English</a></p>
```

Le mot-clé `def` donne un nom à un calcul réutilisable. Le bloc indenté est le
corps de la fonction ; `return` renvoie un résultat à l'appelant.

```python
def energie_cinetique(masse, vitesse):
    """Renvoie 1/2 m v²."""
    return 0.5 * masse * vitesse**2


energie_cinetique(2, 3)
```

Le résultat est `9.0`. Les paramètres comme `masse` sont locaux à la fonction.

L'indentation délimite le corps de la fonction. Sans elle, Python ne peut pas
déterminer quelles instructions appartiennent à la définition.

## Fonction mathématique

```python
import numpy as np

def f(x):
    return np.exp(np.abs(np.sin(x)))
```

Cette définition fonctionne avec un nombre ou avec un tableau NumPy. Elle rend
le programme plus proche de l'écriture mathématique et permet de modifier la
fonction étudiée en un seul endroit.

## Fonction programmatique

Une fonction peut également automatiser plusieurs instructions :

```python
def somme_positive(valeurs):
    total = 0.0
    for valeur in valeurs:
        if valeur > 0:
            total = total + valeur
    return total
```

`total` et `valeur` sont locales. L'appel {funcindex}`somme_positive`(`[9, -5, 5, 6]`)
renvoie `20.0`.
