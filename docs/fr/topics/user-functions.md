# Fonctions définies par l'utilisateur

```{raw} html
<p class="language-switch"><a href="../../en/topics/user-functions.html">English</a></p>
```

Le mot-clé `def` donne un nom à un calcul réutilisable. Le bloc indenté est le
corps de la fonction ; `return` renvoie un résultat à l'appelant.

```python
def energie_cinetique(masse, vitesse):
    """Renvoie 1/2 m v²."""
    return 0.5 * masse * vitesse**2


energie_cinetique(2, 3)
```

Le résultat est `9.0`. Les paramètres comme `masse` sont locaux à la fonction.

