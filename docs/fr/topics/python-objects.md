# Objets Python

```{raw} html
<p class="language-switch"><a href="../../en/topics/python-objects.html">English</a></p>
```

Toute valeur Python est un objet possédant un type.
En mathématiques appliquées,
on utilise couramment les entiers (`int`), les nombres à virgule (`float`),
les nombres complexes,
les
booléens (`bool`), les chaînes (`str`), les listes (`list`) et les tableaux NumPy
(`numpy.ndarray`).

La {funcindex}`type` indique le type de l'objet.

```python
import numpy as np

n = 4
step = 0.25
label = "position"
values = np.array([0.0, 0.25, 0.5, 0.75])

type(values)
```

## Entiers `int`

Les objets de type `int` représentent des nombres entiers, positifs, négatifs ou
nuls. Leur taille n'est pas limitée à 32 ou 64 bits : Python utilise autant de
chiffres que nécessaire, dans la limite de la mémoire disponible. Les calculs
sur de très grands entiers restent donc exacts, mais deviennent progressivement
plus coûteux.

```python
population = 8_200_000_000
large_integer = 2**200
```

Le caractère `_` peut séparer des groupes de chiffres sans modifier la valeur.
Voir les [opérateurs arithmétiques](python-syntax.md) dans la page consacrée à la
syntaxe Python.

On peut utiliser d'autres bases pour représenter des entiers

```Python
m = 0b101010111 # Binary       343
n = 0o7712      # Octal       4042
p = 0x5f1       # Hexadecimal 1521
```

## Nombres à virgule `float`

Les objets de type `float` représentent des nombres à virgule flottante. Sur les
implémentations usuelles de Python, ils suivent la double précision IEEE 754 et
offrent environ 15 à 17 chiffres décimaux significatifs. Leur précision et leur
étendue sont donc limitées.

En particulier, de nombreux nombres décimaux ne possèdent pas de représentation
binaire exacte :

```python
0.1 + 0.2 == 0.3
```

Cette expression renvoie `False`. Pour comparer les résultats de calculs
approchés, il est généralement préférable d'utiliser `np.isclose` ou
`np.allclose` plutôt qu'une égalité stricte. Les valeurs spéciales `inf`, `-inf`
et `nan` représentent respectivement les dépassements ou infinis et les résultats
numériques indéterminés.

Voir les [opérateurs arithmétiques](python-syntax.md).

## Nombres complexes

(Cette partie est surtout utile pour les cours traitant de la transformée de Fourier.)

Les objets de type `complex` représentent un nombre sous la forme <code><em>a</em> + <em>b</em>j</code>, où
$a$ et $b$ désignent deux nombres (int ou float) et où `j` désigne l'unité imaginaire ($j^2 = -1$).
Comme d'autres langages, Python emploie `j`, et non $i$, dans
l'écriture d'un nombre complexe. Pour que ce soit interprété correctement, il
faut écrire un coefficient devant `j`, par exemple `1j` car `j` est interprété comme une variable.

```python
z = 3.9 + 4.7j
modulus = abs(z)
conjugate = z.conjugate()
```

Les attributs `z.real` et `z.imag` donnent les parties réelle et imaginaire;
{py:func}`abs` donne le module et la méthode `conjugate` le complexe conjugué.
Les opérations arithmétiques usuelles fonctionnent avec les complexes. Pour des
fonctions comme la racine carrée, l'exponentielle ou les fonctions
trigonométriques complexes, on utilise le module `cmath`, ou les fonctions NumPy
si l'on travaille avec des tableaux.

## Booléens

Le type `bool` ne possède que deux valeurs: True et False. Une comparaison
produit un booléen ; les opérateurs `and`, `or` et `not` permettent ensuite de
combiner ou d'inverser des conditions.

```python
temperature = 18.5
is_positive = temperature > 0
is_in_interval = 0 <= temperature <= 25
should_warn = temperature < 0 or temperature > 40
is_valid = is_in_interval and not should_warn
```

Les booléens interviennent notamment dans les conditions `if` et les boucles
`while`. Python interprète aussi certains objets comme vrais ou faux dans un
contexte booléen : les nombres nuls, `None` et les conteneurs vides comme `""`
ou `[]` sont considérés comme faux ; la plupart des autres objets sont
considérés comme vrais.

```python
values = []

if not values:
    print("The list is empty")
```

Cette conversion implicite est pratique pour tester si une liste ou une chaîne
est vide. Elle ne doit toutefois pas être utilisée directement avec un tableau
NumPy comportant plusieurs valeurs, car sa valeur de vérité est ambiguë. Voir
les [conditions booléennes et comparaisons](boolean-conditions.md).

## Chaînes de caractères

Une {concept}`chaîne de caractères`, de type `str`, est une suite ordonnée de caractères (un nom, un prénom, un code postal, un numéro de téléphone ou un numéro de sécurité sociale).
Elle peut être délimitée par des guillemets simples `'...'`, doubles `"..."` ou, notamment pour des chaînes sur plusieurs lignes, des constructions

```Python
'''This is a string of
characters containing
ends of lines'''
```

La fonction
{py:func}`len` renvoie son nombre de caractères (cf. [Fonctions usuelles](common-functions.md));
`+` concatène deux chaînes et `*` répète une chaîne.

