# Importing data

```{raw} html
<p class="language-switch"><a href="../../fr/topics/data.html">Français</a></p>
```

If the {concept}`data` come from an external file, the appropriate method depends on the structure of the file.

For a text or CSV file containing only numerical values, NumPy provides the `np.loadtxt` function:

```python
data = np.loadtxt("measurements.csv", delimiter=",", skiprows=1)
```

The `delimiter` argument indicates the separator used, and `skiprows=1` skips the header row here. When some values are missing, `np.genfromtxt` is generally more suitable:

```python
data = np.genfromtxt(
    "measurements.csv",
    delimiter=",",
    skip_header=1,
    missing_values="",
    filling_values=np.nan,
)
```

For more complex tabular data—named columns, missing values or different data types—the pandas library is often more convenient:

```python
import pandas as pd

table = pd.read_csv("measurements.csv")
```

The resulting object is a `DataFrame`, which retains information such as column names. If subsequent calculations are to be performed only with NumPy, the numerical columns can be converted to an array:

```python
data = table[["time", "temperature"]].to_numpy()
```

The file path is interpreted relative to the working directory of the Jupyter kernel. You should therefore check the locations of the notebook and the file, or provide an appropriate path. For a small dataset distributed with a notebook, placing both files in the same folder generally makes them easier to use.
