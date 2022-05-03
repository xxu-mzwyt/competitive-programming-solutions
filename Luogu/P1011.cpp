#include <stdio.h>

const int MAXN = 30;

int a_times[MAXN] = {0, 1, 1, 2};
int k_times[MAXN] = {0, 0, 0, 0};
int fib[MAXN] = {0, 0, 0, 1};

int main() {
	int a, n, m, x;
	scanf("%d%d%d%d", &a, &n, &m, &x);
	
	for (int i = 4; i < n; i++) {
		a_times[i] = a_times[i - 1] + fib[i - 2];
		k_times[i] = k_times[i - 1] + fib[i - 1];
		fib[i] = fib[i - 1] + fib[i - 2];	
	}
	
	a_times[n] = 0;
	k_times[n] = 0;
	
	int k = (m - a_times[n - 1] * a) / k_times[n - 1];
	
//	for (int i = 1; i < n; i++) {
//		printf("%d %d \n", a_times[i], k_times[i]);
//	}

	printf("%d", a_times[x] * a + k_times[x] * k);
	
	return 0;
}

// 1 2 3   4    5     6     7     8
// a k a+k a+2k 2a+3k 3a+5k 5a+8k 8a+13k
// 0 k k   a+k  a+2k  2a+3k 3a+5k 5a+8k
// a 0 a   k    a+k   a+2k  2a+3k 3a+5k
// a a 2a  2a+k 3a+2k 4a+4k 6a+7k 9a+12k
