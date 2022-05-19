#include <stdio.h>

const int MAXI = 5001;
const int MOD = 1e9 + 7;

int sticks[MAXI];

long long choose2(int x);

int main() {
    
    int n;
    scanf("%d", &n);

    int max_len = -1;
    int temp;
    for (int i = 0; i < n; i++) {
        scanf("%d", &temp);
        sticks[temp]++;
        max_len = temp > max_len ? temp : max_len;
    }

    long long rslt = 0;

    for (int i = 0; i <= max_len; i++) {

        if (sticks[i] < 2) continue;
        
        for (int j = 0; j * 2 < i; j++) {
            if (sticks[j] > 0 && sticks[i - j] > 0) {
                rslt += (choose2(sticks[i]) * sticks[j] * sticks[i - j]) % MOD;
                rslt %= MOD;
            }
        }

        if (i % 2 == 0 && sticks[i / 2] > 0) {
            rslt += (choose2(sticks[i]) * choose2(sticks[i / 2])) % MOD;
            rslt %= MOD;
        }

    }
    
    printf("%d", rslt);

}

long long choose2(int x) {
    return (1ll * x * (x - 1) / 2) % MOD;
}
