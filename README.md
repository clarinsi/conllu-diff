# conllu-diff

A tool for statistically comparing two conllu files. It offers two equivalent use modes:
* as a command line program
* as a python package

## Installation

```
pip install conlludiff
```

## CLI use

Run as `python conlludiff <json>`.

The tool is configured through a JSON configuration file (example in `config_files/ssj_sst_upos.json`) where the user defines:
- `file1` - The conllu file containing the first language sample
- `file2` - The conllu file containing the second language sample
- `event` - The linguistic feature the comparison is to be based on, optional events are form, lemma, upos, xpos, upos+feats, feat (each feature separately), feats (all features of a word merged), deprel, deprel+head_deprel
- `filter` - The minimum p-value of the chi-square test for the entry to be filtered from the results
- `fields` - A list of fields to be retained in the output (list of available values is listed below)
- `order` - The field by which the output is to be ordered
- `reverse` - Whether the ordering should be reverse
- `output` - Where the output is to be produced, either stdout or filename

The following fields / values are currently available:
- `chisq` - The chi-square statistical test.
- `chisq_p` - The p-value of the chi-square test. Very useful for discarding results with p-value below 0.05. These results you simply cannot trust (they might have happened by chance) and do not have to look at.
- `cramers_v` - The Cramer's V effect size, based on the chi square statistic and the sample size. Traditionally it should be over 0.1 for small effect, over 0.3 for medium effect and over 0.5 for strong effect, but on language phenomena it will never achieve even medium effect. It is comparable across datasets of different sizes, so if the tool is run on multiple pairs of documents, these effect sizes CAN be used for comparison across datasets.
- `odds_ratio` - The odds ratio effect size. Put simply - it reports how many times the odds of an event are higher in one dataset in comparison to another dataset. It is always higher than 1. This is why `odds_ratio_direction` gives info on the dataset for which the odds of a specific event are higher.
- `odds_ratio_direction` - The direction of the odds ratio presented previously. If `first`, the odds of the event are greater in the first dataset. If `second`, the odds for this event are higher in the second dataset.
- `log_likelihood_ratio` - The log-likelihood ratio, as defined by Danning (1993), here mostly for reasons of popularity in the computational linguistics circles.

## Python API

### Use
The differ can be used through its python API as follows:

```python
from conlludiff import Differ

d = Differ(
    "conllu_files/sl_ssj-ud-train.conllu",
    "conllu_files/sl_sst-ud-train.conllu",
    event="upos",
    filter=0.05,
    fields=[
        "event",
        "cramers_v",
        "odds_ratio",
        "odds_ratio_direction",
        "contingency"
    ],
    order="chisq",
    reverse=True,
)
d.results
#[
# {'event': 'INTJ', 'cramers_v': 0.18546269144487967, 'odds_ratio': 205.64922609298688, 'odds_ratio_direction': 'second'},
# {'event': 'PART', 'cramers_v': 0.09362273156839818, 'odds_ratio': 3.3765821947519883, 'odds_ratio_direction': 'second'},
# {'event': 'PUNCT', 'cramers_v': 0.0817401329794944, 'odds_ratio': 3.619217699912104, 'odds_ratio_direction': 'first'},
# {'event': 'ADV', 'cramers_v': 0.0697921632735567, 'odds_ratio': 2.368271631503067, 'odds_ratio_direction': 'second'},
# {'event': 'NOUN', 'cramers_v': 0.06087356761646711, 'odds_ratio': 1.9182977375177561, 'odds_ratio_direction': 'first'}
# ...]

d.to_tsv("output.tsv")
# Writes the data to a tsv, same way as CLI.
```


## Outputs


Running the tool on the exemplary JSON configuration file compares the UPOS dependence between the two files, `sl_sst-ud-train.conllu` and `sl_ssj-ud-train.conllu`.

The output of the tool with the `event` set to `upos`:

