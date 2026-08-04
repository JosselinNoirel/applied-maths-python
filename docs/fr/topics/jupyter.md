# Travailler dans Jupyter

```{raw} html
<p class="language-switch"><a href="../../en/topics/jupyter.html">English</a></p>
```

Un notebook Jupyter est composé de cellules. Une **cellule de code** exécute du
Python ; une **cellule Markdown** contient des explications et des formules.
Exécutez la cellule sélectionnée avec {kbd}`Maj`+{kbd}`Entrée`.

L'ordre d'exécution est important. Le nombre affiché à côté d'une cellule
indique quand elle a été exécutée, pas sa position dans la page. Si les résultats
semblent incohérents, redémarrez le noyau et exécutez toutes les cellules du haut
vers le bas.

```python
import numpy as np

x = np.linspace(0, 1, 5)
x
```

Résultat attendu :

```text
array([0.  , 0.25, 0.5 , 0.75, 1.  ])
```

