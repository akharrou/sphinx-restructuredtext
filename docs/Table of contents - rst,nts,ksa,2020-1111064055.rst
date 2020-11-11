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
        :depth: int                   <--- max level depth to list, relative to base
        :local:                       <--- generate local table, i.e only include subsections of base
        :backlinks: [entry|top|none]  <--- make headers link back to table of contents
        :class: text                  <--- set "classes" attribute value

**********************************************************************
Examples
**********************************************************************

.. contents::
    :depth: 3
    :local:
    :backlinks: top

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

        Page's TOC

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Directives ➤ Table of contents <https://docutils.sourceforge.io/docs/ref/rst/directives.html#table-of-contents>`_
