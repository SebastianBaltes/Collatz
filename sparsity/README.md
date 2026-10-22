# Deterministic sparsity and symbolic rigidity of individual Syracuse orbits

A standalone extraction of the results from `../paper/` that are (a) fully
proved rather than sketched, and (b) statements about **one** orbit rather
than about a set of starting values.  Nothing here claims progress on the
Collatz conjecture; §6 of the paper lists the limitations explicitly.

Contents:

* **Theorem 1.1** — an aperiodic Syracuse orbit meets `[X,2X)` at most
  `11·X^(1-η)` times, `η = 0.0346155582…`, with an absolute constant.
* **Corollary 1.2** — the reciprocal sum along any aperiodic orbit is below an
  absolute constant (< 464); hence every aperiodic orbit diverges and its
  normalization converges.
* **Theorem 1.3** — the valuation word has repetition exponent ≤ log₂3 and
  factor complexity ≥ m/log₂(3/2) − O(1); it is never quasi-Sturmian.

All four follow from one cylinder lemma plus non-collision of orbit values.

## Build

```bash
make            # -> build/syracuse_sparsity.pdf
make verify     # re-run the numerical checks of Appendix A
```

## Status

Draft.  The proofs are complete as written and every lemma has been checked
numerically (`verify.py`, summarized in Appendix A), but the paper has had no
external review, and the priority check against the (very large) 3x+1
literature is not exhaustive — see the "relation to prior work" remark.
