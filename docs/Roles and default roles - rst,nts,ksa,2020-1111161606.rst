################################################################################
RST ➤ Roles and default roles
################################################################################

**********************************************************************
Synopsis
**********************************************************************

You can create  (register with the parser) custom interpreted text roles
with the ``role`` directive::

    .. role:: <role-name>
        :class: str        <--- set "classes" attribute

Also, you can set the behavior of the default interpreted text role
with the ``default-role`` directive; i.e you can specify the behavior
of applying two backticks to some text, e.g. ```text```.

**********************************************************************
Examples
**********************************************************************

Basic ``role``
============================================================

In
    ::

        .. role:: custom

    After declaration, the document may use the new ``custom`` role:

    ::

        An example of using :custom:`interpreted text`

Out

    This will be parsed into the following document tree fragment:

    .. code-block:: html

        <paragraph>
            An example of using
            <inline classes="custom">
                interpreted text

Customizations
============================================================

In
    ::

        .. role:: custom
            :class: special

        .. role:: custom(emphasis)

        :custom:`interpreted text 1`

        :custom:`interpreted text 2`

Out

    .. code-block:: html

        <paragraph>
            <emphasis classes="custom">
                interpreted text 1

        <paragraph>
            <inline classes="special">
                interpreted text 2

Basic ``default-role``
============================================================

In
    ::

        .. default-role:: subscript

    any subsequent use of implicit-role interpreted text in the document
    will use the ``subscript`` role:

    ::

        An example of a `default` role.

Out

    This will be parsed into the following document tree fragment:

    .. code-block:: html

        <paragraph>
            An example of a
            <subscript>
                default
            role.

**********************************************************************
Details
**********************************************************************

- The ``default-role`` directive may be used without an argument to restore
  the initial default interpreted text role, which is application-dependent.
  The initial default interpreted text role of the standard reStructuredText
  parser is ``title-reference``.

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Directives ➤ Roles <https://docutils.sourceforge.io/docs/ref/rst/directives.html#custom-interpreted-text-roles>`_
