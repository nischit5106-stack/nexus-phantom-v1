from pathlib import Path
import json,csv,shutil,textwrap,os
os.environ.setdefault('MPLCONFIGDIR',str(Path.home()/'.cache/phantom-figures'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.font_manager import FontProperties
import numpy as np
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent
(ROOT/'qa').mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','pdf.fonttype':42})
ink='#172B42';blue='#285F8C';gray='#637080';amber='#9A5A21'
meta=[];layout_checks=[]
def save(fig,name,kind,source,alt):
 fig.canvas.draw();renderer=fig.canvas.get_renderer()
 for ax in fig.axes:
  for artist,rect in getattr(ax,'_boxed_labels',[]):
   x,y,w,h=rect;lo=ax.transData.transform((x,y));hi=ax.transData.transform((x+w,y+h))
   b=artist.get_window_extent(renderer)
   clearances=[b.x0-lo[0],hi[0]-b.x1,b.y0-lo[1],hi[1]-b.y1]
   assert min(clearances)>=3,(name,artist.get_text(),clearances)
   layout_checks.append({'figure':name,'label':artist.get_text(),'minimum_clearance_px':round(min(clearances),2),'inside_box':True})
 if name=='05_external_validation':
  label=fig.axes[0].xaxis.label.get_window_extent(renderer)
  note=fig._source_note.get_window_extent(renderer)
  assert label.y0-note.y1>=8,(name,'axis label and note overlap')
  layout_checks.append({'figure':name,'axis_note_gap_px':round(label.y0-note.y1,2)})
 if name=='06_robustness':
  ax=fig.axes[0];legend=ax.get_legend().get_window_extent(renderer).expanded(1.05,1.05)
  points=[ax.transData.transform(p) for collection in ax.collections for p in collection.get_offsets()]
  assert not any(legend.contains(*point) for point in points),'Robustness legend covers a result'
  layout_checks.append({'figure':name,'legend_covers_data':False})
 for ext in ['pdf','svg','png']:fig.savefig(ROOT/f'figures/{name}.{ext}',bbox_inches='tight',dpi=180,facecolor='white')
 plt.close(fig);meta.append(dict(figure=name,kind=kind,source=source,alt_text=alt))
def canvas(w=8,h=3):
 f,a=plt.subplots(figsize=(w,h));a.set(xlim=(0,1),ylim=(0,1));a.axis('off');return f,a
def box(a,x,y,w,h,t,color=blue):
 a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.009,rounding_size=.012',facecolor='#F3F6F8',edgecolor=color,lw=1))
 renderer=a.figure.canvas.get_renderer();font=FontProperties(family='DejaVu Sans',size=9)
 width=a.transData.transform((x+w,y))[0]-a.transData.transform((x,y))[0]-16
 lines=[]
 for paragraph in t.split('\n'):
  line=''
  for word in paragraph.split():
   trial=(line+' '+word).strip()
   if line and renderer.get_text_width_height_descent(trial,font,False)[0]>width:
    lines.append(line);line=word
   else:line=trial
  lines.append(line)
 label=a.text(x+w/2,y+h/2,'\n'.join(lines),ha='center',va='center',color=ink,fontsize=9,linespacing=1.2)
 if not hasattr(a,'_boxed_labels'):a._boxed_labels=[]
 a._boxed_labels.append((label,(x,y,w,h)))
def arrow(a,p,q):a.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',color=gray,lw=1.1))
f,a=canvas(8,3.3)
texts=['Audit events\nand source limits','Relational surprise\nconditional null','Reconstruct\nmember / target sets','Support and\ncausal alternatives','Preserve evidence\nand equal-priority sets','Human review\nexternal provenance']
for i,t in enumerate(texts):
 row=i//3;col=i%3;x=.02+col*.335;y=.57-row*.43;box(a,x,y,.29,.29,t)
 if col<2:arrow(a,(x+.30,y+.145),(x+.325,y+.145))
arrow(a,(.83,.55),(.83,.49));arrow(a,(.83,.49),(.165,.49));arrow(a,(.165,.49),(.165,.44))
a.text(.5,.015,'Structural evidence throughout; causal attribution requires additional information.',ha='center',fontsize=9,color=ink)
save(f,'01_architecture','verified conceptual diagram','Phase 7.2 operating contract; Phase 9.2; Phase 10','Six steps from audited events to review and external provenance. Enforcement is outside the system.')
f,a=canvas(8,3.1)
box(a,.01,.33,.25,.34,'One observed history\nfixed actors, rows and times')
box(a,.40,.60,.27,.27,'Treatment\nalign selected item assignments')
box(a,.40,.12,.27,.27,'Matched control\ncollision-safe reassignment')
arrow(a,(.27,.56),(.39,.73));arrow(a,(.27,.44),(.39,.25))
box(a,.76,.33,.22,.34,'Compare structure\nsynthetic labels\nshared history')
arrow(a,(.68,.73),(.75,.55));arrow(a,(.68,.25),(.75,.44))
a.text(.5,.01,'Preserve each actor\'s item multiset and timestamp multiset; check semantic duplicates.',ha='center',fontsize=9)
save(f,'02_counterfactual','verified conceptual diagram','Phase 4.8-4.12 reports','Paired interventions change cross-actor assignment while preserving declared actor marginals; pairs share histories.')
f,a=canvas(8,2.3)
box(a,.01,.35,.24,.45,'Coactivity C\nfrom unique triples\n(u, i, bin)')
box(a,.38,.35,.24,.45,'Local permutations\nmedian m\nscale 1.4826 MAD')
box(a,.75,.35,.24,.45,'Robust excess\n(C - m) / scale')
arrow(a,(.26,.57),(.37,.57));arrow(a,(.63,.57),(.74,.57))
a.text(.5,.13,'4095 draws; alert at excess >= 3. Zero-scale rule is explicit.',ha='center',color=ink)
a.text(.5,.01,'Definition schematic: no fitted density, Gaussian tail probability or invented observations.',ha='center',fontsize=8,color=gray)
save(f,'03_local_null','formula schematic','phase4_11/src/local_null.py; Phase 4.11 report','Observed coactivity is centered by its conditional permutation median and scaled by 1.4826 times MAD. Threshold three is not a probability.')
f,a=canvas(8,3)
for k,x in enumerate([.12,.43]):
 pts=[(x,.38),(x+.12,.38),(x+.06,.74)]
 for i,j in [(0,1),(0,2),(1,2)]:a.plot([pts[i][0],pts[j][0]],[pts[i][1],pts[j][1]],color=blue,lw=1.5)
 for xx,yy in pts:a.plot(xx,yy,'o',ms=12,color=blue)
 a.text(x+.06,.20,'Fixed catalog\ncomponent '+str(k+1),ha='center',fontsize=9)
a.plot([.24,.43],[.38,.38],ls='--',color=amber,lw=1.5)
box(a,.72,.30,.26,.48,'Pool all internal pairs\n511 null draws\n60/300 consensus\nfixed fragment links')
arrow(a,(.59,.52),(.71,.52))
a.text(.5,.03,'Illustration only. Shared catalog geometry does not itself establish an alert or cause.',ha='center',fontsize=9)
save(f,'04_reconstruction','illustrative graph schematic; no observed nodes','phase5_1/src/pooling.py','Two illustrative components are pooled against a fixed candidate-family null, then linked by target and period overlap. No actual user data shown.')
f=plt.figure(figsize=(8,3.75))
ax=[f.add_axes([.19,.29,.40,.52]),f.add_axes([.66,.29,.33,.54])]
f.text(.5,.94,'Controlled external-population benchmark',ha='center',fontsize=12)
ax[0].barh(['Treatment detection','Control alerts'],[378,0],color=[blue,gray],height=.5)
for i,val in enumerate([378,0]):ax[0].text(val+7,i,f'{val}/378',va='center',fontsize=10)
ax[0].set(xlim=(0,450),xlabel='Number of benchmark worlds')
ax[0].invert_yaxis();ax[0].spines['left'].set_visible(False);ax[0].grid(axis='x',alpha=.15);ax[0].set_axisbelow(True)
ax[1].axis('off');ax[1].text(.02,.95,'42 disjoint listener groups\n4,032 listeners\n378 matched pairs\n756 worlds\nAUC = 1.000\nWorst-group control alerts = 0%',va='top',linespacing=1.8,color=ink)
f._source_note=f.text(.02,.035,'Real histories with synthetic interventions and labels.\nRepeated worlds share source groups; these counts do not measure fraud accuracy.',fontsize=9,va='bottom',linespacing=1.3)
save(f,'05_external_validation','frozen aggregate data','Phase 4.12 validation/frozen_results.json; claims C06-C13','All 378 treatment worlds alerted and none of 378 controls alerted. These dependent paired worlds come from 42 listener groups, with synthetic labels.')
# Rebuild the presentation from the included frozen table transcription.
with (ROOT/'tables/robustness.csv').open() as stream:
 rows=list(csv.DictReader(stream))
for row in rows:
 for key in ('member_f1','target_f1','control_burden'):row[key]=float(row[key])
labs=['25% actor dropout','25% target dropout','25% event thinning','30-second jitter','75% observed prefix','Four disjoint campaigns','25% overlap, simultaneous','25% overlap, shifted']
f,axs=plt.subplots(1,2,figsize=(8,4.5),gridspec_kw={'width_ratios':[1,1]});y=np.arange(len(rows))
axs[0].scatter([r['member_f1'] for r in rows],y,color=blue,marker='o',label='Member F1')
axs[0].scatter([r['target_f1'] for r in rows],y,color=gray,marker='x',label='Target F1')
axs[0].set(yticks=y,yticklabels=labs,xlim=(-.03,1.05),xlabel='Reconstruction score');axs[0].invert_yaxis();axs[0].legend(loc='upper left',fontsize=8)
axs[1].barh(y,[r['control_burden'] for r in rows],color=[gray]*7+[amber],height=.5)
axs[1].set(yticks=y,yticklabels=[],xlim=(-.03,1.05),xlabel='Control-world alert proportion');axs[1].invert_yaxis()
for ax in axs:ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True)
f.text(.02,.015,'Historical development only; perturbations tested separately.\nPopularity/release shocks additionally alerted 12/12 each.',fontsize=9,va='bottom',linespacing=1.3)
f.tight_layout(rect=(0,.15,1,1))
save(f,'06_robustness','frozen report table transcription','Phase 7 frozen moderate gates; tables/robustness.csv','Reconstruction survives several separate perturbations but shifted overlap fails with F1 0.3636 and every control alerting. Shocks also fail.')
f,a=canvas(8,3.2)
box(a,.01,.61,.30,.26,'Intentional coordination\nhidden causal account A')
box(a,.01,.12,.30,.26,'Recurring external stimulus\nhidden causal account B')
box(a,.43,.34,.23,.29,'Identical visible\nevent array X')
box(a,.77,.34,.22,.29,'Same distribution\nof f(X, U)')
arrow(a,(.32,.73),(.42,.52));arrow(a,(.32,.25),(.42,.44));arrow(a,(.67,.485),(.76,.485))
a.text(.5,.02,'The distinction requires additional provenance or assumptions, not a stronger score on the same X.',ha='center',fontsize=9)
save(f,'07_causal_twins','verified conceptual diagram','Phase 7.1 identifiability report; C22','Two hidden causal stories yield identical observed events, so any event-only detector with cause-independent randomness has the same output distribution.')
f,a=canvas(8,2.7)
ts=['Support\nconditions','Complete evidence\nand alternatives','Equivalence set\nequal priority','Human review\nprovenance needed']
for i,t in enumerate(ts):
 x=.01+i*.25;box(a,x,.40,.22,.40,t)
 if i<3:arrow(a,(x+.23,.60),(x+.245,.60))
a.text(.5,.20,'SUPPORTED | SUPPORTED_WITH_CAUTION\nAMBIGUOUS_COMMON_CAUSE | OUT_OF_SUPPORT',ha='center',va='center',fontsize=8,linespacing=1.3)
a.text(.5,.02,'Support is about evidence applicability. All event-only causal attribution remains withheld.',ha='center',fontsize=9)
save(f,'08_investigation','verified conceptual diagram','Phase 7.2 contract; Phase 9.2 report','Support status and alternatives are retained in complete evidence packets and equal-priority equivalence sets for review.')
assert (ROOT/'figures/09_dashboard.png').is_file(), 'Retain the included direct browser capture; do not synthesize a scientific image.'
meta.append(dict(figure='09_dashboard',kind='public-demo screenshot; frozen synthetic evidence',source='screenshots/dashboard-academic-overview.png',alt_text='Academic Observatory with frozen synthetic hypotheses, explicit causal uncertainty and missing provenance. Screenshot is engineering illustration.'))
(ROOT/'figures/figure_manifest.json').write_text(json.dumps(meta,indent=2))
(ROOT/'qa/figure_layout_checks.json').write_text(json.dumps(layout_checks,indent=2)+'\n')
print('Created 8 vector figures and retained 1 original screenshot')
