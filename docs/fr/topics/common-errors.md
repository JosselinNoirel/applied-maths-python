# Erreurs classiques

```{raw} html
<p class="language-switch"><a href="../../en/topics/common-errors.html">English</a></p>
```

Une erreur (ou exception) indique où Python s'est arrêté et pourquoi. Lisez d'abord la
dernière ligne, puis examinez la ligne de code signalée pour comprendre le problème.

- {concept}`NameError`: le nom est mal orthographié ou sa cellule de définition n'a pas été exécutée.
- {concept}`TypeError`: une opération a reçu un type d'objet inadapté.
- {concept}`IndexError`: un indice est hors des limites d'une liste ou d'un tableau.
- {concept}`ValueError`: le type est acceptable, mais la valeur ou la forme ne l'est pas.
- {concept}`IndentationError`: l'indentation ne forme pas un bloc valide.
- {concept}`SyntaxError`: erreur générique indiquant que la structure même du code est fautive (parenthèse non refermée).
- {concept}`OverflowError`: les calculs effectués génèrent des nombres trop grands.

```python
values = [10, 20, 30]
values[3]  # IndexError: valid indices are 0, 1 and 2
```

Réduisez un calcul défaillant au plus petit exemple qui reproduit l'erreur, puis
inspectez les résultats intermédiaires avec {funcindex}`type`() et, pour les tableaux,
`.shape`.

Ici, nous repertorions les erreurs les plus courantes.

## NameError: Variable ou fonction non définie

```text
NameError: name 'a' is not defined
```

La variable référencée dans le code n'existe pas : Python a beau consulter sa mémoire, aucune variable ou fonction de ce nom n'existe.

