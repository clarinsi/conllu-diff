# Invoke pytest in conllu-diff/conlludiff/tests directory!
from pathlib import Path


def test_importing():
    from conlludiff import Differ

    assert True


def test_loading_files():
    from conlludiff import Differ

    d = Differ("data/sl_ssj-ud-train.conllu", "data/sl_sst-ud-train.conllu")
    assert True


def test_equal_performance_upos():
    from conlludiff import Differ

    d = Differ(
        "data/sl_ssj-ud-train.conllu",
        "data/sl_sst-ud-train.conllu",
        event="upos",
        filter=0.05,
        fields=[
            "event",
            "cramers_v",
            "odds_ratio",
            "odds_ratio_direction",
            # "contingency"
        ],
        order="chisq",
        reverse=True,
    )
    old = Path("data/original_upos.csv").read_text()
    assert d.results_string.split() == old.split()


events = ["deprel", "deprel+head_deprel", "feat", "lemma", "upos"]
paths = [f"data/original_{i}.csv" for i in events]

import pytest


@pytest.mark.parametrize("event,path", [(i, j) for i, j in zip(events, paths)])
def test_equal_performance(event, path):
    from conlludiff import Differ
    from pathlib import Path

    fields = ["event", "cramers_v", "odds_ratio", "odds_ratio_direction"]
    d = Differ(
        "data/sl_ssj-ud-train.conllu",
        "data/sl_sst-ud-train.conllu",
        event=event,
        filter=0.05,
        fields=fields,
        order="chisq",
        reverse=True,
    )
    assert Path(path).exists(), "Path does not exist"
    expected = Path(path).read_text()
    M = len(expected.split())
    assert d.results_string.split()[:M] == expected.split()[:M]
