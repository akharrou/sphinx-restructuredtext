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

**********************************************************************
References
**********************************************************************

- `Docutils ➤ RST ➤ Tables <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#tables>`_
- `Docutils ➤ RST ➤ Grid Tables <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#grid-tables>`_
- `Docutils ➤ RST ➤ Simple Tables <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#simple-tables>`_
