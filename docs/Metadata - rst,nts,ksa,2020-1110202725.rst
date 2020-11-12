################################################################################
RST ➤ Metadata directives
################################################################################

**********************************************************************
Synopsis
**********************************************************************

- HTML metadata is supported with the ``meta`` directive.

- The ``title`` directive specifies the meta title of the document, it overrides a document-supplied title::

- Specify the authors of a section with the ``.. sectionauthor:: name <email>`` directive.

- Specify the authors of code with the ``.. codeauthor:: name <email>`` directive.

.. note:: To display authors:

    .. code-block:: python

        # conf.py
        show_authors = True

**********************************************************************
Examples
**********************************************************************

``meta`` directive
============================================================

In
    ::

        .. meta::
            :description: The Sphinx documentation builder
            :keywords: Sphinx, documentation, builder
        .. title:: Sphinx

Out

    Will generate in the HTML output:

    .. code-block:: html

        <meta name="description" content="The Sphinx documentation builder">
        <meta name="keywords" content="Sphinx, documentation, builder">
        <meta name="title" content="Sphinx">  # unsure of this last one

Authorship directives
============================================================

In
    ::

        Section example
        ============================================================

        .. sectionauthor:: Guido van Rossum <guido@python.org>
        .. sectionauthor:: James Rossum <james@python.org>

        .. code-block:: html

            code

        .. codeauthor:: Guido van Rossum <guido@python.org>
        .. codeauthor:: James Rossum <james@python.org>

Out

Section example
============================================================

.. sectionauthor:: Guido van Rossum <guido@python.org>
.. sectionauthor:: James Rossum <james@python.org>

.. code-block:: html

    code

.. codeauthor:: Guido van Rossum <guido@python.org>
.. codeauthor:: James Rossum <james@python.org>

**********************************************************************
References
**********************************************************************

- `Sphinx ➤ RST ➤ Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#html-metadata>`_
- `Sphinx ➤ Directives ➤ Meta-information markup <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#meta-information-markup>`_
