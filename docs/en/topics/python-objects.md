# Python objects

```{raw} html
<p class="language-switch"><a href="../../fr/topics/python-objects.html">Français</a></p>
```

Every Python value is an object with a type. Applied mathematics commonly uses
integers (`int`), decimal numbers (`float`), Boolean values (`bool`), strings
(`str`), lists (`list`) and NumPy arrays (`numpy.ndarray`).

```python
import numpy as np

n = 4
step = 0.25
label = "position"
values = np.array([0.0, 0.25, 0.5, 0.75])

type(values)
```

Unlike a list, a NumPy array supports element-by-element numerical operations:
`values**2` squares every entry.

