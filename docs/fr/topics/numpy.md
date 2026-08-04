# Bibliothèque NumPy

```{raw} html
<p class="language-switch"><a href="../../en/topics/numpy.html">English</a></p>
```

NumPy fournit des tableaux numériques et des fonctions conçues pour agir sur
toutes leurs valeurs. L'import conventionnel est :

```python
import numpy as np
```

Le préfixe `np.` désigne l'espace de noms de NumPy : `np.sqrt`, par exemple, est
la fonction racine carrée de NumPy.

## Générer des tableaux

### Grille régulière

[`np.linspace`](../reference/numpy-linspace.md) crée un nombre choisi de points
régulièrement espacés entre deux bornes :

```python
x = np.linspace(-2, 3, 101)
```

### Suite d'entiers ou pas fixé

`np.arange(start, stop, step)` utilise un pas fixé et exclut la borne `stop` :

```python
indices = np.arange(0, 10, 2)
```

Pour un intervalle de flottants dont les deux bornes importent, préférez souvent
`linspace`, qui évite les ambiguïtés dues aux arrondis successifs.

### Initialiser et saisir un tableau

```python
vide = np.empty(5)       # valeurs non initialisées
zeros = np.zeros(5)      # cinq zéros
ones = np.ones(5)        # cinq uns
data = np.array([-3.71, 1.43, -2.49, 7.21])
```

N'utilisez les valeurs de `np.empty` qu'après les avoir remplacées.

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
moyenne = np.mean(data)
minimum = np.min(data)
maximum = np.max(data)
ecart_type = np.std(data)
variance = np.var(data)
```

## Fonctions mathématiques fréquentes

| Mathématiques | NumPy |
|---|---|
| $\sqrt{x}$ | `np.sqrt(x)` |
| $\exp(x)$ | `np.exp(x)` |
| $\log(x)$ | `np.log(x)` |
| $\log_{10}(x)$ | `np.log10(x)` |
| $\sin(x)$, $\cos(x)$ | `np.sin(x)`, `np.cos(x)` |
| $\lvert x\rvert$ | `np.abs(x)` |
| arrondi | `np.round(x)` |

Les fonctions trigonométriques utilisent des angles exprimés en radians.

