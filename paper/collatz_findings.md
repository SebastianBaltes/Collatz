---
title: "Arithmetic Clocks and Adelic Barriers in the 3x + 1 Problem"
subtitle: "An audited report on stopping times, restricted valuations, moving primes, and two-place obstructions"
author:
  - "Collaborative research draft"
  - "OpenAI Sol 5.6 (xhigh reasoning effort, 12 h run)"
date: "20 August 2026"
abstract: |
  We develop a collection of exact reductions and quantitative necessary
  conditions for a hypothetical counterexample to the Collatz conjecture.
  The paper is an audited research report, not a claimed resolution.  For the
  odd-only Syracuse map we prove a polynomial shell-sparsity estimate for every
  nonperiodic orbit and deduce reciprocal summability for a divergent positive
  orbit.  This yields a convergent normalized orbit, an exact recharge-clock
  representation, and a time-changed dual map.  Quantitative S-unit bounds
  force logarithmically growing prime support in every long block, while
  periodic-shadow arguments impose stammering and factor-complexity constraints
  on any rational valuation code.  We then isolate the bounded-valuation
  subsystem in which the 2-adic valuation of 3n+1 is always 1 or 2.  Its
  2-adic attractor has Fibonacci
  cylinder growth, but excluding positive integral points is already an open
  restricted Collatz problem.  Exact searches determine least survivors through
  103 restricted Syracuse steps.  Finally, a least hypothetical restricted ray
  is shown either to terminate backward at a multiple of 3, or to admit an
  aperiodic bi-infinite natural extension with summably opposite clock drifts.
  Its future and past encode the same integer by separate 2-adic and
  3-adic series.  The associated approximations lie exactly at the
  product-formula threshold, explaining why standard Roth--Ridout, Subspace,
  finite-state, and fixed-S methods do not close the argument.
keywords: [Collatz conjecture, Syracuse map, 2-adic dynamics, S-unit equations, stopping time, symbolic complexity]
---

# Introduction and status

For the classical Collatz map

$$
C(n)=
\begin{cases}
n/2,&n\equiv0\pmod 2,\\
3n+1,&n\equiv1\pmod 2,
\end{cases}
$$

the conjecture asserts that every positive integer eventually reaches $1$.
It remains open; the surrounding literature is surveyed in [@lagarias1985].  Terras proved that a density-one set has finite stopping
time [@terras1976], and Tao proved that almost every orbit, in logarithmic
density, reaches below any prescribed function tending to infinity
[@tao2022].  Computation has verified convergence for all starting values
below $2^{71}$ [@barina2025].  None of these results changes the universal
quantifier: one exceptional orbit would suffice to disprove the conjecture.

This paper records the outcome of a sustained attempt to turn the familiar
negative-drift heuristic into a deterministic proof.  The useful output is not
a proof of Collatz.  It is a set of exact propositions, several quantitative
constraints, reproducible finite computations, and a precise account of the
remaining obstruction.  Claims labeled as propositions below are proved from
the displayed identities.  Numerical tables are explicitly labeled as finite
computations.  No claim of novelty or priority is made without a separate
literature attribution; the manuscript requires independent mathematical and
computational review before any research use.

The organizing theme is an interaction among three geometries:

1. real size, which controls growth or decay of an orbit;
2. $2$-adic divisibility, which determines the valuation code;
3. $3$-adic divisibility, which determines whether inverse branches are
   integral.

Each geometry alone is flexible.  The unresolved issue is whether a single
positive ordinary integer can satisfy all three indefinitely.

# Odd-only dynamics and exact normalization

Let $\mathcal O$ be the positive odd integers and define the Syracuse map

$$
S(n)=\frac{3n+1}{2^{a(n)}},
\qquad a(n):=v_2(3n+1).
$$

For an orbit $n_{k+1}=S(n_k)$, write

$$
a_k=a(n_k),\qquad
A_k=\sum_{j=0}^{k-1}a_j,\qquad A_0=0,
$$

and put

$$
\alpha=\log_2 3,
\qquad
D_k=A_k-\alpha k,
\qquad
X_k=2^{D_k}=\frac{2^{A_k}}{3^k}.
$$

The affine recurrence can be normalized without approximation.

**Proposition 2.1 (normalized orbit identity).** Define $Y_k=X_kn_k$.
Then

$$
Y_{k+1}=Y_k+\frac{X_k}{3},
$$

and consequently

$$
Y_k=n_0+\frac13\sum_{j=0}^{k-1}X_j.
\qquad\text{(2.1)}
$$

**Proof.** Multiplying $2^{a_k}n_{k+1}=3n_k+1$ by
$X_k/3$ gives

$$
X_{k+1}n_{k+1}=X_kn_k+X_k/3.
$$

