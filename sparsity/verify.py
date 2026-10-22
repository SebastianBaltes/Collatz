"""Numerical checks for "Deterministic sparsity and symbolic rigidity of
individual Syracuse orbits" (Appendix A).  Run with:  make verify
"""
from math import log, log2, comb, inf
from collections import defaultdict
import random

def v2(x): return (x & -x).bit_length() - 1
def word(n, r):
    w = []
    for _ in range(r):
        a = v2(3*n+1); w.append(a); n = (3*n+1) >> a
    return tuple(w), n

# --- Lemma 1: a word of length r, weight B, fixes ONE odd class mod 2^(B+1) ---
bad = 0; checked = 0
for r in range(1, 9):
    cls = defaultdict(set)
    for n in range(1, 1 << 14, 2):
        w, _ = word(n, r); B = sum(w)
        cls[w].add(n % (1 << (B+1)))
    for w, s in cls.items():
        checked += 1
        if len(s) != 1: bad += 1
print(f"L1 residue class: {checked} words checked, {bad} violations")

# every composition realized?
for r in range(1, 7):
    seen = set(word(n, r)[0] for n in range(1, 1 << 16, 2))
    comps = sum(comb(B-1, r-1) for B in range(r, 40))
    print(f"   r={r}: distinct words seen={len(seen)}", end="  ")
    print(f"all weights<=12 realized: {all(w in seen for w in seen if sum(w)<=12)}")
    break

# --- Lemma 2: same length-m factor at i<j  =>  n_i = n_j mod 2^(W+1) ---
bad = 0; pairs = 0
for trial in range(400):
    n0 = random.randrange(3, 10**12) | 1
    seq = [n0]; vals = []
    n = n0
    for _ in range(300):
        a = v2(3*n+1); vals.append(a); n = (3*n+1) >> a; seq.append(n)
        if n == 1: break
    m = 6
    pos = defaultdict(list)
    for i in range(len(vals)-m):
        pos[tuple(vals[i:i+m])].append(i)
    for w, ps in pos.items():
        W = sum(w)
        for x in range(len(ps)):
            for y in range(x+1, len(ps)):
                pairs += 1
                if (seq[ps[x]] - seq[ps[y]]) % (1 << (W+1)) != 0: bad += 1
print(f"L2 factor->congruence: {pairs} pairs checked, {bad} violations")

# --- Lemma 3: corrected endpoint bound, additive form ---
bad_add = 0; bad_prod = 0; tot = 0
for trial in range(3000):
    n_i = random.randrange(3, 10**15) | 1
    r = random.randrange(3, 40)
    w, n_end = word(n_i, r)
    B = sum(w)
    X = n_i / 2            # so that n_i < 2X
    c = B / r
    add  = 2*X*(3/2**c)**r + (1.5)**r
    prod = 2*X*(3/2**c)**r * (1.5)**r - 1
    tot += 1
    if n_end > add + 1e-6: bad_add += 1
    if n_end > prod + 1e-6: bad_prod += 1
print(f"L3 endpoint bound: {tot} blocks; additive-form violations={bad_add}, "
      f"product-form violations={bad_prod}")

# --- the optimisation: c*, eta, and that E4 is never binding ---
g  = lambda c: c*log(c) - (c-1)*log(c-1)
c = 1.64
for _ in range(80): c -= (g(c)-log(3))/log(c/(c-1))
kappa = 1/(c*log(2)); alpha = log2(3)
E1 = 1 - kappa*(c*log(2)-log(3)); E2 = kappa*g(c); E4 = kappa*log(1.5)
print(f"OPT c*={c:.10f} kappa*={kappa:.10f}")
print(f"    E1={E1:.10f} E2={E2:.10f} E4={E4:.10f}  eta=1-E1={1-E1:.10f}")
best = (inf, None)
for k in range(1, 400001):
    cc = 1.5849625007211562 + k*1e-6
    if cc >= 2: break
    for kk in (1/(cc*log(2)),):
        e = max(1-kk*(cc*log(2)-log(3)), kk*g(cc), kk*log(1.5),
                1-kk*(cc*log(2)-g(cc)))
        if e < best[0]: best = (e, cc)
