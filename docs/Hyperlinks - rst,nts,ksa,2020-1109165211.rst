################################################################################
RST ➤ Hyperlinks
################################################################################


**********************************************************************
Synopsis
**********************************************************************

You can link local files as well as remote files (webpages).

.. note::

    Sphinx Configurations:

    .. code-block:: python

        # conf.py
        extensions.append('sphinx.ext.autosectionlabel')
        autosectionlabel_prefix_document = True
        autosectionlabel_maxdepth = 3


**********************************************************************
Examples
**********************************************************************

Download links
============================================================


In

    ::

        Download the configuration file :download:`here <../conf.py>` !

    ::

        .. only:: builder_html

            Download the configuration file :download:`here <../conf.py>` !

Out

    Download the configuration file :download:`here <../conf.py>` !

    .. only:: builder_html

        Download the configuration file :download:`here <../conf.py>` !

.. _crsref-arb-loc:

Arbitrary locations
============================================================


In

    ::

        .. _label-title:

        Title
        -------

    ::

        Cross-reference to the label with :ref:`my-reference-label`.

Out

    Here's a cross-reference to this sub-section: :ref:`crsref-arb-loc`.

Internal links
============================================================


Reference documents
--------------------------------------------------


In

    ::

        See :doc:`Footnotes <Footnotes - rst,nts,ksa,2020-1110104849>`

Out

    See :doc:`Footnotes <Footnotes - rst,nts,ksa,2020-1110104849>` !

Reference sections
--------------------------------------------------


In

    ::

        See :ref:`specimen:Blockquotes`

Out

    See :ref:`specimen:Blockquotes`


External links
============================================================


In

    ::

        Checkout `Sphinx here ! <https://www.sphinx-doc.org>`_

Out

    Checkout Sphinx `here ! <https://www.sphinx-doc.org>`_


**********************************************************************
References
**********************************************************************

- `Sphinx ➤ RST ➤ Basics # Hyperlinks <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks>`_
- `Sphinx ➤ RST ➤ Roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`_
- `Sphinx ➤ Extensions ➤ sphinx.ext.autosectionlabel <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`_
