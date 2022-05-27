#include <stdio.h>
#include <queue>

const int MAXN = 200;

struct floor {
    int num;
    int dep;
};
std::queue <floor> q;

int ki[MAXN];
bool vis[MAXN];

int n, target;

int main() {
    int a, b;
    scanf("%d%d%d", &n, &a, &b);
    target = b - 1;
    
    vis[a - 1] = true;
    q.push((floor){a - 1, 0});

    for (int i = 0; i < n; i++) {
        scanf("%d", &ki[i]);
    }

    while (!q.empty()) {
        
        floor curr = q.front();
        
        if (curr.num == target) {
            printf("%d", curr.dep);
            break;
        }

        q.pop();

        for (int i = -1; i <= 1; i += 2) {
            int next_num = curr.num + (i * ki[curr.num]);
            if (next_num < 0 || next_num >= n) continue;
            if (vis[next_num]) continue;
            vis[next_num] = true;
            q.push((floor){next_num, curr.dep + 1});
        }

    }
    
    if (q.empty()) {
        printf("-1");
    }

    return 0;

}
