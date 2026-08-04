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

Use `while` when repetition continues until a condition changes. Ensure that the
loop body can eventually make that condition false.
