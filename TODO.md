# ✓ Create requirements.txt or environment.yml

useful command:
```bash
pip freeze > requirements.txt
conda env export > environment.yml
```
# How to call it?

One idea:
```python
from conlludiff import Differ

d = Differ("tests/data/sl_ssj-ud-train.conllu", "tests/data/sl_sst-ud-train.conllu", **other_options)
d.to_csv("output.csv")
```
# Inspect Luka's zip, check contingency attribute, perhaps a filtering on contingency > 5 should be implemented

# Transform `__main__.py` so that it runs with `python conlludiff <json>` instead of `python -m conlludiff <json>`