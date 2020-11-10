################################################################################
RST ➤ Directives
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Directives are commands that do something specific. They can take
parameters and content as input.
They are an extension mechanism for reStructuredText, a way of adding
support for new constructs.
The directive block consists of any text on the first line of the directive
after the directive marker, and any subsequent indented text.

There are three logical parts to the directive block:

::

    .. figure:: larch.png   <--- 1. directive arguments
        :scale: 50          <--- 2. directive options

    The larch.              <--- 3. directive content

**********************************************************************
Examples
**********************************************************************

Image directive
============================================================

In
    ::

        .. image:: _assets/lion.jpg
            :scale: 50 %
            :alt: favorite lion
            :align: left

Out

    .. image:: _assets/lion.jpg
        :scale: 50 %
        :alt: favorite lion
        :align: left

----

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Spec. ➤ Directives <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#directives>`_
- `Docutils ➤ Directives <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_
