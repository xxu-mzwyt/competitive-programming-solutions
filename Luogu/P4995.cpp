#include <stdio.h>

const int MAXH = 10001;
int stones[MAXH] = {0};

int main() {
    int n;
    long long rslt = 0;
    scanf("%d", &n);

    int temp;
    int min_h = 0;
    int max_h = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &temp);
        stones[temp]++;
        max_h = temp > max_h ? temp : max_h;
    }
    
    bool up = true;
    int curr = 0;
    while (n-- > 0) {

        if (up) {
            while (!stones[max_h]) max_h--;
            rslt += 1ll * (max_h - curr) * (max_h - curr);
            stones[max_h]--;
            curr = max_h;
            up = false;
        }
        else {
            while (!stones[min_h]) min_h++;
            rslt += 1ll * (curr - min_h) * (curr - min_h);
            stones[min_h]--;
            curr = min_h;
            up = true;
        }

    }
    printf("%lld", rslt);
    return 0;
}
