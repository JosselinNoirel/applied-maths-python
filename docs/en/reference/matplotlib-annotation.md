# Annotating and framing a graph

```{raw} html
<p class="language-switch"><a href="../../fr/reference/matplotlib-annotation.html">Français</a></p>
```

```{py:function} matplotlib.pyplot.title(label)

Set the title of the current axes.
```

```{py:function} matplotlib.pyplot.xlabel(label)

Label the horizontal axis.
```

```{py:function} matplotlib.pyplot.ylabel(label)

Label the vertical axis.
```

```{py:function} matplotlib.pyplot.xlim(left=None, right=None)

Get or set horizontal limits.
```

```{py:function} matplotlib.pyplot.ylim(bottom=None, top=None)

Get or set vertical limits.
```

```{py:function} matplotlib.pyplot.legend()

Display labels supplied to plotted artists with `label=...`.
```

```python
plt.plot(x, y, label="approximation")
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.title("Numerical trajectory")
plt.xlim(0, 10)
plt.ylim(-2, 2)
plt.legend()
```

The corresponding object-oriented methods are `ax.set_title`, `ax.set_xlabel`,
`ax.set_ylabel`, `ax.set_xlim`, `ax.set_ylim` and `ax.legend`.