Iteration proves (2.1). $\square$

Unrolling the same recurrence gives

$$
2^{A_k}n_k
=3^kn_0+
\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}.
\qquad\text{(2.2)}
$$

Equation (2.2) simultaneously contains the real growth law and all finite
$2$-adic congruence conditions.

## The stopping-time equivalence

For $n>1$, let $\sigma(n)$ be the assertion that some iterate falls below its
starting value.

**Proposition 2.2.** The Collatz conjecture is equivalent to

$$
\forall n>1\ \exists k>0:\quad C^k(n)<n.
$$

**Proof.** Reaching $1$ implies a later value below $n$.  Conversely, assume
every $n>1$ eventually falls below itself.  Strong induction on $n$ shows that
all smaller positive integers reach $1$; after the first fall below $n$, the
induction hypothesis completes the orbit. $\square$

This reduction is classical stopping-time language [@terras1976].  Its force
and its limitation are the same: a density-one theorem does not exclude a
single exceptional starting value.

# Shell sparsity and reciprocal summability

The next estimate applies to every nonperiodic positive odd orbit, not merely
to almost every starting value.  For a tail beginning at index $s$, define

$$
V_s(X)=\#\{j\ge s:X\le n_j<2X\}.
$$

**Theorem 3.1 (uniform shell sparsity).** There is an absolute
$\eta>0$ such that, uniformly in $s$,

$$
V_s(X)\ll X^{1-\eta}.
\qquad\text{(3.1)}
$$

The elementary optimization in the proof permits

$$
\eta=0.0346155582\ldots.
$$

**Proof sketch.** Choose

$$
r=\lfloor\kappa\log X\rfloor,
\qquad \alpha<c<2,
$$

and for a start at index $i$ write

$$
B_i^{(r)}=a_i+\cdots+a_{i+r-1}.
$$

Split starts in the shell according as $B_i^{(r)}\le cr$ or
$B_i^{(r)}>cr$.

For the low-valuation part, a word of length $r$ and total weight $B$ fixes one
odd residue class modulo $2^{B+1}$.  The number of words of total weight $B$
is $\binom{B-1}{r-1}$.  If $G_1,\ldots,G_r$ are independent geometric random
variables with $\Pr(G=a)=2^{-a}$, residue counting gives

$$
V_{\mathrm{low}}(X)
\ll X\Pr(G_1+\cdots+G_r\le cr)+\binom{\lfloor cr\rfloor}{r}.
$$

Chernoff and entropy estimates give exponents

$$
I(c)=c\log\!\frac{2(c-1)}c-\log(c-1),
$$

and $cH(1/c)$, respectively.

For the high-valuation part, (2.2) together with the partial-weight bound
$A_{i,j}\le B_i^{(r)}-(r-j)$ gives

$$
n_{i+r}
\le 2X\left(\frac{3}{2^c}\right)^r
+\left(\frac32\right)^r.
$$

The endpoints are distinct because the orbit is nonperiodic.  Hence the
number of high-valuation starts is bounded by the size of this endpoint
interval.  Combining the four resulting exponents and optimizing $c,\kappa$
gives the stated value.  The optimum occurs at

$$
c_*=1.6417941207\ldots,
\qquad
\kappa_*=(c_*\log2)^{-1},
$$

where $c_*H(1/c_*)=\log3$. $\square$

**Corollary 3.2 (reciprocal summability).** If a positive odd orbit is
nonperiodic and divergent, then

$$
\sum_{k\ge0}\frac1{n_k}<\infty.
\qquad\text{(3.2)}
$$

If $n_s$ is a suffix minimum, then uniformly

$$
\sum_{k\ge s}\frac1{n_k}\ll n_s^{-\eta}.
\qquad\text{(3.3)}
$$

**Proof.** Partition the tail into dyadic shells
$[2^qn_s,2^{q+1}n_s)$.  Equation (3.1) bounds the reciprocal contribution of
the $q$th shell by

$$
O\!\left((2^qn_s)^{-\eta}\right),
$$

and the geometric sum converges. $\square$

This deterministic conclusion is stronger than the naive assertion that a
divergent orbit merely tends to infinity.

## Consequences for the clock discrepancy

From

$$
\frac{Y_{k+1}}{Y_k}=1+\frac1{3n_k}
$$

and (3.2), the normalized orbit has a finite positive limit

$$
Y_k\longrightarrow L
=n_0\prod_{j\ge0}\left(1+\frac1{3n_j}\right).
\qquad\text{(3.4)}
$$

Therefore

$$
\sum_{k\ge0}X_k=3(L-n_0)<\infty,
\qquad\text{(3.5)}
$$

so

