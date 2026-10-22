# Paper build and computational notes

The manuscript exists in two synchronized sources:

* `collatz_findings.tex` — the **primary, typeset source** (LaTeX, `amsart`,
  with real theorem environments, automatic equation numbering and
  cross-references, `booktabs` tables and a `biblatex` bibliography).
* `collatz_findings.md` — the original Markdown draft, kept for quick reading
  and for the HTML/Office conversions.

Generated formats are placed in `build/` (LaTeX output) and `build/pandoc/`
(Pandoc output).

## Build the document

Requirements: a TeX Live installation with `latexmk`, `biber`, `newtx`,
`siunitx`, `biblatex`.  Pandoc (and optionally Chromium/LibreOffice) is only
needed for the secondary formats.

```bash
make            # -> build/collatz_findings.pdf
make watch      # continuous preview build (latexmk -pvc)
make clean      # remove LaTeX auxiliary files
```

Equivalent direct invocation:

```bash
latexmk -pdf -interaction=nonstopmode -outdir=build collatz_findings.tex
```

Note that `-outdir=build` puts `build/` on the TeX search path, so no stale
`collatz_findings.tex` may be left there; the Pandoc output therefore lives in
`build/pandoc/`.

### Secondary formats from the Markdown draft

```bash
make html       # -> build/pandoc/collatz_findings.html
make docx       # -> build/pandoc/collatz_findings.docx
```

## Editing conventions in the LaTeX source

* Results use `theorem`/`proposition`/`corollary` sharing one counter numbered
  within the section, which reproduces the numbering of the draft
  (Proposition 2.1, Theorem 3.1, Corollary 3.2, Theorem 8.1, ...).
* Only equations that are referenced carry a number; they are labelled
  `eq:<name>` and cited with `\eqref`.  Because the equation counter is section
  local, inserting a numbered equation renumbers the rest of that section
  automatically — never hard-code a number in the text.
* Sections are labelled `sec:<name>`, tables `tab:<name>`, appendices
  `app:<name>`.
* Large integers are set with `siunitx` (`\num{3184943443593}`), which applies
  the thin-space digit grouping used in the tables.

## Compile the exact-search programs

```bash
make code
```

or directly:

```bash
g++ -O3 -std=c++17 code/min_survivor.cpp -o build/min_survivor
g++ -O3 -std=c++17 code/residue_dp.cpp -o build/residue_dp
g++ -O3 -std=c++17 code/h_residue_dp.cpp -o build/h_residue_dp
```

Examples:

```bash
build/residue_dp 100000 20
build/h_residue_dp 100000 20
```

The large tables in the manuscript require substantially more memory and CPU
time.  They should be independently recomputed before publication.  The code
uses unsigned 128-bit intermediates and 64-bit starting values, so extending
the numerical range also requires a fresh overflow audit.
