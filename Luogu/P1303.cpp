#include <stdio.h>
#include <string.h>

const int DIGIT = 1000;
const int MAXD = 2000 + 10;
const int MAXN = 4000 / 3 + 10; // 10^2000 * 10^2000 = 1000^1333

char num[MAXD];
int a[MAXN], b[MAXN], ans[MAXN];

int str2lst(char n[], int l[]);
void mul(int a[], int alen, int b[], int blen, int ans[]);
void print_lst(int n[], bool neg, int len);

void debug(int lena, int lenb) {
	printf("\nA:");
	for (int i = lena - 1; i >= 0; i--) {
		printf("%d ", a[i]);
	}
	printf("\nB:");
	for (int i = lenb - 1; i >= 0; i--) {
		printf("%d ", b[i]);
	}
	printf("\n\n");
}


int main() {
	
	int alen, blen;
	bool aneg, bneg;
	 
	scanf("%s", num);
	aneg = (num[0] == '-');
	alen = str2lst(num, a);
	
	scanf("%s", num);
	bneg = (num[0] == '-');
	blen = str2lst(num, b);
	
	mul(a, alen, b, blen, ans);
	
//	debug(alen, blen);
	
	print_lst(ans, aneg ^ bneg, alen + blen);
}


int str2lst(char n[], int l[]) {
	
	int digit_cnt = 1;
	int lst_index = 0;
	int curr = 0;
	
	for (int i = strlen(n) - 1; i >= 0; i--) {
		if (i == 0 && n[i] == '-') {
			break;
		}
		curr += (n[i] - '0') * digit_cnt;
		digit_cnt *= 10;
		if (digit_cnt == DIGIT) {
			l[lst_index] = curr;
			curr = 0;
			lst_index++;
			digit_cnt = 1;
		}
	}
	
	if (curr != 0) {
		l[lst_index] = curr;	
		return lst_index + 1;	
	}
	else {
		return lst_index;
	}

	
}

void mul(int a[], int alen, int b[], int blen, int ans[]) {
	
	for (int i = 0; i < alen; i++) {
		for (int j = 0; j < blen; j++) {
			ans[i + j] += a[i] * b[j];
			ans[i + j + 1] += ans[i + j] / DIGIT;
			ans[i + j] %= DIGIT;
		}
	}
	
}

void print_lst(int n[], bool neg, int len) {
	
	if (neg) printf("-");
	while (len > 1 && n[len - 1] == 0) {
		len--;
	}
	printf("%d", n[len - 1]);
	for (int i = len - 2; i >= 0; i--) {
		printf("%03d", n[i]);
	}
	
}
