# Debugging a program

```{raw} html
<p class="language-switch"><a href="../../fr/topics/debug.html">Français</a></p>
```

When a program does not give the expected result, first distinguish between two situations. If Python stops execution and displays an exception, read the *traceback* starting with its last line: it gives the type of error and its message. Then work upwards until you find the first line belonging to your program or notebook. The page about [common errors](common-errors.md) helps interpret the most frequent exceptions.

If the program runs but produces an incorrect result, look for the first step at which values become unexpected. Inspecting intermediate results, as well as the type and shape of objects, often locates the problem quickly:

```python
print("type(x):", type(x))
print("shape:", np.shape(x))
print("value:", x)
```

An assertion expresses a property that must remain true during the calculation. If it is false, Python immediately stops execution at the relevant location:

```python
assert np.all(np.isfinite(x)), "x contains a non-finite value"
```

To make the diagnosis easier, reduce the problem: use a small dataset for which the result is known, isolate the suspicious calculation in a cell or function, and temporarily remove parts unrelated to the error. It is also useful to check a function's {concept}`signature` and the meaning of its arguments in the [documentation](help.md).

In a Jupyter notebook, the order in which cells are executed can leave old variables in memory. When the behaviour seems inconsistent, save the notebook, restart the kernel, and then run all cells from the beginning. This verifies that the result does not depend on a hidden kernel state.

Finally, change only one thing at a time and rerun the smallest relevant test. A correction that removes an error message is not necessarily correct: also check the resulting value, its units and order of magnitude and, whenever possible, compare it with a case solved by hand.
