################################################################################
RST ➤ Admonitions
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Admonitions are supported.
The following admonition directives have been implemented:

- attention
- caution
- danger
- error
- hint
- important
- note
- tip
- warning

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        .. attention:: Lorem ipsum ...

        .. caution:: Lorem ipsum ...

        .. danger:: Lorem ipsum ...

        .. error:: Lorem ipsum ...

        .. hint:: Lorem ipsum ...

        .. important:: Lorem ipsum ...

        .. note:: Lorem ipsum ...

        .. tip:: Lorem ipsum ...

        .. warning:: Lorem ipsum ...

Out

        .. hint:: Lorem ipsum ...

        .. important:: Lorem ipsum ...

        .. tip:: Lorem ipsum ...

----

        .. note:: Lorem ipsum ...

----

        .. attention:: Lorem ipsum ...

        .. caution:: Lorem ipsum ...

        .. warning:: Lorem ipsum ...

----

        .. danger:: Lorem ipsum ...

        .. error:: Lorem ipsum ...



**********************************************************************
References
**********************************************************************

- `Sphinx ➤ Directives ➤ Paragraph-level markup <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#paragraph-level-markup>`_
- `Docutils ➤ Directives ➤ Admonitions <https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonitions>`_
