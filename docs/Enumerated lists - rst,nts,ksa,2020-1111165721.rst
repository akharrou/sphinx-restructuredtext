################################################################################
RST ➤ Enumerated lists
################################################################################

**********************************************************************
Synopsis
**********************************************************************

Enumerated lists are supported.

**********************************************************************
Examples
**********************************************************************

Basic
============================================================

In
    ::

        1. Item-1
        #. Item-2

            A. Item-3
            #. Item-4

                a. Item-5
                #. Item-6

            #. Item-7
            #. Item-8

        #. Item-9
        #. Item-10

Out

    1. Item-1
    #. Item-2

        A. Item-3
        #. Item-4

            a. Item-5
            #. Item-6

        #. Item-7
        #. Item-8

    #. Item-9
    #. Item-10

**********************************************************************
Details
**********************************************************************

The following enumeration sequences are recognized:

- arabic numerals: 1, 2, 3, ... (no upper limit).
- uppercase alphabet characters: A, B, C, ..., Z.
- lower-case alphabet characters: a, b, c, ..., z.
- uppercase Roman numerals: I, II, III, IV, ..., MMMMCMXCIX (4999).
- lowercase Roman numerals: i, ii, iii, iv, ..., mmmmcmxcix (4999).

The following formatting types are recognized:

- suffixed with a period: ``1.``, ``A.``, ``a.``, ``I.``, ``i.``.
- surrounded by parentheses: ``(1)``, ``(A)``, ``(a)``, ``(I)``, ``(i)``.
- suffixed with a right-parenthesis: ``1)``, ``A)``, ``a)``, ``I)``, ``i)``.

Auto-enumerator, ``#``, may be used to automatically enumerate a list.

**********************************************************************
References
**********************************************************************

- `Docutils ➤ Spec. ➤ Enumerated lists <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#enumerated-lists>`_
