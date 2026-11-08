# Système d'équations linéaires

```{raw} html
<p class="language-switch"><a href="../../en/topics/lineqns.html">English</a></p>
```

Un {concept}`système linéaire` s'écrit $Ax=b$, où $A$ contient les
coefficients, $x$ les inconnues et $b$ le second membre. Pour $m$ équations
et $n$ inconnues, on utilise une matrice de forme `(m, n)`, un vecteur
inconnu de forme `(n,)` et un second membre de forme `(m,)`.
Voir les [matrices et vecteurs](matrix.md).

## Vérifier une solution

Considérons le système

$$
\begin{cases}
3x_1-x_2=7,\\
2x_1+4x_2=10.
\end{cases}
$$

Pour vérifier une solution proposée, on calcule le produit matriciel avec
`@`, puis on le compare au second membre.

```python
import numpy as np

A = np.array([[3.0, -1.0], [2.0, 4.0]])
b = np.array([7.0, 10.0])
x = np.array([19.0 / 7.0, 8.0 / 7.0])

residual = A @ x - b
is_solution = np.allclose(A @ x, b, rtol=1e-9, atol=1e-12)
residual_norm = np.linalg.norm(residual)
```

Le {concept}`résidu` est $Ax-b$. On utilise `np.allclose` plutôt qu'une
égalité exacte, car les calculs flottants comportent des erreurs d'arrondi.
Les tolérances relative `rtol` et absolue `atol` doivent être choisies en
fonction de l'échelle et de la précision des données. Un petit résidu indique
que les équations sont bien satisfaites numériquement ; il ne garantit pas
que les inconnues soient précises si le système est mal conditionné.

## Déterminant et rang

Pour une matrice carrée de taille $n\times n$, les propriétés suivantes
sont équivalentes en arithmétique exacte : le déterminant est non nul, le
rang vaut $n$, et chaque second membre admet une solution unique.

```python
determinant = np.linalg.det(A)
rank = np.linalg.matrix_rank(A)
condition_number = np.linalg.cond(A)
```

Numériquement, le rang est estimé avec une tolérance. Tester seulement
`determinant == 0` n'est pas une méthode fiable pour décider si une matrice
est proche d'une matrice singulière : le déterminant dépend notamment de
l'échelle des coefficients. Un grand {concept}`nombre de conditionnement`
indique que de petites perturbations des données peuvent entraîner de grandes
variations de la solution.

Plus généralement, un système admet une solution exacte si et seulement si
$\operatorname{rang}(A)=\operatorname{rang}([A\mid b])$, où $[A\mid b]$
est la matrice augmentée. Si ce rang commun est égal au nombre d'inconnues,
la solution est unique ; sinon, il existe une infinité de solutions. Sur des
données flottantes ou bruitées, cette comparaison de rangs exige de tenir
compte des tolérances numériques.

## Résolution

### Matrice carrée de rang plein

Si $A$ est de taille $n\times n$ et de rang $n$, chaque second membre
$b$ admet une solution unique. Utilisez
[`numpy.linalg.solve`](../reference/numpy-linalg-solve.md).

```python
x = np.linalg.solve(A, b)
verified = np.allclose(A @ x, b, rtol=1e-9, atol=1e-12)
```

Si la matrice est singulière, `solve` peut lever une exception
`np.linalg.LinAlgError`. Si elle est presque singulière, le résultat
peut être très sensible aux erreurs d'arrondi ou aux perturbations des données.

### Matrice carrée de rang insuffisant

Lorsque le rang est inférieur à $n$, le système admet une infinité de
solutions exactes si $b$ appartient à l'image de $A$, et aucune sinon.
Par exemple, les deux lignes de `S` ci-dessous imposent la même équation
$x_1+x_2=2$. Parmi toutes les solutions, `np.linalg.lstsq` renvoie
celle de norme euclidienne minimale, ici $(1,1)$ à l'arrondi près.

```python
S = np.array([[1.0, 1.0], [2.0, 2.0]])
c = np.array([2.0, 4.0])

x, _, rank, _ = np.linalg.lstsq(S, c, rcond=None)
residual = S @ x - c
```

Si l'on remplace le second membre par `[2.0, 5.0]`, les deux
équations deviennent incompatibles. La même fonction donne alors une
solution au sens des {concept}`moindres carrés`, qui minimise
$\lVert Sx-c\rVert_2$. S'il existe plusieurs minimisateurs, elle
renvoie celui de norme minimale.

### Matrice rectangulaire

- **Plus d'équations que d'inconnues ($m>n$).** Le système est
  *surdéterminé*. Un second membre quelconque peut être incompatible
  avec les équations. Si les colonnes sont indépendantes, il existe
  un unique minimisateur de $\lVert Ax-b\rVert_2$. Ce minimisateur
  est une solution exacte lorsque le système est compatible.
- **Moins d'équations que d'inconnues ($m<n$).** Le système est
  *sous-déterminé*. Si les lignes sont indépendantes, tout second
  membre admet une infinité de solutions exactes. On peut alors choisir
  celle de norme minimale. Si le rang est inférieur à $m$, certains
  seconds membres n'admettent aucune solution exacte.

Dans les deux cas, utilisez `np.linalg.lstsq`. Dans l'exemple suivant,
les trois équations correspondent à l'ajustement d'une droite à trois
points. Les points ne sont pas alignés, donc le résidu est non nul.

```python
C = np.array([[1.0, 0.0],
              [1.0, 1.0],
              [1.0, 2.0]])
d = np.array([1.0, 2.0, 2.0])

x, residual_sums, rank, singular_values = np.linalg.lstsq(C, d, rcond=None)
residual = C @ x - d
```

Pour un second membre vectoriel, `residual_sums` contient la somme des
carrés du résidu si la matrice a plus de lignes que de colonnes et si ses
colonnes sont indépendantes. Dans les autres cas, le tableau est vide.
Calculez directement `A @ x - b` pour vérifier si les équations sont
satisfaites à la tolérance souhaitée.

## Inverse et pseudo-inverse

### Interprétation mathématique

Si $A$ est carrée et inversible, son inverse $A^{-1}$ vérifie
$A^{-1}A=AA^{-1}=I$. En multipliant $Ax=b$ à gauche par $A^{-1}$,
on obtient $x=A^{-1}b$.

La {concept}`pseudo-inverse de Moore-Penrose` $A^+$ existe aussi pour
les matrices rectangulaires ou singulières. Le vecteur $A^+b$ minimise
$\lVert Ax-b\rVert_2$. Parmi tous les minimisateurs, il est celui
dont la norme $\lVert x\rVert_2$ est la plus petite. Si le système
est compatible, c'est donc sa solution exacte de norme minimale.
Pour une matrice carrée inversible, $A^+=A^{-1}$.

### En pratique

Pour calculer seulement $x$, utilisez `np.linalg.solve(A, b)` si
$A$ est carrée et de rang plein. Pour une matrice rectangulaire ou
de rang insuffisant, utilisez `np.linalg.lstsq(A, b, rcond=None)`
et examinez le résidu. Ces fonctions calculent $x$ directement,
sans former la matrice inverse ou pseudo-inverse.

Utilisez `np.linalg.inv(A)` ou `np.linalg.pinv(A)` si vous avez
besoin de la matrice elle-même. Pour une matrice presque singulière,
le seuil retenu pour les petites valeurs singulières peut influer
sur le rang numérique et sur la solution.
