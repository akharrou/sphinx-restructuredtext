################################################################################
RST ➤ Markdown
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Sphinx can support Markdown source files with just a few configuration tweaks:

.. code-block:: bash

    pip install --upgrade recommonmark

Add the following to your ``conf.py``:

.. code-block:: python

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

**********************************************************************
References
**********************************************************************

- `Sphinx ➤ Markdown <https://www.sphinx-doc.org/en/master/usage/markdown.html>`_
