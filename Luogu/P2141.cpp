#include <stdio.h>

const int MAXN = 100;

int a[MAXN + 1];

int main(){
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	
	int cnt = 0;
	
	for (int i = 0; i < n; i++) {
		bool done = false;
		for (int j = 0; j < n - 1; j++) {
			if (done) {
				break;
			}
			for (int k = j + 1; k < n; k++) {
				if (a[i] == a[j] + a[k]) {
					cnt++;
					done = true;
					break;
				}
			}
		}
	}
	
	printf("%d", cnt);
	return 0;
}