$$
D_k\to-\infty,
\qquad
n_k\sim L,2^{-D_k}.
\qquad\text{(3.6)}
$$

Notice what (3.6) does *not* imply.  It neither forces $D_k=o(k)$ nor forces
$A_k/k\to\alpha$.  Summable abstract clocks can oscillate between linear and
sublinear negative discrepancies.  Any proof of a critical density requires
arithmetic input beyond real summability.

# Recharge clocks and a dual map

Put

$$
b_k=a_k-1,\qquad B_k=A_k-k=\sum_{j<k}b_j.
$$

For an infinite positive orbit $B_k$ is unbounded; otherwise eventually every
$a_k=1$, which would require an impossible infinite loss of the finite
quantity $v_2(n_k+1)$.  Define the recharge times

$$
t_\ell=\min\{k:B_k\ge\ell\},\qquad \ell\ge1.
$$

Layering the integer $2^{B_k}$ gives an exact identity.

**Proposition 4.1 (recharge series).** In every place where the indicated
series converges,

$$
\sum_{k\ge0}\frac{2^{A_k}}{3^{k+1}}
=1+\sum_{\ell\ge1}2^{\ell-1}
\left(\frac23\right)^{t_\ell}.
\qquad\text{(4.1)}
$$

Let

$$
\rho=\frac{\log2}{\log(3/2)}=1.709511\ldots.
$$

Then real convergence is equivalent to

$$
\sum_{\ell\ge1}
\exp\!\left[-\log(3/2)(t_\ell-\rho\ell)\right]<\infty.
\qquad\text{(4.2)}
$$

In particular $t_\ell-\rho\ell\to+\infty$, but this limit alone is not
sufficient: a logarithmic excess may still make (4.2) diverge.

The same clock produces a second odd-integer dynamics.  Set
$g_\ell=t_\ell-t_{\ell-1}$, $t_0=0$, and normalize the finite recharge
residuals so that

$$
3^{g_\ell}m_{\ell-1}+1
=2^{g_{\ell+1}+1}m_\ell,
$$

where each $m_\ell$ is positive and odd.  With
$x_\ell=3^{g_\ell}m_{\ell-1}$ this becomes

$$
x_{\ell+1}=U(x_\ell),
\qquad
U(x)=
3^{v_2(x+1)-1}\frac{x+1}{2^{v_2(x+1)}}.
\qquad\text{(4.3)}
$$

Moreover the real residual satisfies

$$
R_\ell=(n_0+1)
\prod_{j=1}^{\ell}\left(1+\frac1{x_j}\right),
$$

so convergence is equivalent to $\sum1/x_j<\infty$.

Equation (4.3) is an exact renormalization, but not a descent.  It replaces
one Collatz-type orbit with another.  Long expanding blocks are possible
because positive integers can shadow negative $2$-adic periodic points.
For example the constant exponent $3$ has the negative fixed point $-9$ and

$$
U(x)+9=\frac98(x+9)
$$

along that branch.  Arbitrarily long positive shadows are obtained by taking
$x$ sufficiently close to $-9$ modulo a large power of $2$.  This is a
concrete obstruction to every bounded-window Lyapunov function.

# Moving primes and S-unit equations

Each odd transition satisfies

$$
2^{a_j}n_{j+1}-3n_j=1.
\qquad\text{(5.1)}
$$

Suppose a nonperiodic orbit block $n_M,\ldots,n_{M+K}$ involves $s$ distinct
prime divisors in total.  The $K$ distinct pairs

$$
(x_j,y_j)=(2^{a_j}n_{j+1},n_j)
$$

solve $x-3y=1$ in an $S$-unit group.  Evertse's quantitative $S$-unit theorem
[@evertse1984], in the form quoted and sharpened in
[@beukersschlickewei1996], yields the following.

**Proposition 5.1 (moving-prime bound).** For every such block,

$$
K\le3\cdot7^{,2s+5},
$$

and hence

$$
s\ge\frac12\left(\log_7(K/3)-5\right).
\qquad\text{(5.2)}
$$

Thus, for every fixed $P$, orbit terms having a prime factor greater than $P$
occur with bounded gaps.  Inverting the prime number theorem in (5.2) gives,
uniformly in the block position,

$$
\max_{M\le j\le M+K}P^+(n_j)
\ge
\left(\frac1{2\log7}+o(1)\right)
\log K\log\log K.
\qquad\text{(5.3)}
$$

This is a genuine deterministic restriction: a divergent orbit cannot remain
inside a fixed finite prime alphabet.  It is nevertheless far from a
contradiction.  The set $S$ moves with the orbit, while known $S$-unit bounds
are exponential in its rank.  Consequently these methods naturally force
only logarithmic growth of prime support.

