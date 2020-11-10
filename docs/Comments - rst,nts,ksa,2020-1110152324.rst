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

        .. This is a comment
        ..
        .. _so: is this!
        ..
        .. this:: too!
        ..
        .. |even| this:: !
        ..
        .. [this] however, is a citation.
        ..
        .. [and] this!

Out

    .. This is a comment
    ..
    .. _so: is this!
    ..
    .. this:: too!
    ..
    .. |even| this:: !
    ..
    .. [this] however, is a citation.
    ..
    .. [and] this!

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Spec. ➤ Comments <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#comments>`_
