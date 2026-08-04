# Markdown syntax and formulas

```{raw} html
<p class="language-switch"><a href="../../fr/topics/markdown.html">Français</a></p>
```

A Markdown cell contains structured text, links, images and formulas. A blank
line separates two paragraphs.

## Structure and formatting

````markdown
# Chapter
## Section
### Subsection

*Italic* text and {concept}`bold` text.

- Unnumbered item
- Another item

1. First item
2. Second item
````

## Mathematical formulas

A formula between `$...$` remains inside the paragraph, as in
$a^2+b^2=c^2$. A formula between `$$...$$` is centred on a separate line:

```markdown
$$
e^{i\pi}+1=0
$$
```

$$
e^{i\pi}+1=0
$$

Ordinary spaces are generally ignored in mathematical mode.

## Useful notation

| Result | LaTeX |
|---|---|
| $x_{10}$ | `x_{10}` |
| $10^{-4}$ | `10^{-4}` |
| $\frac{a}{b}$ | `\frac{a}{b}` |
| $\alpha,\Delta,\infty$ | `\alpha, \Delta, \infty` |
| $\sin(x),\exp(x),\log(x)$ | `\sin(x), \exp(x), \log(x)` |
| $\sum_{k=0}^{n}u_k$ | `\sum_{k=0}^{n} u_k` |
| $\int_a^b f(x)\,dx$ | `\int_a^b f(x)\,dx` |

Mathematical commands use a backslash `\`.
