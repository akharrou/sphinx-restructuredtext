################################################################################
RST ➤ Numbering
################################################################################

**********************************************************************
Synopsis
**********************************************************************

You can number sections, figures, tables, and code-blocks.

**********************************************************************
Examples
**********************************************************************

Sections (document wide)
============================================================

In
    ::

        .. toctree::
            :numbered: 2  # number all headings ranked >= 2 (i.e parts, chapters)

Sections (page wide)
============================================================

In

    .. code-block:: python

        # conf.py
        rst_epilog = """
        .. sectnum::
            :depth: int
            :prefix: str
            :suffix: str
            :start: int
        """

Figures, tables and code-blocks
============================================================

In

    .. code-block:: python

        # conf.py
        numfig = True
        numfig_format = {
            'figure': 'Fig. %s',
            'table': 'Table %s',
            'code-block': 'Listing %s',
            'section': 'Section'
        }
        numfig_secnum_depth = 0 # [
        #     0 -> 1., 2., N., ...                            |
        #     1 -> <section>.1, <section>.2, <section>.N,...  |
        #     2 -> l1.l2.l3.1, l1.l2.l3.2, l1.l2.l3.N.,...
        # ]

Out

    .. image:: _assets/fig-no-num\ -\ rst,imgs,ksa,2020-1111072638.jpg
        :scale: 70

    .. code-block:: python

        # conf.py
        numfig = True

    .. image:: _assets/fig-num\ -\ rst,imgs,ksa,2020-1111072653.jpg
        :scale: 70

    .. code-block:: python

        # conf.py
        numfig_format = {
            'figure': 'Fig. %s:',
        }

    .. image:: _assets/fig-num-format\ -\ rst,imgs,ksa,2020-1111072645.jpg
        :scale: 70

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Directives ➤ Automatic section numbering <https://docutils.sourceforge.io/docs/ref/rst/directives.html#sectnum>`_
- `Sphinx ➤ Directives ➤ toctree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#table-of-contents>`_
- `Sphinx ➤ Configuration ➤ rst_epilog <https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=configuration#confval-rst_epilog>`_
- `Sphinx ➤ Configuration ➤ numfig, numfig_format, ... <https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=configuration#confval-numfig>`_
