BUILDDIR = build
DOC = doc
DOCS = $(DOC).tex
SOURCES = sources.bib
codelang = python
codefile = script.py

all: pdf sources pdf2 copy view clean

pdf: $(DOCS)
	-mkdir $(BUILDDIR)
	pdflatex -output-directory=$(BUILDDIR) $(DOCS)

pdf2: $(DOCS)
	pdflatex -output-directory=$(BUILDDIR) $(DOCS)

sources:
	cp -f $(SOURCES) $(BUILDDIR)/$(SOURCES)
	cd $(BUILDDIR); bibtex $(DOC)

clean:
	rm -rf $(BUILDDIR)

copy:
	cp $(BUILDDIR)/$(DOC).pdf .

view:
	open $(DOC).pdf

code:
	@pygmentize -f latex -l $(codelang) -O linenos=1 $(codefile)

codestyle:
	pygmentize -f latex -l $(codelang) -O linenos=1,full=1 $(codefile)
