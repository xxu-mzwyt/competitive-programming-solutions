#include <iostream>

int main() {
    
    int n;
    std::cin >> n;

    int curr_min = 1e9;
    int curr_max = 0 - 1e9;
    int max_rslt = 0 - 1e9;

    int curr;
    for (int i = 0; i < n; i++) {
        
        std::cin >> curr;

        curr_min = std::min(curr_min, curr) + 1;
        curr_max = std::max(curr_max, curr) - 1;

        max_rslt = std::max(max_rslt, std::max(curr_max - curr, curr - curr_min));

    }

    std::cout << max_rslt;

}
