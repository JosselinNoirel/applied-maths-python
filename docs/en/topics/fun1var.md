# Function of one variable

```{raw} html
<p class="language-switch"><a href="../../fr/topics/fun1var.html">Français</a></p>
```

## Defining the function

It is often useful to define a Python function that directly expresses the
mathematical function being studied: this makes the code easier to read and
avoids copying the same expression into several calculations.

For example, for $f(t)=\sin^2(t)\exp(-t)$:

```python
import numpy as np

def f(t):
    return np.sin(t)**2 * np.exp(-t)
```

`**2` denotes squaring, and NumPy's trigonometric functions use angles in
radians. With these NumPy operations, `f` accepts either a number or an
array: in the latter case, it computes a value for each element without an
explicit loop.

```python
value = f(1.0)
values = f(np.array([0.0, 1.0, 2.0]))
```

Before choosing argument values, check the domain of definition: for example,
a real logarithm requires a strictly positive argument, and a denominator
must not be zero. See also [user-defined functions](user-functions.md).

## Plotting the function

Plotting helps develop mathematical intuition and is often the first step
in an analysis. Choose an interval, then construct a grid of values with
[`numpy.linspace`](../reference/numpy-linspace.md).

```python
import matplotlib.pyplot as plt

t = np.linspace(0, np.pi, 200)
fig, ax = plt.subplots()
ax.plot(t, f(t))
ax.set_xlabel("t")
ax.set_ylabel("f(t)")
ax.grid(True)
plt.show()
```

Here, `t` contains 200 evenly spaced points between $0$ and $\pi$,
including both endpoints. `f(t)` contains the 200 corresponding values, and
`ax.plot` connects the points with line segments.

For a rapidly varying function, increase the number of points and compare
the resulting plots. A graph can miss an oscillation or a maximum between
two points: it suggests behaviour but does not constitute a proof. When a
function has a discontinuity or singularity, plot the intervals on which it
is continuous separately to avoid artificially connecting the two sides.
