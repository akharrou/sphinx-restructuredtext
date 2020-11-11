################################################################################
RST ➤ Topic and rubric directives
################################################################################

**********************************************************************
Synopsis
**********************************************************************

You can create content blocks with emboldened titles with the ``topic``
directive, for indented content blocks, and the ``rubric`` directive for
non-indented content blocks.

**********************************************************************
Examples
**********************************************************************

Topic and rubric directives
============================================================

In
    ::

        .. rubric:: John Doe in flesh

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Quisque id diam vel
        quam elementum pulvinar.

        .. topic:: Topic Title

            Subsequent indented lines comprise
            the body of the topic, and are
            interpreted as body elements.

Out

    .. rubric:: John Doe in flesh

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Quisque id diam vel
    quam elementum pulvinar.

.. topic:: Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Spec. ➤ Rubric <https://docutils.sourceforge.io/docs/ref/rst/directives.html#rubric>`_
- `Docutils ➤ Spec. ➤ Topic <https://docutils.sourceforge.io/docs/ref/rst/directives.html#topic>`_
