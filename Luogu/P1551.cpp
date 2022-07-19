#include <cstdio>

const int MAXN = 5001;

int parent[MAXN];

void init(int x);
int find(int x);
void merge(int a, int b);

int main() {
    
    int n, m, p;
    scanf("%d%d%d", &n, &m, &p);
    init(n);

    int mi, mj;
    for (int i = 0; i < m; i++) {
        scanf("%d%d", &mi, &mj);
        merge(mi, mj);
    }
    
    // printf("PARENTS:\n");
    // for (int i = 0; i <= n; i++) {
    //     printf("%d ", parent[i]);
    // }
    // printf("\n");
    // for (int i = 0; i <= n; i++) {
    //     printf("%d ", find(i));
    // }
    // printf("\n");

    int pi, pj;
    for (int i = 0; i < p; i++) {
        scanf("%d%d", &pi, &pj);
        if (find(pi) == find(pj)) {
            printf("Yes\n");
        }
        else {
            printf("No\n");
        }
    }
}

void init(int x) {
    for (int i = 0; i <= x; i++) {
        parent[i] = i;
    }
}

int find(int x) {
    if (parent[x] == x) {
        return x;
    }
    else {
        return find(parent[x]);
    }
}

void merge(int a, int b) {
    if (find(a) == find(b)) {
        return;
    }
    parent[find(b)] = find(a);
}