```
event	cramers_v	odds_ratio	odds_ratio_direction
INTJ	0.18546269144487967	205.64922609298688	second
PART	0.09362273156839818	3.3765821947519883	second
PUNCT	0.0817401329794944	3.619217699912104	first
ADV	0.0697921632735567	2.368271631503067	second
NOUN	0.06087356761646711	1.9182977375177561	first
X	0.054704563268060884	3.730096502268552	second
ADJ	0.04337452602078068	1.914494685493001	first
DET	0.039058849022439675	1.8178073753376662	second
VERB	0.038179122992568475	1.5098089234134449	second
PRON	0.03023447484586653	1.6315601187054114	second
ADP	0.027554631145556924	1.5029875604157752	first
CCONJ	0.020521602435811057	1.3849776400810214	second
PROPN	0.018222766826042337	1.48950205465959	first
SCONJ	0.01516452354505404	1.3147102075692845	second
SYM	0.00788752606312867	31.431147723995498	first
NUM	0.006279927568528497	1.1841482466696223	first
```

The output of the tool if the event is `lemma`:

```
event	cramers_v	odds_ratio	odds_ratio_direction
ja	0.1443680388876384	316.50392575024387	second
eee	0.14224954241402205	9727.90290395421	second
[gap]	0.1404103062969733	9473.866117350688	second
_	0.10342084138781253	5109.162639646662	second
[name:personal]	0.08543886760201726	3486.230522337837	second
,	0.0798983928857083	3017.3227483286178	first
[pause]	0.07793562469300712	2903.1409295352323	second
…	0.06957402089144266	29.21324122737166	second
.	0.06417706510165858	1943.1095197895877	first
ne	0.06172098673848206	4.567216172071131	second
mhm	0.06135550149322792	1808.49138820132	second
pa	0.05533923234690654	3.5866900542385225	second
[speaker:laughter]	0.05267879283333141	1341.047493947355	second
no	0.05236304456192136	33.68782033850626	second
eem	0.05177677215351289	1296.5817666752512	second
ta	0.04975510679153412	3.112790024717654	second
aha	0.04842184761560267	387.7447093352556	second
?	0.047909243941398276	6.54896239567592	second
[name:surname]	0.04599517464931115	1029.9796674731044	second
pol	0.04522323386592585	19.314885381209148	second
vedeti	0.044877978271710375	8.204695698185576	second
[audience:laughter]	0.04443254560578941	963.3805970149255	second
kaj	0.04422508295450475	6.665906246951688	second
jaz	0.04254326905719024	4.205848770006655	second
zdaj	0.04220703488553522	8.449570357876933	second
[:voice]	0.03937486931297157	763.7067235968929	second
pač	0.03880380764818679	16.29708140017637	second
ti	0.0374965082691098	5.789587920409137	second
a	0.036544753303008326	6.611184664673473	second
reči	0.03507827440464862	7.032673208444842	second
tako	0.03488349828161137	3.661944581348252	second
ampak	0.03300775971108695	8.776849122671143	second
mmm	0.03213178836124324	519.9118251928021	second
[incident]	0.03213178836124324	519.9118251928021	second
[all:laughter]	0.03213178836124324	519.9118251928021	second
iti	0.03203659707760247	5.261877926755125	second
aja	0.03063185252461786	475.61510384536297	second
misliti	0.030313213443565672	7.600055895339754	second
ka	0.02979521974817808	158.53763109191857	second
ful	0.02745038147121303	64.78054798745696	second
imeti	0.026728261048545494	2.8695967134026836	second
zdajle	0.02646949225144055	129.01572779605263	second
en	0.026425718058774403	3.8274431810951612	second
dati	0.025769048935856378	6.3530704294133375	second
tale	0.025422305095331388	17.767587428769104	second
te	0.024677083578157007	320.6482861400894	second
ma	0.024643752142178156	114.25932778291704	second
gor	0.023985218122048756	28.75423049244371	second
tam	0.02388517506596499	6.532873916176885	second
samo	0.023726743621988657	4.152648893958719	second
oni	0.02313889520888621	19.023543080403044	second
aaa	0.02269213397252964	276.39252864703764	second
...
```

The output of the tool if the event is `feat`:

