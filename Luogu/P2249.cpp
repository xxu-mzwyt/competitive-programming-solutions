#include <cstdio>
#include <algorithm>

const int MAXN = 1e6 + 1;

int array[MAXN];
int n, m;

int main() {
    
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    int target; 
    for (int i = 0; i < m; i++) {
        scanf("%d", &target);
        int index = std::lower_bound(array, array + n, target) - array;
        printf("%d ", array[index] == target ? index + 1 : -1);
    }

}
