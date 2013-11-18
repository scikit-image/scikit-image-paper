scikit-image paper
==================

Getting started
---------------

1. Run ``make figures`` to generate all figures.
2. Run ``make`` to produce  ``output/skimage/paper.pdf``.

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

Other markup
------------
Please refer to this [example paper](https://github.com/scipy/scipy_proceedings/blob/master/papers/00_vanderwalt/00_vanderwalt.rst)
for examples of how to:

 - Label figures, equations and tables
 - Use math markup
 - Include code snippets

Requirements
------------
 - IEEETran (often packaged as ``texlive-publishers``, or download from `CTAN
   <http://www.ctan.org/tex-archive/macros/latex/contrib/IEEEtran/>`__) LaTeX
   class
 - AMSmath LaTeX classes (included in most LaTeX distributions)
 - `docutils` 0.8 or later (``easy_install docutils``)
 - `pygments` for code highlighting (``easy_install pygments``)
