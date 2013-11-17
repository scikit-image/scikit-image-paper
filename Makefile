.PHONY: all view

all:
	./make_paper.sh skimage

view: all
	xdg-open output/skimage/paper.pdf

