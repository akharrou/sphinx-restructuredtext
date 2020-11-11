################################################################################
RST ➤ Images
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Images are supported with the ``images`` directive.

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        .. image:: _assets/lion\ -\ rst,imgs,ksa,2020-1111065317.jpg

Out

        .. image:: _assets/lion\ -\ rst,imgs,ksa,2020-1111065317.jpg

Customized
============================================================

In
    ::

        .. image:: _assets/lion\ -\ rst,imgs,ksa,2020-1111065317.jpg
            :height: 200
            :width: 200
            :scale: 50
            :alt: favorite lion
            :align: center
            :target: https://www.google.com

Out

    .. image:: _assets/lion\ -\ rst,imgs,ksa,2020-1111065317.jpg
        :height: 200
        :width: 200
        :scale: 50
        :alt: favorite lion
        :align: center
        :target: https://www.google.com

**********************************************************************
References
**********************************************************************

- `Sphinx ➤ RST ➤ Primer # Images <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#images>`_
- `Docutils ➤ Directives ➤ Images <https://docutils.sourceforge.io/docs/ref/rst/directives.html#images>`_
