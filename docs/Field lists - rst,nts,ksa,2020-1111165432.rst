################################################################################
RST ➤ Field lists
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Field lists are supported.

**********************************************************************
Examples
**********************************************************************

Field lists
============================================================

In
    ::

        :Date:          2001-08-16
        :Version:       1
        :Authors:       - John Doe
                        - Steve Smith
                        - Martin Ruberr
        :Indentation:   Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        :Parameter i:   integer

Out

    :Date:          2001-08-16
    :Version:       1
    :Authors:       - John Doe
                    - Steve Smith
                    - Martin Ruberr
    :Indentation:   Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    :Parameter i:   integer

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Spec. ➤ Field lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#field-lists>`_
