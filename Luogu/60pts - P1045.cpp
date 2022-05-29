#include <stdio.h>
#include <cmath>

const int MAXD = 500;

int num[MAXD] = {1};

void mul2(int n[]);
void sub1(int n[]);

int main() {
    int p;
    scanf("%d", &p);
    printf("%d\n", (int)(log10(2) * p + 1));
    for (int i = 0; i < p; i++) {
        mul2(num);
    }
    sub1(num);
    for (int i = MAXD - 1; i >= 0; i--) {
        printf("%d", num[i]);
        if (i % 50 == 0) {
            printf("\n");
        }
    }
}

void mul2(int n[]) {
    for (int i = 0; i < MAXD; i++) {
        n[i] *= 2;
    }
    for (int i = 0; i < MAXD; i++) {
        if (i + 1 < MAXD) {
            n[i + 1] += n[i] / 10;
        }
        n[i] %= 10;
    }
}

void sub1(int n[]) {
    int curr = 0;
    while (n[curr] == 0) {
        n[curr] = 9;
        curr++;
    }
    n[curr]--;
}
