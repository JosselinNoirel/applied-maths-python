# `scipy.integrate.quad`

```{raw} html
<p class="language-switch"><a href="../../en/reference/scipy-integrate-quad.html">English</a></p>
```

```{py:function} scipy.integrate.quad(func, a, b, args=())

Approche l'intégrale définie $\int_a^b f(x)\,dx$ par une quadrature adaptative.
Renvoie `(valeur, erreur_estimée)`.
```

```python
import numpy as np
from scipy.integrate import quad

valeur, erreur = quad(np.sin, 0, np.pi)
```

Ici, `valeur` est proche de `2`. L'intégrande doit accepter un scalaire comme
premier argument. Des paramètres fixes supplémentaires peuvent être transmis
avec `args`.

Un ancien notebook peut utiliser `scipy.integrate.trapz` ou `simps`. Dans un code
actuel, utilisez `numpy.trapezoid` ou `scipy.integrate.simpson` pour des données
échantillonnées, et `quad` pour une fonction appelable.

Voir la [référence officielle SciPy](https://docs.scipy.org/doc/scipy/reference/integrate.html).

