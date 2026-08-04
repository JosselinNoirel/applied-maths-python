# User-defined functions

```{raw} html
<p class="language-switch"><a href="../../fr/topics/user-functions.html">Français</a></p>
```

Use `def` to give a reusable calculation a name. The indented block is the
function body, and `return` sends a result back to the caller.

```python
def kinetic_energy(mass, velocity):
    """Return 1/2 m v²."""
    return 0.5 * mass * velocity**2


kinetic_energy(2, 3)
```

This returns `9.0`. Parameters such as `mass` exist locally inside the function.

Indentation delimits the function body. Without it, Python cannot determine
which instructions belong to the definition.

## Mathematical function

```python
import numpy as np

def f(x):
    return np.exp(np.abs(np.sin(x)))
```

This definition works with a number or a NumPy array. It makes the program
closer to mathematical notation and lets you change the function under study in
one place.

## Programmatic function

A function can also automate several instructions:

```python
def positive_sum(values):
    total = 0.0
    for value in values:
        if value > 0:
            total = total + value
    return total
```

`total` and `value` are local. Calling {funcindex}`positive_sum`(`[9, -5, 5, 6]`) returns
`20.0`.
