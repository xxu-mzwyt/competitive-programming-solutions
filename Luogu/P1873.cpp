#include <stdio.h>

const int MAXN = 1000000;
int tree_ht[MAXN];

int n, m;

bool cut_tree(int ht);

int main() {
    
    scanf("%d%d", &n, &m);

    int max_ht = -1;
    for (int i = 0; i < n; i++) {
        scanf("%d", &tree_ht[i]);
        max_ht = tree_ht[i] > max_ht ? tree_ht[i] : max_ht;
    }

    int lb = 0;
    int ub = max_ht + 1;

    while (ub - lb > 1) {
        
        int mid = (ub + lb) / 2;
            
        // printf("current range: %d - %d - %d\n", lb, mid, ub);

        if (cut_tree(mid)) {
            lb = mid;
        }
        else {
            ub = mid;
        }

    }

    printf("%d", lb);


}

bool cut_tree(int ht) {
    
    long long rslt = 0;
    for (int i = 0; i < n; i++) {
        if (tree_ht[i] > ht) {
            rslt += tree_ht[i] - ht;
        }
    }    
    // printf("%d trees cut\n", rslt);
    // printf("return value is %d\n", rslt >= m);
    // printf("m is %d\n", m);
    return rslt >= m;
}
