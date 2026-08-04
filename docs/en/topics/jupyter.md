# Working in Jupyter

```{raw} html
<p class="language-switch"><a href="../../fr/topics/jupyter.html">Français</a></p>
```

A Jupyter notebook is made of cells. A **code cell** runs Python; a **Markdown
cell** contains explanations and mathematics. Run the selected cell with
{kbd}`Shift`+{kbd}`Enter`.

Execution order matters. The number beside a code cell records when it ran, not
where it appears on the page. When results seem inconsistent, restart the
kernel and run all cells from top to bottom.

```python
import numpy as np

x = np.linspace(0, 1, 5)
x
```

Expected result:

```text
array([0.  , 0.25, 0.5 , 0.75, 1.  ])
```

