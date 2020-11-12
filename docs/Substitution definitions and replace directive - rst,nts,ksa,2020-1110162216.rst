################################################################################
RST ➤ Substitution definitions and replace directive
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Aliases allowing for embedded inline-compatible directives, without the
leading ".. ".
They are a way to include arbitrarily complex inline structures within
text, while keeping the details out of the flow of text.

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        Meet |name| |lion| !

        .. |name| replace:: **John Doe**

        .. |lion| image:: _assets/lion\ -\ rst,imgs,ksa,2020-1111065317.jpg
            :scale: 50%

Out

    Meet |name| |lion| !

    .. |name| replace:: **John Doe**

    .. |lion| image:: _assets/lion\ -\ rst,imgs,ksa,2020-1111065317.jpg
        :scale: 50%

**********************************************************************
References
**********************************************************************

- `Docutils ➤ RST ➤ Substitutino definitions <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-definitions>`_
