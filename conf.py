"""Shared Sphinx configuration for the English and French sites."""

from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

project = "Applied Maths with Python"
author = "Josselin Noirel"
copyright = "2026, Josselin Noirel — CC BY-NC 4.0"

language = os.environ.get("DOC_LANGUAGE", "en")

extensions = [
    "myst_parser",
    "sphinx_codeautolink",
    "extensions.semantic_index",
]

source_suffix = {".md": "markdown"}
root_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
]

html_theme = "pydata_sphinx_theme"
html_title = "Maths appliquées avec Python" if language == "fr" else project
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "show_nav_level": 2,
    "navigation_depth": 3,
    "collapse_navigation": False,
    "navbar_align": "left",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/JosselinNoirel/applied-maths-python",
            "icon": "fa-brands fa-github",
        }
    ],
}

# Analyse Python examples and link resolvable names to local reference entries.
codeautolink_warn_on_missing_inventory = False
codeautolink_global_preface = "import numpy as np"
