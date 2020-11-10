################################################################################
RST ➤ Formatting
################################################################################

**********************************************************************
Synopsis
**********************************************************************

You have the following facilities available for text formatting:

- :ref:`italics <Formatting - rst,nts,ksa,2020-1109221434:Emphasis>`, with ``*text*``
- :ref:`boldface <Formatting - rst,nts,ksa,2020-1109221434:Emphasis>`, with ``**text**``
- :doc:`subscript and superscript <Subscript and superscript - rst,nts,ksa,2020-1110201648>`
- :doc:`typesetting math <Math - rst,nts,ksa,2020-1110203418>`

**********************************************************************
Examples
**********************************************************************

Emphasis
============================================================

In

    ::

        some *text* is italic
        some other **text** is bold

Out

    | some *text* is italic
    | some other **text** is bold

Subscript, superscript
============================================================

In

    ::

        The chemical formula for pure water is |H2O|.

            .. |H2O| replace:: H\ :sub:`2`\ O

Out

    The chemical formula for pure water is |H2O|.

        .. |H2O| replace:: H\ :sub:`2`\ O

Math
============================================================

In

    ::

        .. math::

            (a + b)^2  &=  (a + b)(a + b) \\
                        &=  a^2 + 2ab + b^2

Out

    .. math::

        (a + b)^2  &=  (a + b)(a + b) \\
                    &=  a^2 + 2ab + b^2

**********************************************************************
References
**********************************************************************

- `Sphinx ➤ RST ➤ Basic # Inline markup <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#inline-markup>`_