# Rational coding, shadows, and symbolic complexity

The parity/valuation code of an odd orbit has the $2$-adic Bernstein value

$$
\Phi(a)
=-\sum_{k\ge0}\frac{2^{A_k}}{3^{k+1}}
\quad\text{in }\mathbb Q_2.
\qquad\text{(6.1)}
$$

For an actual positive integer orbit, $\Phi(a)=n_0$.  By contrast, under the
divergence assumptions of Section 3, the same positive-term series converges
over $\mathbb R$ to $L-n_0>0$.  The real and $2$-adic limits are therefore
different, despite having the same rational partial sums.  This place change
is a recurring source of invalid arguments.

## Periodic shadows

For a finite valuation word $w=(a_0,\ldots,a_{q-1})$, put

$$
A(w)=\sum_{i<q}a_i,
$$

and let

$$
Q_w=\sum_{j=0}^{q-1}3^{q-1-j}2^{A_j}.
$$

Repeating $w$ gives the rational fixed point

$$
\xi_w=\frac{Q_w}{2^{A(w)}-3^q}.
\qquad\text{(6.2)}
$$

If an integer orbit agrees with $w^t$ for a long time, it is correspondingly
close to $\xi_w$ in $\mathbb Q_2$.  Clearing the odd denominator of $\xi_w$
shows that this closeness is limited by the ordinary height of the shadow.
More precisely, for a prefix $UV^tV'$, where $V'$ is a prefix of $V$, let
$E=A(V)$ and $E'=A(V')$.  Then

$$
(t-1)E+E'
\le
\log_2(3/2)(|U|+|V|)+O_{n_0,L}(1).
\qquad\text{(6.3)}
$$

Consequently every aperiodic positive-integer valuation word satisfies

$$
\operatorname{Dio}(a)\le\log_2 3=1.5849625\ldots,
\qquad\text{(6.4)}
$$

where $\operatorname{Dio}$ is the prefix repetition exponent used in
combinatorics on words.  Since quasi-Sturmian words have a strictly larger
Diophantine exponent [@adamczewski2010], they cannot be valuation codes of a
hypothetical divergent integer orbit.

## Factor complexity

Write $a_k=1+b_k$ and $B_m=\sum_{k<m}b_k$.  If two length-$m$ valuation
factors agree at positions $i<j$, the two starting values lie in one class
modulo $2^{W+1}$, where $W=A_{i+m}-A_i$ is the common weight of the factor;
they are distinct by aperiodicity, so $2^{W+1}\le\max(n_i,n_j)$ and the height
bound above gives

$$
A_{i+m}-A_i
\le \log_2(3/2)\,j+O_{n_0,L}(1).
$$

Since every letter is at least $1$ we have $A_{i+m}-A_i\ge m$, so pigeonholing
repeated factors proves

$$
p_a(m)
\ge
\frac{m}{\log_2(3/2)}-O_{n_0,L}(1),
\qquad\text{(6.5)}
$$

where $p_a(m)$ is factor complexity.  (The apparently stronger form with
$m+B_m=A_m$ in place of $m$ holds only when the recurring factor is the
initial one: pigeonholing controls the weight of the recurring window, not
that of the initial window.)  In particular

$$
\liminf_{m\to\infty}\frac{p_a(m)}m
\ge\frac1{\log_2(3/2)}=1.709511\ldots.
$$

Equations (6.3)--(6.5) exclude broad low-complexity families, but not arbitrary
words.  Random binary clocks have repetition exponent $1$ and exponential
factor complexity while readily satisfying real negative drift.  Rational
$2$-adic compatibility, not symbolic randomness, is the missing filter.

# The restricted valuation subsystem with valuations 1 and 2

The bounded-valuation subsystem is a useful test case because it retains the
central rationality obstruction while eliminating large local divisions.
Define

$$
f_1(x)=\frac{2x-1}{3},
\qquad
f_2(x)=\frac{4x-1}{3}.
\qquad\text{(7.1)}
$$

These are the inverse branches of the odd Syracuse map when $a=1,2$.  On
$\mathbb Z_2$ they are contractions with disjoint first cylinders, and they
generate the compact set

$$
K=\Phi(\{1,2\}^{\mathbb N}).
$$

Under the classical parity-vector conjugacy of Bernstein and Lagarias
[@bernsteinlagarias1996], the valuation letters $1,2$ expand to the binary
blocks $1,10$.  Thus $K$ corresponds exactly to the golden-mean shift: binary
sequences beginning with $1$ and avoiding $00$.

The only restricted positive predecessor of $1$ is $1$ itself.  Therefore any
$N>1$ in $K\cap\mathbb Z_{>0}$ is already a Collatz counterexample: it lies on
a nontrivial positive cycle or has an unbounded orbit.  Proving

