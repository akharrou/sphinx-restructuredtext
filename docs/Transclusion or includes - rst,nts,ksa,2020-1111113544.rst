################################################################################
RST ➤ Transclusion or includes
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Two directives exist for the task:

- Docutils' ``include`` directive, the output can optionally be literal, i.e code:

    ::

        .. include:: <path>
            :start-line: integer     <--- includes from line
            :end-line: integer       <--- includes up to line
            :end-before: str         <--- includes up to first occurrence of

            :literal:                <--- includes as literal block (code)
            :code: str               <--- (code) language (optional)
            :number-lines: integer   <--- counter start, default is 1

            :encoding: str           <--- name of text encoding, default is 'input_encoding'
            :tab-width: integer      <--- tab spaces, neg. value rep. hard tabs, default 'tab_width'

    .. warning:: The ``include`` directive represents a potential security
       hole. It can be disabled with the ``file_insertion_enabled`` runtime
       setting.

- Sphinx's custom ``literalinclude`` directive, the output is always literal, i.e code::

    .. literalinclude:: <path>
        :name: str                   <--- implicit target name
        :caption: str                <--- optional, leave empty for filename
        :language: str

        :lines: int list             <--- lines to include from file

        :start-after: str            <---  only lines that follow the first line containing that string are included
        :start-at: str               <--- same, but lines containing the match string are included
        :end-before: str             <--- only lines that precede the first lines containing that string are included
        :end-at: str                 <--- same, but lines containing the match string are included

        :prepend: str                <--- prepend line to output
        :append: str                 <--- append line to output

        :lineno-start: int           <--- starting line number
        :linenos:                    <--- turn on line numbering
        :emphasize-lines: int list   <--- lines to highlight

        :dedent:                     <--- strip indentation characters
        :tab-width: int              <--- spaces used in tab
        :encoding: str               <--- file character encoding

        :pyobject:                   <--- for python modules, you can select class/function/method to include

        :diff: <path>                <--- shows differences between this file

**********************************************************************
Examples
**********************************************************************

Basic ``include``
============================================================

In
    ::

        This first example will be parsed at the document level, and can
        thus contain any construct, including section headers.

        .. include:: ../Makefile
            :literal:
            :code: makefile
            :start-line: 5
            :end-line: 14

        Back in the main document.

            This second example will be parsed in a block quote context.
            Therefore it may only contain body elements.  It may not
            contain section headers.

            .. include:: ../Makefile
                :literal:
                :code: makefile
                :start-line: 5
                :end-line: 14

Out

    This first example will be parsed at the document level, and can
    thus contain any construct, including section headers.

    .. include:: ../Makefile
        :literal:
        :code: makefile
        :start-line: 5
        :end-line: 14

    Back in the main document.

        This second example will be parsed in a block quote context.
        Therefore it may only contain body elements.  It may not
        contain section headers.

        .. include:: ../Makefile
            :literal:
            :code: makefile
            :start-line: 5
            :end-line: 14

Basic ``literalinclude``
============================================================

In

    .. code-block:: make

        .. literalinclude:: ../Makefile
            :name: include_makefile
            :caption: Sphinx Makefile
            :language: make
            :lines: 6-10,13,14,17-
            :linenos:
            :lineno-start: 1
            :emphasize-lines: 13,14,17-18
            :tab-width: 4
Out

    .. literalinclude:: ../Makefile
        :name: include_makefile
        :caption: Sphinx Makefile
        :language: make
        :lines: 6-10,13,14,17-
        :linenos:
        :lineno-start: 1
        :emphasize-lines: 13,14,17-18
        :tab-width: 4

Diff w/ ``literalinclude``
============================================================

In

    ::

        .. literalinclude:: _assets/example_diff_new.txt
            :name: include_example_diff
            :caption: Example ``diff``
            :diff: _assets/example_diff_original.txt

        See :ref:`the compilation makefile <include_makefile>`
        as well as the :ref:`example diff <include_example_diff>`.

Out

    .. literalinclude:: _assets/example_diff_new.txt
        :name: include_example_diff
        :caption: Example ``diff``
        :diff: _assets/example_diff_original.txt

    See :ref:`the compilation makefile <include_makefile>` as well as the :ref:`example diff <include_example_diff>`.

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Directives ➤ Including an external document fragment <https://docutils.sourceforge.io/docs/ref/rst/directives.html#including-an-external-document-fragment>`_
