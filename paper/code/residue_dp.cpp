#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>

// Exact cylinder count C_k(X) for restricted valuations {1,2}.
// Once a cylinder contains only one integer <= X, that integer is followed
// literally.  This provides an implementation independent of the best-first
// search in min_survivor.cpp.

using u128 = __uint128_t;

struct Node {
    std::uint64_t residue;
    int weight;
    u128 endpoint;
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
        argc > 1 ? std::stoull(argv[1]) : 568541921ULL;
    const int horizon = argc > 2 ? std::stoi(argv[2]) : 80;

    std::vector<u128> powers_three(horizon + 1);
    powers_three[0] = 1;
    for (int j = 1; j <= horizon; ++j) powers_three[j] = 3 * powers_three[j - 1];

    std::vector<Node> current{{1, 0, 1}};
    for (int k = 0; k <= horizon; ++k) {
        std::uint64_t count = 0;
        bool explicit_all = true;
        for (auto const& node : current) {
            std::uint64_t here = 1;
            if (node.weight + 1 < 63) {
                const std::uint64_t modulus = std::uint64_t(1) << (node.weight + 1);
                here = (cutoff - node.residue) / modulus + 1;
            }
            count += here;
            explicit_all = explicit_all && (here == 1);
        }

        std::cout << k << ' ' << count << ' ' << current.size();
        if (k > 0 && explicit_all) {
            std::vector<std::uint64_t> values;
            values.reserve(current.size());
            for (auto const& node : current) values.push_back(node.residue);
            std::sort(values.begin(), values.end());
            std::uint64_t minimum = 0;
            for (auto value : values) {
                if (value > 1) {
                    minimum = value;
                    break;
                }
            }
            std::cout << " MIN " << minimum;
        }
        std::cout << '\n';
        if (k == horizon) break;

        std::vector<Node> next;
        next.reserve(current.size() * 2);
        for (auto const& node : current) {
            const bool singleton = node.weight + 1 >= 63 ||
                (std::uint64_t(1) << (node.weight + 1)) > cutoff;
            if (singleton) {
                const u128 y = 3 * node.endpoint + 1;
                const int a = valuation_two(y);
                if (a <= 2) next.push_back({node.residue, node.weight + a, y >> a});
                continue;
            }

            const std::uint64_t modulus = std::uint64_t(1) << (node.weight + 1);
            for (int a = 1; a <= 2; ++a) {
                for (int t = 0; t < (1 << a); ++t) {
                    const std::uint64_t residue = node.residue + std::uint64_t(t) * modulus;
                    if (residue > cutoff) continue;
                    const u128 state = node.endpoint + u128(2 * t) * powers_three[k];
                    const u128 y = 3 * state + 1;
                    if (valuation_two(y) == a) {
                        next.push_back({residue, node.weight + a, y >> a});
                    }
                }
            }
        }
        current.swap(next);
    }
}
