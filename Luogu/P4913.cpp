#include <cstdio>

const int MAXN = 1e6 + 1;

int lc[MAXN], rc[MAXN];
int max_dep = 0;

void update_dep(int idx, int dep);

int main() {
    
    int n;
    scanf("%d", &n);
    
    for (int i = 1; i <= n; i++) {
        scanf("%d%d", &lc[i], &rc[i]);
    }
    
    update_dep(1, 1);

    printf("%d", max_dep);

}

void update_dep(int idx, int dep) {
    
    max_dep = dep > max_dep ? dep : max_dep;

    if (lc[idx]) {
        update_dep(lc[idx], dep + 1);
    }
    if (rc[idx]) {
        update_dep(rc[idx], dep + 1);
    }
    return;

}
