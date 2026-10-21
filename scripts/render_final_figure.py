from pathlib import Path
import json,csv,os
os.environ.setdefault('MPLCONFIGDIR',str(Path.home()/'.cache/phantom-figures'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1]
aggregate=json.loads((R/'tables/final_evaluation_aggregates.json').read_text())
# Actual plotting reads only the portable aggregate.
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'pdf.fonttype':42,'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False})
f=plt.figure(figsize=(8,3.85));a=f.add_axes([.21,.32,.32,.46]);b=f.add_axes([.66,.32,.30,.46])
a.barh([1,0],[aggregate['treatment_alerts'],aggregate['control_alerts']],height=.48,color=['#285F8C','#647184'])
a.set(yticks=[1,0],yticklabels=['Treatment detections','Control alerts'],xlim=(0,475),xticks=[0,126,252,378],xlabel='World count')
for y,x in [(1,378),(0,0)]:a.text(x+10,y,f'{x}/378',va='center',fontsize=10,color='#172B42')
a.spines['left'].set_visible(False);a.tick_params(axis='y',length=0);a.grid(axis='x',alpha=.14);a.set_axisbelow(True)
x=[z['block']+1 for z in aggregate['blocks']]
b.scatter(x,[z['treatment_detection'] for z in aggregate['blocks']],s=10,color='#285F8C',label='Treatment')
b.scatter(x,[z['control_alert_rate'] for z in aggregate['blocks']],s=10,marker='x',color='#647184',label='Control')
b.set(xlim=(0,43),ylim=(-.14,1.18),xticks=[1,14,28,42],yticks=[0,.5,1],xlabel='Source group',ylabel='Alert proportion')
b.legend(loc='center right',fontsize=8,frameon=False);b.grid(alpha=.14)
f.text(.04,.94,'Prospective sealed final evaluation',fontsize=13,weight='bold',color='#172B42')
f.text(.04,.865,'4,032 listeners | 42 groups of 96 | 3,714,102 original observed events',fontsize=10,color='#526174')
f.text(.04,.14,'Mean block / pooled AUC: 1.000 / 1.000  |  Nine worlds per arm per group',fontsize=10,color='#172B42')
f.text(.04,.035,'Real observed listening histories; controlled intervention labels.\nDependent paired worlds. Zero observed control alerts is not a natural-population guarantee.',fontsize=9,color='#172B42',linespacing=1.3)
for ext in ['pdf','svg','png']:f.savefig(R/f'figures/10_prospective_final.{ext}',dpi=200,bbox_inches='tight',facecolor='white')
meta=json.loads((R/'figures/figure_manifest.json').read_text());meta=[x for x in meta if x['figure']!='10_prospective_final'];meta.append({'figure':'10_prospective_final','kind':'frozen aggregate plot','source':'tables/final_evaluation_aggregates.json','alt_text':'All 378 controlled treatments alert and no controls alert; 42 groups each have nine worlds per arm. Real histories with constructed labels.'});(R/'figures/figure_manifest.json').write_text(json.dumps(meta,indent=2))
print('Final figure generated from frozen aggregates.')
