################################################################################
RST ➤ Metadata
################################################################################

**********************************************************************
Synopsis
**********************************************************************

HTML metadata is supported with the ``meta`` directive.

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        .. meta::
            :description: The Sphinx documentation builder
            :keywords: Sphinx, documentation, builder

Out

    Will generate in the HTML output:

    .. code-block:: html

        <meta name="description" content="The Sphinx documentation builder">
        <meta name="keywords" content="Sphinx, documentation, builder">

**********************************************************************
References
**********************************************************************

- `Sphinx ➤ RST ➤ Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#html-metadata>`_
