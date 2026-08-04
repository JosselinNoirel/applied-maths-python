# Working in Jupyter

```{raw} html
<p class="language-switch"><a href="../../fr/topics/jupyter.html">Français</a></p>
```

A Jupyter notebook is made of cells. A {concept}`code cell` runs Python; a
{concept}`Markdown cell` contains explanations and mathematics. Run the selected cell with
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

## Command mode and edit mode

{concept}`Edit mode` changes the cell contents. {concept}`Command mode` acts on the whole
cell. {kbd}`Enter` enters edit mode and {kbd}`Esc` returns to command mode.

Useful shortcuts in command mode:

- {kbd}`A` and {kbd}`B` add a cell above or below;
- {kbd}`C`, {kbd}`V` and {kbd}`X` copy, paste and cut a cell;
- {kbd}`M` changes the cell to Markdown;
- {kbd}`Y` changes the cell to Python code;
- {kbd}`1`, {kbd}`2`, {kbd}`3` turn a Markdown cell into a heading at the
  corresponding level.

In edit mode, {kbd}`Shift`+{kbd}`Enter` runs the cell and selects the next one.
Shortcuts can differ slightly between JupyterLab and the classic Notebook; check
the command palette in your interface.

See also [Markdown syntax and formulas](markdown.md).
