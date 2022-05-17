#include <stdio.h>

const int MAXMN = 6;

int used[MAXMN][MAXMN];

int dir_x[4] = {0, 1, 0, -1};
int dir_y[4] = {-1, 0, 1, 0};

int paths_cnt = 0;

int n, m, t;
int sx, sy, fx, fy;


void find_paths(int x, int y);

int main() {

    scanf("%d%d%d", &n, &m, &t);
    scanf("%d%d%d%d", &sx, &sy, &fx, &fy);

    int bx, by;
    for (int i = 0; i < t; i++) {
        scanf("%d%d", &bx, &by);
        used[bx][by] = true;
    }

    find_paths(sx, sy);
    printf("%d", paths_cnt);

    return 0;

}

void find_paths(int x, int y) {
   
    // printf("now at (%d, %d)\n", x, y);

    if (x == fx && y == fy) {
        paths_cnt++;
        return;
    }

    used[x][y] = true;

    for (int i = 0; i < 4; i++) {
        
        int nx = x + dir_x[i];
        int ny = y + dir_y[i];

        if (nx > m || nx <= 0) continue;
        if (ny > n || ny <= 0) continue;

        if (used[nx][ny]) continue;

        find_paths(nx, ny);
    }

    used[x][y] = false;

}
