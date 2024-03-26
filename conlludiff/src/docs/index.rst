.. conlludiff documentation master file, created by
   sphinx-quickstart on Tue Mar 26 14:44:53 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to conlludiff's documentation!
======================================

Example use
-----------


.. code-block:: python

    from conlludiff import Differ
    d = Differ("file1.conllu", "file2.conllu")
    d.to_tsv("output.tsv")



.. automodule:: conlludiff
   :no


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   intro
   examples
   conlludiff
   module

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`
