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

### Grille régulière

[{funcindex}`np.linspace`](../reference/numpy-linspace.md) crée un nombre choisi de points
régulièrement espacés entre deux bornes :

```python
x = np.linspace(-2, 3, 101)
```

### Suite d'entiers ou pas fixé

{funcindex}`np.arange`(`start, stop, step`) utilise un pas fixé et exclut la borne `stop` :

```python
indices = np.arange(0, 10, 2)
```

Pour un intervalle de flottants dont les deux bornes importent, préférez souvent
`linspace`, qui évite les ambiguïtés dues aux arrondis successifs.

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
average = np.mean(data)
minimum = np.min(data)
maximum = np.max(data)
standard_deviation = np.std(data)
variance = np.var(data)
```

## Fonctions mathématiques fréquentes

| Mathématiques | NumPy |
|---|---|
| $\sqrt{x}$ | {funcindex}`np.sqrt`(`x`) |
| $\exp(x)$ | {funcindex}`np.exp`(`x`) |
| $\log(x)$ | {funcindex}`np.log`(`x`) |
| $\log_{10}(x)$ | {funcindex}`np.log10`(`x`) |
| $\sin(x)$, $\cos(x)$ | {funcindex}`np.sin`(`x`), {funcindex}`np.cos`(`x`) |
| $\lvert x\rvert$ | {funcindex}`np.abs`(`x`) |
| arrondi | {funcindex}`np.round`(`x`) |

Les fonctions trigonométriques utilisent des angles exprimés en radians.

## Référence détaillée

- [Créer des tableaux : `array`, `zeros`, `empty`, `arange`](../reference/numpy-array-creation.md)
- [Fonctions mathématiques : `exp`, `log`, `sqrt`, `sin`, `cos`, `abs`, `sum`](../reference/numpy-mathematics.md)
- [Grilles de coordonnées avec `meshgrid`](../reference/numpy-meshgrid.md)
- [Résoudre un système avec `numpy.linalg.solve`](../reference/numpy-linalg-solve.md)
- [Statistiques : `min`, `max`, `mean`, `std`](../reference/numpy-statistics.md)
- [Comparaison et interpolation : `isclose`, `allclose`, `interp`](../reference/numpy-comparison-interpolation.md)

Utilisez `np.isclose` pour comparer un ou plusieurs flottants terme à terme et
`np.allclose` lorsqu'un seul booléen doit résumer la comparaison de deux tableaux.
Utilisez `np.interp` pour une interpolation linéaire unidimensionnelle simple.
