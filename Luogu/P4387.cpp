#include <cstdio>
#include <stack>

const int MAXN = 100001;

std::stack <int> s;
int pushed[MAXN];
int popped[MAXN];

int main() {
    int q;
    scanf("%d", &q);
    while (q --> 0) {
        
        int n;
        scanf("%d", &n);

        int temp;
        bool rslt = true;
        for (int i = 0; i < n; i++) {
            scanf("%d", &temp);
            pushed[i] = temp;
        }
        for (int i = 0; i < n; i++) {
            scanf("%d", &temp);
            popped[i] = temp;
        }
        int curr_topop = 0;
        for (int i = 0; i < n; i++) {
            s.push(pushed[i]);
            while (!s.empty() && s.top() == popped[curr_topop]) {
                s.pop();
                curr_topop++;
            }
        }
        if (s.empty()) printf("Yes\n");
        else printf("No\n");
        while (!s.empty()) s.pop();
    }
}
