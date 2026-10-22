TEX     := syracuse_sparsity.tex
BIB     := references.bib
BUILD   := build
LATEXMK := latexmk -pdf -interaction=nonstopmode -file-line-error -outdir=$(BUILD)

.PHONY: all pdf watch verify clean distclean

all: pdf
pdf: $(BUILD)/syracuse_sparsity.pdf

$(BUILD)/syracuse_sparsity.pdf: $(TEX) $(BIB) | $(BUILD)
	$(LATEXMK) $(TEX)

watch: | $(BUILD)
	$(LATEXMK) -pvc $(TEX)

# Re-run the numerical checks reported in Appendix A.
verify:
	python3 verify.py

$(BUILD):
	mkdir -p $@

clean:
	latexmk -c -outdir=$(BUILD) $(TEX)
distclean:
	latexmk -C -outdir=$(BUILD) $(TEX)
