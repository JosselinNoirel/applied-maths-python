# System of linear equations

```{raw} html
<p class="language-switch"><a href="../../fr/topics/lineqns.html">Français</a></p>
```

A {concept}`linear system` is written as $Ax=b$, where $A$ contains the
coefficients, $x$ the unknowns and $b$ the right-hand side. For $m$ equations
and $n$ unknowns, use a matrix of shape `(m, n)`, an unknown vector of shape
`(n,)` and a right-hand side of shape `(m,)`.
See [matrices and vectors](matrix.md).

## Checking a solution

Consider the system

$$
\begin{cases}
3x_1-x_2=7,\\
2x_1+4x_2=10.
\end{cases}
$$

To check a proposed solution, compute the matrix product using `@`, then
compare it with the right-hand side.

```python
import numpy as np

A = np.array([[3.0, -1.0], [2.0, 4.0]])
b = np.array([7.0, 10.0])
x = np.array([19.0 / 7.0, 8.0 / 7.0])

residual = A @ x - b
is_solution = np.allclose(A @ x, b, rtol=1e-9, atol=1e-12)
residual_norm = np.linalg.norm(residual)
```

The {concept}`residual` is $Ax-b$. Use `np.allclose` rather than exact
equality because floating-point calculations involve rounding errors.
Choose the relative tolerance `rtol` and absolute tolerance `atol` according
to the scale and precision of the data. A small residual indicates that the
equations are satisfied numerically; it does not guarantee accurate unknowns
if the system is ill-conditioned.

## Determinant and rank

For a square $n\times n$ matrix, the following properties are equivalent in
exact arithmetic: the determinant is nonzero, the rank is $n$, and every
right-hand side has a unique solution.

```python
determinant = np.linalg.det(A)
rank = np.linalg.matrix_rank(A)
condition_number = np.linalg.cond(A)
```

Numerically, the rank is estimated using a tolerance. Testing only
`determinant == 0` is not a reliable way to decide whether a matrix is close
to singular: the determinant depends, among other things, on the scale of
the entries. A large {concept}`condition number` indicates that small
perturbations in the data can cause large changes in the solution.

More generally, a system has an exact solution if and only if
$\operatorname{rank}(A)=\operatorname{rank}([A\mid b])$, where $[A\mid b]$
is the augmented matrix. If this common rank equals the number of unknowns,
the solution is unique; otherwise, there are infinitely many solutions.
For floating-point or noisy data, this comparison of ranks requires
attention to numerical tolerances.

## Solving the system

For a square system of full rank, use
[`numpy.linalg.solve`](../reference/numpy-linalg-solve.md).

```python
x = np.linalg.solve(A, b)
verified = np.allclose(A @ x, b, rtol=1e-9, atol=1e-12)
```

This function solves the system directly without explicitly computing the
inverse of `A`. It requires a square matrix and may raise
`np.linalg.LinAlgError` if the matrix is singular. A nearly singular matrix
can produce a result without a Python error, but with high sensitivity to
rounding errors or the data.

## Pseudoinverse

For a rectangular or rank-deficient matrix, one can seek a
{concept}`least squares` solution, which minimises $\lVert Ax-b\rVert_2$.
The {concept}`pseudoinverse` computes this solution; when there are several
minimisers, it selects the one with the smallest Euclidean norm.

```python
C = np.array([[1.0, 0.0],
              [1.0, 1.0],
              [1.0, 2.0]])
d = np.array([1.0, 2.0, 2.0])

x_pinv = np.linalg.pinv(C) @ d
residual = C @ x_pinv - d
```

Here, three equations constrain two unknowns, and there is no exact solution:
the residual remains nonzero. To compute the least squares solution
directly, use:

```python
x_lstsq, residual_sums, rank, singular_values = np.linalg.lstsq(C, d, rcond=None)
```

`residual_sums` contains the sum of squared residuals when the matrix has
more rows than columns and has full column rank; this array is empty in
other cases. Compute `C @ x_lstsq - d` to examine the residual in all cases.
These methods use a numerical threshold to handle very small singular
values and do not remove the difficulties caused by ill-conditioning.
