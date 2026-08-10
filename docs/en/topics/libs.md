# Python libraries

```{raw} html
<p class="language-switch"><a href="../genindex.html">Index</a> · <a href="../../fr/topics/libs.html">Français</a></p>
```

A {concept}`library` is a collection of reusable code that adds functions,
classes or data to a program. In practice, a library may contain several
**modules** and **packages**. A module is often a Python file, whereas a package
organizes several modules in one directory tree. “Library” is a general term
rather than a distinct syntactic category in Python.

The standard library, which includes `math` and `statistics`, is installed with
Python. Third-party libraries such as NumPy, SciPy and pandas must be installed
separately, although they are already available in many scientific
distributions and Jupyter platforms.

## Importing a library

The `import` statement makes a module available to the program:

```python
import math

result = math.exp(1.0)
```

Here, the import creates the name `math`. Objects from the module are accessed
by prefixing their names with `math.`, for example `math.exp` or `math.pi`. This
notation immediately shows where the object comes from.

## Namespaces

A {concept}`namespace` associates names with objects. Each module has its own
namespace: `math.exp` and a user-defined function called `exp` can therefore
coexist without replacing one another. This separation limits collisions and
makes the program easier to read. See also [user-defined
functions](user-functions.md).

Some libraries conventionally use a short alias:

```python
import numpy as np
import matplotlib.pyplot as plt
```

The aliases `np` and `plt` are understood by most scientific Python users. It
is better to keep these conventions than to invent a personal alias that is
difficult to recognize.

It is also possible to import a few objects directly into the current
namespace:

```python
from math import exp, log

result = exp(1.0) + log(2.0)
```

This form allows `exp(...)` and `log(...)` to be written directly, but their
module of origin is no longer visible where they are used. It is most suitable
for a small number of explicitly selected names. Avoid `from module import *`:
it imports many names without making them apparent and increases the risk of
collisions.

Importing does not install a library. If the requested module is absent from
the Python environment used by the Jupyter kernel, the statement raises a
`ModuleNotFoundError`. The library must then be installed in the correct
environment, or a platform administrator must be asked to install it.

## Common libraries

### Mathematics and scientific computing

- [`math`](https://docs.python.org/3/library/math.html) provides common
  mathematical functions for real scalar numbers and belongs to the standard
  library.
- [`cmath`](https://docs.python.org/3/library/cmath.html) provides corresponding
  functions for complex scalar numbers.
- [NumPy](https://numpy.org/doc/stable/) provides multidimensional arrays,
  element-wise calculation, basic linear algebra, FFTs and statistical tools.
  Its functions support vectorized calculations.
- [SciPy](https://docs.scipy.org/doc/scipy/) complements NumPy with algorithms
  for integration, interpolation, optimization, signal processing,
  differential equations and statistics.
- [SymPy](https://docs.sympy.org/latest/) supports symbolic computation,
  including expression simplification, differentiation, integration and exact
  solution where possible.
- [Autograd](https://autograd.readthedocs.io/en/latest/) performs automatic
  differentiation of numerical functions written with part of the NumPy
  interface.

For array creation and calculation, see the [NumPy library](numpy.md).

### Data processing and statistics

- [`statistics`](https://docs.python.org/3/library/statistics.html), from the
  standard library, provides simple descriptive statistics for ordinary Python
  data.
- [NumPy](https://numpy.org/doc/stable/reference/routines.statistics.html)
  efficiently computes sums, means, standard deviations, quantiles and other
  summaries of homogeneous numerical arrays.
- [pandas](https://pandas.pydata.org/docs/) provides `Series` and `DataFrame`
  objects for importing, cleaning, selecting, grouping and aggregating tabular
  data with labelled rows and columns.
- [`scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html) provides
  probability distributions, descriptive statistics, tests and several
  estimation methods.
- [statsmodels](https://www.statsmodels.org/stable/) is intended for statistical
  modelling, including regression and time-series analysis.

### Visualization

- [Matplotlib](https://matplotlib.org/stable/) is the foundational library for
  creating and customizing scientific plots in Python.
- [pandas](https://pandas.pydata.org/docs/user_guide/visualization.html) provides
  plotting methods directly on `Series` and `DataFrame` objects; these generally
  use Matplotlib.
- [seaborn](https://seaborn.pydata.org/) provides a higher-level interface for
  statistical graphics and works conveniently with pandas tabular data.

For the first plots in this course, see [Graphs and
visualization](visualisation.md).

## Choosing documentation

To learn a concept, start with the library's user guide or a tutorial. To check
a function's signature, parameters and return type, then consult its API
reference. Prefer documentation matching the installed version: behavior and
available functions may change between versions.
