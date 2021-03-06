################################################################################
RST ➤ Comments
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Comment out anything by prepending the line with ``..``.

.. note::

    Explicit markup blocks recognized as either citation, directive,
    footnote, hyperlink target or substitution definition will not
    be processed as comments.

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

    .. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    .. tempor incididunt ut labore et dolore magna aliqua.

Out

    .. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    .. tempor incididunt ut labore et dolore magna aliqua.

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Spec. ➤ Comments <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#comments>`_
