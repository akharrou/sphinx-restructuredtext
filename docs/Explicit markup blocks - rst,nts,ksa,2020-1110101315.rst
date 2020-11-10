################################################################################
RST ➤ Explicit markup blocks
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Explicit blocks are text blocks:

- which begin with ".. "
- whose subsequent lines (if any) are indented
- and which end at the first unindented line

They are used for:

- :doc:`Footnotes <Footnotes - rst,nts,ksa,2020-1110104849>`
- citations
- hyperlink targets
- directives
- substitution definitions
- comments

**********************************************************************
Examples
**********************************************************************

Footnotes
============================================================

In
    ::

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua.[#note]_

        .. [#note] Footnote content

Out

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. [#note]_


Citations
============================================================

In
    ::

        Here is a citation reference: [CIT2002]_.

        .. [CIT2002]

            This is the citation.  It's just like a footnote,
            except the label is textual.


Out

    Here is a citation reference: [CIT2002]_.

    .. [CIT2002]

        This is the citation.  It's just like a footnote,
        except the label is textual.

Hyperlink targets
============================================================

In
    ::



Out

Directives
============================================================

In
    ::



Out

Substitution definitions
============================================================

In
    ::



Out

Comments
============================================================

In
    ::



Out

**********************************************************************
References
**********************************************************************

- `Docutils ➤ RST ➤ Explicit markup blocks <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#explicit-markup-blocks>`_

.. [#note] Footnote content
