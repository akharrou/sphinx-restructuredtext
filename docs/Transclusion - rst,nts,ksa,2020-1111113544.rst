################################################################################
RST ➤ Transclusion
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Two directives exist for the task:

- Docutils' ``include`` directive

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

    .. warning:: The "``include``" directive represents a potential security
       hole. It can be disabled with the "``file_insertion_enabled``" runtime
       setting.


- Sphinx's custom ``literalinclude`` directive.



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

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Directives ➤ Including an external document fragment <https://docutils.sourceforge.io/docs/ref/rst/directives.html#including-an-external-document-fragment>`_
