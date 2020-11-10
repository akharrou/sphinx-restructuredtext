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

- :doc:`footnotes <Footnotes - rst,nts,ksa,2020-1110104849>`
- :doc:`citations <Citations - rst,nts,ksa,2020-1110112449>`
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


        Internal hyperlink targets:

        External hyperlink targets:

            See the Python_ home page for info.

            `Write to me`_ with your questions.

            .. _Python: http://www.python.org
            .. _Write to me: jdoe@example.com

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
