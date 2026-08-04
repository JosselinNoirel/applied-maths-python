# Équations différentielles ordinaires

```{raw} html
<p class="language-switch"><a href="../../en/topics/ordinary-differential-equations.html">English</a></p>
```

Un problème de Cauchy spécifie une équation $y'=f(t,y)$ et un état initial
$y(t_0)=y_0$. Programmer les schémas d'Euler, de Heun ou de Crank–Nicolson est
utile pour comprendre les méthodes numériques. Pour un solveur général robuste,
utilisez [`scipy.integrate.solve_ivp`](../reference/scipy-solve-ivp.md).

```python
import numpy as np
from scipy.integrate import solve_ivp

def rhs(t, state):
    position, velocity = state
    return [velocity, -position]

t = np.linspace(0, 10, 300)
solution = solve_ivp(rhs, (0, 10), [1.0, 0.0], t_eval=t)
```

Vérifiez le succès du solveur, choisissez les tolérances selon l'échelle du
problème et comparez si possible avec une solution connue ou une étude de
convergence.

