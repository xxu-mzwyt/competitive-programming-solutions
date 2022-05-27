#include <stdio.h>
#include <queue>

const int MAXN = 400;

int rslt[MAXN][MAXN];
bool vis[MAXN][MAXN];

struct step {
    int x;
    int y;
    int dep;
};
std::queue <step> q;

int dx[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int dy[8] = {1, 2, 2, 1, -1, -2, -2, -1};

int n, m;

int main() {
    int x, y;
    scanf("%d%d%d%d", &n, &m, &x, &y);
    step init;
    init.x = x - 1;
    init.y = y - 1;
    init.dep = 0;
    vis[x - 1][y - 1] = true;
    q.push(init);
    while (!q.empty()) {
        step curr = q.front();
        q.pop();
        rslt[curr.x][curr.y] = curr.dep;
        // vis[curr.x][curr.y] = true;
        // printf("current front is %d, %d; depth %d\n", curr.x, curr.y, curr.dep);
        for (int i = 0; i < 8; i++) {
            int nx = curr.x + dx[i];
            int ny = curr.y + dy[i];
            if (nx < 0 || nx >= n) continue;
            if (ny < 0 || ny >= m) continue;
            if (vis[nx][ny]) continue;
            step next;
            next.x = nx;
            next.y = ny;
            next.dep = curr.dep + 1;
            vis[nx][ny] = true;
            q.push(next);
        }
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++) {
            if (!vis[i][j]) printf("%-5d", -1);
            else printf("%-5d", rslt[i][j]);
        }
        printf("\n");
    }
}