$$
K\cap\mathbb Z_{>0}=\{1\}
\qquad\text{(7.2)}
$$

is an open restricted Collatz problem, not a routine property of a $2$-adic
fractal.

## Fibonacci sparsity

At binary depth $L$, the number of golden-mean cylinders is Fibonacci.  If

$$
C(X)=\#(K\cap[1,X]),
$$

stopping each address when its valuation sum first reaches
$\lceil\log_2X\rceil-1$ yields

$$
C(X)\le F_{\lceil\log_2X\rceil+1}
\ll X^{\log_2\varphi},
\qquad
\log_2\varphi=0.6942419\ldots.
\qquad\text{(7.3)}
$$

The exponent is sharp for pure $2$-adic cylinder counting: $K$ occupies
exactly Fibonacci-many residue classes modulo $2^L$.  The estimate proves
polynomial sparsity and density zero but cannot exclude one isolated positive
integer.

This also explains why the base-conversion viewpoint of St\'erin and Woods
[@sterinwoods2020] does not produce a finite-state proof.  Exact sections of
the conjugacy already have Fibonacci growth, and after the finite binary input
has been consumed, the carry is the unbounded Collatz iterate itself.

## Least survivors

Let

$$
E_k=\{n\in\mathcal O:
a(n),a(Sn),\ldots,a(S^{k-1}n)\in\{1,2\}\},
$$

and define

$$
M_k=\min(E_k\setminus\{1\}).
$$

The sets are nested, so $M_k$ is nondecreasing.  More importantly,

$$
M_k\to\infty
\quad\Longleftrightarrow\quad
\bigcap_k(E_k\setminus\{1\})=\varnothing.
\qquad\text{(7.4)}
$$

Hence proving even qualitative divergence of $M_k$ is exactly the restricted
problem (7.2); an exponential lower bound would be strictly stronger.

For $j\ge0$ and $r\pmod{3^j}$ define

$$
\mu_{k,j}(r)=
\min\{n\in E_k\setminus\{1\}:n\equiv r\pmod{3^j}\}.
$$

With

$$
s_a(r)\equiv(3r+1)2^{-a}\pmod{3^{j+1}},
$$

the exact min-plus recurrence is

$$
\mu_{k,j}(r)=
\min_{a=1,2}
\frac{2^a\mu_{k-1,j+1}(s_a(r))-1}{3}.
\qquad\text{(7.5)}
$$

Every iteration consumes a new ternary digit.  Thus a fixed ternary modulus is
not a closed state space.  Contractive shadows of the negative fixed point
$-1$ and the negative cycle $-5\leftrightarrow-7$ survive in every finite
quotient, preventing a congruence-only growth proof.

## Exact finite computations

Two independent exact cylinder searches produced the following least
survivors.  These are finite statements, not evidence of an asymptotic law.

| Restricted length $k$ | Exact $M_k$ |
|---:|---:|
| $60$ | $3{,}041{,}391$ |
| $61$--$76$ | $319{,}804{,}831$ |
| $77$--$79$ | $379{,}027{,}947$ |
| $80$--$81$ | $16{,}339{,}660{,}827$ |
| $82$ | $82{,}928{,}941{,}737$ |
| $83$--$87$ | $527{,}048{,}380{,}911$ |
| $88$ | $721{,}664{,}657{,}161$ |
| $89$ | $962{,}219{,}542{,}881$ |
| $90$--$92$ | $971{,}145{,}319{,}023$ |
| $93$--$94$ | $1{,}613{,}948{,}193{,}195$ |
| $95$--$102$ | $2{,}388{,}707{,}582{,}695$ |
| $103$ | $3{,}184{,}943{,}443{,}593$ |

The computation also certifies $M_{104}>2^{42}-1$.  For example,

$$
C_{82}(82{,}928{,}941{,}736)=1,
\qquad
C_{82}(82{,}928{,}941{,}737)=2,
$$

where the count includes the permanent survivor $1$.

The observed $\log M_k/k$ crosses both sides of $\log(4/3)$; no stable
exponential rate is visible in this range.

## Starts that remain above themselves

For a potential least counterexample it is natural to impose the stronger
prefix condition

$$
H_k=
\{N>1:N\in E_k\text{ and }S^j(N)\ge N\ (0\le j\le k)\},
$$

and let $h_k=\min H_k$.  Exact search gives

