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

