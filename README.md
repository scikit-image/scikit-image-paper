scikit-image paper
==================

Getting started
---------------

Run ``make latex`` to build the LaTeX version of the paper, found in
``latex/skimage.pdf``. All other versions are deprecated.

Other targets are ``clean`` (remove built files) and ``view`` (open PDF with
``xdg-open``).

General Guidelines
------------------
- All figures and tables should have captions.
- License conditions on images and figures must be respected (Creative Commons,
  etc.).
- Code snippets should be formatted to fit inside a single column without
  overflow.
- Avoid custom LaTeX markup where possible.

Requirements
------------
 - AMSmath LaTeX classes (included in most LaTeX distributions)
 - `docutils` 0.8 or later (``easy_install docutils``)
 - `pygments` for code highlighting (``easy_install pygments``)
 - lineno.sty -- from texlive-humanities

