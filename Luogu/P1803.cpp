#include <stdio.h>
#include <algorithm>

const int MAXN = 1000001;

struct contest {
    int st;
    int et;
};

contest ctst[MAXN];

bool contest_cmp(contest a, contest b) {
    // if (a.st == b.st) return a.et <= b.et;
    // else return a.st <= b.st;
    return a.et < b.et;
}

int main() {
    
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d%d", &ctst[i].st, &ctst[i].et);
    }

    std::sort(ctst, ctst + n, contest_cmp);

    int curr_t = 0;
    int rslt = 0;
    for (int i = 0; i < n; i++) {
        // printf("curr ctst is %d \n", i);
        if (ctst[i].st < curr_t) continue;
        rslt++;
        curr_t = ctst[i].et;
    }

    printf("%d", rslt);

}
