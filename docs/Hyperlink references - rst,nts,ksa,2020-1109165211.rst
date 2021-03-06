################################################################################
RST ➤ Hyperlink references
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Hyperlink references are pointers to markers (:doc:`hyperlink targets <Hyperlink targets - rst,nts,ksa,2020-1110115624>`). They render to clickable links that redirect (points) to wherever the matching hyperlink target (marker) points to. Hyperlink refernces follow the form: ```marker-name`_``.

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        .. _Python: https://www.python.org/   <--- target, marker

        See the Python_ home page for info.   <--- reference, pointer

Out

    .. _Python: https://www.python.org/

    See the Python_ home page for info.

**********************************************************************
References
**********************************************************************

- `Docutils ➤ RST ➤ Hyerplink references <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#hyperlink-references>`_
