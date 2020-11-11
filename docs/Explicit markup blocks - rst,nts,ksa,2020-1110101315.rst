################################################################################
RST ➤ Explicit markup blocks
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Explicit blocks are text blocks:

- which begin with ``..`` + whitespace
- whose subsequent lines (if any) are indented
- and which end at the first unindented line

They are used for:

- :doc:`footnotes <Footnotes - rst,nts,ksa,2020-1110104849>`
- :doc:`citations <Citations - rst,nts,ksa,2020-1110112449>`
- :doc:`hyperlink targets <Hyperlink targets - rst,nts,ksa,2020-1110115624>`
- :doc:`directives <Directives - rst,nts,ksa,2020-1110130642>`
- :doc:`substitution definitions <Substitution definitions - rst,nts,ksa,2020-1110162216>`
- :doc:`comments <Comments - rst,nts,ksa,2020-1110152324>`

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

    .. [#note] Footnote content


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

        Section name
        ------------

            .. _paragraph:
            .. _target:

        This one links to the paragraph_ below, ...

        Lorem ipsum...

        ... this points to the same `paragraph above`_.

            .. _`paragraph above`: paragraph_

        See doc-utils_ if you have any questions. Also see `Section name`_.

            .. _doc-utils:  https://
                            docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#hyperlink-targets

Out

Section name
------------

        .. _paragraph:
        .. _target:

    This one links to the paragraph_ below, ...

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quisque id diam vel quam elementum pulvinar. Orci nulla pellentesque dignissim enim. Magna fringilla urna porttitor rhoncus dolor purus. Mollis nunc sed id semper risus in hendrerit gravida rutrum. Faucibus turpis in eu mi bibendum. Ultrices neque ornare aenean euismod elementum. Consectetur lorem donec massa sapien faucibus. At imperdiet dui accumsan sit amet nulla facilisi morbi tempus. Rhoncus urna neque viverra justo nec ultrices dui. Sed faucibus turpis in eu mi bibendum.

    ... this points to the same `paragraph above`_.

        .. _`paragraph above`: paragraph_

    See doc-utils_ if you have any questions. Also see `Section name`_.

        .. _doc-utils:  https://
                        docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#hyperlink-targets

Directives
============================================================

In
    ::

        .. image:: _assets/lion\ -\ rst,imgs,ksa,2020-1111065317.jpg
            :scale: 50 %
            :alt: favorite lion
            :align: left

Out

    .. image:: _assets/lion\ -\ rst,imgs,ksa,2020-1111065317.jpg
        :scale: 50 %
        :alt: favorite lion

Substitution definitions
============================================================

In
    ::

        Meet |name| !

        .. |name| replace:: **John Doe**

Out

    Meet |name| !

    .. |name| replace:: **John Doe**

Comments
============================================================

In
    ::

        .. some restructuredtext

Out

    .. some restructuredtext

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Spec. ➤ Explicit markup blocks <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#explicit-markup-blocks>`_
