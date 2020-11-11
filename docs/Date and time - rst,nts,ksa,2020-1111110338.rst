################################################################################
RST ➤ Date and time
################################################################################

**********************************************************************
Synopsis
**********************************************************************

You can generate the current local date and time with the ``date`` and
``time`` directvies respectively.

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        .. |date| date:: %Y/%m/%d
        .. |time| date:: %H:%M:%S
        .. |datetime| date:: %Y/%m/%d, %H:%M
        .. |timestamp| date:: %Y%m%d%H%M%S

        Today's date is |date|.
        This document was generated on |date| at |time|.
        This document was generated on |datetime|.
        This document was generated on |timestamp|.

Out

    .. |date| date:: %Y/%m/%d
    .. |time| date:: %H:%M:%S
    .. |datetime| date:: %Y/%m/%d, %H:%M
    .. |timestamp| date:: %Y%m%d%H%M%S

    | **Date:** |date|
    | **Time:** |date| at |time|
    | **Datetime:** |datetime|
    | **Timestamp:** |timestamp|

.. tip::

    To make these macros (substitution definitions) accessible
    documentation wide:

    .. code-block:: python

        # conf.py
        rst_epilog = """
        .. |date| date:: %Y/%m/%d
        .. |time| date:: %H:%M:%S
        .. |datetime| date:: %Y/%m/%d, %H:%M
        .. |timestamp| date:: %Y%m%d%H%M%S
        """

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Directives ➤ Date and time <https://docutils.sourceforge.io/docs/ref/rst/directives.html#date>`_
