.PHONY: all view figures rstbuild latex clean viewtex

FIGS = $(wildcard skimage/fig_*.py)

all: figures rstbuild latex

rstbuild:
	./make_paper.sh skimage

clean:
	rm -rf output

figures: $(FIGS)
	mkdir -p skimage/figures
	$(foreach fig, $(FIGS), python $(fig))

view: all
	xdg-open output/skimage/paper.pdf

latex: figures rstbuild
	cd latex && \
	pdflatex skimage.tex && \
	bibtex skimage.aux && \
	python pythontex/pythontex.py skimage.tex && \
	pdflatex skimage.tex && \
	pdflatex skimage.tex

viewtex: latex
	xdg-open ./latex/skimage.pdf