| Restricted length $k$ | Exact $h_k$ |
|---:|---:|
| $61$--$76$ | $319{,}804{,}831$ |
| $77$ | $12{,}418{,}828{,}455$ |
| $78$--$81$ | $16{,}339{,}660{,}827$ |
| $82$ | $138{,}936{,}284{,}607$ |
| $83$--$87$ | $527{,}048{,}380{,}911$ |
| $88$--$90$ | $1{,}021{,}326{,}591{,}007$ |
| $91$--$102$ | $2{,}388{,}707{,}582{,}695$ |

and $h_{103}>2^{42}-1$.

If $A_j=j+B_j$, the exact height condition from (2.2) is

$$
(3^j-2^{A_j})N+
\sum_{i<j}3^{j-1-i}2^{A_i}\ge0.
\qquad\text{(7.6)}
$$

In particular every such prefix obeys

$$
B_j
\le
j\log_2(3/2)+
j\log_2\left(1+\frac1{3N}\right).
\qquad\text{(7.7)}
$$

For large $N$ this is an almost-critical upper ballot condition.  It still
does not resolve the quantifier: every infinite restricted orbit has a least
attained value, whose suffix belongs to all $H_k$.  Thus $h_k\to\infty$ is
again equivalent to (7.2).

# A least ray and its natural extension

Assume that a nontrivial infinite restricted orbit exists, and let $N$ be
the least value attained by *any* such orbit.  Since

$$
S(N)=\frac{3N+1}{2^{a(N)}}\ge N,
$$

one must have $a(N)=1$.  If $N\equiv2\pmod3$, the restricted predecessor
$(2N-1)/3$ would lie on an infinite restricted orbit while being smaller
than $N$, contradicting the choice of $N$.  Therefore

$$
N\not\equiv2\pmod3.
$$

There are two cases:

1. $N\equiv3\pmod{12}$.  Then $3\mid N$ and the restricted backward tree
   terminates at $N$.
2. $N\equiv7\pmod{12}$.  Then the unique predecessor is
   $(4N-1)/3>N$, and the orbit may extend indefinitely backward.

The second case admits an exact two-sided normalization.  Suppose
$(n_i,a_i)_{i\in\mathbb Z}$ is a nonperiodic positive restricted orbit with

$$
2^{a_i}n_{i+1}=3n_i+1,
\qquad n_0=N.
$$

Set $X_0=1$ and define

$$
X_{i+1}=\frac{2^{a_i}}3X_i,
\qquad Y_i=X_in_i.
$$

Then for every $i\in\mathbb Z$,

$$
Y_{i+1}=Y_i+\frac{X_i}{3}.
\qquad\text{(8.1)}
$$

For $k>0$ put

$$
D_k^+=\sum_{i=0}^{k-1}(a_i-1)-k\log_2(3/2),
$$

and

$$
D_k^-=\sum_{i=-k}^{-1}(a_i-1)-k\log_2(3/2).
$$

Then

$$
X_k=2^{D_k^+},
\qquad
X_{-k}=2^{-D_k^-}.
$$

**Theorem 8.1 (two-sided clock summability).** For a hypothetical nonperiodic
least ray with an infinite backward extension,

$$
\sum_{k\ge0}2^{D_k^+}<\infty,
\qquad
\sum_{k\ge1}2^{-D_k^-}\le3N.
\qquad\text{(8.2)}
$$

Consequently there are finite limits

$$
0\le L_-<N<L_+<\infty
$$

such that

$$
Y_i\longrightarrow L_\pm
\quad(i\to\pm\infty),
$$

and

$$
L_+-L_-=\frac13\sum_{i\in\mathbb Z}X_i.
\qquad\text{(8.3)}
$$

**Proof.** Forward summability is (3.5).  For the negative half, telescope
(8.1):

$$
\sum_{r=1}^kX_{-r}=3(N-Y_{-k})<3N,
$$

because $Y_{-k}>0$.  Monotone convergence proves the result. $\square$

Thus the clock is summably subcritical in the forward direction and summably
supercritical in the backward direction.  An eventually periodic backward
word would force the junction value to equal its rational affine fixed point
in $\mathbb Q_3$; it is therefore negative, nonintegral, or an actual positive
cycle.  Every noncyclic bi-infinite ray must have an aperiodic backward word.

# The adelic obstruction

The natural extension represents the same integer by two local-field series.
For

$$
A_k^+=\sum_{i=0}^{k-1}a_i,
\qquad
E_m=\sum_{i=-m}^{-1}a_i,
$$

one has

$$
N=-\sum_{j\ge0}\frac{2^{A_j^+}}{3^{j+1}}
\quad\text{in }\mathbb Q_2,
\qquad\text{(9.1)}
$$

and

$$
N=\sum_{j\ge1}\frac{3^{j-1}}{2^{E_j}}
\quad\text{in }\mathbb Q_3.
\qquad\text{(9.2)}
$$

