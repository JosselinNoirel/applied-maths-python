# Matrices and vectors

```{raw} html
<p class="language-switch"><a href="../../fr/topics/matrix.html">Français</a></p>
```

## Matrices

Matrices and vectors are represented by NumPy arrays (`array`). A
{concept}`matrix` is a two-dimensional array: enter its entries row by row,
with a comma between rows.

```python
import numpy as np

A = np.array([[1,  1,  1],
              [2, -1, -1],
              [2,  0,  1],
              [1, -1,  1]])
```

`A.shape` returns `(4, 3)`: four rows and three columns. Indices start at
zero: `A[i, j]` refers to the entry in row `i` and column `j`.
`A[i, :]` extracts a row and `A[:, j]` a column, as one-dimensional arrays.

## Vectors

A {concept}`vector` is usually represented by a one-dimensional array.
A two-dimensional array can also be used to distinguish explicitly between
a column vector and a row vector.

```python
v = np.array([1.0, 2.0, 3.0])
column = v.reshape(3, 1)
row = v.reshape(1, 3)

print(v.shape)       # (3,)
print(column.shape)  # (3, 1)
print(row.shape)     # (1, 3)
```

An array of shape `(3,)` has no second axis, so its transpose `v.T` is
identical to `v`. In contrast, `column.T` is a row vector. When solving a
linear system, the one-dimensional representation is often the simplest.

## Special matrices

NumPy can construct several common matrices directly.

```python
identity = np.eye(3)
zero = np.zeros((2, 3))
diagonal = np.diag([2.0, 4.0, 6.0])

nodes = np.array([1.0, 2.0, 3.0])
vandermonde = np.vander(nodes, N=3, increasing=True)
```

- `np.eye(3)` creates the $3\times3$ identity matrix.
- `np.zeros((2, 3))` creates a zero matrix with two rows and three columns.
- `np.diag` constructs a diagonal matrix from a vector. When applied to a
  matrix, it extracts the diagonal.
- `np.vander` constructs a {concept}`Vandermonde matrix`. Here, each row is
  $[1, x_i, x_i^2]$. Without `increasing=True`, the powers are arranged in
  decreasing order.

## Basic matrix operations

To add or subtract two matrices in the usual sense, they must have the same
shape. Multiplication by a scalar acts on every entry and can also be used
to form linear combinations.

```python
B = np.array([[1.0, 2.0], [3.0, 4.0]])
C = np.array([[2.0, 0.0], [1.0, 2.0]])

matrix_sum = B + C
matrix_difference = B - C
scaled = 2 * B
linear_combination = 2 * B - 3 * C
```

The {concept}`matrix product` is written with `@`. If $A$ has shape
$m\times n$ and $B$ has shape $n\times p$, then $AB$ has shape
$m\times p$: the number of columns in the first factor must equal the
number of rows in the second.

```python
product = B @ C
entrywise_product = B * C
transpose = B.T
rank = np.linalg.matrix_rank(B)
determinant = np.linalg.det(B)
```

`B * C` multiplies corresponding entries; this differs from `B @ C`.
For some combinations of different shapes, NumPy automatically expands the
operands (*broadcasting*), so check their shapes before a calculation.

The {concept}`transpose` exchanges rows and columns. The {concept}`rank` is
the number of linearly independent columns (or rows).
`np.linalg.matrix_rank` estimates it numerically using a tolerance. The
{concept}`determinant` is defined only for square matrices; in exact
arithmetic, it is nonzero if and only if the matrix is invertible. Its
floating-point value alone does not establish the reliability of a numerical
solution.

## Basic vector operations

The following examples use one-dimensional arrays of the same length.
Addition, subtraction and multiplication by a scalar act entry by entry.

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

For real vectors, `u @ v` is the {concept}`dot product`: it returns a
number. `np.linalg.norm(u)` computes the {concept}`Euclidean norm`.
The {concept}`cross product` `np.cross(u, v)` is used here for two vectors
with three components; the result is orthogonal to both factors, and its
direction depends on their order.

To construct a right-handed orthonormal basis from two non-collinear
directions, normalise the first direction and then their cross product:

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

The columns of `Q` form the new basis. `Q.T @ x` gives a vector's
coordinates in this basis, and `Q @ coordinates` reconstructs it in the
original basis. This construction requires `a` to be nonzero and the two
directions to be non-collinear; nearly collinear directions make the
calculation sensitive to rounding errors.
