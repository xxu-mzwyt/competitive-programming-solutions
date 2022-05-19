#include <stdio.h>

const int MAXN = 25;

bool used[MAXN];
int output[MAXN];

void print_arr(int dep);

int n, r;

int main() {
    scanf("%d%d", &n, &r);
    print_arr(0);
    return 0;
}

void print_arr(int dep) {
    if (dep == r) {
        for (int i = 0; i < r; i++) {
            printf("%3d", output[i]);
        }
        printf("\n");
        return;
    }
    
    int lb = dep > 0 ? output[dep - 1] + 1 : 1;
    for (int i = lb; i <= n; i++) {
        if (!used[i]) {
            used[i] = true;
            output[dep] = i;
            print_arr(dep + 1);
            used[i] = false;
        }
    }
}