1. Si vous venez d'ouvrir un carnet Jupyter, il est peut-être nécessaire d'exécuter certaines cellules du carnet avant d'en arriver au calcul qui provoque l'erreur.  (Il n'est pas exclu que lors de la création du carnet, la cellule définissant la variable \(a\) ait été insérée par erreur plus bas que celle du calcul provoquant l'erreur.  Il n'est pas non plus exclu que la cellule ayant défini la variable ait été retirée par erreur.)

2. Il est possible que vous exécutiez une cellule de code donnant l'impression de définir la variable \(a\) mais qu'elle soit en fait inopérante. Par exemple, si l'affectation est soumise à une condition que vous pensez *vraie* à tort :

```python
if b < 0:
    a = np.pi
```

3. Il est possible que vous ayez fait une erreur 

Par ailleurs, ne confondez pas `=` pour l'affectation et `==` pour tester l'égalité (cf. [Variables définies par l'utilisateur](variables.md)).

## TypeError et IndexError: Objet non indexable et indice hors limites

Il est possible d'accéder à un élément d'une liste, d'un tuple ou d'un dictionnaire via <code>L[i]</code>. Mais si <code>L</code> n'est pas une liste ou un dictionnaire par exemple, les crochets (*subscript* le fait de passer un indice) n'ont pas de sens et leur utilisation fautive produit des erreurs.

```text
TypeError: 'int' object is not subscriptable
```

`L[i]` n'a de sens que pour un objet indexable. Pour une séquence de trois
valeurs, les indices valides sont `0`, `1` et `2`. L'utilisation d'un indice au-delà de 2 provoque une erreur.  (Cette erreur est parfois le résultat de celle, précédemment décrite, par laquelle on utilise `L[1]` pour parler du premier élément d'une liste.)

```text
IndexError: list index out of range
```

Le même genre d'erreur est rencontré avec des tableaux NumPy.

## Indexation

Une {concept}`erreur silencieuse` ([*off by one*](https://en.wikipedia.org/wiki/Off-by-one_error)) peut provenir du fait que Python fait partie des langages qui indexent les listes à partir de [zéro](https://en.wikipedia.org/wiki/Zero-based_numbering).

Le premier élément d'une liste est `L[0]` et non `L[1]`!

## IndentationError: Problème avec les blocs

L'{concept}`indentation` en bloc est importante en Python: elle marque d'un point de vue syntaxique les relations de dépendance des diverses instructions.  Dans l'exemple suivant

```Python
if b < 0:
    if a < 0:
        c = a * b
```

l'instruction `c = a * b` est subordonné au deuxième `if`, qui lui-même dépend du premier.

On peut donc rencontrer deux types d'IndentationError:

* Soit *expected an indented block* (Python n'attendait pas d'indentation à cet endroit)
* Soit *unexpected indent* (Python n'attendait pas d'indentation à cet endroit)

Parfois une erreur peut être silencieuse (les pires bugs). Il faut bien distinguer

```Python
if b < 0:
    if a < 0:
        c = a * b
else:
    c = -a * b
```

et

```Python
if b < 0:
    if a < 0:
        c = a * b
    else:
        c = -a * b
```

## SyntaxError: Oubli d'un caractère, expressions mal formées

Si des parenthèses sont mal formées ou mal fermées, Python se plaindra avec une SyntaxError (*unmatched parenthesis*).

Les structures de contrôle nécessitent un *deux points* `:`. S'il venait à manquer, Python se plaindrait avec une SyntaxError.

Si un opérateur n'existe pas (par exemple `8***4`), SyntaxError!

Généralement, le problème est assez clairement identifié par Python:

```text
  Cell In[31], line 1
    if a == b
             ^
SyntaxError: expected ':'
```

## OverflowError: Dépassement numérique

Les entiers de Python peuvent en principe être aussi grands que l'on veut (mais la mémoire et le temps de calcul vont tout de même imposer des limites à ce qu'il est possible de faire).  Ce n'est pas le cas des nombres à virgule flottante qui ne peuvent dépasser des nombres de l'ordre de $10^{300}$. Certain calculs dépassant cette valeur génèrent donc une erreur.

Une exponentielle trop grande peut
produire OverflowError ou un RuntimeWarning (*overflow encountered in exp* par exemple). Ce
message signale souvent qu'il faut revoir l'échelle, les unités ou la formulation
mathématique du calcul et pas seulement masquer l'avertissement ou abandonner.

## Boucles infinie

Si vous mettez en place une boucle `while`, le programme dépend d'une condition dont il faut absolument se convaincre qu'elle va devenir fausse.

Une définition classique de la factorielle $n! = n \times (n - 1)!$ et $0! = 1$ se traduit par une implémentation récursive en Python

```Python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

Cette fonction est correcte mais elle attend un entier positif ou nul.
`factorial(1.5)` fait partir Python dans une boucle infinie, car valeurs successives passées à `factorial` ne sont jamais égales à $0$.

## Séparateur décimal

Le séparateur décimal utilisé par Python est le point `.` et non la virgule comme le veut l'usage en français.  Afin d'éviter toute confusion et afin de rendre aussi transparente que possible la correspondance entre le code et les mathématiques, nous utilisons systématiquement dans le cours le séparateur décimal `.`.  On notera par exemple que $\pi \approx 3.14$.

Python utilise la virgule dans d'autres contextes, comme le fait de passer des arguments à une fonction

```Python
x = np.linspace(-3, +3)
```

ou pour créer des listes de nombres

```Python
L = np.array([1, 2, 3, 4])
```

Les *tuples* sont une structure de données similaire à une liste. Leur intérêt est limité pour nos activités pédagogiques en mathématiques appliquées mais elles existent et utilisent une syntaxe telle que

```Python
T = (1, 2, 3, 4)
```

mais les parenthèses peuvent être omises (au moins dans certains cas) ce qui fait que la syntaxe suivante est possible

```Python
T = 1, 2, 3, 4
```

On peut donc être surpris par le comportement de

```Python
pi = 3,14
```

*en réalité, un tuple composé de deux nombres, 3 et 14.*  Les opérations les plus perverses sont celles qui ne provoquent pas d'erreur.  Ainsi l'opération

```Python
pi * 3
```

renvoie-t-elle un tuple de 6 nombres $(3, 14, 3, 14, 3, 14)$. La fonction NumPy sinus `np.sin()` considère que le tuple peut être traité comme un tableau NumPy et retourne un tableau composé du sinus de chacun des deux nombres.

Des opérations numériques comme `pi + 3` ou `pi**2` vont donner une erreur `TypeError`.
