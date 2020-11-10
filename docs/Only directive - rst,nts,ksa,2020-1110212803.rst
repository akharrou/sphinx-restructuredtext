################################################################################
RST ➤ Only directive
################################################################################

**********************************************************************
Synopsis
**********************************************************************

You can make the inclusion of certain content conditional, on e.g. the
builder that Sphinx uses (e.g. html, latex). The directive to do so is
``.. only:: <condition>``.

**********************************************************************
Examples
**********************************************************************

Builder
============================================================

In
    ::

        .. only:: builder_html

            Download the :download:`Makefle <../Makefile>`.

Out

    .. only:: builder_html

        Download the :download:`Makefle <../Makefile>`.

**********************************************************************
References
**********************************************************************

- `Sphinx ➤ Directives ➤ Including content based on tags <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#including-content-based-on-tags>`_
