################################################################################
RST ➤ Hyperlink targets
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Hyperlink targets are markers in your document that identify a location, within or outside of the document, which may be linked to by hyperlink references. You can create them with the ``.. _marker-name: location`` syntax.

**********************************************************************
Examples
**********************************************************************

Internal targets
============================================================

In
    ::

        Hyperlink targets always point to the element right below them,
        in this case the paragraph_ that's right below them.

        .. _paragraph:
        .. _target:

        The hyperlink target above points to this paragraph.
        The targets "paragraph" and "target" are synonyms; they both
        point to this paragraph.

Out

    Hyperlink targets always point to the element right below them,
    in this case the paragraph_ that's right below them.

    .. _paragraph:
    .. _target:

    The hyperlink target above points to this paragraph.
    The targets "paragraph" and "target" are synonyms; they both
    point to this paragraph.

External targets
============================================================

In
    ::

        See the Python_ home page for info.
        `Write to me`_ with your questions.
        Also join the `Python DOC-SIG mailing list archive`_ if you want.

        .. _Python: http://www.python.org
        .. _Write to me:
            fake@email.com

        .. _Python DOC-SIG mailing list archive:
        .. _archive:
        .. _Doc-SIG: http://
            mail.python.org/pipermail/doc-sig/

Out

    | See the Python_ home page for info.
    | `Write to me`_ with your questions.
    | Also join the `Python DOC-SIG mailing list archive`_ if you want.

    .. _Python: http://www.python.org
    .. _Write to me:
        fake@email.com

    .. _Python DOC-SIG mailing list archive:
    .. _archive:
    .. _Doc-SIG: http://
        mail.python.org/pipermail/doc-sig/

    .. note::   The targets directly above ``Doc-SIG`` inherit the end location.
                Also we call these chained targets.

Indirect targets
============================================================

In
    ::

        .. _one: two_
        .. _two: three_
        .. _three:

Out

    - ``_one`` points to ``_two``
    - ``_two`` points to ``_three``
    - therefore ``_one`` in fact points to ``_three``

    | Try: one_ !
    | Try: two_ !
    | Try: three_ !

    .. _one: two_
    .. _two: three_
    .. _three:

    This paragraph is your final destination, whether you picked
    ``one``, ``two``, ``three``.

**********************************************************************
Remarks
**********************************************************************

- Whitespaces, in for example file names, must be escaped ``\␣``::

    .. _reference: ../local\ path\ with\ spaces.html

- Colons must be escaped ``\:``::

    .. _Chapter One\: "Tadpole Days":
    It's not easy being green...

- Underscores as last character of a location name must be escaped ``\_``::

    This link_ refers to a file called ``underscore_``.

    .. _link: underscore\_

**********************************************************************
References
**********************************************************************

- `Docutils ➤ RST ➤ Hyperlink targets <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#hyperlink-targets>`_
