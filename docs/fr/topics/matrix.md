# Matrices et vecteurs

```{raw} html
<p class="language-switch"><a href="../../en/topics/matrix.html">English</a></p>
```

## Matrices

Les matrices et les vecteurs sont représentés par des tableaux NumPy
(`array`). Une {concept}`matrice` est un tableau à deux dimensions : les
coefficients sont entrés ligne par ligne, avec une virgule entre les lignes.

```python
import numpy as np

A = np.array([[1,  1,  1],
              [2, -1, -1],
              [2,  0,  1],
              [1, -1,  1]])
```

`A.shape` renvoie `(4, 3)` : quatre lignes et trois colonnes. Les indices
commencent à zéro : `A[i, j]` désigne le coefficient de la ligne `i` et de
la colonne `j`. `A[i, :]` extrait une ligne et `A[:, j]` une colonne, sous
forme de tableaux à une dimension.

## Vecteurs

Un {concept}`vecteur` est généralement représenté par un tableau à une dimension.
On peut aussi utiliser un tableau à deux dimensions pour distinguer explicitement
un vecteur colonne d'un vecteur ligne.

```python
v = np.array([1.0, 2.0, 3.0])
column = v.reshape(3, 1)
row = v.reshape(1, 3)

print(v.shape)       # (3,)
print(column.shape)  # (3, 1)
print(row.shape)     # (1, 3)
```

Un tableau de forme `(3,)` ne possède pas de second axe : sa transposée
`v.T` est donc identique à `v`. En revanche, `column.T` est un vecteur ligne.
Pour résoudre un système linéaire, la représentation à une dimension est
souvent la plus simple.

## Matrices particulières

NumPy permet de construire directement plusieurs matrices usuelles.

```python
identity = np.eye(3)
zero = np.zeros((2, 3))
diagonal = np.diag([2.0, 4.0, 6.0])

nodes = np.array([1.0, 2.0, 3.0])
vandermonde = np.vander(nodes, N=3, increasing=True)
```

- `np.eye(3)` crée la matrice identité de taille $3\times3$.
- `np.zeros((2, 3))` crée une matrice nulle de deux lignes et trois colonnes.
- `np.diag` construit une matrice diagonale à partir d'un vecteur. Appliquée
  à une matrice, cette fonction en extrait la diagonale.
- `np.vander` construit une {concept}`matrice de Vandermonde`. Ici, chaque
  ligne vaut $[1, x_i, x_i^2]$. Sans `increasing=True`, les puissances sont
  rangées dans l'ordre décroissant.

## Opérations simples sur les matrices

Pour additionner ou soustraire deux matrices au sens usuel, elles doivent avoir
les mêmes dimensions. La multiplication par un scalaire agit sur chaque
coefficient ; elle permet aussi de former des combinaisons linéaires.

```python
B = np.array([[1.0, 2.0], [3.0, 4.0]])
C = np.array([[2.0, 0.0], [1.0, 2.0]])

matrix_sum = B + C
matrix_difference = B - C
scaled = 2 * B
linear_combination = 2 * B - 3 * C
```

Le {concept}`produit matriciel` s'écrit avec `@`. Si $A$ est de taille
$m\times n$ et $B$ de taille $n\times p$, alors $AB$ est de taille
$m\times p$ : le nombre de colonnes du premier facteur doit être égal au
nombre de lignes du second.

```python
product = B @ C
entrywise_product = B * C
transpose = B.T
rank = np.linalg.matrix_rank(B)
determinant = np.linalg.det(B)
```

`B * C` multiplie les coefficients deux à deux ; ce calcul est différent de
`B @ C`. Pour certaines formes différentes, NumPy étend automatiquement les
opérandes (*broadcasting*) : vérifiez donc les formes avant un calcul.

La {concept}`transposée` échange lignes et colonnes. Le {concept}`rang` est
le nombre de colonnes (ou de lignes) linéairement indépendantes.
`np.linalg.matrix_rank` l'estime numériquement avec une tolérance. Le
{concept}`déterminant` n'est défini que pour les matrices carrées ; en
arithmétique exacte, il est non nul si et seulement si la matrice est
inversible. Sa valeur flottante ne suffit pas à évaluer la fiabilité d'une
résolution numérique.

## Opérations simples sur les vecteurs

Les exemples suivants utilisent des tableaux à une dimension de même longueur.
L'addition, la soustraction et la multiplication par un scalaire se font
coefficient par coefficient.

```python
u = np.array([1.0, 0.0, 0.0])
v = np.array([0.0, 1.0, 0.0])

vector_sum = u + v
vector_difference = u - v
linear_combination = 2 * u - 3 * v
dot_product = u @ v
cross_product = np.cross(u, v)
norm = np.linalg.norm(u)
```

Pour des vecteurs réels, `u @ v` est le {concept}`produit scalaire` : il
renvoie un nombre. `np.linalg.norm(u)` calcule la {concept}`norme euclidienne`.
Le {concept}`produit vectoriel` `np.cross(u, v)` s'utilise ici pour deux
vecteurs de trois composantes ; le résultat est orthogonal aux deux facteurs,
et son sens dépend de leur ordre.

Pour construire une base orthonormale directe à partir de deux directions
non colinéaires, on normalise la première, puis leur produit vectoriel :

```python
a = np.array([1.0, 1.0, 0.0])
b = np.array([0.0, 1.0, 1.0])

e1 = a / np.linalg.norm(a)
normal = np.cross(e1, b)
e3 = normal / np.linalg.norm(normal)
e2 = np.cross(e3, e1)

Q = np.column_stack((e1, e2, e3))
x = np.array([2.0, 3.0, 4.0])
coordinates = Q.T @ x
reconstructed = Q @ coordinates
```

Les colonnes de `Q` forment la nouvelle base. `Q.T @ x` donne les coordonnées
d'un vecteur dans cette base et `Q @ coordinates` le reconstruit dans la base
initiale. Cette construction exige que `a` soit non nul et que les deux
directions ne soient pas colinéaires ; des directions presque colinéaires
rendent le calcul sensible aux erreurs d'arrondi.
