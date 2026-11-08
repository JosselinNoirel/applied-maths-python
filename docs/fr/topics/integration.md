# Intégration numérique

```{raw} html
<p class="language-switch"><a href="../../en/topics/integration.html">English</a></p>
```

## Intégrer une fonction d'une variable réelle

L'intégration numérique approche l'aire représentée par une intégrale définie.
Choisissez l'outil selon l'information disponible:

- pour une fonction appelable $f(x)$, utilisez
  [`scipy.integrate.quad`](../reference/scipy-integrate-quad.md) ;
- pour des valeurs déjà échantillonnées, utilisez `numpy.trapezoid` ou
  `scipy.integrate.simpson` ;
- implémentez manuellement les sommes de rectangles, de trapèzes ou la méthode de Simpson lorsque vous
  étudiez le fonctionnement de la méthode numérique.
  
NB: Dans le cas de la fonction `quad()`, l'argument doit être réel mais la fonction peut, elle, être complexe pourvu que l'argument optionnel `complex_func=True` soit passé.

Exemple d'application avec l'intégrale
$$
    \int_{-\infty}^{+\infty} e^{-t^2} dt = \sqrt{\pi}
$$

Le code suivant retourne un tuple $(1.7724538509055159, 1.4\times10^{8})$ ce qui signifie que l'intégrale est estimée à $1.77245385$ avec une erreur de $1.4\times 10^{-8}$
```Python
from scipy.integrate import quad
import numpy as np

def f(t):
    return np.exp(-t**2)

quad(f, -np.inf, +np.inf)
```

On peut vérifier la précision en comparant avec $\sqrt{\pi}$.

## Autres fonctionnalités de SciPy

Liste non exhaustive:

- On peut calculer des volumes avec [`scipy.integrate.dblquad`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.dblquad.html).
- Si une fonction retourne un tableau NumPy, on peut recourir à [`scipy.integrate.quad_vec`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad_vec.html) pour intégrer ces valeurs en parallèle.
