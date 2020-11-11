################################################################################
RST ➤ Toctree
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Sphinx uses a custom directive, the ``toctree`` directive, to add relations
between the single files in the documentation, and to create a master table
of contents::

    .. toctree::
        :caption: str             <--- alternate title
        :name: str                <--- toc ID
        :titlesonly:              <--- display only the title of document not other same level headings
        :maxdepth: int <level>    <--- display headings up to depth level
        :numbered: int <level>    <--- number headings up to depth level
        :glob:                    <--- specify files with glob patterns, files ordered by name alphabetically
        :reversed:                <--- reverse sorting
        :hidden:                  <--- inform sphinx of document hierarchy, but don't display
        :includehidden:           <--- keep only top-level toctree, hide all others

.. note::   To create a table of contents for single documents, use the
            :doc:`standard RST contents directive <Table of contents - rst,nts,ksa,2020-1111064055>`.

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        .. toctree::
            :caption: Table of Contents
            :name: mastertoc
            :maxdepth: 2
            :numbered: 2
            :glob:

**********************************************************************
References
**********************************************************************

- `Sphinx ➤ Directives ➤ toctree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#table-of-contents>`_
