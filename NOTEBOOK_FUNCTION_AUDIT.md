# Notebook function audit

This inventory was produced from the code cells of 164 notebooks placed in the
ignored `.notebook-input/` directory. The notebooks themselves are not tracked.

## Summary

- 4,571 function or method call occurrences
- 290 distinct call expressions before pedagogical filtering
- 74 names defined locally with `def`
- 12 code cells with incomplete or intentionally invalid Python syntax

Local functions, dynamically called objects, model-specific methods and repeated
aliases were excluded from the documentation selection.

## Selected for documentation

### Python

`range`, `print`, `abs`, `len`, `min`, `max`, `enumerate`

### NumPy

`linspace`, `array`, `zeros`, `empty`, `arange`, `exp`, `log`, `sqrt`, `sin`,
`cos`, `abs`, `min`, `max`, `sum`, `mean`, `std`, `isclose`, `allclose`,
`interp`, `polyfit`, `meshgrid`, `linalg.solve`, `linalg.det`, `fft.fft`,
`fft.fftfreq`, `fft.ifft`

### Matplotlib

`subplots`, `plot`, `scatter`, `show`, `title`, `xlabel`, `ylabel`, `xlim`,
`ylim`, `legend`, `quiver`, `streamplot`

### SciPy

`integrate.quad`, `integrate.solve_ivp`, `interpolate.interp1d`,
`stats.linregress`

`interp1d` is documented as a legacy interface with current replacements.
Old calls to `scipy.integrate.trapz` and `scipy.integrate.simps` are documented as
migration notes pointing to `numpy.trapezoid` and `scipy.integrate.simpson`.

## Detected but not yet given dedicated documentation

These calls are valid candidates for later expansion, but they are less frequent,
more advanced, redundant with selected functions, or outside the core course.

### Python built-ins

`sum`, `int`, `str`, `all`, `list`

### NumPy

`arccos`, `tan`, `arcsin`, `random.normal`, `copy`, `random.seed`, `round`,
`where`, `logical_and`, `arctan`,
`random.exponential`, `linalg.matrix_rank`, `argmin`, `linalg.pinv`, `isinf`,
`dot`, `apply_along_axis`, `insert`, `vectorize`, `prod`, `ones`,
`logical_not`, `linalg.eig`, and miscellaneous random helpers.

### Matplotlib

`savefig`, `yscale`, `xscale`, `figure`, `text`, `hist`, `grid`, `semilogy`,
`loglog`, `axhline`, `axvline`, `subplot`, `close`, `fill_between`, animation
helpers and interactive widget classes.

### SciPy

`special.gamma`, `special.sici`, plus the superseded `integrate.trapz` and
`integrate.simps` calls noted above.

### Course-external or advanced libraries

Calls from Autograd, SymPy, pandas, statsmodels, IPython, ipywidgets, Plotly,
scikit-learn and Keras/TensorFlow were detected but were not selected for this
core Python–NumPy–Matplotlib–SciPy reference.

## Suggested next expansion

The most useful next group would be Python's `sum`, `numpy.random.normal`,
`numpy.copy`, `numpy.where`, `numpy.linalg.matrix_rank`, `numpy.linalg.pinv`,
`numpy.linalg.eig`, `matplotlib.pyplot.savefig`, logarithmic axes, histograms
and grids, followed by `scipy.special.gamma` and `scipy.special.sici` where the
course material needs them.
