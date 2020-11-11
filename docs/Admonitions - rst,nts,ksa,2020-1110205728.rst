################################################################################
RST ➤ Admonitions
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Admonitions are supported.
The following admonition directives have been implemented:

- ``attention``
- ``caution``
- ``danger``
- ``error``
- ``hint``
- ``important``
- ``note``
- ``tip``
- ``warning``

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        .. hint:: Lorem ipsum ...

        .. important:: Lorem ipsum ...

        .. tip:: Lorem ipsum ...

        .. note:: Lorem ipsum ...

        .. attention:: Lorem ipsum ...

        .. caution:: Lorem ipsum ...

        .. warning:: Lorem ipsum ...

        .. danger::     Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit, sed do eiusmod tempor incididunt ut labore et
                        dolore magna aliqua.

        .. error::

                Lorem ipsum dolor sit amet, consectetur adipiscing
                elit, sed do eiusmod tempor incididunt ut labore et
                dolore magna aliqua.

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

        .. danger::     Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit, sed do eiusmod tempor incididunt ut labore et
                        dolore magna aliqua.

        .. error::

                Lorem ipsum dolor sit amet, consectetur adipiscing
                elit, sed do eiusmod tempor incididunt ut labore et
                dolore magna aliqua.

**********************************************************************
References
**********************************************************************

- `Sphinx ➤ Directives ➤ Paragraph-level markup <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#paragraph-level-markup>`_
- `Docutils ➤ Directives ➤ Admonitions <https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonitions>`_
