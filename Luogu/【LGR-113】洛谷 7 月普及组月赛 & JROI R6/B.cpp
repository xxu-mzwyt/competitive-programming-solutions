#include <iostream>
#include <algorithm>

const int MAXN = 1e6;

int price[MAXN];

int main() {
    
    // freopen("exchange01.in", "r", stdin);
    
    int n;
    std::cin >> n;
    
    for (int i = 0; i < n; i++) {
        std::cin >> price[i];
    }

    std::sort(price, price + n);
    // std::cout << price[0] << price[1] << price[2] << std::endl;

    int w;
    std::cin >> w;

    int chosen = -1;
    for (int i = n - 1; i >= 0; i--) {
        if (price[i] <= w) {
            chosen = price[i];
            break;
        }
    }

    // std::cout << "chosen: " << chosen << std::endl;
    int rslt = 0;
    for (int i = 0; i < n; i++) {
        if (price[i] <= chosen) {
            rslt++;
            chosen -= price[i];
        }
        else {
            break;
        }
    }
    std::cout << rslt;
    

}   
