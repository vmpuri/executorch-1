# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


# Configuration file for the Sphinx documentation builder.
# Created by isphinx-quickstart on Tue Jul 19 14:58:12 2022.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import pytorch_sphinx_theme

sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------

project = "ExecuTorch"
copyright = "2023, ExecuTorch"
author = "ExecuTorch Contributors"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

import os
import sys

sys.path.insert(0, os.path.abspath("../../"))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "myst_parser",
    "sphinx_design",
    "sphinx_gallery.gen_gallery",
]

templates_path = ["_templates"]


myst_enable_extensions = [
    "colon_fence",
]

sphinx_gallery_conf = {
    "examples_dirs": ["tutorials_source"],
    "gallery_dirs": ["tutorials"],
    "filename_pattern": "/tutorials/",
    "promote_jupyter_magic": True,
    "backreferences_dir": None,
    "first_notebook_cell": ("%matplotlib inline"),
}

source_suffix = [".rst", ".md"]


autodoc_typehints = "none"

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["../_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pytorch_sphinx_theme"
html_theme_path = [pytorch_sphinx_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "pytorch_project": "executorch",
    "display_version": True,
    "logo_only": True,
    "collapse_navigation": False,
    "sticky_navigation": False,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = ["css/custom.css"]
html_js_files = ["js/custom.js"]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "numpy": ("https://docs.scipy.org/doc/numpy/", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
}

# Custom directives defintions to create cards on main TorchServe page

from custom_directives import (
    CustomCardEnd,
    CustomCardItem,
    CustomCardStart,
    SupportedDevices,
    SupportedProperties,
)
from docutils.parsers import rst

# Register custom directives


rst.directives.register_directive("devices", SupportedDevices)
rst.directives.register_directive("properties", SupportedProperties)
rst.directives.register_directive("customcardstart", CustomCardStart)
rst.directives.register_directive("customcarditem", CustomCardItem)
rst.directives.register_directive("customcardend", CustomCardEnd)
