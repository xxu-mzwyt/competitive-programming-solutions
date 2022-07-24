#include <iostream>
#include <cmath>

const int MAXN = 4 * 1e6;

int lst[MAXN];

int main() {
    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::cin >> lst[i];
    }

    if (n <= 5000) {
        int max_rslt = 0xc0c0c0c0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int rslt = abs(lst[i] - lst[j]) - j + i - 1;
                max_rslt = rslt > max_rslt ? rslt : max_rslt;
            }
        }
        std::cout << max_rslt;
    }
    else {
        std::cout << -1;
    }
}
