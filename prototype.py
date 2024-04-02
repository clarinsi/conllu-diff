import argparse
import importlib
import logging
import sys
from collections import Counter
from math import log, sqrt

import numpy as np
from conllu import parse, parse_incr
from scipy.stats import chi2_contingency

parser = argparse.ArgumentParser(description="")
parser.add_argument("config", metavar="c", type=str, help="JSON configuration file")
args = parser.parse_args()
import json

# from types import SimpleNamespace
# config=json.load(open(args.config),object_hook=lambda d: SimpleNamespace(**d))
config = json.load(open(args.config))

predefined_events = {
    "form": lambda x: x["token"]["form"],
    "lemma": lambda x: x["token"]["lemma"],
    "upos": lambda x: x["token"]["upos"],
    "xpos": lambda x: x["token"]["xpos"],
    "upos+feats": lambda x: x["token"]["upos"]
    + "_"
    + "|".join([e[0] + ":" + e[1] for e in x["token"]["feats"].items()])
    if x["token"]["feats"] != None
    else x["token"]["upos"],
    "feat": lambda x: [e[0] + ":" + e[1] for e in x["token"]["feats"].items()]
    if x["token"]["feats"] != None
    else None,
    "feats": lambda x: "|".join(
        [e[0] + ":" + e[1] for e in x["token"]["feats"].items()]
    )
    if x["token"]["feats"] != None
    else None,
    "deprel": lambda x: x["token"]["deprel"],
    "deprel+head_deprel": lambda x: x["token"]["deprel"]
    + "_"
    + x["tokenlist"][x["token"]["head"] - 1]["deprel"]
    if x["token"]["deprel"] != "root"
    else None,
}

if config["event"] in predefined_events:
    config["event_function"] = predefined_events[config["event"]]
else:
    config["event_function"] = eval(config["event"])

events1 = []
for tokenlist in parse_incr(open(config["file1"])):
    # print(tokenlist[0]['feats'])
    for token in tokenlist:
        event = config["event_function"]({"token": token, "tokenlist": tokenlist})
        if event != None:
            if not isinstance(event, list):
                events1.append(event)
            else:
                events1.extend(event)
c1 = len(events1)
events1 = Counter(events1)

events2 = []
for tokenlist in parse_incr(open(config["file2"])):
    # print(tokenlist[0]['form'])
    for token in tokenlist:
        event = config["event_function"]({"token": token, "tokenlist": tokenlist})
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


invalid_counter = 0
results = []
for event in set(events1).union(set(events2)):
    f1 = events1.get(event, 0)
    f2 = events2.get(event, 0)
    test = chi2_contingency(((f1, c1 - f1), (f2, c2 - f2)))
    or_result, or_direction = odds_ratio(f1, c1, f2, c2)
    expected_f = list(np.append(*test.expected_freq))

    # check if all expected frequencies are above 5
    if any(y < 5 for y in expected_f):
        invalid_counter += 1
    else:
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

if invalid_counter:
    logging.warning(
        f"{invalid_counter} events were not recorded since one or more expected values were "
        f"less than 5"
    )

# adam's wilcoxon
# difference in relative frequency
# craig's zetta (might need substructure
# multiple feature extractors? a vs b

# filter results
if "filter" in config:
    results = [e for e in results if e["chisq_p"] < float(config["filter"])]
if config["order"] in results[0]:
    results = sorted(
        results,
        key=lambda x: (x[config["order"]], x["event"]),
        reverse=config["reverse"],
    )
import csv

if config["output"] == "stdout":
    csvfile = sys.stdout
else:
    csvfile = open(config["output"], "w")
writer = csv.DictWriter(
    csvfile, config["fields"], delimiter="\t", extrasaction="ignore"
)
writer.writeheader()
for result in results:
    writer.writerow(result)
csvfile.close()
