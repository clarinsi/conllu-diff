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
