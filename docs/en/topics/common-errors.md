# Common errors

```{raw} html
<p class="language-switch"><a href="../../fr/topics/common-errors.html">Français</a></p>
```

An exception reports where Python stopped and why. Read the final line first,
then inspect the referenced source line.

- `NameError`: the name is misspelled or its defining cell has not run.
- `TypeError`: an operation received an unsuitable kind of object.
- `IndexError`: an index lies outside a list or array.
- `ValueError`: the object type is acceptable but its value or shape is not.
- `IndentationError`: the indentation does not define a valid block.

```python
values = [10, 20, 30]
values[3]  # IndexError: valid indices are 0, 1 and 2
```

Reduce a failing calculation to the smallest example that still produces the
error, and inspect intermediate values with {funcindex}`type`() and, for arrays, `.shape`.

## Undefined variable

```text
NameError: name 'a' is not defined
```

Check the spelling and the execution order of Jupyter cells. An assignment
inside a false condition does not create the variable:

```python
if b < 0:
    a = np.pi
```

## Non-subscriptable object and out-of-range index

```text
TypeError: 'int' object is not subscriptable
IndexError: list index out of range
```

`L[i]` only makes sense for a subscriptable object. For a sequence of three
values, the valid indices are `0`, `1` and `2`.

## Numerical overflow

Floating-point numbers have a limited range. An exponential that is too large
can produce `OverflowError` or `RuntimeWarning: overflow encountered in exp`.
This often means that you should reconsider the scale, units or mathematical
formulation—not merely hide the warning.
