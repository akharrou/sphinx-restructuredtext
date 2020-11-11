################################################################################
RST ➤ Raw directive
################################################################################

**********************************************************************
Synopsis
**********************************************************************

You can pass raw data to the Writer (program that writes the output files) to
write straight into the output files with the ``raw`` directive::

    .. raw:: <writer>      <--- type of writer, e.g. html, latex, ...
        :file: str         <--- path to file to be included
        :url: str          <--- URL to file to be included
        :encoding: str     <--- encoding of raw data

.. warning:: The ``raw`` directive represents a potential security hole. It can
   be disabled with the "raw_enabled" or "file_insertion_enabled" runtime
   settings.

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    Pass data to HTML Writer::

        .. raw:: html

            <hr width=50 size=10>


    Pass data to LaTeX Writer::

        .. raw:: latex

            \setlength{\parindent}{0pt}

    Pass raw data from external file::

        .. raw:: html
            :file: inclusion.html

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Directives ➤ Raw data pass-through <https://docutils.sourceforge.io/docs/ref/rst/directives.html#raw-data-pass-through>`_
