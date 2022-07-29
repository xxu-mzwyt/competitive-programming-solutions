#include <iostream>
#include <cstring>

const int P1 = 11451497;
const int P2 = 20030117;
const int P3 = 10000007;
const int P4 = 10000009;

bool bkt1[P1], bkt2[P2], bkt3[P3], bkt4[P4];

int mod(int x, int p);

inline int read() {
    int w = 1, q = 0;
    char ch = ' ';
    while (ch != '-' && (ch < '0' || ch > '9')) ch = getchar();
    if (ch == '-') w = -1, ch = getchar();
    while (ch >= '0' && ch <= '9') q = q * 10 + ch - '0', ch = getchar();
    return w * q;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int t = read();
    while (t--) {
        int n = read();
        memset(bkt1, 0, sizeof(bkt1));
		memset(bkt2, 0, sizeof(bkt2));
        for (int i = 0; i < n; i++) {
            int num = read();
            if (!bkt1[mod(num, P1)] || !bkt2[mod(num, P2)] || !bkt3[mod(num, P3)] || !bkt4[mod(num, P4)]) {
                std::cout << num << ' ';
            }
            bkt1[mod(num, P1)] = true;
            bkt2[mod(num, P2)] = true;
            bkt3[mod(num, P3)] = true;
            bkt4[mod(num, P4)] = true;
        }
        std::cout << '\n';
    }
}

int mod(int x, int p) {
    return (x % p + p) % p;
}
