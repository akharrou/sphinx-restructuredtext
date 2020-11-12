################################################################################
RST ➤ Math directive and role
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Math is supported with the ``math`` role for inline, and ``math`` directive for blocks. Input is LaTeX markup.

**********************************************************************
Examples
**********************************************************************

Inline
============================================================

In
    ::

        Einstein came up with :math:`e=mc^2`.

Out

    Einstein came up with :math:`e=mc^2`.

Block
============================================================

In
    ::

        Lorem ipsum dolor sit amet.

        .. math:: (a + b)^2 = a^2 + 2ab + b^2

        Consectetur adipiscing elit.

        .. math::

            (a + b)^2 = a^2 + 2ab + b^2

            (a - b)^2 = a^2 - 2ab + b^2

        Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

        .. math::

            (a + b)^2  &=  (a + b)(a + b) \\
                        &=  a^2 + 2ab + b^2

Out

        Lorem ipsum dolor sit amet.

        .. math:: (a + b)^2 = a^2 + 2ab + b^2

        Consectetur adipiscing elit.

        .. math::

            (a + b)^2 = a^2 + 2ab + b^2

            (a - b)^2 = a^2 - 2ab + b^2

        Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

        .. math::

            (a + b)^2  &=  (a + b)(a + b) \\
                        &=  a^2 + 2ab + b^2

More LaTeX
============================================================

In
    ::

        .. math::
            :nowrap:

            \begin{eqnarray}
                y    & = & ax^2 + bx + c \\
                f(x) & = & x^2 + 2xy + y^2
            \end{eqnarray}

Out

    .. math::
        :nowrap:

        \begin{eqnarray}
            y    & = & ax^2 + bx + c \\
            f(x) & = & x^2 + 2xy + y^2
        \end{eqnarray}

**********************************************************************
References
**********************************************************************

- `Sphinx ➤ Directives ➤ Math <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#math>`_
- `Sphinx ➤ Extensions ➤ spinx.ext.imgmath <https://www.sphinx-doc.org/en/master/usage/extensions/math.html#math-support>`_ (render math output as PNG/SVG)