```
event	cramers_v	odds_ratio	odds_ratio_direction
Person:1	0.04939558517684953	3.5638167542809853	second
Person:2	0.047040110877374676	5.079993584778688	second
PronType:Dem	0.037175859411220154	3.245197490851571	second
Case:Gen	0.03144647693695685	2.172092243237678	first
NumForm:Word	0.028272960330824267	3.440339072082062	second
VerbForm:Fin	0.0267587007742558	1.5225701489232548	second
Mood:Ind	0.02504649601144956	1.5056171393724438	second
Gender:Masc	0.025042316104147304	1.4748890960035126	first
Reflex:Yes	0.024416673107363094	699.5006025688363	first
Tense:Pres	0.023517648140906504	1.4896134066798563	second
NumForm:Digit	0.022483697118357206	593.4206504177673	first
Case:Loc	0.02179297260457836	1.7083552918624372	first
Gender:Fem	0.02129852556496575	1.4327016742281735	first
PronType:Int	0.019116864692380664	2.8254802331440025	second
Mood:Imp	0.018378570965450702	3.791997651968869	second
Case:Ins	0.018308854809044352	2.0816886275516455	first
Aspect:Imp	0.01595530651024542	1.491526932928539	second
Polarity:Pos	0.015389343283813696	1.3931175980723853	second
Number:Plur	0.015101686601082178	1.2937540626185027	first
PronType:Prs	0.012840220897127438	1.391913401310955	second
Polarity:Neg	0.010467835392964546	1.6218991635410638	second
Abbr:Yes	0.009174573465203728	100.64168811481056	first
Tense:Fut	0.008659708802953942	1.6695810431815645	second
Poss:Yes	0.008622929553196686	1.8430908774898307	first
PronType:Ind	0.007988560895972635	1.5545205160767552	second
VerbForm:Sup	0.007606299226342561	6.994685959408413	second
VerbForm:Part	0.007588183914607259	1.2152331908399183	first
PronType:Neg	0.0072933899363323805	2.492256128366947	second
Gender[psor]:Masc	0.006270434086374932	7.047436934055062	first
Degree:Pos	0.006204462420882378	1.1017059175543398	second
Definite:Def	0.006094185561369171	1.6136203228373713	first
Case:Dat	0.005207882750413297	1.296449710663011	first
NumType:Ord	0.004907024006001947	1.6690069108717716	first
Gender[psor]:Fem	0.0043045691241584165	4.971538958295724	first
Number:Sing	0.0042501886679687595	1.0445633278559616	first
Number[psor]:Sing	0.004168042039340886	1.7214890333000743	first
Variant:Short	0.004116420078423952	1.15773584843268	second
Number[psor]:Plur	0.003520769896614546	1.4800187255151183	second
Animacy:Anim	0.0031959140489293135	1.609703528865278	first
Number:Dual	0.003119169910226467	1.1902942252586413	second
Degree:Sup	0.0028717358191274397	1.4607040532750566	first
NumForm:Roman	0.002735775335474741	10.900416396883163	first
Definite:Ind	0.0027015758531109017	1.230778104542293	first
NumType:Mult	0.002586134214293405	5.35236774349564	second
```

Output of the tool if the event is `deprel`:

```
event	cramers_v	odds_ratio	odds_ratio_direction
discourse	0.1995606615688087	75.78024049293329	second
discourse:filler	0.1545168231515424	11514.411314984709	second
reparandum	0.14274706919825084	9797.236607142857	second
punct	0.08173482846847689	3.6189527899648515	first
parataxis:discourse	0.08119452932918503	3149.6412683633353	second
root	0.06758699304934265	2.238339638285662	second
advmod	0.06730374982664965	2.026798690361553	second
nmod	0.05472055507805954	3.295046424712571	first
parataxis:restart	0.05222972721988518	1318.8134851138354	second
amod	0.047244641439906455	2.3917425656320344	first
conj:extend	0.04225937967772594	874.6138211382115	second
parataxis	0.0398717788389968	2.265339381899786	second
dislocated	0.035933307354648995	47.53133350886273	second
case	0.030560438744177788	1.5760166637679451	first
vocative	0.029795832802305106	9.331577965730597	second
fixed	0.024153593693035522	2.418883738805336	second
obl	0.0214600136068333	1.4392252992918104	first
conj	0.01946154708029554	1.509069018715358	first
list	0.014859841032733846	105.90846429170628	first
nummod	0.013237722191482327	1.5856577201396964	first
flat	0.01226834979992188	2.865560442489671	second
ccomp	0.012109670762191542	1.5403849395768785	second
appos	0.01192489066635104	2.0258632065250364	first
mark	0.011210811993208638	1.2446775351581985	second
acl	0.011205361560489591	1.4731494732818564	first
orphan	0.009752798810071982	2.3358535915763845	first
cc	0.008654128343704083	1.1770939880197218	second
advcl	0.007143729012211228	1.284389185911365	second
flat:name	0.006644743576550729	1.417384017797551	first
dep	0.006150595406649066	4.385886921540406	first
aux	0.005735206555028642	1.1100447817440058	first
```

