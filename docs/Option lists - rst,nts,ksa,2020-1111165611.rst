################################################################################
RST ➤ Option lists
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Option lists are supported.

**********************************************************************
Examples
**********************************************************************

Option lists
============================================================

In
    ::

        -a          Output all.
        -b          Output both (this description is
                    quite long).
        -c arg      Output just arg.
        --long         Output all day long.

        -p          First paragraph.

                    Second paragraph.

        --very-long-option  Long options.

        --an-even-longer-option
                Description can also start on the next line.

        -2, --two  Two variants.

        -f FILE, --file=FILE  Synonymous options; both have
                            arguments.

        /V         A VMS/DOS-style option.

Out
    -a          Output all.
    -b          Output both (this description is
                quite long).
    -c arg      Output just arg.
    --long         Output all day long.

    -p          First paragraph.

                Second paragraph.

    --very-long-option  Long options.

    --an-even-longer-option
            Description can also start on the next line.

    -2, --two  Two variants.

    -f FILE, --file=FILE  Synonymous options; both have
                        arguments.

    /V         A VMS/DOS-style option.

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Spec. ➤ Option lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#option-lists>`_
