# conlludiff package

## Submodules

## conlludiff.differ module

### *class* conlludiff.differ.Differ(file1: str | Path, file2: str | Path, event: str = 'upos', filter: float | None = None, fields: list[str] = ['event', 'cramers_v', 'odds_ratio', 'odds_ratio_direction', 'contingency'], order: str = 'chisq', reverse: bool = True)

Bases: `object`

Class for reading and statistical analysis of two
CONLLU documents.

### Example use

```python
from conlludiff import Differ
d = Differ("file1.conllu", "file2.conllu")
d.to_tsv("output.tsv")
```

#### \_\_init_\_(file1: str | Path, file2: str | Path, event: str = 'upos', filter: float | None = None, fields: list[str] = ['event', 'cramers_v', 'odds_ratio', 'odds_ratio_direction', 'contingency'], order: str = 'chisq', reverse: bool = True)

Method to instantiate an instance with all the necessary data and run analysis.

* **Parameters:**
  * **file1** (*str* *|* *Path*) – First CONLLU path
  * **file2** (*str* *|* *Path*) – Second CONLLU path
  * **event** (*str* *,* *optional*) – The linguistic feature the comparison is to be based on, optional events are “form”, “lemma”, “upos”, “xpos”, “upos+feats”, “feat” (each feature separately), “feats” (all features of a word merged), “deprel”, “deprel+head_deprel”. defaults to “upos”
  * **filter** (*float* *|* *None* *,* *optional*) – The minimum p-value of the chi-square test for the entry to be filtered from the results, defaults to None
  * **fields** (*list* *[**str* *]* *,* *optional*) – List of values to be returned, defaults to [ “event”, “cramers_v”, “odds_ratio”, “odds_ratio_direction”, “contingency”, ]
  * **order** (*str* *,* *optional*) – The value by which the events will be ordered, defaults to “chisq”
  * **reverse** (*bool* *,* *optional*) – Whether the order has to be reverse, defaults to True

After instantiating a Differ object, the metrics will be calculated automatically.

#### to_tsv(path: str | Path)

Export the results to tsv file

* **Parameters:**
  **path** (*str* *|* *Path*) – Path to which results will be written

## Module contents
