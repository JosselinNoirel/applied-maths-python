# `scipy.integrate.solve_ivp`

```{raw} html
<p class="language-switch"><a href="../../fr/reference/scipy-solve-ivp.html">Français</a></p>
```

```{py:function} scipy.integrate.solve_ivp(fun, t_span, y0, method='RK45', t_eval=None, **options)

Solve an initial-value problem $y'=f(t,y)$ with $y(t_0)=y_0$.
```

```python
import numpy as np
from scipy.integrate import solve_ivp

def rhs(t, y):
    return -2 * y

t = np.linspace(0, 3, 100)
solution = solve_ivp(rhs, (0, 3), [1.0], t_eval=t)
y = solution.y[0]
```

The derivative function receives `t` first and the state vector `y` second. Even
for one equation, `y0` is a sequence. Inspect `solution.success` and
`solution.message` before relying on the values.

`RK45` is a useful explicit default. Stiff equations may require an implicit
method such as `Radau` or `BDF`.

See the [official SciPy reference](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html).

