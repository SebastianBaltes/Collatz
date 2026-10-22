# Build targets for the Collatz manuscript.
#
#   make            LaTeX -> build/collatz_findings.pdf   (primary format)
#   make html       Pandoc -> build/pandoc/collatz_findings.html
#   make docx       Pandoc -> build/pandoc/collatz_findings.docx
#   make code       compile the exact-search programs into build/
#   make clean      remove LaTeX auxiliary files
#   make distclean  remove everything under build/

TEX      := collatz_findings.tex
MD       := collatz_findings.md
BIB      := references.bib
BUILD    := build
PANDOC   := $(BUILD)/pandoc
LATEXMK  := latexmk -pdf -interaction=nonstopmode -file-line-error -outdir=$(BUILD)
CXXFLAGS := -O3 -std=c++17

.PHONY: all pdf watch html docx code clean distclean

all: pdf

pdf: $(BUILD)/collatz_findings.pdf

$(BUILD)/collatz_findings.pdf: $(TEX) $(BIB) | $(BUILD)
	$(LATEXMK) $(TEX)

# Continuous preview build.
watch: | $(BUILD)
	$(LATEXMK) -pvc $(TEX)

html: | $(PANDOC)
	pandoc $(MD) --bibliography $(BIB) --citeproc --standalone --mathml \
	  --toc --number-sections --css paper.css \
	  --metadata title-prefix="Collatz findings" \
	  --metadata toc-title="Contents" \
	  -o $(PANDOC)/collatz_findings.html
	cp -f paper.css $(PANDOC)/

docx: | $(PANDOC)
	pandoc $(MD) --bibliography $(BIB) --citeproc --toc --number-sections \
	  -o $(PANDOC)/collatz_findings.docx

code: | $(BUILD)
	g++ $(CXXFLAGS) code/min_survivor.cpp  -o $(BUILD)/min_survivor
	g++ $(CXXFLAGS) code/residue_dp.cpp    -o $(BUILD)/residue_dp
	g++ $(CXXFLAGS) code/h_residue_dp.cpp  -o $(BUILD)/h_residue_dp

$(BUILD) $(PANDOC):
	mkdir -p $@

clean:
	latexmk -c -outdir=$(BUILD) $(TEX)

distclean:
	latexmk -C -outdir=$(BUILD) $(TEX)
	rm -rf $(PANDOC)
