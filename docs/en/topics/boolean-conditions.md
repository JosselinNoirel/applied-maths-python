# Boolean conditions

```{raw} html
<p class="language-switch"><a href="../../fr/topics/boolean-conditions.html">Français</a></p>
```

A Boolean condition asks a question whose answer is `True` or `False`. For
example, `x > 0` asks whether the value of `x` is strictly positive.

## Comparisons

| Python | Meaning |
|---|---|
| `a < b` | $a<b$ |
| `a <= b` | $a\leq b$ |
| `a == b` | equality |
| `a != b` | $a\neq b$ |
| `a >= b` | $a\geq b$ |
| `a > b` | $a>b$ |

Do not confuse assignment `=` with comparison `==`.

Rounding errors make exact floating-point equality fragile. Prefer
{funcindex}`np.isclose`(`a, b`):

```python
import numpy as np

np.isclose(0.1 + 0.2, 0.3)
```

## Membership and missing values

```python
3 in [1, 2, 3]
option is None
```

`in` tests membership. `is None` checks that a variable contains the special
value `None`.

## Combining conditions

The operators `and`, `or` and `not` combine or reverse conditions:

```python
inside = x >= 0 and x <= 1
outside = x < 0 or x > 1
not_inside = not inside
```

For NumPy arrays, use `&`, `|` and `~`, with parentheses around each comparison.
