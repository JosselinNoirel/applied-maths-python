# Importer des données

```{raw} html
<p class="language-switch"><a href="../../en/topics/data.html">English</a></p>
```

Si les {concept}`données` proviennent d’un fichier extérieur, la méthode dépend de la structure du fichier.

Pour un fichier texte ou CSV contenant uniquement des valeurs numériques, NumPy dispose de la fonction `np.loadtxt`:

```python
data = np.loadtxt("measurements.csv", delimiter=",", skiprows=1)
```

L’argument `delimiter` indique le séparateur utilisé et `skiprows=1` ignore ici la ligne d’en-tête. Lorsque certaines valeurs sont manquantes, `np.genfromtxt` est généralement mieux adapté :

```python
data = np.genfromtxt(
    "measurements.csv",
    delimiter=",",
    skip_header=1,
    missing_values="",
    filling_values=np.nan,
)
```

Pour des données tabulaires plus complexes — colonnes nommées, valeurs manquantes ou types différents — la bibliothèque pandas est souvent plus pratique :

```python
import pandas as pd

table = pd.read_csv("measurements.csv")
```

L’objet obtenu est un `DataFrame`, qui conserve notamment les noms des colonnes. Si les calculs doivent ensuite être réalisés uniquement avec NumPy, les colonnes numériques peuvent être converties en tableau :

```python
data = table[["time", "temperature"]].to_numpy()
```

Le chemin du fichier est interprété relativement au répertoire de travail du noyau Jupyter. Il faut donc vérifier l’emplacement du carnet et du fichier, ou fournir un chemin approprié. Pour un petit jeu de données distribué avec le carnet, placer les deux fichiers dans le même dossier simplifie généralement leur utilisation.
