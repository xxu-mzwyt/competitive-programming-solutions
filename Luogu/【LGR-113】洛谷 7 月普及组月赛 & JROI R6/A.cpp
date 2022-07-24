#include <iostream>

int main() {

    int t;
    std::cin >> t;

    while (t--) {
        long long l, r, x;
        std::cin >> l >> r >> x;
        if (r / x == l / x) {
            std::cout << l / x << std::endl;
        }
        else {
            std::cout << 1 << std::endl;
        }
    }

}
