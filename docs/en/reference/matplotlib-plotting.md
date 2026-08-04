# Basic plotting with Matplotlib

```{raw} html
<p class="language-switch"><a href="../../fr/reference/matplotlib-plotting.html">Français</a></p>
```

```{py:function} matplotlib.pyplot.subplots(nrows=1, ncols=1, **options)

Create a figure and one or more axes. For one plot, it returns `(fig, ax)`.
```

```{py:function} matplotlib.pyplot.plot(x, y, **style)

Plot values as a line, optionally with markers.
```

```{py:function} matplotlib.pyplot.scatter(x, y, **style)

Plot values as separate markers without joining them.
```

```{py:function} matplotlib.pyplot.show()

Display all currently open figures. In some Jupyter environments display is
automatic, but calling `show` makes the intended output explicit.
```

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin(x)")
ax.scatter(x[::10], np.sin(x[::10]), color="black")
ax.legend()
plt.show()
```

The object-oriented `ax.plot` form is recommended for structured figures;
`plt.plot` is convenient for short exploratory examples.

