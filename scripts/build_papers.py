"""Compile the included manuscript sources; never run research producers."""
from pathlib import Path
import subprocess,shutil
R=Path(__file__).resolve().parents[1]
for kind in ["Technical_Report","Conference_Manuscript"]:
 p=R/"papers"/f"PHANTOM_{kind}_FINAL_v1"
 shutil.copytree(R/"figures",p/"figures",dirs_exist_ok=True)
 shutil.copy2(R/"references/references.bib",p/"references.bib")
 subprocess.run(["tectonic","main.tex"],cwd=p,check=True)
 shutil.copy2(p/"main.pdf",R/"papers"/f"PHANTOM_{kind}_FINAL_v1.pdf")
