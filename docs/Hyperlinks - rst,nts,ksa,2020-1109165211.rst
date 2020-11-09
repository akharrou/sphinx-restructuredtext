********************************************************************************
RST ➤ Hyperlinks
********************************************************************************


Synopsis
================================================================================

You can link local files as well as remote files (webpages).

.. note::

    Sphinx configuration:

    .. code-block:: python

        # conf.py
        extensions.append('sphinx.ext.autosectionlabel')
        autosectionlabel_prefix_document = True
        autosectionlabel_maxdepth = 3


Examples
********************************************************************************

Download links
---------------------------------------

In

.. code-block:: rst

    Download the configuration file :download:`here <../conf.py>` !

.. code-block:: rst

    .. only:: builder_html

        Download the configuration file :download:`here <../conf.py>` !

Out

Download the configuration file :download:`here <../conf.py>` !

.. only:: builder_html

    Download the configuration file :download:`here <../conf.py>` !


.. _crsref-arb-loc:

Arbitrary locations
---------------------------------------

In

.. code-block:: rst

    .. _label-title:

    Title
    -------

.. code-block:: rst

    Cross-reference to the label with :ref:`my-reference-label`.

Out

Here's a cross-reference to this sub-section: :ref:`crsref-arb-loc`.


Internal links
---------------------------------------

Reference documents
###################

In

.. code-block:: rst

  See :doc:`specimen` !

Out

See :doc:`specimen` !

Reference sections
###################

In

.. code-block:: rst

  See :ref:`specimen:Blockquotes`

Out

See :ref:`specimen:Blockquotes`


External links
---------------------------------------

In

.. code-block:: rst

  Checkout `Sphinx here ! <https://www.sphinx-doc.org>`_

Out

Checkout Sphinx `here ! <https://www.sphinx-doc.org>`_


References
================================================================================

- `Sphinx ➤ RST ➤ Basics # Hyperlinks <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks>`_
- `Sphinx ➤ RST ➤ Roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`_
- `Sphinx ➤ Extensions ➤ sphinx.ext.autosectionlabel <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`_
