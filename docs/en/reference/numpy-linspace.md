# `numpy.linspace`

```{raw} html
<p class="language-switch"><a href="../../fr/reference/numpy-linspace.html">Français</a></p>
```

```{py:function} numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

Return `num` evenly spaced samples over the interval from `start` to `stop`.
```

## Minimal syntax

```python
import numpy as np

x = np.linspace(start, stop, num)
```

The result is a NumPy array containing `num` values. By default, both `start`
and `stop` are included.

## Parameters needed at first

`start`
: First value of the interval.

`stop`
: Last value of the interval when `endpoint=True`.

`num`
: Number of samples. It must be a non-negative integer; the default is `50`.

`endpoint`
: If `True`, include `stop`. If `False`, leave it out and use a different spacing.

## Example: sampling a function

Sample $f(x)=x^2$ at five points on $[-1,1]$:

```python
import numpy as np

x = np.linspace(-1, 1, 5)
y = x**2
```

This produces:

```text
x = [-1.  -0.5  0.   0.5  1. ]
y = [ 1.   0.25 0.   0.25 1. ]
```

## Endpoint behaviour

```python
import numpy as np

closed = np.linspace(0, 1, 5)
half_open = np.linspace(0, 1, 5, endpoint=False)
```

`closed` includes `1`; `half_open` ends at `0.8`. The latter is useful for
periodic grids where the first and last points would otherwise represent the
same location.

## Common mistake

The third argument is a **number of points**, not a step size:

```python
np.linspace(0, 1, 0.1)  # incorrect: 0.1 is not a number of points
np.linspace(0, 1, 11)   # 11 points separated by 0.1
```

For the authoritative API and advanced options, see the
[official NumPy documentation](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html).

