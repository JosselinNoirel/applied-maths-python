# Numerical integration

```{raw} html
<p class="language-switch"><a href="../../fr/topics/integration.html">Français</a></p>
```

Numerical integration approximates the area represented by a definite integral.
Choose the tool according to the information available:

- for a callable function $f(x)$, use
  [`scipy.integrate.quad`](../reference/scipy-integrate-quad.md);
- for already sampled values, use `numpy.trapezoid` or
  `scipy.integrate.simpson`;
- implement rectangle or trapezoidal sums manually when studying how the
  numerical method works.

```python
import numpy as np
from scipy.integrate import quad

value, error = quad(lambda x: np.exp(-x**2), 0, 1)
```

The returned error is a numerical estimate, not a proof that the mathematical
model or integrand is correct.

