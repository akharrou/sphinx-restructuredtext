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

# -- Project information -----------------------------------------------------

project = 'Markdown Notebook'
copyright = '2020, 💎 Akharrou'
author = 'akharrou'
release = '0.1.0' # full version, including alpha/beta/rc tags


# -- General configuration ---------------------------------------------------

needs_sphinx = '3.3.0'

master_doc = 'index'
primary_domain = None
nitpicky = True
numfig = True
smartquotes = True
language = "en"
highlight_language = 'rst'
linter = 'rstcheck'
autosummary_generate = True
autoclass_content = "class"
latex_engine = 'pdflatex' # 'xelatex' | 'lualatex'
templates_path = ['_templates']

rst_epilog = """
.. |psf| replace:: Python Software Foundation
.. |date| date:: %Y/%m/%d
.. |time| date:: %H:%M:%S
.. |datetime| date:: %Y/%m/%d, %H:%M
.. |timestamp| date:: %Y%m%d%H%M%S
"""

rst_prolog = """
"""

numfig = True
numfig_format = {
    'figure': 'Fig. %s:',
    'table': 'Table %s',
    'code-block': 'Listing %s',
    'section': 'Section'
}
numfig_secnum_depth = 0 # [
    #     0 -> 1., 2., N., ...                            |
    #     1 -> <section>.1, <section>.2, <section>.N,...  |
    #     2 -> l1.l2.l3.1, l1.l2.l3.2, l1.l2.l3.N.,...
    # ]

suppress_warnings = [
    # 'app.add_node',
    # 'app.add_directive',
    # 'app.add_role',
    # 'app.add_generic_role',
    # 'app.add_source_parser',
    # 'download.not_readable',
    # 'image.not_readable',
    # 'ref.term',
    # 'ref.ref',
    # 'ref.numref',
    # 'ref.keyword',
    # 'ref.option',
    # 'ref.citation',
    # 'ref.footnote',
    # 'ref.doc',
    # 'ref.python',
    # 'misc.highlighting_failure',
    # 'toc.circular',
    # 'toc.secnum',
    # 'epub.unknown_project_files',
    # 'epub.duplicated_toc_entry',
    # 'autosectionlabel.*'
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

extensions = [
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


# enable markdown support; (https://www.sphinx-doc.org/en/master/usage/markdown.html); (https://recommonmark.readthedocs.io/); requires: pip install --upgrade recommonmark
from recommonmark.parser import CommonMarkParser
extensions.append('recommonmark')
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
source_parsers = {
    '.md': CommonMarkParser,
}


# enable cross-reference with `file:header` syntax; (https://recommonmark.readthedocs.io/en/latest/#linking-to-headings-in-other-files); (https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html)
extensions.append('sphinx.ext.autosectionlabel')
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3



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

html_logo = '_static/alfred_100.png'
html_favicon = '_static/alfred_100.png'
html_title = 'Home'


# - THEMES - - - - - - - - - - - - - - - - - - - -

# default
# html_theme = 'alabaster'


# enable sphinx ReadTheDocs theme; (https://www.sphinx-doc.org/en/master/usage/theming.html); (https://sphinx-rtd-theme.readthedocs.io/en/stable/installing.html); requires: pip install sphinx-rtd-theme
import sphinx_rtd_theme
extensions.append('sphinx_rtd_theme')
html_theme = 'sphinx_rtd_theme'


# enable sphinx material theme; (https://bashtage.github.io/sphinx-material/)
# import sphinx_material
# html_theme = 'sphinx_material'
# html_theme_options = {

#     # Set the repo location to get a badge with stats
#     'repo_url': 'https://github.com/akharrou/sphinx-markdown/',
#     'repo_name': 'sphinx-markdown',
#     'repo_type': 'github',

#     # Specify a base_url used to generate sitemap.xml. If not
#     # specified, then no sitemap will be built.
#     'base_url': 'https://akharrou.github.io/sphinx-markdown/',

#     # Set you GA account ID to enable tracking
#     # 'google_analytics_account': 'UA-XXXXX',

#     # 'html_minify': True,
#     # 'css_minify': True,

#     # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

#     # Set the name of the project to appear in the navigation.
#     'nav_title': 'Markdown Notebook',

#     # Menu bar pages
#     'master_doc': False, # includes master document in menu
#     'nav_links': [
#       { 'href': 'index', 'title': 'Home', 'internal': True, },
#       { 'href': 'test', 'title': 'Notebooks', 'internal': True, },
#     ],
#     # "heroes": {
#     #     "index": "Welcome to the best Markdown notes on the internet !",
#     # },

#     # "version_dropdown": True,
#     # "version_json": "_static/versions.json",
#     # "version_info": {
#     #     "Release": "test.html",
#     #     "Development": "https://bashtage.github.io/sphinx-material/devel/",
#     #     "Release (rel)": "/sphinx-material/",
#     #     "Development (rel)": "/sphinx-material/devel/",
#     # },

#     "table_classes": ["plain"],

#     # -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

#     # Set the color and the accent color; red, pink, deep-purple, indigo, blue, teal, green, deep-orange;
#     'color_primary': 'deep-orange',
#     'color_accent': 'deep-blue',
#     # 'theme_color': '212121',
#     # 'logo_icon': '&#9997',

#     'globaltoc_depth': 3, # Visible levels of the global TOC; -1 means unlimited
#     'globaltoc_collapse': False, # If False, expand all TOC entries
#     'globaltoc_includehidden': False, # If True, show hidden TOC entries
# }
