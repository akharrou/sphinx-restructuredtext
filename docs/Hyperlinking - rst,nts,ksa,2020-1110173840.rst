################################################################################
RST ➤ Hyperlinking
################################################################################

**********************************************************************
Synopsis
**********************************************************************

You can hyperlink to all kinds of things: webpages, local documents (files), sections, particular paragraphs, images, and any content.

There's a couple dozen ways of hyperlinking, here are a few:

- `standalone hyperlinks`_
- `embedded URI, aliases`_
- `document hyperlinks`_
- `section hyperlinks`_
- `download hyperlinks`_
- `abritrary hyperlinks (references to targets)`_

... and there are way more ! See `Sphinx ➤ RST ➤ Roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`_.

**********************************************************************
Examples
**********************************************************************

Standalone hyperlinks
============================================================

In
    ::

        http://www.python.org

        ftp://ftp.python.org/pub/python

        mailto:someone@somewhere.com

        news:comp.lang.python

Out

    http://www.python.org

    ftp://ftp.python.org/pub/python

    mailto:someone@somewhere.com

    news:comp.lang.python

Embedded URI, Aliases
============================================================

In
    ::

        See the `Python home page <http://www.python.org>`_ for info.
        This `link <Python home page_>`_ is an alias to the link above.

        Equivalent to:

        See the `Python home page`_ for info.
        This link_ is an alias to the link above.

            .. _Python home page: http://www.python.org
            .. _link: `Python home page`_

Out

    | See the `Python home page <http://www.python.org>`_ for info.
    | This `link <Python home page_>`_ is an alias to the link above.

    Equivalent to:

    | See the `Python home page`_ for info.
    | This link_ is an alias to the link above.

        .. _Python home page: http://www.python.org
        .. _link: `Python home page`_

Abritrary location hyperlinks
============================================================

In
    ::

        .. _explanation:

        Lorem ipsum...

        See explanation_.

Out

    .. _explanation:

    Paragraph. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
    eiusmod tempor incididunt ut labore et dolore magna aliqua. Quisque id
    diam vel quam elementum pulvinar. Orci nulla pellentesque dignissim
    enim. Magna fringilla urna porttitor rhoncus dolor purus. Mollis nunc
    sed id semper risus in hendrerit gravida rutrum. Faucibus turpis in eu
    mi bibendum. Ultrices neque ornare aenean euismod elementum.
    Consectetur lorem donec massa sapien faucibus. At imperdiet dui
    accumsan sit amet nulla facilisi morbi tempus. Rhoncus urna neque
    viverra justo nec ultrices dui. Sed faucibus turpis in eu mi bibendum.

    See explanation_.

Document hyperlinks
============================================================

In

    ::

        See :doc:`Footnotes - rst,nts,ksa,2020-1110104849`
        and :doc:`citations <Citations - rst,nts,ksa,2020-1110112449>`

Out

    See :doc:`Footnotes - rst,nts,ksa,2020-1110104849`
    and :doc:`citations <Citations - rst,nts,ksa,2020-1110112449>` !

Section hyperlinks
============================================================

.. note::

    Sphinx Configurations:

    Allows you to refer to sections with their title.

    .. code-block:: python

        # conf.py
        extensions.append('sphinx.ext.autosectionlabel')  # sphinx built-in extension
        autosectionlabel_prefix_document = True
        autosectionlabel_maxdepth = 3

In

    ::

        See :ref:`Footnotes - rst,nts,ksa,2020-1110104849:Autonumber label`
        and :ref:`auto-symbols <Footnotes - rst,nts,ksa,2020-1110104849:Auto-symbol footnotes>`.

Out

    See :ref:`Footnotes - rst,nts,ksa,2020-1110104849:Autonumber label`
    and :ref:`auto-symbols <Footnotes - rst,nts,ksa,2020-1110104849:Auto-symbol footnotes>`.

Download hyperlinks
============================================================

In

    ::

        Download the :download:`Makefle <../Makefile>`.

Out

    Download the :download:`Makefle <../Makefile>`.

.. tip::

        .. code-block:: rst

            .. only:: builder_html

                Download the :download:`Makefle <../Makefile>`.

**********************************************************************
References
**********************************************************************

- :doc:`RST ➤ Footnotes <Citations - rst,nts,ksa,2020-1110112449>`
- :doc:`RST ➤ Citations <Footnotes - rst,nts,ksa,2020-1110104849>`
- :doc:`RST ➤ Hyperlink references <Hyperlink references - rst,nts,ksa,2020-1109165211>`
- :doc:`RST ➤ Hyperlink targets <Hyperlink targets - rst,nts,ksa,2020-1110115624>`
- `Sphinx ➤ RST ➤ Basics # Hyperlink references <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks>`_
- `Sphinx ➤ RST ➤ Roles <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`_
- `Sphinx ➤ Extensions ➤ sphinx.ext.autosectionlabel <https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html>`_
- `Docutils ➤ Spec. ➤ Reference names <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#reference-names>`_
