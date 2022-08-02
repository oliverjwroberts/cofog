"""Sphinx configuration."""
project = "Cofog"
author = "Oliver Roberts"
copyright = "2022, Oliver Roberts"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
