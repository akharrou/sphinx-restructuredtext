################################################################################
RST ➤ Table of contents
################################################################################

.. contents::
    :depth: 3
    :backlinks: top

**********************************************************************
Synopsis
**********************************************************************

You can generate a table of contents (TOC), like the one at the start of this
page, for any topic, i.e under any section or transition with the ``contents``
directive::

    .. contents:: [<title>]
        :depth: integer
        :local: flag (empty)
        :backlinks: [entry|top|none]
        :class: text

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        .. contents:: Table of contents
            :depth: 3
            :backlinks: top

Out

    .. figure:: _assets/toc\ -\ rst,imgs,ksa,2020-1111065308.jpg
        :alt: toc
        :align: center

        Would be page TOC

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Directives ➤ Table of contents <https://docutils.sourceforge.io/docs/ref/rst/directives.html#table-of-contents>`_
