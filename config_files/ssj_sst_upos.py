file1='conllu_files/sl_ssj-ud-train.conllu'
file2='conllu_files/sl_sst-ud-train.conllu'
#event_function=lambda x:x['token']['deprel']+'_'+x['tokenlist'][x['token']['head']-1]['deprel'] if x['token']['deprel']!='root' else None
#event_function=lambda x:x['token']['form']
#event_function=lambda x:x['token']['upos']
#event_function=lambda x:x['token']['lemma']
#event_function=lambda x:x['token']['xpos']
#event_function=lambda x:x['token']['deprel']
event_function=lambda x:[e[0]+':'+e[1] for e in x['token']['feats'].items()] if x['token']['feats']!=None else None

#rank_function=lambda x:sorted(x,key=lambda x:x['llr'],reverse=True)
rank_function=lambda x:[e for e in sorted(x,key=lambda x:x['chisq'],reverse=True) if e['chisq_p']<0.05]

fieldnames=['event','cramers_v','odds_ratio','odds_ratio_direction']
import sys
output=sys.stdout