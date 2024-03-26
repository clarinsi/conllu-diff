Example use
===========

.. code-block:: python
    from conlludiff import Differ
    d = Differ("file1.conllu", "file2.conllu")
    d.to_tsv("output.tsv")