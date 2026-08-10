# Bibliothèque NumPy

```{raw} html
<p class="language-switch"><a href="../../en/topics/numpy.html">English</a></p>
```

NumPy fournit des tableaux numériques et des fonctions conçues pour agir sur
toutes leurs valeurs. L'import conventionnel est :

```python
import numpy as np
```

Le préfixe `np.` désigne l'espace de noms de NumPy : {funcindex}`np.sqrt`, par exemple, est
la fonction racine carrée de NumPy.

## Générer des tableaux

### Tableau explicite

Un tableau peut être créé à partir de données explicites

```python
L = np.array([1, 2, 7, 2])
M = np.array([ [ 1, 2, 3], [ 4, 5, 6], [ 7, 8, 9] ]) # A 3 x 3 matrix
```

NB: Si des données sont trop conséquentes, il est courant de les stocker sous la forme d'un fichier externe.
Cf [Importer des données](data.md).

### Grille régulière

[{funcindex}`np.linspace`](../reference/numpy-linspace.md) crée un nombre choisi de points
régulièrement espacés entre deux bornes :

TODO. Image

```python
x = np.linspace(-1, 1, 5)
```

Ici, `x` vaut `array([-1. , -0.5, 0. , 0.5, 1. ])`. Consultez la
[fiche complète de {funcindex}`numpy.linspace`](../reference/numpy-linspace.md) pour les
règles sur les bornes, la valeur renvoyée, les exemples et les erreurs courantes.

### Suite d'entiers ou pas fixé

`np.arange(start, stop)` crée une liste d'entiers allant de `start` (inclus) à `stop` (exclu).

```python
indices = np.arange(0, 10)
```

`np.arange(start, stop, step)` utilise un pas fixé et exclut la borne `stop`:

```python
indices = np.arange(0, 10, 2)
```

Pour un intervalle de flottants dont les deux bornes importent, préférez souvent
`linspace`, qui évite les ambiguïtés dues aux arrondis successifs.

{funcindex}`np.arange` et {funcindex}`np.linspace`

Préférez une fonction qui exprime directement l'intention mathématique. Utilisez
par exemple {funcindex}`np.linspace`(`a, b, n`) lorsque le nombre de points importe, et
{funcindex}`np.arange`(`debut, fin, pas`) lorsque c'est l'incrément qui importe.

### Initialiser et saisir un tableau

```python
uninitialised = np.empty(5)
zeros = np.zeros(5)
ones = np.ones(5)
data = np.array([-3.71, 1.43, -2.49, 7.21])
```

N'utilisez les valeurs de {funcindex}`np.empty` qu'après les avoir remplacées.

## Calcul terme à terme

```python
x = np.linspace(0, 1, 5)
y = np.exp(-x) * np.sin(2 * np.pi * x)
```

Les opérateurs `+`, `-`, `*`, `/` et `**`, ainsi que les fonctions NumPy,
agissent sur chaque valeur du tableau. Cette écriture vectorisée est généralement
plus claire et plus rapide qu'une boucle Python.

## Résumer un tableau

```python
total = np.sum(data)
product = np.prod(data)
average = np.mean(data)
minimum = np.min(data)
maximum = np.max(data)
standard_deviation = np.std(data)
variance = np.var(data)
```

## Fonctions mathématiques fréquentes

| Mathématiques | NumPy |
|---|---|
| $\sqrt{x}$ | `np.sqrt(x)` |
| $\exp(x)$ | `np.exp(x)` |
| $\log(x)$ | `np.log(x)` |
| $\log_{10}(x)$ | `np.log10(x)` |
| $\sin(x)$ | `np.sin(x)` |
| $\cos(x)$ | `np.cos(x)` |
| $\lvert x\rvert$ | `np.abs(x)` |
| arrondi | `np.round(x)` |

Les fonctions trigonométriques utilisent des angles exprimés en radians (ayez recours sinon à la fonction {funcindex}`np.degrees`.)

Une liste des fonctions mathématiques disponibles est:
`acos`, `acosh`, `asin`, `asinh`, `atan`, `atan2`, `atanh`, `cbrt` (racine cubique), `ceil`, `cos`, `cosh`, `degrees` (conversion en degrés), `exp`, `exp2` ($2^x$),
`expm1` ($e^x - 1$, pour des raisons numériques), `fabs`, `floor`, `fmod`, `frexp`, `gcd`, `hypot` (distance euclidienne en dimension $n$),
`isclose` (cf. [Conditions booléennes](boolean-conditions.md)), `isfinite`, `isinf`, `isnan`, `lcm`, `ldexp`, `log`, `log10`, `log1p` ($\log(1 + x)$, pour des raisons numériques), `log2`, `modf`, `nextafter`, `pow`, `prod` (calculer le produit), `radians` (conversion en radians), `remainder`, `sin`, `sinh`, `sqrt`, `sum` (calculer la somme), `tan`, `tanh`, `trunc`

Par ailleurs la bibliothèque inclut les constantes suivantes `e` et `pi` ainsi que `inf` pour désigner l'infini (par exemple dans une borne d'intégration).

## Représentation des nombres

Lorsqu'elle est utilisée sur un tableau NumPy, une fonction NumPy retourne un tableau NumPy affiché de façon lisible comme une liste classique `[...]` enveloppée dans un objet NumPy de type *array*

```text
array([1.        , 1.11751907, 1.24884887, 1.39561243, 1.5596235 ,
       1.742909  , 1.94773404, 2.17662993, 2.43242545, 2.71828183])
```

En revanche, lorsqu'elle est utilisée sur un nombre à virgule, une fonction NumPy retourne un objet
de type `np.float64` sous la forme

```text
np.float64(3.3201169227365472)
```

NumPy prend en charge plusieurs précisions numériques
(`np.float16`, `np.float32`, `np.float64`, `np.longdouble`) quand
Python ne possède pour sa part qu’un seul type flottant usuel, float, équivalent à un nombre en double précision.

On peut former un résultat de type float avec la fonction {funcindex}`float` comme décrit dans la partie *Conversions* de
[Objets Python](python-objects.md).

## Référence détaillée

- [Créer des tableaux NumPy](../reference/numpy-array-creation.md)
- [Fonctions mathématiques avec NumPy](../reference/numpy-mathematics.md)
- [Grilles de coordonnées avec `meshgrid`](../reference/numpy-meshgrid.md)
- [Résoudre un système avec `numpy.linalg.solve`](../reference/numpy-linalg-solve.md)
- [Statistiques : `min`, `max`, `mean`, `std`](../reference/numpy-statistics.md)
- [Comparaison et interpolation : `isclose`, `allclose`, `interp`](../reference/numpy-comparison-interpolation.md)

Utilisez `np.isclose` pour comparer un ou plusieurs flottants terme à terme et
`np.allclose` lorsqu'un seul booléen doit résumer la comparaison de deux tableaux.
Utilisez `np.interp` pour une interpolation linéaire unidimensionnelle simple.
