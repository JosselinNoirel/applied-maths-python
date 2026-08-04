# How to edit these pages

```{raw} html
<p class="language-switch"><a href="../../fr/topics/howto.html">Français</a></p>
```

Most content changes only require editing the Markdown files under `docs/en/` and `docs/fr/`.

- Keep corresponding English and French pages at matching paths, such as `docs/en/topics/numpy.md` and `docs/fr/topics/numpy.md`.
- For a new bilingual topic, copying an existing pair such as the corresponding
  [good-practice page](good-practice.md) in each language is a safe starting
  point.
- Preserve the language-switch block near the top of each page.
- When adding a topic page, add it to both hidden `{toctree}` sections in the two `index.md` files. The label before `<...>` is the short navigation title.
- Keep code blocks *identical* across languages. Translate the surrounding explanation, but not variable names, comments, docstrings, strings or plot labels.
- Use `{py:func}\`numpy.mean\`` to link a documented function. Use `{concept}\`term\`` for an indexed bold notion and `{funcindex}\`name\`` for an indexed code-style function occurrence.
- Define newly documented functions with:

````markdown
```{py:function} numpy.example(argument)

Explanation.
```
````

Be careful:

- Avoid defining the same fully qualified function twice in one language; Sphinx will report a duplicate target.
- Keep Markdown links relative and omit `.html` in source files. For example: `[NumPy](numpy.md)`.
- Don’t edit `_site/` or `_build/`; those are generated directories.

Before committing, activate the environment and run:

```bash
source .venv/bin/activate
make docs
git diff --check
```

`make docs` builds both languages and treats Sphinx warnings as errors, so it
should catch most accidental breakage; `git diff --check` catches small Git-level
whitespace mistakes. Then inspect `_site/index.html` locally if you want a visual
check.
