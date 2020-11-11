################################################################################
RST ➤ Figure
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Figures are supported with the ``.. figure:: <image>`` directive.
Figures consist of an ``image`` directive, plus an optional caption,
single paragraph (below that), plus an optional legend (table) below
that::

    .. figure:: <path>
        :width: int
        :height: int
        :scale: int%
        :align: [left|center|right]
        :alt: text
        :target: text

        <caption>

        <paragraph>

        <legend>

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        .. figure:: _assets/lion\ -\ rst,imgs,ksa,2020-1111065317.jpg
            :scale: 50 %
            :align: center
            :alt: lion

            Caption 1.

        .. figure:: _assets/lion\ -\ rst,imgs,ksa,2020-1111065317.jpg
            :scale: 50 %
            :align: center
            :alt: lion

            Caption 2.
Out

    .. figure:: _assets/lion\ -\ rst,imgs,ksa,2020-1111065317.jpg
        :scale: 50 %
        :align: center
        :alt: lion

        Caption 1.

    .. figure:: _assets/lion\ -\ rst,imgs,ksa,2020-1111065317.jpg
        :scale: 50 %
        :align: center
        :alt: lion

        Caption 2.

.. note:: Figures are automatically numbered in the order of their declaration.

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Directives ➤ Figure <https://docutils.sourceforge.io/docs/ref/rst/directives.html#figure>`_
