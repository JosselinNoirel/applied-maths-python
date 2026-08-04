# Annoter et cadrer un graphique

```{raw} html
<p class="language-switch"><a href="../../en/reference/matplotlib-annotation.html">English</a></p>
```

```{py:function} matplotlib.pyplot.title(label)

Définit le titre des axes courants.
```

```{py:function} matplotlib.pyplot.xlabel(label)

Légende l'axe horizontal.
```

```{py:function} matplotlib.pyplot.ylabel(label)

Légende l'axe vertical.
```

```{py:function} matplotlib.pyplot.xlim(left=None, right=None)

Consulte ou définit les limites horizontales.
```

```{py:function} matplotlib.pyplot.ylim(bottom=None, top=None)

Consulte ou définit les limites verticales.
```

```{py:function} matplotlib.pyplot.legend()

Affiche les légendes fournies aux tracés avec `label=...`.
```

```python
plt.plot(x, y, label="approximation")
plt.xlabel("temps (s)")
plt.ylabel("position (m)")
plt.title("Trajectoire numérique")
plt.xlim(0, 10)
plt.ylim(-2, 2)
plt.legend()
```

Les méthodes orientées objet correspondantes sont `ax.set_title`,
`ax.set_xlabel`, `ax.set_ylabel`, `ax.set_xlim`, `ax.set_ylim` et `ax.legend`.

