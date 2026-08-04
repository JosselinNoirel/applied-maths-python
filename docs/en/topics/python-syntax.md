# Python syntax

```{raw} html
<p class="language-switch"><a href="../../fr/topics/python-syntax.html">Français</a></p>
```

Python generally reads a program line by line. Each line contains a complete
instruction unless, for example, an open parenthesis indicates that the
instruction continues on the next line.

## Instructions and comments

A program is a sequence of instructions: assignments, operations, function calls
and control structures. The `#` character begins a comment that Python ignores:

```python
x = x + 1  # Increment x by one
```

A useful comment explains the purpose of a calculation instead of repeating the
code.

## Arithmetic operators

| Python | Operation |
|---|---|
| `x + y`, `x - y` | addition, subtraction |
| `x * y`, `x / y` | multiplication, division |
| `x**a` | power $x^a$ |
| `-x` | additive inverse of $x$ |
| `n % m` | remainder of integer division |
| `n // m` | integer quotient |

For an $n$th root, use $x^{1/n}$, written `x**(1/n)`. The parentheses make the
intention clear and are important when `n` is a variable.

With NumPy arrays, these operators act element by element.

## Calling a function

Parentheses identify a function call:

```python
function(argument_1, argument_2)
```

Positional arguments must follow the expected order. Named arguments can be
written in a different order:

```python
import numpy as np

x = np.linspace(start=0, stop=10, num=21)
```

Optional arguments have default values. For example, {funcindex}`np.linspace`(`0, 10`) uses
`num=50` and `endpoint=True` by default.

See also [Variables](variables.md), [User-defined functions](user-functions.md)
and [Common functions](common-functions.md).
