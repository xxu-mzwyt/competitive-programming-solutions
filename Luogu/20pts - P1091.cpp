#include <cstdio>

const int MAXN = 101;
const int INF = 1e9;

int ht[MAXN];

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &ht[i]);
    }
    int min_out = INF;
    for (int i = 0; i < n; i++) {
        int out = 0;
        
        int last = INF;
        for (int j = i; j >= 0; j--) {
            if (ht[j] >= last) {
                out++;
            }
            else {
                last = ht[j];
            }
        }
        last = INF;
        for (int j = i; j < n; j++) {
            if (ht[j] >= last) {
                out++;
            }
            else {
                last = ht[j];
            }
        }
        min_out = out < min_out ? out : min_out;
    }
    printf("%d", min_out);
}
