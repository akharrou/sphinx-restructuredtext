################################################################################
RST ➤ Code listings
################################################################################

**********************************************************************
Synopsis
**********************************************************************

You can write inline ``code`` as well as::

    codeblocks

you can even directly paste in Python interactive sessions (doctests):

>>> 1 + 1
2

- Project wide highlighting configured with: ``highlight_language = 'language'``, in your ``conf.py``.
- Document wide highlighting configured with: ``.. highlight:: language``, at top of document.
- Block-by-block highlighting configured with: ``.. codeblock:: language``, per block.

**********************************************************************
Examples
**********************************************************************

Inline
============================================================

In
    ::

        This is ``code`` that is inlined

Out

    This is ``code`` that is inlined

Literal blocks
============================================================

In
    ::

        Expanded form:

            Paragraph:

            ::

                Literal block

        Partially minimized form:

            Paragraph: ::

                Literal block

        Fully minimized form:

            Paragraph::

                Literal block

Out

    Expanded form:

        ::

            Literal block

    Partially minimized form: ::

        Literal block

    Fully minimized form::

        Literal block

Codeblock directive
============================================================

In
    ::

        .. code-block:: none

            $ tree vendor/composer
            ├── ClassLoader.php
            ├── LICENSE
            ├── autoload_classmap.php
            ├── ...
            └── installed.json

Out

    .. code-block:: none

            $ tree vendor/composer
            ├── ClassLoader.php
            ├── LICENSE
            ├── autoload_classmap.php
            ├── ...
            └── installed.json

Emphasized, numbered lines
============================================================

In

    ::

        .. code-block:: javascript
            :emphasize-lines: 1,5,8

        var _extends = function(target) {
            for (var i = 1; i < arguments.length; i++) {
            var source = arguments[i];
            for (var key in source) {
                target[key] = source[key];
            }
            }
            return target;
        };

Out

    .. code-block:: javascript
        :emphasize-lines: 1,5,8
        :linenos:

        var _extends = function(target) {
            for (var i = 1; i < arguments.length; i++) {
            var source = arguments[i];
            for (var key in source) {
                target[key] = source[key];
            }
            }
            return target;
        };

Doctest blocks
============================================================

In
    ::

        >>> 1 + 1
        2

Out

    >>> 1 + 1
    2

**********************************************************************
References
**********************************************************************

- `Sphinx ➤ RST ➤ Basics # Inline markup <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#inline-markup>`_
- `Sphinx ➤ RST ➤ Basics # Literal blocks <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#literal-blocks>`_
- `Docutils ➤ Spec. ➤ Literal blocks <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#literal-blocks>`_
- `Write the docs ➤ RST ➤ Code samples <https://www.writethedocs.org/guide/writing/reStructuredText/#code-samples>`_

.. .. testcode::

..     print('hi')

.. .. testoutput::

..     hi there !
