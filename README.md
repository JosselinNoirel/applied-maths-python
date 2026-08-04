# Applied Maths with Python · Maths appliquées avec Python

A bilingual, introductory reference for the Python, NumPy and Matplotlib tools
used in an applied mathematics course.

This site modernises and extends material originally developed in
[`JosselinNoirel/docpy`](https://github.com/JosselinNoirel/docpy). The French
material has been adapted to the new structure and is accompanied by an English
version.

The course documentation covers:

- Jupyter environments
- Python variables, objects, functions and control flow
- Graphs and visualisation
- Common Python, NumPy and Matplotlib functions
- Systems of equations, differentiation, integration and ODEs
- Common errors

La documentation, disponible en français et en anglais, présente :

- l'environnement Jupyter ;
- les variables, objets, fonctions et structures de contrôle Python ;
- les graphiques et la visualisation ;
- les fonctions usuelles de Python, NumPy et Matplotlib ;
- les systèmes d'équations, la dérivation, l'intégration et les EDO ;
- les erreurs classiques.

## Build locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-docs.txt
make docs
python -m http.server --directory _site 8000
```

Then open <http://localhost:8000/>.

GitHub Pages deployment is configured in `.github/workflows/pages.yml`.

## License

Except where otherwise indicated, this repository is licensed under the
[Creative Commons Attribution-NonCommercial 4.0 International License](LICENSE.md).
You may share and adapt the material with attribution, but not for commercial
purposes.
