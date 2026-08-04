# Basic statistics

```{raw} html
<p class="language-switch"><a href="../../fr/topics/basic-statistics.html">Français</a></p>
```

For a numerical sample $x_1,\ldots,x_n$, useful first summaries are its size,
minimum, maximum, sum, arithmetic mean and standard deviation.

```python
import numpy as np

data = np.array([4.1, 3.8, 4.4, 5.0, 4.2])
n = len(data)
minimum = np.min(data)
maximum = np.max(data)
total = np.sum(data)
mean = np.mean(data)
standard_deviation = np.std(data, ddof=1)
```

The choice between `ddof=0` and `ddof=1` depends on whether the values represent
the full population or a sample used to estimate population variability. See
[the function reference](../reference/numpy-statistics.md).

To describe a linear relationship between paired measurements, continue with
[linear regression and polynomial fitting](../reference/linear-regression.md).