The real values of these series are not $N$.  They are respectively
$L_+-N$ after reversing the sign in (9.1), and $N-L_-$ in (9.2).  Rational
partial sums may therefore converge to unrelated limits in different
completions.

Let

$$
F_k=-\sum_{j=0}^{k-1}\frac{2^{A_j^+}}{3^{j+1}},
\qquad
G_m=\sum_{j=1}^{m}\frac{3^{j-1}}{2^{E_j}}.
$$

The orbit identities give exactly

$$
N-F_k=\frac{2^{A_k^+}n_k}{3^k},
\qquad
N-G_m=\frac{3^mn_{-m}}{2^{E_m}}.
\qquad\text{(9.3)}
$$

Therefore

$$
|N-F_k|_2=2^{-A_k^+},
\qquad
|N-G_m|_3=3^{-m},
$$

but also

$$
|N-F_k|_\infty|N-F_k|_2
=\frac{n_k}{3^k},
\qquad\text{(9.4)}
$$

and

$$
|N-G_m|_\infty|N-G_m|_3
=\frac{n_{-m}}{2^{E_m}}.
\qquad\text{(9.5)}
$$

Equations (9.4)--(9.5) identify the decisive barrier.  The endpoint integers
$n_k,n_{-m}$ exactly compensate the small local factors.  Relative to the
rational heights of $F_k,G_m$, these approximations occur only at the trivial
product-formula scale $H^{-1}$, not at $H^{-1-\varepsilon}$.  Ridout's
$p$-adic extension of Roth's theorem [@ridout1958] and standard Subspace
Theorem arguments therefore do not apply.

The $2$-adic conjugacy [@bernsteinlagarias1996] supplies a symbolic natural
extension, but it does not assert that its coordinates remain positive
ordinary integers.  Likewise, rational-cycle theory [@lagarias1990] proves
aperiodicity requirements, not nonexistence of an aperiodic positive
bi-infinite ray.

# Cycles

If $n_0,\ldots,n_{k-1}$ is an odd-only cycle, then

$$
(2^{A_k}-3^k)n_0
=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}.
\qquad\text{(10.1)}
$$

Thus a positive cycle requires $2^{A_k}>3^k$.  In the restricted
$\{1,2\}$ subsystem, if $h$ of the $k$ letters equal $2$, then $A_k=k+h$ and

$$
\log_2(3/2)
<\frac hk
\le
\log_2(3/2)+\log_2\left(1+\frac1{3m}\right),
\qquad\text{(10.2)}
$$

where $m$ is the least cycle element.  At the minimum, the outgoing exponent
is $1$ and the incoming exponent is $2$, so every nontrivial restricted cycle
minimum satisfies $m\equiv7\pmod{12}$.

Current cycle bounds are enormous [@hercher2023; @barina2025], but they do not
exclude cycles of unbounded combinatorial complexity.  Primitive-divisor
arguments applied only to $2^{A_k}-3^k$ cannot settle divisibility in (10.1):
repeating a word multiplies the numerator and denominator by the same
geometric factor.  The reduced denominator, not the raw difference, is the
essential arithmetic object.

# Why the principal approaches stop

The following table summarizes exact failure modes rather than vague warnings.

| Approach | Rigorous gain | Exact obstruction |
|---|---|---|
| Negative expected logarithmic drift | Explains empirical descent | Bits along one orbit are not independent |
| Finite residue classes | Every finite valuation word is analyzable | Every finite word is realized by a positive residue class |
| Fixed-window Lyapunov functions | Can charge one periodic shadow | Negative $2$-adic shadows produce arbitrarily long expanding blocks |
| Density and shell estimates | Exceptional sets have density zero and reciprocal sums converge | One isolated integral address may remain |
| $S$-unit equations | Prime support grows at least logarithmically | The prime set moves with the orbit |
| Periodic shadows | Exclude high repetition and low complexity | Power-poor random words satisfy all combinatorial bounds |
| Automatic/base-conversion models | Give exact finite conversion structure | The carry state is the unbounded Collatz iterate |
| Fourier estimates on endpoint residues | Prove average rarity | The relevant interval is at the critical mean-spacing scale |
| Roth--Ridout/Subspace methods | Control supercritical rational approximation | Equations (9.4)--(9.5) are exactly product-formula critical |

The repeated theme is a quantifier gap.  All finite patterns, all fixed prime
alphabets, or almost all addresses can be controlled.  The conjecture asks for
one statement about every positive integer.

# Concrete research targets

The analysis suggests several exact targets whose resolution would constitute
real progress.

1. **Restricted rationality.** Prove
   $\Phi(\{1,2\}^{\mathbb N})\cap\mathbb Z_{>0}=\{1\}$.  This settles the
   bounded-valuation subsystem but not full Collatz.

