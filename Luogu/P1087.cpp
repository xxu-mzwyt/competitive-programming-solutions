#include <cstdio>
#include <iostream>

const int MAXN = 10;
int pow_2[MAXN + 1] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};
char str[1024];

char fbi(int l, int r);
void build_fbi_tree(int l, int r);

int main() {

    int n;
    std::cin >> n;
    for (int i = 0; i < pow_2[n]; i++) {
        std::cin >> str[i];
    }
    build_fbi_tree(0, pow_2[n]);

}

char fbi(int l, int r) {
    bool zeros = true;
    bool ones = true;
    for (int i = l; i < r; i++) {
        if (zeros && str[i] == '1') zeros = false;
        if (ones && str[i] == '0') ones = false;
        if (!zeros && !ones) break;
    }
    if (zeros) return 'B';
    else if (ones) return 'I';
    else return 'F';
}

void build_fbi_tree(int l, int r) {
    // std::cout << l << ' ' << r << ' ' << fbi(l, r) << std::endl;
    if (r - l > 1) {
        build_fbi_tree(l, (l + r) / 2);
        build_fbi_tree((l + r) / 2, r);
    }
    std::cout << fbi(l, r);
}
