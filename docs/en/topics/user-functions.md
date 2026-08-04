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

