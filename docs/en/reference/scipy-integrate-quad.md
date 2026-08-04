# `scipy.integrate.quad`

```{raw} html
<p class="language-switch"><a href="../../fr/reference/scipy-integrate-quad.html">Français</a></p>
```

```{py:function} scipy.integrate.quad(func, a, b, args=())

Approximate the definite integral $\int_a^b f(x)\,dx$ using adaptive
quadrature. Return `(value, estimated_error)`.
```

```python
import numpy as np
from scipy.integrate import quad

value, error = quad(np.sin, 0, np.pi)
```

Here `value` is approximately `2`. The integrand must accept a scalar as its
first argument. Additional fixed parameters can be passed with `args`.

An old notebook may use `scipy.integrate.trapz` or `simps`. In current code use
`numpy.trapezoid` or `scipy.integrate.simpson` for sampled data, and `quad` for a
callable function.

See the [official SciPy integration reference](https://docs.scipy.org/doc/scipy/reference/integrate.html).

