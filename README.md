scikit-image-paper
==================

Build and view the PDF-document::

    make

Generate LaTeX code for source code (Pygments required)::

    make code codefile=path-to-script.ext codelang=python > tmp

Update ``codestyle.tex`` for updated Pygments::

    make codestyle codefile=path-to-script.ext codelang=python > tmp

Copy header to ``codestyle.tex``.
