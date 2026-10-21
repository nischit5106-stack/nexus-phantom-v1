# Search and release configuration

Prepared association: Nischit Girish Kumar → NEXUS Research Initiative → PHANTOM. Four authored pages have unique titles/descriptions, Person and Organization relationships, a research/project page, a ScholarlyArticle paper page and a ProfilePage author page. The demo retains a separate synthetic-research description. Every meaningful image has alt text. NEXUS is explicitly an independent research identity.

The staged site uses root-relative routes and Schema.org IDs. Open Graph and social-card fields are present. No domain, DOI, university affiliation, conference acceptance, GitHub repository or author social account is invented. `release-config.json` leaves the canonical base URL and GitHub URL null. A configured canonical URL, absolute structured-data IDs, absolute social-card URL, sitemap and GitHub crosslinks can be generated with `scripts/configure_site_metadata.py` once actual destinations are chosen. That script edits local files only and retains noindex/robots restrictions.

Indexing stays disabled: all pages have noindex/nofollow and robots.txt disallows crawling. No live sitemap is advertised while the domain is unknown. `sitemap.paths.json` supplies the complete route list. Explicit author approval is required before deployment or removing the staging/noindex controls. This package does not claim that search engines have indexed the author's work.

The social card is an original vector composition incorporating the author-selected NEXUS mark; a PNG export is included for platforms that require raster Open Graph images. No live preview metadata service is contacted.
