# Mathematical functions with NumPy

```{raw} html
<p class="language-switch"><a href="../../fr/reference/numpy-mathematics.html">Français</a></p>
```

The following functions act element by element on arrays and also accept scalar
numbers.

```{py:function} numpy.exp(x)

Calculate $e^x$ element by element.
```

```{py:function} numpy.log(x)

Calculate the natural logarithm. Real inputs must be positive; zero produces
`-inf` and negative real inputs produce `nan`.
```

```{py:function} numpy.sqrt(x)

Calculate the principal square root. Negative real inputs produce `nan` unless
the array has a complex data type.
```

```{py:function} numpy.sin(x)

Calculate the sine of angles given in radians.
```

```{py:function} numpy.cos(x)

Calculate the cosine of angles given in radians.
```

```{py:function} numpy.abs(x)

Calculate the absolute value, or the magnitude for complex values.
```

```{py:function} numpy.sum(a, axis=None)

Add array entries. With `axis=None`, add every entry; otherwise reduce along the
selected axis.
```

```python
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.exp(-x) * np.cos(x)
total = np.sum(y)
```

Use NumPy versions rather than functions from `math` when the argument may be an
array.

