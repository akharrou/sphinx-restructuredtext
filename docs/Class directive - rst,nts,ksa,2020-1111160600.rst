################################################################################
RST ➤ Class directive
################################################################################

**********************************************************************
Synopsis
**********************************************************************

You can style, set the ``classes`` attribute of, blocks of content with
the ``class`` directive.

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In

    .. code-block:: rst

        .. class:: special

        This is a "special" paragraph.

        .. class:: exceptional remarkable

        An Exceptional Section
        ======================

        This is an ordinary paragraph.

        .. class:: multiple

        First paragraph.

        Second paragraph.

Out

    .. code-block:: html

        <paragraph classes="special">
            This is a "special" paragraph.
        <section classes="exceptional remarkable">
            <title>
                An Exceptional Section
            <paragraph>
                This is an ordinary paragraph.
            <paragraph classes="multiple">
                First paragraph.
            <paragraph classes="multiple">
                Second paragraph.

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Directives ➤ Class <https://docutils.sourceforge.io/docs/ref/rst/directives.html#class>`_
