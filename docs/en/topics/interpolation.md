# Interpolation

```{raw} html
<p class="language-switch"><a href="../../fr/topics/interpolation.html">Français</a></p>
```

Interpolation estimates values between known samples. It is not the same as
extrapolation beyond the sampled interval.

The notebooks use [`scipy.interpolate.interp1d`](../reference/scipy-interpolation.md),
which is now a legacy interface. For new linear interpolation, prefer
{py:func}`numpy.interp`;
use `scipy.interpolate.make_interp_spline` when a spline is
required.

```python
import numpy as np

x = np.array([0.0, 1.0, 2.0])
y = np.array([0.0, 1.0, 4.0])
y_new = np.interp(1.5, x, y)
```

Always inspect the sampling density and the behaviour expected between points.
