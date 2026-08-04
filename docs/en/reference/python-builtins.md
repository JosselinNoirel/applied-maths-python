# Frequently used Python functions

```{raw} html
<p class="language-switch"><a href="../../fr/reference/python-builtins.html">Français</a></p>
```

These built-in functions require no import.

## `range`

```{py:function} range(start, stop, step=1)

Produce an immutable sequence of integers from `start` up to, but excluding,
`stop`. With one argument, `start` is `0`.
```

```python
for k in range(1, 6):
    print(k**2)
```

Use `range` for loop indices. Use `numpy.arange` or `numpy.linspace` when you
need a numerical array for calculations.

## `print`

```{py:function} print(*objects, sep=' ', end='\n')

Display one or more objects as text.
```

```python
iteration = 4
error = 2.3e-5
print("iteration:", iteration, "error:", error)
```

`print` is useful for inspecting intermediate values, but a function should
normally return a result rather than only print it.

## `abs`

```{py:function} abs(x)

Return the absolute value of a number.
```

```python
absolute_error = abs(approximation - exact_value)
```

Use `numpy.abs` for arrays.

## `len`

```{py:function} len(object)

Return the number of items in a container.
```

```python
values = [2.0, 3.5, 4.1]
n = len(values)
```

For a multidimensional NumPy array, `len(a)` is only the size of its first axis;
inspect `a.shape` for all dimensions.

See the [official Python built-in functions](https://docs.python.org/3/library/functions.html).

