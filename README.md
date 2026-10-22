# Collatz

Research notes and two self-contained write-ups on the 3x + 1 problem. Neither
claims a resolution of the Collatz conjecture; both state their limitations
explicitly.

## Contents

* **[paper/](paper/)** — *Arithmetic Clocks and Adelic Barriers in the 3x + 1
  Problem*: an audited report on stopping times, restricted valuations, moving
  primes and two-place obstructions. Readable as
  [collatz_findings.md](paper/collatz_findings.md); the LaTeX source builds the
  same text as a PDF.
* **[sparsity/](sparsity/)** — *Deterministic sparsity and symbolic rigidity of
  individual Syracuse orbits*: the subset of the above that is fully proved and
  concerns a single orbit. Shell-sparsity bound, reciprocal summability, and
  repetition/complexity constraints on the valuation word.
* **[restricted_scan.py](restricted_scan.py)** — exact search for least
  survivors in the bounded-valuation subsystem.
* **[sparsity/verify.py](sparsity/verify.py)** — numerical checks of the
  constants used in the sparsity paper.

## Build

Both document directories carry a `Makefile`; `make` produces the PDF in
`build/`. Requires a TeX distribution with `latexmk` and `biber`.
