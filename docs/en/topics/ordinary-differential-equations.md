# Ordinary differential equations

```{raw} html
<p class="language-switch"><a href="../../fr/topics/ordinary-differential-equations.html">Français</a></p>
```

An initial-value problem specifies an equation $y'=f(t,y)$ and an initial state
$y(t_0)=y_0$. Hand-written Euler, Heun and Crank–Nicolson schemes are valuable
for understanding numerical methods. For a robust general-purpose solver, use
[`scipy.integrate.solve_ivp`](../reference/scipy-solve-ivp.md).

```python
import numpy as np
from scipy.integrate import solve_ivp

def rhs(t, state):
    position, velocity = state
    return [velocity, -position]

t = np.linspace(0, 10, 300)
solution = solve_ivp(rhs, (0, 10), [1.0, 0.0], t_eval=t)
```

Check solver success, choose tolerances in relation to the problem scale, and
compare with a known solution or convergence study whenever possible.

