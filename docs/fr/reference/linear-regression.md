# Régression linéaire et ajustement polynomial

```{raw} html
<p class="language-switch"><a href="../../en/reference/linear-regression.html">English</a></p>
```

```{py:function} numpy.polyfit(x, y, deg)

Ajuste les coefficients d'un polynôme par moindres carrés, de la puissance la
plus élevée au terme constant.
```

```python
import numpy as np

x = np.array([0.0, 1.0, 2.0, 3.0])
y = np.array([1.1, 2.9, 5.2, 6.8])
pente, ordonnee_origine = np.polyfit(x, y, deg=1)
```

Utilisez `numpy.polyval` pour évaluer le polynôme. Un ajustement de degré élevé
peut être mal conditionné ; changez l'échelle des coordonnées ou utilisez l'API
polynomiale récente de NumPy pour une application exigeante.

```{py:function} scipy.stats.linregress(x, y)

Calcule une régression linéaire par moindres carrés et renvoie la pente,
l'ordonnée à l'origine, la corrélation, un test d'hypothèse et des erreurs types.
```

```python
from scipy.stats import linregress

resultat = linregress(x, y)
y_ajuste = resultat.intercept + resultat.slope * x
r_carre = resultat.rvalue**2
```

Utilisez `polyfit(..., deg=1)` pour obtenir simplement les coefficients. Utilisez
`linregress` lorsque les sorties statistiques — erreurs types ou valeur p du test
sur la pente — sont importantes.

Voir la [référence officielle de `linregress`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html).