```python
message = 'Applied mathematics'
number_of_characters = len(message)
title = message + ' with Python'
separator = "-" * 20
```

### Caractères spéciaux

Les chaînes de caractères peuvent contenir des caractères particuliers comme
`\n` (fin de ligne) ou `\t` (tabulation) introduits par la barre oblique inverse `\` (backslash), qui joue le rôle de {concept}`caractère d'échappement`.
Ce caractère permet également d'inclure des guillemets comme dans `'My grandparents\' house'`.
On insère une barre oblique inverse à l'aide de `\\`.

Les chaînes sont {concept}`immutables`: on ne peut pas modifier directement un de leurs
caractères. Une opération produit une nouvelle chaîne.

### Chaînes de caractères *r* et *f*

Les chaînes de caractères introduites avec *r* sont brutes (*r* comme *raw*): elles ne donnent pas lieu à une interprétation des caractères spéciaux.

```Python
s1 =  '\t' # One character (tab)
s2 = r'\t' # Two characters: backslash - t letter
```

On peut construire des chaînes de caractères affichant le contenu d'une variable ou d'un calcul à l'aide des chaînes de caractères introduite avec *f*
au sein desquelles les accolades `{...}` provoque l'insertion du résultat de l'évaluation de l'expression qu'elles contiennent:

```Python
pi = 3.1415926535
s = f'Square pi and you approximately get {pi**2}!'
```

Par ailleurs, cette construction offre la possibilité de modeler l'affichage:

```Python
f'{{ et }}'
f'{value:.2f}'       # Fixed decimal precision
f'{ratio:.1%}'       # Percentage
f'{value:10.2f}'     # Width and precision
f'{name:<15}'        # Left alignment
f'{integer:04d}'     # Leading zeros
f'{integer:#x}'      # Hexadecimal representation
f'{large_number:,}'  # Thousands separator
f'{variable=}'       # Debugging
```

Voir la [mini-syntaxe officielle de formatage de Python](https://docs.python.org/3/library/string.html#format-specification-mini-language).

## Listes

Une {concept}`liste` est une suite ordonnée et modifiable. Ses éléments peuvent être un mélange de
types différents. L'indexation commence à zéro; un indice négatif compte à
partir de la fin. Une tranche ({concept}`slice`) `start:stop` sélectionne les éléments
depuis `start` jusqu'à `stop` exclu.

```python
values = [2.0, 3.5, 4.1, 5.8, 2.5, 9.1, 3.2]
first_value = values[0]
last_value = values[-1]
middle_values = values[1:6]
```

La tranche existe aussi sous une forme ternaire `start:stop:step`. À noter que
si `start` est vide (`values[:3:2]`), on suppose que la tranche commence au début de la liste;
si `end` est vide (`values[1::2]`), on suppose que la tranche va aussi loin que possible;
si `step` est vide (`values[1:5:]`), on suppose des pas de $1$;
si `step` vaut $-1$, la liste est lue à rebours.

Pour inverser une liste, la méthode la plus idiomatique est donc `values[::-1]`.

On peut modifier une liste

```Python
values[0] = 1.5
values.append(7.2)
```

La méthode {funcindex}`list.append` permet de construire petit à petit des listes; par exemple, on pourrait imaginer, dans une boucle [for](control-flow.md), de construire une liste des nombres premiers à mesure qu'on en trouve de nouveaux.

```{important}
Python n'est pas confortablement équipé pour le calcul vectoriel ou matriciel.
La [bibliothèque NumPy](numpy.md) fournit les fonctionnalités utiles pour cela.

Contrairement à une liste, un tableau NumPy permet des opérations numériques
terme à terme: `values**2` élève chaque valeur au carré. Voir la
[bibliothèque NumPy](numpy.md).
```

## Conversions

Les constructeurs de types permettent de convertir un objet lorsque la
conversion demandée a un sens :

```python
float(4)
int(3.14)
int('1230')
str(3.14)
```

`int(3.14)` donne `3` : la partie décimale est supprimée, sans arrondi. Une
chaîne ne peut être convertie que si son contenu possède la forme attendue ; par
exemple, `int("twelve")` provoque une `ValueError`.

Certaines conversions numériques ont lieu implicitement. Une opération entre un
entier et un nombre à virgule produit généralement un `float`. De même, la
division `/` renvoie toujours un `float` : `15 / 3` donne `5.0`. La division
entière `//`, en revanche, donne le quotient arrondi vers le bas.

D'autres conversions sont le résultat de l'action d'une fonction dédiée comme
{funcindex}`round`. Employée sans second argument, celle-ci arrondit un `float`
et renvoie un entier : `round(3.6)` donne `4`.

La transformation d'une chaîne `s` avec `list(s)` produit la liste de ses
caractères. La méthode `join` effectue l'opération inverse en assemblant une
séquence de chaînes :

```python
s = "This is a string"
characters = list(s)
reconstructed = "".join(characters)
```

La méthode `split` découpe une chaîne à chaque occurrence d'un séparateur :

```python
words = s.split(" ")
```

Sans argument, `s.split()` traite toute suite d'espaces comme un seul séparateur.
