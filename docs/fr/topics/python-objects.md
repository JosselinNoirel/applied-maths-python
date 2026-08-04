# Objets Python

```{raw} html
<p class="language-switch"><a href="../../en/topics/python-objects.html">English</a></p>
```

Toute valeur Python est un objet possédant un type. En mathématiques appliquées,
on utilise couramment les entiers (`int`), les nombres décimaux (`float`), les
booléens (`bool`), les chaînes (`str`), les listes (`list`) et les tableaux NumPy
(`numpy.ndarray`).

```python
import numpy as np

n = 4
pas = 0.25
etiquette = "position"
valeurs = np.array([0.0, 0.25, 0.5, 0.75])

type(valeurs)
```

Contrairement à une liste, un tableau NumPy permet des opérations numériques
terme à terme : `valeurs**2` élève chaque valeur au carré.

