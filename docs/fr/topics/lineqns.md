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
```

Les deux approches suivantes peuvent être employées:

```python
np.linalg.norm(A @ x - b) # Residual
```

Le {concept}`résidu` est la différence $A \cdot x - b$.
Le résidu est mathématiquement égal à zéro pour une solution; numériquement, on peut simplement regarder si la norme du résidu est assez faible.

```python
np.allclose(A @ x, b, rtol=1e-9, atol=1e-12)
```

On utilise `np.allclose` pour vérifier que toutes les composantes du vecteur $A \cdot x$ sont à peu près égales à celles du vecteur $b$.
Il faut recourir à une égalité _à peu près_ plutôt qu'une
égalité exacte car les calculs flottants comportent des erreurs d'arrondi.

## Déterminant et rang

Pour une matrice carrée $A$ $n\times n$, les propriétés suivantes
sont mathématiquement équivalentes: le déterminant est non nul, le
rang vaut $n$ et chaque équation $A \cdot x = b$ admet une solution unique, quelque soit $b$.

```python
np.linalg.det(A)
np.linalg.matrix_rank(A)
```

## Résolution

### Matrice carrée de rang plein

Si $A$ est de taille $n\times n$ et de rang $n$, chaque second membre
$b$ admet une solution unique. Utilisez
[`numpy.linalg.solve`](../reference/numpy-linalg-solve.md).

```python
x = np.linalg.solve(A, b)
```

Si la matrice est singulière, `solve` peut lever une exception
`np.linalg.LinAlgError`. Si elle est presque singulière, le résultat
peut être très sensible aux erreurs d'arrondi ou aux perturbations des données.

### Matrice carrée de rang insuffisant

Lorsque le rang est inférieur à $n$, le système admet une infinité de
solutions exactes si $b$ appartient à l'image de $A$, et aucune sinon.
Par exemple, les deux lignes de `S` ci-dessous imposent la même équation
$x_1+x_2=2$. Parmi toutes les solutions, `np.linalg.lstsq` renvoie
celle de norme euclidienne minimale, ici $(1, 1)$ à l'arrondi près.

```python
S = np.array([[1.0, 1.0], [2.0, 2.0]])
c = np.array([2.0, 4.0])

x = np.linalg.lstsq(S, c, rcond=None)[0]
```

Si l'on remplace le second membre par `[2.0, 5.0]`, les deux
équations deviennent incompatibles. La même fonction donne alors une
solution au sens des {concept}`moindres carrés`, qui minimise
$\| S \cdot x-c \|$.  On peut calculer la norme du résidu pour savoir quelle est la situation:
la norme `np.linalg.norm(S @ x - c)` vaut (approximativement) zéro si une solution (au moins) existe et
est (significativement) différente de zéro quand il n'y aucune solution.

### Matrice rectangulaire

- **Plus d'équations que d'inconnues ($m>n$).** Le système est
  *surdéterminé*. Un second membre quelconque peut être incompatible
  avec les équations. Si les colonnes sont indépendantes, il existe
  un unique minimisateur de $\| A \cdot x - b\|$. Ce minimisateur
  est une solution exacte lorsque le système est compatible.
- **Moins d'équations que d'inconnues ($m < n$).** Le système est
  *sous-déterminé*. Si les lignes sont indépendantes, tout second
  membre admet une infinité de solutions exactes. On peut alors choisir
  celle de norme minimale. Si le rang est inférieur à $m$, certains
  seconds membres n'admettent aucune solution exacte.

## Inverse et pseudo-inverse

### Interprétation mathématique

Si $A$ est carrée et inversible, son inverse $A^{-1}$ vérifie
$A^{-1}A = A \cdot A^{-1} = I$. L'équation $A \cdot x=b$ a pour solution
on obtient $x=A^{-1}b$.

La {concept}`pseudo-inverse de Moore-Penrose` $A^+$ existe aussi pour
les matrices rectangulaires ou singulières. Le vecteur $A^+ \cdot b$ minimise
$\|A \cdot x - b\|$.

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
