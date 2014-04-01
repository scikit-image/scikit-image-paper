.PHONY: all view figures

FIGS = $(wildcard skimage/fig_*.py)


all:
	./make_paper.sh skimage

clean:
	rm -rf output

figures: $(FIGS)
	mkdir -p skimage/figures
	$(foreach fig, $(FIGS), python $(fig))

view: all
	xdg-open output/skimage/paper.pdf

latex: figures
	cd latex && \
	pdflatex skimage.tex && \
	bibtex skimage.aux && \
	python pythontex/pythontex.py skimage.tex && \
	pdflatex skimage.tex && \
	pdflatex skimage.tex

viewtex: latex
	xdg-open ./latex/skimage.pdf