Output of the tool if the event is `deprel+head_deprel`:

```
discourse_root	0.18202736862729124	76.9150923698931	second
discourse:filler_root	0.10398408766447145	4883.512041884816	second
discourse_parataxis	0.08310549743890455	66.31108288242072	second
reparandum_root	0.07203903218914691	2350.031683626272	second
parataxis:discourse_root	0.0654853384402872	1946.6054409980939	second
advmod_root	0.06281476752222244	2.557906542509336	second
cc_root	0.055707328412306335	6.9863965946940025	second
discourse:filler_parataxis	0.052954640088375506	1283.8629836802952	second
advmod_parataxis	0.0494810299649954	3.0164190203770955	second
advmod_reparandum	0.04878776582774138	1094.9009164793358	second
parataxis:restart_root	0.04824164203380061	1071.2929106628242	second
mark_root	0.04787571436102816	12.4166781015429	second
discourse:filler_conj	0.04656491000281119	1000.4852186941738	second
cc_conj:extend	0.0454127571242677	953.2936905790837	second
advmod_parataxis:restart	0.044825592848028915	929.7020050702926	second
parataxis_root	0.04359034032395506	2.5377329342701413	second
reparandum_advmod	0.042395817338828114	835.3624423963133	second
advmod_parataxis:discourse	0.04112721883273275	788.2089621011404	second
reparandum_parataxis	0.04112721883273275	788.2089621011404	second
punct_acl	0.040188438192249216	81.79756089838132	first
case_root	0.039176461994083936	11.178670793434415	second
parataxis_parataxis:restart	0.038464927462689126	693.9345848209144	second
parataxis:discourse_parataxis	0.038464927462689126	693.9345848209144	second
discourse:filler_obl	0.03777009901119597	670.3727759543962	second
discourse:filler_obj	0.03777009901119597	670.3727759543962	second
reparandum_reparandum	0.03634068952927306	623.2572974840232	second
discourse_conj	0.03560451757262082	599.7036269430051	second
fixed_discourse	0.03489266792523979	74.48440528972571	second
discourse:filler_acl	0.03485283496868408	576.1526682401703	second
reparandum_nsubj	0.03485283496868408	576.1526682401703	second
punct_conj	0.0343037374311866	14.76598098276567	first
nsubj_parataxis:restart	0.03408461936979407	552.604420907207	second
discourse:filler_nsubj	0.03408461936979407	552.604420907207	second
amod_nmod	0.03357833694236596	4.584717922597381	first
obl_parataxis:restart	0.03329873115421483	529.0588844759109	second
reparandum_mark	0.03249389371815959	505.51605847818576	second
punct_reparandum	0.03249389371815959	505.51605847818576	second
discourse:filler_ccomp	0.03249389371815959	505.51605847818576	second
reparandum_ccomp	0.03249389371815959	505.51605847818576	second
dislocated_root	0.032099983181928804	47.94146069256899	second
nmod_nmod	0.03179350017167992	6.360152211571991	first
reparandum_obl	0.03166866930185818	481.9759424460431	second
conj:extend_root	0.030821429049221256	458.4385359116022	second
discourse:filler_parataxis:restart	0.030821429049221256	458.4385359116022	second
punct_root	0.03071311098406396	1.8745367606973529	first
mark_reparandum	0.029950315528831664	434.90383840708984	second
reparandum_case	0.029950315528831664	434.90383840708984	second
reparandum_amod	0.029950315528831664	434.90383840708984	second
punct_parataxis:restart	0.029950315528831664	434.90383840708984	second
punct_appos	0.02980646118765951	133.54577644396244	first
discourse:filler_nmod	0.02905319526331687	411.3718494648406	second
cc_parataxis	0.02872166122883359	22.302391238742672	second
reparandum_advcl	0.028127597813434026	387.8425686172967	second
...
```
# Notes for developers

## Building and publishing
```
cd conllu-diff/conlludiff
# Bump version when done:
bumpver update --patch # or --minor or --major
python -m build
twine check dist/*
# test upload:
twine upload --verbose -r testpypi dist/*
# real upload:
twine upload --verbose dist/*
```

## Testing
```
cd conllu-diff/conlludiff/tests
pytest -vv
```