"""Prepare absolute metadata locally. Does not publish or enable indexing."""
import argparse,json,re
from pathlib import Path
from urllib.parse import urlsplit
from xml.sax.saxutils import escape
p=argparse.ArgumentParser();p.add_argument('--site',type=Path,required=True);p.add_argument('--base-url',required=True);p.add_argument('--github-url');a=p.parse_args()
base=a.base_url.rstrip('/');u=urlsplit(base)
assert u.scheme=='https' and u.netloc and not u.query and not u.fragment,'Use the actual chosen HTTPS origin'
if a.github_url: assert urlsplit(a.github_url).netloc in ['github.com','www.github.com'] and urlsplit(a.github_url).scheme=='https'
for path in json.loads((a.site/'sitemap.paths.json').read_text()):
 f=a.site/path.strip('/')/'index.html' if path!='/' else a.site/'index.html';s=f.read_text()
 s=re.sub(r'<link rel="canonical"[^>]+>','',s)
 s=s.replace('</head>',f'<link rel="canonical" href="{escape(base+path)}"><meta property="og:url" content="{escape(base+path)}"></head>')
 s=s.replace('content="/assets/phantom-social-card.png"',f'content="{escape(base)}/assets/phantom-social-card.png"')
 def update(m):
  data=json.loads(m[1])
  def walk(x):
   if isinstance(x,dict):return {k:(base+v if k in ['@id','url'] and isinstance(v,str) and v.startswith('/') else walk(v)) for k,v in x.items()}
   if isinstance(x,list):return [walk(v) for v in x]
   return x
  return '<script type="application/ld+json">'+json.dumps(walk(data))+'</script>'
 s=re.sub(r'<script type="application/ld\+json">(.*?)</script>',update,s,flags=re.S)
 if a.github_url:s=s.replace('Prepared source package; not a live GitHub repository','Prepared source package; project repository linked below').replace('</footer>',f'<a href="{escape(a.github_url)}">PHANTOM on GitHub</a></footer>')
 assert 'noindex' in s;f.write_text(s)
paths=json.loads((a.site/'sitemap.paths.json').read_text());(a.site/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+escape(base+x)+'</loc></url>' for x in paths)+'</urlset>')
print('Local canonical metadata prepared. Indexing remains disabled; nothing published.')
