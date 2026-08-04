# Intégration numérique

```{raw} html
<p class="language-switch"><a href="../../en/topics/integration.html">English</a></p>
```

L'intégration numérique approche l'aire représentée par une intégrale définie.
Choisissez l'outil selon l'information disponible :

- pour une fonction appelable $f(x)$, utilisez
  [`scipy.integrate.quad`](../reference/scipy-integrate-quad.md) ;
- pour des valeurs déjà échantillonnées, utilisez `numpy.trapezoid` ou
  `scipy.integrate.simpson` ;
- implémentez manuellement les sommes de rectangles ou de trapèzes lorsque vous
  étudiez le fonctionnement de la méthode numérique.

```python
import numpy as np
from scipy.integrate import quad

value, error = quad(lambda x: np.exp(-x**2), 0, 1)
```

L'erreur renvoyée est une estimation numérique, et non une preuve de la validité
du modèle mathématique ou de l'intégrande.

