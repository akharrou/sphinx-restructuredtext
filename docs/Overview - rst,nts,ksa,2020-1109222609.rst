################################################################################
RST ➤ Overview
################################################################################

.. A reStructuredText document is made up of body or block-level elements, and may be structured into sections. Sections are indicated through title style (underlines & optional overlines). Sections contain body elements and/or subsections. Some body elements contain further elements, such as lists containing list items, which in turn may contain paragraphs and other body elements. Others, such as paragraphs, contain text and inline markup elements.

.. Here are examples of body elements:

.. Paragraphs (and inline markup):

.. Paragraphs contain text and may contain inline markup:
.. *emphasis*, **strong emphasis**, `interpreted text`, ``inline
.. literals``, standalone hyperlinks (http://www.python.org),
.. external hyperlinks (Python_), internal cross-references
.. (example_), footnote references ([1]_), citation references
.. ([CIT2002]_), substitution references (|example|), and _`inline
.. internal targets`.

.. Paragraphs are separated by blank lines and are left-aligned.
.. Five types of lists:

.. Bullet lists:

.. - This is a bullet list.

.. - Bullets can be "*", "+", or "-".
.. Enumerated lists:

.. 1. This is an enumerated list.

.. 2. Enumerators may be arabic numbers, letters, or roman
..    numerals.
.. Definition lists:

.. what
..     Definition lists associate a term with a definition.

.. how
..     The term is a one-line phrase, and the definition is one
..     or more paragraphs or body elements, indented relative to
..     the term.
.. Field lists:

.. :what: Field lists map field names to field bodies, like
..        database records.  They are often part of an extension
..        syntax.

.. :how: The field marker is a colon, the field name, and a
..       colon.

..       The field body may contain one or more body elements,
..       indented relative to the field marker.
.. Option lists, for listing command-line options:

.. -a            command-line option "a"
.. -b file       options can have arguments
..               and long descriptions
.. --long        options can be long also
.. --input=file  long options can also have
..               arguments
.. /V            DOS/VMS-style options too
.. There must be at least two spaces between the option and the description.

.. Literal blocks:

.. Literal blocks are either indented or line-prefix-quoted blocks,
.. and indicated with a double-colon ("::") at the end of the
.. preceding paragraph (right here -->)::

..     if literal_block:
..         text = 'is left as-is'
..         spaces_and_linebreaks = 'are preserved'
..         markup_processing = None
.. Block quotes:

.. Block quotes consist of indented body elements:

..     This theory, that is mine, is mine.

..     -- Anne Elk (Miss)
.. Doctest blocks:

.. >>> print 'Python-specific usage examples; begun with ">>>"'
.. Python-specific usage examples; begun with ">>>"
.. >>> print '(cut and pasted from interactive Python sessions)'
.. (cut and pasted from interactive Python sessions)
.. Two syntaxes for tables:

.. Grid tables; complete, but complex and verbose:

.. +------------------------+------------+----------+
.. | Header row, column 1   | Header 2   | Header 3 |
.. +========================+============+==========+
.. | body row 1, column 1   | column 2   | column 3 |
.. +------------------------+------------+----------+
.. | body row 2             | Cells may span        |
.. +------------------------+-----------------------+
.. Simple tables; easy and compact, but limited:

.. ====================  ==========  ==========
.. Header row, column 1  Header 2    Header 3
.. ====================  ==========  ==========
.. body row 1, column 1  column 2    column 3
.. body row 2            Cells may span columns
.. ====================  ======================
.. Explicit markup blocks all begin with an explicit block marker, two periods and a space:

.. Footnotes:

.. .. [1] A footnote contains body elements, consistently
..    indented by at least 3 spaces.
.. Citations:

.. .. [CIT2002] Just like a footnote, except the label is
..    textual.
.. Hyperlink targets:

.. .. _Python: http://www.python.org

.. .. _example:

.. The "_example" target above points to this paragraph.
.. Directives:

.. .. image:: mylogo.png
.. Substitution definitions:

.. .. |symbol here| image:: symbol.png
.. Comments:

.. .. Comments begin with two dots and a space.  Anything may
..    follow, except for the syntax of footnotes/citations,
..    hyperlink targets, directives, or substitution definitions.

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Spec. ➤ Quick syntax <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#quick-syntax-overview>`_
