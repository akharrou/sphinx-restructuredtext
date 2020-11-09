# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# import sphinx_rtd_theme
import sphinx_material
from recommonmark.parser import CommonMarkParser

# -- Project information -----------------------------------------------------

project = 'Markdown Notebook'
copyright = '2020, akharrou'
author = 'akharrou'

# The full version, including alpha/beta/rc tags
release = '0.1.0'


# -- General configuration ---------------------------------------------------

master_doc = 'index'
primary_domain = None
nitpicky = True
numfig = True
smartquotes = True
language = "en"


# reStructuredText linter -> rstcheck; requires: pip install rstcheck; ps, this opption is just a note for me, has no use in sphinx
linter = 'rstcheck'


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [

    # enable ReadTheDocs sphinx theme; (https://www.sphinx-doc.org/en/master/usage/theming.html); (https://sphinx-rtd-theme.readthedocs.io/en/stable/installing.html); requires: pip install sphinx-rtd-theme
    # 'sphinx_rtd_theme',

    # enable markdown; (https://www.sphinx-doc.org/en/master/usage/markdown.html); (https://recommonmark.readthedocs.io/); requires: pip install --upgrade recommonmark
    'recommonmark',


    # "sphinx.ext.autodoc",
    # "numpydoc",
    # "sphinx.ext.doctest",
    # "sphinx.ext.extlinks",
    # "sphinx.ext.intersphinx",
    # "sphinx.ext.todo",
    # "sphinx.ext.mathjax",
    # "sphinx.ext.viewcode",
    # "nbsphinx",
    # "sphinx_markdown_tables",
    # "sphinx_copybutton",
]

autosummary_generate = True
# autoclass_content = "class"


# Cross-reference page@header; (https://recommonmark.readthedocs.io/en/latest/#linking-to-headings-in-other-files); (https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html)
# syntax rst          ->   :ref:`path:header`  ->  :ref:`index:Introduction`
# syntax recommonmark ->   [My Subtitle]: <path:Header>
extensions.append('sphinx.ext.autosectionlabel')
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


source_parsers = {
    '.md': CommonMarkParser,
}


# -- Options for HTML output -------------------------------------------------

html_use_index = True
html_copy_source = True
html_show_sourcelink = True
html_show_copyright = True
html_show_sphinx = True
html_compact_lists = True
html_secnumber_suffix = '.'
html_add_permalinks = '⚓︎'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_css_files = ['']
# html_js_files = ['']

html_logo = '_static/alfred.png'
html_favicon = '_static/alfred.png'
html_title = 'Home'

# - THEMES - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# default
# html_theme = 'alabaster'


# https://sphinx-rtd-theme.readthedocs.io/en/stable/installing.html
# html_theme = 'sphinx_rtd_theme'


# https://bashtage.github.io/sphinx-material/
html_theme = 'sphinx_material'

# HTML theme options
html_theme_options = {

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/akharrou/sphinx-markdown/',
    'repo_name': 'sphinx-markdown',
    'repo_type': 'github',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://akharrou.github.io/sphinx-markdown/',

    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',

    # 'html_minify': True,
    # 'css_minify': True,

    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

    # Set the name of the project to appear in the navigation.
    'nav_title': 'Markdown Notebook',

    # Menu bar pages
    'master_doc': False, # includes master document in menu
    'nav_links': [
      { 'href': 'index', 'title': 'Home', 'internal': True, },
      { 'href': 'test', 'title': 'Notebooks', 'internal': True, },
    ],
    # "heroes": {
    #     "index": "Welcome to the best Markdown notes on the internet !",
    # },

    # "version_dropdown": True,
    # "version_json": "_static/versions.json",
    # "version_info": {
    #     "Release": "test.html",
    #     "Development": "https://bashtage.github.io/sphinx-material/devel/",
    #     "Release (rel)": "/sphinx-material/",
    #     "Development (rel)": "/sphinx-material/devel/",
    # },

    "table_classes": ["plain"],

    # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

    # Set the color and the accent color; red, pink, deep-purple, indigo, blue, teal, green, deep-orange;
    'color_primary': 'deep-orange',
    'color_accent': 'deep-blue',
    # 'theme_color': '212121',
    # 'logo_icon': '&#9997',

    'globaltoc_depth': 3, # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_collapse': False, # If False, expand all TOC entries
    'globaltoc_includehidden': False, # If True, show hidden TOC entries
}
