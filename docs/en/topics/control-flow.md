# Control structures

```{raw} html
<p class="language-switch"><a href="../../fr/topics/control-flow.html">Français</a></p>
```

Control structures decide which instructions run and how often.

The expressions used after `if` and `while` are explained in
[Boolean conditions](boolean-conditions.md).

## Conditions

```python
temperature = 1.5

if temperature < 0:
    state = "ice"
else:
    state = "liquid water"
```

## Loops

Use a `for` loop when iterating over known values:

```python
squares = []
for n in range(5):
    squares.append(n**2)
```

When both the position and the value are needed, use `enumerate` rather than a
manually updated counter:

```python
values = [2.0, 3.5, 4.1]
for index, value in enumerate(values):
    print(index, value)
```

See the [`range` and `enumerate` reference](../reference/python-builtins.md).

Use `while` when repetition continues until a condition changes. Ensure that the
loop body can eventually make that condition false.
