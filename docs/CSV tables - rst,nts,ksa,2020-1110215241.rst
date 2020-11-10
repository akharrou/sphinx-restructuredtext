################################################################################
RST ➤ CSV tables
################################################################################

**********************************************************************
Synopsis
**********************************************************************

CSV tables are supported and can be directly pasted into your file
under the ``.. csv-table:: <title>`` directive.

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        .. csv-table:: Frozen Delights!
            :header: "Treat", "Quantity", "Description"
            :widths: 15, 10, 30

            "Albatross", 2.99, "On a stick!"
            "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
            crunchy, now would it?"
            "Gannet Ripple", 1.99, "On a stick!"

Out

    .. csv-table:: Frozen Delights!
        :header: "Treat", "Quantity", "Description"
        :widths: 15, 10, 30

        "Albatross", 2.99, "On a stick!"
        "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
        crunchy, now would it?"
        "Gannet Ripple", 1.99, "On a stick!"

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Directives ➤ CSV Table <https://docutils.sourceforge.io/docs/ref/rst/directives.html#csv-table>`_
