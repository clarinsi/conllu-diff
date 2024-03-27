import argparse
import importlib
import csv
import sys
from pathlib import Path
from collections import Counter
from conllu import parse_incr, parse
from scipy.stats import chi2_contingency
from math import sqrt, log, inf


predefined_events = {
    "form": lambda x: x["token"]["form"],
    "lemma": lambda x: x["token"]["lemma"],
    "upos": lambda x: x["token"]["upos"],
    "xpos": lambda x: x["token"]["xpos"],
    "upos+feats": lambda x: (
        x["token"]["upos"]
        + "_"
        + "|".join([e[0] + ":" + e[1] for e in x["token"]["feats"].items()])
        if x["token"]["feats"] != None
        else x["token"]["upos"]
    ),
    "feat": lambda x: (
        [e[0] + ":" + e[1] for e in x["token"]["feats"].items()]
        if x["token"]["feats"] != None
        else None
    ),
    "feats": lambda x: (
        "|".join([e[0] + ":" + e[1] for e in x["token"]["feats"].items()])
        if x["token"]["feats"] != None
        else None
    ),
    "deprel": lambda x: x["token"]["deprel"],
    "deprel+head_deprel": lambda x: (
        x["token"]["deprel"] + "_" + x["tokenlist"][x["token"]["head"] - 1]["deprel"]
        if x["token"]["deprel"] != "root"
        else None
    ),
}


class Differ:
    """Class for reading and statistical analysis of two
    CONLLU documents.

    Example use
    ===========

    .. code-block:: python

        from conlludiff import Differ
        d = Differ("file1.conllu", "file2.conllu")
        d.to_tsv("output.tsv")
    """

    def __init__(
        self,
        file1: str | Path,
        file2: str | Path,
        event: str = "upos",
        filter: float | None = None,
        fields: list[str] = [
            "event",
            "cramers_v",
            "odds_ratio",
            "odds_ratio_direction",
            "contingency",
        ],
        order: str = "chisq",
        reverse: bool = True,
    ):
        """Method to instantiate an instance with all the necessary data and run analysis.

        :param file1: First CONLLU path
        :type file1: str | Path
        :param file2: Second CONLLU path
        :type file2: str | Path
        :param event: The linguistic feature the comparison is to be based on, optional events are "form", "lemma", "upos", "xpos", "upos+feats", "feat" (each feature separately), "feats" (all features of a word merged), "deprel", "deprel+head_deprel". defaults to "upos"
        :type event: str, optional
        :param filter: The minimum p-value of the chi-square test for the entry to be filtered from the results, defaults to None
        :type filter: float | None, optional
        :param fields: List of values to be returned, defaults to [ "event", "cramers_v", "odds_ratio", "odds_ratio_direction", "contingency", ]
        :type fields: list[str], optional
        :param order: The value by which the events will be ordered, defaults to "chisq"
        :type order: str, optional
        :param reverse: Whether the order has to be reverse, defaults to True
        :type reverse: bool, optional


        After instantiating a Differ object, the metrics will be calculated automatically.
        """
        self.config = {
            "file1": file1,
            "file2": file2,
            "event": event,
            "filter": filter,
            "fields": fields,
            "order": order,
            "reverse": reverse,
        }
        self._run()

    def to_tsv(self, path: str | Path):
        """Export the results to tsv file

        Args:
            path (str | Path): Path to which results will be written
        """
        Path(path).write_text(self.results_string)

    def _run(self):
        config = self.config
        if not config["filter"]:
            config["filter"] = inf
        if config["event"] in predefined_events:
            config["event_function"] = predefined_events[config["event"]]
        else:
            config["event_function"] = eval(config["event"])

        events1 = []
        with open(config["file1"], "r") as f:
            for tokenlist in parse_incr(f):
                for token in tokenlist:
                    event = config["event_function"](
                        {"token": token, "tokenlist": tokenlist}
                    )
                    if event != None:
                        if not isinstance(event, list):
                            events1.append(event)
                        else:
                            events1.extend(event)
        c1 = len(events1)
        events1 = Counter(events1)

        events2 = []
        with open(config["file2"], "r") as f:
            for tokenlist in parse_incr(f):
                for token in tokenlist:
                    event = config["event_function"](
                        {"token": token, "tokenlist": tokenlist}
                    )
                    if event != None:
                        if not isinstance(event, list):
                            events2.append(event)
                        else:
                            events2.extend(event)

        c2 = len(events2)
        events2 = Counter(events2)

        def odds_ratio(f1, c1, f2, c2):
            result = ((f1 + 0.5) / (c1 - f1)) / ((f2 + 0.5) / (c2 - f2))
            if result >= 1.0:
                return (result, "first")
            else:
                return (((f2 + 0.5) / (c2 - f2)) / ((f1 + 0.5) / (c1 - f1)), "second")

        def llr(f1, c1, f2, c2):
            f1 += 0.5
            f2 += 0.5
            e1 = c1 * (f1 + f2) / (c1 + c2)
            e2 = c2 * (f1 + f2) / (c1 + c2)
            try:
                return 2 * ((f1 * log(f1 / e1)) + (f2 * log(f2 / e2)))
            except:
                return

        results = []
        for event in set(events1).union(set(events2)):
            f1 = events1.get(event, 0)
            f2 = events2.get(event, 0)
            # try:
            test = chi2_contingency(((f1, c1 - f1), (f2, c2 - f2)))
            # except:
            #    continue
            or_result, or_direction = odds_ratio(f1, c1, f2, c2)
            results.append(
                {
                    "event": event,
                    "chisq": test[0],
                    "chisq_p": test[1],
                    "cramers_v": sqrt(test[0] / (c1 + c2)),
                    "odds_ratio": or_result,
                    "odds_ratio_direction": or_direction,
                    "llr": llr(f1, c1, f2, c2),
                    "contingency": ((f1, c1 - f1), (f2, c2 - f2)),
                }
            )
        # adam's wilcoxon
        # difference in relative frequency
        # craig's zetta (might need substructure
        # multiple feature extractors? a vs b

        if "filter" in config:
            results = [e for e in results if e["chisq_p"] < float(config["filter"])]
        if config["order"] in results[0]:
            results = sorted(
                results,
                key=lambda x: (x[config["order"]], x["event"]),
                reverse=config["reverse"],
            )
        self.results = [{f: i.get(f) for f in config["fields"]} for i in results]
        from contextlib import redirect_stdout
        import io

        f = io.StringIO()
        with redirect_stdout(f):
            writer = csv.DictWriter(
                f, config["fields"], delimiter="\t", extrasaction="ignore"
            )
            writer.writeheader()
            for result in results:
                writer.writerow(result)
        self.results_string = f.getvalue()
