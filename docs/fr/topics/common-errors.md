# Erreurs classiques

```{raw} html
<p class="language-switch"><a href="../../en/topics/common-errors.html">English</a></p>
```

Une exception indique où Python s'est arrêté et pourquoi. Lisez d'abord la
dernière ligne, puis examinez la ligne de code signalée.

- `NameError` : le nom est mal orthographié ou sa cellule de définition n'a pas été exécutée.
- `TypeError` : une opération a reçu un type d'objet inadapté.
- `IndexError` : un indice est hors des limites d'une liste ou d'un tableau.
- `ValueError` : le type est acceptable, mais la valeur ou la forme ne l'est pas.
- `IndentationError` : l'indentation ne forme pas un bloc valide.

```python
valeurs = [10, 20, 30]
valeurs[3]  # IndexError : les indices valides sont 0, 1 et 2
```

Réduisez un calcul défaillant au plus petit exemple qui reproduit l'erreur, puis
inspectez les résultats intermédiaires avec `type()` et, pour les tableaux,
`.shape`.

