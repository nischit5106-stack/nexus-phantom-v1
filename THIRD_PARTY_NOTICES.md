# Third-party notices

The delivered manuscript depends on external acmart 2.20; `acmart.cls` and its upstream source distribution are not bundled. Obtain the complete official package at https://www.ctan.org/pkg/acmart . ACM copyright and LPPL 1.3 attribution are retained; the license text is at https://www.latex-project.org/lppl/lppl-1-3c/ . The only included upstream template file is the unmodified `ACM-Reference-Format.bst` bibliography style, whose header expressly declares public-domain status and credits Nelson H. F. Beebe, Boris Veytsman and Gerald Murray. Its embedded notices remain intact. See [template provenance and dependency setup](papers/PHANTOM_Conference_Manuscript_FINAL_v1/TEMPLATE_PROVENANCE.md). The paper source is not an ACM publication or endorsement.

Matplotlib, NumPy, ReportLab and TeX/fonts are external build dependencies, not bundled executable libraries. Website typography uses installed system fonts; no font binaries are redistributed. Scientific diagrams are original vector encodings of the documented method or frozen aggregates. No third-party paper figures or article PDFs are included. Bibliographic facts and links are attributed in the papers and citation ledger.

The public demo carries original PHANTOM HTML/CSS/JavaScript and wholly synthetic fixtures. The author-selected NEXUS ribbon/logo assets are included for project presentation at the author’s explicit request. Phase 10 provenance records a user-selected reference and AI-assisted extraction/derivative process. No exclusive-originality, trademark-clearance or unrestricted standalone-logo reuse claim is made; reference concept boards and screenshots are excluded.

## External build tools and fonts

The [SBOM](docs/PHANTOM_PUBLIC_SBOM.csv) records observed build versions, declared TeX dependencies and conditional branches. Python/Matplotlib/NumPy/ReportLab and their dependency packages remain external; their permissive notices apply if those packages are redistributed. Optional SVG conversion uses svglib (LGPL-3.0-or-later); optional PDF inspection/rendering uses tools with their own MIT/BSD/GPL terms. These tools are not bundled. The external TeX stack includes LPPL components and the GPL-covered `comment` package; tool usage does not itself make independent manuscript output GPL. Do not copy dependency code into this package without a fresh license review.

PDF font subsets include DejaVu Sans, Linux Libertine/Biolinum, Libertinus Math, Latin Modern Math, Computer Modern/AMS, Inconsolata and Arial; Helvetica/Times appear as viewer-provided base-font references. Open-font document embedding and the inspected Arial embedding permissions are respected. No standalone font files ship. Font software remains owned/licensed by its respective authors; this package does not relicense it. See the [OFL document-use guidance](https://openfontlicense.org/ofl-faq/) and [font embedding guidance](https://learn.microsoft.com/en-us/typography/fonts/font-faq).

## Dataset and reference boundaries

Retain the Deezer dataset and accompanying-paper citations and the ListenBrainz/MetaBrainz citation and snapshot identifiers in [source reproduction](docs/SOURCE_REPRODUCTION.md). Neither source's raw records are bundled. The license of the separate Deezer PISA code repository is not a grant covering the raw dataset. Copied Deezer/ListenBrainz author-source examples retained as private audit evidence are not part of this public code release. Citation of another paper does not convey ownership of that paper or permission to redistribute its figures.

The full upstream DejaVu/Bitstream/Arev notice accompanying embedded subsets is retained in [PDF font notices](site/assets/FONT_NOTICES.txt), also present in the standalone portfolio assets.
