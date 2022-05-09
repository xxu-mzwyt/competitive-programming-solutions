#include <stdio.h>
#include <string.h>

const int MAXN = 20;
const int MAXLEN = 100000;
const int MAXUSE = 2;

char words[MAXN][MAXLEN];
int used[MAXN];

int curr_len = 0;
int max_len = -1;
int n;

int debug[MAXN];
int debugindex = 0;


void connect(int c);
int overlap(int a, int b);

int main() {
    
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        scanf("%s", words[i]);
    }
    
    char start;
    scanf("\n%c", &start);
    
    for (int i = 0; i < n; i++) {
        
        if (words[i][0] == start) {
            curr_len = strlen(words[i]);
            max_len = curr_len > max_len ? curr_len : max_len;
            used[i]++;
            connect(i);
            curr_len = 0;
            used[i]--;
        }

    }
    
    printf("%d", max_len);

}


void connect(int c) {

    // debug[debugindex++] = c;
    
    for (int i = 0; i < n; i++) {
        if (used[i] < MAXUSE) {
            int overlap_len = overlap(c, i);
            if (overlap_len > 0) {
                used[i]++;
                curr_len += strlen(words[i]) - overlap_len;
                
                // if (curr_len > max_len) {
                //     for (int d = 0; d < debugindex; d++)
                //         printf("%d ", debug[d]);
                //     printf("%d\n", i);
                // }
                
                max_len = curr_len > max_len ? curr_len : max_len;
                connect(i);
                used[i]--;
                curr_len -= strlen(words[i]) - overlap_len;
            }    
        }
    }

    // debugindex--;

}

int overlap(int a, int b) {
    for (int i = strlen(words[a]) - 1; i > 0; i--) {
        if (i + strlen(words[b]) <= strlen(words[a])) {
            break;
        }
        if (words[a][i] == words[b][0]) {
            bool overlapped = true;
            for (int j = i; j < strlen(words[a]); j++) {
                if (words[a][j] != words[b][j - i]) {
                    overlapped = false;
                    break;
                }
            }
            if (overlapped) {
                return strlen(words[a]) - i;
            }
        }
    }
    return 0;
}
