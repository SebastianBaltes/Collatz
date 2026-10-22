#!/usr/bin/env python3
"""Exact scans of the width-two (a in {1,2}) Syracuse survivor set.

The script is deliberately evidence-only: finite scans cannot decide whether an
integer survives forever.  It reports record finite survival times and simple
word-complexity diagnostics for the corresponding valuation prefixes.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


def v2(x: int) -> int:
    return (x & -x).bit_length() - 1


@dataclass(frozen=True)
class Result:
    steps: int
    word: str
    terminal: int
    exit_valuation: int | None
    peak: int
    reached_one: bool


def restricted_prefix(n: int, cap: int) -> Result:
    assert n > 0 and n & 1
    word: list[str] = []
    peak = n
    for _ in range(cap):
        if n == 1:
            return Result(len(word), "".join(word), n, None, peak, True)
        a = v2(3 * n + 1)
        if a > 2:
            return Result(len(word), "".join(word), n, a, peak, False)
        word.append(str(a))
        n = (3 * n + 1) >> a
        peak = max(peak, n)
    return Result(len(word), "".join(word), n, None, peak, False)


def least_period(word: str) -> int:
    if not word:
        return 0
    for p in range(1, len(word) + 1):
        if all(word[i] == word[i % p] for i in range(len(word))):
            return p
    raise AssertionError("unreachable")


def longest_periodic_prefix(word: str, max_period: int) -> tuple[int, int]:
    best_len, best_period = 0, 0
    for p in range(1, min(max_period, len(word)) + 1):
        length = p
        while length < len(word) and word[length] == word[length % p]:
            length += 1
        if length > best_len:
            best_len, best_period = length, p
    return best_len, best_period


def scan(bits: int, cap: int, top: int) -> None:
    limit = 1 << bits
    records: list[tuple[int, Result]] = []
    best = -1
    histogram: dict[int, int] = {}
    for n in range(3, limit, 2):
        result = restricted_prefix(n, cap)
        histogram[result.steps] = histogram.get(result.steps, 0) + 1
        if result.steps > best:
            best = result.steps
            records.append((n, result))

    print(f"odd starts: {limit // 2 - 1}")
    print(f"maximum finite survival: {best}")
    print("record survivors:")
    for n, result in records[-top:]:
        lp_len, lp_period = longest_periodic_prefix(result.word, 32)
        print(
            f"  N={n} bits={n.bit_length()} steps={result.steps} "
            f"exit_a={result.exit_valuation} peak={result.peak} "
            f"least_period={least_period(result.word)} "
            f"best_prefix_period<=32={lp_period}:{lp_len} "
            f"word={result.word}"
        )

    survivors = sum(count for steps, count in histogram.items() if steps >= best)
    print(f"starts attaining maximum: {survivors}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, default=20)
    parser.add_argument("--cap", type=int, default=10_000)
    parser.add_argument("--top", type=int, default=12)
    args = parser.parse_args()
    scan(args.bits, args.cap, args.top)


if __name__ == "__main__":
    main()
