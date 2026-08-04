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

`range`, `print`, `abs`, `len`

### NumPy

`linspace`, `array`, `zeros`, `empty`, `arange`, `exp`, `log`, `sqrt`, `sin`,
`cos`, `abs`, `sum`, `meshgrid`, `linalg.solve`

### Matplotlib

`subplots`, `plot`, `scatter`, `show`, `title`, `xlabel`, `ylabel`, `xlim`,
`ylim`, `legend`, `quiver`, `streamplot`

### SciPy

`integrate.quad`, `integrate.solve_ivp`, `interpolate.interp1d`

`interp1d` is documented as a legacy interface with current replacements.
Old calls to `scipy.integrate.trapz` and `scipy.integrate.simps` are documented as
migration notes pointing to `numpy.trapezoid` and `scipy.integrate.simpson`.

## Detected but not yet given dedicated documentation

These calls are valid candidates for later expansion, but they are less frequent,
more advanced, redundant with selected functions, or outside the core course.

### Python built-ins

`max`, `min`, `enumerate`, `sum`, `int`, `str`, `all`, `list`

### NumPy

`polyfit`, `arccos`, `tan`, `arcsin`, `random.normal`, `mean`, `copy`,
`allclose`, `random.seed`, `round`, `where`, `logical_and`, `arctan`,
`random.exponential`, `linalg.matrix_rank`, `argmin`, `linalg.pinv`, `isinf`,
`isclose`, `dot`, `apply_along_axis`, `insert`, `vectorize`, `interp`,
`linalg.det`, `prod`, `ones`, `logical_not`, `fft.fft`, `fft.fftfreq`,
`fft.ifft`, `linalg.eig`, and miscellaneous random helpers.

### Matplotlib

`savefig`, `yscale`, `xscale`, `figure`, `text`, `hist`, `grid`, `semilogy`,
`loglog`, `axhline`, `axvline`, `subplot`, `close`, `fill_between`, animation
helpers and interactive widget classes.

### SciPy

`stats.linregress`, `special.gamma`, `special.sici`, plus the superseded
`integrate.trapz` and `integrate.simps` calls noted above.

### Course-external or advanced libraries

Calls from Autograd, SymPy, pandas, statsmodels, IPython, ipywidgets, Plotly,
scikit-learn and Keras/TensorFlow were detected but were not selected for this
core Python–NumPy–Matplotlib–SciPy reference.

## Suggested next expansion

The most useful next group would be `max`, `min`, `enumerate`, `numpy.mean`,
`numpy.isclose`, `numpy.allclose`, `numpy.polyfit`, `numpy.interp`,
`numpy.linalg.det`, `matplotlib.pyplot.savefig`, logarithmic axes, and the three
NumPy FFT functions.

