# Syntaxe Markdown et formules

```{raw} html
<p class="language-switch"><a href="../../en/topics/markdown.html">English</a></p>
```

Une cellule Markdown contient du texte structuré, des liens, des images et des
formules. Une ligne blanche sépare deux paragraphes. Cela permet de produire des
documents ou des rapports riches et complexes incluant directement le résultat
des calculs effectués avec Python, sous une forme de tableaux, de nombres ou de graphiques.

## Structurer et mettre en forme

````markdown
# Chapter
## Section
### Subsection

*Italic* text and **bold** text.

You can insert `code` inline or in a block:

```Python
x = np.linspace(0, 1)
```

- Unnumbered item
- Another item

1. First item
2. Second item
````

## Formules mathématiques

Une formule entre `$...$` reste dans le paragraphe, comme $a^2+b^2=c^2$. Une
formule entre `$$...$$` est centrée sur une ligne distincte :

```markdown
$$
  e^{i\pi} + 1 = 0
$$
```

$$
  e^{i\pi}+1=0
$$

Les espaces ordinaires sont généralement ignorés en mode mathématique. Pour un
décimal français, préférez le point `3.1415`, cohérent avec Python. La virgule `,` est en effet comprise par défaut comme un séparateur.

| Résultat | LaTeX |
|---|---|
| $x_{10}$ | `x_{10}` |
| $10^{-4}$ | `10^{-4}` |
| $\frac{a}{b}$ | `\frac{a}{b}` |
| $\alpha,\Delta,\infty$ | `\alpha, \Delta, \infty` |
| $\sin(x),\exp(x),\log(x)$ | `\sin(x), \exp(x), \log(x)` |
| $\sum_{k=0}^{n}u_k$ | `\sum_{k=0}^{n} u_k` |
| $\int_a^b f(x)\,dx$ | `\int_a^b f(x)\,dx` |

Les commandes mathématiques utilisent une barre oblique inverse `\`.

(Cf. [Mathematical expressions](https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols) par Overleaf.)
