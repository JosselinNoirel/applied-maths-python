# Travailler dans Jupyter

```{raw} html
<p class="language-switch"><a href="../../en/topics/jupyter.html">English</a></p>
```

Un notebook Jupyter est composé de cellules. Une {concept}`cellule de code` exécute du
Python ; une {concept}`cellule Markdown` contient des explications et des formules.
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

## Mode commande et mode édition

Le {concept}`mode édition` modifie le contenu de la cellule. Le {concept}`mode commande` agit
sur la cellule entière. {kbd}`Entrée` passe en mode édition et {kbd}`Échap`
revient au mode commande.

Raccourcis utiles en mode commande :

- {kbd}`A` et {kbd}`B` ajoutent une cellule au-dessus (*above*) ou en dessous
  (*below*) ;
- {kbd}`C`, {kbd}`V` et {kbd}`X` copient, collent et coupent une cellule ;
- {kbd}`M` transforme la cellule en Markdown ;
- {kbd}`Y` transforme la cellule en code Python ;
- {kbd}`1`, {kbd}`2`, {kbd}`3` transforment une cellule Markdown en titre du
  niveau correspondant.

En mode édition, {kbd}`Maj`+{kbd}`Entrée` exécute la cellule et sélectionne la
suivante. Les raccourcis peuvent varier légèrement entre JupyterLab et le
Notebook classique ; consultez la palette de commandes de votre interface.

Voir aussi [Syntaxe Markdown et formules](markdown.md).
