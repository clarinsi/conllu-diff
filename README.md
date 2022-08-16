# conllu-diff

Prototype results on sl_sst-ud-train.conllu vs. sl_ssj-ud-train.conllu. Ten strongest differences (if significant) ordered by the chi-square
statistic are given.

Differences on `lambda x:x['token']['upos']`:

```
{'event': 'INTJ', 'chisq': 8070.360866235494, 'chisq_p': 0.0, 'cramers_v': 0.18546269144487967, 'odds_ratio': (205.64922609298688, True)}
{'event': 'PART', 'chisq': 2056.565068284886, 'chisq_p': 0.0, 'cramers_v': 0.09362273156839818, 'odds_ratio': (3.3765821947519883, True)}
{'event': 'PUNCT', 'chisq': 1567.6550956294793, 'chisq_p': 0.0, 'cramers_v': 0.0817401329794944, 'odds_ratio': (3.619217699912104, False)}
{'event': 'ADV', 'chisq': 1142.860330852419, 'chisq_p': 1.598073190148637e-250, 'cramers_v': 0.0697921632735567, 'odds_ratio': (2.368271631503067, True)}
{'event': 'NOUN', 'chisq': 869.4354601346188, 'chisq_p': 4.3282461189130264e-191, 'cramers_v': 0.06087356761646711, 'odds_ratio': (1.9182977375177561, False)}
{'event': 'X', 'chisq': 702.1452287539261, 'chisq_p': 1.0214358052951111e-154, 'cramers_v': 0.054704563268060884, 'odds_ratio': (3.730096502268552, True)}
{'event': 'ADJ', 'chisq': 441.4172722521342, 'chisq_p': 5.321012378877541e-98, 'cramers_v': 0.04337452602078068, 'odds_ratio': (1.914494685493001, False)}
{'event': 'DET', 'chisq': 357.94699558351994, 'chisq_p': 7.881761145747209e-80, 'cramers_v': 0.039058849022439675, 'odds_ratio': (1.8178073753376662, True)}
{'event': 'VERB', 'chisq': 342.00443253230947, 'chisq_p': 2.335310205815499e-76, 'cramers_v': 0.038179122992568475, 'odds_ratio': (1.5098089234134449, True)}
{'event': 'PRON', 'chisq': 214.47896133270953, 'chisq_p': 1.4478754766508423e-48, 'cramers_v': 0.030234474845866527, 'odds_ratio': (1.6315601187054114, True)}
```

Differences on `lambda x:x['token']['lemma']`:

```
{'event': 'ja', 'chisq': 4890.147430679087, 'chisq_p': 0.0, 'cramers_v': 0.1443680388876384, 'odds_ratio': (316.50392575024387, True)}
{'event': 'eee', 'chisq': 4747.68169967276, 'chisq_p': 0.0, 'cramers_v': 0.14224954241402205, 'odds_ratio': (9727.90290395421, True)}
{'event': '[gap]', 'chisq': 4625.7037167557555, 'chisq_p': 0.0, 'cramers_v': 0.1404103062969733, 'odds_ratio': (9473.866117350688, True)}
{'event': '_', 'chisq': 2509.5506880391117, 'chisq_p': 0.0, 'cramers_v': 0.10342084138781252, 'odds_ratio': (5109.162639646662, True)}
{'event': '[name:personal]', 'chisq': 1712.737497185906, 'chisq_p': 0.0, 'cramers_v': 0.08543886760201726, 'odds_ratio': (3486.230522337837, True)}
{'event': ',', 'chisq': 1497.807242458878, 'chisq_p': 0.0, 'cramers_v': 0.0798983928857083, 'odds_ratio': (3017.3227483286178, False)}
{'event': '[pause]', 'chisq': 1425.1214614141568, 'chisq_p': 0.0, 'cramers_v': 0.07793562469300712, 'odds_ratio': (2903.1409295352323, True)}
{'event': '…', 'chisq': 1135.7272474952044, 'chisq_p': 5.673920109982285e-249, 'cramers_v': 0.06957402089144266, 'odds_ratio': (29.21324122737166, True)}
{'event': '.', 'chisq': 966.3613311948499, 'chisq_p': 3.6831991618905715e-212, 'cramers_v': 0.06417706510165858, 'odds_ratio': (1943.1095197895877, False)}
{'event': 'ne', 'chisq': 893.8107212975139, 'chisq_p': 2.1742059484156198e-196, 'cramers_v': 0.06172098673848206, 'odds_ratio': (4.567216172071131, True)}
```

