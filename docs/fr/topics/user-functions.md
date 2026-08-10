# Fonctions définies par l'utilisateur

```{raw} html
<p class="language-switch"><a href="../../en/topics/user-functions.html">English</a></p>
```

## Principe général

Le mot-clé {funcindex}`def` donne un nom à une recette de calcul réutilisable, une **fonction**.
Le nom de la fonction suit les mêmes conventions qu'un [nom de variable](variables.md). Le bloc indenté est le
corps de la fonction; {funcindex}`return` indique quel est le résultat que la fonction renvoie à l'appelant.

À noter que `return` peut intervenir à plusieurs reprises dans une fonction. Le premier `return` atteint provoque la sortie de la fonction avec le résultat en question.

Il est possible (et recommandé d'inclure une {index}`docstring`) documentant la fonction dans la ou les lignes suivant la ligne du `def`.

```python
def kinetic_energy(mass, velocity):
    """Return 1/2 m v²."""
    return 0.5 * mass * velocity**2

kinetic_energy(2, 3)
```

Le résultat est `9.0`. Les paramètres comme `mass` sont locaux à la fonction. La chaîne de caractère
`"""Return 1/2 m v²."""` fournit la documentation docstring de la fonction.

L'indentation délimite le corps de la fonction. Sans elle, Python ne peut pas
déterminer quelles instructions appartiennent à la définition.

## Fonction mathématique

L'application la plus simple que l'on voit permet de coller aux notations mathématiques.  Quand on dit: soit $f$ la fonction $x \mapsto e^{|\sin x|}$, il est pratique de définir

```python
import numpy as np

def f(x):
    '''Returns e^{|sin x|} where x is a number or a 1D NumPy array'''
    return np.exp(np.abs(np.sin(x)))
```

Cette définition fonctionne avec un nombre ou avec un tableau NumPy (c'est utile de l'indiquer dans la documentation). Elle rend
le programme plus proche de l'écriture mathématique et permet de modifier la
fonction étudiée en un seul endroit. (Cela permet de penser de façon *modulaire*.)

## Fonction programmatique

Une fonction peut également automatiser plusieurs instructions :

```python
def positive_sum(values):
    '''Given a list of values (list or 1D NumPy array),
       returns the sum of the values that are > 0.'''
    total = 0.0
    for value in values:
        if value > 0:
            total = total + value
    return total
```

Dans ce cas, les variables `total` et `value` sont locales (cf. aussi *Portée locale* des [Variables définies par l'utilisateur](variables.md)). L'appel `positive_sum([9, -5, 5, 6])`
renvoie `20.0`.
