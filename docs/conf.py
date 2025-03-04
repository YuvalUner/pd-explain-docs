# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If your documentation sources are in a different directory relative to this
# conf.py, adjust the path accordingly.
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

project = 'Pd-Explain'
author = 'analysis-bots'
release = '1.0.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',    # Automatically document modules
    'sphinx.ext.napoleon',   # Support for NumPy and Google style docstrings
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # Default theme; 'sphinx_rtd_theme' is popular on Read the Docs
html_static_path = ['_static']