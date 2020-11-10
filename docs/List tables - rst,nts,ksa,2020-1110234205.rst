################################################################################
RST ➤ List tables
################################################################################

**********************************************************************
Synopsis
**********************************************************************

You can create tables out of a list with the ``.. list-table:: <title>``
directive.

**********************************************************************
Examples
**********************************************************************

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

.. warning:: indentation must be exact, else the table won't render.

**********************************************************************
References
**********************************************************************

- `Docutisl ➤ Directives ➤ List tables <https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table>`_
