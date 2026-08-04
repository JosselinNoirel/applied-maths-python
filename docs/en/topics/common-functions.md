# Common functions

```{raw} html
<p class="language-switch"><a href="../../fr/topics/common-functions.html">Français</a></p>
```

Python, NumPy and Matplotlib provide reusable functions for constructing data,
performing calculations and displaying results. Import NumPy using the customary
alias `np`:

```python
import numpy as np
```

## Construct an evenly spaced interval

[`numpy.linspace`](../reference/numpy-linspace.md) constructs a chosen number of
evenly spaced values between two endpoints.

```python
import numpy as np

x = np.linspace(-1, 1, 5)
```

Here `x` is `array([-1. , -0.5, 0. , 0.5, 1. ])`. See the complete
[`numpy.linspace` reference](../reference/numpy-linspace.md) for endpoint rules,
return values, examples and common mistakes.

## Choosing a function

Prefer a function that expresses the mathematical intention directly. For
example, use `np.linspace(a, b, n)` when the number of sample points matters. Use
`np.arange(start, stop, step)` when the increment matters instead.

## Fundamental Python functions

- `len(x)` gives the number of elements;
- `type(x)` reports the object's type;
- `abs(x)` calculates an absolute value;
- `min(x)` and `max(x)` give extreme values;
- `round(x)` rounds a value.

## Importing a library

```python
import numpy as np
import matplotlib.pyplot as plt
```

The aliases `np` and `plt` are widely used conventions. They keep names short
while showing where each function comes from. Avoid `from numpy import *`, which
mixes namespaces and can hide existing functions.

For constructing and calculating with arrays, see [The NumPy library](numpy.md).
For displaying data, see [Graphs and visualisation](visualisation.md).
