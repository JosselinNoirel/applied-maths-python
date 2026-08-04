# `numpy.linspace`

```{raw} html
<p class="language-switch"><a href="../../en/reference/numpy-linspace.html">English</a></p>
```

```{py:function} numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

Renvoie `num` valeurs régulièrement espacées dans l'intervalle allant de `start`
à `stop`.
```

## Syntaxe minimale

```python
import numpy as np

x = np.linspace(debut, fin, nombre)
```

Le résultat est un tableau NumPy contenant `nombre` valeurs. Par défaut, les
deux bornes sont incluses.

## Paramètres utiles pour débuter

`start`
: Première valeur de l'intervalle.

`stop`
: Dernière valeur de l'intervalle lorsque `endpoint=True`.

`num`
: Nombre de points. Il doit s'agir d'un entier positif ou nul ; sa valeur par
  défaut est `50`.

`endpoint`
: Si sa valeur est `True`, `stop` est inclus. Si elle est `False`, `stop` est
  exclu et l'espacement est modifié.

## Exemple : échantillonner une fonction

Échantillonnons $f(x)=x^2$ en cinq points sur $[-1,1]$ :

```python
import numpy as np

x = np.linspace(-1, 1, 5)
y = x**2
```

On obtient :

```text
x = [-1.  -0.5  0.   0.5  1. ]
y = [ 1.   0.25 0.   0.25 1. ]
```

## Comportement des bornes

```python
import numpy as np

ferme = np.linspace(0, 1, 5)
semi_ouvert = np.linspace(0, 1, 5, endpoint=False)
```

`ferme` contient `1` ; `semi_ouvert` se termine par `0.8`. Ce dernier cas est
utile pour un maillage périodique, où le premier et le dernier point
représenteraient sinon la même position.

## Erreur classique

Le troisième argument est un **nombre de points**, et non un pas :

```python
np.linspace(0, 1, 0.1)  # incorrect : 0.1 n'est pas un nombre de points
np.linspace(0, 1, 11)   # 11 points séparés par un pas de 0.1
```

Pour l'API de référence et les options avancées, consultez la
[documentation officielle de NumPy](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html).

