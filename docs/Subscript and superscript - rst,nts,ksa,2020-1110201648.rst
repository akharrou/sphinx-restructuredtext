################################################################################
RST ➤ Subscript and superscript
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Subscript and superscript are supported with the ``:sub:`txt``` and ``:sup:`txt``` syntax.

.. note::

    Whitespace or punctuation is required around interpreted text.
    Backslash-escaped whitespace can be used; the whitespace will be
    removed from the processed document:

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        H :sub:`2` O
        H\ :sub:`2`\ O

        E = mc\ :sup:`2`

Out

    | H :sub:`2` O
    | H\ :sub:`2`\ O

    E = mc\ :sup:`2`


.. tip::

    Readability of the plain text can be greatly improved with substitutions::

        The chemical formula for pure water is |H2O|.

            .. |H2O| replace:: H\ :sub:`2`\ O

**********************************************************************
References
**********************************************************************

- `Docutils ➤ RST ➤ Roles # Subscript <https://docutils.sourceforge.io/docs/ref/rst/roles.html#subscript>`_
- `Docutils ➤ RST ➤ Roles # Superscript <https://docutils.sourceforge.io/docs/ref/rst/roles.html#superscript>`_
