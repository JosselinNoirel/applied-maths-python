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

