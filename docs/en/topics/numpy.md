# The NumPy library

```{raw} html
<p class="language-switch"><a href="../../fr/topics/numpy.html">Français</a></p>
```

NumPy provides numerical arrays and functions designed to act on all their
values. The conventional import is:

```python
import numpy as np
```

The prefix `np.` identifies the NumPy namespace: `np.sqrt`, for example, is
NumPy's square-root function.

## Creating arrays

### Regular grid

[`np.linspace`](../reference/numpy-linspace.md) creates a chosen number of evenly
spaced points between two endpoints:

```python
x = np.linspace(-2, 3, 101)
```

### Integer sequence or fixed step

`np.arange(start, stop, step)` uses a fixed step and excludes `stop`:

```python
indices = np.arange(0, 10, 2)
```

For a floating-point interval whose endpoints matter, prefer `linspace` in many
cases because it avoids ambiguity from accumulated rounding.

### Initialising and entering an array

```python
uninitialised = np.empty(5)
zeros = np.zeros(5)
ones = np.ones(5)
data = np.array([-3.71, 1.43, -2.49, 7.21])
```

Do not use the values in `np.empty` before replacing them.

## Element-by-element calculation

```python
x = np.linspace(0, 1, 5)
y = np.exp(-x) * np.sin(2 * np.pi * x)
```

The operators `+`, `-`, `*`, `/` and `**`, as well as NumPy functions, act on
every array value. This vectorised form is generally clearer and faster than a
Python loop.

## Summarising an array

```python
total = np.sum(data)
average = np.mean(data)
minimum = np.min(data)
maximum = np.max(data)
standard_deviation = np.std(data)
variance = np.var(data)
```

## Common mathematical functions

| Mathematics | NumPy |
|---|---|
| $\sqrt{x}$ | `np.sqrt(x)` |
| $\exp(x)$ | `np.exp(x)` |
| $\log(x)$ | `np.log(x)` |
| $\log_{10}(x)$ | `np.log10(x)` |
| $\sin(x)$, $\cos(x)$ | `np.sin(x)`, `np.cos(x)` |
| $\lvert x\rvert$ | `np.abs(x)` |
| rounding | `np.round(x)` |

Trigonometric functions expect angles in radians.

