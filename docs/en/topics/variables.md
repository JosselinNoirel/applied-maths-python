# User-defined variables

```{raw} html
<p class="language-switch"><a href="../../fr/topics/variables.html">Français</a></p>
```

A variable associates a name with an object. Assignment uses `=`; mathematical
equality is tested with `==`.

```python
mass = 2.5
acceleration = 9.81
force = mass * acceleration

force == 24.525
```

Choose descriptive names such as `initial_velocity`. Names cannot contain spaces
or start with a digit, and Python distinguishes uppercase from lowercase.

An assignment can reuse the previous value:

```python
k = 10
k = k + 1
```

The result is `11`. This Python instruction is not the mathematical equation
$k=k+1$: it first evaluates the right-hand side and then replaces the value of
`k`.

## Naming variables well

Short names such as `i`, `j`, `k`, `x` and `y` suit indices and temporary
mathematical quantities. For a value retained for longer, prefer a descriptive
name such as `number_of_points` or `initial_velocity`. Avoid reusing the name of
a function such as {funcindex}`sum`, {funcindex}`min` or {funcindex}`max`.

## Local scope

A variable created inside a function is local to that function. It is not
available after the call unless the function returns it with `return`.
