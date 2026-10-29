# Matrices et vecteurs

```{raw} html
<p class="language-switch"><a href="../../en/topics/matrix.html">English</a></p>
```

## Matrices

Les matrices et les vecteurs sont représentés par des tableaux NumPy
(`array`). Une {concept}`matrice` est un tableau à deux dimensions: les
coefficients sont entrés ligne par ligne, avec une virgule entre les lignes.

```python
import numpy as np

A = np.array([ [1,  1,  1],
               [2, -1, -1],
               [2,  0,  1],
               [1, -1,  1] ])
```

`A.shape` renvoie `(4, 3)`: quatre lignes et trois colonnes.

`A[i, j]` désigne le coefficient de la ligne `i` et de la colonne `j`.
**Attention:** Les indices commencent à zéro. 

`A[i, :]` extrait une ligne et `A[:, j]` une colonne.

## Vecteurs

Un {concept}`vecteur` est généralement représenté par un tableau à une dimension.
On peut aussi utiliser un tableau à deux dimensions pour distinguer explicitement
un vecteur colonne d'un vecteur ligne.

```python
v = np.array([1.0, 2.0, 3.0])                # As 1D vector
v = np.array([ [ 1.0, 2.0, 3.0] ])           # 2D row vector
v = np.array([ [ 1.0 ], [ 2.0 ], [ 3.0 ] ])  # 2D column vector
```

La représentation à une dimension est souvent la plus simple.

## Matrices particulières

NumPy permet de construire directement plusieurs matrices usuelles.

```python
np.identity(3)                # Identity matrix
np.zeros( (2, 3) )            # Null matrix
np.diag([2.0, 4.0, 6.0])      # Diagonal matrix

# Vandermonde matrix (full rank)
np.vander([1.0, 2.0, 3.0], N=3, increasing=True)
```

- `np.identity(3)` crée la matrice identité de taille $3\times3$.
- `np.zeros((2, 3))` crée une matrice nulle de deux lignes et trois colonnes.
- `np.diag` construit une matrice diagonale à partir d'un vecteur. Appliquée
  à une matrice, cette fonction en extrait la diagonale.
- `np.vander` construit une {concept}`matrice de Vandermonde`. Ici, chaque
  ligne vaut $[1, x_i, x_i^2]$. Sans `increasing=True`, les puissances sont
  rangées dans l'ordre décroissant.

## Opérations simples sur les matrices

Pour additionner ou soustraire deux matrices au sens usuel, elles doivent avoir
les mêmes dimensions. La multiplication par un scalaire agit sur chaque
élément; elle permet aussi de former des combinaisons linéaires.

```python
B = np.array([[1.0, 2.0], [3.0, 4.0]])
C = np.array([[2.0, 0.0], [1.0, 2.0]])

B + C          # Addition
B - C          # Difference
2 * B          # Multiplication by a scalar
2 * B - 3 * C  # Linear combination
```

Le {concept}`produit matriciel` s'écrit avec `@`. Si $A$ est de taille
$m\times n$ et $B$ de taille $n\times p$, alors $A \cdot B$ est de taille
$m\times p$: le nombre de colonnes du premier facteur doit être égal au
nombre de lignes du second.

```python
B @ C
```

**Attention:** `B * C` est une multiplication terme à terme et les deux matrices
doivent avoir les mêmes dimensions dans ce cas.

```
B.T                       # Transpose
np.linalg.matrix_rank(B)  # Rank
np.linalg.det(B)          # Determinant (for square matrices)
```

- La {concept}`transposée` échange lignes et colonnes.
- Le {concept}`rang` est
le nombre de colonnes (ou de lignes) linéairement indépendantes.
`np.linalg.matrix_rank` l'estime numériquement avec une tolérance.
- Le {concept}`déterminant` n'est défini que pour les matrices carrées; en
arithmétique exacte, il est non nul si et seulement si la matrice est
inversible.

## Opérations simples sur les vecteurs

Les exemples suivants utilisent des tableaux à une dimension de même longueur.
L'addition, la soustraction et la multiplication par un scalaire se font
coefficient par coefficient.

```python
u = np.array([1.0, 0.0, 0.0])
v = np.array([0.0, 1.0, 0.0])

u + v              # Sum of vectors
u - v              # Difference
2 * u - 3 * v      # Linear combination
u @ v              # Dot product
np.cross(u, v)     # Cross product
np.linalg.norm(u)  # Norm
```

Pour des vecteurs réels, `u @ v` est le {concept}`produit scalaire` : il
renvoie un nombre. Le produit scalaire est nul si les deux vecteurs sont orthogonaux.

`np.linalg.norm(u)` calcule la {concept}`norme euclidienne`.
Le {concept}`produit vectoriel` `np.cross(u, v)` s'utilise ici pour deux
vecteurs de trois composantes; le résultat est orthogonal aux deux facteurs,
et son sens dépend de leur ordre.

## Changement de base

Pour créer un vecteur unitaire à partir d'un vecteur quelconque $e$ (non nul),
on calcule $e = e/\|e\|$:

```Python
e = np.array([1, 2, 1])
e = e/np.linalg.norm(e)
```

Lorsque l'on cherche à exprimer les composantes (coordonnées) d'un vecteur $x$
dans une base orthonormée $(e_1, e_2, \dots)$

$$
  x = x_1 e_1 + x_2 e_2 + \cdots
$$

où $x_i = x \cdot e_i$.

Si la base est orthonormale mais non orthonormée

$$
  x = x_1 e_1 + x_2 e_2 + \cdots
$$

où $x_i = x \cdot e_i/\|e_i\|$.
