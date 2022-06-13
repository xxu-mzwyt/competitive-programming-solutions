#include <cstdio>
#include <queue>

const int MAXN = 5e3 + 1;
const int MOD = 80112002;

std::queue <int> q;

int val[MAXN];
int edges[MAXN][MAXN];
int ind[MAXN], oud[MAXN];

void input_edges(int m);

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    input_edges(m);

    // for (int i = 1; i <= n; i++) {
    //     printf("node %d, ind %d, oud %d\n", i, ind[i], oud[i]);
    // }

    for (int i = 1; i <= n; i++) {
        if (ind[i] == 0) {
            q.push(i);
            val[i] = 1;
        }
    }

    int rslt = 0;

    while (!q.empty()) {
        int curr = q.front();
        // printf("Now dealing with %d\n", curr);
        q.pop();
        if (oud[curr] == 0) {
            rslt += val[curr];
            rslt %= MOD;
        }
        else {
            for (int i = 0; i < oud[curr]; i++) {
                int next = edges[curr][i];
                // printf("next is %d\n", next);
                ind[next]--;
                val[next] += val[curr];
                val[next] %= MOD;
                if (ind[next] == 0) {
                    q.push(next);
                }
            }
        }
    }

    printf("%d", rslt);
}

void input_edges(int m) {
    int from, to;
    for (int i = 0; i < m; i++) {
        scanf("%d%d", &from, &to);
        edges[from][oud[from]] = to;
        oud[from]++; 
        ind[to]++;
    }
}
