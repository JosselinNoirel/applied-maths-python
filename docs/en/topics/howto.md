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

## Assets

For this repository, the simplest structure is:

```text
docs/
├── en/
│   ├── _static/
│   │   ├── images/
│   │   │   └── example.png
│   │   └── notebooks/
│   │       └── example.ipynb
│   └── topics/
└── fr/
    ├── _static/
    │   ├── images/
    │   │   └── example.png
    │   └── notebooks/
    │       └── example.ipynb
    └── topics/
```

From a topic page, reference an image with:

```markdown
![Description of the figure](../_static/images/example.png)
```

Link a downloadable notebook with:

```markdown
[Download the example notebook](../_static/notebooks/example.ipynb)
```

- Commit the assets to Git. GitHub Actions only sees committed files.
- If an asset is used by both languages, currently the safest approach is to put a copy under both `docs/en/_static/` and `docs/fr/_static/`.
- Use lowercase filenames without spaces, for example `fourier-spectrum.png`.
- Compress large PNG files and notebooks where practical; repository assets are downloaded by site visitors.
- Note that the notebook will be offered as a download. Sphinx is not currently configured to render `.ipynb` files as documentation pages.

After adding an asset, you can check it locally with:

```bash
source .venv/bin/activate
make docs
```

Then open `_site/index.html` and test the image or download link locally. If it works there and the asset is committed, it should work on GitHub Pages as well.
