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

## Résoudre

Pour un système carré de rang plein, utilisez
[`numpy.linalg.solve`](../reference/numpy-linalg-solve.md).

```python
x = np.linalg.solve(A, b)
verified = np.allclose(A @ x, b, rtol=1e-9, atol=1e-12)
```

Cette fonction résout directement le système, sans calculer explicitement
l'inverse de `A`. Elle exige une matrice carrée et peut lever
`np.linalg.LinAlgError` si la matrice est singulière. Une matrice presque
singulière peut produire un résultat sans erreur Python, mais avec une forte
sensibilité aux erreurs d'arrondi ou aux données.

## Pseudoinverse

Pour une matrice rectangulaire ou de rang insuffisant, on peut chercher une
solution au sens des {concept}`moindres carrés`, qui minimise
$\lVert Ax-b\rVert_2$. La {concept}`pseudoinverse` permet de calculer cette
solution ; parmi plusieurs minimisateurs, elle sélectionne celui de norme
euclidienne minimale.

```python
C = np.array([[1.0, 0.0],
              [1.0, 1.0],
              [1.0, 2.0]])
d = np.array([1.0, 2.0, 2.0])

x_pinv = np.linalg.pinv(C) @ d
residual = C @ x_pinv - d
```

Ici, trois équations contraignent deux inconnues, et il n'existe pas de
solution exacte : le résidu reste non nul. Pour effectuer directement le
calcul des moindres carrés, on peut utiliser :

```python
x_lstsq, residual_sums, rank, singular_values = np.linalg.lstsq(C, d, rcond=None)
```

`residual_sums` contient la somme des carrés des résidus lorsque la matrice a
plus de lignes que de colonnes et possède un rang colonne plein ; ce tableau
est vide dans les autres cas. Calculez donc `C @ x_lstsq - d` pour examiner
le résidu dans tous les cas. Ces méthodes utilisent un seuil numérique pour
traiter les valeurs singulières trop petites et ne suppriment pas les
difficultés liées à un mauvais conditionnement.
