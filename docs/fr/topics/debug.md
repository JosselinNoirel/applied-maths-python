# Corriger ses erreurs

```{raw} html
<p class="language-switch"><a href="../../en/topics/debug.html">English</a></p>
```

Lorsqu'un programme ne donne pas le résultat attendu, il faut d'abord distinguer deux situations. Si Python interrompt l'exécution et affiche une exception, lire le *traceback* en commençant par la dernière ligne : elle indique le type de l'erreur et son message. Remonter ensuite jusqu'à la première ligne qui appartient au programme ou au carnet. La page consacrée aux [erreurs classiques](common-errors.md) aide à interpréter les exceptions les plus courantes.

Si le programme s'exécute mais produit un résultat incorrect, rechercher la première étape à laquelle les valeurs deviennent inattendues. Examiner les résultats intermédiaires, ainsi que le type et la forme des objets, permet souvent de localiser rapidement le problème :

```python
print("type(x):", type(x))
print("shape:", np.shape(x))
print("value:", x)
```

Une assertion permet d'exprimer une propriété qui doit rester vraie pendant le calcul. Si elle est fausse, Python interrompt immédiatement l'exécution à l'endroit concerné :

```python
assert np.all(np.isfinite(x)), "x contains a non-finite value"
```

Pour simplifier le diagnostic, réduire le problème : utiliser un petit jeu de données dont le résultat est connu, isoler le calcul suspect dans une cellule ou une fonction, puis retirer temporairement les parties sans rapport avec l'erreur. Il est également utile de vérifier la {concept}`signature d'une fonction <signature>` et la signification de ses arguments dans la [documentation](help.md).

Dans un carnet Jupyter, l'ordre d'exécution des cellules peut laisser en mémoire des variables anciennes. Lorsque le comportement semble incohérent, enregistrer le carnet, redémarrer le noyau, puis exécuter toutes les cellules depuis le début. Cette opération permet de vérifier que le résultat ne dépend pas d'un état caché du noyau.

Enfin, ne modifier qu'une chose à la fois et relancer le plus petit test pertinent. Une correction qui supprime le message d'erreur n'est pas nécessairement correcte : il faut aussi contrôler le résultat obtenu, ses unités, son ordre de grandeur et, si possible, le comparer à un cas résolu à la main.