print(f"    grid search over c (kappa=1/(c ln2)): best exponent {best[0]:.10f} at c={best[1]:.7f}")
from math import log, log2, inf
from fractions import Fraction
import random
def v2(x): return (x & -x).bit_length() - 1
alpha = log2(3)

# ---- 2D optimum with ALL FOUR exponents (previous run omitted E3) ----
g = lambda c: c*log(c) - (c-1)*log(c-1)     # = c H(1/c), entropy of words
I = lambda c: c*log(2) - g(c)               # Chernoff rate for sum of geometrics
J = lambda c: c*log(2) - log(3)             # decay rate of 3^r/2^{cr}
best = (inf, None, None)
for ci in range(1, 41500):
    c = 1.5849625007211562 + ci*1e-5
    if c >= 2: break
    for ki in range(1, 2000):
        k = ki*1e-3
        e = max(1-k*I(c), k*g(c), 1-k*J(c), k*log(1.5))
        if e < best[0]: best = (e, c, k)
print(f"2D optimum (4 exponents): exponent {best[0]:.9f} at c={best[1]:.6f}, kappa={best[2]:.6f}")
print(f"   eta = {1-best[0]:.9f}   claimed 0.034615558   |  c*=1.6417941, kappa*=0.8787308")

# ---- Proposition (height bound) tested with its actual constant ----
# W + 1 <= log2(L) + (alpha-1)(u+p)  for every repeat  w[u..u+m) == w[u+p..u+p+m)
viol = 0; tested = 0; slack = inf
for trial in range(300):
    n0 = random.randrange(3, 10**14) | 1
    n = n0; w = []; seq = [n0]; A = [0]
    while n != 1 and len(w) < 3000:
        a = v2(3*n+1); w.append(a); n = (3*n+1) >> a; seq.append(n); A.append(A[-1]+a)
    if len(w) < 40: continue
    T = len(w)
    L = max(Fraction(2**A[k]*seq[k], 3**k) for k in range(T+1))   # sup Y_k, exact
    logL = log2(L.numerator) - log2(L.denominator)
    for u in range(T):
        for p in range(1, T-u):
            m = 0
            while u+p+m < T and w[u+m] == w[u+p+m]: m += 1
            if m == 0: continue
            W = A[u+m]-A[u]
            tested += 1
            lhs = W + 1; rhs = logL + (alpha-1)*(u+p)
            slack = min(slack, rhs-lhs)
            if lhs > rhs + 1e-9: viol += 1
print(f"Proposition W+1 <= log2 L + (a-1)(u+p): {tested} repeats tested, "
      f"{viol} violations, min slack {slack:.3f}")

# ---- Theorem D: p(m) >= (m - log2 L)/log2(1.5) - 1 ----
viol = 0; tested = 0; ratios = []
for trial in range(300):
    n0 = random.randrange(3, 10**14) | 1
    n = n0; w = []; seq=[n0]; A=[0]
    while n != 1 and len(w) < 3000:
        a = v2(3*n+1); w.append(a); n=(3*n+1)>>a; seq.append(n); A.append(A[-1]+a)
    if len(w) < 60: continue
    L = max(Fraction(2**A[k]*seq[k], 3**k) for k in range(len(w)+1))
    logL = log2(L.numerator)-log2(L.denominator)
    for m in (3,4,5,6,7,8):
        p = len(set(tuple(w[i:i+m]) for i in range(len(w)-m+1)))
        bound = (m - logL)/log2(1.5) - 1
        tested += 1; ratios.append(p/m)
        if p < bound - 1e-9: viol += 1
print(f"Theorem D  p(m) >= (m-log2 L)/log2(1.5) - 1: {tested} cases, {viol} violations")
print(f"   observed p(m)/m: min {min(ratios):.2f}, median {sorted(ratios)[len(ratios)//2]:.2f}")
