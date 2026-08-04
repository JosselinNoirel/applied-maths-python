# Graphs and visualisation

```{raw} html
<p class="language-switch"><a href="../../fr/topics/visualisation.html">Français</a></p>
```

Matplotlib represents data using figures and axes. For a first graph, create the
sampling points, calculate the values, and label both axes.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(xlabel="x", ylabel="sin(x)", title="Sine function")
ax.grid()
plt.show()
```

Always label quantities and, when relevant, include their physical units.

## Example: a function with a singularity

Consider $f(x)=1/(x-1)$ on $[-4,6]$. The singularity at $x=1$ requires us to
separate the two branches of the curve:

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / (x - 1)

x = np.linspace(-4, 6, 500)
left = x < 1
right = x > 1

fig, ax = plt.subplots()
ax.plot(x[left], f(x[left]), color="black", label="f(x)")
ax.plot(x[right], f(x[right]), color="black")
ax.axhline(0, color="gray", linewidth=0.8)
ax.axvline(1, color="lightgray", linestyle="--", label="asymptote")
ax.set(xlabel="x", ylabel="f(x)", ylim=(-5, 5))
ax.legend()
plt.show()
```

Plotting all values in one call would create a misleading segment across the
discontinuity. A graph is an analytical tool: consider the domain, singularities
and scale.

## Curves, points and scales

- {funcindex}`ax.plot`(`x, y`) joins values with segments;
- {funcindex}`ax.scatter`(`x, y`) displays separate points;
- {funcindex}`ax.set_xscale`(`"log"`) or {funcindex}`ax.set_yscale`(`"log"`) uses a logarithmic scale when
  values are strictly positive;
- the `label` argument and {funcindex}`ax.legend`() construct a legend.
