# Invoke pytest in conllu-diff/conlludiff directory!

def test_importing():
    from conlludiff import Differ
    assert True

def test_loading_files():
    from conlludiff import Differ
    d = Differ("tests/data/sl_ssj-ud-train.conllu", "tests/data/sl_sst-ud-train.conllu")
    assert True

def test_equal_performance():
    from conlludiff import Differ
    from pathlib import Path
    d = Differ("tests/data/sl_ssj-ud-train.conllu",
               "tests/data/sl_sst-ud-train.conllu",
                event="upos",
                filter=0.05,
                fields=["event",
                        "cramers_v",
                        "odds_ratio",
                        "odds_ratio_direction",
                        "contingency"
                        ],
                order="chisq",
                reverse=True,
                               )
    old = Path("tests/data/original_output.csv").read_text()
    assert d.results_string.split() == old.split()