2. **Least-survivor escape.** Prove merely $M_k\to\infty$, or equivalently
   $h_k\to\infty$.  Any explicit rate is stronger.

3. **Anchored anti-clustering.** For
   $C_k(X)=\#(E_k\cap[1,X])$, prove a bound of the form

   $$
   C_k(X)\le1+C X(3/4)^k.
   $$

   This would give a logarithmic restricted exit time, but it is substantially
   stronger than (7.2).

4. **Natural-extension rigidity.** Exclude aperiodic bi-infinite positive
   integer orbits satisfying the two summability conditions (8.2).  The
   one-sided terminal case $N\equiv3\pmod{12}$ must still be handled
   separately.

5. **A supercritical adelic gain.** Find an invariant or approximation whose
   combined real/$2$-adic/$3$-adic error improves (9.4)--(9.5) by a fixed
   power of height.  Without such an $\varepsilon$-gain, current arithmetic
   geometry is at its natural boundary.

6. **Temporal tail control.** Shell sparsity controls how many small states
   occur, not how late they occur.  A nontrivial upper bound on last-exit times
   or on the rate of $\sum_{j\ge k}1/n_j$ in terms of $k$ would materially
   strengthen recharge and paradoxical-segment arguments
   [@rozierterracol2026].  No such bound is presently derived here.

# Conclusion

The Collatz conjecture is neither proved nor disproved in this work.  The main
deterministic advance is a coherent chain of necessary conditions:

$$
\begin{aligned}
\text{divergence}
&\Longrightarrow \text{shell sparsity},\\
&\Longrightarrow \text{reciprocal summability},\\
&\Longrightarrow \text{summable clock discrepancy},\\
&\Longrightarrow \text{real/2-adic incompatibility constraints},
\end{aligned}
$$

together with moving-prime and symbolic-complexity restrictions.  In the
bounded-valuation subsystem, exact Fibonacci sparsity and finite computations
still leave the denominator-one intersection (7.2) unresolved.  A least
hypothetical two-sided ray produces dual $\mathbb Q_2$ and $\mathbb Q_3$
representations, but their approximations saturate rather than beat the
product formula.

The resulting obstruction is sharper than the statement that Collatz
``behaves randomly.''  The difficult object is a positive integer whose
infinite symbolic address is simultaneously compatible with real positivity,
$2$-adic divisibility, and $3$-adic inverse integrality.  Existing methods
control any two of these features much more readily than all three.

# Appendix A. Computational recurrence {.unnumbered}

For a restricted word $w$ of depth $k$, store

$$
(r_w,A_w,n_w),
$$

where $r_w$ is the canonical starting residue modulo $2^{A_w+1}$ and
$n_w=S^k(r_w)$.  Put $M=2^{A_w+1}$.  Appending $a\in\{1,2\}$ requires the
unique lift $t_a\in\{0,\ldots,2^a-1\}$ satisfying

$$
v_2\!\left(3(n_w+2t_a3^k)+1\right)=a.
$$

The child is

$$
r_{wa}=r_w+t_aM,
$$

$$
A_{wa}=A_w+a,
$$

$$
n_{wa}=\frac{3(n_w+2t_a3^k)+1}{2^a}.
$$

In particular $r_{wa}\ge r_w$, which justifies best-first enumeration.
Once $2^{A_w+1}$ exceeds the search cutoff, every cylinder contains at most one
candidate integer and the computation becomes an explicit survivor scan.

For the strengthened sets $H_k$, a cylinder also stores the largest lift
parameter consistent with every prefix-height condition.  This permits exact
pruning without floating-point arithmetic.  All reported large computations
used unsigned 128-bit integer intermediates and were cross-checked by an
independent exhaustive implementation in overlapping ranges.

# Appendix B. Reproducibility and limitations {.unnumbered}

The accompanying source directory contains:

- `restricted_scan.py`, a dependency-free finite scanner;
- `min_survivor.cpp`, a best-first exact cylinder search for $M_k$;
- `h_residue_dp.cpp`, an exact cutoff search for $h_k$;
- `residue_dp.cpp`, an independent cylinder-count implementation.

The computations certify only the stated finite ranges.  They cannot decide
whether a survivor exists for every depth.  Compiler overflow bounds, cutoff
logic, and independent implementations should be reviewed before extending
the tables.  A formal proof assistant implementation would be preferable for
publication-grade computational certificates.

The mathematical results in this report were checked by multiple independent
derivations during the investigation, but they have not undergone external
peer review.  In particular, the optimized shell exponent, the exact
least-survivor tables, and the natural-extension packaging should be regarded
as draft results pending verification.

::: {#refs}
:::
