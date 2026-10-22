#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

// Exact cutoff search for starts whose first k restricted Syracuse iterates
// all remain at least as large as the start.

using u128 = __uint128_t;

struct Node {
    std::uint64_t residue;
    std::uint16_t weight;
    u128 endpoint;
    std::uint64_t qmax;
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
    const std::uint64_t cutoff =
        argc > 1 ? std::stoull(argv[1]) : 4294967295ULL;
    const int horizon = argc > 2 ? std::stoi(argv[2]) : 100;

    std::vector<u128> powers_three(std::max(horizon + 2, 65));
    powers_three[0] = 1;
    for (int i = 1; i < static_cast<int>(powers_three.size()); ++i) {
        powers_three[i] = 3 * powers_three[i - 1];
    }

    std::vector<Node> current{{1, 0, 1, (cutoff - 1) / 2}};
    for (int k = 0; k <= horizon; ++k) {
        std::uint64_t count = 0;
        std::uint64_t minimum = 0;
        bool explicit_all = true;
        for (auto const& node : current) {
            count += node.qmax + 1;
            explicit_all = explicit_all && (node.qmax == 0);
            if (node.residue > 1 && (minimum == 0 || node.residue < minimum)) {
                minimum = node.residue;
            }
        }
        std::cout << k << ' ' << count << ' ' << current.size();
        if (explicit_all) std::cout << " MIN " << minimum;
        std::cout << '\n';
        if (k == horizon) break;

        std::vector<Node> next;
        next.reserve(current.size() * 2);
        for (auto const& node : current) {
            if (node.weight + 1 >= 64) {
                const u128 y = 3 * node.endpoint + 1;
                const int a = valuation_two(y);
                const u128 child = y >> a;
                if (a <= 2 && child >= node.residue) {
                    next.push_back({node.residue,
                                    static_cast<std::uint16_t>(node.weight + a),
                                    child,
                                    0});
                }
                continue;
            }

            const u128 modulus = u128(1) << (node.weight + 1);
            for (int a = 1; a <= 2; ++a) {
                for (int t = 0; t < (1 << a); ++t) {
                    if (static_cast<std::uint64_t>(t) > node.qmax) continue;
                    const u128 raw_residue = u128(node.residue) + u128(t) * modulus;
                    if (raw_residue > cutoff) continue;
                    const u128 state = node.endpoint + u128(2 * t) * powers_three[k];
                    const u128 y = 3 * state + 1;
                    if (valuation_two(y) != a) continue;

                    const u128 child_endpoint = y >> a;
                    std::uint64_t child_qmax = (node.qmax - t) >> a;
                    const std::uint64_t child_residue =
                        static_cast<std::uint64_t>(raw_residue);

                    if (child_qmax == 0) {
                        if (child_endpoint < child_residue) continue;
                    } else {
                        const u128 child_modulus = modulus << a;
                        const u128 twice_three = 2 * powers_three[k + 1];
                        if (child_modulus > twice_three) {
                            if (child_endpoint < child_residue) continue;
                            const u128 cap =
                                (child_endpoint - child_residue) /
                                (child_modulus - twice_three);
                            if (cap < child_qmax) child_qmax = static_cast<std::uint64_t>(cap);
                        }
                    }

                    next.push_back({child_residue,
                                    static_cast<std::uint16_t>(node.weight + a),
                                    child_endpoint,
                                    child_qmax});
                }
            }
        }
        current.swap(next);
    }
}
