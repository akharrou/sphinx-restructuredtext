################################################################################
RST ➤ Definition lists
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Definition lists are supported.

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        Term 1
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.

        Term 2
            Faucibus turpis in eu mi bibendum.

        Term 3
            Sed faucibus turpis in eu mi bibendum.

Out

    Term 1
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.

    Term 2
        Faucibus turpis in eu mi bibendum.

    Term 3
        Sed faucibus turpis in eu mi bibendum.


Variations
============================================================

In
    ::

        Term 1
            Definition 1.

        Term 2
            Paragraph 1.

            Paragraph 2.

        Term 3 : classifier
            Definition 3.

        Term 4 : classifier one : classifier two
            Definition 4.

        Term 5
            Lorem ipsum...

            .. code-block:: python

                print('codeblock')

            Lorem ipsum...

        Term 6
            Lorem ipsum...

            Term 6-1
                Lorem ipsum...

Out
    Term 1
        Definition 1.

    Term 2
        Paragraph 1.

        Paragraph 2.

    Term 3 : classifier
        Definition 3.

    Term 4 : classifier one : classifier two
        Definition 4.

    Term 5
        Lorem ipsum...

        .. code-block:: python

            print('codeblock')

        Lorem ipsum...

    Term 6
        Lorem ipsum...

        Term 6-1
            Lorem ipsum...

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Spec. ➤ Definition lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#definition-lists>`_
