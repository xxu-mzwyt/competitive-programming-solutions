#include <stdio.h>
#include <string.h>

const int MAXK = 100 + 1;
const int MAXM = 1000 + 1;

char vig(char m, char k) {
    if (k >= 'A' && k <= 'Z') {
        k += 'a' - 'A';
    }
    char rslt = m + k - 'a';
    if (m >= 'A' && m <= 'Z' && rslt > 'Z') {
        rslt -= 26;
    }
    else if (m >= 'a' && m <= 'z' && rslt > 'z') {
        rslt -= 26;
    }
    printf("%c %c %c\n", m, k, rslt);
    return rslt;
}

int main() {
    
    char message[MAXM];
    char key[MAXK];
    scanf("%s", key);
    scanf("%s", message);
    int keylen = strlen(key);
    int meslen = strlen(message);
    
    int curr_key = 0;
    for (int i = 0; i < meslen; i++) {
        printf("%c\n", message[i]);
        printf("%c", vig(message[i], key[curr_key]));
        curr_key++;
        if (curr_key == keylen) {
            curr_key = 0;
        }
    }
}
