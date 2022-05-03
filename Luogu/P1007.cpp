#include <stdio.h>

int min(int a, int b) {
	return a < b ? a : b;
}
int max(int a, int b) {
	return a > b ? a : b;
}

const int MAXN = 5010;
int arr[MAXN];

int main() {
	int l, n;
	scanf("%d%d", &l, &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	
	int min_t = 0;
	int max_t = 0;
	
	for (int i = 0; i < n; i++) {
		if (min(arr[i], l + 1 - arr[i]) > min_t) {
			min_t = min(arr[i], l + 1 - arr[i]);
		}
		if (max(arr[i], l + 1 - arr[i]) > max_t) {
			max_t = max(arr[i], l + 1 - arr[i]);
		}
	}
	
	printf("%d %d", min_t, max_t);
}
