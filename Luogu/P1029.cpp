#include <stdio.h>


bool is_prime(int x);
int find_pq(int g, int l);


int main() {
    
    int gcd, lcm;
    scanf("%d%d", &gcd, &lcm);

    printf("%d", find_pq(gcd, lcm));

}


bool is_prime(int x) {
    for (int i = 2; i * i <= x; i++) {
        if (x % i == 0) return false;
    }
    return true;
}

int find_pq(int g, int l) {
    
    if (g > l) return 0;
    if (l % g != 0) return 0;
    if (g == l) return 1;

    int pq_cnt = 1;
    int curr = 2;
    int g_cnt, l_cnt;

    while (g != 1 || l != 1) {
        
        // printf("CURR: %d\n", curr);
        
        if (is_prime(curr)) {
            g_cnt = 0;
            l_cnt = 0;
            while (g % curr == 0) {
                g /= curr;
                g_cnt += 1;
            }        
            while (l % curr == 0) {
                l /= curr;
                l_cnt += 1;
            }
            
            // printf("factor %d: g - %d, l - %d \n", curr, g_cnt, l_cnt);

            if (g_cnt != l_cnt) {
                pq_cnt *= 2; 
            }
        }

        curr++;
 
    }

    return pq_cnt;

}
