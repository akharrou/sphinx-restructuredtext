################################################################################
RST ➤ Footnotes
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Footnotes are supported with the ``[#label]_``, ``.. [#label] def`` syntax.

Footnote labels can be:

- decimal number
- ``#`` (:ref:`Footnotes - rst,nts,ksa,2020-1110104849:Auto-numbered footnotes`)
- ``#label`` (:ref:`Footnotes - rst,nts,ksa,2020-1110104849:Autonumber label`)
- ``*`` (:ref:`Footnotes - rst,nts,ksa,2020-1110104849:Auto-symbol footnotes`).

**********************************************************************
Examples
**********************************************************************

Auto-numbered footnotes
============================================================

In
    ::

        [#]_ is a reference to footnote 1, and [#]_ is a reference to
        footnote 2.

        .. [#] This is footnote 1.
        .. [#] This is footnote 2.
        .. [#] This is footnote 3.

        [#]_ is a reference to footnote 3.

Out

    [#]_ is a reference to footnote 1, and [#]_ is a reference to
    footnote 2.

    .. [#] This is footnote 1.
    .. [#] This is footnote 2.
    .. [#] This is footnote 3.

    [#]_ is a reference to footnote 3.

Autonumber label
============================================================

In
    ::

        If ``[#note]_`` is the fourth footnote reference, it will show up as:
        [#note]_, [4].  We can refer to it again as ``[#note]_`` and again see:
        [#note]_, [4].  We can also refer to it as ``note_`` (an ordinary internal hyperlink reference), it shows up as: note_.

        .. [#note] This is the footnote labeled "note".

Out

    If ``[#note]_`` is the fourth footnote reference, it will show up as:
    [#note]_, [4].  We can refer to it again as ``[#note]_`` and again see:
    [#note]_, [4].  We can also refer to it as ``note_`` (an ordinary internal hyperlink reference), it shows up as: note_.

    .. [#note] This is the footnote labeled "note".

Auto-symbol footnotes
============================================================

In
    ::

        Here is a symbolic footnote reference: [*]_.
        And here's another one: [*]_.
        And another: [*]_.

        .. [*] This is the footnote.
        .. [*] This is the footnote.
        .. [*] This is the footnote.

Out

    Here is a symbolic footnote reference: [*]_.
    And here's another one: [*]_.
    And another: [*]_.

    .. [*] This is the footnote.
    .. [*] This is the footnote.
    .. [*] This is the footnote.

**********************************************************************
References
**********************************************************************

- `Docutils ➤ RST ➤ Footnotes <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#footnotes>`_
