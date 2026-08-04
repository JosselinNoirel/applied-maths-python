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
error, and inspect intermediate values with `type()` and, for arrays, `.shape`.

