# Good programming practice

```{raw} html
<p class="language-switch"><a href="../../fr/topics/good-practice.html">Français</a></p>
```

Good scientific code should be easy to understand, test, reuse and modify.
These qualities matter even for a short notebook because course exercises often
grow into larger calculations.

## Modular design

Use {concept}`modular design`: divide a calculation into small functions with a
single clear responsibility. Keep data preparation, numerical calculation and
visualisation separate when possible. A function should receive the information
it needs through parameters and return its result explicitly.

```python
import numpy as np

def damped_signal(time, frequency, decay_rate):
    """Return a sinusoidal signal with exponential damping."""
    oscillation = np.sin(2 * np.pi * frequency * time)
    return np.exp(-decay_rate * time) * oscillation

time = np.linspace(0.0, 5.0, 500)
signal = damped_signal(time, frequency=2.0, decay_rate=0.4)
```

This structure lets you test the calculation without also creating a plot.

## Legibility and names

Prefer {concept}`legibility` to cleverness. Use descriptive names such as
`decay_rate` and `sampling_frequency`, consistent indentation, spaces around
operators and reasonably short lines. Avoid unexplained one-letter names except
where a conventional mathematical name genuinely improves clarity.

Use English for identifiers, comments and docstrings. This keeps code consistent
with Python keywords and library interfaces, and makes it easier to share. Write
comments to explain a choice or assumption—not merely to repeat the instruction
on the same line—and update them when the code changes.

## Function docstrings

A {concept}`docstring` is the string immediately below a function definition.
Give every reusable function a concise docstring stating what it does. For a
more substantial function, also document its parameters, returned value,
important assumptions and possible errors.

```python
def relative_error(approximation, reference):
    """Return the absolute relative error.

    Parameters
    ----------
    approximation : float
        Value being assessed.
    reference : float
        Non-zero reference value.

    Returns
    -------
    float
        Absolute relative error.
    """
    if reference == 0:
        raise ValueError("reference must be non-zero")
    return abs((approximation - reference) / reference)
```

## Python style references

[PEP 8—the Style Guide for Python Code](https://peps.python.org/pep-0008/)
covers layout, naming and comments, and explicitly recommends English comments
for code that may be shared. [PEP 257—Docstring
Conventions](https://peps.python.org/pep-0257/) explains one-line and multi-line
docstrings. Treat these documents as shared conventions rather than rules that
override clarity within a particular project.
