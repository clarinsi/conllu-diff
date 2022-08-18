from conllu import parse_incr,parse
from scipy.stats import chi2_contingency
import argparse
import importlib
parser = argparse.ArgumentParser(description='')
#parser.add_argument('file1', metavar='f1', type=open, help='first conllu file')
#parser.add_argument('file2', metavar='f2', type=open, help='second conllu file')
parser.add_argument('config', metavar='c', type=str, help='configuration file')
args = parser.parse_args()
spec = importlib.util.spec_from_file_location('config',args.config)
config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config)
from collections import Counter
from math import sqrt,log

events1=[]
for tokenlist in parse_incr(open(config.file1)):
    #print(tokenlist[0]['feats'])
    for token in tokenlist:
        event=config.event_function({'token':token,'tokenlist':tokenlist})
        if event!=None:
            if not isinstance(event,list):
                events1.append(event)
            else:
                events1.extend(event)
c1=len(events1)
events1=Counter(events1)

events2=[]
for tokenlist in parse_incr(open(config.file2)):
    #print(tokenlist[0]['form'])
    for token in tokenlist:
        event=config.event_function({'token':token,'tokenlist':tokenlist})
        if event!=None:
            if not isinstance(event,list):
                events2.append(event)
            else:
                events2.extend(event)
        
c2=len(events2)
events2=Counter(events2)

def odds_ratio(f1,c1,f2,c2):
    result=((f1+0.5)/(c1-f1))/((f2+0.5)/(c2-f2))
    if result>=1.0:
        return (result,'first')
    else:
        return(((f2+0.5)/(c2-f2))/((f1+0.5)/(c1-f1)),'second')

def llr(f1,c1,f2,c2):
    f1+=0.5
    f2+=0.5
    e1=c1*(f1+f2)/(c1+c2)
    e2=c2*(f1+f2)/(c1+c2)
    try:
        return 2*((f1*log(f1/e1))+(f2*log(f2/e2)))
    except:
        return

results=[]
for event in set(events1).union(set(events2)):
    f1=events1.get(event,0)
    f2=events2.get(event,0)
    #try:
    test=chi2_contingency(((f1,c1-f1),(f2,c2-f2)))
    #except:
    #    continue
    or_result,or_direction=odds_ratio(f1,c1,f2,c2)
    results.append({'event':event,'chisq':test[0],'chisq_p':test[1],'cramers_v':sqrt(test[0]/(c1+c2)),'odds_ratio':or_result,'odds_ratio_direction':or_direction,'llr':llr(f1,c1,f2,c2),'contingency':((f1,c1-f1),(f2,c2-f2))})
# adam's wilcoxon
# difference in relative frequency
# craig's zetta (might need substructure
# multiple feature extractors? a vs b

results=config.rank_function(results)
import csv
csvfile=config.output
writer=csv.DictWriter(csvfile,config.fieldnames,delimiter='\t',extrasaction='ignore')
writer.writeheader()
for result in results:
    writer.writerow(result)
