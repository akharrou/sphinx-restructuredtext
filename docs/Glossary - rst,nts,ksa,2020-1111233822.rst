################################################################################
RST ➤ Glossary
################################################################################

**********************************************************************
Synopsis
**********************************************************************

With Sphinx making glossaries is supported with its custom ``glossary``
directive and cross-referenced with its ``term`` role.

**********************************************************************
Examples
**********************************************************************

Create glossary
============================================================

In
    ::

        .. glossary::
            :sorted:

            term : key
                definition

            term 1 : key 1
            term 2 : key 2
                definition of both

Out

    See the :doc:`glossary <glossary>` of this documentation.

Reference glossary terms
============================================================

In
    ::

        :term:`Terminals <> terminal>` are the best.

Out

    :term:`Terminals <> terminal>` are the best.

**********************************************************************
References
**********************************************************************

- `Sphinx ➤ Directives ➤ Glossary <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#glossary>`_
- `Sphinx ➤ Roles ➤ Term <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-term>`_
