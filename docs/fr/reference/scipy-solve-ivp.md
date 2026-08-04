# `scipy.integrate.solve_ivp`

```{raw} html
<p class="language-switch"><a href="../../en/reference/scipy-solve-ivp.html">English</a></p>
```

```{py:function} scipy.integrate.solve_ivp(fun, t_span, y0, method='RK45', t_eval=None, **options)

Résout un problème de Cauchy $y'=f(t,y)$ avec $y(t_0)=y_0$.
```

```python
import numpy as np
from scipy.integrate import solve_ivp

def second_membre(t, y):
    return -2 * y

t = np.linspace(0, 3, 100)
solution = solve_ivp(second_membre, (0, 3), [1.0], t_eval=t)
y = solution.y[0]
```

La fonction dérivée reçoit d'abord `t`, puis le vecteur d'état `y`. Même pour
une seule équation, `y0` est une séquence. Vérifiez `solution.success` et
`solution.message` avant d'utiliser les valeurs.

`RK45` est un bon choix explicite par défaut. Une équation raide peut nécessiter
une méthode implicite comme `Radau` ou `BDF`.

Voir la [référence officielle SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).

