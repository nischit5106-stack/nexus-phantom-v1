# ACM template provenance

## Included template file

The public source candidate includes only `ACM-Reference-Format.bst` from the ACM template distribution. Its unchanged header credits Nelson H. F. Beebe, Boris Veytsman and Gerald Murray and expressly identifies its license as **public domain**. The header records bibliography-style version 2.2, acmart-version 2.19, dated August 12, 2026. All embedded notices are preserved.

SHA-256 of the included bibliography style: `4342d27456645567ef1a027f6474e894715bc31d468f040142fa54540440ad04`.

`main.tex` and `references.bib` are PHANTOM manuscript sources, not an upstream template distribution. The public candidate does not distribute `acmart.cls`, `acmart.dtx`, `acmart.ins`, upstream README/sample files, or an `upstream-template/` directory. No Tectonic executable or TeX bundle is included.

## External class dependency and rebuilding

The reviewed conference PDF was built with unmodified **acmart 2.20 (2026-08-16)** and **Tectonic 0.17.0**. The original local class and bibliography style were obtained from the official TeX Live runtime package. The class is now an external build dependency; this packaging correction does not rebuild or change the reviewed PDF.

Obtain the complete official package through the [CTAN acmart page](https://www.ctan.org/pkg/acmart) or its [full distribution download](https://mirrors.ctan.org/macros/latex/contrib/acmart.zip). The [official source directory and README](https://ctan.org/tex-archive/macros/latex/contrib/acmart) link the User's Guide, whose Installation section describes installation. CTAN listed version 2.20 on 21 October 2026; check the version because the latest download can change.

Before running `python3 scripts/build_papers.py` from the repository root, obtain the complete version 2.20 distribution and its dependencies. Install/extract its unmodified class following the upstream instructions, then place `acmart.cls` beside this manuscript's `main.tex` in your local build copy so Tectonic uses it instead of an older bundled class. Retain the complete upstream distribution and notices locally. The class used for the reviewed build has SHA-256 `784c4f2fb07a70d8a797ee9d1c63f441c10fbd2f915c9c615d28cda35c0b742a`; check this identifier and the 2.20 version before rebuilding. Do not silently substitute a different version when comparing layouts. Compiler, font and dependency versions can affect PDF bytes.

## License and publication status

CTAN identifies acmart as copyright 2016–2026 Association for Computing Machinery, under LPPL 1.3; consult the [LaTeX Project Public License](https://www.latex-project.org/lppl/lppl-1-3c/) and the notices in the complete upstream distribution. The generated class header requires its original source to accompany redistribution. The public candidate therefore omits the class rather than redistributing it without that source. The bibliography style's explicit public-domain notice is retained separately. These third-party terms do not license PHANTOM code or source data.

The manuscript uses `sigconf,nonacm`, with no invented DOI, conference venue or copyright transfer. It remains an independent manuscript, without ACM acceptance or endorsement. Check the target venue's current formatting, anonymity and AI policies before any future submission.
