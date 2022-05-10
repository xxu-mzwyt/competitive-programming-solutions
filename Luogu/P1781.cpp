#include <stdio.h>
#include <string.h>

const int MAXL = 101;

char max[MAXL];
char curr[MAXL];

bool str_gt(char* a, char* b);

int main() {
    
    int n;
    int max_index = 1;

    scanf("%d", &n);
    scanf("%s", max);

    for (int i = 2; i <= n; i++) {
        scanf("%s", curr);
        if (str_gt(curr, max)) {
            strcpy(max, curr); // max = curr
            max_index = i;
        }
    }

    printf("%d\n%s", max_index, max);

}

bool str_gt(char* a, char* b) {

    int alen = strlen(a);
    int blen = strlen(b);

    if (alen != blen) {
        return alen > blen;
    }
    
    for (int i = 0; i < alen; i++) {
        if (a[i] != b[i]) {
            return a[i] > b[i];
        }
    }

    return false; // a == b
}
