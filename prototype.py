import argparse
from conllu import parse_incr
from scipy.stats import chi2_contingency

parser = argparse.ArgumentParser(description='')
parser.add_argument('file1', metavar='f1', type=open, help='first conllu file')
parser.add_argument('file2', metavar='f2', type=open, help='second conllu file')
#parser.add_argument('config', metavar='c', type=str, nargs='+', help='configuration file')
args = parser.parse_args()
from collections import Counter
from math import sqrt

event_function=lambda x:x['token']['deprel']+'_'+x['tokenlist'][x['token']['head']-1]['deprel']

events1=[]
for tokenlist in parse_incr(args.file1):
    for token in tokenlist:
        events1.append(event_function({'token':token,'tokenlist':tokenlist}))
c1=len(events1)
events1=Counter(events1)

events2=[]
for tokenlist in parse_incr(args.file2):
    for token in tokenlist:
        events2.append(event_function({'token':token,'tokenlist':tokenlist}))
c2=len(events2)
events2=Counter(events2)

def odds_ratio(f1,c1,f2,c2):
    result=((f1+0.5)/(c1-f1))/((f2+0.5)/(c2-f2))
    if result>=1.0:
        return (result,True)
    else:
        return(((f2+0.5)/(c2-f2))/((f1+0.5)/(c1-f1)),False)

results=[]
for event in set(events1).union(set(events2)):
    f1=events1.get(event,0)
    f2=events2.get(event,0)
    #print(event,f1,f2)
    try:
        test=chi2_contingency(((f1,c1-f1),(f2,c2-f2)))
    except:
        continue
    #print(test)
    if test[1]<0.05:
        results.append({'event':event,'chisq':test[0],'chisq_p':test[1],'cramers_v':sqrt(test[0]/(c1+c2)),'odds_ratio':odds_ratio(f1,c1,f2,c2)})
#print(results[:10])
results=sorted(results,key=lambda x:-x['chisq'])
for top in results[:10]:
    print(top)
