# Python objects

```{raw} html
<p class="language-switch"><a href="../../fr/topics/python-objects.html">Français</a></p>
```

Every Python value is an object with a type. Applied mathematics commonly uses
integers (`int`), floating-point numbers (`float`), complex numbers (`complex`),
Boolean values (`bool`), strings (`str`), lists (`list`) and NumPy arrays
(`numpy.ndarray`).

The {funcindex}`type` function reports the type of an object.

```python
import numpy as np

n = 4
step = 0.25
label = "position"
values = np.array([0.0, 0.25, 0.5, 0.75])

type(values)
```

## Integers: `int`

Objects of type `int` represent positive, negative or zero integers. Their size
is not restricted to 32 or 64 bits: Python uses as many digits as necessary,
subject to available memory. Calculations with very large integers therefore
remain exact, although they gradually become more expensive.

```python
population = 8_200_000_000
large_integer = 2**200
```

The `_` character can separate groups of digits without changing the value. See
the [arithmetic operators](python-syntax.md) on the Python syntax page.

## Floating-point numbers: `float`

Objects of type `float` represent floating-point numbers. On usual Python
implementations they follow IEEE 754 double precision and provide approximately
15 to 17 significant decimal digits. Their precision and range are therefore
limited.

In particular, many decimal numbers have no exact binary representation:

```python
0.1 + 0.2 == 0.3
```

This expression returns `False`. To compare approximate calculation results,
prefer `np.isclose` or `np.allclose` to strict equality. The special values
`inf`, `-inf` and `nan` represent infinities or overflows and indeterminate
numerical results, respectively.

See the [arithmetic operators](python-syntax.md).

## Complex numbers

Objects of type `complex` represent a number in the form $a+bj$, where `j`
denotes the imaginary unit ($j^2=-1$). Python uses `j`, rather than `i`, in a
complex literal. Even when the real part is zero, a coefficient must precede
`j`, for example `1j`.

```python
z = 3 + 4j
real_part = z.real
imaginary_part = z.imag
modulus = abs(z)
conjugate = z.conjugate()
```

The `real` and `imag` attributes give the real and imaginary parts;
{py:func}`abs` gives the modulus and the `conjugate` method gives the complex
conjugate. The usual arithmetic operations work with complex numbers. For
functions such as the complex square root, exponential or trigonometric
functions, use the `cmath` module, or NumPy functions when working with arrays.

## Booleans

The `bool` type has only two values: `True` and `False`. A comparison produces a
Boolean value; the `and`, `or` and `not` operators then combine or invert
conditions.

```python
temperature = 18.5
is_positive = temperature > 0
is_in_interval = 0 <= temperature <= 25
should_warn = temperature < 0 or temperature > 40
is_valid = is_in_interval and not should_warn
```

Booleans are used in particular by `if` conditions and `while` loops. Python
also interprets certain objects as true or false in a Boolean context: zero
numbers, `None` and empty containers such as `""` or `[]` are considered false;
most other objects are considered true.

```python
values = []

if not values:
    print("The list is empty")
```

This implicit conversion is convenient for testing whether a list or string is
empty. It should not be applied directly to a NumPy array containing several
values, because its truth value is ambiguous. See [Boolean conditions and
comparisons](boolean-conditions.md).

## Strings

A string, of type `str`, is an ordered sequence of characters. Single or double
quotes can delimit it. The {py:func}`len` function returns its number of
characters; `+` concatenates two strings and `*` repeats a string.

```python
message = "Applied mathematics"
number_of_characters = len(message)
title = message + " with Python"
separator = "-" * 20
```

Strings are *immutable*: an individual character cannot be changed directly.
An operation produces a new string.

## Lists

A list is an ordered, mutable sequence. Its elements may have different types.
Indexing starts at zero, and a negative index counts from the end. A slice
`start:stop` selects entries from `start` up to, but excluding, `stop`.

```python
values = [2.0, 3.5, 4.1, 5.8]
first_value = values[0]
last_value = values[-1]
middle_values = values[1:3]
values[0] = 1.5
values.append(7.2)
```

## Conversions

Type constructors convert an object when the requested conversion makes sense:

```python
float(4)
int(3.14)
int("1230")
str(3.14)
```

`int(3.14)` gives `3`: it discards the fractional part without rounding. A
string can be converted only if its contents have the expected form; for
example, `int("twelve")` raises a `ValueError`.

Some numerical conversions happen implicitly. An operation between an integer
and a floating-point number generally produces a `float`. Similarly, division
with `/` always returns a `float`: `15 / 3` gives `5.0`. Floor division with
`//`, however, gives the quotient rounded down.

Other conversions result from a dedicated function such as
{funcindex}`round`. Without a second argument, it rounds a `float` and returns an
integer: `round(3.6)` gives `4`.

Converting a string `s` with `list(s)` produces a list of its characters. The
`join` method performs the reverse operation by assembling a sequence of
strings:

```python
s = "This is a string"
characters = list(s)
reconstructed = "".join(characters)
```

The `split` method cuts a string at each occurrence of a separator:

```python
words = s.split(" ")
```

Without an argument, `s.split()` treats any run of whitespace as one separator.

Unlike a list, a NumPy array supports element-by-element numerical operations:
`values**2` squares every entry. See the [NumPy library](numpy.md).
