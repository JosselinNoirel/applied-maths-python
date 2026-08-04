# Comment modifier ces pages

```{raw} html
<p class="language-switch"><a href="../../en/topics/howto.html">English</a></p>
```

La plupart des modifications de contenu ne nécessitent que d'éditer les fichiers
Markdown dans `docs/en/` et `docs/fr/`.

- Conservez des chemins correspondants pour les pages anglaises et françaises,
  par exemple `docs/en/topics/numpy.md` et `docs/fr/topics/numpy.md`.
- Pour créer un nouveau thème bilingue, vous pouvez partir d'une paire existante,
  comme la [page des bonnes pratiques](good-practice.md) correspondante dans
  chaque langue.
- Conservez le bloc de changement de langue situé près du début de chaque page.
- Lorsque vous ajoutez une page thématique, ajoutez-la aussi aux sections
  `{toctree}` cachées des deux fichiers `index.md`. Le libellé placé avant `<...>`
  est le titre court utilisé dans la navigation.
- Gardez les blocs de code *identiques* dans les deux langues. Traduisez le texte
  qui les entoure, mais pas les noms de variables, commentaires, docstrings,
  chaînes de caractères ou légendes de graphiques.
- Utilisez `{py:func}\`numpy.mean\`` pour créer un lien vers une fonction
  documentée. Utilisez `{concept}\`terme\`` pour une notion en gras ajoutée à
  l'index et `{funcindex}\`nom\`` pour une occurrence de fonction en style code
  ajoutée à l'index.
- Définissez une nouvelle fonction documentée ainsi :

````markdown
```{py:function} numpy.example(argument)

Explanation.
```
````

Soyez vigilant :

- Ne définissez pas deux fois la même fonction entièrement qualifiée dans une
  langue ; Sphinx signalerait une cible dupliquée.
- Utilisez des liens Markdown relatifs et omettez `.html` dans les fichiers
  sources. Par exemple : `[NumPy](numpy.md)`.
- Ne modifiez pas `_site/` ou `_build/` : ces répertoires sont générés.

Avant de créer un commit, activez l'environnement et exécutez :

```bash
source .venv/bin/activate
make docs
git diff --check
```

`make docs` construit les deux versions linguistiques et traite les avertissements
Sphinx comme des erreurs ; cette commande devrait donc détecter la plupart des
problèmes accidentels. `git diff --check` repère les petites erreurs d'espacement
signalées par Git. Vous pouvez ensuite ouvrir `_site/index.html` localement pour
effectuer une vérification visuelle.
