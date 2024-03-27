from conlludiff import Differ
from pathlib import Path

d = Differ(
    "data/sl_ssj-ud-train.conllu",
    "data/sl_sst-ud-train.conllu",
    event="deprel+head_deprel",
    filter=0.05,
    fields=[
        "event",
        "cramers_v",
        "odds_ratio",
        "odds_ratio_direction",
    ],
    order="chisq",
    reverse=True,
)
old = Path("data/original_deprel+head_depreHl.csv").read_text()
d.to_tsv("data/new_deprel+head_deprel.csv")
2 + 2
