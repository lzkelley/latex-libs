latex-libs
==========

Static files for latex projects, specifically style files, templates and helpful, common
definitions.


Organization
------------
-   docs/           - Documents and Documentation for packages, use subfolders for each one.
-   styles/         - Style files and general purpose definitions which can be included in other
                      latex files.  These files should be linked to:
                      '/Users/lzkelley/Library/texmf/tex/latex'
-   biblio/         - Bibliography style files.  Should be linked to:
                      '/Users/lzkelley/Library/texmf/bibtex/bst'
-   templates/      - Template files (for use with `TeXShop`).  Should be linked to:
                      '/Users/lzkelley/Library/TeXShop/Templates'

-   symlink.py      - Create symbolic links of local files into the required library directories
                      so they can be found by the latex compilers.
