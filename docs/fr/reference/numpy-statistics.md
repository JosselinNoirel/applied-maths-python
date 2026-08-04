# Statistiques élémentaires avec NumPy

```{raw} html
<p class="language-switch"><a href="../../en/reference/numpy-statistics.html">English</a></p>
```

```{py:function} numpy.min(a, axis=None)

Renvoie le minimum d'un tableau, ou les minima suivant un axe.
```

```{py:function} numpy.max(a, axis=None)

Renvoie le maximum d'un tableau, ou les maxima suivant un axe.
```

```{py:function} numpy.mean(a, axis=None)

Renvoie la moyenne arithmétique, éventuellement suivant un axe.
```

```{py:function} numpy.std(a, axis=None, ddof=0)

Renvoie l'écart type. La valeur par défaut `ddof=0` utilise la définition pour
une population ; utilisez `ddof=1` pour l'écart type corrigé courant d'un
échantillon.
```

Le total se calcule avec {py:func}`numpy.sum`.

```python
import numpy as np

donnees = np.array([2.1, 2.4, 2.5, 3.0])
resume = {
    "minimum": np.min(donnees),
    "maximum": np.max(donnees),
    "moyenne": np.mean(donnees),
    "ecart_type": np.std(donnees),
    "somme": np.sum(donnees),
}
```

Lorsque `NaN` représente une donnée manquante, les réductions ordinaires le
propagent. Des fonctions comme `numpy.nanmean` et `numpy.nanstd` ignorent
explicitement les valeurs `NaN`.
