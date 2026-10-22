#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <queue>
#include <string>
#include <vector>

// Best-first exact search for the least positive odd start, other than 1,
// whose first k odd Syracuse valuations all lie in {1,2}.
//
// Scope: uint64_t starting values and unsigned-128-bit orbit states.  The
// published table was independently cross-checked with residue_dp.cpp.

using u128 = __uint128_t;

struct Node {
    std::uint64_t residue;
    std::uint16_t depth;
    std::uint16_t weight;
    u128 endpoint;
    bool trivial;
};

struct Greater {
    bool operator()(Node const& x, Node const& y) const {
        if (x.residue != y.residue) return x.residue > y.residue;
        return x.depth > y.depth;
    }
};

static int valuation_two(u128 x) {
    int a = 0;
    while ((x & 1) == 0) {
        ++a;
        x >>= 1;
    }
    return a;
}

int main(int argc, char** argv) {
    const int horizon = argc > 1 ? std::stoi(argv[1]) : 90;
    std::vector<u128> powers_three(65);
    powers_three[0] = 1;
    for (int i = 1; i < 65; ++i) powers_three[i] = 3 * powers_three[i - 1];

    std::priority_queue<Node, std::vector<Node>, Greater> queue;
    queue.push({1, 0, 0, 1, true});
    std::vector<std::uint64_t> minima(horizon + 1, 0);
    std::uint64_t popped = 0;
    int found = 0;

    while (!queue.empty() && found < horizon) {
        Node node = queue.top();
        queue.pop();
        ++popped;

        if (node.depth > 0 && !node.trivial && minima[node.depth] == 0) {
            minima[node.depth] = node.residue;
            ++found;
            std::cout << "M " << node.depth << ' ' << node.residue
                      << " popped=" << popped << " queue=" << queue.size() << '\n';
        }
        if (node.depth == horizon) continue;

        // Once the cylinder modulus exceeds uint64_t, it contains at most one
        // uint64_t representative and follows its literal orbit.
        if (node.weight + 1 >= 64) {
            const u128 y = 3 * node.endpoint + 1;
            const int a = valuation_two(y);
            if (a <= 2) {
                queue.push({node.residue,
                            static_cast<std::uint16_t>(node.depth + 1),
                            static_cast<std::uint16_t>(node.weight + a),
                            y >> a,
                            node.trivial && a == 2});
            }
            continue;
        }

        const u128 modulus = u128(1) << (node.weight + 1);
        for (int a = 1; a <= 2; ++a) {
            for (int t = 0; t < (1 << a); ++t) {
                const u128 lifted = u128(node.residue) + u128(t) * modulus;
                if (lifted > std::numeric_limits<std::uint64_t>::max()) continue;
                const u128 state = node.endpoint + u128(2 * t) * powers_three[node.depth];
                const u128 y = 3 * state + 1;
                if (valuation_two(y) != a) continue;
                queue.push({static_cast<std::uint64_t>(lifted),
                            static_cast<std::uint16_t>(node.depth + 1),
                            static_cast<std::uint16_t>(node.weight + a),
                            y >> a,
                            node.trivial && a == 2 && t == 0});
            }
        }
    }

    std::cout << "DONE popped=" << popped << " queue=" << queue.size()
              << " found=" << found << '\n';
    for (int k = 1; k <= horizon; ++k) {
        if (minima[k] != 0) std::cout << "ROW " << k << ' ' << minima[k] << '\n';
    }
}