Differences on `lambda x:x['token']['deprel']`:

```
{'event': 'discourse', 'chisq': 9343.93284851421, 'chisq_p': 0.0, 'cramers_v': 0.1995606615688087, 'odds_ratio': (75.78024049293329, True)}
{'event': 'discourse:filler', 'chisq': 5601.848762765675, 'chisq_p': 0.0, 'cramers_v': 0.1545168231515424, 'odds_ratio': (11514.411314984709, True)}
{'event': 'reparandum', 'chisq': 4780.950412717735, 'chisq_p': 0.0, 'cramers_v': 0.14274706919825084, 'odds_ratio': (9797.236607142857, True)}
{'event': 'punct', 'chisq': 1567.4516368485306, 'chisq_p': 0.0, 'cramers_v': 0.0817348284684769, 'odds_ratio': (3.6189527899648515, False)}
{'event': 'parataxis:discourse', 'chisq': 1546.7971951595625, 'chisq_p': 0.0, 'cramers_v': 0.08119452932918504, 'odds_ratio': (3149.6412683633353, True)}
{'event': 'root', 'chisq': 1071.7810863150387, 'chisq_p': 4.489282674727148e-235, 'cramers_v': 0.06758699304934265, 'odds_ratio': (2.238339638285662, True)}
{'event': 'advmod', 'chisq': 1062.816680427586, 'chisq_p': 3.9865151523574164e-233, 'cramers_v': 0.06730374982664965, 'odds_ratio': (2.026798690361553, True)}
{'event': 'nmod', 'chisq': 702.5558056288976, 'chisq_p': 8.316275380229946e-155, 'cramers_v': 0.054720555078059535, 'odds_ratio': (3.295046424712571, False)}
{'event': 'parataxis:restart', 'chisq': 640.052139965117, 'chisq_p': 3.255369019821476e-141, 'cramers_v': 0.05222972721988518, 'odds_ratio': (1318.8134851138354, True)}
{'event': 'amod', 'chisq': 523.7028691386917, 'chisq_p': 6.621236773231577e-116, 'cramers_v': 0.047244641439906455, 'odds_ratio': (2.3917425656320344, False)}
```

Differences on `lambda x:x['token']['deprel']+'_'+x['tokenlist'][x['token']['head']-1]['deprel']`:

```
{'event': 'root_root', 'chisq': 7070.889958513253, 'chisq_p': 0.0, 'cramers_v': 0.17359896035273648, 'odds_ratio': (648.5884638574395, True)}
{'event': 'discourse_root', 'chisq': 6897.109601269658, 'chisq_p': 0.0, 'cramers_v': 0.17145242984385184, 'odds_ratio': (72.03408395115126, True)}
{'event': 'discourse:filler_root', 'chisq': 2254.959428374757, 'chisq_p': 0.0, 'cramers_v': 0.09803461483029019, 'odds_ratio': (4589.407566950384, True)}
{'event': 'root_discourse', 'chisq': 1967.221263830765, 'chisq_p': 0.0, 'cramers_v': 0.09156651507631461, 'odds_ratio': (4003.3505234788017, True)}
{'event': 'discourse_parataxis', 'chisq': 1437.573273020124, 'chisq_p': 0.0, 'cramers_v': 0.07827536035072087, 'odds_ratio': (62.33594120436226, True)}
{'event': 'root_obl', 'chisq': 1247.726673223756, 'chisq_p': 2.588978271840005e-273, 'cramers_v': 0.07292388715079515, 'odds_ratio': (65.09883449678254, True)}
{'event': 'root_advmod', 'chisq': 1135.8275302941938, 'chisq_p': 5.396198838828705e-249, 'cramers_v': 0.0695770924579469, 'odds_ratio': (781.3144361833953, True)}
{'event': 'reparandum_root', 'chisq': 1082.2808867948213, 'chisq_p': 2.344559240210394e-237, 'cramers_v': 0.06791724722869547, 'odds_ratio': (2209.9641271807577, True)}
{'event': 'root_parataxis', 'chisq': 1075.3010136537969, 'chisq_p': 7.711232176151803e-236, 'cramers_v': 0.06769788616909038, 'odds_ratio': (180.29914132748706, True)}
{'event': 'parataxis:discourse_root', 'chisq': 894.3125564326243, 'chisq_p': 1.6912466578959566e-196, 'cramers_v': 0.06173831110739071, 'odds_ratio': (1830.7758754061163, True)}
```
