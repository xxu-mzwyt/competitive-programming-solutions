#include <stdio.h>
#include <string.h>

const int MAXN = 100;
const int TARGET_LEN = 7;

char mat[MAXN][MAXN];
char rslt[MAXN][MAXN];

char target[TARGET_LEN + 1] = "yizhong";

void detect(int x, int y);
bool detect_word(int x, int y, int dir_x, int dir_y, int dep);

int n;

int main() {
    
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%c", &mat[i][j]);
            while (mat[i][j] < 'a' || mat[i][j] > 'z') {
                scanf("%c", &mat[i][j]);
            }
            rslt[i][j] = '*';
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] == target[0]) {
                detect(i, j);
            }    
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%c", rslt[i][j]);
        }
        printf("\n");
    }
}

void detect(int x, int y) {

    for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
            detect_word(x, y, dx, dy, 0);
            // printf("start detection at %d %d, dir %d %d\n", x, y, dx, dy);
        }
    }

}

bool detect_word(int x, int y, int dir_x, int dir_y, int dep) {
    
    // printf("current depth is %d\n", dep);
    
    if (dep == TARGET_LEN) {
        return true;
    }
    else if (x < 0 || x >= n || y < 0 || y >= n) {
        return false;
    }
    else if (mat[x][y] != target[dep]) {
        return false;
    }

    bool finished = detect_word(x + dir_x, y + dir_y, dir_x, dir_y, dep + 1); 
    if (finished) {
        // printf("finished\n");
        rslt[x][y] = mat[x][y];
    }
    return finished;

}

