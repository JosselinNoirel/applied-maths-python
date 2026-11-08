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

def f(x):
    return  np.exp(-x**2)

value, error = quad(f, 0, 1)
```

L'intégrande (la fonction $f$ ou une fonction anonyme lambda) doit accepter un scalaire comme premier argument.
Des paramètres fixes supplémentaires peuvent être transmis avec `args`.

Les bornes peuvent être finies ou infinies (`np.inf`).

Si la fonction $f$ retourne un résultat complexe (avec une composante imaginaire), l'argument `complex_func=True` doit être passé.

Voir la [référence officielle SciPy](https://docs.scipy.org/doc/scipy/reference/integrate.html).

