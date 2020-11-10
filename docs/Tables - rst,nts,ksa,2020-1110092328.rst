################################################################################
RST ➤ Tables
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Supported tables are: grid tables, simple tables.

**********************************************************************
Examples
**********************************************************************

Grid tables
============================================================

In
    ::

        +------------------------+------------+----------+----------+
        | Header row, column 1   | Header 2   | Header 3 | Header 4 |
        | (header rows optional) |            |          |          |
        +========================+============+==========+==========+
        | body row 1, column 1   | column 2   | column 3 | column 4 |
        +------------------------+------------+----------+----------+
        | body row 2             | Cells may span columns.          |
        +------------------------+------------+---------------------+
        | body row 3             | Cells may  | - Table cells       |
        +------------------------+ span rows. | - contain           |
        | body row 4             |            | - body elements.    |
        +------------------------+------------+---------------------+

Out

    +------------------------+------------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 |
    | (header rows optional) |            |          |          |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | Cells may span columns.          |
    +------------------------+------------+---------------------+
    | body row 3             | Cells may  | - Table cells       |
    +------------------------+ span rows. | - contain           |
    | body row 4             |            | - body elements.    |
    +------------------------+------------+---------------------+

Simple tables
============================================================

In
    ::

        =====  =====  =======
        A      B       A and B
        =====  =====  =======
        False  False  False
        True   False  False
        False  True   False
        True   True   True
        =====  =====  =======

        =====  =====  ======
        Inputs        Output
        ------------  ------
        A      B      A or B
        =====  =====  ======
        False  False  False
        True   False  True
        False  True   True
        True   True   True
        =====  =====  ======

Out

    =====  =====  =======
    A      B      A and B
    =====  =====  =======
    False  False  False
    True   False  False
    False  True   False
    True   True   True
    =====  =====  =======

    =====  =====  ======
    Inputs        Output
    ------------  ------
    A      B      A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

List tables
============================================================

In
    ::

        .. list-table:: Frozen Delights!
            :widths: 15 10 30
            :header-rows: 1

           * - Treat
               - Quantity
               - Description
           * - Albatross
               - 2.99
               - On a stick!
           * - Crunchy Frog
               - 1.49
               - If we took the bones out, it wouldn't be
               crunchy, now would it?
           * - Gannet Ripple
               - 1.99
               - On a stick!

Out

    .. list-table:: Frozen Delights!

       * - Treat
           - Quantity
           - Description
       * - Albatross
           - 2.99
           - On a stick!
       * - Crunchy Frog
           - 1.49
           - If we took the bones out, it wouldn't be
           crunchy, now would it?
       * - Gannet Ripple
           - 1.99
           - On a stick!

CSV tables
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

- `Docutils ➤ Spec. ➤ Tables <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#tables>`_
- `Docutils ➤ Spec. ➤ Grid Tables <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#grid-tables>`_
- `Docutils ➤ Spec. ➤ Simple Tables <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#simple-tables>`_
