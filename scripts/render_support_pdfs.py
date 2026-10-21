from pathlib import Path
import re,json
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,KeepTogether,PageBreak
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
R=Path(__file__).resolve().parents[1]
styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='NBody',fontName='Helvetica',fontSize=10,leading=14,spaceAfter=8,textColor=HexColor('#172B42'),splitLongWords=1))
styles.add(ParagraphStyle(name='NTitle',fontName='Helvetica-Bold',fontSize=23,leading=27,spaceAfter=15,textColor=HexColor('#172B42')))
styles.add(ParagraphStyle(name='NHead',fontName='Helvetica-Bold',fontSize=15,leading=19,spaceBefore=15,spaceAfter=9,textColor=HexColor('#285F8C'),keepWithNext=True))
styles.add(ParagraphStyle(name='NSub',fontName='Helvetica-Bold',fontSize=11,leading=15,spaceBefore=9,spaceAfter=5,textColor=HexColor('#172B42'),keepWithNext=True))
def footer(c,d):
 c.saveState();c.setStrokeColor(HexColor('#C8D1DC'));c.line(54,44,558,44);c.setFont('Helvetica',8);c.setFillColor(HexColor('#637080'));c.drawString(54,30,'NEXUS / PHANTOM | Independent Technical Report | October 2026');c.drawRightString(558,30,str(d.page));c.restoreState()
def render(md,out,brief=False):
 content=md.read_text()
 content=re.sub(r'(?m)^(#{1,3} .+)\n(?!\n)', r'\1\n\n', content)
 story=[]
 for p in content.split('\n\n'):
  p=p.strip()
  if not p:continue
  if p.startswith('## F. Prospective final'):story.append(PageBreak())
  if p.startswith('### '):sty='NSub';p=p[4:]
  elif p.startswith('## '):sty='NHead';p=p[3:]
  elif p.startswith('# '):sty='NTitle';p=p[2:]
  else:sty='NBody'
  p=escape(p).replace('\n','<br/>')
  p=re.sub(r'([0-9a-f]{16})(?=[0-9a-f]{16})',r'\1<wbr/>',p)
  st=styles[sty]
  if brief:
   st=ParagraphStyle(name='brief'+sty,parent=st,fontSize=10.0 if sty=='NBody' else (18 if sty=='NTitle' else st.fontSize),leading=13.0 if sty=='NBody' else (22 if sty=='NTitle' else st.leading),spaceAfter=4,spaceBefore=5 if sty in ['NSub','NHead'] else 0)
  story.append(Paragraph(p,st))
 doc=SimpleDocTemplate(str(out),pagesize=letter,leftMargin=54,rightMargin=54,topMargin=47,bottomMargin=58,title=md.stem.replace('_',' ').replace('PRE FINAL','FINAL'),author='Nischit Girish Kumar',subject='FINAL v1; Controlled prospective result confirmed; Independent manuscript; not peer reviewed')
 doc.build(story,onFirstPage=footer,onLaterPages=footer)
render(R/'papers/PHANTOM_Supplementary_Appendix_FINAL_v1.md',R/'papers/PHANTOM_Supplementary_Appendix_FINAL_v1.pdf')
render(R/'papers/PHANTOM_Industry_Research_Brief_FINAL_v1.md',R/'papers/PHANTOM_Industry_Research_Brief_FINAL_v1.pdf',True)
print('Supplement and industry brief rendered')
