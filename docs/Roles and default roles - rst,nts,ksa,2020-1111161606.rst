################################################################################
RST ➤ Roles and default roles
################################################################################

**********************************************************************
Synopsis
**********************************************************************

*Roles*, in the RST sense, can be understood as namespaces for hyperlink
targets. The role directives, written as such::

    :role-name:`target`
    :role-name:`text <target>`

have for effect of searching for the specified ``target`` in the role's namespace and render a hyperlink to it.

``role-name`` is an arbitrary name, typically one that describes the type of the hyperlink target, i.e a hyperlink target that points to, a certain type of thing, e.g. documents, figures, python objects -- i.e describes the "role" of the hyperlink target -- calling a role has for effect to search in the namespace for the specified target and render a link to it.

For example here's a few standard roles:

- ``:any:``
    All targets within the documentation.

    .. tip:: This is a good candiate to set for the ``default-role``.

- ``:ref:``
    All `internal and implicit hyperlink targets <Hyperlink targets - rst,nts,ksa,2020-1110115624>`.

Also you can create (register with the parser) custom interpreted text roles
with the ``role`` directive::

    .. role:: <role-name>
        :class: str        <--- set "classes" attribute

Additionally, you can set the behavior of the default interpreted text role
with the ``default-role`` directive; i.e you can specify the behavior
of applying two backticks to some text, e.g. ```text```.

.. note:: The default role (`text`) has no special meaning by default. You
   are free to use it for anything you like, e.g. variable names; use the
   default_role config value to set it to a known role - the any role to find
   anything

See :mailheader:`Content-type`. Do :kbd:`C-x C-f` and :kbd:`Control-x Control-f`.

See :file:`index.rst` and :file:`Admonitions - rst,nts,ksa,2020-1110205728`.

Perform the :command:`ls` and then :command:`echo`.

Make sure you type :command:`ls` properly and make things

**********************************************************************
Examples
**********************************************************************

``role`` directive
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

Extending existing roles
============================================================

In

        .. role:: custom(emphasis)

        :custom:`text`

Out

    The parsed result is as follows:

    .. code-block:: html

        <paragraph>
            <emphasis classes="custom">
                text

Custom class name
============================================================

In
    ::

        .. role:: custom
            :class: special

        :custom:`interpreted text`

Out

    .. code-block:: html

        <paragraph>
            <inline classes="special">
                interpreted text 2

``default-role`` directive
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

- If you prefix the content (in ``:role:`content```) with ``!``, no reference hyperlink will be created.

- If you prefix the content with ``~``, the link text will only be the last component of the target. For example, ``:py:meth:`~Queue.Queue.get``` will refer to ``Queue.Queue.get`` but only display ``get`` as the link text. This does not work with all cross-reference roles, but is domain specific.

- In HTML output, the link's (defualt) ``title`` attribute, if not explicitly specified, will always be the full target name.

- The ``default-role`` directive may be used without an argument to restore
  the initial default interpreted text role, which is application-dependent.
  The initial default interpreted text role of the standard reStructuredText
  parser is ``title-reference``.

- Set ``default-role`` documentation wide:

    .. code-block:: python

        # conf.py
        rst_prolog = """
        .. default-role:: any
        """

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Directives ➤ Roles <https://docutils.sourceforge.io/docs/ref/rst/directives.html#custom-interpreted-text-roles>`_
- `Sphinx ➤ Domains # Python Roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#cross-referencing-python-objects>`_
- `Sphinx ➤ Domains # C Roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#cross-referencing-c-constructs>`_
- `Sphinx ➤ Domains # C++ Roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#cross-referencing>`_
- `Sphinx ➤ Domains # Javascript Roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#js-roles>`_
