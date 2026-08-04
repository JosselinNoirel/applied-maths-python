# Syntaxe Markdown et formules

```{raw} html
<p class="language-switch"><a href="../../en/topics/markdown.html">English</a></p>
```

Une cellule Markdown contient du texte structuré, des liens, des images et des
formules. Une ligne blanche sépare deux paragraphes.

## Structurer et mettre en forme

````markdown
# Chapitre
## Section
### Sous-section

Texte *italique* et texte {concept}`gras`.

- Élément non numéroté
- Autre élément

1. Premier élément
2. Deuxième élément
````

## Formules mathématiques

Une formule entre `$...$` reste dans le paragraphe, comme $a^2+b^2=c^2$. Une
formule entre `$$...$$` est centrée sur une ligne distincte :

```markdown
$$
e^{i\pi}+1=0
$$
```

$$
e^{i\pi}+1=0
$$

Les espaces ordinaires sont généralement ignorés en mode mathématique. Pour un
décimal français, préférez le point `3.1415`, cohérent avec Python, ou protégez
la virgule avec `3{,}1415`.

## Écritures utiles

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
